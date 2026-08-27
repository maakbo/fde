---
name: mermaid-diagram-export
description: Explicitly export an existing Mermaid block or standalone .mmd source to self-contained SVG and PNG assets, validate the selected diagram profile, and inspect publication output. Use only when the user asks to render, export, publish, generate an image, create SVG or PNG, or perform visual artifact review; do not invoke for ordinary Mermaid authoring or Markdown preview.
---

# Mermaid Diagram Export

Convert an agreed Mermaid source into stable media assets. Treat export as a publication or visual-review gate, not a default part of diagram authoring.

## Core contract

- Require an existing `.md` with one Mermaid block or an explicitly maintained `.mmd` source.
- Never rewrite the working source during export.
- Validate the requested context or flow profile before rendering.
- Embed the selected Lucide SVG data into the generated outputs so they do not depend on remote icons afterward.
- Generate only the formats the user requests; default to both SVG and PNG when they ask generally for image export.
- Inspect the PNG when visual review is part of the request.

## Workflow

1. Confirm the source path, diagram type, requested formats, and output directory from context. Ask only when ambiguity would overwrite an unrelated artifact.
2. Install the optional rendering dependency once when needed:

```bash
npm ci
```

3. Export explicitly:

```bash
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py path/to/context.md --type context
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py path/to/flow.md --type flow --format svg
```

Use `--output-dir path/to/assets` to separate published assets from working Markdown.

4. Inspect the PNG when one was generated. Report clipping, false routes, density, and uneven visual weight without changing business meaning silently.

## Output contract

Return the unchanged source path, generated artifact paths, validation result, and visual-review finding. Do not create a `.mmd` copy merely as an intermediate artifact.
