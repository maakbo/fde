---
name: architecture-modeling
description: Turn loose descriptions of human, AI-agent, application, system, repository, knowledge-artifact, external-service, communication-channel, and ownership relationships into discussion-ready architecture Views. Use when clarifying a workspace or product boundary, drawing System Context or Architecture Context diagrams, showing how agents and repositories cooperate, expanding one architecture node into a detailed context, or separating a structural architecture View from an Interaction Flow.
---

# Architecture Modeling

Turn an ordinary description of a technical or human-agent environment into a small Model that
people can inspect, question, and refine together. Treat the diagram as a discussion surface, not
as infrastructure truth.

## Core contract

- Write a two- or three-sentence architecture story before listing nodes. Say who initiates or
  operates, what is in focus, which systems or repositories hold responsibility, and who receives
  the result.
- State the View purpose, reader, boundary, state, and one-sentence reading before drawing.
- Extract only elements and relationships supported by the story. Keep uncertain candidates as
  `unresolved`; do not invent diagram glue.
- Classify from the selected boundary. Read [modeling-rules.md](references/modeling-rules.md) before
  naming elements, relationships, or boundaries.
- Use left for initiators, providers, upstream systems, or operators; center for the in-focus
  workspace, system, or capability; and right for consumers, downstream systems, or outcome
  receivers. Let placement carry ordinary direction.
- Use `---` by default. Use an unlabelled `-->` only when direction changes the View's answer and
  left/center/right placement is insufficient. Put sequence in a separate Interaction Flow.
- Use a named subgraph only when a repository, product, runtime, ownership, or trust boundary is
  part of the question. Never group nodes only to force layout.
- Separate the authoring workspace from the reader-facing sample. Keep evidence, candidate
  inventory, relationship model, boundary reasoning, naming candidates, checks, and unresolved
  items private or in Skill references. Publish only a short introduction, the diagram, a short
  reading, and natural links.
- Keep Markdown Mermaid as the editable source. Do not create committed SVG or PNG unless the user
  explicitly requests fixed assets.
- Move down to detail and back up to the parent whenever detail changes a node's responsibility,
  boundary, name, or relationship.

## Workflow

### 1. Choose the View question

Infer a plausible version zero when the input is sufficient. Ask at most one blocking question.
Choose one View role:

- **Architecture Overview / System Context**: the whole environment, main people or agents, the
  in-focus system, and important external responsibilities.
- **Architecture Context**: the relationships around one selected workspace, system, repository,
  or capability.
- **Detailed Architecture Context**: the internal parts and boundaries of one parent node.
- **Interaction Flow**: request, response, review, publish, sync, or decision order.

These are reference shapes, not a mandatory fixed ladder. Use one role and one relationship meaning
per diagram.

### 2. Tell the architecture story

Describe the current, future, or comparison state in ordinary language. Identify the initiator,
in-focus responsibility, durable stores, agents or systems that act, external dependencies, and
result receiver. Do not mix current and future state.

Extract candidates into: human, AI agent, application/system, repository, knowledge/artifact,
external service, communication channel, boundary, implementation detail, and unresolved. Write
`none observed` where a type does not occur; the taxonomy is available, not compulsory.

### 3. Build the relationship model

Before Mermaid, record each candidate relation with its two endpoints, plain meaning, source
evidence, and whether direction is essential. Remove transport or artifact nodes that exist only to
join two other nodes. Keep a repository or channel only when storage, ownership, publication,
access, or communication is part of the question.

Compress each label to a short reader term without changing identity. Preserve the source wording
and naming rationale in the authoring workspace.

### 4. Set placement and boundaries

Place upstream or operating roles left, the in-focus responsibility center, and downstream or
outcome roles right. A node may have several relationships; its horizontal position is not a
substitute for those relationships.

Name each boundary by the responsibility it encloses. Distinguish containment from an ordinary
relation. If a node crosses a boundary in reality, do not place it inside merely to simplify lines.

### 5. Author and validate the context

Copy [`templates/architecture-context.md`](../../../templates/architecture-context.md), then use
the existing `mermaid-diagram-authoring` Skill for notation. Validate the source:

```bash
python3 .agents/skills/architecture-modeling/scripts/check_architecture_context.py \
  path/to/architecture-context.md --strict
```

For a documented directional exception, add `--allow-directed`. For an intentionally dense
observation View, add `--allow-complexity` only after visual inspection.

### 6. Add an Interaction Flow only when order matters

Use `templates/business-flow.md` and the `mermaid-diagram-authoring` flow conventions. Name actions
after the responsible role when responsibility matters. Validate with:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py \
  path/to/interaction-flow.md --strict
```

Do not repeat the full structural topology in the Flow. Link it to the parent architecture View.

### 7. Inspect and refine both directions

Inspect the Mermaid preview or an explicitly requested temporary render. Check semantic
left/center/right placement, boundary truth, label readability, relation crossings, and whether an
arrow is doing work that placement or a separate Flow should do.

Let each detail expand one named parent node. Return to the parent when detail reveals a wrong
responsibility, boundary, identity, or relationship. Use the hierarchy guidance in
[modeling-rules.md](references/modeling-rules.md).

## Output contract

For an authoring workspace or private checkpoint, return:

1. Purpose, reader, boundary, state, and reading sentence.
2. Architecture story and compact candidate inventory.
3. Relationship model, boundary reasoning, and naming candidates.
4. Markdown Mermaid source and a short text alternative.
5. Parent/detail trace when more than one View exists.
6. Validation and visual-review result.
7. Assumptions, omitted details, and unresolved items.

For a public sample, follow [reader-facing-artifacts.md](references/reader-facing-artifacts.md) and
omit the authoring material above.
