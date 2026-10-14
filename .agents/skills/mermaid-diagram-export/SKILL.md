---
name: mermaid-diagram-export
description: Explicitly export an existing Mermaid block or standalone .mmd source to self-contained SVG and PNG assets, validate the selected business-context, architecture-context, or flow profile, and inspect publication output. Use only for an explicit preview, render, export, image, fixed-asset publication, or visual-review request; do not invoke during ordinary source-only authoring.
---

# Mermaid Diagram Export

Render an agreed Mermaid source for an explicitly requested preview or fixed asset. Temporary visual review and fixed-asset publication are separate; ordinary source-only authoring does not generate images.

## Core contract

- Require an existing `.md` with one Mermaid block, an explicit `--diagram N` selection from a multi-diagram page, or an explicitly maintained `.mmd` source.
- Never rewrite the working source during export. SVG and PNG must be direct derivatives of that source; do not apply position or typography adjustments after export.
- Validate the requested context or flow profile before rendering.
- Infer the existing diagram's `maakbo` or `mdi` family from its explicit URLs. The project preference must not rewrite a source during export.
- Embed local maakbo SVGs or SVGs fetched from the explicit official MDI GitHub or Iconify URL for MDI. MDI export requires network access; generated outputs are self-contained afterward. Never fall back to fde-hosted MDI assets.
- Generate only the formats the user requests; default to both SVG and PNG when they ask generally for image export.
- Inspect generated assets for clipping or export failure, while keeping working visual judgment in the Markdown Mermaid source.
- An explicit preview or visual-review request authorizes temporary rendering;
  it does not request publishing or committing fixed assets. Keep temporary
  previews outside the source tree. Surface PNGs when images were requested or
  useful for the review; do not publish merely to provide a preview URL.

## Workflow

1. Infer the source path, diagram type, requested formats, and output directory from context. Ask only when ambiguity would overwrite an unrelated artifact.
2. Install the optional rendering dependency once when needed:

```bash
npm ci
```

3. Export explicitly:

```bash
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py path/to/context.md --type context
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py path/to/architecture.md --type architecture
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py path/to/flow.md --type flow --format svg
```

Use `--output-dir path/to/assets` to separate published assets from working Markdown.

4. Inspect the PNG when one was generated for clipping and export failure. If layout or visual hierarchy needs revision, return to the Markdown Mermaid source; do not adjust the generated asset.

## Output contract

Return the unchanged source path, generated artifact paths, validation result, and asset-integrity finding. Do not create a `.mmd` copy merely as an intermediate artifact.

## Multiple diagrams and page titles

Reader-facing Markdown uses its subject heading as the visible title. Export
must not reinsert `title:` into the working source. Standalone diagrams may keep
an explicit title when that is needed for the requested artifact.

For a page with several diagrams, select a one-based block using `--diagram N`.
The chosen block is validated and rendered without rewriting the page, and the
output stem includes the number so review images do not overwrite each other.

```bash
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py \
  examples/maakbo-fde/README.md --diagram 5 --type context \
  --allow-complexity --format png --output-dir /tmp/fde-review
```

Inspect each changed diagram after rendering. Read the authoring Skill's
`references/layout-and-curves.md` for engine/curve differences. When preview is
unavailable, report that limit instead of claiming visual verification.

Purpose/outcome, requirement, and other native Mermaid diagrams need not fit the
icon Context or Flow profiles. Use `--type mermaid` for those diagrams: the
renderer checks Mermaid syntax, but no Business Context/Flow semantic validation
is claimed. Use governed types for diagrams that actually follow those profiles;
do not weaken their checks or change a model merely to make it exportable.

The renderer serves its installed Mermaid modules only over loopback HTTP, so
managed browsers need no `file://` navigation. It uses the existing npm lockfile
and Puppeteer configuration, embeds the icons, and closes the temporary browser
and server after output. No new external hosting service is involved.
