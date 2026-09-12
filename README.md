# Copperkeep curriculum

Lessons, the skills ontology, reading tiers, and the tests that grade them. Built into
the `content` and `audio` images that
[`copperkeep/copperkeep`](https://github.com/copperkeep/copperkeep) deploys.

This is a separate repository because it has a separate release cadence, entirely
different CI, and — eventually — authors who are not engineers.

## Versioning

Calendar, not semver: `2026.09.1`. `manifest.yaml` declares `minAppVersion`, and the API
fails its readiness probe on a mismatch, so a curriculum needing a newer app never goes
live.

## Working on it

```sh
pip install pyyaml
python tools/check.py            # every gate
python tools/build.py --out dist # what the content image serves
```

Point a local platform at it:

```sh
cd dist && python -m http.server 8080
# then run the API with COPPERKEEP_CONTENT_BASE_URL=http://localhost:8080
```

## The gates

Run on every pull request. None of them are advisory.

| Gate | What it catches |
|---|---|
| `structure` | A step tagging a skill that does not exist, a predict step whose answer is not among its options, a free-code step with no tests |
| `ids` | A released skill or step ID that disappeared without a transition |
| `solutions` | **A broken exercise, before a child finds it.** Every reference solution runs against its own tests |
| `readability` | grade3 prose above the target grade, a sentence too long, a word outside the allowlist |
| `subresources` | Any external URL. Everything ships inside the image |
| `packages` | A lesson importing something the runtimes image does not vendor |

## The ID contract

Skill and step IDs are stored as opaque strings in an append-only event log.

**Never rename one. Never reuse one.** A rename silently orphans every historical event:
mastery estimates reset and parent reports go blank. Splitting or merging a skill is an
entry in `skills.yaml`'s `transitions`, applied at projection time — history keeps its
original IDs forever.

`released-ids.json` is the baseline, updated by the release job. CI fails if a released
ID vanishes.

## Authoring

See [`docs/authoring/`](docs/authoring/).

## Licence

**CC BY-SA 4.0** — see [`LICENSE`](LICENSE).

Lessons are not software, which is why this repo is licensed differently from the
[platform](https://github.com/copperkeep/copperkeep) (AGPL-3.0). Use these lessons, adapt
them, translate them, teach from them commercially — attribute, and share your
adaptations under the same terms.

Share-alike is the part that matters: it keeps an adapted curriculum open rather than
letting it be repackaged as a closed product.

Contributions follow the platform's [CLA](https://github.com/copperkeep/copperkeep/blob/main/CLA.md),
for the same reason it exists there.

Copyright (C) 2026 Jeffrey Chin.
