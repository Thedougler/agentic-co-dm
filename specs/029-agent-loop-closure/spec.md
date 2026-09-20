# Feature Specification: Agent Loop Closure

**Feature Branch**: `029-agent-loop-closure`

**Created**: 2026-09-20

**Status**: Draft

**Input**: User description: "Make the capability graph established by 028 reliably converge through fresh owner-relative observations, meaningful progress, stall detection, validated completion, and specific evidence-backed blockers without introducing another orchestration layer."

## Classification and Scope

- **work_class**: `agent-system`
- **route**: `full-sdd`
- **Objective**: Ensure every repeated owner-capability iteration begins from a fresh observation, advances owner-relative evidence or state, and terminates at the owner's completion guard or a specific blocker.
- **User value**: The DM receives complete, validated Work without wasted loops, lost objectives, read-route mutation, duplicate finalization, or false completion.
- **In scope**: Completion-guard coherence; baseline and replay trajectories; common capability-loop semantics; deterministic progress evidence where an existing operation already owns both observations; convergence behavior for the named query, context-pack, lint, ingest, capture, update, session-planning, place, and run-guide owners; trajectory-focused evaluation; paired promotion evidence.
- **Out of scope**: A new orchestrator, workflow engine, loop ledger, progress command, persistent execution state, global iteration policy, changes to outer harness safety limits without evidence, broad skill normalization, unrelated templates or validation rules, and campaign-content changes.
- **Canon impact**: Campaign canon remains unchanged. This feature changes agent operating behavior, owner completion guards, observation evidence, and evaluation coverage.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Close Every Capability Branch (Priority: P1)

As a DM requesting Co-DM work, I want each capability branch to continue only while it makes meaningful progress so that successful work finishes with validated output and unsuccessful work stops with a useful blocker.

**Why this priority**: Convergence is the feature's core value. All owner-specific behavior depends on a reliable common transition rule.

**Independent Test**: Run cold success and deliberately stalled jobs through representative read, write, ingest, maintenance, and parent/child loops; verify each branch ends at its owner completion guard or a specific blocker without repeating an equivalent action against unchanged evidence.

**Acceptance Scenarios**:

1. **Given** an incomplete owner contract and a fresh observation, **When** an owner-sanctioned action changes required state, evidence, dependencies, validation, or the diagnostic, **Then** the branch may continue from a new observation.
2. **Given** the same observation after an action, **When** the identical action would be repeated, **Then** the agent chooses a materially different owner-sanctioned path or returns a specific blocker.
3. **Given** an owner completion guard has not passed, **When** prose or a child response merely claims completion, **Then** the branch remains incomplete.
4. **Given** a branch cannot succeed, **When** no sanctioned path can change its observation, **Then** it terminates with the owner, affected artifact or scope, surviving evidence, and blocker.

---

### User Story 2 - Preserve Correct Guards and Scope (Priority: P1)

As a maintainer, I want loop entry and completion guards to agree with current authority so that a convergent loop cannot reliably finish on the wrong condition or mutate outside its requested scope.

**Why this priority**: Loop controls amplify whatever guard they are given; contradictory guards must be corrected before baseline or promotion evidence is trustworthy.

**Independent Test**: Exercise read isolation, scoped maintenance, faction filing, and user-said canon filing against their current authoritative contracts and verify the named contradictions are absent.

**Acceptance Scenarios**:

1. **Given** a read-only wiki query, **When** it completes, **Then** canonical pages, manifests, indexes, and logs remain unchanged.
2. **Given** a selected lint scope, **When** observation, deterministic repair, and re-observation run, **Then** every phase preserves that same scope; whole-vault repair occurs only for a whole-vault request.
3. **Given** a faction page reaches Done, **When** its path is checked, **Then** the current faction owner path is accepted and the legacy path is not required.
4. **Given** the user states canon during place work, **When** filing is required, **Then** the current immediate-filing rule applies without a separate acceptance wait.

---

### User Story 3 - Converge Deterministic Maintenance (Priority: P1)

As a wiki maintainer, I want repair operations to expose a compact before/after observation and avoid retrying unchanged repairs so that maintenance advances through findings or stops precisely.

**Why this priority**: Maintenance already has deterministic observations and repairs, making it the strongest first proof that semantic stall detection works.

**Independent Test**: Run scoped lint cases where a fixer resolves a finding, skips an unsupported finding, and leaves a semantic finding unchanged; verify the resulting trajectory advances, changes strategy, or blocks without duplicate equivalent repair.

**Acceptance Scenarios**:

1. **Given** a deterministic repair changes the worklist, **When** post-repair observation completes, **Then** the result exposes before and after totals, resolved findings or rules, changed files, next-target change, and whether state changed.
2. **Given** a deterministic fixer reports skipped or unsupported and the finding remains identical, **When** the loop continues, **Then** that fixer is not invoked again for the same observation.
3. **Given** semantic owner repair leaves the same finding, **When** the page is reconsidered, **Then** the surviving evidence and current owner contract are reread before a materially different action or blocker.
4. **Given** no sanctioned action can change a finding, **When** the file closes, **Then** the blocker identifies path, rule, evidence, owner, and reason.

---

### User Story 4 - Deepen Retrieval Without Spinning (Priority: P2)

As a DM asking a question or requesting a context pack, I want retrieval to deepen only when it adds relevant evidence so that answers remain grounded without repeated equivalent searches.

**Why this priority**: Read loops must gather enough evidence while preserving read isolation and bounded context.

**Independent Test**: Run first-page, one-deepening, and unchanged-candidate cases for query and context-pack owners; verify evidence sufficiency, non-mutation, and no duplicate equivalent retrieval.

**Acceptance Scenarios**:

1. **Given** the first retrieved page supports the answer, **When** sufficiency is evaluated, **Then** synthesis begins without unnecessary deepening.
2. **Given** current evidence is insufficient and a focused unexplored path remains, **When** retrieval deepens, **Then** the new iteration adds supporting, conflicting, or gap evidence.
3. **Given** an equivalent retrieval returns the same evidence from an unchanged candidate set, **When** another iteration is considered, **Then** the same retrieval is not repeated and the branch either changes strategy or reports the evidenced gap.
4. **Given** read work discovers a potentially useful edit, **When** the answer completes, **Then** canonical state remains unchanged.

---

### User Story 5 - Resume Parent Work After Bounded Handoffs (Priority: P2)

As a DM requesting composed session or place work, I want child capabilities to return bounded evidence that changes the parent's unresolved state so that dependencies close without recursive redelegation or objective loss.

**Why this priority**: Parent/child loops cross capability boundaries and are vulnerable to incomplete returns, irrelevant context inheritance, and repeated entry into the same seam.

**Independent Test**: Run session planning, place design, and run-guide cases with complete, incomplete, and stalled child returns; verify parent resumption, dependency tracking, context reset, and final owner completion.

**Acceptance Scenarios**:

1. **Given** a child completes a required dependency with evidence, **When** control returns, **Then** the parent's dependency set or artifact state changes and the original objective resumes.
2. **Given** a child return lacks required completion evidence, **When** the parent re-observes, **Then** dependent work does not advance.
3. **Given** re-entering the same child seam would not change dependency, artifact state, or completion evidence, **When** no different sanctioned action remains, **Then** the parent returns a specific blocker instead of redelegating recursively.
4. **Given** context is compacted between iterations, **When** the parent resumes, **Then** the original objective and unresolved dependencies survive while unrelated child context does not return.

---

### User Story 6 - Finalize Bounded Write Work Once (Priority: P2)

As a maintainer, I want ingest, capture, and update loops to advance bounded source and destination work and finalize exactly once so that every source is accounted for without duplicate tracking or refresh work.

**Why this priority**: Multi-artifact writes can appear complete several times as children finish; duplicate finalization corrupts evidence and wastes work.

**Independent Test**: Run representative multi-child ingest, capture, and update jobs; verify unprocessed work shrinks, every destination closes, validation runs at the required boundary, and tracking/finalization occurs once.

**Acceptance Scenarios**:

1. **Given** bounded source material and destinations, **When** an iteration completes, **Then** unprocessed material shrinks, a destination closes, validation advances, or a more specific blocker appears.
2. **Given** several children complete, **When** the parent reaches finalization, **Then** tracking and retrieval refresh each occur exactly once after all required destinations validate.
3. **Given** a child fails without changing its diagnostic, **When** documented recovery is exhausted, **Then** the operation stops with a specific blocker rather than consuming the outer runtime budget.

---

### User Story 7 - Promote from Paired Trajectory Evidence (Priority: P3)

As a project owner, I want baseline and replay evidence for the same representative jobs so that convergence changes are promoted only when they preserve quality and eliminate spinning.

**Why this priority**: Outcome and trajectory evidence are needed to distinguish real convergence from merely shorter or differently ordered execution.

**Independent Test**: Capture pre-change and post-change trajectories for at least ten comparable cases, including success and deliberate stalls, then evaluate hard gates, semantic quality, duplicate actions, and termination reasons.

**Acceptance Scenarios**:

1. **Given** the 028 behavior before loop changes, **When** representative owner jobs run cold with the weakest sufficient executor, **Then** outcome and required trajectory metrics are recorded through existing evaluation infrastructure rather than the error ledger.
2. **Given** the new behavior, **When** the same jobs replay, **Then** no new hard-gate failure, parent-objective loss, duplicate finalization, read-route mutation, or outer-budget stall occurs.
3. **Given** a token-improvement claim, **When** paired evidence is assessed, **Then** at least ten comparable cases show semantic non-inferiority and meet the existing median trajectory-token threshold.
4. **Given** no token-improvement claim, **When** promotion is assessed, **Then** correctness and convergence gates still apply without requiring token reduction.

### Edge Cases

- A tool fails transiently, its documented fallback produces a different diagnostic, and a later retry succeeds.
- A fallback returns the same terminal failure with no new recovery evidence.
- Finding count stays constant while finding identity, rule, file, or next target changes.
- Finding count drops while a more severe owner-level finding appears.
- A creative owner adds a required section without changing deterministic lint counts.
- A child changes its artifact but does not satisfy its output contract.
- A child satisfies one dependency while discovering another real prerequisite.
- An action changes files outside the selected maintenance scope.
- The same retrieval phrase is used against a changed candidate set and therefore is not equivalent to the prior action.
- Compaction removes trajectory detail but must preserve the parent objective, unresolved dependencies, last observation, and last action outcome.
- The existing operation cannot expose a before/after delta without performing a second unrelated observation.
- Baseline execution reveals another completion-guard contradiction outside the named set; it is changed only when the conflict is demonstrated by evidence.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The capability authority MUST define the operating shape as route, observe, act, re-observe, then continue, hand off, complete, or block.
- **FR-002**: Every repeated owner-capability iteration MUST begin from a fresh observation of that owner's current boundary.
- **FR-003**: Progress MUST mean a change in required state, relevant evidence, unresolved dependencies, validation result, or diagnostic, interpreted relative to the current owner.
- **FR-004**: An agent MUST NOT repeat an equivalent action against an unchanged observation.
- **FR-005**: A stalled branch MUST take a materially different owner-sanctioned action, obtain different evidence, or terminate with a specific evidence-backed blocker.
- **FR-006**: Only the current owner's completion guard MUST close its branch.
- **FR-007**: The common loop rule MUST remain within the existing ephemeral Execution Graph and MUST NOT create durable loop state or another orchestration layer.
- **FR-008**: The root agent guidance MUST expose only a compact invariant and pointer to the canonical capability authority.
- **FR-009**: Wiki-specific guidance MUST point to the canonical capability authority where needed rather than duplicate common loop semantics.
- **FR-010**: Durable glossary additions MUST be limited to terms required to distinguish an iteration and its progress evidence; the existing Execution Graph definition MUST remain unchanged.
- **FR-011**: The query owner MUST complete without mutating canonical pages, manifests, indexes, or logs.
- **FR-012**: Lint observation, deterministic repair, semantic repair, and re-observation MUST preserve the selected scope.
- **FR-013**: Whole-vault lint repair MUST occur only when the selected scope is the whole vault.
- **FR-014**: The faction owner completion guard MUST use the current canonical faction path.
- **FR-015**: The place owner completion guard MUST follow immediate filing for user-said canon without a separate acceptance wait.
- **FR-016**: Before behavioral loop changes are measured, the named guard contradictions MUST be corrected and checked for focused coherence.
- **FR-017**: A pre-change trajectory baseline MUST cover query, context-pack, lint, ingest, session planning, place design, and run-guide owners using cold focused context and the weakest sufficient executor.
- **FR-018**: Baseline and replay records MUST include outcome, turns, tool calls, retrieval attempts, duplicate equivalent actions, capability handoffs, validation passes, trajectory tokens, and termination reason.
- **FR-019**: Baseline coverage MUST include both successful loops and deliberately stalled cases and MUST NOT be derived from the error ledger.
- **FR-020**: An existing deterministic operation that naturally owns both pre-action and post-action observations MUST expose compact progress evidence from those observations.
- **FR-021**: Lint repair progress evidence MUST include finding totals before and after, resolved findings or rules, changed files, whether the next target changed, and whether any state changed.
- **FR-022**: Progress evidence MUST be added to existing result surfaces when available; the feature MUST NOT add a separate progress command or loop ledger.
- **FR-023**: Health observation MUST retain ownership of maintenance action ordering.
- **FR-024**: A deterministic fixer that reports skipped or unsupported while leaving the finding unchanged MUST NOT be invoked again against that observation.
- **FR-025**: A semantic repair that leaves an identical finding MUST trigger rereading of the surviving finding and owner contract before a different action or blocker.
- **FR-026**: An unresolved lint blocker MUST identify the path, rule, evidence, owner, and reason no sanctioned action can progress.
- **FR-027**: Query and context-pack retrieval MUST deepen only while a focused unexplored path can add supporting, conflicting, or gap evidence.
- **FR-028**: Equivalent retrieval against an unchanged candidate set MUST NOT repeat.
- **FR-029**: Ingest, capture, and update iterations MUST advance bounded source or destination work, validation, or blocker specificity.
- **FR-030**: Tracking and retrieval finalization for a bounded write operation MUST occur exactly once after all required owned work closes.
- **FR-031**: Session planning, place design, and run-guide child returns MUST change a required dependency, owned artifact state, or completion evidence before the same capability seam may be entered again.
- **FR-032**: Incomplete child evidence MUST NOT permit dependent parent work to advance.
- **FR-033**: Parent resumption MUST preserve the original objective and unresolved dependencies while excluding unrelated child context.
- **FR-034**: Tool recovery MAY continue only when the observation or diagnostic changes or a documented fallback remains available.
- **FR-035**: Repeated terminal tool failure with no new recovery evidence MUST end in a specific blocker.
- **FR-036**: Trajectory evaluations MUST test premature completion, stalled retrieval, repeated deterministic repair, incomplete child return, parent resumption, duplicate finalization, transient tool failure, read/write isolation, and context reset after capability handoff.
- **FR-037**: Evaluation MUST grade observable outcomes and meaningful trajectory invariants without requiring one exact tool sequence.
- **FR-038**: A valid alternative strategy MUST pass when it preserves ownership, reaches the completion guard, and does not spin.
- **FR-039**: Promotion MUST use paired baseline and replay evidence for at least ten comparable cases.
- **FR-040**: Promotion MUST require zero new hard-gate failures, zero lost parent objectives, zero duplicate tracking or finalization, zero read-route canonical mutations, and specific blockers for every intentionally stalled case.
- **FR-041**: A trajectory-token improvement claim MUST also require semantic non-inferiority and the existing five-percent median improvement threshold.
- **FR-042**: Existing harness recursion, request, runtime, isolation, auto-continuation, compaction, and memory settings MUST remain outer safety bounds unless trajectory evidence demonstrates a required change.
- **FR-043**: Changes to additional owner capabilities MUST require an evaluation demonstrating a local loop failure not covered by the common rule.
- **FR-044**: Templates, campaign pages, unrelated validation rules, and unrelated skills MUST remain unchanged unless evaluation demonstrates they govern an in-scope failure.
- **FR-045**: The feature MUST preserve every 028 ownership, dependency, context-projection, capability-handoff, read-isolation, and observable-completion guarantee.

### Key Entities

- **Capability iteration**: One owner-relative cycle consisting of a fresh observation, an owner-sanctioned action, and re-observation of the same boundary.
- **Progress evidence**: Evidence that an iteration changed required state, relevant evidence, unresolved dependencies, validation, or diagnostic specificity.
- **Observation**: The current owner-relative evidence used to choose an action and later determine whether that action progressed.
- **Equivalent action**: An action with the same material target, inputs, and expected effect as an earlier action against the same observation.
- **Stall**: A state where the current path would repeat an equivalent action against an unchanged observation.
- **Specific blocker**: Termination evidence naming the owner and affected boundary, the surviving observation, attempted sanctioned paths, and why no remaining path can progress.
- **Trajectory record**: A redacted evaluation record of outcome, actions, observations, handoffs, validation, tokens, and termination for one representative job.
- **Progress delta**: A compact comparison produced by an existing operation that already owns both the before and after observations.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In representative cold evaluations, 100% of successful branches reach their owner's observable completion guard and 100% of unsuccessful branches terminate with a specific blocker.
- **SC-002**: Across the paired evaluation set, zero branches repeat an equivalent action against an unchanged observation.
- **SC-003**: Every intentionally stalled case terminates before consuming the outer harness request or runtime limit.
- **SC-004**: Read-route evaluations produce zero canonical page, manifest, index, or log mutations.
- **SC-005**: Scoped maintenance evaluations produce zero repairs or observations outside the selected scope.
- **SC-006**: Every evaluated deterministic lint repair exposes all required before/after progress fields, and no unchanged skipped or unsupported repair is invoked twice.
- **SC-007**: In parent/child evaluations, 100% of complete child returns change the parent's relevant dependency or artifact state, while zero incomplete child returns advance dependent work.
- **SC-008**: Multi-child write evaluations perform tracking and retrieval finalization exactly once per operation.
- **SC-009**: Across at least ten comparable baseline/replay cases, replay introduces zero new hard-gate failures, lost parent objectives, duplicate finalizations, or read-route mutations and preserves semantic quality.
- **SC-010**: If a token-efficiency improvement is claimed, the paired set achieves at least a five-percent reduction in median trajectory tokens with semantic non-inferiority; otherwise no token-improvement claim is made.
- **SC-011**: Review finds zero new orchestrators, workflow engines, persistent execution ledgers, loop ledgers, progress commands, universal iteration schemas, or proactive capability carve-outs.
- **SC-012**: A maintainer can determine the current observation, last action, progress evidence, unresolved dependency, and termination reason for every evaluated trajectory from its existing evaluation record.
- **SC-013**: All named completion-guard contradictions pass focused post-change scenarios before new loop behavior is promoted.

## Assumptions

- Feature 028 is the accepted baseline for capability ownership, minimum context projection, dependency ordering, capability handoffs, and completion guards.
- Existing capability, observation, validation, handoff, evaluation, and efficiency surfaces remain the foundation; this feature closes their loops rather than replacing them.
- Progress is owner-relative: deterministic counts are useful for maintenance, while creative owners may progress by completing required artifact state or resolving dependencies.
- A fresh observation may reuse an existing compact surface when its underlying state is known to be current; it does not require a new command.
- Equivalent actions are judged by material target, inputs, and expected effect, not superficial wording or tool-call identity.
- Existing outer harness bounds remain safeguards for escaped pathologies, not normal completion conditions.
- No fixed global iteration count is needed unless paired trajectory evidence demonstrates semantic stall detection is insufficient.
- Campaign canon and table-facing content are not changed by this feature.
- An accountable issue will be created or linked before implementation, as required by project governance.

## Dependencies and Authoritative Context

- **context_used**: User-provided 029 direction; project constitution v3.1.0; root agent context; `CONTEXT.md`; hybrid SDD contract; feature 028 specification and established capability-boundary model; current extension configuration and specification template.
- **context_omitted**: Campaign entity pages, session prose, unrelated skill bodies, unrelated templates, and full historical error-ledger content because this specification governs agent-system convergence rather than campaign canon or a general cleanup.
- **Canonical owners**: Hybrid SDD capability-composition authority for common loop semantics; root agent context for the compact invariant and routing pointer; wiki agent context for wiki semantics; individual owner guidance for owner-relative observation, progress, and Done; existing CLI contracts for deterministic observation results; existing evaluation and efficiency infrastructure for trajectory evidence.
- **Dependencies**: Accepted feature 028 behavior; current scoped query, lint, health, ingest, capture, update, session planning, place, and run-guide owner contracts; an accountable issue before implementation.

## Named Failure Modes and Evidence

- **Loop repeats unchanged work** → User Story 1; FR-002–FR-006; SC-001–SC-003.
- **Convergence targets a contradictory guard** → User Story 2; FR-011–FR-016; SC-004–SC-005 and SC-013.
- **Scoped repair expands to the whole vault** → User Story 2 scenario 2; FR-012–FR-013; SC-005.
- **Read route mutates canonical state** → User Stories 2 and 4; FR-011 and FR-027–FR-028; SC-004.
- **Deterministic fixer spins on unsupported finding** → User Story 3; FR-020–FR-026; SC-006.
- **Retrieval repeats unchanged candidates** → User Story 4; FR-027–FR-028; SC-002.
- **Child return loses parent objective or advances without evidence** → User Story 5; FR-031–FR-033; SC-007.
- **Write finalizes more than once** → User Story 6; FR-029–FR-030; SC-008.
- **Tool recovery consumes outer budget** → User Story 6 scenario 3; FR-034–FR-035; SC-003.
- **Evaluation overfits one exact tool sequence** → User Story 7; FR-036–FR-038; SC-009.
- **Efficiency claim sacrifices quality** → User Story 7; FR-039–FR-041; SC-009–SC-010.
- **New orchestration state duplicates the Execution Graph** → FR-007–FR-010 and FR-022; SC-011.
- **Scope spreads to unrelated owners or artifacts** → FR-043–FR-044; SC-011.
