# Implementation Plan: Agent Autonomy Scope

**Branch**: `026-agent-autonomy-scope` | **Date**: 2026-09-18 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/026-agent-autonomy-scope/spec.md`

```text
work_class: agent-system
route: full-sdd
reason: reusable AGENTS.md rule for autonomous wiki ops vs DM-gated campaign-fact writes
```

## Summary
Operationalize Constitution XV/X as one binary table in `AGENTS.md`. Agents execute FR-002 without a Work prompt and emit a short done-summary. Wait only when the user asked to make something new, or the op invents canon / reconciles contradiction. Mixed: autonomous first + done-summary, then Work in the same turn. Instruction changes reviewed with existing `skill-creator` evals. No new code, checklist, PR template, or review skill.

## Technical Context

**Language/Version**: Markdown agent instructions; no new Python

**Primary Dependencies**: Existing `AGENTS.md`, `docs/agents/work.md`, `docs/agents/wiki-maintenance-loop.md`, wiki-lint, wiki-ingest. No new packages.

**Storage**: Vault markdown + YAML frontmatter. Classification is not stored.

**Testing**: Cold-context behavioral validation ([quickstart.md](quickstart.md) V-001–V-008). Skill/instruction diffs use existing `skill-creator` evals. No new test framework.

**Target Platform**: Agent instruction surface (OMP, Codex, Claude Code)

**Project Type**: Agent infrastructure (skills/instructions primary; scripts supporting)

**Performance Goals**: N/A

**Constraints**: Must not weaken Work for FR-003. Must not use avoided term "autonomous GM". Must not add a third classification. Staged writes stay orthogonal. Dedup merge stays Nick-gated. MUST NOT add a review checklist, PR template, or review skill (FR-007).

**Scale/Scope**: Six instruction files. Spec artifacts only under `specs/026-agent-autonomy-scope/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Domain Language Is Binding | PASS | Campaign-fact / Work / DM. Avoid "autonomous GM". |
| II. Issues Are the Work Surface | PASS | Feature branch `026-agent-autonomy-scope` is the Spec Kit surface. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) has testable FR/SC. |
| IV. Behavioral Tests | PASS | Quickstart V-001–V-008; SC-005 two-agent classify. |
| V. Single Source of Truth | PASS | Table lives only in `AGENTS.md`. |
| VI. Agent-Shaped | PASS | Positive table + named fail modes in contract. |
| VII. Creative Judgment Is Protected | PASS | No creative-method constraint. |
| VIII. Safe Automation Runs Unattended | PASS | FR-002 unattended. |
| IX. Measured Efficiency | PASS | One table replaces inferred multi-doc pauses. |
| X. DM Owns Canon | PASS | FR-003 stays Work-gated. |
| XIV. Simplest Adequate Tool | PASS | Table, not a classifier script. |
| XV. Autonomous Operation | PASS | This feature. |
| XVI. Constitutional Layering | PASS | Principles stay in constitution; table in AGENTS.md. |
| XVII. Wiki Additive / Self-Sealing | PASS | Structural repair only; facts still accepted. |
| XX. Lean Agent-Facing Documents | PASS | Table + one decision sentence. |
| XXI. Linter Root-Cause | PASS | Over-ask removed at source files, not exempted. |
| XXIII. Real Surfaces | PASS | Quickstart uses the live vault/agent, not fixtures-only. |
| XXIV. Synchronized Content Systems | PASS | Instruction change only; templates/Vale unchanged. |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/026-agent-autonomy-scope/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── autonomy-boundary.md
└── tasks.md             # Phase 2 — not this command
```

### Source Code (repository root)

```text
AGENTS.md                                      # table + project identity
docs/agents/work.md                            # Work scope vs FR-002
docs/agents/wiki-maintenance-loop.md           # Layer A may apply FR-002
.agents/skills/wiki-lint/SKILL.md              # autonomous structural repair
.agents/skills/wiki-lint/CONSOLIDATE.md        # confirm only non-FR-002
.agents/skills/wiki-ingest/SKILL.md            # named ingest, no second ask
```

**Structure Decision**: Instruction edits only. Canonical table in `AGENTS.md`. Skills defer.

**Owners**: one writer per file at implement time. No parallel writes to `AGENTS.md`.

## Post-Design Constitution Check

| Principle | Status | Evidence |
|-----------|--------|----------|
| V. Single Source of Truth | PASS | [contracts/autonomy-boundary.md](contracts/autonomy-boundary.md) names `AGENTS.md` as the only table. |
| X. DM Owns Canon | PASS | Wait rule matches FR-003; invent/reconcile/new-owner stay Work-gated; no stubs. |
| XIV. Simplest Adequate Tool | PASS | No classifier binary; markdown table. Reuse `skill-creator` evals. |
| XV. Autonomous Operation | PASS | FR-002 closed list; kebab remorph aligned with 2026-09-14 greenlight; done-summary not a pause. |
| XVI. Layering | PASS | Constitution unchanged. |
| XX. Lean | PASS | Skills get pointer-level deltas, not copied tables. No extra review skill. |
| VII. Creative Judgment | PASS | No voice/method rules. |
| IV. Behavioral Tests | PASS | Quickstart V-001–V-008; SC-005 two-agent classify; skill-eval for instruction diffs. |

**Post-design gate**: PASS. No `NEEDS CLARIFICATION`. Session 2026-09-18 clarifications absorbed (done-summary, same-turn mixed, wait-only-for-new, skill-eval reuse). Dedup merge deliberately excluded from autonomous (research R-002).

## Complexity Tracking

No violations to justify.
