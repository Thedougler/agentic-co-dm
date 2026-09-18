# Implementation Plan: Agent-Safe Wiki Operations

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/025-agent-safe-wiki-ops/spec.md`

## Summary

Four reusable layers — QMD-backed identity resolution, typed semantic mutations, scoped lint with template contracts, and batched transaction finalization — that let agents lint, repair, and consolidate wiki content without composing line-number patches, guessing page identity, regex-editing the 107KB index, creating redirect stubs, or triggering redundant QMD refreshes. Every open error in scope (e-10, e-12 through e-38) traces to a missing layer; this spec fills those gaps with Python CLI commands consistent with the existing `scripts/` pattern.

## Technical Context

**Language/Version**: Python 3.14 (matches `.venv` and existing `scripts/`)

**Primary Dependencies**: No new dependencies. Existing stack: Python stdlib, QMD CLI/content index for similarity, PyYAML already used by 024-creative-linting, `scripts/wiki-bulk-ops` (frontmatter parsing, link rewriting, atomic writes, rename, replace, tag normalize), `tools/lint_wiki.py` (structural HARD checks), `scripts/manifest.py` (manifest CRUD), `scripts/wiki-lint` (CLI wrapper), `scripts/wiki-maintain` (Layer A facade). Template files at `wiki/templates/*.md`. 024-creative-linting adds `tools/creative_lint/` (registry, engine, findings, severity, bundles) and `rules/` (registry.yml, bundles.yml).

**Storage**: Filesystem — wiki markdown pages, `wiki/index.md` (107KB single-line structured index), `wiki/.manifest.json` (ingest provenance), template YAML contracts (new, co-located with templates).

**Testing**: `pytest` convention (existing `tests/` with `test_*.py`). Temp-dir vault fixtures per `test_wiki_bulk_ops.py` pattern.

**Target Platform**: macOS (darwin), repo-local. CI-compatible.

**Project Type**: CLI tools + library within an existing Obsidian wiki management repo.

**Performance Goals**: Identity resolution <2s for full vault (~200 pages). Mutation operations <1s per file. Transaction finalization (index + manifest + QMD) <10s total.

**Constraints**: No new dependencies. Compose with existing `scripts/wiki-bulk-ops` utilities (frontmatter parsing, link rewriting, atomic writes), QMD similarity, `tools/lint_wiki.py`, and `scripts/wiki-lint`. Mutations must be atomic — fail cleanly with original untouched. Single-writer per artifact (Constitution XIV). Template contracts are YAML files co-located with templates, not changes to the markdown templates themselves. Merge operations remove obsolete pages and MUST NOT create redirect stubs. The QMD hook is a standalone shell script (not a git hook) callable by any harness; it runs a count-bounded embedding pass (at most N pages per invocation), produces zero output on success, and exits 0 silently when QMD is not installed.

**Scale/Scope**: ~200 wiki pages. ~28 templates. 28 open errors to regress (e-10, e-12 through e-38). 4 layers, ~6 task phases.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| I. Domain Language Is Binding | PASS | New terms (mutation operation, scope object, identity resolution, template contract, repair class, transaction) will be added to domain vocabulary if needed. All match spec. |
| II. Issues Are the Work Surface | PASS | Tracked through Spec Kit on branch `025-agent-safe-wiki-ops`. |
| III. Spec Before System Change | PASS | Spec complete at `specs/025-agent-safe-wiki-ops/spec.md`. |
| IV. Behavioral Tests | PASS | Each story has an independent test. Causal regression tests for every open error (SC-007). |
| V. Single Source of Truth | PASS | Template contracts own section semantics (not restated in skills). Identity signals come from existing frontmatter, manifest, wikilinks, filenames, and QMD similarity; legacy redirect stubs are lint errors. Mutation operations are the single owner of wiki state transitions. |
| VI. Software Is Agent-Shaped | PASS | All new surfaces are Python CLI: args in, JSON out, exit status. Extend existing `scripts/` pattern. |
| VII. Creative Judgment Is Protected | PASS | Deterministic repairs are structural only (links, frontmatter, index entries). No creative content mutation without human review. Repair classes explicitly separate deterministic from judgment-only. |
| VIII. Safe Automation Runs Unattended | PASS | Mutations verify preconditions and fail cleanly. Transactions are atomic. Ambiguous identity blocks automatic mutation. |
| IX. Measured, Quality-Bounded Efficiency | PASS | Scoped lint eliminates full-vault scans. Batched finalization eliminates redundant QMD refreshes. Compact output stays under 1000 tokens for agent consumption. |
| X. DM Owns Canon | PASS | Mutations that change canon content require DM acceptance. Identity resolution surfaces ambiguity for human decision rather than guessing. |
| XIV. Designated Writers Have Bounded Concurrency | PASS | Mutation preconditions (content hash verification) enforce single-writer semantics. |
| XVI. The Simplest Adequate Tool | PASS | Reuses `wiki-bulk-ops` frontmatter parsing, link rewriting, and atomic writes. Extends existing lint infrastructure. No new frameworks. |
| XVIII. Constitutional Layering | PASS | Feature behavior in spec/contracts. Implementation in plan/tasks. No constitution duplication. |
| XIX. Wiki Is Additive, Self-Sealing | PASS | Mutations are additive with provenance. Merges record `merged_into` transitions. No silent deletion of history. |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/025-agent-safe-wiki-ops/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
scripts/
├── wiki-bulk-ops         # Existing (extended: new mutation subcommands)
├── wiki-lint             # Existing (extended: scoped lint, template conformance)
├── manifest.py           # Existing (extended: identity transitions)
├── wiki-identity         # New: identity resolution CLI
└── qmd-hook.sh           # New: standalone QMD hook (count-bounded, silent no-op)

tools/
├── lint_wiki.py          # Existing (extended: scope filtering, template contracts)
├── creative_lint/        # Existing from 024 (extended: repair class on findings)
└── wiki_ops/             # New: mutation + transaction library
    ├── __init__.py
    ├── identity.py       # Identity resolution: resolve/ambiguous/distinct
    ├── mutations.py      # Typed mutation operations with preconditions
    ├── transactions.py   # Multi-file transaction coordination + finalization
    ├── index_ops.py      # Structured index.md parsing and entry operations
    └── manifest_ops.py   # Manifest identity transitions (merged_into, etc.)

wiki/templates/
├── contracts/            # New: machine-readable template contracts
│   ├── faction.yml       # Section semantics for faction template
│   └── ...               # One per template

tests/
├── test_wiki_ops.py      # New: identity, mutations, transactions
├── test_wiki_bulk_ops.py # Existing
└── fixtures/
    └── wiki_ops/         # New: test vault fixtures
```

**Structure Decision**: New mutation/transaction logic goes in `tools/wiki_ops/` as a library consumed by CLI scripts. CLI surfaces extend existing `scripts/wiki-bulk-ops` and `scripts/wiki-lint` with new subcommands, plus one new `scripts/wiki-identity` for identity resolution. Template contracts are YAML files under `wiki/templates/contracts/`. This preserves the existing pattern: library code in `tools/`, CLI entry points in `scripts/`, tests in `tests/`.

### Harness Integration (final implementation phase)

Wire `scripts/qmd-hook.sh` into the OMP harness so wiki-write boundaries invoke the hook automatically. OMP currently has no wiki-write hook infrastructure (`.omp/config.yml` has no hooks section; `.omp/RULES.md` has no wiki-write trigger). Implementation adds the call site so OMP agents get the same post-write QMD maintenance that Claude Code agents get through their existing `scripts/qmd-maintain.sh` call. The hook is harness-agnostic by design — OMP wiring is configuration/instruction, not a hook redesign.

## Post-Design Constitution Check

| Principle | Status | Evidence |
|---|---|---|
| V. Single Source of Truth | PASS | Template contracts own section semantics. Identity signals come from existing frontmatter/manifest. Mutation operations are the single owner of wiki state transitions. Policy ownership registry prevents restated rules. |
| VI. Software Is Agent-Shaped | PASS | All new surfaces are CLI: args in, JSON out, exit status. `wiki-identity`, `wiki-bulk-ops mutate`, `wiki-lint --scope`, `wiki-bulk-ops transact` follow the existing `scripts/` pattern. |
| VIII. Safe Automation Runs Unattended | PASS | Mutations verify preconditions atomically. Transactions roll back on failure. Ambiguous identity blocks automatic mutation and derived maintenance is deferred. Deterministic repairs are structural-only. |
| IX. Measured, Quality-Bounded Efficiency | PASS | Scoped lint eliminates full-vault scans. Batched finalization eliminates redundant QMD refreshes. Compact JSON output stays under 1000 tokens for agent consumption. |
| XIV. Designated Writers Have Bounded Concurrency | PASS | Content-hash preconditions enforce single-writer semantics per section. Transaction validation rejects overlapping mutations. |
| XVI. The Simplest Adequate Tool | PASS | Reuses `wiki-bulk-ops` frontmatter parsing, link rewriting, and atomic writes. stdlib hashlib for preconditions. Existing QMD provides content similarity. No new frameworks or dependencies. |
| XIX. Wiki Is Additive, Self-Sealing | PASS | Merges record `merged_into` transitions. Obsolete pages are removed without redirect stubs. Index and manifest updated atomically. No silent deletion of provenance. |

**Post-design gate**: PASS. No `NEEDS CLARIFICATION` remains. All four layers (identity, mutation, scope, transaction) compose through existing CLI patterns. Template contracts are YAML co-located with templates. Error regression tests cover all 28 open errors in SC-007.

## Complexity Tracking

No constitution violations to justify.
