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

This contract governs business model pages. A worked practice case may instead
follow a field question through evidence, decisions, execution and retesting,
linking the relevant model pages without copying their diagrams. Keep its
synthetic inputs, measured runs and unmeasured outcomes distinguishable. A case
does not become evidence of method quality merely by illustrating the method.

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

```mermaid
...
```

業務の目的、関わる人、扱う情報、次の仕事に渡る結果について必要な補足。
[親の業務を見る](parent.md) / [詳しい場面を見る](detail.md)
````

Use the ordinary business name or theme as the heading, put the diagram
directly below it, and explain only what the diagram cannot carry afterward. A page
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

## Business-owned working directories

When a reader needs to go one level deeper, link to the Business's directory
and its `README.md`, not to a flat collection of context files. The directory
is a working boundary for that Business: its README explains the scene, and
only the intermediate or final artifacts, tasks, records, supporting material,
or child Businesses that the work actually needs belong beside it. Do not
create empty `flows/`, `models/`, or `tasks/` buckets for appearance, and do
not make the reader pass through a catalog or index before reaching the child.
Keep the root-to-child link natural and return to the parent when a child
discovery changes the meaning.

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
- Before compressing or rewriting a purpose, distinguish the desired lived
  state from enabling capabilities and delivery methods. Keep the user's
  reason for changing the work, including organizational aims and participants'
  own intentions and circumstances. Do not silently replace it with efficiency,
  automation, visibility, or autonomous improvement. Carry the agreed purpose
  into target selection and outcome evaluation, not only the opening paragraph.
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

## Editorial and independent review

The visible pattern is `business/theme heading → diagram → necessary supplement`.
Do not add headings such as `モデル`, `このモデルが表していること`, `読み方`,
or `このページの構成`. Do not repeat the heading in Mermaid frontmatter `title`.
Use business names for real sections; substantive lists remain useful when
readers need to compare criteria or conditions.

Remove sentences that announce what the author will show, how the page is
organized, or which view comes next. Use natural Japanese about what participants
confirm, decide, do, and pass on. Avoid repeated introductions, rhetorical
contrasts, abstract promises, and restating every diagram relation in prose.
A relation view explains participants and information; its neighboring flow
explains order and decisions. Read adjacent sections together for duplication.

Maintenance intent such as scope, parent/expanded IDs, relation semantics,
omissions, and native layout constraints belongs in Mermaid `%%` comments.
Do not hide reader-relevant uncertainty or criteria in comments. Private
history and review logs stay outside the published page.

When pages are consolidated, preserve separate questions and make the business
context continuous. Removing a flow diagram does not remove the Businesses it
represents. Map each retained Business into the consolidated sections, keeping
its responsibility, handled Information, acceptance decisions, and rework.
Use real business subheadings when several Businesses belong to one scene;
do not collapse distinct work just to match the number of diagrams. Update links and validation/packaging assumptions rather
than retaining redundant pages solely because a checker expects them.

Use `reader-facing-artifact-review` when proofreading, consolidating, or finishing
reader pages. Resolve independent reviewer findings before closing when delegation
is authorized and available. A source checker cannot establish natural prose,
semantic preservation, or visual readability; report the evidence actually used.
