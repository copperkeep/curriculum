# Writing a lesson

A lesson is a directory. Nothing is registered anywhere else — the `steps:` list in
`lesson.yaml` is the order a learner walks.

```
courses/python-a/modules/03-loops/lessons/02-for-range/
├── lesson.yaml
└── steps/
    └── 04-count-to-ten/
        ├── meta.yaml          skills, prerequisites, hints, step type
        ├── prose.grade3.mdx   what a young reader sees
        ├── prose.adult.mdx    same skills, same tests, different words
        ├── starter.py         what is in the editor when they arrive
        ├── solution.py        the reference. Never shipped to the browser
        └── tests.yaml         how it is graded
```

## Pick the step type deliberately

The type is not a formatting choice; it changes how much a correct answer is worth.

| Type | Use it to | What it costs |
|---|---|---|
| `narrative` | Introduce a concept | No signal at all — nothing is graded |
| `predict` | Kill tweak-until-green: there is nothing to permute | A 4-option question has a 25% guess floor |
| `parsons` | Give a no-typing on-ramp that keeps real Python on screen | Weak without distractors |
| `fill-blank` | Bridge from parsons to writing code | — |
| `free-code` | Real practice | The strongest ordinary signal |
| `explain-back` | Catch pattern-matching | Needs a well-chosen wrong answer |
| `project` | End a module | Slow to grade well |

A skill is never mastered from one step type alone. Two distinct types, three
opportunities, and an estimate over the threshold — write lessons that can supply that.

## Transfer items earn their keep

`transferFor: [for-loop-range]` marks a step as a **visibly different problem shape** for
a skill already taught. Counting by twos after counting to ten is a transfer item;
counting to twenty is not.

It is the strongest single signal that a learner understands rather than remembers, and
a skill solved with AI guidance cannot be marked mastered until one is passed. Put one
at the end of every lesson.

## Hints: count semantic failures only

```yaml
hints:
  - afterSemanticFailures: 2
    tier: grade3
    text: "Remember, range(10) counts 0 to 9."
```

`afterSemanticFailures` counts submissions that **ran cleanly and produced the wrong
answer**. Syntax errors and exceptions do not count — a beginner fights a missing colon
constantly, and being re-taught loops for it would punish exactly the trial-and-error
this is supposed to encourage.

Write the ladder as nudge → targeted hint → worked example. Never write the answer: when
AI guidance is enabled it fires only after this ladder is exhausted, and a generated
hint that contains code is rejected by the server before a learner sees it.

## Tests are learner-facing

```yaml
cases:
  - id: counts-zero-to-nine
    expectedStdout: |
      0
      1
    message: "shows 0 to 9, one on each line"
```

The `message` is what a child reads when the row goes red. Write it as a description of
what was wanted, not as a diagnosis of what they did wrong. `expectedStdout` is compared
after stripping surrounding whitespace.

For anything not about output, use an expression evaluated in the learner's namespace:

```yaml
  - id: uses-a-loop
    assert: "total == 45"
    message: "adds the numbers up to 45"
```

## grade3 prose is gated mechanically

Not by discipline. `python tools/check.py` fails on:

- a Flesch-Kincaid grade above 4.0
- any sentence over 14 words
- any word outside `vocabulary/grade3-allowlist.txt`

The word check is additive by design. When it flags a word, decide: an eight-year-old
either knows it — add it to the list — or does not, and the sentence gets rewritten.
Either way the decision is written down instead of remembered.

Write the `adult` tier as the base and simplify from it. A missing tier falls back to the
next simpler one, never to `adult`.

## Two things to know about grading

**Nothing is verified server-side.** Execution is client-side, so a determined student
with DevTools can forge a pass. The server checks that prerequisites are held, that a
submission accompanies the completion, and that the timing is physically plausible — it
cannot check the result itself. This is fine for your own children and matters the moment
a certificate depends on it.

**A `predict` step's answer ships to the browser.** It is in `course.json` because the
client grades the step. Treat predict items as a signal about understanding, not as an
assessment you could publish a score from.
