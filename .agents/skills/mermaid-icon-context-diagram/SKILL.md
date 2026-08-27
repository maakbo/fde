---
name: mermaid-icon-context-diagram
description: Create, refine, lint, render, and audit focused or intentionally dense icon-based Mermaid context diagrams whose visual objects stay fixed regardless of label length. Use for relationship maps, business context diagrams, complexity observation views, comparison backbones, linked model sets, or requests to replace uneven text boxes with icons, short labels, and simple lines.
---

# Mermaid Icon Context Diagram

Create a quiet relationship diagram from fixed-size icon points and simple lines. Keep Mermaid source editable and generate SVG and PNG for stable review.

## Core contract

- Keep one subject and one relationship meaning per diagram.
- Start a focused view with 3–7 semantic nodes; allow a larger observation view when density itself is useful and acknowledged.
- Put short labels below fixed-size icons; never use visible text boxes.
- Connect nodes with `---`; move direction and process into a flow diagram.
- Use the minimal Iconify set: Phosphor Thin for actor, information, external system, and devices; Lucide ellipse for business activity.
- Add another icon only when the subject requires deliberate visual emphasis and record the reason.
- Keep `.mmd` canonical and render `.svg` and `.png`.

Read [references/coding-conventions.md](references/coding-conventions.md) before changing Mermaid source.

## Workflow

1. State purpose, reader, subject, and a one-sentence reading.
2. List concrete candidates before choosing a focused or observation view.
3. Copy the repository-root template `/templates/icon-context.mmd` and keep its source order.
4. Connect relationships to icon node IDs, never explanatory prose.
5. Run strict validation and render:

```bash
python3 .agents/skills/mermaid-icon-context-diagram/scripts/check_context_diagram.py path/to/diagram.mmd --strict
python3 .agents/skills/mermaid-icon-context-diagram/scripts/render_context_diagram.py path/to/diagram.mmd
```

Add `--allow-complexity` to both commands for an intentional observation view.

6. Inspect the PNG. Classify false meaning as `stop`, reproducibility or clipping failures as `must fix`, density or ambiguity as `observe`, and coherent fixed-weight output as `accept`.

Do not solve overload by shrinking text, adding edge labels, nesting subgraphs, or inventing layout machinery.

## Output contract

Return purpose and reading, canonical `.mmd`, rendered `.svg` and `.png`, visible PNG preview, compact text alternative, validation results, and unresolved label/icon/relationship decisions.
