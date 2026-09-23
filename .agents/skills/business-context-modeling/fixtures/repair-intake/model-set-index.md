# Repair service model set

## Purpose

Connect the repair-intake boundary discussion to the wider repair service without flattening capability, activity, and task details into one diagram.

## View map

| View | Role | Level | Parent / expanded node | Child views | Focus | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [overview](overview.md) | overview flow | capability / business area | — | [context](context.md) | High-level handoff from intake to repair and return | working hypothesis |
| [context](context.md) | focused relationship context | business activity | `overview.md / b_manage_intake` | [flow](flow.md) | Relationships among intake inputs, outputs, scheduling, and recipient | working hypothesis |
| [flow](flow.md) | focused flow | task | `context.md / b_receive_request` | — | Completeness decision and missing-detail rework | working hypothesis |

## Master layer

| Master | Role | Canonical prefix | Source | Context consumer |
| --- | --- | --- | --- | --- |
| Actor map | participants and peer relations | `a_` | [master-actor-map.md](master-actor-map.md) | [context](context.md) |
| External-system map | outside systems and integrations | `x_` | [master-system-map.md](master-system-map.md) | [context](context.md) |
| Information model | conceptual information relations | `i_` | [master-information-model.md](master-information-model.md) | [context](context.md) |

See the [master model index](master-model-index.md) for the canonical layer and
its sparse-system note.

## Abstract to concrete

- `b_manage_intake` expands into the customer, repair request, intake record, scheduling service, repair booking, repair team, and `b_receive_request` activity.
- `b_receive_request` expands into receiving, checking completeness, requesting details, and booking.

## Concrete to abstract

- The intake details group under `b_manage_intake` because they share the outcome of producing a repair booking that the repair team can act on.
- If the detail shows that booking allocates repair capacity rather than merely completing intake, revise the overview boundary between `b_manage_intake` and `b_repair_item`.

## Open modeling question

Does scheduling complete intake, or begin repair execution?
