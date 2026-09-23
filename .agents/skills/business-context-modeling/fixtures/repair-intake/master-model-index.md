# Repair intake master model index

These three files are the canonical element layer for the repair-intake
context. This index only links the masters and records their consumers.

## Master views

| Master | Role | Source | Context consumer |
| --- | --- | --- | --- |
| Actor map | actors and peer relations | [master-actor-map.md](master-actor-map.md) | [context.md](context.md) |
| External-system map | outside systems and integrations | [master-system-map.md](master-system-map.md) | [context.md](context.md) |
| Information model | conceptual information relations | [master-information-model.md](master-information-model.md) | [context.md](context.md) |

## Reconciliation note

Only one external system is currently observed, so its master is intentionally
sparse. Add another node only when the source or discussion provides evidence.
