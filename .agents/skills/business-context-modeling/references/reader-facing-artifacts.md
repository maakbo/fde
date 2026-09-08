# Reader-facing model artifacts

Separate the place where a model is made from the place where a business is
understood.

## Three surfaces

| Surface | First reader | Keep here | Keep out |
| --- | --- | --- | --- |
| Authoring workspace | modeler, agent, reviewer | evidence, analysis, candidates, comparisons, naming tests, boundary, validation | polished duplication of the public page |
| Reader-facing sample | person trying to understand the business | diagram, nearby Japanese explanation, direct links to parent / child Views | authoring history, method tutorials, internal uncertainty, validator notes |
| Private checkpoint | project owner and future workers | decisions, rejected options, unresolved items, review state, next, stopping point | public-facing repetition that already exists in the sample |

Do not solve this separation by leaving a hidden public `model.md` full of
authoring history. Move reusable knowledge to references, project history to a
private checkpoint, and delete the remaining duplication.

## The diagram is the reader's entry point

A reader-facing model exists to support shared recognition of the work. The
reader should be able to look at the diagram, understand the nearby business
meaning, and move directly to a deeper or higher View without hunting through
an index.

Treat the diagram as both a **discussion surface** and a **navigation surface**:

- when a Business node has a child Context or Flow, link that node to the child;
- when the diagram is an overview, link each expandable Business to its detail;
- always provide an ordinary Markdown link directly below the diagram as a
  fallback for renderers where Mermaid node links are unavailable;
- keep parent navigation close to the title or diagram, not at the bottom of a
  long technical appendix;
- supporting master maps should be optional nearby links, not mandatory steps
  in the reader's journey.

For GitHub-rendered Mermaid, use a fully qualified repository URL for a node
`click` link when reliability matters. Relative Mermaid links may resolve from
the rendering surface rather than the Markdown file. Keep the adjacent
Markdown link relative so the source remains portable.

## Keep the explanation beside the diagram

Do not force the reader to open a decomposition catalog merely to understand
what the nodes mean. Immediately below the diagram, add a compact Japanese
section such as `図の業務` or `この図の業務`.

For each Business node, state one short sentence explaining the transformation
or outcome. This is where detail belongs; do not push the entire transformation
into the node label.

Example:

```markdown
## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **現行理解** | 現在の業務・ルール・例外を、関係者が同じ前提で話せる状態にする。 |
| [**要件合意**](requirements-flow.md) | 抜けや矛盾を解き、後続が参照できる合意済み要件にする。 |
```

A catalog may still exist as an authoring or reference surface, but the
reader-facing page must carry enough nearby explanation for a meeting or review
without switching files.

## Reader-facing naming

Derive every Business name from input / transformation / output in the
authoring workspace, but publish the shortest label that still evokes the same
business concept.

Prefer a compact semantic name such as:

- `現行理解` rather than `現行を把握する`;
- `責務設計` rather than `人とシステムの責務を分ける`;
- `単体検証` rather than `単体で振る舞いを検証する`;
- `運用移管` rather than `運用へ責任を移す`.

The compact label and the adjacent Japanese explanation work as a pair. Do not
shorten until meaning disappears, but do not make the node carry a sentence.
Stable IDs retain identity when the public label is refined.

## Reader-facing page pattern

Use this as the default for a published Model / View:

````markdown
# Business name or reader question

One or two short sentences explaining what this work changes or makes possible.

← [Parent model](...)

## モデル

```mermaid
...
```

## 図の業務

A compact table or list that explains each Business in ordinary Japanese.
Link Business names to child Views when available.

## この図が表していること

Two or three short sentences. Explain only the relationship or reading that
the diagram and nearby Business descriptions cannot carry.

[Child flow](...) →
````

The exact Japanese headings may change, but preserve the information order:
short introduction, parent path, diagram, adjacent business meaning, short
reading, natural child/supporting links.

## Sample entry page

Lead with an ordinary-language account of the business and its top-level
diagram. Let the diagram itself provide the main paths into detail.

A reader should not need to walk through an Actor Requirement, model-set index,
decomposition catalog, or method page before reaching the main business Views.
Those supporting artifacts can remain available for modelers and deeper review.

## Editing rules for public prose

- Prefer the reader's language over internal canonical terms. Keep canonical
  terminology in IDs, checkers, and the workspace.
- Use short sentences with the subject close to the verb.
- Prefer concrete verbs over strings of abstract nouns.
- Do not repeat every relationship from the diagram in prose.
- Explain Business labels locally when compression would otherwise hide their
  meaning.
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

- the main diagram appears before method or inventory detail;
- the diagram's Business nodes have compact labels;
- the meaning of those labels is available immediately below the diagram;
- expandable Business nodes lead naturally to child Views, with text-link
  fallbacks;
- navigation reaches the parent without returning to a separate index;
- internal analysis lives in the workspace or checkpoint;
- no duplicated `model.md` remains merely as hidden storage;
- Mermaid visual language and source validation still follow the authoring
  Skill.
