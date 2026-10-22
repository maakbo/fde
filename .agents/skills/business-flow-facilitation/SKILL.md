---
name: business-flow-facilitation
description: Turn a selected business activity and concrete work stories into a conversational business flow, separating task detail from the parent Context and comparing evidenced As-Is with proposed To-Be. Use for sequence, handoffs, decisions, exceptions, or rework after or alongside business-context modeling.
---

# Business Flow Facilitation

Help participants point to a step, correct it, and try a different way of working.
A diagram plus actionable dialogue is the output; a method description alone is not.

## Entry and grain

- Start from the work the user wants to discuss. Do not demand a completed Context
  or an intake form. If a Context exists, select the Business to expand and retain
  its file and stable ID. Otherwise create a provisional parent Business Story
  with `business-context-modeling`; keep its boundary unconfirmed until checked.
- Read [field-interview-and-grain.md](../business-context-modeling/references/field-interview-and-grain.md)
  for the purpose / Business / task distinction, concrete-case interviewing,
  5W1H, and As-Is / To-Be handling.
- Keep the parent's multiple Business activities at their outcome/responsibility
  level. Put operations and decision detail inside this selected Business's Flow
  or its task notes. A Flow must not silently join unrelated parent activities.
  If the question spans them, revisit the parent boundary first.

## Work through the conversation

1. **Frame one run.** Identify the trigger, first input, last output, recipient,
   state (observed current or proposed future), and question to resolve. An honest
   version zero is useful; distinguish evidence, reported behavior, assumptions,
   and unknowns in the workspace.
2. **Trace the case before drawing.** Use a compact step record: action, executor,
   input/output, decision owner/condition, next step, failure/return, evidence.
   Ask a focused question where ambiguity changes order, responsibility, or
   completion. Do not infer order from the Context's spatial placement or lines.
3. **Choose the level.** Name steps by meaningful actions. Keep clicks, filenames,
   shell commands, and keystrokes in task notes unless that operation is the
   actual question. Check each step's contribution to the selected parent output.
   If there are distinct outcomes or responsibilities, return upward or split
   into linked details; do not erase exceptions to fit a small diagram.
4. **Make the current Flow.** Use `mermaid-diagram-authoring` and its business-flow
   profile. Show the main route and the evidenced decision/return under discussion.
   Put executor, information, and completion criteria in nearby prose or a small
   table where icons cannot carry them. Keep unknown branches explicit in prose;
   do not invent a two-way rule to satisfy a checker. Choose a smaller evidenced
   segment when the full flow is not known. Source size limits are review signals
   to choose a focused child, not reasons to pretend a complex process is simple.
   When two outcomes are known but their later return/reconvergence is not, keep
   both in the conversation. The foundation checker requires a single final
   activity; never invent a return to satisfy it. You may show the honest branch
   as a provisional Mermaid draft and report that it does not yet pass that
   profile, alongside the specific missing question. Alternatively, provide
   linked, validated known-route segments and state the branching condition
   beside them. Do not call the partial picture the complete current Flow or
   omit an observed outcome without explaining the narrower scope. Finalize the
   governed source only after its real boundary/return is established.
5. **Walk it with the participant.** Ask a concrete question such as 「不足した時は
   この担当へ戻りますか、それとも受け取り直しですか」. Follow a normal example,
   then an exception. Change the source when corrected. If a new participant,
   Information identity, outcome, or responsibility appears, update the parent
   Context and reusable masters as applicable; preserve parent/child links.
6. **Explore the future separately.** When improvement is in scope, use ECRS and
   compare Human / rule / existing-system / AI alternatives. Check why controls
   exist before proposing removal. Record each change against current evidence,
   expected outcome, constraint, authority, and validation. Make a separate To-Be
   source with the same boundary and stable IDs for retained meanings; do not
   present an unagreed proposal as current practice.
7. **Test the proposed run.** Walk a normal case and an exception through both
   states. Check owner, information available at the decision time, wait/failure,
   return, and finish. If approval or data is unavailable, record the constraint
   and revise the smallest trial. Preserve the distinction between desk exercise,
   observed workplace use, and measured effect.

## Deliver and continue

Return the linked parent Context and Markdown Flow, necessary business prose,
state, the decision or unresolved point, and one question participants can answer
by pointing at the work. Do not wait until all questions are closed to show a
usable draft. Keep authoring evidence and change comparison in the workspace or
private checkpoint; reader pages explain the work and their state naturally.

Run the flow source checker, reader checker, and repository validation. Inspect
actual previews when rendering/review is authorized; do not claim visual review
from lint alone. Follow `reader-facing-artifact-review` for independent finishing.
Do not create fixed images during ordinary source authoring.

See the linked fictional [current](https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/development-flow.md)
and [proposed](https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/agent-assisted-flow.md)
development flows. They expand the implementation/unit-test Business of the
root Context; their responsibilities are example assumptions, not defaults.
