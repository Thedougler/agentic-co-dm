# Implementation Plan: Hybrid Spec-Driven Development

**Branch**: `021-hybrid-sdd-adaptation` | **Date**: 2026-09-16 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/Users/nick/agentic-co-dm/specs/021-hybrid-sdd-adaptation/spec.md`

## Summary

Adapt the repository-owned Spec Kit operating layer so substantial work is classified as `engineering`, `agent-system`, `campaign-architecture`, or `creative-system`, while routine campaign content keeps its existing skill and Work route. The implementation keeps generated Spec Kit adapters and managed templates unchanged; a compact root `AGENTS.md` route points to a progressive-disclosure contract in `docs/agents/hybrid-sdd.md`. Maintainer-owned efficiency policy, a redacted JSONL trace helper, and a deterministic feature fixture provide the missing operational seams without creating a second canon, lifecycle, or retrieval system.

The native-tokenizer requirement is gated by the separate governance change named by the specification. This feature must not silently replace the current repository-wide tiktoken policy; traces carry tokenizer-family identity so cross-family comparisons are rejected.

## Technical Context

**Language/Version**: Markdown/YAML agent instructions and contracts; Python >=3.12 for two small standard-library CLIs and a feature fixture checker.

**Primary Dependencies**: Existing Spec Kit 1.0.8.dev0 runtime with the repository's 1.0.6 integration manifests; existing `AGENTS.md`, constitution, Work protocol, QMD/retrieval primitives, wiki checks, 012 blind evaluation contract, and 019 sitting/error-ledger helper. No new third-party dependency.

**Storage**: Versioned `config/efficiency.yaml`; local gitignored `.local/efficiency/traces.jsonl`; existing `errors.md` and `sittings.jsonl`; feature contracts and fixtures under `specs/021-hybrid-sdd-adaptation/`. No database.

**Testing**: Standard-library `specs/021-hybrid-sdd-adaptation/fixtures/check.py` at a public file/CLI seam; `specify integration status --json`; `./scripts/check-omp-baseline.sh`; focused Markdown checks. No pytest suite and no snapshots of instruction prose.

**Target Platform**: Local macOS workstations and coding-agent hosts that load repository instructions; GitHub CI-compatible command surfaces.

**Project Type**: Agent-facing operating policy, Spec Kit-adjacent documentation, and small agent-shaped CLI helpers.

**Performance Goals**: Classification and completion evidence load only the route-required context; comparable efficiency reports use the same sitting class and job; promotion requires at least 10 paired cases and a 5% median trajectory-token reduction without hard-gate or semantic regression.

**Constraints**: Preserve the existing Spec Kit lifecycle and hooks; do not edit generated `.agents/skills/speckit-*` or `.omp/commands/speckit.*` adapters or managed `.specify/templates/*`; preserve current wiki, Work acceptance, reveal, visibility, identity, agency, and designated-writer authorities; keep raw prompt, campaign, wiki, and model content out of normal traces; do not wrap QMD or git; do not silently change the current tiktoken governance.

**Scale/Scope**: One repository, four substantial-work classes plus the routine-content route, one maintainer policy, one trace stream, one deterministic fixture checker, and no campaign-content migration.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — uses existing Spec Kit, Work, DM, canon, reveal, visibility, agency, QMD, and wiki vocabulary; new work-class names are scoped to this feature. |
| II. Issues are the work surface | Pass — the feature remains represented by its existing tracked Spec Kit work surface; contracts do not create a second request intake. |
| III. Spec before system change | Pass — the accepted feature spec supplies the four classes, route boundaries, acceptance scenarios, and named failures. |
| IV. Behavioral tests | Pass — fixture and helper checks observe routing, schema, state, trace, and promotion behavior at public seams; they do not snapshot prose. |
| V. Single source of truth | Pass — `AGENTS.md` points to the hybrid contract, `config/efficiency.yaml` owns policy, specs own feature behavior, and existing wiki/Work/constitution owners remain authoritative. |
| VI. Software is agent-shaped | Pass — both new CLIs accept arguments or structured input, emit text/JSON, report errors on stderr, and distinguish success from failure. |
| VII. Creative judgment is protected | Pass — agency and creative quality remain evidence/review surfaces; the plan does not prescribe voice, story structure, or a creative method. |
| VIII. Safe automation runs unattended | Pass — deterministic checks and trace maintenance are explicit, idempotent, and surface failures; DM approval remains on fact-changing Work. |
| IX. Measured, quality-bounded efficiency | Pass — traces measure the whole useful trajectory, compare same-kind work, and retain quality gates; the tokenizer-policy conflict is an explicit prerequisite, not a silent override. |
| X. DM owns canon | Pass — proposed and conditional material stays separate from accepted truth and uses the existing Work acceptance path. |
| XI. Players choose; the world acts | Pass — creative and campaign-architecture artifacts must expose player-owned decisions and independent world motion. |
| XII. Evidence precedes invention | Pass — the route contract requires authoritative context, identity resolution, provenance, and visible conflicts before invention. |
| XIII. Self-improvement is evidence-driven | Pass — promotion uses pinned paired replay, hard gates, blind semantic evaluation, canaries, and rollback. |
| XIV. Designated writers have bounded concurrency | Pass — dependency records include canonical owner and writer; parallel work is allowed only for disjoint artifacts. |
| XV. Artifacts expose machine-readable identity | Pass — work class, route, trace schema version, sitting class, work status, and policy version are explicit fields. |
| XVI. Prompt other agents with objectives | Pass — delegated work uses the feature objective, acceptance evidence, deliverables, and named failure prevention; no harness manual is copied into prompts. |
| XVII. Simplest adequate tool | Pass — reuses existing checks and contracts, adds only the two missing public seams, and does not wrap QMD or git. |
| XVIII. Autonomous operation | Pass — safe deterministic maintenance and trace recording do not add human gates; semantic, canon, policy, and threshold changes retain required review. |
| XIX. Constitutional layering | Pass — stable invariants remain in the constitution; route procedure lives in `AGENTS.md`/`docs/agents`, feature behavior in the spec/contracts, and runtime policy in `config/efficiency.yaml`. |

## Project Structure

### Documentation (this feature)

```text
specs/021-hybrid-sdd-adaptation/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── hybrid-sdd.md
│   └── efficiency-telemetry.md
├── fixtures/
│   ├── check.py
│   ├── routes/
│   ├── evidence/
│   └── telemetry/
└── tasks.md                         # /speckit.tasks; not created by this command
```

### Source Changes (repository root)

```text
AGENTS.md                             # compact route and pointer only
docs/agents/hybrid-sdd.md             # detailed route, artifact, and evidence contract
config/efficiency.yaml                # maintainer-owned policy and thresholds
.gitignore                            # ignore local efficiency traces
scripts/hybrid-sdd-check.py           # deterministic route/evidence hard-gate seam
scripts/efficiency-trace.py           # redacted trace append/report/quarantine seam
```

Generated Spec Kit files remain unchanged:

```text
.agents/skills/speckit-*/
.omp/commands/speckit.*
.specify/templates/*
.specify/extensions/*
```

**Structure Decision**: Keep the current Spec Kit integration intact and use the existing agent-context injection to make `AGENTS.md` the always-loaded route map. Put detailed hybrid behavior in one progressive-disclosure document, policy in a versioned configuration file, and runtime measurement in two narrowly scoped agent-shaped CLIs. Feature-local fixtures are the permanent behavioral check; they do not become a second application test framework.

## Implementation Design

### Routing and artifact flow

1. Before a substantial change is written, classify it once and record `Work Class` plus `Route` in the feature artifact or completion evidence. Routine content does not get a feature directory.
2. `AGENTS.md` points substantial work to `docs/agents/hybrid-sdd.md`, which defines the minimum contract for each class and the existing skill/Work handoffs.
3. The plan records authoritative context loaded, intentionally omitted context, canonical owners, dependency edges, agency/canon constraints where applicable, and verification surfaces.
4. Tasks use serial/parallel waves with one writer per canonical artifact. A task cannot be parallel merely because it is prose.
5. Completion evidence separates specification approval, plan approval, task completion, Work production, DM acceptance, and accepted campaign truth.

### Measurement and promotion flow

1. `config/efficiency.yaml` is the only owner of sampling, retention, risk class, canary, non-inferiority, and rollback policy.
2. `scripts/efficiency-trace.py` validates a versioned redacted record, assigns every token occurrence one primary source owner, appends normal records to the gitignored JSONL stream, reports the required metric vector, and quarantines incompatible schema records without rewriting history.
3. Trace records distinguish `prep` and `wrapup`, `produced`, `accepted`, `failed`, and `incomplete`, and `complete` versus `measurement-gap` telemetry. Failed/incomplete work remains reportable but is excluded from accepted-Work denominators.
4. Promotion consumes equivalent paired records, requires the policy thresholds, and routes low-, moderate-, and high-risk candidates to auto-promotion, shadow/canary review, or human review respectively. Any hard-gate or semantic regression rolls back.

### Verification flow

`scripts/hybrid-sdd-check.py` owns only objective hybrid checks: class/route identity, required evidence fields, allowed state transitions, schema/version compatibility, primary-source token attribution, accepted-Work denominator rules, and hard-gate result recording. Existing wiki, link, schema, and literal-newline checks remain their own authorities. Blind semantic evaluation uses the existing 012 evaluation contract and a fixed paired rubric; it is never reported as deterministic lint.

## Complexity Tracking

None. The two CLIs have separate owners and public seams: one records/reports telemetry, the other validates hybrid artifact and evidence invariants. A shared framework or second database would add complexity without a named failure it prevents.

## Phase 0: Research

- Confirmed current Spec Kit status is healthy (`status: ok`), OMP remains the default, four integrations are installed, no managed files are missing or modified, and the OMP baseline passes.
- Confirmed existing 012 blind evaluation supplies the cold semantic-evaluation pattern and existing quality authorities; no numeric creative score or new creative-writing rubric is needed.
- Confirmed existing 019 supplies the sitting/error-ledger vocabulary and fixture-check pattern; new efficiency telemetry must remain a separate owner because it has a different schema, retention, and reporting contract.
- Confirmed current repository token policy is tiktoken-based. Native-tokenizer comparisons therefore require the separate governance change named by the spec before activation; this feature records the dependency and must not edit that policy silently.
- Confirmed the lowest-cost routing surface is a compact `AGENTS.md` pointer plus one detailed `docs/agents/hybrid-sdd.md`, rather than editing generated adapters or copying policy into every harness.

**Post-research gate**: all technical unknowns are resolved in [research.md](./research.md); the plan has no unresolved technical decisions.

## Phase 1: Design

- Model work classification, hybrid artifacts, canon/agency records, dependency ownership, completion evidence, traces, policy, semantic evaluations, promotion candidates, and quarantine states in [data-model.md](./data-model.md).
- Define agent-facing routing/completion rules in [contracts/hybrid-sdd.md](./contracts/hybrid-sdd.md).
- Define trace, report, schema evolution, retention, and promotion inputs in [contracts/efficiency-telemetry.md](./contracts/efficiency-telemetry.md).
- Provide runnable fixture validation in [quickstart.md](./quickstart.md) and the feature-local checker.

**Post-design gate**: constitution checks still pass; no generated Spec Kit integration or existing campaign authority is replaced; no new human gate is added to safe deterministic maintenance.
