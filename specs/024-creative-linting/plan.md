# Implementation Plan: Creative Linting

**Branch**: `024-creative-linting` | **Date**: 2026-09-17 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/024-creative-linting/spec.md`

## Summary

An executable lint-rule engine for canon, agency, temporal truth, knowledge boundaries, retrieval discipline, and creative heuristics — layered as a cross-cutting validation surface over the existing `wiki-lint` / `wiki-maintain` / `tools/lint_wiki.py` architecture. Rules live in YAML, have stable IDs and a five-level severity model, and run through typed evaluators (static first, semantic later). The engine plugs into the existing `scripts/wiki-lint` CLI, agent prep/wrapup loops, and `scripts/wiki-maintain` Layer A.

## Technical Context

**Language/Version**: Python 3.14 (matches `.venv`)

**Primary Dependencies**: [Vale](https://vale.sh/) v3.13.0 (already installed at `~/.local/bin/vale`) — static prose linting engine with custom YAML rules, markdown-aware scoping, and JSON output. Existing stack: `tools/lint_wiki.py` (deterministic lint engine, 546 LOC), `scripts/wiki-lint` (CLI wrapper), `scripts/wiki-maintain` (Layer A facade), `scripts/lint-obsidian-markdown`, `scripts/lint-literal-newlines`, `scripts/lint-wiki-write`. No new Python dependencies.

**Storage**: Filesystem — YAML rule definitions, JSON findings, JSON waiver/shadow telemetry files. No database.

**Testing**: `pytest` convention (existing `tests/` directory with `test_*.py` files). Python 3.14, stdlib `unittest`/`assert`-based tests.

**Target Platform**: macOS (darwin), repo-local execution. CI-compatible (graceful degradation when LLM unavailable via `CI=true`).

**Project Type**: CLI tool + agent-consumed library within an existing Obsidian wiki management repo.

**Performance Goals**: <10s for deterministic rules on the full corpus (~200 pages). Static evaluators: <1s per page. Semantic evaluators: bounded by LLM call latency (out of scope for Phase 1).

**Constraints**: Dependencies are permitted (PyYAML for registry parsing). Vale is already installed. Must compose with existing `tools/lint_wiki.py` findings (not replace them). Must not increase `wiki-lint --json` startup cost for the existing HARD checks. Token overhead for lint+repair ≤20% of generation cost.

**Scale/Scope**: ~15 initial rules across 6 families. ~200 wiki pages in the vault. 5-8 task bundles.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| I. Domain Language Is Binding | PASS | Rule IDs, severity levels, evaluator types, and bundle names become domain terms. Will add to `CONTEXT.md` if needed. |
| II. Issues Are the Work Surface | PASS | This work tracks through Spec Kit on branch `024-creative-linting`. |
| III. Spec Before System Change | PASS | Spec complete at `specs/024-creative-linting/spec.md`. |
| IV. Behavioral Tests | PASS | Fixture files (should-fail/should-pass/ambiguous) are the behavioral test surface per FR-009/Story 9. `test_creative_lint.py` will cover registry, evaluator dispatch, bundle resolution, and finding schema. |
| V. Single Source of Truth | PASS | Rule definitions in YAML are the single owner. Skills reference by ID (FR-012). No prose duplication. |
| VI. Software Is Agent-Shaped | PASS | CLI in/out, JSON structured findings, exit status. Extends existing `scripts/wiki-lint` surface. |
| VII. Creative Judgment Is Protected | PASS | Core design: BLOCK correlates only with truth/safety/agency/schema (FR-016). Taste never BLOCKs. WARN/INFO are diagnostics, not mandates (FR-006). |
| VIII. Safe Automation Runs Unattended | PASS | Deterministic evaluators are idempotent scripts. Shadow mode records without affecting output. |
| IX. Measured, Quality-Bounded Efficiency | PASS | Task bundles limit rule scope per task (FR-004). Deterministic evaluators run without LLM cost. Token overhead is measurable (SC-007). |
| X. DM Owns Canon | PASS | Linter surfaces findings; DM remains authority. Waivers require DM approval. Canon rules reference wiki as source of truth. |
| XI. Players Choose; The World Acts | PASS | AGENCY rules detect authored PC decisions — this principle is a primary consumer. |
| XII. Evidence Precedes Invention | PASS | CANON/KNOW rules enforce retrieval before invention. |
| XVI. The Simplest Adequate Tool | PASS | Extends existing `tools/lint_wiki.py` rather than building a new framework. YAML rules parsed with minimal code. No new dependencies. |
| XVIII. Constitutional Layering | PASS | Rule definitions are lower-layer (YAML files). Constitution principles are the invariants being encoded as rules. |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/024-creative-linting/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
# Vale static rules
.vale.ini                     # Vale configuration
styles/
└── CoDM/                    # Custom Vale style (one YAML per rule)
    ├── AGENCY001.yml
    ├── AGENCY002.yml
    ├── AGENCY003.yml
    ├── KNOW001.yml
    ├── KNOW002.yml
    ├── TEMP001.yml
    ├── SCENE001.yml
    └── SCENE002.yml

# Python orchestration + symbolic evaluators
tools/
├── lint_wiki.py              # Existing (unchanged)
├── creative_lint/
│   ├── __init__.py           # Package init
│   ├── registry.py           # Rule registry: load YAML metadata, lookup by ID
│   ├── engine.py             # Orchestrator: invoke Vale + symbolic evaluators, merge findings
│   ├── evaluators/
│   │   ├── __init__.py
│   │   └── symbolic.py       # Symbolic evaluators (cross-page graph, state, chronology)
│   ├── bundles.py            # Bundle resolution: task → rule set with severity gates
│   ├── severity.py           # Five-level severity model + status computation
│   ├── vale_adapter.py       # Invoke Vale CLI, parse JSON, map to finding schema
│   ├── waivers.py            # Waiver loading, matching, expiry (Phase 2+)
│   └── shadow.py             # Shadow-mode recording (Phase 2+)

# Rule metadata + bundles
rules/
├── registry.yml              # All rule metadata (single source of truth)
└── bundles.yml               # Task-specific bundle definitions

# Tests
tests/
├── test_creative_lint.py     # Registry, engine, evaluators, bundles, severity
└── fixtures/
    └── creative_lint/        # Per-rule fixture files (should-fail/pass/ambiguous)

# CLI
scripts/
├── wiki-lint                 # Extended: new subcommands (task, rule, --severity filter)
```

**Structure Decision**: Three-layer composition. Vale (`styles/CoDM/`) handles static prose-pattern matching with markdown awareness. `tools/creative_lint/` Python package handles symbolic evaluators, orchestration, bundle routing, and the unified finding schema. `tools/lint_wiki.py` continues owning structural HARD checks unchanged. `scripts/wiki-lint` CLI orchestrates all three.

## Complexity Tracking

No constitution violations to justify.
