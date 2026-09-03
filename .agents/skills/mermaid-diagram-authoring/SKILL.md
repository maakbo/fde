---
name: mermaid-diagram-authoring
description: Create and refine simple Mermaid diagrams directly inside Markdown or as explicitly requested standalone .mmd sources. Use for fast GitHub or VS Code preview, actor/system/information master maps, relationship diagrams, business context views, operational flows, decisions, rework, and source-only Mermaid cleanup. This Skill never creates SVG or PNG; route explicit media requests to mermaid-diagram-export.
---

# Mermaid Diagram Authoring

Write the smallest diagram people can inspect while the conversation is still changing. Treat Mermaid as a thinking surface, not merely a final rendering format.

## Core contract

- Default to one `mermaid` code block inside a Markdown file.
- Keep one diagram and one main question per working file.
- Keep the Markdown file as the single editable source and working visual-review surface; do not duplicate it into `.mmd` automatically.
- Use a standalone `.mmd` only when the user explicitly asks for one or an integration requires it.
- Preserve business meaning while improving notation and visual consistency. Treat the established icon stroke width and size, spacing, relation line, arrow usage, color, and typography as visual-language assets; do not change them without explicit agreement.
- In a business model set, keep the profiles separate: overall context for the
  title-level business area and major actors, use-case context for one changing
  scene, and business flow for order or decisions inside that scene. Record the
  parent/expanded-node trace outside the Mermaid block.
- Keep image-node properties in the exact order `label`, `img`, `pos`, `w`,
  `h`, `constraint`, so the stable English ID and Japanese label remain easy
  to compare while editing.
- Before adding layout machinery, try the semantic relationships, node and relationship source order, and Mermaid's native layout. Do not use dummy nodes, meaningless transparent relations, or derived-asset adjustments to force an arrangement.
- Never create SVG or PNG, invoke a renderer, or install rendering dependencies unless the user explicitly asks to export.

## Workflow

1. Identify the diagram's purpose, reader, subject, and one-sentence reading.
2. Reuse an existing Markdown file when one already carries the discussion. Otherwise copy `/templates/icon-context.md` or `/templates/business-flow.md`.
3. Choose the smallest suitable profile:
   - Read [references/icon-context.md](references/icon-context.md) for actors,
     activities, information, systems, semantic left/center/right layout, and
     context relationships.
   - For an actor, external-system, or information master map, read
     `../business-context-modeling/references/master-elements.md`, copy the
     matching template, and run `check_master_map.py` with its `--kind`.
   - Read [references/business-flow.md](references/business-flow.md) for order, decisions, and rework.
   - For another Mermaid type, use native syntax and avoid adding visual machinery that the subject does not require.
4. Edit the Mermaid block and its short reading or unresolved question together.
5. For a governed profile, run the relevant source-only checker:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py path/to/context.md --strict
python3 .agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py path/to/flow.md --strict
```

For Business Context semantics, also run:

```bash
python3 .agents/skills/business-context-modeling/scripts/check_business_context.py path/to/context.md
```

The context checker rejects arrows by default. If direction itself is a
documented semantic exception, opt in with `--allow-arrow-exception`; ordinary
provider, recipient, input, and output relations do not need it.

6. Inspect the native or rendered preview after source validation. For a
   Business Context, confirm the Business is centered, both semantic sides are
   legible, and relation endpoints are intact. Then let the user inspect the
   Markdown in GitHub or VS Code.

## Modeling relationship

When `business-context-modeling` leads the task, use this Skill as its notation discipline inside the same loop:

```text
conversation -> tentative model -> Mermaid -> inspect density and relationships
             -> revise boundary or grain -> update Mermaid
```

Layout pressure is evidence for modeling, not permission to silently change meaning.

Use source order as a semantic layout hint: provider/executor/input nodes,
then the Business, then recipient/output nodes. Write each relation in that
same endpoint order. Never add a fake edge to force coordinates.

## Output contract

Return the Markdown working source, the Mermaid block, a compact text
alternative, source-validation and visual-review results when applicable, and
one unresolved semantic or visual question. Do not list image artifacts that
were not explicitly requested.
