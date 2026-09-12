# Parity Sign-off

**Date:** 2026-08-09
**ADR:** ADR-0042 — wiki-cli is engine of record

## Live parity result

`uv run python -m wiki_cli.parity --live` → **exit 0** (all ported rules, whole vault, 0 diffs).

Parity = detection parity: `(rule_id, rel_path, line)` sets match between npm and wiki-cli engines.

## Test suite

- `uv run pytest -q` → 380 passed, 1 skipped
- `uv run ruff check src tests` → clean

## Deferred legacy-bug fixes

| Module | Bug |
|--------|-----|
| `src/wiki_cli/rules/grandfather_link.py` | LEGACY-BUG: the legacy module reads `parent:`, but ADR-0040's `within:` is the canonical key; ported bug-compatible, fix post-retirement |
