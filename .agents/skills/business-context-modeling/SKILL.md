---
name: business-context-modeling
description: Extract actors, business activities, information, and external systems from loose business descriptions; maintain reusable actor, external-system, and information master maps; align abstraction and grain; connect canonical elements into discussion-ready Mermaid models; and move through overall, use-case, and flow views while navigating between dense observation, focused details, and one-level-higher overviews. Use when visualizing or organizing a business or operation, clarifying a current or future boundary, aligning stakeholder understanding, or moving repeatedly between concrete and abstract business views.
---

# Business Context Modeling

Turn an ordinary conversation about a business or operation into a small model that people can inspect, question, and refine together. Treat the Mermaid diagram as a discussion surface, not final truth.

## Core contract

- Start from loose language; do not require a form before producing a first model.
- Before listing candidates, describe the business in two or three natural-language sentences: who (Actors and External Systems) provides which Information, how the Business uses it, which Information it creates or updates, and who receives it.
- Extract four default types: actor, business activity, information, and external system from that description.
- At the Business boundary, Actor and External System are peer kinds of participant: either may provide value or Information to the Business and either may receive value or Information from it. Distinguish them by purposeful action and responsibility (Actor) versus a technical system outside the selected boundary (External System).
- Peer participation does not require both types to appear in every Business Context. Include an External System only when the described business shows its provider or recipient relationship; otherwise record `none observed` and keep genuinely possible systems as unresolved, outside the candidate inventory.
- When participants, systems, or information relationships matter, maintain three
  canonical master views: an actor map, an external-system map, and an
  information model. These maps may connect same-type nodes; they are not
  substitutes for the business-centered context view.
- Give master elements stable IDs and reuse those IDs, labels, icons, and sizes
  when selecting them in a context view. Record the selection in a `Master
  references` section because Mermaid cannot import another Markdown diagram.
- Connect non-business elements through business activities in the foundation context view.
- Keep one modeling question, boundary, state, and main abstraction level per diagram.
- Use a three-rung model set when the work needs more than one context: overall
  context (title-level business area and major actors), use-case context (one
  changing scene around one business outcome), then business flow (order,
  decisions, or rework inside that scene). The flow is a separate diagram, not
  another relationship context.
- Start a focused view with 3–7 semantic nodes. Treat growth beyond seven as a signal to observe, not an automatic deletion rule.
- Preserve a dense observation view when seeing the complexity supports the discussion.
- When focused diagrams multiply, add or update a one-level-higher overview and trace each detail to one expanded overview node.
- Keep uncertainty, omitted details, and open questions in companion Markdown.
- Use `mermaid-diagram-authoring` inside the modeling loop; let diagram density and layout pressure inform the next abstraction decision.
- When writing Mermaid image nodes, keep properties in the exact order
  `label`, `img`, `pos`, `w`, `h`, `constraint` so stable English IDs and
  Japanese labels can be compared at a glance.
- Default to one Mermaid block inside a Markdown working file. Do not create `.mmd`, SVG, or PNG unless the user explicitly asks for standalone source or export.

Read [references/modeling-rules.md](references/modeling-rules.md) before classifying or connecting elements. Read [references/master-elements.md](references/master-elements.md) when the task asks for actor, system, or information inventories, same-type relationships, or reusable elements. Read [references/multi-view-modeling.md](references/multi-view-modeling.md) when a view grows beyond seven nodes or needs decomposition.

## Workflow

### 1. State the question

Infer, when possible:

- Purpose: which shared understanding or decision the model supports.
- Reader: who will discuss it.
- Boundary: what business or responsibility is inside.
- State: current, future, or comparison. Do not mix current and future.
- Reading: one sentence explaining what the relationships mean.

Ask at most one blocking question. Build version zero when the input supports a plausible first pass and expose assumptions instead.

### 2. Describe the business, then preserve concrete candidates

Write a two- or three-sentence natural-language description before making an inventory. State who provides which Information, what the Business does with it, which Information it creates or updates, and who receives it. Here, `who` can include both Actors and External Systems; do not invent an External System to fill the type when none appears in the description. This description expresses relevant relationships, not a fixed chronological flow.

Collect the nouns, verbs, and Information objects that actually occur in that description before abstracting. Classify each as actor, business activity, information, external system, implementation detail, or unresolved. Do not carry a candidate forward merely because it appeared in an earlier inventory or because it belongs to the modeling method itself.

Always return four compact candidate groups for actor, activity, information, and external system. Write `none observed` or `unresolved` rather than silently omitting a type. Keep omitted implementation details and unresolved items in prose.

When a master layer already exists, reconcile each actor, external-system, and
information candidate against its canonical ID before creating a new one. Keep
source wording and possible aliases in the companion Markdown. Do not silently
merge two candidates that differ by responsibility, abstraction, state, or
boundary.

### 3. Align abstraction and grain

Use the abstraction ladder in `modeling-rules.md`. Choose capability or outcome-sized activity for a context model. Choose outcome-sized activities or tasks for a flow. Do not mix a broad capability such as `sell products` with an operation such as `export CSV` in one foundation view.

Name actors, information, and systems with short nouns. Name activities with one outcome-oriented verb phrase. Split or rename labels that contain two predicates.

If the request includes same-type relationships, update the relevant master map
before composing the context. Use the master templates and run
`check_master_map.py` with `--kind actor`, `--kind system`, or `--kind
information`.

Choose the context rung before writing Mermaid:

- **Overall context**: center a title-level business area or outcome as a
  `b_` node and place the major actor subjects around it. This is a relationship
  view, not a process route; keep detailed information and systems for a child
  view unless they are essential to the overall boundary.
- **Use-case context**: cut one scene where an actor responsibility, external
  system boundary, information handoff, or value recipient changes. Center one
  outcome-sized `b_` activity and select the surrounding `a_`, `x_`, and `i_`
  nodes from the masters. If the scene becomes crowded, split by scene or
  discussion question and trace each child to the same parent node.
- **Business flow**: only after a use-case context shows that order, decisions,
  or rework matter. Expand one activity from that context and use the
  `mermaid-business-flow-diagram` Skill for directional arrows.

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

Describe the provider, recipient, and Information relationship in companion prose. Keep the Business Context's ordinary lines as relationships, not a one-way route; move time, order, decisions, and detailed handoffs to a Business Flow.

When the modeling question is specifically the direction of value or Information handoff, use an explicit value-flow context as a separate View variant:

```text
actor --> business activity <-- input information
business activity --> output information
business activity --> external system --> business activity
business activity --> recipient
```

Use `flowchart LR` and solid `-->` edges only when that direction is the question. Keep the Business activity as the hub and include an External System only when one is observed. In this variant, arrows mean value or Information handoff, not chronology; move detailed order, decisions, and rework to a Business Flow. State this reading in the companion prose.

For every selected `a_`, `x_`, or `i_` node, copy the canonical master node
definition and add a `## Master references` table with the master path, ID,
canonical label, and reason for selection. The context may use a different
layout or a narrower reading, but it must not invent a second identity.
Use a path that resolves from the context file to the exact master source, not
only a same-named file in another model set.
Run `check_master_references.py` when the master paths are available; it compares
the selected node's ID, label, icon, size, and class against the canonical map.
Add `--allow-sparse` when a supplied master intentionally contains multiple
candidate nodes whose same-type relationships have not been observed yet.

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

When adding use-case / scene diagrams, create or update an overall (or
one-level-higher) overview exactly one abstraction level above them. Decide
whether the overview shows undirected relationships or directional handoffs.
Let each detail expand one stable overview node ID and record the trace in the
repository-root template `/templates/model-set-index.md`.

Move upward by grouping details around shared outcomes or responsibilities. Move downward by expanding one overview node into a focused context and, only when order matters, a focused flow. Record the three master views in the model-set index with role `master`, then link context views to the exact master IDs they select. Treat the index as navigation and trace, not as a second canonical registry.

For a three-rung set, record the chain explicitly: `overall context` → `use-case
context` → `business flow`. A use-case context has one overview parent and a flow
has one use-case parent. If several use-case scenes emerge, keep sibling views
separate and let the overview remain one level higher. If the overview itself
becomes dense, add one more higher overview rather than flattening the set.

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
6. Model-set trace when multiple diagrams exist, including each view's rung,
   parent, expanded node, and child views.
7. Master views and `Master references` when actor, system, or information maps are in scope.
8. One focused discussion question.
9. Source-validation result, including the matching master-map checks when used. Include export results only when the user explicitly requested `mermaid-diagram-export`.
