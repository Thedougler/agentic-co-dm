# Implementation Plan: Agent Loop Closure

**Branch**: `029-agent-loop-closure` | **Date**: 2026-09-20 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/029-agent-loop-closure/spec.md`

```text
work_class: agent-system
route: full-sdd
reason: changes reusable owner-capability iteration, completion, blocker, and evaluation behavior for future agents
```

## Summary
**Accountable issue**: https://github.com/Thedougler/agentic-co-dm/issues/167

Extend feature 028's existing capability composition with an owner-relative observe/act/re-observe invariant. Each incomplete branch continues only on meaningful progress, reaches its existing owner completion guard, changes to a materially different sanctioned path, or stops with a specific blocker. Correct four guard contradictions before measurement; add compact lint-fix progress to the existing CLI result; update only named owners and cold trajectory evaluations; preserve ephemeral execution state and existing exactly-once finalization.

## Technical Context

**Language/Version**: Agent-facing Markdown/YAML/JSON; existing Python 3.12+ CLI, evaluation, and telemetry tooling

**Primary Dependencies**: `AGENTS.md`, `CONTEXT.md`, `docs/agents/hybrid-sdd.md`, `wiki/AGENTS.md`, feature 028 contracts, `specs/027-wiki-agent-cli/contracts/wiki-cli.md`, `scripts/wiki`, `tools/wiki_ops`, named owner skills/evals, skill-creator grading, `scripts/efficiency-trace.py`, `scripts/token-count.py`, `config/efficiency.yaml`, pytest, tiktoken, PyYAML. No new package.

**Storage**: Existing repository guidance/contracts, owner eval JSON, gitignored redacted local efficiency/evaluation records, and wiki files. Capability execution remains ephemeral; no new database or ledger.

**Testing**: Focused pytest at the public `scripts/wiki lint fix` seam; cold focused owner trajectories with typed outcome assertions using the weakest sufficient executor; blind paired semantic review; existing telemetry fixtures; Spec Kit and OMP integration checks.

**Target Platform**: Existing macOS/Darwin agent workspace and CI-compatible Python 3.12 checks; local model-dependent cold evaluations.

**Project Type**: Agent instruction/skill architecture plus a narrow Python CLI contract extension in the existing Obsidian wiki/Co-DM repository.

**Performance Goals**: 100% of representative success branches reach owner guards; 100% of intentional stalls produce specific blockers before outer limits; zero repeated equivalent actions, read-route canonical mutations, lost parent objectives, or duplicate finalizations across at least ten paired cases. Token improvement is optional and claimed only at the existing five-percent median threshold.

**Constraints**: Preserve D&D craft, canon fidelity, player agency, owner specialization, feature 028 boundaries, selected lint scope, health ordering, immediate canon filing, and exactly-once finalization. No orchestrator, workflow engine, owner registry, persistent execution/loop ledger, progress command, universal iteration schema, global iteration count, unrelated campaign/template/rule changes, or proactive owner carve-outs.

**Scale/Scope**: Shared loop authority; four named guard contradictions; lint-fix progress result; query/context-pack, ingest/capture/update, session-planning/place/run-guide owner behavior; focused owner evals; at least ten baseline/replay cases. Other owners change only after a local failing evaluation.

No `NEEDS CLARIFICATION` remains; Phase 0 decisions are recorded in [research.md](research.md).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| Product invariant | PASS | Observable target is complete validated Work without stalls, lost objectives, false completion, or duplicate finalization; protected quality remains mandatory. |
| I. Domain Language | PASS | Uses `CONTEXT.md` Capability, Owner capability, Parent operation, Completion guard, Observation surface, and Execution graph. |
| II. Issues | PASS WITH IMPLEMENTATION GATE | Planning may complete; an accountable issue must be linked before implementation. |
| III. Spec Before System Change | PASS | `spec.md` contains independent scenarios, requirements, success criteria, scope, failures, and canon impact. |
| IV. Behavioral Tests | PASS | Plan requires focused public-seam tests and cold agent behavior trajectories; static checks are supporting evidence only. |
| V. Single Source of Truth | PASS | Hybrid SDD owns common semantics; owner skills own local procedure; CLI contract owns result shape; no duplicate registry. |
| VI. Agent-Shaped | PASS | Guidance names positive execution and Done behavior; CLI keeps arguments-in/JSON-out/exit-status behavior. |
| VII. Creative Judgment | PASS | Owner craft and D&D quality remain protected; evaluations grade outcomes rather than one exact method. |
| VIII. Safe Automation | PASS | Existing deterministic lint repair remains idempotent and scope-safe; no new human chore. |
| IX. Measured Efficiency | PASS | Paired objective measurement and semantic non-inferiority are required for any efficiency claim. |
| X–XII. Canon, Agency, Evidence | PASS | Campaign canon is unchanged; read isolation and immediate filing of user-said canon are corrected; no PC outcomes are authored. |
| XIII. Evidence-Driven Improvement | PASS | Named failures map to focused baseline/replay scenarios; promotion is evidence-gated. |
| XIV. Simplest Tool | PASS | Reuses feature 028, existing owner skills, CLI observations, evals, telemetry, and policy; adds one result object only where both observations already exist. |
| XV–XVII. Autonomy, Layering, Wiki | PASS | Safe work runs unattended; authorities remain layered; wiki writes/finalization preserve existing owners. |
| XVIII. Checked Todo | PASS | Planning execution uses a checked task list; implementation tasks will preserve explicit dependencies. |
| XIX–XXI. Durable Fix, Lean Text, Root Cause | PASS | Contradictions are repaired at authoritative owner text/contracts; shared rule lives once; focused failures are rerun. |
| XXII–XXIII. Delegation and Real Surfaces | PASS | Planning research used bounded read-only slices; validation uses actual owner/CLI surfaces. |
| XXIV. Synchronized Systems | PASS | Runtime contract, focused tests, owner guidance, and relevant evals change together; unrelated templates/Vale stay unchanged. |
| XXV. Carve-Outs | PASS | The named owner set follows one composed rule; additional owners require observed local failure, not proactive exceptions. |
| XXVI. Weakest Model | PASS | Cold evaluation uses the weakest sufficient executor with focused context. |

**Gate result**: PASS. No constitutional violation requires a complexity exception. Accountability remains a pre-implementation dependency.

## Project Structure

### Documentation (this feature)

```text
specs/029-agent-loop-closure/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── capability-loop.md
└── tasks.md                 # generated by /speckit.tasks, not this command
```

### Source Code (repository root)

```text
AGENTS.md                              # compact always-loaded loop invariant and pointer
docs/agents/hybrid-sdd.md              # canonical cross-capability loop semantics
wiki/AGENTS.md                         # wiki semantic pointer; change only if contradiction remains

.agents/skills/
├── wiki-query/SKILL.md                # remove canonical log write; retrieval stop/stall rule
├── wiki-context-pack/SKILL.md         # focused unexplored-path stop/stall rule
├── wiki-lint/SKILL.md                 # selected-scope loop and deterministic stall behavior
├── wiki-ingest/SKILL.md               # bounded progress; exactly-once parent finalization
├── wiki-capture/SKILL.md              # mode-relative progress/finalization
├── wiki-update/SKILL.md               # delta/no-op progress/finalization
├── faction-design/SKILL.md            # current owner path guard
├── place-design/SKILL.md              # immediate user-said canon; child progress evidence
├── session-beats/SKILL.md             # child return and parent resumption progress
├── run-guide/SKILL.md                 # pass completion and blocker behavior
└── <named-owner>/evals/evals.json     # focused cold trajectory assertions

scripts/wiki                            # lint-fix before/after progress composition
tools/wiki_ops/                         # reuse worklist and repair primitives; no new subsystem
specs/027-wiki-agent-cli/
├── contracts/wiki-cli.md              # public progress result contract
└── data-model.md                       # result shape if maintained there

tests/test_wiki_cli.py                  # public lint-fix progress/scope/idempotence tests
tests/test_wiki_ops.py                  # only if extracted pure comparison logic warrants it

.agents/skills/skill-creator/           # reuse grading schemas and cold workflow
scripts/efficiency-trace.py             # reuse; extend only if trajectory fields cannot live in eval records
config/efficiency.yaml                  # unchanged policy owner unless evidence requires governance change
specs/021-hybrid-sdd-adaptation/         # existing telemetry contract/fixture; update only with trace schema change
```

**Structure Decision**: This is a narrow extension of existing authority, owner skill, CLI, test, and evaluation surfaces. The implementation adds no module tree or orchestration component. `scripts/wiki lint fix` is the only runtime surface requiring new progress output because it already owns both observations. Shared authority files have one writer; disjoint owner skill/eval slices may follow their dispatch rules after the shared contract is fixed.

## Ownership and Active Writers

| Artifact group | Canonical owner | Active writer | Dependency |
|---|---|---|---|
| Common loop invariant | `docs/agents/hybrid-sdd.md`; compact pointer in `AGENTS.md` | Session agent (`class: not`) | First after accountability/baseline |
| Wiki semantics | `wiki/AGENTS.md` | Session agent (`class: not`) | Only for confirmed contradiction/pointer coherence |
| CLI progress behavior | `scripts/wiki`, 027 CLI contract/data model | Runtime owner | After baseline; before consuming guidance |
| CLI public behavior tests | `tests/test_wiki_cli.py` | Runtime owner | Red first, paired with CLI change |
| Owner-local behavior | Each named `.agents/skills/<owner>/SKILL.md` | Skill-design dispatch determines writer | After common contract and guard fixes |
| Owner trajectory cases | Matching `evals/evals.json` and skill-creator records | Same slice as owner change | Paired with owner behavior |
| Evaluation/telemetry policy | Existing skill-creator, efficiency trace, and config owners | Existing owner; prefer unchanged | Change only if current records cannot carry required evidence |
| Feature artifacts | `specs/029-agent-loop-closure/` | Session agent through Spec Kit | Plan now; tasks next |

## Dependency Waves

1. **Accountability and baseline**: link/create the issue; freeze comparable cold baseline cases and record current guard contradictions before edits.
2. **Guard coherence**: repair query read isolation, lint selected scope, faction owner path, and immediate user-said canon filing; run focused coherence scenarios.
3. **Shared loop authority**: add the canonical owner-relative invariant to hybrid SDD and its compact root pointer without duplicating owner procedure.
4. **Deterministic proof**: add a failing public-seam test, implement lint-fix `progress` from existing same-scope worklists, update the 027 contract/data model, and verify idempotent skipped/unsupported behavior.
5. **Read and write owners**: update query/context-pack retrieval convergence and ingest/capture/update bounded progress/exactly-once finalization; keep disjoint skill/eval files parallel only after contracts stabilize.
6. **Campaign parents**: update session planning, place, and run-guide child-return/re-entry/blocker semantics while preserving specialized craft and dependency order.
7. **Trajectory replay**: run at least ten comparable cold baseline/replay pairs, grade observable invariants and semantic quality, and record promotion evidence. Do not claim token improvement without passing measurement conditions.
8. **Repository verification and cleanup**: run focused runtime tests, eval validation, Spec Kit/OMP checks, inspect changed surfaces for forbidden machinery or unrelated churn, and remove throwaway artifacts.

## Context Boundaries

**context_used**: Feature 029 spec; constitution v3.1.0; root and OMP agent context; `CONTEXT.md`; hybrid SDD; writing-for-agents; feature 028 spec/plan/research/data model/contract/quickstart; 027 CLI contract; named owner skills/evals; `scripts/wiki` and `tools/wiki_ops` observations; skill-creator grading; efficiency trace/policy and token method; bounded research results.

**context_omitted**: Campaign entity/session bodies, full wiki index/log/manifest, unrelated skill craft, unrelated templates/Vale rules, generated Spec Kit adapters, historical error-ledger content, and harness internals beyond existing safety bounds. They do not govern this agent-system convergence change.

## Post-Design Constitution Check

Phase 1 resolves all technical choices in [research.md](research.md), defines ephemeral concepts without a runtime schema in [data-model.md](data-model.md), fixes the observable contract boundary in [contracts/capability-loop.md](contracts/capability-loop.md), and supplies fifteen runnable validation scenarios in [quickstart.md](quickstart.md). The gate remains **PASS**. No `NEEDS CLARIFICATION` remains. The only pre-implementation gate is the accountable issue required by the spec and constitution.

## Complexity Tracking

No constitutional violation requires justification. The design reuses existing owners and observations and adds no orchestration layer, persistent state, dependency, or global policy.
