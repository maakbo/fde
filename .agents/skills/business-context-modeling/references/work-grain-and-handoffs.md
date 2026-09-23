# Work grain and handoffs

Use the words people at the site use. These distinctions are modeling tests, not mandatory labels in a reader-facing diagram.

| Lens | Question | Modeling treatment |
| --- | --- | --- |
| Work / 仕事 | Why does this scope exist, and who is accountable for its value? | State purpose, boundary, desired outcome, and accountable parties at the root. |
| Phase / 工程 | When or in which familiar stage is it encountered? | Use as a navigation index or tag; it is not a semantic parent of a Business. It can repeat, overlap, or be skipped. |
| Business / 業務 | What recognizable outcome is produced, using and changing which information, for whom? | Model as a verb-named activity with Actor, Information, and External System relations. Recursively decompose into child Businesses at the next useful grain. |
| Task / 作業 | What does someone concretely do to produce or verify that outcome? | Put instructions, commands, checks, exceptions, and evidence in a procedure or teaching sheet. A task is not automatically a Business node. |

The reader may enter through `work → phase → major Business`; retain a separate semantic trace `work → Business → child Business → task`. A Business can span phases. A phase can contain several Businesses, and a Business can recur in several phases. Do not assume phase order, ownership, or a fixed decomposition depth from a process label. Record phase memberships as an index and parent/child Business IDs as different relationships.

## Decide the grain

1. State the input, transformation, and observable output. If it changes a meaningful outcome or responsibility, test it as a Business.
2. If it is an execution step such as opening a console, running a command, recording evidence, or checking a result, keep it as a task under the Business it serves.
3. If a supposed Business only names a stage (`基本設計`, `導入`) ask what actually gets decided or made there. Preserve the stage term in navigation; use outcome verbs for child Businesses.
4. If a task hides a distinct decision, participant, information change, or escalation boundary, lift that part to a child Business and keep the operational steps below it.
5. Let one Business have multiple child Businesses and expand one child again when useful. Link each detail to the exact parent Business ID. Keep a phase tag separate from this trace.

## Model a transfer of responsibility

Begin with the reason for transfer and what must remain reliable for the users of the system. Record current state and intended state explicitly; do not silently treat a planned transfer as completed. Distinguish who **executes**, who **judges go/no-go or accepts the result**, who **can change the procedure**, and who **supports/escalates**. An executor change does not imply a decision-right change.

For each selected Business, gather only observed actors, source information, changed information, external systems, and recipient. A useful small matrix is:

| Business ID / outcome | Phase tags | Current executor / decider | Intended executor / decider | Referenced and updated information | Task and exception evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| observed ID | observed tags | observed roles | proposed roles | business terms | link to procedure | confirmed / hypothesis / unknown |

For teaching, take one actual case from trigger to completion: why it starts, inputs and prerequisites, who decides, live demonstration, expected result and evidence, failure/rollback path, escalation contact, and the receiving team performing it back while the current team observes. Mark access and authority prerequisites before a task is considered transferable. Record remaining support conditions and a clear acceptance criterion. Never invent commands, production identifiers, responsibilities, or checks from a generic example.

Keep confidential project facts in a private authoring workspace. Public samples must be synthetic and labeled as such. Publish only reader-facing purpose, diagram, short reading, and natural detail links; keep the detailed teaching sheet in the project workspace.
