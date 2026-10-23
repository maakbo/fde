---
name: workflow-design-facilitation
description: Turn a selected business flow into a testable human and agent workflow with automation boundaries, triggers, actions, typed handoffs, branches, review and restart conditions. Use when a flow must become executable work; not for drawing a business context alone or granting deployment rights.
---

# Workflow Design Facilitation

Make the next person able to run one agreed piece of work and judge its result.
Use the current Issue or work record; [workflow-brief](../../../templates/workflow-brief.md)
is optional support. A diagram alone and a list of tools are not an executable design.

## Choose the work and autonomy

1. **Recover one run.** Preserve its purpose, owner, input, final recipient, agreed
   conditions and exclusions. Use Discovery/Definition if these are unclear and
   [Business Flow](../business-flow-facilitation/SKILL.md) for order or handoffs.
   Keep proposed automation separate from current practice and product behavior
   separate from the team's development work.
   In a development handoff, name the parent as the team's requirements, design,
   implementation or review work. The product feature identifies its subject;
   the application's user activity does not replace that parent Business.
2. **Choose automation per action.** Compare occasional assistance, reusable
   task guidance, a predetermined workflow, and bounded agent planning. These
   can coexist in one process; a stage name does not confer tools or authority.
   Prefer the least complex arrangement that tests the needed value. State
   why more autonomy is useful, how it is contained, and what remains human.
   Trial thresholds come from consequence and current evidence, not a universal
   percentage. Read [automation-boundaries.md](references/automation-boundaries.md)
   for choices, tradeoffs and when to revise them.

## Turn the flow into contracts

3. **Choose a natural trigger.** Identify the business change or request first,
   then manual/chat/form, clock/deadline, event notification or polling. Record
   object and version, event/action, timing needs, eligibility and allowed scope.
   A webhook is a delivery mechanism for events; its arrival is not approval.
   Define identity, duplicate/late events, authentication and input trust where
   relevant. An example manual run is not an installed event integration.
4. **Specify each action.** Record owner (person, deterministic tool, model),
   inputs, evidence, permitted operation, output, validation, next consumer and
   stop/return. Separate obtaining data, interpreting/generating, and side effects;
   an API can do any of these. Arrange dependencies before notifying a recipient.
   Link related workflows through their output contract, rather than one giant flow.
5. **Make handoff values explicit.** For each value record name, meaning, source,
   expected type/allowed values, missing versus empty/false/zero, validator,
   lifetime, access and consumers. Distinguish one run's intermediate state from
   durable approved knowledge. Extracted or model-generated values are candidates
   until checked. Validate structure and business meaning separately.
6. **Walk every branch.** Distinguish yes/no choice, routing to one owner, and
   filtering each item. Define priority for overlapping conditions and an explicit
   unknown/default route. Missing evidence, no matches, invalid input, denied
   authority and tool failure need different meanings. Do not make low model
   confidence the only escalation condition or mistake high confidence for approval.
   Return an unmet requirement to its owner, not to a prompt that invents it.
7. **Prepare the worker's context.** Use Architecture's
   [task-context.md](../architecture-modeling/references/task-context.md) to select
   instructions, current sources, decisions, state, tool/environment constraints
   and output contract for this action. Carry the selected version through the
   result; after a source change reassess the affected decision and tests.

## Run, review and resume

8. **Specify completion and recovery.** State whether the action succeeded,
   needs input, awaits review, failed or was stopped. Give the named reviewer
   what to inspect, choices to accept/correct/return, and a next action. Define
   a checkpoint, allowed retries and a stop bound for transient failures; validate
   that repeating side effects is safe. Fixed workflows can retry and recover.
   Agent replanning is useful only inside the permitted purpose and actions.
9. **Test the design before expansion.** Fix normal/exception expectations, run
   one actual handoff, inspect returned evidence, then apply different conditions.
   Check missing/false values, unknown categories, overlapping branches, denied
   action, changed sources and a resumed run where relevant. Keep desk simulation,
   executed deterministic code, actual model use and field effect distinct.
   Correct the nearest contract/Skill and rerun the affected case. Use
   [AI Pilot Evaluation](../ai-pilot-evaluation/SKILL.md) for quality, adoption,
   effect and operations readiness, preserving remaining unknowns.

Return the linked work/flow, chosen automation and alternatives, trigger/action
contracts, value/branch rules, worker context, observed result, review/return and
next smallest run. Use Mermaid authoring if a new diagram helps participants;
do not invent transitions just to satisfy a profile. Follow host validation and
independent review for reusable work. This Skill adds no external messaging,
service setup, permission, model spend or rollout authority.

[A normal feature-development handoff](https://github.com/maakbo/fde/blob/main/examples/field-delivery/order-search/work-handoff.md)
