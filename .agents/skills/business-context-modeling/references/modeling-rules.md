# Business modeling rules

## Narrative grounding

Before making an element inventory, describe the chosen Business in two or three ordinary sentences. Say which Actors or External Systems provide which Information, how the Business uses it, which Information it creates or updates, and which Actors or External Systems receive it. Actor and External System are peer participant types when they occur; neither type is mandatory. Do not invent an unobserved External System merely to fill the inventory; record `none observed` and retain genuinely possible systems as unresolved. This is a relationship account, not a mandatory one-way process route; model time, decisions, and detailed order separately in a Business Flow.

Extract candidates only when they arise naturally from that description. Information should work as the object of a business verb such as receive, use as a basis, reference, create, update, or provide. Do not add `Model`, `View`, or another modeling-method concept merely because the method uses it; include it only when the described Business actually receives, uses, creates, updates, or provides it.

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

Foundation context lines mean relevant business relationships, not time order. Every line joins exactly one business activity and one actor, information item, or external system.

Describe providers, recipients, and Information relationships in companion prose. Keep the Business Context's ordinary lines as relationships, not a one-way route; detailed sequence belongs in a Business Flow.

When direction of value or Information handoff is itself the modeling question, use a value-flow context as a separate View variant: use `flowchart LR` with solid `-->` arrows, keep one Business activity as the hub, and include each provider, recipient, or External System only when observed. Its arrows mean handoff direction, not chronological order; detailed sequence, decisions, and rework belong in a Business Flow. State that reading in companion prose.

Diagnostic smells:

- An actor connected directly to many systems may indicate an access-architecture question.
- Information connected only to systems may hide the business purpose.
- Activities connected only to activities may hide actors or business objects.
- An activity with no visible value recipient may explain the work but hide why it matters; add the actor or business area receiving its output.
- Many edge labels may indicate vague nodes or mixed relationship meanings.
- One node connected to everything may make the subject too broad for discussion.

Use another general context view when information ownership, storage, access, or integration is the actual subject.

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
