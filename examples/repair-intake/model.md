# Repair intake — working model

## Modeling question

How does a repair request become a bookable repair without hiding missing-information rework?

- Reader: customer-support and repair-operations participants.
- Boundary: repair intake, before physical repair begins.
- State: current-state synthetic example.
- Context reading: the left-to-right arrows show value and information handoffs from the customer through intake and scheduling to the repair team.
- Flow reading: read from receiving a request to booking the repair, following the labeled decision branches.

## Candidate inventory

- Actors: customer; repair team; intake coordinator (unresolved).
- Business activities: receive repair request; request missing details; book repair.
- Information: repair request; intake record; repair booking.
- External systems: scheduling service.
- Implementation details omitted from the first model: email channel; form fields; notification mechanism.
- Unresolved: whether the intake coordinator must appear as an actor depends on whether internal responsibility is part of the discussion.

## Selected views

- [Overview working view](overview.md)
- [Context working view](context.md)
- [Flow working view](flow.md)
- [Model-set trace](model-set-index.md)

Each working view contains one Mermaid block for immediate preview. No standalone `.mmd`, SVG, or PNG is required during the modeling loop.

## Text alternative

The customer passes a repair request into intake. Intake creates a record, scheduling turns it into a repair booking, and the repair team receives that value. The flow then checks completeness, requests missing details, and rechecks when necessary.

The overview places intake before repair and return. The context expands the stable overview node `b_manage_intake`; the detailed flow expands `b_receive_request` inside that context. If detailed intake work reveals that booking belongs to repair execution rather than intake, revise the boundary upward in the overview.

## Assumptions and omissions

- The scheduling service is outside the selected repair-intake responsibility boundary.
- Repair booking is visible in the value context so the receiving repair team and the outcome of intake are explicit.
- The example does not assert which channel carries missing-detail requests.

## Next discussion question

Is scheduling an outside service that completes intake, or part of the repair team's work?
