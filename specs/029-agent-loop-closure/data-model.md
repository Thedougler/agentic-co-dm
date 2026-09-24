# Data Model: Agent Loop Closure

This feature adds no database, persistent workflow state, owner registry, or universal runtime schema. The following concepts extend feature 028's ephemeral Execution Graph and appear in agent guidance, existing CLI results, and evaluation records.

## Capability Iteration

One cycle at an active owner boundary.

| Field | Meaning | Validation |
|---|---|---|
| owner | Existing capability responsible for the boundary | Resolves through current root routing; never a generic fallback |
| boundary | Owned artifact, operation, scope, or dependency | Bounded and observable |
| observation_before | Fresh evidence used to choose the action | Current for the same owner and boundary |
| action | Owner-sanctioned mutation, retrieval, validation, handoff, or recovery | Material target, inputs, and expected effect are identifiable |
| observation_after | Re-observation of the same boundary | Captured after the action or failed attempt |
| progress | Owner-relative delta between observations | Changes required state, relevant evidence, dependencies, validation, or diagnostic specificity |
| outcome | Continue, complete, change-path, or block | Justified by progress and the owner's completion guard |

State transitions:

```text
observe -> act -> re-observe -> progress -> observe
                          |-> completion guard passes -> complete
                          |-> unchanged + alternative path -> change-path -> observe
                          `-> unchanged + no sanctioned path -> specific blocker
```

Invalid transitions: action without a current observation; continuation on an unchanged observation with an equivalent action; completion by assertion without the owner guard; parent advancement from incomplete child evidence.

## Observation

Current owner-relative evidence for one boundary.

| Field | Meaning | Validation |
|---|---|---|
| owner | Observation authority | Same owner as the active iteration |
| boundary | Artifact, operation, scope, candidate set, dependency, or diagnostic | Stable enough for before/after comparison |
| evidence | Compact current result | Sufficient to select the next owner-sanctioned action |
| freshness | Why the evidence is current | Newly observed, or compact cached surface whose underlying state is known current |
| completion_status | Result of the owner's completion guard | Passed, failed with actionable evidence, or blocked |

An observation is not a planner, persistent ledger, or second source of truth.

## Progress Evidence

Evidence that one iteration materially advanced its owner boundary.

Valid progress dimensions:
- required artifact or operation state changed;
- supporting, conflicting, or gap evidence changed;
- an unresolved dependency completed or became more specific;
- validation findings or next target changed;
- a tool diagnostic became more specific or exposed a documented fallback.

Invalid progress:
- repeated prose claiming completion;
- different wording for the same action;
- a child return without changed dependency/artifact/completion evidence;
- retrying an unchanged skipped or unsupported deterministic action.

## Equivalent Action

Two actions are equivalent when they have the same material target, inputs, and expected effect against the same observation. Tool name, prose wording, or call encoding does not by itself distinguish actions.

Identity fields: owner, boundary, target, material inputs, expected effect, observation identity.

## Stall

A stall exists when the active path would repeat an equivalent action against an unchanged observation.

Transitions:

```text
unchanged observation + unexplored sanctioned path -> change-path
unchanged observation + no sanctioned path -> specific blocker
```

A stall is not resolved by consuming the outer harness request/runtime limit.

## Specific Blocker

Terminal evidence for an unsuccessful capability branch.

| Field | Required content |
|---|---|
| owner | Capability that owns the blocked boundary |
| boundary | Affected artifact, operation, scope, or dependency |
| observation | Surviving evidence after the last sanctioned action |
| attempted_paths | Owner-sanctioned paths already tried |
| reason | Why no remaining sanctioned path can progress |
| parent_effect | Which original objective or dependency remains incomplete, if applicable |

## Progress Delta

A compact comparison emitted only by an existing deterministic operation that naturally owns both observations.

For `wiki lint fix`:

| Field | Type | Rule |
|---|---|---|
| before_total | non-negative integer | Pre-fix complete finding total for the resolved scope |
| after_total | non-negative integer | Post-fix complete finding total for the same scope |
| resolved | array | Stable finding identities or rules present before and absent after |
| changed_files | array of vault-relative paths | Files changed by the atomic repair |
| next_changed | boolean | Whether the compact next target changed |
| state_changed | boolean | True when findings, next target, or files changed |

The delta augments the existing lint-fix result. It does not replace `applied`, `skipped`, `remaining`, or health action ordering.

## Parent Operation

Feature 028's Parent Operation gains no persistent fields. During execution it retains:
- original objective;
- active owner;
- unresolved and completed dependencies;
- last relevant observation per active boundary;
- child completion evidence;
- final completion guard.

A complete child return must change a required dependency, owned artifact state, or completion evidence. Parent resumption omits unrelated child context.

## Trajectory Record

A redacted evaluation record for one representative job. It extends existing evaluation/efficiency evidence; it is not runtime execution state.

| Field | Meaning |
|---|---|
| case_id / pair_id | Stable baseline/replay identity |
| category | Query, context-pack, lint, ingest, capture/update, session planning, place, run-guide, or recovery |
| outcome | Complete or specific blocker |
| observations | Ordered redacted owner/boundary evidence summaries |
| actions | Ordered material targets/inputs/effects |
| turns / tool_calls | Non-negative counts |
| retrieval_attempts | Count and unexplored-path evidence |
| duplicate_equivalent_actions | Must be zero for promotion |
| capability_handoffs | Owner, bounded child output, return evidence, resume point |
| validation_passes | Owner validation results |
| trajectory_tokens | Objective token count with tokenizer identity |
| termination_reason | Completion guard or specific blocker |
| hard_gates | Read isolation, scope, parent objective, exactly-once finalization, and blocker checks |
| semantic_review | Blind paired fixed-rubric result |

## Relationships and invariants

- A Capability Iteration belongs to one existing owner and one boundary.
- Its before/after Observations produce zero or one Progress Evidence result.
- No progress plus an equivalent next action creates a Stall.
- A Stall changes path or creates a Specific Blocker.
- A Parent Operation advances only from complete child evidence.
- A Trajectory Record observes execution for evaluation; it never drives runtime behavior.
- Canonical wiki state is unchanged by read trajectories.
- Tracking and retrieval finalization occur once per bounded write operation after all required owned work closes.
