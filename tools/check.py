#!/usr/bin/env python3
"""Every gate the curriculum pipeline runs, in one command.

Order matters only in that the structural checks run first — a broken reference is not
worth a readability report.

  structure    every skill and prerequisite referenced actually exists
  ids          no released ID vanished without a transition
  solutions    every reference solution passes its own tests
  readability  grade3 prose clears the grade, sentence and vocabulary gates
  subresources no external URL anywhere in the content
  packages     no lesson imports something the runtimes image does not ship
  starters     no starter already passes its own tests
  predictions  every predict answer is what the shown code really prints

`solutions` is the highest-value gate here: it catches a broken exercise before a child
does.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import signal
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build import ROOT, build_course, read_yaml  # noqa: E402
from harness import _exec, evaluate  # noqa: E402
from readability import check as readability_check  # noqa: E402
from readability import load_allowlist  # noqa: E402

SNAPSHOT = ROOT / "released-ids.json"
ALLOWLIST = ROOT / "vocabulary" / "grade3-allowlist.txt"
EXTERNAL_URL = re.compile(r"https?://", re.IGNORECASE)


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, gate: str, detail: str) -> None:
        self.failures.append(f"[{gate}] {detail}")

    def note(self, detail: str) -> None:
        self.notes.append(detail)

    def ok(self, gate: str) -> None:
        print(f"ok    {gate}")


def collect() -> tuple[dict, dict, list[dict]]:
    manifest = read_yaml(ROOT / "manifest.yaml")
    skills = read_yaml(ROOT / "skills.yaml")
    steps: list[dict] = []
    for entry in manifest["courses"]:
        _, course_steps = build_course(ROOT / "courses" / entry["id"])
        steps.extend(course_steps)
    return manifest, skills, steps


def check_structure(skills: dict, steps: list[dict], report: Report) -> None:
    known = {s["id"] for s in skills.get("skills", [])}
    seen_steps: set[str] = set()

    for skill in skills.get("skills", []):
        for prerequisite in skill.get("prerequisites", []):
            if prerequisite not in known:
                report.fail("structure", f"skill {skill['id']} requires unknown {prerequisite}")

    for step in steps:
        if step["id"] in seen_steps:
            report.fail("structure", f"duplicate step id {step['id']}")
        seen_steps.add(step["id"])

        if not step["skills"]:
            report.fail("structure", f"step {step['id']} tags no skills")
        for ref in step["skills"]:
            if ref["id"] not in known:
                report.fail("structure", f"step {step['id']} tags unknown skill {ref['id']}")
        for prerequisite in step["prerequisites"]:
            if prerequisite not in known:
                report.fail(
                    "structure", f"step {step['id']} requires unknown skill {prerequisite}"
                )
        for skill_id in step["transferFor"]:
            if skill_id not in known:
                report.fail(
                    "structure", f"step {step['id']} is a transfer item for unknown {skill_id}"
                )

        if step["type"] in ("predict", "explain-back"):
            if not step.get("options") or not step.get("answer"):
                report.fail("structure", f"{step['type']} step {step['id']} needs options and an answer")
            elif step["answer"] not in step["options"]:
                report.fail("structure", f"step {step['id']} answer is not one of its options")
        if step["type"] == "parsons" and not step.get("lines"):
            report.fail("structure", f"parsons step {step['id']} has no lines")
        if step["type"] in ("free-code", "fill-blank") and "tests" not in step:
            report.fail("structure", f"{step['type']} step {step['id']} has no tests")

    if not report.failures:
        report.ok("structure")


def check_ids(skills: dict, steps: list[dict], report: Report) -> None:
    """IDs are a public contract: they are opaque strings in an append-only event log.

    A rename silently orphans every historical event, so removal requires an explicit
    transition rather than a quiet deletion.
    """
    if not SNAPSHOT.exists():
        report.note(
            "no released-ids.json yet — run `python tools/check.py --update-snapshot` "
            "at release time to start tracking ID stability"
        )
        return

    previous = json.loads(SNAPSHOT.read_text())
    current_skills = {s["id"] for s in skills.get("skills", [])}
    current_steps = {s["id"] for s in steps}

    transitioned: set[str] = set()
    for transition in skills.get("transitions", []):
        sources = transition["from"]
        transitioned.update([sources] if isinstance(sources, str) else sources)

    for skill_id in previous.get("skills", []):
        if skill_id not in current_skills and skill_id not in transitioned:
            report.fail(
                "ids",
                f"released skill {skill_id} disappeared with no transition in skills.yaml",
            )
    for step_id in previous.get("steps", []):
        if step_id not in current_steps:
            report.fail("ids", f"released step {step_id} disappeared")

    if not any(f.startswith("[ids]") for f in report.failures):
        report.ok("ids")


def check_solutions(steps: list[dict], report: Report) -> None:
    checked = 0
    for step in steps:
        if "tests" not in step:
            continue
        solution_path = step["_dir"] / "solution.py"
        if not solution_path.exists():
            report.fail("solutions", f"step {step['id']} has tests but no solution.py")
            continue

        result = evaluate(solution_path.read_text(), step["tests"])
        checked += 1
        if not result.passed:
            failed = [c.id for c in result.cases if not c.passed]
            detail = f"step {step['id']} solution fails {failed}"
            if result.failure_kind:
                detail += f" ({result.failure_kind})"
            for case in result.cases:
                if not case.passed and case.expected is not None:
                    detail += f"\n        expected {case.expected!r}, got {case.actual!r}"
                elif not case.passed:
                    detail += f"\n        {case.message}"
            report.fail("solutions", detail)

    if not any(f.startswith("[solutions]") for f in report.failures):
        report.ok(f"solutions ({checked} checked)")


def check_readability(steps: list[dict], report: Report) -> None:
    allowlist = load_allowlist(ALLOWLIST) if ALLOWLIST.exists() else None
    if allowlist is None:
        report.note(f"no vocabulary allowlist at {ALLOWLIST} — skipping the word check")

    for step in steps:
        for tier, text in step["prose"].items():
            if tier != "grade3":
                continue
            for problem in readability_check(text, tier, allowlist):
                report.fail("readability", f"{step['id']} ({tier}): {problem}")

    if not any(f.startswith("[readability]") for f in report.failures):
        report.ok("readability")


def check_subresources(steps: list[dict], report: Report) -> None:
    """No CDN fonts, no remote images, no iframes, no external embeds.

    Already required by the on-premise design; COEP require-corp now makes a violation
    fail *silently in the browser*, which moves this from hygiene to load-bearing.
    """
    for step in steps:
        for tier, text in step["prose"].items():
            if EXTERNAL_URL.search(text):
                report.fail(
                    "subresources",
                    f"{step['id']} ({tier}) references an external URL — everything must "
                    "ship inside the image",
                )
        if "<iframe" in "".join(step["prose"].values()).lower():
            report.fail("subresources", f"{step['id']} embeds an iframe")

    if not any(f.startswith("[subresources]") for f in report.failures):
        report.ok("subresources")


STARTER_SECONDS = 5  # the browser's wall clock; a starter slower than that times out there


class _TimedOut(Exception):
    pass


def _alarm(_signum, _frame):
    raise _TimedOut


def _with_timeout(fn, *args):
    """Runs fn under the browser's time budget. A starter that is deliberately slow (an
    uncached fib(80)) would otherwise hang CI — and it fails in the browser anyway."""
    previous = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(STARTER_SECONDS)
    try:
        return fn(*args)
    except _TimedOut:
        return None
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def check_starters(steps: list[dict], report: Report) -> None:
    """A starter that already passes its own tests hands every learner a free pass."""
    for step in steps:
        starter = step["_dir"] / "starter.py"
        if "tests" not in step or not starter.exists():
            continue
        result = _with_timeout(evaluate, starter.read_text(), step["tests"])
        # The harness catches everything, so a timeout arrives as an ordinary failure.
        if result is not None and result.passed:
            report.fail("starters", f"step {step['id']} starter already passes its own tests")

    if not any(f.startswith("[starters]") for f in report.failures):
        report.ok("starters")


def _normalise(text: str) -> str:
    """Predict options show multi-line output on one line, space-separated, and may say
    "1 then 2" for readability. "Nothing" means no output at all."""
    text = " ".join(text.replace(" then ", " ").split())
    return "" if text == "Nothing" else text


def check_predictions(steps: list[dict], report: Report) -> None:
    """A predict step's answer is graded in the browser, so a wrong key marks every
    correct learner wrong. Run the shown code and compare.

    What a run shows is its output followed, if it raised, by the exception's name — so
    an answer like "one AssertionError" is checkable. A step whose code reads input sets
    predictStdin in meta.yaml to the line the prose tells the learner to imagine typing.
    """
    checked = 0
    for step in steps:
        starter = step["_dir"] / "starter.py"
        if step["type"] != "predict" or not starter.exists():
            continue
        meta = read_yaml(step["_dir"] / "meta.yaml")
        ran = _with_timeout(_exec, starter.read_text(), meta.get("predictStdin", ""))
        if ran is None or isinstance(ran[2], _TimedOut):
            report.fail("predictions", f"step {step['id']} code did not finish in time")
            continue
        _namespace, stdout, failure = ran
        if meta.get("predictCheck") == "last-line":
            # For a question about one line, e.g. the greeting after an input() prompt.
            stdout = stdout.rstrip("\n").rsplit("\n", 1)[-1]
            if "predictStdin" in meta:
                # input() writes its prompt with no newline, so it shares the last line.
                stdout = stdout.split("? ", 1)[-1]
        shown = " ".join(stdout.split())
        if failure is not None:
            shown = f"{shown} {type(failure).__name__}".strip()
        checked += 1
        if _normalise(step["answer"]) != shown:
            report.fail(
                "predictions",
                f"step {step['id']} answer is {step['answer']!r} but the code shows {shown!r}",
            )

    if not any(f.startswith("[predictions]") for f in report.failures):
        report.ok(f"predictions ({checked} checked)")


def check_packages(manifest: dict, steps: list[dict], report: Report) -> None:
    allowed = set(manifest.get("allowedPackages", [])) | set(sys.stdlib_module_names)

    for step in steps:
        for name in ("starter.py", "solution.py"):
            path = step["_dir"] / name
            if not path.exists():
                continue
            try:
                tree = ast.parse(path.read_text())
            except SyntaxError:
                continue  # a deliberately broken starter is legitimate
            for node in ast.walk(tree):
                modules = []
                if isinstance(node, ast.Import):
                    modules = [a.name.split(".")[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    modules = [node.module.split(".")[0]]
                for module in modules:
                    if module not in allowed:
                        report.fail(
                            "packages",
                            f"{step['id']} imports {module}, which is not in "
                            "manifest.allowedPackages — vendor the wheel into the "
                            "runtimes image and list it there",
                        )

    if not any(f.startswith("[packages]") for f in report.failures):
        report.ok("packages")


def update_snapshot(manifest: dict, skills: dict, steps: list[dict]) -> None:
    SNAPSHOT.write_text(
        json.dumps(
            {
                "contentVersion": manifest["contentVersion"],
                "skills": sorted(s["id"] for s in skills.get("skills", [])),
                "steps": sorted(s["id"] for s in steps),
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {SNAPSHOT}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-snapshot",
        action="store_true",
        help="record the current IDs as released — do this as part of cutting a release",
    )
    args = parser.parse_args()

    manifest, skills, steps = collect()

    if args.update_snapshot:
        update_snapshot(manifest, skills, steps)
        return 0

    report = Report()
    check_structure(skills, steps, report)
    check_ids(skills, steps, report)
    check_solutions(steps, report)
    check_readability(steps, report)
    check_subresources(steps, report)
    check_packages(manifest, steps, report)
    check_starters(steps, report)
    check_predictions(steps, report)

    for note in report.notes:
        print(f"note  {note}")

    if report.failures:
        print(f"\n{len(report.failures)} failure(s):\n")
        for failure in report.failures:
            print(f"  {failure}")
        return 1

    print(f"\nAll gates passed — {len(steps)} steps at {manifest['contentVersion']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
