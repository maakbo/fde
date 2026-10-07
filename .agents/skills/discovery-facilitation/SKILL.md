---
name: discovery-facilitation
description: Turn loose descriptions of real work into a grounded Discovery decision: what problem matters, what work should be removed or changed first, whether AI is appropriate, and what should move into Definition.
---

# Discovery Facilitation

Use this Skill when the user wants to improve real work, identify a useful AI / automation opportunity, decide what to change first, or move from a loose field description toward the first stage of the FDE delivery process.

This Skill does not assume that AI is the answer. Its purpose is to find the most meaningful change target and produce a grounded handoff into Definition.

## One-line entry

When the user says something as short as 「この業務を改善したい」, start Discovery immediately. Do not ask the user to invoke a longer prompt, fill out a template, or name the 5D stage. Ask one natural opening question, such as 「今、どんな仕事で困っていますか？」, and continue one question at a time. Work toward the Discovery Brief incrementally; do not expose the full checklist at the outset. The user can provide context naturally over several turns.

## Core contract

- Start from ordinary language. Do not require the user to fill a form before making progress.
- Understand the work before selecting technology.
- Use the business-context-modeling Skill when the work is not yet visible enough to discuss actors, activities, information, systems, decisions, or boundaries.
- Reconsider the work itself before automating it. Do not automate waste.
- Separate observed facts, user judgments, hypotheses, and unknowns.
- Prefer evidence and concrete examples over generic best practices.
- Do not invent pain points, volumes, risks, legal requirements, or ROI.
- Treat Human / rule / RPA / AI Agent / existing-system change as alternative intervention modes, not as a maturity ladder.
- A high-impact problem with weak evidence stays a hypothesis.
- The result of Discovery is a decision surface and a Definition handoff, not a full solution design.

## Workflow

### 1. Hear the field story

Let the user describe the work in their own language.

Extract only what is actually present:

- purpose / desired outcome;
- people involved;
- major activities;
- information used or produced;
- external systems;
- observed friction;
- decisions and exceptions;
- current measures or evidence;
- known constraints.

If the work is still hard to see, use business-context-modeling to create the smallest useful Business Story / Context / Flow before continuing.

### 2. Reconsider the work before automating it

For each meaningful activity or friction point, ask whether the work can be:

- removed;
- combined;
- reordered;
- simplified.

Use ICRS as a thinking lens, not as a mandatory public label.

Do not carry a task forward merely because it exists today.

### 3. Identify the bottleneck

Look for the part of the work that most limits the desired outcome.

Evidence may include:

- elapsed time or waiting;
- repeated rework;
- frequent mistakes;
- handoff friction;
- dependence on one experienced person;
- repetitive low-value effort;
- inconsistent judgment;
- inability to scale;
- inability to respond to change.

Do not choose the easiest-to-automate task if it is not the meaningful bottleneck.

### 4. Generate intervention candidates

For each candidate bottleneck, consider the smallest plausible intervention:

- stop / remove the work;
- simplify the process;
- clarify a rule or responsibility;
- improve information quality;
- change the existing system;
- use deterministic automation / RPA;
- use an AI assistant;
- use an AI agent with bounded autonomy;
- leave the work primarily human.

Do not design the solution in detail yet.

### 5. Assess candidates

Assess each candidate qualitatively from evidence available now.

Use four lenses:

- Impact — if this changes, how much does the desired outcome improve?
- Feasibility — are the required data, knowledge, systems, skills, and operating conditions available?
- Risk — what could go wrong operationally, legally, ethically, or organizationally?
- AI fit — does the work benefit from language understanding, context-sensitive judgment, exception handling, or tool use?

For AI fit, explicitly look for reasons not to use an AI agent, such as:

- legally required perfect correctness;
- empathy / relationship as the core value;
- data that cannot be exposed to the available AI environment;
- physical manipulation as the core work;
- deterministic rules being sufficient;
- cost or risk exceeding likely benefit.

Do not calculate a numeric score unless the underlying measurements are available and meaningful. Prefer High / Medium / Low with a short evidence statement.

### 6. Select the first target

Choose one first target when the evidence supports it.

State:

- what is being changed;
- why this target matters now;
- why other candidates are not first;
- the likely intervention mode;
- what evidence is still missing;
- what would cause the target to be reconsidered.

If evidence is insufficient, the correct output may be a field-observation task rather than a selected AI use case.

### 7. Hand off to Definition

Discovery is complete enough to move forward when the team can discuss:

- the selected business scope;
- the problem / bottleneck;
- the intended outcome;
- the leading intervention hypothesis;
- important exclusions;
- known constraints;
- the evidence behind the choice;
- unresolved questions.

Do not jump to prompt, RAG, MCP, schema, or implementation detail before this handoff is stable enough to support them.

## Output contract

Create a compact Discovery Brief using templates/discovery-brief.md.

The brief should contain:

1. Purpose / desired outcome.
2. Current work in plain language.
3. Observed friction and evidence.
4. Work to remove / combine / reorder / simplify.
5. Bottleneck hypothesis.
6. Intervention candidates.
7. Impact / feasibility / risk / AI-fit comparison.
8. Selected first target or observation task.
9. Non-targets.
10. Evidence, assumptions, and unknowns.
11. Definition handoff.
12. One field-test instruction.

Keep the main brief readable without requiring the user to understand 5D terminology.

## Field-use loop

field story -> visible work -> reconsider work -> find bottleneck -> compare interventions -> choose first target -> Definition -> field evidence -> revise

After field use, capture what was hard:

- questions the user could not answer;
- information that was missing;
- categories that felt unnatural;
- a decision that the brief failed to support;
- a case where the selected intervention was wrong.

Use that evidence to refine this Skill, its template, or the underlying business-modeling capability.
