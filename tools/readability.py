"""Readability gates for grade3 prose.

"A third grader can understand it" should be a mechanical guarantee, not something an
author has to remember to do. Three checks, all cheap:

  - Flesch-Kincaid grade level against a target
  - sentence length ceiling
  - vocabulary: words outside the allowlist are flagged

The vocabulary list is deliberately additive. A flagged word is not an error in the
prose — it is a prompt to decide whether an eight-year-old knows that word, and to write
it down either way.
"""

from __future__ import annotations

import re
from pathlib import Path

VOWELS = "aeiouy"

TARGETS = {
    "grade3": {"maxGrade": 4.0, "maxSentenceWords": 14},
    "grade7": {"maxGrade": 8.0, "maxSentenceWords": 22},
    "adult": {"maxGrade": 14.0, "maxSentenceWords": 40},
}


def strip_markup(text: str) -> str:
    text = re.sub(r"`[^`]*`", " code ", text)  # inline code is not prose
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*_#>\[\]()]", " ", text)
    return text


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", strip_markup(text).strip())
    return [p.strip() for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def count_syllables(word: str) -> int:
    word = word.lower().strip("'")
    if not word:
        return 0
    groups = re.findall(rf"[{VOWELS}]+", word)
    count = len(groups)
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def flesch_kincaid_grade(text: str) -> float:
    sentence_list = sentences(text)
    word_list = words(text)
    if not sentence_list or not word_list:
        return 0.0
    syllables = sum(count_syllables(w) for w in word_list)
    return (
        0.39 * (len(word_list) / len(sentence_list))
        + 11.8 * (syllables / len(word_list))
        - 15.59
    )


def load_allowlist(path: Path) -> set[str]:
    allowed: set[str] = set()
    for line in path.read_text().splitlines():
        line = line.split("#")[0].strip().lower()
        if line:
            allowed.add(line)
    return allowed


def check(text: str, tier: str, allowlist: set[str] | None = None) -> list[str]:
    """Returns a list of problems. Empty means the prose passes."""
    target = TARGETS.get(tier)
    if target is None:
        return [f"unknown reading tier {tier}"]

    problems: list[str] = []

    grade = flesch_kincaid_grade(text)
    if grade > target["maxGrade"]:
        problems.append(f"Flesch-Kincaid grade {grade:.1f} exceeds {target['maxGrade']}")

    for sentence in sentences(text):
        length = len(words(sentence))
        if length > target["maxSentenceWords"]:
            problems.append(
                f"sentence of {length} words exceeds {target['maxSentenceWords']}: "
                f"{sentence[:60]}…"
            )

    if allowlist is not None:
        unknown = sorted({w for w in words(text) if w not in allowlist})
        if unknown:
            problems.append(
                "words outside the allowlist: "
                + ", ".join(unknown)
                + " — add them to vocabulary/grade3-allowlist.txt if a third grader "
                "knows them, otherwise rewrite"
            )

    return problems
