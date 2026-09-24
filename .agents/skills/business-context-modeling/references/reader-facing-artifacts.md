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
what the nodes mean. The default reader-facing contract is:

````markdown
# 普通の業務名

短い自然な導入文。

```mermaid
...
```

この図を読むために必要な1〜3文の説明。
[親の業務を見る](parent.md) / [詳しい場面を見る](detail.md)
````

Use the ordinary business name as the page title, show the diagram as soon as
the reader needs it, and explain only what the diagram cannot carry. A page
may have several sections and diagrams when each section keeps this same
contract; do not add method-aware headings, inventories, or tables by default.
Short lists or tables are fine when they clarify a real relationship that a
label and a sentence cannot hold.

Keep the compact label and nearby explanation as a pair. Do not push an entire
transformation into a node label, but do not make a reader open a catalog just
to learn what a Business node means.

## Parent first, detail second

When a whole Business contains major child Businesses, put the parent, those
children, and their meaningful relationships on the first discussion surface.
This gives the reader the semantic center before asking them to open a detail
View. Link expandable Business nodes to a natural child page and keep a plain
Markdown link beside or below the diagram as a fallback.

Split into a child View only when the scene changes enough to justify it: the
participants, provider or recipient, Information, External System,
responsibility/value boundary, or visual density no longer reads as one
conversation. Business count alone is not a boundary. A detail View should
retain a parent link, and discoveries in the detail should be checked back
against the parent.

When the root reader question explicitly includes Business, participants, and
Information together, a child Information View is supplemental: it must not
replace the major Information projection on the root page. If that integrated
projection cannot remain readable at an honest grain, stop at the review
boundary and record the available grain choices.

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

## Sample entry page

Lead with an ordinary-language account of the business and its top-level
diagram. Let the diagram itself provide the main paths into detail.

A reader should not need to walk through an Actor Requirement, model-set index,
decomposition catalog, or method page before reaching the main business Views.
Those supporting artifacts can remain available for modelers and deeper review.

## Root page pattern

A reader-facing root page may gather the upper views that people need to read
together:

```text
# Whole-system business name
[whole-system diagram]

## What it seeks to make possible
[short natural explanation]

## Business
### Major business name
[business diagram]
[short explanation]

## Information
[information relationship diagram]
[short explanation]
```

Keep the whole-system diagram, business composition, and Information
relationship diagrams as separate questions on one page. Do not turn them into
one giant picture or expose model types in the section titles. If the root
copies reusable Actor, External System, or Information nodes, keep those
definitions aligned with the owning master maps and use validation to catch
stale copies. A child discovery that changes an identity or relation returns to
the root before the child-only edit is considered complete.

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
- Explain the work, not the diagram: after hiding the Mermaid block, the prose
  should still say why the work exists, who participates, what Information is
  handled, and what result reaches the next person or activity. Rewrite prose
  whose subject is `図`, `モデル`, `View`, `ノード`, placement, or authoring.
- Do not explain ASCII alternatives, arrow-selection debates, stable IDs,
  rename / split / merge decisions, or validator behavior on the public page.
- Do not expose private people, customers, credentials, or confidential facts.

## Publishing check

Read the page once as a person who wants to understand the work, not learn the
method. They should be able to say what the work seeks, who participates, what
changes, and where to go next without reading the authoring history.

Then verify:

- the page starts with an ordinary business name or reader question;
- the main diagram appears before method or inventory detail;
- the diagram's Business nodes have compact labels and nearby natural
  explanations;
- the parent diagram shows major child Businesses and their meaningful
  relationships before a reader opens detail;
- expandable Business nodes lead naturally to child Views, with text-link
  fallbacks, and detail pages link back to the parent;
- the page does not require method headings, an index, or authoring history;
- internal analysis and split reasons live in the workspace or checkpoint;
- the prose passes a reader-only review for purpose, participants, Information,
  and result without relying on the diagram or method vocabulary;
- no duplicated `model.md` remains merely as hidden storage;
- Mermaid visual language and source validation still follow the authoring
  Skill.
