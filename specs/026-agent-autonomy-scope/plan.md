# Implementation Plan: Agent Autonomy Scope

**Branch**: `026-agent-autonomy-scope` | **Date**: 2026-09-18 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/026-agent-autonomy-scope/spec.md`

```text
work_class: agent-system
route: full-sdd
reason: reusable agent-system rules for four-line canon, lint-as-contract, no approval wait
```

## Summary

Replace Work gates with the four-line canon rule. File what those lines make canon. Encode FR-001–FR-003 and FR-013 as checkable rules (`AGENT001`–`AGENT003`). Bulk-rename existing agent-facing files to that placement rule and update old instruction files until green. Amend constitution X/XV/XVII and Operating Boundaries in the same change so AGENTS.md does not contradict XVI. Skill/instruction review stays on existing `skill-creator` evals. No new checklist, PR template, review skill, or lint framework.

## Technical Context

**Language/Version**: Markdown agent instructions; Python 3 stdlib checker (same shape as `scripts/check-policy-conflicts`)

**Primary Dependencies**: Existing `AGENTS.md`, constitution, `docs/agents/work.md`, wiki-lint, `rules/registry.yml`, `skill-creator` eval loop. No new packages.

**Storage**: Vault markdown + YAML frontmatter. Canon is not a separate store.

**Testing**: `scripts/check-agent-standards.py` + one pytest; cold-context quickstart V-001–V-008; skill/instruction diffs use existing `skill-creator` evals.

**Target Platform**: Agent instruction surface (OMP, Codex, Claude Code) plus wiki write path

**Project Type**: Agent infrastructure (skills/instructions primary; scripts supporting)

**Performance Goals**: N/A

**Constraints**: MUST NOT add Work gates or extra canon steps. MUST NOT use avoided term "autonomous GM". MUST NOT add a review checklist, PR template, or review skill (FR-007). MUST bulk-rename existing agent-facing files to AGENT002. MUST update every old instruction file to the new checkable standards. Wiki writes go to live vault paths.

**Scale/Scope**: Constitution MAJOR `3.0.0`; `AGENTS.md` / `wiki/AGENTS.md` / `docs/agents/*` / skill strips + kebab remorph of non-conforming agent-facing paths; three registry rules + one script + one test.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Domain Language | PASS | Canon / done-summary / lint contract. Avoid "autonomous GM". |
| II. Issues Are the Work Surface | PASS | Feature branch `026-agent-autonomy-scope`. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) has testable FR/SC. |
| IV. Behavioral Tests | PASS | Quickstart + AGENT001–003 + skill-eval for instruction diffs. |
| V. Single Source of Truth | PASS | Four-line canon in constitution; AGENTS.md points; rules execute. |
| VI. Agent-Shaped | PASS | Checker: args in, JSON out, exit status. |
| VII. Creative Judgment | PASS | No voice/method rules. |
| VIII. Safe Automation | PASS | FR-002 unattended; unsaid lore still not invented. |
| IX. Measured Efficiency | PASS | Delete Work-gate copies; one checker. |
| X. DM Owns Canon | PASS **after amendment** | Redefined to four-line canon in this feature. Shipping AGENTS.md without that amendment would FAIL XVI. |
| XII. Evidence Precedes Invention | PASS | Unsaid material is not canon; no wait. |
| XIV. Simplest Adequate Tool | PASS | One script + registry; no new framework. |
| XV. Autonomous Operation | PASS **after amendment** | Remove DM-approval boundary for novel content the user said. |
| XVI. Layering | PASS | Constitution owns the principle; AGENTS.md why/examples; rules/ the check. |
| XVII. Wiki Additive | PASS **after amendment** | File user/transcript/non-contradicting ingest; still no silent history overwrite. |
| XX. Lean | PASS | Strip Work-gate headers; do not copy the four lines into every skill. |
| XXI. Linter Root-Cause | PASS | Green-before-done; do not weaken AGENT001–003. |
| XXIII. Real Surfaces | PASS | Quickstart uses live vault/agent. |
| XXIV. Synchronized Content | PASS | Constitution + AGENTS.md + skills + registry/script in one feature. |

No unjustified violations. Gate passes **because** the plan amends X/XV/XVII rather than contradicting them.

## Project Structure

### Documentation (this feature)

```text
specs/026-agent-autonomy-scope/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── agent-autonomy.md
└── tasks.md             # Phase 2 — not this command
```

Replace stale `contracts/autonomy-boundary.md` (binary dm-gated table) with `contracts/agent-autonomy.md`.

### Source Code (repository root)

```text
.specify/memory/constitution.md          # MAJOR 3.0.0: X, XV, XVII, Operating Boundaries
AGENTS.md                                # four-line canon pointer, lint pointer, done-summary, identity
wiki/AGENTS.md                           # file-it; remove accept-before-write
docs/agents/work.md                      # no Propose/Decide wait; file what is canon
docs/agents/wiki-maintenance-loop.md     # no Autonomy table; Layer C = unsaid invent only
docs/agents/hybrid-sdd.md                # dm_acceptance not-required for user-said canon
docs/agents/policy-owners.yml            # drop acceptance_semantics wait
.agents/skills/**/SKILL.md               # delete ## Work gate sections
.agents/skills/**/*.md                   # kebab remorph of companions (checks.md, consolidate.md, …)
rules/registry.yml                       # AGENT001 AGENT002 AGENT003
scripts/check-agent-standards.py         # the checker
tests/test_agent_standards.py            # one pytest
```

**Structure Decision**: Instruction + constitution edits. One stdlib checker. Bulk-rename non-conforming agent-facing paths in the same change. Canonical four-line rule in constitution; AGENTS.md points; registry/script enforces.

**Owners**: one writer per file at implement time. Constitution then AGENTS.md then work.md then skill strips then remorph then checker (AGENT001/002 fail until strips and renames land). No parallel writes to `AGENTS.md` or constitution.

## Post-Design Constitution Check

| Principle | Status | Evidence |
|-----------|--------|----------|
| V. Single Source of Truth | PASS | [contracts/agent-autonomy.md](contracts/agent-autonomy.md) names constitution as the four-line owner. |
| X / XV / XVII | PASS | Amendment is in scope; lower layers point, do not restate competing gates. |
| XIV | PASS | One script; reuse skill-creator evals. |
| XVI | PASS | Principles in constitution; checks in registry; AGENTS.md why/examples. |
| XX | PASS | Skills lose Work-gate headers; they do not gain a copied table. |
| IV | PASS | Quickstart V-001–V-008; AGENT001–003; skill-eval. |
| XXI | PASS | Green-before-done is FR-012; checker BLOCK. |

**Post-design gate**: PASS. No `NEEDS CLARIFICATION`. Session 2026-09-18 clarifications absorbed (file user-said canon, mixed one summary, lint contract, bulk-rename + update every old instruction file).

## Complexity Tracking

> Fill ONLY if Constitution Check has violations that must be justified

None. The MAJOR constitution amendment is the compliant path, not a violation.
