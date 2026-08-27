---
name: business-context-modeling
description: Extract actors, business activities, information, and external systems from loose business descriptions; align their abstraction and grain; connect them into discussion-ready Mermaid models; and navigate between dense observation views, focused details, and one-level-higher overviews. Use when visualizing or organizing a business or operation, clarifying a current or future boundary, aligning stakeholder understanding, or moving repeatedly between concrete and abstract business views.
---

# Business Context Modeling

Turn an ordinary conversation about a business or operation into a small model that people can inspect, question, and refine together. Treat the Mermaid diagram as a discussion surface, not final truth.

## Core contract

- Start from loose language; do not require a form before producing a first model.
- Extract four default types: actor, business activity, information, and external system.
- Connect non-business elements through business activities in the foundation context view.
- Keep one modeling question, boundary, state, and main abstraction level per diagram.
- Start a focused view with 3–7 semantic nodes. Treat growth beyond seven as a signal to observe, not an automatic deletion rule.
- Preserve a dense observation view when seeing the complexity supports the discussion.
- When focused diagrams multiply, add or update a one-level-higher overview and trace each detail to one expanded overview node.
- Keep uncertainty, omitted details, and open questions in companion Markdown.
- Keep `.mmd` canonical and render `.svg` and `.png`.

Read [references/modeling-rules.md](references/modeling-rules.md) before classifying or connecting elements. Read [references/multi-view-modeling.md](references/multi-view-modeling.md) when a view grows beyond seven nodes or needs decomposition.

## Workflow

### 1. State the question

Infer, when possible:

- Purpose: which shared understanding or decision the model supports.
- Reader: who will discuss it.
- Boundary: what business or responsibility is inside.
- State: current, future, or comparison. Do not mix current and future.
- Reading: one sentence explaining what the relationships mean.

Ask at most one blocking question. Build version zero when the input supports a plausible first pass and expose assumptions instead.

### 2. Preserve concrete candidates

Collect the user's actual nouns and verbs before abstracting. Classify each as actor, business activity, information, external system, implementation detail, or unresolved.

Always return four compact candidate groups for actor, activity, information, and external system. Write `none observed` or `unresolved` rather than silently omitting a type. Keep omitted implementation details and unresolved items in prose.

### 3. Align abstraction and grain

Use the abstraction ladder in `modeling-rules.md`. Choose capability or outcome-sized activity for a context model. Choose outcome-sized activities or tasks for a flow. Do not mix a broad capability such as `sell products` with an operation such as `export CSV` in one foundation view.

Name actors, information, and systems with short nouns. Name activities with one outcome-oriented verb phrase. Split or rename labels that contain two predicates.

### 4. Build the foundation backbone

Prefer:

```text
actor --- business activity
input information --- business activity
business activity --- output information
external system --- business activity
```

Use only relationships stated by the user or explicitly marked as hypotheses. Reserve external system for software or technical systems outside the chosen boundary; outside people and organizations remain actors.

Use a separate general context view when ownership, storage, access, delivery, or technical integration is itself the question.

### 5. Observe complexity

When the backbone exceeds seven nodes or renders awkwardly, consider preserving the full same-level view as a complexity observation artifact. Inspect:

1. mixed subject;
2. mixed abstraction;
3. mixed boundary;
4. repeated outcomes;
5. missing focused or overview views.

Do not simplify automatically. Choose deliberately among keeping the view, refining its grain or boundary, and adding diagrams.

### 6. Build a navigable model set

When adding focused diagrams, create or update an overview exactly one abstraction level higher. Decide whether the overview shows undirected relationships or directional handoffs. Let each detail expand one stable overview node ID and record the trace in the repository-root template `/templates/model-set-index.md`.

Move upward by grouping details around shared outcomes or responsibilities. Move downward by expanding one overview node into a focused context and, only when order matters, a focused flow.

### 7. Draw, validate, and render

- Use `mermaid-icon-context-diagram` for relationships.
- Use `mermaid-business-flow-diagram` for order, decisions, and rework.

For a foundation context:

```bash
python3 .agents/skills/business-context-modeling/scripts/check_business_context.py path/to/context.mmd
python3 .agents/skills/mermaid-icon-context-diagram/scripts/render_context_diagram.py path/to/context.mmd
```

Add `--allow-complexity` to both commands for an intentionally dense observation view. Inspect the PNG.

### 8. Open the discussion

Ask one specific question about boundary, grain, classification, or a relationship. Do not ask only whether the picture looks good.

## Output contract

Return:

1. Modeling question, boundary, and reading sentence.
2. Four-part candidate inventory and nodes selected for the first view.
3. Canonical `.mmd`, rendered `.svg`, rendered `.png`, and a visible preview.
4. Compact text alternative of the relationship backbone.
5. Assumptions, omitted details, and unresolved classifications.
6. Model-set trace when multiple diagrams exist.
7. One focused discussion question.
8. Validation and render results.
