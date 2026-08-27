---
name: mermaid-business-flow-diagram
description: Create, refine, lint, render, and audit small icon-based Mermaid business flow diagrams with fixed-size symbols, short labels, directional arrows, and optional decisions or feedback loops. Use for process maps, operational flows, approval paths, request-to-completion sequences, or Git-managed diagrams simple enough to redraw by hand.
---

# Mermaid Business Flow Diagram

Turn one business process into a quiet sequence of fixed-size symbols and arrows.

## Core contract

- Show one process and one reading direction.
- Start with 2–5 activities and allow at most 8 total nodes.
- Omit start and end symbols when first and last activities make the boundary clear.
- Use the ellipse for activities and the Phosphor Thin diamond for a real route-changing decision.
- Put short labels below symbols; never put prose inside a visible box.
- Use `-->` for forward flow and one labeled return route only when rework changes completion.
- Keep `.mmd` canonical and render `.svg` and `.png`.
- Split responsibility, context, data structure, and exception catalogs into separate views.

Read [references/coding-conventions.md](references/coding-conventions.md) before changing Mermaid source.

## Workflow

1. State purpose, reader, first activity, last activity, and the reading sentence.
2. List actions as verbs. Keep actions that change responsibility, information, decision, or completion state.
3. Choose the smallest pattern: straight flow, one decision, one return route, or multiple diagrams.
4. Copy the repository-root template `/templates/business-flow.mmd` and keep its source order.
5. Validate and render:

```bash
python3 .agents/skills/mermaid-business-flow-diagram/scripts/check_business_flow.py path/to/flow.mmd --strict
python3 .agents/skills/mermaid-business-flow-diagram/scripts/render_business_flow.py path/to/flow.mmd
```

6. Inspect the PNG for false routes, clipped labels, ambiguous branches, crossings, or uneven symbol weight.

Do not add swimlanes, subgraphs, color-coded status, several arrow styles, or decorative verb icons to the foundation flow.

## Output contract

Return purpose and reading, canonical `.mmd`, rendered `.svg` and `.png`, visible preview, compact text alternative, validation results, and unresolved action/decision/route wording.
