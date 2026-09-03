# Business Story and 5W2H

Use this reference in the authoring workspace before selecting public Views.
The analysis may be detailed; the published result does not need to expose the
analysis format.

## Start with a Business Story

Write two or three ordinary sentences that answer:

- Who provides value or Information?
- What does the Business use or change?
- What Information or value does it create, update, or make usable?
- Who receives, operates, changes, or grows the result?

Describe relationships first. Do not force a chronological route; sequence,
decisions, and rework belong in a Business Flow only when they matter.

Keep the user's nouns and verbs as evidence. After the story is coherent,
extract candidates and name the Business with `modeling-rules.md`.

## Use 5W2H as an analysis lens

5W2H checks whether the story carries enough meaning. It is not a mandatory
public heading set.

| Lens | Question for the workspace | Typical model consequence |
| --- | --- | --- |
| Why | What ultimate purpose, desired state, and enabling outcome are distinct here? | Purpose / Outcome View and the criteria used to evaluate How |
| Who | Who has purpose, judgment, action, or responsibility? Which technical systems remain outside the selected boundary? | Actor candidates, External System candidates, System Context |
| What | What value or capability does the whole Business provide? What state must remain after delivery? | Business definition and Business Map |
| When | What event, condition, or change creates the need? | Scope, trigger, or a later Flow; not every example becomes a node |
| Where | In what physical, organizational, informational, or system environment does the work hold? | Boundary and Context |
| How | Which activities, relationships, flows, and implementation choices produce the value? | Business Context, Business Flow, implementation Views |
| How much | What is the smallest valuable unit, cadence, completion condition, and acceptable dependency? | Slice size, iteration policy, completion criteria |

Check the answers against the natural-language story. If a 5W2H answer cannot
be grounded in the story or source material, keep it unresolved; do not invent
it to complete the table.

## Preserve the meaning trace

Keep this chain in the workspace:

```text
Why / Purpose
  -> Desired State / Outcome
  -> Business / Activity
  -> Actor / Information / System relationships
  -> How / Flow / Implementation
```

This is not a waterfall. Move downward to make meaning concrete. Move upward
when a detailed How fails the purpose, a Business boundary proves wrong, or an
Actor's responsibility changes.

Treat the Model as a meaning axis people can return to after technology,
systems, or conditions change. The public sample may summarize this in one
sentence; keep the full trace and its revisions in the authoring workspace or
private checkpoint.

## What to publish

Absorb the agreed Business Story into a short introduction and the selected
diagrams. Publish a 5W2H table only when the reader's question is explicitly to
inspect 5W2H. Otherwise it remains authoring knowledge.
