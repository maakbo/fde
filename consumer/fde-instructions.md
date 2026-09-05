# FDE consumer integration

This repository has a managed Portable FDE profile. Its reusable Skills live at
`.agents/skills/`; local Business Models, diagrams and root instructions remain
consumer-owned.

Add the following sentence to the consumer's own routing surface when desired;
do not replace that surface with this file:

> Route loose business or operational descriptions through
> `.agents/skills/business-context-modeling/SKILL.md`; use its Mermaid authoring
> dependency for source-only diagrams and checks.

Use `.fde/fde check --artifact-url <tagged-profile-zip-url>` before accepting an
upstream profile update. Once a published profile manifest records that URL,
the `--artifact-url` argument becomes optional. The manager stops rather than
overwriting a locally changed managed file.
