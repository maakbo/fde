# Repository instructions

Read and follow `/AGENTS.md` before changing artifacts.

- Route improvement and end-to-end introduction requests through
  `.agents/skills/discovery-facilitation/SKILL.md` and its field-delivery loop.
  Continue selected targets with `.agents/skills/definition-facilitation/SKILL.md`.
- Route sequence, handoff, decision, and rework dialogue through
  `.agents/skills/business-flow-facilitation/SKILL.md`; retain a parent Business
  and separate current from proposed flows.
- Route knowledge capture, authorized sources and retrieval failures through
  `.agents/skills/knowledge-stewardship/SKILL.md`; use
  `.agents/skills/ai-pilot-evaluation/SKILL.md` for bounded trial decisions.
- Route loose business descriptions through `.agents/skills/business-context-modeling/SKILL.md`.
- Route human, AI-agent, system, repository, service, channel, artifact, and
  boundary descriptions through `.agents/skills/architecture-modeling/SKILL.md`.
- If actors, external systems, or information need their own relationships,
  update the matching master map first and record `Master references` in each
  context source.
- If same-type relationships are not yet evidenced, keep candidates as
  disconnected nodes and validate with `--allow-sparse` rather than inventing
  a relationship.
- Use `.agents/skills/mermaid-diagram-authoring/SKILL.md` for fast-preview Mermaid in Markdown.
- Write image nodes as `label`, `img`, `pos`, `w`, `h`, `constraint` in that
  order so the English ID and Japanese label stay adjacent while editing.
- Do not generate `.mmd`, SVG, or PNG during ordinary modeling or authoring.
- Use `.agents/skills/mermaid-diagram-export/SKILL.md` after an explicit export,
  image, preview, or visual-review request; temporary review is separate from
  publishing fixed assets.
- Route proofreading, page consolidation, and reader-facing finishing through
  `.agents/skills/reader-facing-artifact-review/SKILL.md`. When authorized and
  available, use a read-only independent reviewer before completion.
- Use a business/theme heading, diagram, then supplement. Omit duplicate Mermaid
  titles and author-facing headings; maintenance intent belongs in `%%` comments.
- New reader diagrams default to Dagre/basis. Compare actual previews for routing
  changes; equal curve settings do not make ELK and Dagre lines look alike.
- Do not copy private or identifying data into examples; use synthetic fixtures.
- When the work needs several levels, use the model ladder: overall context
  (title-level business area and major actors) → use-case / scene context (one
  changing business outcome with canonical master elements) → business flow
  (order, decisions, and rework). Trace each child to one parent node.
- For architecture, treat Overview / System Context, Architecture Context,
  Detailed Architecture Context, and Interaction Flow as optional recursive
  View roles rather than a fixed mandatory ladder.
- Run `python3 scripts/validate_repository.py` before reporting completion.
