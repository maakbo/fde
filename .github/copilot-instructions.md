# Repository instructions

Read and follow `/AGENTS.md` before changing artifacts.

- Route requests to improve real work, find bottlenecks, choose what to change first,
  or assess AI / automation fit through `.agents/skills/discovery-facilitation/SKILL.md`.
  Start from the user's own words, ask one focused question at a time, and do not assume AI is the answer.
- Route requests to visualize how work happens (activities, actors, information,
  decisions, or boundaries) through `.agents/skills/business-context-modeling/SKILL.md`.
  Discovery may call this Skill when the current work is not visible enough.
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
- Use `.agents/skills/mermaid-diagram-export/SKILL.md` only after an explicit export or image request.
- Do not copy private or identifying data into examples; use synthetic fixtures.
- When the work needs several levels, use the model ladder: overall context
  (title-level business area and major actors) → use-case / scene context (one
  changing business outcome with canonical master elements) → business flow
  (order, decisions, and rework). Trace each child to one parent node.
- For architecture, treat Overview / System Context, Architecture Context,
  Detailed Architecture Context, and Interaction Flow as optional recursive
  View roles rather than a fixed mandatory ladder.
- Run `python3 scripts/validate_repository.py` before reporting completion.
