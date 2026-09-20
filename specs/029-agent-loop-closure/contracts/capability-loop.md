# Contract: Owner-Relative Capability Loop

## Authority chain

1. `AGENTS.md` selects the existing owner and carries the compact loop invariant.
2. `docs/agents/hybrid-sdd.md` owns the complete cross-capability observe/act/re-observe rule.
3. The active owner defines valid actions, evidence, completion guard, and local handoffs.
4. `wiki/AGENTS.md` governs wiki semantics, canon, scope, and mutation boundaries.
5. Existing CLI/contracts define deterministic result shapes and side effects.
6. Evaluation and efficiency policy determine promotion, never runtime ownership.

## Iteration contract

For every incomplete owner boundary:

1. Obtain a fresh owner-relative observation. Existing compact evidence may be reused only when its underlying state is known current.
2. Select an owner-sanctioned action that can change required state, relevant evidence, unresolved dependencies, validation, or diagnostic specificity.
3. Execute the action once.
4. Re-observe the same owner boundary.
5. Continue only when the completion guard passes or meaningful progress is evidenced.
6. If the observation is unchanged, do not repeat an equivalent action. Choose a materially different sanctioned path or return a specific blocker.

Outer harness recursion, request, runtime, isolation, continuation, compaction, and memory limits remain safeguards, not normal termination conditions.

## Completion contract

A successful branch closes only when its existing owner completion guard passes. Prose existence, a child assertion, or a reduced finding count without the required guard is insufficient.

An unsuccessful branch closes with a blocker naming:
- owner;
- artifact, operation, scope, or dependency;
- surviving observation;
- attempted sanctioned paths;
- why no remaining path can progress;
- effect on the parent objective when applicable.

## Progress contract

Progress is owner-relative. Valid evidence changes at least one of:
- required artifact or operation state;
- supporting, conflicting, or gap evidence;
- unresolved dependencies;
- validation result or next target;
- diagnostic specificity or documented fallback availability.

A changed tool call, paraphrased action, or repeated completion claim is not progress.

## Read contract

Query and context-pack retrieval deepen only while a focused unexplored path can add supporting, conflicting, or gap evidence. An equivalent retrieval does not repeat against an unchanged candidate set.

Read routes do not mutate canonical pages, `.manifest.json`, `index.md`, or `log.md`. Derived cache and command timing side effects remain limited to the CLI contract.

## Deterministic maintenance contract

`wiki lint fix` preserves the resolved input scope through pre-observation, repair, and post-observation. Its result retains existing fields and adds:

```json
{
  "progress": {
    "before_total": 0,
    "after_total": 0,
    "resolved": [],
    "changed_files": [],
    "next_changed": false,
    "state_changed": false
  }
}
```

Rules:
- totals come from complete worklists over the same resolved scope;
- `resolved` uses stable finding identity or rule evidence;
- `changed_files` remains vault-relative;
- a skipped or unsupported fixer that leaves its finding unchanged is not invoked again for that observation;
- an unchanged semantic finding causes rereading of the surviving finding and artifact-owner contract before a different action or blocker;
- `wiki health` retains maintenance action ordering.

## Write and finalization contract

Ingest, capture, and update parents advance bounded source/destination work, validation, or blocker specificity. Required children return observable completion evidence before dependent work resumes.

After all required owned work closes, the parent invokes its existing tracking and retrieval finalization path exactly once. Child owners do not duplicate source-level manifest/index/log/hot tracking or QMD refresh.

## Parent/child contract

A child return includes:
- receiving owner;
- bounded artifact or operation;
- changed dependency, owned state, or completion evidence;
- unresolved blocker, if any;
- parent resume point.

Incomplete evidence blocks dependent work. On resumption, the parent preserves the original objective and unresolved dependencies while excluding unrelated child context.

## Recovery contract

A tool retry is valid only when the observation or diagnostic changed, or a documented fallback remains. Repeated terminal failure with no new recovery evidence returns a specific blocker before outer harness limits are consumed.

## Evaluation contract

Cold focused baseline/replay cases use the weakest sufficient executor and grade observable outcomes, not one exact tool sequence. Coverage includes:
- premature completion;
- stalled query and context-pack retrieval;
- resolving and unchanged deterministic repair;
- incomplete child return and parent resumption;
- duplicate finalization;
- transient and terminal tool failure;
- read/write isolation;
- context reset after capability handoff;
- the named guard contradictions.

Promotion requires at least ten comparable pairs, zero new hard-gate failures, zero repeated equivalent actions, zero lost parent objectives, zero duplicate finalizations, zero read mutations, specific blockers for intentional stalls, and semantic non-inferiority. A token claim additionally uses objective compatible token measurements and the existing five-percent median threshold.

## Compatibility

Feature 028 ownership, context projection, dependency, handoff, read isolation, and observable completion guarantees remain binding. No new owner registry, orchestrator, workflow engine, persistent execution ledger, loop ledger, progress command, universal iteration schema, or proactive capability carve-out is introduced.
