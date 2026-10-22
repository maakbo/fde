# FDE consumer integration

This repository has a managed Portable FDE profile. Its reusable Skills live at
`.agents/skills/`; local Business Models, diagrams and root instructions remain
consumer-owned.

Add the following sentence to the consumer's own routing surface when desired;
do not replace that surface with this file:

> Route loose business or operational descriptions through
> `.agents/skills/business-context-modeling/SKILL.md`; use its Mermaid authoring
> dependency for source-only diagrams and checks. For sequence, handoff, or
> decision dialogue, use `.agents/skills/business-flow-facilitation/SKILL.md`
> to expand one Business into separate current and proposed flows.

Use `.fde/fde check --artifact-url <tagged-profile-zip-url>` before accepting an
upstream profile update. Once a published profile manifest records that URL,
the `--artifact-url` argument becomes optional. The manager stops rather than
overwriting a locally changed managed file.

The consumer-owned `.fde/config.json` selects `"icon_set": "mdi"` or
`"icon_set": "maakbo"`. Initial installation defaults to MDI and accepts
`--icon-set`; updates never replace the config or rewrite existing diagrams.
Both families use uniform 28 x 28 image nodes, with label text kept at 14px.
For new diagrams, use the authoring Skill's `icon_registry.py create` command
or resolve semantic URLs with `show`. Read its `references/icon-selection.md`
for changing the preference and explicitly migrating an existing diagram.

MDI image URLs default to official MDI GitHub (v7.4.47), independent of this
repository. Set `"mdi_source": "iconify"` for Iconify API in supported environments;
GitHub Mermaid blocks that API. MDI exports
fetch and embed the SVGs; they require network access at export time.

For proofreading, consolidating, or finishing business model pages, use
`.agents/skills/reader-facing-artifact-review/SKILL.md`. It checks reader
structure and routes natural-language and authorized independent review.
Embedded diagrams use their Markdown business heading, without an extra
Mermaid `title`; maintenance notes use `%%` comments. Layout/curve checks do not
prove visual readability. A visual-review request permits temporary rendering
when a native preview or exporter is available; source-only installations need
no Node/browser dependencies merely for prose review.

Use `.agents/skills/knowledge-stewardship/SKILL.md` for tacit judgments, sources,
retrieval and maintenance. Use `.agents/skills/ai-pilot-evaluation/SKILL.md` for
quality, adoption and effect trials. Their templates support existing work
records; they do not grant permission to upload data or deploy a service.
