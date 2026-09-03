---
name: business-context-modeling
description: Turn loose business or operational language into purpose, business, actor, information, system, context, and flow models; name Business activities from their transformations; connect Why to How; and publish reader-facing model sets without exposing the authoring workspace.
---

# Business Context Modeling

Turn an ordinary conversation about work into a model people can inspect,
question, and refine. Keep the analysis rigorous behind the scenes and make the
published model quiet enough for a reader who wants to understand the business.

## Core contract

- Start from the user's language. Do not require a form before producing a
  first model.
- Work in two surfaces: an **authoring workspace** for evidence, candidates,
  classifications, comparisons, and unresolved questions; and a
  **reader-facing artifact** for the model, a short explanation, and links to
  related views.
- Keep project-specific decisions and open questions in the project's private
  checkpoint when one exists. Do not hide them inside a public sample.
- Preserve the trace from Why / Purpose through the desired outcome, Business,
  and Actor / Information / System relationships to How / Flow /
  implementation. Move both downward and upward as the model changes.
- Describe a Business's input, transformation, and output before naming it.
  Name the transformation, not a method merely used to perform the work.
- Treat modeling as a basic action across Business activities whenever meaning
  can be externalized. Do not confine it to one activity called modeling.
- Keep a Business Map of constituent capabilities separate from a Business
  Flow. A map shows composition or relationships; a flow shows order,
  decisions, and rework.
- Do not invent Actors, Information, External Systems, exchanges, or
  responsibilities to fill a notation.
- Keep Markdown Mermaid as the editable source. Do not create `.mmd`, SVG, or
  PNG unless the user explicitly requests standalone source or export.

## Reference routing

Read only the references needed for the task:

- [business-story-and-5w2h.md](references/business-story-and-5w2h.md): build a
  Business Story, use 5W2H as an analysis lens, and preserve the Why-to-How
  meaning trace.
- [modeling-rules.md](references/modeling-rules.md): extract candidates,
  classify Actor / Business / Information / External System, align grain, and
  name Business activities through semantic compression and transformation.
- [master-elements.md](references/master-elements.md): maintain canonical
  actor, external-system, and information maps when reusable identities or
  same-type relationships matter.
- [multi-view-modeling.md](references/multi-view-modeling.md): distinguish Model
  from View, choose Purpose / Map / Context / Flow views, and keep upward and
  downward trace.
- [reader-facing-artifacts.md](references/reader-facing-artifacts.md): separate
  the modeling workspace from a public sample and edit for business readers.

Use [mermaid-diagram-authoring](../mermaid-diagram-authoring/SKILL.md) for the
notation and source-only validation of each diagram.

## Workflow

### 1. Frame the work

Infer the purpose, first reader, business boundary, state, and the one question
the current View should answer. Ask at most one blocking question; make a
reviewable version zero when the language already supports one.

### 2. Build the Business Story in the workspace

Write a short natural-language account of who provides which Information, what
the Business changes, what it produces, and who receives or uses the result.
Use 5W2H to find missing meaning, not as a required public-page format. Follow
`business-story-and-5w2h.md`.

### 3. Extract and name

Preserve concrete source words, then classify the observed Actor, Business,
Information, and External System candidates. For each Business, state input,
transformation, and output; compress the transformation into a short natural
name; and test it as a verb. Record rename / split / merge decisions in the
workspace or private checkpoint, not in the reader-facing page.

### 4. Connect Why to How and choose Views

Keep the meaning chain behind the model. Publish only the Views that answer a
reader's question, such as:

- Purpose / Outcome: what state the work seeks;
- System Context: who participates around the whole Business;
- Business Map: which peer Business capabilities constitute the whole;
- Business Context: who and what relate around one Business outcome;
- Business Flow: what order, decision, or rework occurs inside one Context.

Do not make one diagram answer all levels.

### 5. Reconcile reusable elements

When actor, external-system, or information identities recur across Contexts,
reconcile them with the corresponding master map. Reuse stable IDs, labels,
icons, and sizes. If a relationship is not observed, keep it unresolved in the
workspace rather than drawing it.

### 6. Author and validate the working model

Use Mermaid as a discussion surface. Keep one subject, state, relationship
meaning, and main abstraction level per diagram. Run the matching source-only
checker. Let density or awkward layout send the work back to boundary, grain,
or naming before adding layout machinery.

### 7. Publish for the reader

Edit the agreed meaning into the reader-facing pattern:

1. a title that names the business question;
2. one or two short sentences;
3. the Mermaid diagram;
4. only the explanation the diagram cannot carry;
5. natural links to its parent, child, or supporting View.

Remove authoring history, candidate tables, method explanations, validation
notes, and private uncertainty from that surface. Follow
`reader-facing-artifacts.md`.

### 8. Garden knowledge and close

- Move reusable methods to this Skill or its nearest reference.
- Move project-specific decisions, unresolved items, and review state to the
  private checkpoint.
- Delete obsolete or duplicated public explanations instead of hiding them.
- Validate the repository, run `git diff --check`, and report exports only when
  they were explicitly requested.

## Output contract

Maintain three different outputs when the project needs them:

### Authoring workspace

Business Story, 5W2H notes, source evidence, candidate inventory, input /
transformation / output, naming decisions, boundary, assumptions, omissions,
unresolved questions, view trace, and validation results.

### Reader-facing artifact

The model diagram, a short business explanation, a short reading, and links to
related Models / Views. Do not require the reader to understand the modeling
method.

### Private checkpoint

Project-specific decisions, alternatives, rename / split / merge candidates,
review state, unresolved items, next action, and stopping point.
