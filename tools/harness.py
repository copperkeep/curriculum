"""Runs a step's tests against a solution, the way the browser does.

This mirrors the Python harness the Pyodide adapter injects
(`packages/runtime-python/src/harness.py.ts` in the platform repo). The duplication is
deliberate and small: CI must be able to run every reference solution without a browser,
and the alternative — driving a headless browser to check curriculum — is far more
machinery for the same answer.

If the two ever disagree about what "passed" means, the browser is correct and this is
the bug.
"""

from __future__ import annotations

import io
import sys
from dataclasses import dataclass, field


@dataclass
class CaseResult:
    id: str
    passed: bool
    message: str = ""
    expected: str | None = None
    actual: str | None = None


@dataclass
class EvalResult:
    passed: bool
    failure_kind: str | None = None
    cases: list[CaseResult] = field(default_factory=list)


def _classify(exc: BaseException) -> str:
    return "parse" if isinstance(exc, SyntaxError | IndentationError) else "runtime"


def _exec(code: str, stdin_text: str = "") -> tuple[dict, str, BaseException | None]:
    namespace: dict = {"__name__": "__main__"}
    out = io.StringIO()
    saved = (sys.stdout, sys.stdin)
    sys.stdout, sys.stdin = out, io.StringIO(stdin_text)
    try:
        # dont_inherit: this module's own __future__ imports must not leak into the
        # learner's code, or annotations become strings here but not in the browser.
        exec(compile(code, "<lesson>", "exec", dont_inherit=True), namespace)  # noqa: S102
        failure = None
    except BaseException as exc:  # noqa: BLE001
        failure = exc
    finally:
        sys.stdout, sys.stdin = saved
    return namespace, out.getvalue(), failure


def _all_failed(cases: list[dict], failure: BaseException) -> EvalResult:
    """A program that never ran cleanly tells us nothing, so no case is attempted."""
    return EvalResult(
        passed=False,
        failure_kind=_classify(failure),
        cases=[CaseResult(id=c.get("id", "?"), passed=False, message=str(failure)) for c in cases],
    )


def evaluate(code: str, spec: dict) -> EvalResult:
    cases = spec.get("cases", [])

    # A case with its own stdin gets a run of its own; the shared input-less run exists
    # only for cases without stdin. Otherwise a program that calls input() fails with
    # EOFError before any case is looked at.
    shared = None
    if not cases or any(not c.get("stdin") for c in cases):
        shared = _exec(code)
        if shared[2] is not None:
            return _all_failed(cases, shared[2])

    results: list[CaseResult] = []
    run_failure: BaseException | None = None
    for case in cases:
        if case.get("stdin"):
            namespace, stdout, failure = _exec(code, case["stdin"])
            if failure is not None:
                if _classify(failure) == "parse":
                    return _all_failed(cases, failure)
                run_failure = run_failure or failure
                results.append(CaseResult(id=case["id"], passed=False, message=str(failure)))
                continue
        else:
            namespace, stdout, _ = shared
        try:
            if case.get("assert"):
                passed = bool(eval(case["assert"], dict(namespace)))  # noqa: S307
                results.append(
                    CaseResult(
                        id=case["id"],
                        passed=passed,
                        message=case.get("message", ""),
                        expected="true",
                        actual=str(passed).lower(),
                    )
                )
            else:
                expected = case.get("expectedStdout", "")
                results.append(
                    CaseResult(
                        id=case["id"],
                        passed=stdout.strip() == expected.strip(),
                        message=case.get("message", ""),
                        expected=expected,
                        actual=stdout,
                    )
                )
        except BaseException as exc:  # noqa: BLE001
            results.append(CaseResult(id=case["id"], passed=False, message=str(exc)))

    passed = bool(results) and all(r.passed for r in results)
    if passed:
        kind = None
    elif run_failure is not None:
        kind = _classify(run_failure)  # crashed on some input: not a clean run
    else:
        kind = "semantic"  # ran clean and failed the tests: the real signal
    return EvalResult(passed=passed, failure_kind=kind, cases=results)
