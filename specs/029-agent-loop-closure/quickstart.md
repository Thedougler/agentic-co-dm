# Quickstart: Validate Agent Loop Closure

## Prerequisites

- Repository venv available.
- Feature branch `029-agent-loop-closure`.
- Accountable issue linked before implementation begins.
- Feature 028 ownership and boundary checks remain available.
- Cold behavioral runs use the weakest sufficient executor.
- Token measurements use `scripts/token-count.py`; do not estimate from bytes or characters.

Use [data-model.md](data-model.md) for evidence fields and [contracts/capability-loop.md](contracts/capability-loop.md) for pass conditions.

## V-001 — Guard coherence

Exercise focused query, scoped lint, faction filing, and user-said place canon scenarios.

Expected:
- query changes no canonical page, manifest, index, or log;
- lint observation, fix, and rerun preserve the selected scope;
- faction Done accepts the current faction owner path;
- user-said canon files immediately without a separate acceptance wait.

Covers FR-011–FR-016 and SC-004, SC-005, SC-013.

## V-002 — Successful owner iteration

Run a cold owner job requiring more than one valid action.

Expected:
- every action begins from fresh owner-relative evidence;
- each continuation has progress evidence;
- the final owner completion guard passes;
- no equivalent action repeats against unchanged evidence.

Covers FR-001–FR-006 and SC-001–SC-003.

## V-003 — Intentional stall and blocker

Give an owner an incomplete boundary where all sanctioned paths are exhausted.

Expected:
- the repeated equivalent action is not invoked;
- termination occurs before outer harness limits;
- blocker names owner, boundary, observation, attempted paths, reason, and parent effect.

Covers FR-004–FR-006 and SC-001–SC-003.

## V-004 — Deterministic repair progress

On a disposable configured vault, create one registered deterministic finding. Run:

```bash
scripts/wiki lint <vault-relative-path>
scripts/wiki lint fix <vault-relative-path>
scripts/wiki lint <vault-relative-path>
```

Expected:
- all three operations retain the exact selected scope;
- lint-fix output retains its existing result and includes the `progress` contract;
- before/after totals, resolved evidence, changed files, next-target change, and state change match observations;
- post-fix validation reaches clean or exposes the next surviving finding.

Covers FR-020–FR-023 and SC-005–SC-006.

## V-005 — Skipped and semantic repair stalls

Exercise an unsupported deterministic finding and a semantic finding that remains identical after owner work.

Expected:
- skipped/unsupported repair is not invoked twice for the same observation;
- the semantic path rereads the surviving finding and owner contract;
- the next action is materially different or a blocker identifies path, rule, evidence, owner, and reason.

Covers FR-024–FR-026 and SC-006.

## V-006 — Query retrieval convergence

Run a query with one sufficient hit and one case with an unchanged candidate set after focused retrieval.

Expected:
- sufficient evidence stops retrieval;
- deepening follows only unexplored supporting, conflicting, or gap paths;
- unchanged candidates do not receive equivalent retrieval twice;
- canonical wiki and tracking files remain unchanged.

Covers FR-027–FR-028 and SC-002, SC-004.

## V-007 — Context-pack convergence

Run one bounded context-pack request that meets its evidence/budget contract and one deliberately silent/failing collection path.

Expected:
- the successful pack stops at its owner output contract;
- fallback occurs only where the owner documents it;
- repeated terminal retrieval produces a specific blocker;
- no canonical mutation occurs.

Covers FR-027–FR-028, FR-034–FR-035, and SC-001–SC-004.

## V-008 — Ingest exactly-once finalization

Run a multi-source ingest whose destinations require more than one child owner.

Expected:
- each child advances bounded destination state and returns completion evidence;
- the parent retains source-level completion responsibility;
- manifest/index/log/hot tracking and retrieval refresh each occur exactly once after children close;
- an incomplete child blocks finalization.

Covers FR-029–FR-030 and SC-007–SC-008.

## V-009 — Capture and update progress

Run full capture, quick capture, and project update/no-op cases.

Expected:
- each mode preserves its existing tracking/finalization contract;
- every repeated iteration advances bounded source/destination work, validation, or blocker specificity;
- no-op update terminates rather than reprocessing unchanged evidence;
- finalization is not duplicated.

Covers FR-029–FR-030 and SC-002, SC-008.

## V-010 — Session parent resumption

Run a cold session-planning case requiring a typed beat child and an intentionally incomplete child return.

Expected:
- complete child evidence changes a dependency, artifact state, or completion evidence;
- incomplete return does not advance dependent work;
- the parent preserves the original objective and unresolved dependencies;
- unrelated child context is absent after resumption.

Covers FR-031–FR-033 and SC-007.

## V-011 — Place bounded handoff

Run place design requiring a bounded faction or narration child, plus one child blocker.

Expected:
- the child owns only its requested artifact or section;
- a complete return changes required place state before re-entry;
- a blocked return prevents dependent place completion;
- focused place retrieval resumes the same owner without inherited unrelated context.

Covers FR-031–FR-033 and SC-007.

## V-012 — Run-guide pass convergence

Run a complete four-pass guide and a case with a missing owner/path/section.

Expected:
- each pass meets its own completion evidence before the next begins;
- the complete guide reaches the Reading-view/table gate;
- the stalled case stops at a specific blocker and later passes do not advance;
- the parent session objective remains intact.

Covers FR-031–FR-033 and SC-001, SC-007.

## V-013 — Tool recovery

Inject one transient diagnostic with a documented fallback and one repeated terminal diagnostic.

Expected:
- transient recovery continues only after changed evidence or through the fallback;
- terminal failure does not repeat unchanged recovery;
- terminal failure reports a specific blocker before outer limits.

Covers FR-034–FR-035 and SC-003.

## V-014 — Paired trajectory promotion

Capture at least ten comparable baseline/replay pairs spanning V-002 through V-013, including successes and intentional stalls. Record the fields in [data-model.md](data-model.md).

Expected:
- every success reaches its owner guard;
- every intentional stall has a specific blocker;
- duplicate equivalent actions, lost objectives, duplicate finalizations, and read mutations are zero;
- valid alternative strategies pass;
- blind paired semantic review is non-inferior;
- any token claim meets the existing five-percent median threshold with compatible objective measurements; otherwise report no token claim.

Covers FR-017–FR-019, FR-036–FR-041, and SC-009–SC-012.

## V-015 — Compatibility and repository checks

Run the focused CLI tests changed by the progress contract, applicable owner eval validation, Spec Kit integration status, and OMP baseline. Review changed paths.

Expected:
- feature 028 guarantees remain green;
- current CLI contract and targeted public-seam tests pass;
- no campaign page, unrelated template/rule/skill, generated Spec Kit adapter, harness safety limit, new orchestration layer, persistent ledger, progress command, or proactive carve-out changed without required evidence;
- any pre-existing repository blocker is reported with exact evidence, not hidden.

Covers FR-042–FR-045 and SC-011, SC-013.
