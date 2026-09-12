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
        exec(compile(code, "<lesson>", "exec"), namespace)  # noqa: S102 - that is the job
        failure = None
    except BaseException as exc:  # noqa: BLE001
        failure = exc
    finally:
        sys.stdout, sys.stdin = saved
    return namespace, out.getvalue(), failure


def evaluate(code: str, spec: dict) -> EvalResult:
    namespace, stdout, failure = _exec(code)
    cases = spec.get("cases", [])

    if failure is not None:
        return EvalResult(
            passed=False,
            failure_kind=_classify(failure),
            cases=[
                CaseResult(id=c.get("id", "?"), passed=False, message=str(failure))
                for c in cases
            ],
        )

    results: list[CaseResult] = []
    for case in cases:
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
                if case.get("stdin"):
                    _, actual, case_failure = _exec(code, case["stdin"])
                    if case_failure is not None:
                        results.append(
                            CaseResult(id=case["id"], passed=False, message=str(case_failure))
                        )
                        continue
                else:
                    actual = stdout
                expected = case.get("expectedStdout", "")
                results.append(
                    CaseResult(
                        id=case["id"],
                        passed=actual.strip() == expected.strip(),
                        message=case.get("message", ""),
                        expected=expected,
                        actual=actual,
                    )
                )
        except BaseException as exc:  # noqa: BLE001
            results.append(CaseResult(id=case["id"], passed=False, message=str(exc)))

    passed = bool(results) and all(r.passed for r in results)
    # Ran clean and failed the tests: the real signal.
    return EvalResult(passed=passed, failure_kind=None if passed else "semantic", cases=results)
