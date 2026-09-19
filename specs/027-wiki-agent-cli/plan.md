# Implementation Plan: Agent-Shaped Wiki CLI

**Branch**: `027-wiki-agent-cli` | **Date**: 2026-09-19 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/027-wiki-agent-cli/spec.md`

```text
work_class: engineering
route: full-sdd
reason: new public wiki command and default result contract; FR-018 updates agent lint/query invocations in the same change
```

## Summary

One `scripts/wiki` command (`lint`, `query`, `health`) that composes existing structural lint, Vale, Layer A maintenance, and qmd retrieval. Default stdout is a compact worklist/snapshot agents can load; `--pretty` is the only human text; `--json` is a no-op. Unchanged files reuse checker results from `$VAULT/_meta/lint-cache.json`. Creative lint stays on `scripts/wiki-lint`. `scripts/wiki-maintain --report` aliases `wiki health`.

## Technical Context

**Language/Version**: Python 3.12+ (matches `pyproject.toml` `requires-python`)

**Primary Dependencies**: Existing: stdlib, PyYAML, Vale, tiktoken, `tools/lint_wiki.py`, `tools/wiki_ops/cli.py` (`configured_vault`, `emit_json`, `emit_error`), `scripts/wiki-lint`, `scripts/wiki-maintain`, `scripts/token-count.py`, `scripts/context-waste-scan.py`, qmd CLI. No new packages.

**Storage**: Wiki markdown on disk. Checker cache: `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Not git-canonical wiki content.

**Testing**: pytest temp-vault pattern in `tests/test_wiki_ops.py`. New `tests/test_wiki_cli.py`. Live-wiki size check for SC-002. Cold-context smol subject for SC-008.

**Target Platform**: macOS/darwin local repo; CI-compatible except qmd query (needs local LLM; `env -u CI`).

**Project Type**: CLI within existing wiki-ops repo.

**Performance Goals**: Unknown path fails in <1s (SC-007). Default bulk lint of ~100-page prefix <8 KB stdout (SC-002). Second identical lint does not re-run Vale on cached pages (SC-003).

**Constraints**: No fuzzy path matching. No TTY detection. No owner guessing. No creative-hydra migration. Machine errors on stdout (named VI split; see Complexity Tracking). Agent instruction examples must not keep `./scripts/wiki-lint --json wiki/` as the default structural pass.

**Scale/Scope**: One dispatcher script, thin worklist/cache/pretty helpers under `tools/wiki_ops/`, health alias, skill/AGENTS command-string updates. Does not replace `tools/lint_wiki.py`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Domain Language | PASS | Wiki / Search index. Product terms worklist, finding record, health snapshot from the spec. |
| II. Issues Are the Work Surface | PASS | Feature `027-wiki-agent-cli`. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) has FR/SC; grill locked the tree. |
| IV. Behavioral Tests | PASS | pytest on the CLI seam + quickstart V-008 cold subject. |
| V. Single Source of Truth | PASS | Contract owns the result shape; skills point at `scripts/wiki`; lint_wiki remains checker owner. |
| VI. Agent-Shaped | PASS with named split | Args in, compact JSON out, exit 0/1/2. Machine errors on stdout (wiki-ops `emit_error`); `--pretty` errors on stderr. Spec Assumptions. |
| VII. Creative Judgment | PASS | No voice/method rules. |
| VIII. Safe Automation | PASS | Cache and health are deterministic; unknown paths fail closed. |
| IX. Measured Efficiency | PASS | Worklist + cache; drop nested finding dumps and health essays. |
| X. DM Owns Canon | PASS | No wiki fact invention. |
| XII. Evidence Precedes Invention | PASS | Query does not invent hits; lint does not invent owners. |
| XIV. Simplest Adequate Tool | PASS | Compose existing checkers; one new `scripts/wiki`. |
| XV. Autonomous Operation | PASS | Unattended lint/health. |
| XVI. Layering | PASS | Contract owns CLI behavior; AGENTS.md/skills only retarget invocations. |
| XVII. Wiki Additive | PASS | Cache is derived; live pages unchanged by this CLI. |
| XX. Lean | PASS | Do not copy the JSON schema into every skill. |
| XXI. Linter Root-Cause | PASS | Checkers unchanged; default output is the defect. |
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

tools/wiki_ops/
├── cli.py                   # Existing emit_json / resolve_vault
├── worklist.py              # New: worklist + unique targets from a lint report
├── lint_cache.py            # New: per-file checker cache
└── pretty.py                # New: --pretty text for lint/query/health

tests/test_wiki_cli.py       # New behavioral tests

.agents/skills/wiki-lint/SKILL.md
.agents/skills/wiki-lint/evals/evals.json
AGENTS.md                    # Standing lint/query command examples only
```

**Structure Decision**: New public command is `scripts/wiki`. Helpers stay in `tools/wiki_ops/` next to `cli.py`. Do not add `src/`. Do not fold creative lint into the dispatcher this sitting.

## Post-Design Constitution Check

Same table as above. Design artifacts: [research.md](research.md), [data-model.md](data-model.md), [contracts/wiki-cli.md](contracts/wiki-cli.md), [quickstart.md](quickstart.md). No new `NEEDS CLARIFICATION`. Cache path and qmd `-n`/`-c`/`--format json` are resolved. Gate still PASS.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| VI: machine errors on stdout | Agents load one stream (`emit_error` already) | stderr-only errors force a second parse; spec Assumptions name the split |
