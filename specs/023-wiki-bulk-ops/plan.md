# Implementation Plan: Wiki Bulk Operations

**Branch**: `023-wiki-bulk-ops` | **Date**: 2026-09-17 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/023-wiki-bulk-ops/spec.md`

## Summary

Provide a single Python CLI script (`scripts/wiki-bulk-ops`) that agents invoke for token-efficient, idempotent bulk operations on the Obsidian wiki vault: entity rename (with wikilink rewrite), find-and-replace (with markdown safety zones), frontmatter mutation, broken-link repair (auto-resolve via git history/aliases/fuzzy matching + explicit mapping), tag normalization (against taxonomy), and orphan detection (report-only). Every operation supports `--dry-run` and produces machine-readable JSON output. The design generalizes the existing `remorph-*` script patterns into one composable tool.

## Technical Context

**Language/Version**: Python 3.14 (matches project `.venv`; stdlib only — no new dependencies)

**Primary Dependencies**: None beyond stdlib (`argparse`, `re`, `json`, `pathlib`, `dataclasses`, `sys`, `shutil`, `tempfile`)

**Storage**: Filesystem — markdown files under `OBSIDIAN_VAULT_PATH` (default `wiki/`)

**Testing**: Assert-based `__main__` self-check in the script + one `tests/test_wiki_bulk_ops.py` using stdlib `unittest` (matches project pattern)

**Target Platform**: macOS / Linux (Darwin 25.x primary)

**Project Type**: CLI script (agent-shaped: args in, JSON/text out, exit codes)

**Performance Goals**: Full-vault rename across 1565 files in <5s wall clock

**Constraints**: Zero external dependencies; must preserve Obsidian markdown syntax; must be idempotent; writes go to live vault paths


MOC eligibility: generate navigation pages only for folders with at least two direct markdown pages or at least one eligible child MOC. One-page leaf folders are not useful navigation surfaces; stale generated MOCs are removed on regeneration. Generated MOCs remain structural pages and are excluded from identity and template-conformance checks.
**Scale/Scope**: ~1565 markdown files, ~44k total lines, single vault

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| I. Domain Language | PASS | Uses existing wiki vocabulary (wikilink, frontmatter, entity, vault) |
| III. Spec Before System Change | PASS | `spec.md` written and accepted |
| IV. Behavioral Tests | PASS | Will add behavioral test at public seam (CLI in/out) |
| V. Single Source of Truth | PASS | One script, one authority; generalizes remorph pattern |
| VI. Agent-Shaped | PASS | Args in, JSON/text out, stderr errors, exit codes |
| VII. Creative Judgment | N/A | Deterministic structural tool, no creative output |
| VIII. Safe Automation | PASS | Dry-run default; idempotent; preserves data |
| IX. Measured Efficiency | PASS | Replaces ~100+ tool calls with one invocation |
| XVII. Simplest Tool | PASS | Single Python script, stdlib only, no framework |
| XX. Additive Wiki | PASS | Deterministic maintenance; no lore invention |

No violations. No complexity justification needed.

## Project Structure

### Documentation (this feature)

```text
specs/023-wiki-bulk-ops/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── cli-contract.md
└── tasks.md             # Phase 2 output (speckit-tasks)
```

### Source Code (repository root)

```text
scripts/
└── wiki-bulk-ops        # Single executable Python script (chmod +x, shebang)

tests/
└── test_wiki_bulk_ops.py  # Behavioral tests at CLI seam
```

**Structure Decision**: Single script under `scripts/` — matches the existing `remorph-*` pattern exactly. No `src/` tree, no package, no library split. The remorph scripts prove this pattern works for vault-wide file transformations at this scale.

## Constitution Re-Check (Post-Phase 1)

All principles re-checked — no new violations. MOC generation (FR-017–FR-022) added to data model, CLI contract, and quickstart; it is deterministic structural maintenance (XX), agent-shaped (VI), and does not invent lore (VII/X). No complexity justification needed.

## Complexity Tracking

No violations to justify.
