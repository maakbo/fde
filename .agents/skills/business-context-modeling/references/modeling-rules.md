# Business modeling rules

## Element types

| Type | Meaning | Naming | Exclude when |
| --- | --- | --- | --- |
| Actor | Person, role, organization, or party participating in work | Short role noun | Responsibility is irrelevant to the question |
| Business activity | Meaningful work unit producing an observable outcome | Short verb phrase | It is only a click, screen action, or technical job |
| Information | Business object received, referenced, changed, or produced | Short domain noun | It is merely a format, folder, or transport |
| External system | Technical system outside the chosen responsibility boundary | Short system noun | It is internal or its product name adds no meaning |

Classify from the selected boundary, not an absolute ontology. An outside company remains an actor; use external system only for software or technical systems.

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

Diagnostic smells:

- An actor connected directly to many systems may indicate an access-architecture question.
- Information connected only to systems may hide the business purpose.
- Activities connected only to activities may hide actors or business objects.
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
