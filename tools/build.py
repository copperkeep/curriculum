#!/usr/bin/env python3
"""Builds the curriculum tree into the JSON the content image serves.

Three documents come out of this:

  manifest.json  version, minAppVersion, the course list
  skills.json    the skill registry and ontology transitions
  steps.json     a flat index of every step — this is what the API loads to validate
                 events and compute prerequisites. It carries no prose and no tests.
  courses/*.json the full tree the browser reads

`solution.py` is deliberately never emitted. The answer does not travel to the browser.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TIERS = ("grade3", "grade7", "adult")


def read_yaml(path: Path) -> dict:
    with path.open() as handle:
        return yaml.safe_load(handle) or {}


def read_text(path: Path) -> str | None:
    return path.read_text().strip() if path.exists() else None


def build_step(step_dir: Path, course_id: str, lesson_id: str) -> dict:
    meta = read_yaml(step_dir / "meta.yaml")

    prose = {}
    for tier in TIERS:
        text = read_text(step_dir / f"prose.{tier}.mdx")
        if text is not None:
            prose[tier] = text

    step = {
        "id": meta["id"],
        "type": meta["type"],
        "title": meta["title"],
        "skills": meta.get("skills", []),
        "prerequisites": meta.get("prerequisites", []),
        "estimatedMinutes": meta.get("estimatedMinutes", 5),
        "aiGuidance": meta.get("aiGuidance", "allow"),
        "transferFor": meta.get("transferFor", []),
        "prose": prose,
        "hints": meta.get("hints", []),
    }

    if audio := meta.get("audio"):
        step["audio"] = audio
    if starter := read_text(step_dir / "starter.py"):
        step["starter"] = starter
    if (step_dir / "tests.yaml").exists():
        step["tests"] = read_yaml(step_dir / "tests.yaml")
    for key in ("options", "answer", "lines", "distractors"):
        if key in meta:
            step[key] = meta[key]

    # Underscore-prefixed keys are stripped before anything is emitted; they exist so the
    # CI gates can find the source files again.
    step["_courseId"] = course_id
    step["_lessonId"] = lesson_id
    step["_dir"] = step_dir
    return step


def build_course(course_dir: Path) -> tuple[dict, list[dict]]:
    course = read_yaml(course_dir / "course.yaml")
    modules, all_steps = [], []

    for module_name in course["modules"]:
        module_dir = course_dir / "modules" / module_name
        module = read_yaml(module_dir / "module.yaml")
        lessons = []

        for lesson_name in module["lessons"]:
            lesson_dir = module_dir / "lessons" / lesson_name
            lesson = read_yaml(lesson_dir / "lesson.yaml")
            steps = []

            for step_name in lesson["steps"]:
                step = build_step(
                    lesson_dir / "steps" / step_name, course["id"], lesson["id"]
                )
                all_steps.append(step)
                steps.append({k: v for k, v in step.items() if not k.startswith("_")})

            lessons.append(
                {
                    "id": lesson["id"],
                    "title": lesson["title"],
                    "claim": lesson["claim"],
                    "steps": steps,
                }
            )

        modules.append({"id": module["id"], "title": module["title"], "lessons": lessons})

    return {"id": course["id"], "title": course["title"], "modules": modules}, all_steps


def build(out: Path) -> dict:
    manifest = read_yaml(ROOT / "manifest.yaml")
    skills = read_yaml(ROOT / "skills.yaml")

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    step_index: dict[str, dict] = {}
    for entry in manifest["courses"]:
        course_dir = ROOT / "courses" / entry["id"]
        course, steps = build_course(course_dir)

        course_path = out / entry["path"]
        course_path.parent.mkdir(parents=True, exist_ok=True)
        course_path.write_text(json.dumps(course, indent=2))

        for step in steps:
            # Exactly what the API needs, and nothing else: it never reads prose or
            # tests. optionCount is here because pGuess is a property of the item.
            step_index[step["id"]] = {
                "courseId": step["_courseId"],
                "lessonId": step["_lessonId"],
                "type": step["type"],
                "skills": step["skills"],
                "prerequisites": step["prerequisites"],
                "transferFor": step["transferFor"],
                "aiGuidance": step["aiGuidance"],
                "estimatedMinutes": step["estimatedMinutes"],
                "optionCount": len(step["options"]) if "options" in step else None,
            }

    (out / "manifest.json").write_text(
        json.dumps(
            {
                "contentVersion": manifest["contentVersion"],
                "minAppVersion": manifest["minAppVersion"],
                "courses": manifest["courses"],
                "allowedPackages": manifest.get("allowedPackages", []),
                "readingTiers": manifest.get("readingTiers", ["grade3", "adult"]),
            },
            indent=2,
        )
    )
    (out / "skills.json").write_text(json.dumps(skills, indent=2))
    (out / "steps.json").write_text(json.dumps({"steps": step_index}, indent=2))

    return {"steps": len(step_index), "version": manifest["contentVersion"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    result = build(args.out)
    print(f"built {result['steps']} steps at version {result['version']} into {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
