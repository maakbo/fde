# Repository instructions

Read and follow `/AGENTS.md` before changing artifacts.

- Route loose business descriptions through `.agents/skills/business-context-modeling/SKILL.md`.
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
- Run `python3 scripts/validate_repository.py` before reporting completion.
