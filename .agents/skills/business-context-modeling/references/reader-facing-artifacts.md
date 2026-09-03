# Reader-facing model artifacts

Separate the place where a model is made from the place where a business is
understood.

## Three surfaces

| Surface | First reader | Keep here | Keep out |
| --- | --- | --- | --- |
| Authoring workspace | modeler, agent, reviewer | evidence, analysis, candidates, comparisons, naming tests, boundary, validation | polished duplication of the public page |
| Reader-facing sample | person trying to understand the business | diagram, short explanation, reading, links to related Views | authoring history, method tutorials, internal uncertainty, validator notes |
| Private checkpoint | project owner and future workers | decisions, rejected options, unresolved items, review state, next, stopping point | public-facing repetition that already exists in the sample |

Do not solve this separation by leaving a hidden public `model.md` full of
authoring history. Move reusable knowledge to references, project history to a
private checkpoint, and delete the remaining duplication.

## Reader-facing page pattern

Use this as the default for a published Model / View:

````markdown
# Business name or reader question

One or two short sentences explaining what this work changes or makes possible.

## モデル

```mermaid
...
```

## このモデルが表していること

Two or three short sentences. Explain only what the diagram cannot carry.

← [Parent model](...)

[Related or child model](...) →
````

The exact Japanese headings may change, but preserve the information order:
short introduction, diagram, short reading, natural navigation.

## Sample entry page

Lead with an ordinary-language account of the business. Then offer a few
reader questions rather than an authoring sequence:

- What does this work seek?
- Who realizes it together?
- Which Business activities constitute it?
- Where can one activity be inspected in detail?

Put supporting Views next to the Model they support. Do not make every reader
walk through an Actor Requirement, model index, or method page before reaching
the main business diagrams.

## Editing rules for public prose

- Prefer the reader's language over internal canonical terms. Keep canonical
  terminology in IDs, checkers, and the workspace.
- Use short sentences with the subject close to the verb.
- Prefer concrete verbs over strings of abstract nouns.
- Avoid repeating the diagram in prose.
- Remove labels such as `working hypothesis`, `candidate`, `boundary`, and
  `unresolved` unless that status is itself necessary for the reader.
- Do not explain ASCII alternatives, arrow-selection debates, stable IDs,
  rename / split / merge decisions, or validator behavior on the public page.
- Do not expose private people, customers, credentials, or confidential facts.

## Publishing check

Read the page once as a person who wants to understand the work, not learn the
method. They should be able to say what the work seeks, who participates, what
changes, and where to go next without reading the authoring history.

Then verify:

- every page has one main question;
- navigation reaches the parent and relevant children;
- internal analysis lives in the workspace or checkpoint;
- no duplicated `model.md` remains merely as hidden storage;
- Mermaid visual language and source validation still follow the authoring
  Skill.
