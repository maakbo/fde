# Reader-facing Architecture Artifacts

Keep model-making history separate from the page used to understand the architecture.

## Page pattern

Use this order:

````markdown
# Architecture or responsibility name

```mermaid
...
```

Two or three sentences about who acts, where responsibility lies, and what reaches
another person or system. Add related-work links when useful.
````

Keep the architecture story, candidate inventory, relationship evidence, naming alternatives,
boundary reasoning, validator output, and unresolved items in the authoring workspace or private
checkpoint.

## Publishing check

- One page answers one reader question.
- A first reader can identify the decision maker, in-focus responsibility, and outcome surface.
- Public labels are understandable without internal project history.
- Navigation connects the Overview to relevant Context or Flow Views.
- Private decisions, unpublished intent, credentials, local paths, and operational mailbox content
  are absent.
- Markdown contains one Mermaid block and no committed derived image unless explicitly requested.

The heading owns the title; omit Mermaid frontmatter `title` for embedded
reader diagrams. Omit author-facing headings such as `モデル` and
`このモデルが表していること`. Put concise scope, parent-node traces, and
maintenance rationale in Mermaid `%%` comments. Keep reader-relevant decisions
and uncertainty in the prose; private history stays private.

Use `reader-facing-artifact-review` for the final reader/independent review when
requested or authorized. Use the authoring layout reference when line shapes
are inconsistent; matching `curve` alone does not make ELK and Dagre equivalent.
