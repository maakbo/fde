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
- Use `mermaid-diagram-authoring` inside the modeling loop; let diagram density and layout pressure inform the next abstraction decision.
- Default to one Mermaid block inside a Markdown working file. Do not create `.mmd`, SVG, or PNG unless the user explicitly asks for standalone source or export.

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

Use ordinary relationship lines by default:

```text
actor --- business activity
input information --- business activity
business activity --- output information
external system --- business activity
```

Use only relationships stated by the user or explicitly marked as hypotheses. Reserve external system for software or technical systems outside the chosen boundary; outside people and organizations remain actors.

Use `-->` only when a strong dependency is an intentional part of the question. Do not use arrows for every ordinary relationship.

When the modeling question is specifically how value or information enters and leaves the business activity, use an explicit value-flow context variant:

```text
actor --> business activity <-- input information
business activity --> output information
business activity --> external system --> business activity
business activity --> recipient
```

Use `flowchart LR` and solid `-->` edges. Keep the business activity as the hub, with the input provider, output recipient, and any external system visible around it. In this variant, arrows mean a value or information handoff, not a detailed process sequence; move detailed order or decisions to a focused flow diagram. Keep this exception visible in the companion reading so it is not confused with the ordinary context convention.

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

### 7. Author, preview, and revise

- Follow `mermaid-diagram-authoring` for both relationships and flows.
- Use its icon-context profile for relationships.
- Use its business-flow profile for order, decisions, and rework.
- Keep the diagram in Markdown so the user can preview it immediately in GitHub or VS Code.

For a foundation context:

```bash
python3 .agents/skills/business-context-modeling/scripts/check_business_context.py path/to/context.md
```

The business-context checker includes the authoring profile's strict source validation. Add `--allow-complexity` for an intentionally dense observation view. Inspect the Markdown preview and the relationships it exposes; do not export images as part of the normal modeling loop.

Return to steps 3–6 when the diagram reveals mixed grain, boundary pressure, repeated outcomes, or an unstable parent-child trace.

### 8. Open the discussion

Ask one specific question about boundary, grain, classification, or a relationship. Do not ask only whether the picture looks good.

## Output contract

Return:

1. Modeling question, boundary, and reading sentence.
2. Four-part candidate inventory and nodes selected for the first view.
3. Markdown working source with one previewable Mermaid block.
4. Compact text alternative of the relationship backbone.
5. Assumptions, omitted details, and unresolved classifications.
6. Model-set trace when multiple diagrams exist.
7. One focused discussion question.
8. Source-validation result. Include export results only when the user explicitly requested `mermaid-diagram-export`.
