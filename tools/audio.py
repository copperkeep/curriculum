#!/usr/bin/env python3
"""Generates narration with Piper, at build time.

Deterministic, reviewable in a pull request, works identically on every device, and no
runtime dependency. The Web Speech API was rejected because Chrome frequently routes
synthesis through Google's servers, which fails or degrades on an isolated network.

Only changed prose is regenerated — the corpus is 50-200MB and a typo fix must not
rewrite all of it. A content hash per file is what decides.

    python tools/audio.py --voice voices/en_US-amy-medium.onnx --out dist-audio

Piper voice models carry their own licences, separate from Piper's MIT. Check the one
you ship before shipping its audio.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build import ROOT, build_course, read_yaml  # noqa: E402

MANIFEST_NAME = "audio-hashes.json"


def speakable(markdown: str) -> str:
    """Prose as it should be heard, not as it is written."""
    text = re.sub(r"`([^`]*)`", r"\1", markdown)  # read code spans as their contents
    text = re.sub(r"[*_#>]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--voice", type=Path, required=True, help="Piper .onnx voice model")
    parser.add_argument("--out", type=Path, default=ROOT / "dist-audio")
    parser.add_argument("--tier", default="grade3")
    args = parser.parse_args()

    if shutil.which("piper") is None:
        print("piper not on PATH — skipping narration", file=sys.stderr)
        return 0

    manifest = read_yaml(ROOT / "manifest.yaml")
    args.out.mkdir(parents=True, exist_ok=True)
    hash_file = args.out / MANIFEST_NAME
    previous = json.loads(hash_file.read_text()) if hash_file.exists() else {}
    current: dict[str, str] = {}

    generated = skipped = 0
    for entry in manifest["courses"]:
        _, steps = build_course(ROOT / "courses" / entry["id"])
        for step in steps:
            target = (step.get("audio") or {}).get(args.tier)
            text = step["prose"].get(args.tier)
            if not target or not text:
                continue

            spoken = speakable(text)
            digest = hashlib.sha256(spoken.encode()).hexdigest()
            current[target] = digest

            destination = args.out / target
            if previous.get(target) == digest and destination.exists():
                skipped += 1
                continue

            destination.parent.mkdir(parents=True, exist_ok=True)
            wav = destination.with_suffix(".wav")
            subprocess.run(
                ["piper", "--model", str(args.voice), "--output_file", str(wav)],
                input=spoken.encode(),
                check=True,
            )
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                 "-c:a", "libopus", "-b:a", "48k", str(destination)],
                check=True,
            )
            wav.unlink()
            generated += 1

    hash_file.write_text(json.dumps(current, indent=2, sort_keys=True))
    print(f"narration: {generated} generated, {skipped} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
