# Multi-view business modeling

Master element maps are a parallel canonical layer, not another abstraction
rung: actor, external-system, and information views hold same-type identities
and relationships. Context and overview views select those IDs and record the
links in the model-set index. If a detail changes the meaning of an element,
revise the master first, then propagate the canonical label and ID to consumers.

## View roles

| View | Purpose | Typical level |
| --- | --- | --- |
| Complexity observation | Preserve the full same-level backbone for discussion | Activity or capability |
| Overview context | Relate areas covered by focused views | One level above children |
| Overview flow | Show high-level handoffs or order | One level above children |
| Focused context | Explain elements around one overview node | One level below parent |
| Focused flow | Explain order, decisions, or rework inside one activity | Activity or task |

Observation and overview are different. Observation preserves complexity at the current level; overview summarizes it at a higher level.

Move upward one rung at a time:

| Child | Parent overview |
| --- | --- |
| Operation or task | Activity or outcome unit |
| Activity | Capability or business area |
| Capability | Purpose or value concept |

Do not add another overview at the same level merely to reduce node count.

## Concrete to abstract

1. Preserve the candidate inventory and useful dense observation view.
2. Group details that share an outcome, responsibility, or boundary.
3. Name each group as one next-higher concept.
4. Choose relationship or handoff semantics and assign stable IDs.
5. Record which detailed views and concrete nodes each overview node summarizes.

Do not group items merely because Mermaid placed them near each other.

## Abstract to concrete

1. Select one overview node whose meaning needs discussion.
2. State a narrower question and boundary.
3. Expand it into a focused context.
4. Add a flow only when internal order or decisions matter.
5. Link the child to its parent diagram and exact parent node ID.

## Bidirectional trace

For every view, record level, role, parent and expanded node ID, children, one-sentence focus, and status. Keep the observation view while it remains meaningful evidence. Revise upward when detail changes a shared concept; descend when overview hides a disputed distinction.
