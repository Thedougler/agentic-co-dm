# Research: Skill Graph Architecture

## Decision 1: Use existing authority layers

**Decision**: Keep `AGENTS.md` as the direct intent-to-owner router and global-invariant pointer, `docs/agents/hybrid-sdd.md` as the substantial-work composition contract, `wiki/AGENTS.md` as wiki semantic/output authority, and each capability skill as owner of its procedure, completion guard, and local handoffs.

**Rationale**: The repository already has shallow routing and owner-specific craft. The defect is scattered and duplicated boundary prose, not missing runtime machinery.

**Alternatives considered**:
- A machine-readable owner registry: rejected until observed duplication causes a maintenance failure (FR-024).
- A generic orchestrator or persistent execution ledger: rejected because it duplicates current authorities and violates FR-025.
- Moving all routing into `hybrid-sdd.md` or `wiki/AGENTS.md`: rejected because each has a narrower load boundary.

## Decision 2: Normalize capability boundaries without a universal schema

**Decision**: Every in-scope wiki-facing capability will expose Input, Work, Done, and Capability Handoff as headings or clear equivalents. Preserve specialized completion tests, craft, and local seams.

**Rationale**: Equivalent boundary concepts make ownership and closure inspectable while avoiding a new configuration/state schema. Strong pointers replace duplicate procedure text only after the canonical owner is explicit.

**Alternatives considered**:
- Identical boilerplate in every skill: rejected because it would flatten specialized craft and create the universal schema FR-025 forbids.
- Removing all local handoffs: rejected because subtype dispatch and return-to-parent behavior belong at the receiving capability.

## Decision 3: Compose four existing workflow families

**Decision**: Define read, write, ingest, and maintenance as recurring compositions of existing capabilities:
- Read: route → focused retrieval → sufficient evidence → answer; no canonical wiki mutation.
- Write: route → retrieve/resolve owner → mutate through the owner contract → scoped validation → close.
- Ingest: source evidence → destination owner → write/track → scoped validation → retrieval refresh → close.
- Maintenance: health/lint observation → explicit next action → deterministic fixer or artifact owner → rerun affected scope → close green.

**Rationale**: Existing query, transaction, lint, repair-plan, and health surfaces already implement the required seams. Guidance should consume them rather than reconstruct policy.

**Alternatives considered**:
- A workflow engine: rejected; no second execution authority is needed.
- One giant serialized recipe: rejected; real dependencies remain serial while disjoint write surfaces remain concurrent.

## Decision 4: Treat health and CLI contracts as observation owners

**Decision**: `specs/027-wiki-agent-cli/contracts/wiki-cli.md` plus `scripts/wiki` and `tools/wiki_ops` remain authoritative for query/lint/health result shapes. `wiki-status` owns status/delta/insights evidence, not a competing action planner; health ordering remains authoritative.

**Rationale**: Query, lint, and health already return compact, stable, actionable evidence. A second ranking layer creates drift and violates FR-022.

**Alternatives considered**:
- Rebuild observation output for this feature: rejected absent a demonstrated contract failure.
- Preserve the separate status ranking: rejected because it duplicates health action ordering.

## Decision 5: Make read-only mean no canonical mutation

**Decision**: Read capabilities do not mutate campaign pages, manifests, indexes, or logs. Runtime caches and command timing records allowed by the CLI contract are operational observations, not canonical wiki mutation. Any content write or durable insight report is a write workflow and requires explicit mutation intent.

**Rationale**: This resolves the current ambiguity where read guidance can claim read-only while appending `log.md` or writing `_insights.md`.

**Alternatives considered**:
- Call all side effects read-only: rejected because it makes SC-005 untestable.
- Ban operational caches/traces: rejected because they are existing derived observation surfaces, not campaign canon.

## Decision 6: Reuse cold-context skill evaluation

**Decision**: Add focused route evaluations using the existing skill-creator with-skill/baseline pattern, typed assertions, isolated workspaces, and the weakest sufficient executor model. Cover direct routing, parent return, dependency order/concurrency, bounded context, read/write isolation, validation feedback, output-contract preservation, forbidden machinery, and every named failure.

**Rationale**: Static heading checks do not prove agent behavior. The existing trigger-only runner proves invocation but not routing or completion; the existing benchmark pattern supports transcript/output assertions.

**Alternatives considered**:
- Trigger-only evaluation: rejected as insufficient for FR-027.
- One end-to-end scenario: rejected because a plausible final artifact can hide wrong routing or premature completion.
- Strongest model executor: rejected by constitution XXVI.

## Decision 7: Synchronize only governing counterparts

**Decision**: Guidance-only route/handoff changes update the owning skill, root/docs authority, and cold eval. Template/contract/Vale sources change only when artifact validity or validation behavior changes. Generated Vale vocabulary is never hand-edited.

**Rationale**: Constitution XXIV requires relevant systems to remain synchronized, not unrelated churn. The existing policy-owner map identifies governing counterparts.

**Alternatives considered**:
- Touch every template and Vale rule for prose-only routing changes: rejected as weightless duplication.
- Ignore counterparts entirely: rejected because output-shape or validation changes would drift.

## Resolved clarifications

- **Language/runtime**: Agent-facing Markdown/YAML plus existing Python 3.12+ evaluation and CLI tooling; no new runtime.
- **Storage**: Existing repository guidance, eval JSON, and wiki files; execution state remains ephemeral.
- **Testing**: Cold-context behavioral evaluation through skill-creator conventions; existing pytest public seams only if runtime contracts change.
- **Platform**: Existing local macOS/CI-compatible repository workflow.
- **Performance**: Reduce unrelated first-turn context and duplicate instruction load without weakening protected D&D quality; measure only equivalent work.
- **Accountability**: An issue must be linked or created before implementation begins; planning may complete before that gate.
