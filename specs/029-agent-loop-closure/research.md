# Research: Agent Loop Closure

## Decision 1: Close loops inside existing owner capabilities

**Decision**: Use one owner-relative invariant: observe the active owner boundary, choose an owner-sanctioned action, act, then re-observe the same boundary. Continue only when the owner completion guard passes or the new observation shows meaningful progress; otherwise choose a materially different sanctioned path or return a specific blocker.

**Rationale**: Feature 028 already defines owners, dependencies, completion guards, observation surfaces, and an ephemeral Execution Graph. The missing behavior is convergence, not orchestration.

**Alternatives considered**:
- New orchestrator, workflow engine, or persistent loop ledger: rejected because it duplicates the Execution Graph and owner authority.
- Fixed global iteration limit: rejected because valid creative work has owner-specific depth; harness limits remain escape safeguards.
- Universal runtime state schema: rejected because current owner contracts already expose the necessary evidence.

## Decision 2: Put the invariant in the existing authority chain

**Decision**: `docs/agents/hybrid-sdd.md` owns the complete cross-capability loop rule. `AGENTS.md` carries only the compact always-loaded invariant and pointer. `wiki/AGENTS.md` retains wiki semantics and points to the common rule. Individual owners state only local observation, progress, completion, and blocker details not supplied by the common authority.

**Rationale**: This preserves feature 028 layering and avoids repeated instructions. Shared behavior has one owner; local craft stays local.

**Alternatives considered**:
- Copy the full loop into every skill: rejected as context waste and drift risk.
- Move all owner procedure into the hybrid contract: rejected because it would flatten specialized owners.

## Decision 3: Correct contradictory guards before measuring behavior

**Decision**: Reconcile four confirmed contradictions before baseline/replay promotion:
1. `wiki-query` must not append canonical `log.md` during a read.
2. `wiki-lint` must preserve the selected path scope through observation, fix, and re-observation.
3. `faction-design` must accept the current `wiki/entities/faction/` owner path rather than require the legacy campaign faction path.
4. `place-design` must file user-said canon immediately under constitution X without a separate acceptance wait.

**Rationale**: A reliable loop aimed at a wrong completion guard converges to the wrong result. The current CLI contract and wiki authority already define the correct behavior.

**Alternatives considered**:
- Treat contradictions as evaluation exceptions: rejected as proactive carve-outs.
- Preserve both old and new guards: rejected because dual authority prevents observable completion.

## Decision 4: Add deterministic progress to `wiki lint fix`

**Decision**: Extend the existing `scripts/wiki lint fix` result with one compact `progress` object computed from its existing pre-fix and post-fix worklists. It contains before/after finding totals, resolved finding identities or rules, changed files, whether `next` changed, and whether state changed. Update the 027 CLI contract and focused CLI tests with the public behavior.

**Rationale**: `lint fix` already owns scope resolution, the pre-observation, safe repair, atomic mutation, and same-scope post-observation. It can compute a truthful delta without new storage or commands.

**Alternatives considered**:
- Add a `wiki progress` command: rejected because it would duplicate existing observations.
- Put the delta in `health`: rejected because health observes once and owns ordering, not an action boundary.
- Persist progress records: rejected because trajectory state remains ephemeral or evaluation-local.

## Decision 5: Treat unchanged actions semantically, not by tool identity

**Decision**: An action is equivalent when its material target, inputs, and expected effect are unchanged against the same observation. A deterministic skipped/unsupported repair is not invoked again for that observation. An unchanged semantic finding triggers rereading the surviving finding and owner contract before a different action or blocker. Tool recovery continues only when the diagnostic changes or a documented fallback remains.

**Rationale**: Exact command comparison misses paraphrased repetition, while exact tool-sequence grading rejects valid strategies.

**Alternatives considered**:
- Compare tool call strings: rejected as too brittle and too weak.
- Retry every failure until the harness limit: rejected because outer limits are not completion behavior.

## Decision 6: Deepen retrieval only into unexplored evidence

**Decision**: Query and context-pack owners continue retrieval only while a focused unexplored path can add supporting, conflicting, or gap evidence. An unchanged candidate set cannot receive an equivalent retrieval action twice. Reads leave canonical pages, manifest, index, and log unchanged; permitted derived command timing remains governed by the CLI contract.

**Rationale**: Existing QMD-first and bounded context-pack protocols already expose candidate evidence. The required change is an explicit stop/change-path rule and trajectory coverage.

**Alternatives considered**:
- New retrieval planner: rejected because owner retrieval protocols already select and deepen evidence.
- Logging query results to canonical wiki files: rejected because it violates read isolation.

## Decision 7: Keep write finalization operation-owned and exactly once

**Decision**: Ingest, capture, and update owners advance bounded source/destination work, validation, or blocker specificity. Child artifact owners return completion evidence to the parent. The parent performs its existing manifest/index/log/hot tracking and retrieval refresh exactly once after all required child work closes.

**Rationale**: Existing write owners already define tracking and QMD finalization. Re-entry must not repeat those terminal side effects.

**Alternatives considered**:
- Let every child finalize: rejected because multi-child operations would duplicate tracking and refresh.
- Add a persistent finalization flag: rejected because the parent operation already owns ephemeral completion state.

## Decision 8: Extend existing cold evaluations with trajectory evidence

**Decision**: Reuse owner `evals/evals.json`, skill-creator grading records, redacted efficiency traces, `scripts/token-count.py`, and `config/efficiency.yaml`. Add trajectory-focused cases and records for outcome, observations, actions, turns, tool calls, retrieval attempts, equivalent-action repeats, handoffs, validation passes, tokens, and termination reason. Grade outcomes and invariants, not one exact sequence.

**Rationale**: Trigger-only evaluation cannot prove convergence. Existing grading and telemetry surfaces cover behavioral assertions, token accounting, paired replay, quality review, and promotion policy.

**Alternatives considered**:
- Derive baseline from `errors.md`: rejected because the baseline must include representative success and intentional stall cases.
- Use output characters or bytes as tokens: rejected; project token measurement uses tiktoken.
- Require a token improvement claim: rejected; correctness may be promoted without claiming efficiency.

## Decision 9: Use paired, quality-bounded promotion

**Decision**: Run at least ten comparable baseline/replay pairs with the weakest sufficient executor. Require zero new hard-gate failures, lost parent objectives, duplicate finalizations, read-route mutations, or unspecific stalled outcomes, plus semantic non-inferiority. Claim token improvement only with at least five-percent median trajectory-token reduction under compatible tokenizer/model conditions.

**Rationale**: The constitution and efficiency policy protect D&D quality from process optimization and already define promotion thresholds.

**Alternatives considered**:
- Promote from static text review: rejected because agent-facing behavior needs cold execution.
- Use the strongest model: rejected because it can mask unclear guidance.

## Resolved technical context

- **Language/runtime**: Agent-facing Markdown/YAML/JSON plus existing Python 3.12+ CLI, evaluation, and telemetry tooling.
- **Dependencies**: Existing authority documents, owner skills/evals, `scripts/wiki`, `tools/wiki_ops`, skill-creator, pytest, tiktoken, and PyYAML. No new package.
- **Storage**: Repository guidance and contracts, owner eval JSON, redacted local evaluation/efficiency records, and existing wiki files. No persistent execution state.
- **Platform**: Existing macOS/Darwin workspace and CI-compatible Python checks.
- **Performance**: Semantic convergence before outer harness limits; no repeated equivalent action on unchanged evidence; token claims only under existing paired policy.
- **Accountability**: An issue must be linked or created before implementation; planning may complete before that gate.
