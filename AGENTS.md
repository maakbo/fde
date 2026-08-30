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
   When actor, external-system, or information inventories and their same-type
   relationships are part of the question, update the corresponding master maps
   before assembling a business context. Reuse their stable IDs and record
   `Master references` in the context Markdown.
3. Use `mermaid-diagram-authoring` for Mermaid source in Markdown, whether the request begins with a business model or a direct diagram task.
4. Use `mermaid-diagram-export` only when the user explicitly asks for SVG, PNG, rendering, image generation, publishing assets, or visual artifact review.
5. Read only the references directly required by the selected Skill.

## Working principles

- Produce a reviewable version zero when the input supports one. Ask at most one blocking question.
- Preserve the user's original nouns and verbs before abstracting them.
- Separate observations, assumptions, omissions, and open questions.
- Do not invent roles, exchanges, systems, or responsibilities because they are common elsewhere.
- If a master contains multiple candidates but no same-type relationship is
  evidenced yet, keep the nodes disconnected and use `--allow-sparse`; never
  add an edge just to make the map look connected.
- Keep one modeling question, boundary, state, and main abstraction level per diagram.
- Center foundation context models on business activities.
- Keep the three master views distinct from the business-centered context:
  actor hierarchy/relations, external-system relations, and conceptual
  information relations may connect same-type nodes; context edges still join
  one business activity to one non-business element.
- Treat Mermaid layout pressure as modeling evidence. Observe complexity before simplifying it.
- When focused diagrams multiply, add or update a one-level-higher overview and trace each detail to its expanded overview node.
- Keep important meaning in companion Markdown; a diagram alone is not the model.
- Use synthetic examples. Never add personal, customer, credential, or confidential data.

## Artifact rules

- Default to one Mermaid block inside a Markdown working file for immediate GitHub or VS Code preview.
- Keep one editable source per diagram. Do not create a duplicate `.mmd` automatically.
- Keep labels short and place them below fixed-size icons.
- Use the thin Lucide assets defined by the selected diagram Skill; do not introduce a new icon merely for decoration.
- Do not create SVG or PNG during ordinary modeling or diagram authoring.
- When export is explicitly requested, keep the Markdown source unchanged and inspect the PNG when visual review matters.
- When a PNG is requested for review, surface the image in the final response. For public synthetic examples, also provide a tap-friendly raw URL; never publish a private diagram as a fallback.
- Run `python3 scripts/validate_repository.py` before committing. Node and npm are optional until explicit export.
- Keep changes small, reversible, and scoped to the active modeling question.

## Completion

Return or record:

1. The modeling question, boundary, and reading sentence.
2. Candidate actors, activities, information, and external systems.
3. Selected nodes and relationships.
4. Markdown working source with one previewable Mermaid block.
5. Assumptions, omitted details, and unresolved classifications.
6. One focused question that can improve the shared model.
7. Source-validation results, plus export results only when explicitly requested.
