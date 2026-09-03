# Business modeling rules

## Narrative grounding

Before making an element inventory, describe the chosen Business in two or three ordinary sentences. Say which Actors or External Systems provide which Information, how the Business uses it, which Information it creates or updates, and which Actors or External Systems receive it. Actor and External System are peer participant types when they occur; neither type is mandatory. Do not invent an unobserved External System merely to fill the inventory; record `none observed` and retain genuinely possible systems as unresolved. This is a relationship account, not a mandatory one-way process route; model time, decisions, and detailed order separately in a Business Flow.

Extract candidates only when they arise naturally from that description. Information should work as the object of a business verb such as receive, use as a basis, reference, create, update, or provide. Do not add `Model`, `View`, or another modeling-method concept merely because the method uses it; include it only when the described Business actually receives, uses, creates, updates, or provides it.

## Information as business vocabulary

Information is a named domain concept used by people doing the work, not an
intermediate node invented to complete a diagram. For each candidate, ask:

- Can people naturally say they reference, check, update, or share it?
- Does it affect a judgment, responsibility, or value?
- Which Businesses create, update, reference, or provide it?
- Is the term observed in the Business Story, or derived only from the modeling
  method?

Maintain its stable ID, business term, plain definition, source evidence,
creating, updating, and referencing Businesses, recipients, and confidence in
the Information master companion. Reuse the same canonical identity across
Businesses and Contexts. A Context selects only relations relevant to its Use
Case; it does not create a local synonym.

An Information node connected only between two Businesses is a review smell,
not an error. If it is a real term in the work, retain it. If its only purpose
is to make the backbone continuous, remove it and use an observed direct
Business relationship instead. A perfectly alternating Business / Information
backbone deserves the same review.

## Semantic compression and identity

Natural-language source phrases are evidence, not automatic model labels. After extraction, ask what each candidate essentially is and propose a short, simple business name that remains meaningful at the view's abstraction level and can be concretized later. Reread the business description with the proposed name before confirming the inventory. Do not shorten a name until it becomes unclear.

A **rename** refines the expression of the same concept: retain its stable ID and record the previous label as an alias. A **split** marks a newly discovered difference in meaning: create new stable IDs and record their relationship to the former concept. A **merge** is allowed only when evidence shows candidates describe one concept at the same responsibility, state, boundary, and abstraction level; preserve the decision and absorbed identities instead of silently collapsing them.

## Business naming from transformation

Before naming a Business, state its input, the transformation it performs, and
its observable output. Compress the transformation into a short natural
business phrase and test whether it reads as a verb. Do not name the Business
after a method such as modeling, prototyping, or tuning unless that method is
itself the responsibility and outcome being modeled. Externalizing meaning as
a model may support every Business; it does not by itself define a separate
Business.

Keep the source phrase, input, transformation, output, proposed name, verb
reading, and confidence in the authoring workspace. Keep rename / split / merge
history there or in a private checkpoint. A reader-facing page normally needs
only the selected name and a short description of the transformation.

## Element types

| Type | Meaning | Naming | Exclude when |
| --- | --- | --- | --- |
| Actor | Person, role, organization, or party participating in work | Short role noun | Responsibility is irrelevant to the question |
| Business activity | Meaningful work unit producing an observable outcome | Short verb phrase | It is only a click, screen action, or technical job |
| Information | Business object received, referenced, changed, or produced | Short domain noun | It is merely a format, folder, or transport |
| External system | Technical system outside the chosen responsibility boundary that provides value or Information to, or receives it from, the Business | Short system noun | It is internal or its product name adds no meaning |

Classify from the selected boundary, not an absolute ontology. An outside company remains an actor; use external system only for software or technical systems. At the Business boundary, Actors and External Systems are peers as providers or recipients; they remain different types because Actors have purposeful action and responsibility, while External Systems mark technical responsibility boundaries.
Peer status does not require both types in every view.

## Abstraction ladder

Use one main level per diagram.

| Level | Question | Example |
| --- | --- | --- |
| Purpose / value | Why does the business exist? | Enable a safe purchase |
| Capability / area | What can the business reliably do? | Sell products |
| Activity / outcome unit | What meaningful work outcome occurs? | Receive an order |
| Procedure / task | How is the outcome produced? | Check stock |
| Operation / implementation | What action does a person or system execute? | Export CSV |

If connected activities are more than one level apart, rename them to peers or move the detail into another diagram.

## Grain tests

- Outcome: did the work produce something participants recognize?
- Responsibility: does it mark a useful ownership boundary?
- Decomposition: can it contain several tasks unnecessary to the current question?
- Peer: are sibling activities comparable in breadth?
- Removal: would removing it make the main reading false or only less detailed?

Merge nodes with the same actor, outcome, and discussion consequence. Split nodes with different outcomes, responsibility, or stakeholder disagreement.

## Relationship rules

One Business Context represents one Business Use Case or coherent business
scene. Its central backbone contains one or more sibling Business activities
that together make the Use Case work. Each activity has an observable outcome,
marks a useful responsibility, sits above procedure/task grain, and is broadly
comparable in size with its siblings.

Use spatial meaning before arrow direction:

- left: the Actor executing the Business, or an Actor / External System /
  Information item providing value or input;
- center: the Business backbone, made of sibling outcome-sized activities and
  any observed Information that meaningfully connects them;
- right: an Actor or External System receiving value, or Information created,
  updated, or provided by the Business.

Use `flowchart LR` and `---` for ordinary relations. List left-side nodes, then
Business activities and genuine shared Information according to their semantic
roles, then right-side nodes. Do not force a Business / Information
alternation. Write relations in the same approximate left-to-right source
order. This gives Mermaid a meaningful layout signal without fake edges; it
does not assert exact sequence.

When one Business creates or updates Information used by another, use
`Business A --- Information X --- Business B` if that Information is a real
business concept observed in the story. When continuity matters but no such
Information is observed, `Business A --- Business B` is allowed. It means a
business connection or handoff within the scene, not procedure order. Never
invent a bridge or a direct edge only to improve layout. Companion prose may
clarify value, but it must not compensate for meaningless placement.

Input/output or provider/recipient meaning alone never justifies an arrow. Use
`-->` only when direction is essential to the modeling question and placement
cannot carry it, such as a strong one-way dependency or derivation. Record why
placement is insufficient in the authoring workspace and use the explicit
checker exception. The former arrow-based “value-flow context” profile is
retired; its useful value reading is now the canonical spatial Business
Context. Sequence, decisions, and rework remain Business Flow concerns.

## Context boundary and splitting

Do not split because there is one Business activity, or because a fixed node
count was crossed. Split into sibling Contexts when:

- participant or stakeholder composition changes materially;
- value provider or recipient changes materially;
- Information or External System boundary changes materially;
- responsibility or ownership moves enough to create a distinct scene; or
- density, crossings, or backbone shape makes the discussion target hard to
  see.

Complexity thresholds are review signals. Semantic coherence and readability
make the final decision. If central activities have slipped into small steps,
keep the Context at outcome grain and expand one Business as a Business Flow.

Diagnostic smells:

- An actor connected directly to many systems may indicate an access-architecture question.
- Information connected only to systems may hide the business purpose.
- Activities connected only to activities may hide actors or business objects.
- An activity with no visible value recipient may explain the work but hide why it matters; add the actor or business area receiving its output.
- Many edge labels may indicate vague nodes or mixed relationship meanings.
- One node connected to everything may make the subject too broad for discussion.
- A two-Business bridge used nowhere else may be diagram glue rather than
  business vocabulary.
- An Actor connected only to the first or last Business may reflect endpoint
  layout rather than actual participation.
- If every Information has degree two on one path, or the backbone alternates
  mechanically between Business and Information, the diagram may be dictating
  the Model.

Use another general context view when information ownership, storage, access, or integration is the actual subject.

## Semantic audit before reusing a Context pattern

A common page structure helps readers navigate, but it does not justify a
common diagram structure. Before reusing an existing Context, set its diagram
aside and restate the Use Case story, Why, sibling Business activities, their
inputs, transformations, outputs, and each participant's responsibility. For
every Actor or External System, ask
what it provides, what it receives, and whether it participates directly in
this Business.

Create these matrices before Mermaid:

| Relationship model | Allowed values |
| --- | --- |
| Actor / External System × Business | executes, provides, participates, decides, receives value, none |
| Information × Business | create, update, reference, provide, none |

An Actor's left or right position expresses its primary value role across the
whole Use Case. Its individual Business relations express direct participation
and may span the backbone. Do not infer that a left Actor participates only in
the first Business or a right Actor only in the last. In a multi-Business
Context, an Actor attached only to one endpoint is a review smell that must be
checked against the participation matrix.

Then choose the Context contents from the meaning:

- use the canonical left/backbone/right Business Context for ordinary value,
  participation, comparison, and feedback relationships;
- use an arrow exception only when direction itself changes the answer and
  spatial placement is insufficient;
- do not draw every Actor as both provider and recipient merely because an
  earlier page did;
- do not duplicate one Actor identity on both sides as a layout workaround;
  revisit the boundary, modeling question, or grain when both roles are equally
  important;
- do not reduce a transfer of capability, responsibility, or ownership to an
  Information handoff;
- distinguish a Context of the work that designs collaboration from a Context
  of the resulting Actor / System topology. Do not invent the latter before
  concrete responsibilities and boundaries are observed.

Uniformity belongs to the reader-facing page pattern. Differences in Actor
count, Information count, relations, and semantic emphasis are expected when
the Businesses mean different things.

## Mermaid pressure

Accept Mermaid automatic layout as a modeling constraint. A crowded result can reveal hubs, clusters, crossings, and mixed concerns.

After observing it, consider:

1. keeping the full view because the complexity matters;
2. removing implementation detail;
3. replacing product names with business roles;
4. merging activities that truly share one outcome;
5. separating current from future;
6. separating relationship context from sequence;
7. adding focused views and a one-level-higher overview.

Preserve every extracted candidate and explain omissions in companion Markdown. Change medium only when essential complexity would otherwise be misrepresented.
