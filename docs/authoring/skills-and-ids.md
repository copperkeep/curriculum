# Skills, IDs, and changing your mind later

## The contract

Progress events store skill and step IDs as **opaque strings**, forever, in a log that is
never rewritten. That makes them a public interface with exactly one rule:

> Never rename an ID. Never reuse one.

Rename `for-loop-range` to `loops-range` and every historical event referencing it is
orphaned: mastery estimates reset to zero, parent reports go blank, and nothing errors.

`released-ids.json` records what has shipped. CI fails if one of those IDs disappears.

## Adding a skill

```yaml
- id: while-loop-condition
  title: Repeating until something changes
  prerequisites: [for-loop-range]
  pInit: 0.05      # how many learners already know it
  pLearn: 0.18     # chance of learning it in one opportunity
  pSlip: 0.10      # chance of an error despite knowing it
  reportQuestion: "Ask {name} how a while loop knows when to stop."
```

There is no `pGuess`. Guessing is a property of the **item**, not the skill: a 4-option
predict step has a 25% floor by construction, and the engine derives it from the step
type and option count.

Starting values: `pInit` high for something learners arrive with (counting), near zero
for something genuinely new (loops). Everything is calibrated once there is real data,
and recalibration is a replay rather than a migration.

`reportQuestion` is the most-read line in a parent digest. `{name}` is substituted.

## Splitting a skill

You will eventually decide that `for-loop-range` is really two skills. A 1:1 alias cannot
express that, so:

```yaml
ontologyVersion: 2
transitions:
  - from: for-loop-range
    to: [for-loop-iteration, range-generator]
    kind: split
    policy: carry-forward-reduced   # inherit P(known), require one fresh opportunity each
```

Historical events keep saying `for-loop-range` forever. The mapping is applied when
`skill_state` is projected, so applying a transition is a replay, not a destructive
change — and an operator can rebuild any learner's state at any time with
`POST /v1/admin/learners/:id/recompute`.

Merges work the same way, with `policy: min` — take the lower estimate, because claiming
mastery a learner has not demonstrated is the worse error.

## Removing a skill

Removal needs a transition entry too. A skill that simply vanishes fails CI, which is the
point: there is no accidental way to break the log.

## Step prerequisites vs skill prerequisites

They are different, and both matter.

- **Skill prerequisites** (`skills.yaml`) shape the map: what is available, what is
  locked, what order the graph implies.
- **Step prerequisites** (`meta.yaml`) are enforced. The API rejects an attempt on a step
  whose prerequisites the learner does not hold, so a step gated behind a skill nobody
  can reach is a step nobody can complete.

When adding a lesson, check the whole chain is reachable from a learner with an empty
skill map.
