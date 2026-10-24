---
name: ai-pilot-evaluation
description: Design and review a bounded AI-assisted work trial with evidence for quality, adoption, and business effect, then decide continue, revise, stop, or prepare operations. Use after a target is known or when a PoC works technically but its field value is unclear; not as deployment authorization.
---

# AI Pilot Evaluation

Turn a desire for AI into a testable decision. Use the existing Issue, PR, or
project record; `templates/ai-trial-brief.md` is optional support, not an intake gate.
Read [governance-and-use.md](references/governance-and-use.md) when defining inputs,
permissions, specialist review, or operational readiness.

## Facilitate the trial

1. **Recover the problem.** State whose work should change, current workaround,
   intended outcome, and what remains uncertain: technical feasibility, field
   fit, or realized effect. Use Discovery when the target is not grounded and
   Definition when observable behavior or responsibility is unclear. Distinguish
   AI assisting developers from an AI feature in a delivered product.
2. **Inspect evidence.** Read available documents, elicit actual decisions, and
   walk normal and exception cases. Use `knowledge-stewardship` when missing,
   conflicting, stale, or inaccessible knowledge prevents the test. Do not make
   a prototype stand in for understanding the user's work.
3. **Choose one testable scope.** Compare importance, data/readiness, resources,
   failure consequences and reversibility. State the hypothesis, exclusion,
   comparison method, allowed actions, stop and recovery path, owner and decision
   point. A prototype is a minimal artifact, a PoC tests an uncertainty, and an
   MVP delivers a smallest usable scope; names alone establish no readiness.
4. **Define success from effect backwards.** State the desired business effect,
   what people must be able and willing to use for it to occur, then the quality
   necessary to support that use. Record current evidence, target or TBD, method,
   assessor, denominator and time window. Do not import sample thresholds.
   - Quality: representative behaviors, omissions, false alarms, critical errors,
     latency, review burden and cost where relevant. Compare to current work and
     error consequences, not an arbitrary overall accuracy percentage.
   - Adoption: eligible opportunities, actual use, abandonment/reasons, field
     observations and participant explanation. Short trials can use both counts
     and qualitative feedback; a click or forced use is not meaningful adoption.
   - Effect: keep whose work changes explicit. For AI-assisted development,
     measure the development handoff; product users' search or business outcomes
     are a different hypothesis unless explicitly included. Do not switch scope
     when naming a convenient metric.
     Outcome, rework, waiting, human effort including correction and
     maintenance, and downstream quality. Capture a baseline before the trial
     when possible. If absent, record it as missing and plan how to obtain it.
     Before/after differences alone do not establish causal attribution.
     For each measure name observation frequency and the action/owner when it
     worsens; include small qualitative handoff friction, not just totals.
5. **Agree evaluation cases before tuning.** Keep input, source version, expected
   evidence/behavior, assessor, observed result and failure severity. Include
   normal, exception, unavailable evidence, conflict, access denial and relevant
   harmful error classes. Reserve different conditions for forward evaluation;
   do not tune only on the example then call it general success. Use synthetic
   or already authorized data, and separate expected results from measured runs.
6. **Build and run only what tests the uncertainty.** Use a desk walkthrough,
   read-only retrieval, draft-only assistant, or minimal prototype as appropriate.
   Record actual environment, version, input and result within permitted data
   retention. API/schema checks, executed software tests, model evaluation,
   desk simulation and workplace use are different evidence. Missing permission
   stops dependent actions, not preparation of the reviewable plan.
7. **Review three layers and diagnose.** First see whether required quality holds,
   then whether it fits actual use, then whether the outcome improved. These are
   lenses, not a guaranteed causal ladder. Diagnose wrong output, cumbersome UX,
   mismatched workflow, or trust/organizational concerns without blaming users.
   Retrieve/generate failures go back to the knowledge procedure; changed scope
   or responsibility returns to Definition/Context/Flow. Keep unacceptable risks
   visible even when average scores improve.
8. **Decide and carry the work forward.** Return continue, revise and retest,
   pause for evidence, or stop/use an alternative, with reason and owner. No
   single metric overrules safety/rights or resolves a missing authority. When
   ready for limited operations, check data access, service identity, integration,
   load/performance, failure/monitoring, stop/recovery, training/support and
   maintenance owners separately. A successful PoC does not authorize rollout.
   Plan ongoing observation and re-evaluation when data, model, purpose, or policy
   changes; retain rollback and return-to-human work where needed.

When people need an introduction plan, new responsibilities, practical learning
or support, use [team-adoption-facilitation](../team-adoption-facilitation/SKILL.md).
Preserve the same scope and evidence. Do not turn a technical pass into adoption,
or use AI activity counts as an employee performance judgment.

Use [operational-learning.md](references/operational-learning.md) for sandbox vs
pilot decisions, failure-to-retest, Go/No-Go/Pivot, operational handoff, rollout
vs changed-scope scaling, and turning observed work into maintained knowledge.
Carry actual evidence and limits into the next decision, not just stage labels.

## Return the decision surface

Show scope, evidence for each layer, limits, governing constraints, decision,
next smallest test and one question participants can answer. Preserve their
reason for the work; do not replace it with maximizing AI usage. Publish no
organizational approval, business effect, or model capability you did not verify.

Use the [fictional development collaboration example](https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/agent-assisted-flow.md).
Follow host validation and independent reader/forward review for reusable Skills;
validate actual artifacts and observations, not merely template completeness.
