# AGENTS.md

This repository is a portable environment for forward-deployed business modeling.

## Purpose

- Enter through the user's loose language, not a required form.
- Turn situated conversation into a small artifact people can inspect and question together.
- Treat diagrams as discussion surfaces, not final truth.
- Move repeatedly between concrete observation and useful abstraction.
- Keep Markdown and Mermaid source as the durable source of truth.

## Start here

1. If a request clearly matches a Skill under `.agents/skills/`, read that `SKILL.md` completely and follow it.
2. Use `business-context-modeling` for loose business or operational descriptions.
3. Use `mermaid-icon-context-diagram` for undirected relationships.
4. Use `mermaid-business-flow-diagram` for sequence, decisions, or rework.
5. Read only the references directly required by the selected Skill.

## Working principles

- Produce a reviewable version zero when the input supports one. Ask at most one blocking question.
- Preserve the user's original nouns and verbs before abstracting them.
- Separate observations, assumptions, omissions, and open questions.
- Do not invent roles, exchanges, systems, or responsibilities because they are common elsewhere.
- Keep one modeling question, boundary, state, and main abstraction level per diagram.
- Center foundation context models on business activities.
- Treat Mermaid layout pressure as modeling evidence. Observe complexity before simplifying it.
- When focused diagrams multiply, add or update a one-level-higher overview and trace each detail to its expanded overview node.
- Keep important meaning in companion Markdown; a diagram alone is not the model.
- Use synthetic examples. Never add personal, customer, credential, or confidential data.

## Artifact rules

- Keep canonical diagrams as `.mmd`.
- Keep labels short and place them below fixed-size icons.
- Use Iconify icons defined by the selected diagram Skill; do not introduce a new icon merely for decoration.
- Render sibling `.svg` and `.png` after semantic changes.
- Inspect the PNG, not only the Mermaid source.
- Run `npm run validate` before committing.
- Keep changes small, reversible, and scoped to the active modeling question.

## Completion

Return or record:

1. The modeling question, boundary, and reading sentence.
2. Candidate actors, activities, information, and external systems.
3. Selected nodes and relationships.
4. Canonical `.mmd`, rendered `.svg`, and rendered `.png`.
5. Assumptions, omitted details, and unresolved classifications.
6. One focused question that can improve the shared model.
7. Validation and render results.
