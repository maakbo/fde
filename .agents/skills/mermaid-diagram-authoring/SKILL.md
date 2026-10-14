---
name: mermaid-diagram-authoring
description: Create and refine simple Mermaid diagrams directly inside Markdown or as explicitly requested standalone .mmd sources. Use for fast GitHub or VS Code preview, actor/system/information master maps, relationship diagrams, business context views, operational flows, decisions, rework, and source-only Mermaid cleanup. This Skill never creates SVG or PNG; route explicit media requests to mermaid-diagram-export.
---

# Mermaid Diagram Authoring

Write the smallest diagram people can inspect while the conversation is still changing. Treat Mermaid as a thinking surface, not merely a final rendering format.

## Core contract

- Default to one `mermaid` code block inside a Markdown file.
- Keep one main question per diagram. A reader page may contain several subject sections and diagrams; validate each block separately rather than splitting the page solely for a one-block checker.
- Keep the Markdown file as the single editable source and working visual-review surface; do not duplicate it into `.mmd` automatically.
- Use a standalone `.mmd` only when the user explicitly asks for one or an integration requires it.
- Preserve business meaning while improving notation and visual consistency. Treat the established icon stroke width and size, spacing, relation line, arrow usage, color, and typography as visual-language assets; do not change them without explicit agreement.
- In a business model set, keep the profiles separate: Overall / Business Map,
  Business Context for one scene with a multi-Business backbone, and a Flow or
  recursive Detailed Business Context expanding one selected Business. Record
  the parent/expanded-node trace in Mermaid `%%` comments or an existing model-set
  index; keep it out of reader prose.
- Keep image-node properties in the exact order `label`, `img`, `pos`, `w`,
  `h`, `constraint`, so the stable English ID and Japanese label remain easy
  to compare while editing.
- Before adding layout machinery, try the semantic relationships, node and relationship source order, and Mermaid's native layout. Do not use dummy nodes, meaningless transparent relations, or derived-asset adjustments to force an arrangement.
- In reader-facing Markdown, use a business/theme heading, the diagram, then a
  short business explanation. Omit Mermaid frontmatter `title` so the heading
  is not repeated in the picture. Standalone exports may have a title when needed.
- Keep scope, relation meaning, parent/expanded IDs, omissions, and layout notes
  needed for maintenance in `%%` comments. Comments do not replace facts readers
  need to understand or decide; sensitive project history stays private.
- Default to `layout: dagre` with `curve: basis` for smooth connected curves.
  Read [layout-and-curves.md](references/layout-and-curves.md) before changing
  routing or comparing mixed engines. Do not silently migrate existing layouts.
- Do not generate images during ordinary authoring. An explicit request to
  preview, render, or visually review authorizes temporary rendering via
  `mermaid-diagram-export`; publishing or committing fixed assets is separate.

## Workflow

Before creating a diagram, read [icon-selection.md](references/icon-selection.md).
Resolve the project's `icon_set` and semantic icons through the common registry.
Instantiate templates with `icon_registry.py create` so the destination's
preference is applied. Existing diagrams keep their explicit icon URLs.

1. Identify the diagram's purpose, reader, subject, and one-sentence reading.
2. Reuse an existing Markdown file when one already carries the discussion. Otherwise instantiate `/templates/icon-context.md` or `/templates/business-flow.md` with `icon_registry.py create`.
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
   Business Context, confirm the Business backbone is traceable, both semantic
   sides are legible, crossings do not hide the scene, and relation endpoints
   are intact. Then let the user inspect the Markdown in GitHub or VS Code. When the user asks
   for independent review or a finished reader-facing artifact, use
   `reader-facing-artifact-review` to check prose, presentation, and meaning.
   Source validation alone is not evidence that a rendered layout is readable.

## Modeling relationship

When `business-context-modeling` leads the task, use this Skill as its notation discipline inside the same loop:

```text
conversation -> tentative model -> Mermaid -> inspect density and relationships
             -> revise boundary or grain -> update Mermaid
```

Layout pressure is evidence for modeling, not permission to silently change meaning.

Use source order as a semantic layout hint: provider/executor/input nodes,
then Business activities and genuine shared Information in positions matching
their roles, then recipient/output nodes. Do not force a Business / Information
alternation. Write each relation in approximate left-to-right endpoint order.
Never add a fake node or edge to force coordinates.

## Output contract

Return the Markdown working source, the Mermaid block, a compact text
alternative, source-validation and visual-review results when applicable, and
one unresolved semantic or visual question. Do not list image artifacts that
were not explicitly requested.
