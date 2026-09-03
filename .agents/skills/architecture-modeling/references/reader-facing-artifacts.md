# Reader-facing Architecture Artifacts

Keep model-making history separate from the page used to understand the architecture.

## Page pattern

Use this order:

````markdown
# Reader question or architecture name

One or two short sentences that state what environment this View shows.

## モデル

```mermaid
...
```

## このモデルが表していること

Two or three short sentences explaining the responsibility or boundary the diagram cannot carry.

← [Parent or sample entry](...)

[Related context or interaction flow](...) →
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
