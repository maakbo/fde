# Repository instructions

Read and follow `/AGENTS.md` before changing artifacts.

- Route loose business descriptions through `.agents/skills/business-context-modeling/SKILL.md`.
- Use `.agents/skills/mermaid-diagram-authoring/SKILL.md` for fast-preview Mermaid in Markdown.
- Do not generate `.mmd`, SVG, or PNG during ordinary modeling or authoring.
- Use `.agents/skills/mermaid-diagram-export/SKILL.md` only after an explicit export or image request.
- Do not copy private or identifying data into examples; use synthetic fixtures.
- Run `python3 scripts/validate_repository.py` before reporting completion.
