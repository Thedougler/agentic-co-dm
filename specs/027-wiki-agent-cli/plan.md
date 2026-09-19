# Implementation Plan: Agent-Shaped Wiki CLI

**Branch**: `027-wiki-agent-cli` | **Date**: 2026-09-19 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/027-wiki-agent-cli/spec.md`

```text
work_class: engineering
route: full-sdd
reason: new public wiki command and default result contract; FR-018 updates agent lint/query/health invocations (run health, do next) in the same change
```

## Summary

One `scripts/wiki` command (`lint`, `query`, `health`) that composes existing structural lint, Vale, Layer A maintenance, sitting/efficiency/error trackers, and qmd retrieval. Default lint stdout is summary fields plus every finding grouped by file (Vale on, 1-based lines). `--pretty` is the only human text; `--json` and `--full` are no-ops on the default dump. Unchanged files reuse checker results from `$VAULT/_meta/lint-cache.json` keyed by content sha256 + config digest. Each run appends a `record_kind=command` row to the existing `.local/efficiency/traces.jsonl` and includes compact `timing` on stdout. Health is a compact snapshot (no findings dump) with `trends.slowest_commands`, `trends.token_heaviest`, ordered `focus`, and `next`. Creative lint stays on `scripts/wiki-lint`. `scripts/wiki-maintain --report` aliases `wiki health`. No npm wrappers. No skill-eval dashboard.

## Technical Context

**Language/Version**: Python 3.12+ (matches `pyproject.toml` `requires-python`)

**Primary Dependencies**: Existing: stdlib, PyYAML, Vale, tiktoken, `tools/lint_wiki.py`, `tools/wiki_ops/cli.py` (`configured_vault`, `emit_json`, `emit_error`), `scripts/wiki-lint`, `scripts/wiki-maintain`, `scripts/token-count.py`, `scripts/context-waste-scan.py`, `scripts/error-ledger.py`, `scripts/efficiency-trace.py`, qmd CLI. No new packages.

**Storage**: Wiki markdown on disk. Checker cache: `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Not git-canonical wiki content. Health **reads** `sittings.jsonl`, `errors.md`, `.local/efficiency/traces.jsonl`. Every `wiki` subcommand **appends** one command record to that same traces file (not a second ledger).

**Testing**: pytest temp-vault pattern in `tests/test_wiki_ops.py`. New `tests/test_wiki_cli.py`. Cold-context smol subject for SC-008 and SC-009.

**Target Platform**: macOS/darwin local repo; CI-compatible except qmd query (needs local LLM; `env -u CI`).

**Project Type**: CLI within existing wiki-ops repo.

**Performance Goals**: Unknown path fails in <1s (SC-007). Second identical lint does not re-run Vale on cached pages (SC-003). Default lint dump is complete (no 8 KB cap).

**Constraints**: No fuzzy path matching. No TTY detection. No owner guessing. No creative-hydra migration. No second benchmark file. No skill-eval inventory. No npm wrappers. Machine errors on stdout (named VI split; see Complexity Tracking). Agent instruction examples must not keep `./scripts/wiki-lint --json wiki/` as the default structural pass.

**Scale/Scope**: One dispatcher script, thin dump/cache/pretty/health helpers under `tools/wiki_ops/`, health alias, small `efficiency-trace` command-record accept path, skill/AGENTS command-string updates. Does not replace `tools/lint_wiki.py`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Domain Language | PASS | Wiki / Search index. Product terms worklist, finding record, file group, health snapshot, command timing record. |
| II. Issues Are the Work Surface | PASS | Feature `027-wiki-agent-cli`. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) has FR/SC; grill + clarify 2026-09-19 locked dump, timings, token-heaviest, skill-evals out. |
| IV. Behavioral Tests | PASS | pytest on the CLI seam + quickstart V-008/V-009 cold subjects. |
| V. Single Source of Truth | PASS | Contract owns the result shape; skills point at `scripts/wiki`; lint_wiki remains checker owner; one traces file. |
| VI. Agent-Shaped | PASS with named split | Args in, compact JSON out, exit 0/1/2. Machine errors on stdout (wiki-ops `emit_error`); `--pretty` errors on stderr. Spec Assumptions. |
| VII. Creative Judgment | PASS | No voice/method rules. |
| VIII. Safe Automation | PASS | Cache and health are deterministic; unknown paths fail closed; timing append is best-effort. |
| IX. Measured Efficiency | PASS | Cache skips Vale on unchanged bytes. Default lint dump is complete by clarify (not 8 KB). Health stays compact (no findings dump, no raw traces). |
| X. DM Owns Canon | PASS | No wiki fact invention; `focus` layout items only from existing remorph/layout plans. |
| XII. Evidence Precedes Invention | PASS | Query does not invent hits; lint does not invent owners. |
| XIV. Simplest Adequate Tool | PASS | Compose existing checkers and the existing traces file; one new `scripts/wiki`. |
| XV. Autonomous Operation | PASS | Unattended lint/health; agents act on `next` without a DM wait. |
| XVI. Layering | PASS | Contract owns CLI behavior; AGENTS.md/skills only retarget invocations. |
| XVII. Wiki Additive | PASS | Cache is derived; live pages unchanged by this CLI. |
| XX. Lean | PASS | Do not copy the JSON schema into every skill. |
| XXI. Linter Root-Cause | PASS | Checkers unchanged; default output is the defect list. |
| XXIII. Real Surfaces | PASS | Quickstart on configured vault; temp vaults for fail-closed. |
| XXIV. Synchronized Content | PASS | Skills + standing command examples update with the CLI. |
| XXV. Carve-Outs | PASS | Creative hydra left on `wiki-lint` is deferred scope, not a rule exclude list. |

Gate: PASS. VI stdout errors are the existing wiki-ops convention named in the spec, not a silent contradiction.

## Project Structure

### Documentation (this feature)

```text
specs/027-wiki-agent-cli/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── wiki-cli.md
└── tasks.md             # Phase 2 — not this command
```

### Source Code (repository root)

```text
scripts/wiki                 # New dispatcher: lint | query | health
scripts/wiki-lint            # Unchanged creative hydra; structural path stays for existing tests
scripts/wiki-maintain        # --report aliases wiki health
scripts/efficiency-trace.py  # Accept record_kind=command on the existing traces stream

tools/wiki_ops/
├── cli.py                   # Existing emit_json / resolve_vault
├── worklist.py              # New: summary fields + files dump from a lint report
├── lint_cache.py            # New: per-file checker cache (sha256 + config digest)
├── health.py                # New: compose Layer A + trends + focus/next
├── timing.py                # New: duration + append command record
└── pretty.py                # New: --pretty text for lint/query/health

tests/test_wiki_cli.py       # New behavioral tests

.agents/skills/wiki-lint/SKILL.md
.agents/skills/wiki-lint/evals/evals.json
.agents/skills/wiki-status/SKILL.md   # health invocation if present
AGENTS.md                    # Standing lint/query/health command examples only
```

**Structure Decision**: New public command is `scripts/wiki`. Helpers stay in `tools/wiki_ops/` next to `cli.py`. Command timings stay in `.local/efficiency/traces.jsonl`. Do not add `src/`. Do not fold creative lint into the dispatcher this sitting.

## Post-Design Constitution Check

Same table as above. Design artifacts: [research.md](research.md), [data-model.md](data-model.md), [contracts/wiki-cli.md](contracts/wiki-cli.md), [quickstart.md](quickstart.md). No new `NEEDS CLARIFICATION`. Cache path, qmd flags, command-record discriminator, `focus` cap 5, and `next` = `focus[0]` are resolved. Gate still PASS.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| VI: machine errors on stdout | Agents load one stream (`emit_error` already) | stderr-only errors force a second parse; spec Assumptions name the split |
