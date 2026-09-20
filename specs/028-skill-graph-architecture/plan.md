# Implementation Plan: Skill Graph Architecture

**Branch**: `028-skill-graph-architecture` | **Date**: 2026-09-20 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/028-skill-graph-architecture/spec.md`

```text
work_class: agent-system
route: full-sdd
reason: reusable routing, capability-boundary, handoff, context, and completion behavior changes for future agents
```

## Summary

Refactor existing agent guidance into a shallow capability execution graph without adding graph machinery. Root routing selects existing owners directly; each owner exposes Input, Work, Done, and Capability Handoff or clear equivalents; parent operations retain the original objective across bounded child work; real prerequisites and shared write surfaces determine ordering; each capability receives a minimum context projection; existing query, lint, and health contracts drive retrieval and validation feedback. Cold route-level evaluations use the weakest sufficient model. Campaign canon and runtime CLI contracts remain unchanged unless behavioral evidence exposes a concrete defect.

## Technical Context

**Language/Version**: Agent-facing Markdown/YAML/JSON; existing Python 3.12+ repository and evaluation tooling

**Primary Dependencies**: Existing `AGENTS.md`, `CONTEXT.md`, `docs/agents/hybrid-sdd.md`, `docs/agents/skill-design-dispatch.md`, `.agents/skills/skill-creator`, owner skills, `docs/agents/policy-owners.yml`, `specs/027-wiki-agent-cli/contracts/wiki-cli.md`, `scripts/wiki`, existing pytest and skill-eval tooling. No new package.

**Storage**: Existing repository guidance, skill eval JSON, templates/contracts, and wiki files. Capability execution state is ephemeral; no new database or ledger.

**Testing**: Cold focused with-skill/baseline behavioral evaluations with typed assertions and weakest sufficient executor; targeted pytest public-seam checks only if executable CLI/validation behavior changes; OMP and Spec Kit integration checks.

**Target Platform**: Existing macOS/darwin agent workspace and CI-compatible repository checks; local model-dependent evals where required.

**Project Type**: Agent instruction and skill architecture within the existing Obsidian wiki/Co-DM repository.

**Performance Goals**: Representative routes select the correct owner without generic indirection; unrelated artifact groups are absent from capability context; maintainers identify owner/context/dependencies/done/handoff in under two minutes; any claimed token reduction uses equivalent measured samples.

**Constraints**: Preserve D&D craft, canon fidelity, agency, output contracts, entity-before-spoken, DM-facing explicitness, read-only boundaries, and validation safeguards. No graph runtime/database, owner registry, persistent workflow ledger, generic orchestrator, universal state schema, bespoke node class, global DAG, or giant workflow.

**Scale/Scope**: Root routing and invariants; all live wiki-facing capabilities named by root routing; representative cross-capability campaign composers and subtype owners; four recurring workflow shapes; route-level evaluations. Campaign pages and generated Spec Kit adapters remain out of scope.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| Product invariant | PASS | Observable target is more reliable, complete, canon-faithful Work with less routing/context drift; protected quality remains a hard constraint. |
| I. Domain Language | PASS | Uses Capability, Owner capability, Parent operation, Capability dependency, Completion guard, Context projection, Observation surface, Output contract, Knowledge graph, and Execution graph from `CONTEXT.md`. |
| II. Issues Are the Work Surface | PASS with implementation gate | Spec requires an accountable issue before implementation; planning completes now, implementation cannot begin until linked. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) contains independent acceptance scenarios, FR-001–FR-032, and SC-001–SC-010. |
| IV. Behavioral Tests | PASS | [quickstart.md](quickstart.md) specifies cold public-seam route evaluations, not static prose checks alone. |
| V. Single Source of Truth | PASS | Root routes; owner skills execute; wiki context governs semantics; templates/validation govern output; CLI contract governs observations. |
| VI. Agent-Shaped | PASS | Capability boundaries state positive input/work/done/handoff and named failure evidence. |
| VII. Creative Judgment | PASS | Equivalent boundary concepts do not prescribe craft, voice, or one output structure. |
| VIII. Safe Automation | PASS | Existing transactions/fixers/finalization are reused; no new mutation engine. |
| IX. Measured Efficiency | PASS | Context/token improvement requires equivalent measured work and cannot trade protected quality. |
| X/XII/XVII. Canon and Evidence | PASS | Campaign canon unchanged; retrieval precedes invention; read routes do not mutate canonical state. |
| XIII. Evidence-Driven Improvement | PASS | Implementation is gated by cold route evidence and named failures. |
| XIV. Simplest Adequate Tool | PASS | Reuses current routing, skills, CLI contracts, transactions, health, lint, and eval tooling. |
| XV. Autonomous Operation | PASS | Existing unattended maintenance and green-before-done behavior remain. |
| XVI. Constitutional Layering | PASS | Authority chain prevents duplicate principles and procedure copies. |
| XVIII. Checked Todo | PASS | Implementation tasks will enumerate the full live capability inventory and dependencies. |
| XX. Lean Agent Documents | PASS | Duplicate procedure text is removed only after authority and strong pointers exist. |
| XXI. Linter Root-Cause | PASS | Findings route to deterministic repair or artifact owner and rerun affected scope. |
| XXII. Appropriate Delegation | PASS | Child scope is bounded; parent retains integration; shared surfaces stay serial. |
| XXIII. Real Surfaces | PASS | Quickstart exercises cold agents and actual `scripts/wiki` surfaces where applicable. |
| XXIV. Synchronized Content | PASS | Counterparts update only when they govern the changed behavior; templates/Vale are not churned for route-only prose. |
| XXV. Carve-Outs | PASS | The named live wiki-facing capability set is inventoried from the root authority; no smallest-slice filter. |
| XXVI. Weakest Sufficient Model | PASS | Cold executor uses the weakest model that completes the scenario. |

**Pre-design gate**: PASS. No unresolved clarification or unjustified violation.

## Project Structure

### Documentation (this feature)

```text
specs/028-skill-graph-architecture/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── capability-boundaries.md
└── tasks.md                         # Phase 2; not created by this command
```

### Source Code and Guidance (repository root)

```text
AGENTS.md                              # canonical direct routing and global invariants
CONTEXT.md                             # existing domain terms; change only if implementation clarifies a term
docs/agents/
├── hybrid-sdd.md                     # substantial cross-capability composition
├── skill-design-dispatch.md          # designated-writer procedure; unchanged unless evidence requires
├── wiki-maintenance-loop.md          # health/lint maintenance composition
└── policy-owners.yml                 # counterpart discovery; change only if ownership changes

.agents/skills/
├── wiki-*/SKILL.md                   # live wiki-facing read/write/ingest/maintenance owners
├── cross-linker|tag-taxonomy|daily-update|memory-bridge|.../SKILL.md
│                                        # remaining live root-routed wiki capabilities
├── session-beats/SKILL.md
├── hook-beats|development-beats|cliffhanger-beats|climax-beats|resolution-beats/SKILL.md
├── run-guide|theatre-of-the-mind/SKILL.md
├── place-design|city-design|region-design/SKILL.md
└── <artifact-owner>/evals/evals.json # focused cold route assertions where that owner changes

specs/017-session-beats-skills/contracts/beat-skill-routing.md
                                        # update only if beat route behavior changes
specs/027-wiki-agent-cli/contracts/wiki-cli.md
                                        # observation authority; expected unchanged
scripts/wiki                            # expected unchanged
tools/wiki_ops/                         # expected unchanged
wiki/AGENTS.md                          # wiki semantic/output authority pointer cleanup
wiki/templates/                         # change only if artifact validity changes
rules/ and styles/                      # change only if validation behavior changes
tests/                                  # targeted public-seam tests only for runtime contract changes
```

**Structure Decision**: This is an authority and behavior refactor over existing files, not a new module. The live root routing tables define the named capability inventory. Implementation changes only owners whose boundary or duplicate procedure requires correction; every named capability still receives evaluation coverage. Design-impact skill changes follow `docs/agents/skill-design-dispatch.md` with a designated writer. Generated adapters remain untouched.

## Ownership and Active Writers

| Artifact group | Canonical owner | Active writer | Order |
|---|---|---|---|
| Global intent routing and invariants | `AGENTS.md` | Session agent (`class: not`) | First; establishes pointers |
| Cross-capability substantial-work contract | `docs/agents/hybrid-sdd.md` | Session agent (`class: not`) | After root authority |
| Wiki semantics/output rules | `wiki/AGENTS.md` | Session agent (`class: not`) | After root/docs authority; serial shared policy surface |
| Owner skill boundary/craft text | Each `.agents/skills/<owner>/SKILL.md` | Designated writer for design-impact batches; session agent only for established small edits | After authority; disjoint skill files may be parallel |
| Owner cold evaluations | Each owner `evals/evals.json` or existing skill-creator workspace | Same writer as the paired skill/eval slice | Paired with owner change; aggregate after all |
| Beat route contract | `specs/017.../beat-skill-routing.md` | Session agent | Only after a demonstrated beat route change |
| Observation behavior | 027 contract + `scripts/wiki`/`tools/wiki_ops` | Existing runtime owner | Expected unchanged; serial if evidence requires change |
| Templates/contracts | Each template/contract owner | Corresponding owner writer | Only after output-shape change; before validation counterpart |
| Vale/rule sources | Rule registry/style owner | Validation writer | Only after validation semantics change; generated vocabulary excluded |
| Feature artifacts | `specs/028-*` | Session agent through Spec Kit phases | Plan now; tasks next |

Shared files have one writer and execute serially. Disjoint skill files may be dispatched concurrently only after root authority and exact cross-slice contracts are fixed.

## Dependency Waves

1. **Accountability**: link/create the implementation issue; inventory the live root-routed capability set and policy counterparts.
2. **Authority**: update root routing/invariants, then `hybrid-sdd.md`, then wiki semantic pointers. Do not prune safeguards before replacement pointers exist.
3. **Capability boundaries**: update owner skills in disjoint design-impact batches. Preserve specialized craft and local subtype seams.
4. **Workflow reconciliation**: normalize read/write/ingest/maintenance feedback; remove query/log read ambiguity; make health the action-order owner.
5. **Counterpart synchronization**: update only governing templates/contracts/rules and their tests if waves 2–4 changed artifact validity or validation behavior.
6. **Cold evaluation**: run focused weakest-model scenarios and named-failure coverage; correct owners, not symptoms.
7. **Repository verification**: targeted tests if runtime changed, OMP baseline, Spec Kit status, real wiki scope if affected, then cleanup.
## Implementation gate

Accountable issue: https://github.com/Thedougler/agentic-co-dm/issues/166

The issue is linked before implementation. The live root routing inventory has no
absent owner paths; policy counterparts are limited to the authority files and
owner skills named by the synchronization contract.

## Route inventory reconciliation

The live Wiki, Wiki kind, Co-DM, world-building, and presentation routing tables
resolve to existing `.agents/skills/<owner>/SKILL.md` paths. No route was
redirected or removed. `docs/agents/policy-owners.yml` continues to own only
shared artifact-shape, mutation, acceptance, and capability-boundary policies;
individual skills remain procedure owners.

## Completion evidence

Implementation records route, context used/omitted, affected and resolved
owners, dependencies, deterministic checks, cold quality review, work status,
canon state, filing, and measured/estimated/inferred context results in
`quickstart.md`.


## Context Boundaries

**context_used**: `spec.md`; constitution v3.1.0; root routing/context; `CONTEXT.md`; hybrid SDD; skill design dispatch; writing-for-agents; representative owner skills; wiki CLI contract; existing skill-creator evaluation patterns; policy-owner map.

**context_omitted**: campaign entity/session bodies, unrelated skill craft bodies, full wiki index/log/manifest, generated Spec Kit adapters, and CLI implementation internals unless evaluation exposes a runtime contract defect.

## Post-Design Constitution Check

Phase 1 artifacts resolve all technical choices: [research.md](research.md) establishes authority and reuse decisions; [data-model.md](data-model.md) defines concepts without persistence; [contracts/capability-boundaries.md](contracts/capability-boundaries.md) defines observable composition; [quickstart.md](quickstart.md) provides cold and real-surface validation. The gate remains **PASS**. No `NEEDS CLARIFICATION` remains. The only pre-implementation gate is the spec-required accountable issue.

## Complexity Tracking

No constitutional violation requires justification. The plan removes duplication and reuses existing seams; it adds no runtime architecture.
