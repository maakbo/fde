---
name: mermaid-diagram-authoring
description: Create and refine simple Mermaid diagrams directly inside Markdown or as explicitly requested standalone .mmd sources. Use for fast GitHub or VS Code preview, actor/system/information master maps, relationship diagrams, business context views, operational flows, decisions, rework, and source-only Mermaid cleanup. This Skill never creates SVG or PNG; route explicit media requests to mermaid-diagram-export.
---

# Mermaid Diagram Authoring

Write the smallest diagram people can inspect while the conversation is still changing. Treat Mermaid as a thinking surface, not merely a final rendering format.

## Core contract

- Default to one `mermaid` code block inside a Markdown file.
- Keep one diagram and one main question per working file.
- Keep the Markdown file as the single editable source; do not duplicate it into `.mmd` automatically.
- Use a standalone `.mmd` only when the user explicitly asks for one or an integration requires it.
- Preserve business meaning while improving notation and visual consistency.
- Never create SVG or PNG, invoke a renderer, or install rendering dependencies unless the user explicitly asks to export.

## Workflow

1. Identify the diagram's purpose, reader, subject, and one-sentence reading.
2. Reuse an existing Markdown file when one already carries the discussion. Otherwise copy `/templates/icon-context.md` or `/templates/business-flow.md`.
3. Choose the smallest suitable profile:
   - Read [references/icon-context.md](references/icon-context.md) for actors, activities, information, systems, undirected relationships, and value-flow context views.
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

6. Stop after source validation. Let the user preview the Markdown immediately in GitHub or VS Code.

## Modeling relationship

When `business-context-modeling` leads the task, use this Skill as its notation discipline inside the same loop:

```text
conversation -> tentative model -> Mermaid -> inspect density and relationships
             -> revise boundary or grain -> update Mermaid
```

Layout pressure is evidence for modeling, not permission to silently change meaning.

## Output contract

Return the Markdown working source, the Mermaid block, a compact text alternative, source-validation results when applicable, and one unresolved semantic or visual question. Do not list image artifacts that were not explicitly requested.
