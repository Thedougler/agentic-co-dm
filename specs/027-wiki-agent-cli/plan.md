# Implementation Plan: Agent-Shaped Wiki CLI

**Branch**: `027-wiki-agent-cli` | **Date**: 2026-09-19 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/027-wiki-agent-cli/spec.md`

```text
work_class: engineering
route: full-sdd
reason: new public wiki command and default result contract; FR-018 updates agent lint/query/health invocations (run health, do next) in the same change
```

## Summary

One `scripts/wiki` command (`lint`, nested `lint fix`, `query`, `health`) composes existing structural lint, Vale, template-conformance, creative checks, Layer A maintenance, sitting/efficiency/error trackers, and qmd retrieval. `wiki lint` always exposes every configured finding in aggregate and per-file form by default. `wiki lint fix` is the explicit safe-repair path: it selects only registered deterministic/idempotent fixers, applies hash-preconditioned atomic mutations, reruns lint on the same scope, and returns compact repair metadata plus the complete remaining findings.

## Technical Context

**Language/Version**: Python 3.12+ (matches `pyproject.toml` `requires-python`)

**Primary Dependencies**: Existing: stdlib, PyYAML, Vale, tiktoken, `tools/lint_wiki.py`, `tools/wiki_ops/cli.py` (`configured_vault`, `emit_json`, `emit_error`), `tools/wiki_ops/mutations.py` (`MutationOp`, atomic apply), `tools/wiki_ops/transactions.py`, `tools/wiki_ops/repair_plans.py` (extended explicit fixer registry), `scripts/wiki-lint`, `scripts/wiki-maintain`, `scripts/token-count.py`, `scripts/context-waste-scan.py`, `scripts/error-ledger.py`, `scripts/efficiency-trace.py`, qmd CLI. No new packages.

**Storage**: Wiki markdown on disk. Checker cache: `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Fixes use existing atomic mutation semantics; no separate fix ledger. Health reads `sittings.jsonl`, `errors.md`, `.local/efficiency/traces.jsonl`. Every `wiki` subcommand appends one command record to that same traces file.

**Testing**: pytest temp-vault pattern in `tests/test_wiki_cli.py` and existing mutation/transaction tests. Add behavioral coverage for one file, multiple files/prefixes, whole vault, registry eligibility, unsupported findings, precondition rejection without writes, post-fix rerun, idempotence, structured result fields, and fix-first agent instructions. Cold-context smol subjects cover SC-008, SC-009, and SC-017.

**Target Platform**: macOS/darwin local repo; CI-compatible except qmd query (needs local LLM; `env -u CI`).

**Project Type**: CLI within existing wiki-ops repo.

**Performance Goals**: Unknown path fails in <1s (SC-007). Second identical lint does not re-run Vale on cached pages (SC-003). Fix runs one preflight and one post-fix lint over the resolved scope; default output includes the complete finding dump.

**Constraints**: No fuzzy path matching, TTY detection, owner guessing, checker-suppression flags, generic text rewriting, unsafe cross-scope mutation, second benchmark file, skill-eval inventory, or npm wrappers. Machine errors on stdout (named VI split). Agent instructions must teach fix before manual one-file lint.

**Scale/Scope**: One dispatcher, existing cache/worklist/health/timing/pretty helpers, one explicit fixer registry at the repair-plan boundary, and synchronized agent guidance. Registry entries must declare exact action/finding shape, validate preconditions, produce scope-safe `MutationOp` operations, and be no-ops when already satisfied. The initial registry is limited to `delete_redirect_stub`; unsupported deterministic-looking actions remain skipped until their full mutation contracts exist. Findings without eligible registered fixers remain manual.


## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Domain Language | PASS | Wiki / Search index. Product terms worklist, finding record, file group, health snapshot, command timing record. |
| II. Issues Are the Work Surface | PASS | Feature `027-wiki-agent-cli`. |
| III. Spec Before System Change | PASS | [spec.md](spec.md) has FR/SC; grill + clarify 2026-09-19 locked dump, timings, token-heaviest, skill-evals out. |
| IV. Behavioral Tests | PASS | pytest CLI/mutation seams plus quickstart V-008/V-009/V-011 and cold-agent SC-017 instruction validation. |
| V. Single Source of Truth | PASS | Contract owns the result shape; skills point at `scripts/wiki`; lint_wiki remains checker owner; one traces file. |
| VI. Agent-Shaped | PASS with named split | Args in, compact JSON out, exit 0/1/2. Fix results expose applied/skipped/remaining machine fields. Machine errors on stdout use existing `emit_error`; `--pretty` errors on stderr. |
| VII. Creative Judgment | PASS | No voice/method rules; unsupported or content-bearing findings stay manual. |
| VIII. Safe Automation | PASS | Fixer registry is explicit; preconditions, atomic mutation, and idempotent no-op behavior gate automatic repair. |
| IX. Measured Efficiency | PASS | Cache skips Vale on unchanged pages; fix reports post-fix results without raw trace dumps. |
| X. DM Owns Canon | PASS | No wiki fact invention; `focus` layout items only from existing remorph/layout plans. |
| XII. Evidence Precedes Invention | PASS | Query does not invent hits; lint does not invent owners. |
| XIV. Simplest Adequate Tool | PASS | Compose existing checkers, mutation/transaction seams, repair-plan registry, and existing traces file; no new dependency. |
| XV. Autonomous Operation | PASS | Unattended lint/fix/health; agents act on `next`, apply safe fixes, and continue to manual detail without a DM wait. |
| XVI. Layering | PASS | Contract owns CLI behavior; AGENTS.md/skills only retarget invocations. |
| XVII. Wiki Additive | PASS | Cache is derived; live pages unchanged by this CLI. |
| XX. Lean | PASS | Do not copy the JSON schema into every skill. |
| XXI. Linter Root-Cause | PASS | Checkers unchanged; default output is the defect list. |
| XXIII. Real Surfaces | PASS | Quickstart on configured vault; temp vaults for fail-closed. |
| XXIV. Synchronized Content | PASS | Skills + standing command examples update with the CLI. |
| XXV. Carve-Outs | PASS | The agent-facing lint command has no hard-only or checker-specific omission path; all configured findings are displayed by default. |

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
scripts/wiki                 # Existing dispatcher: add nested lint fix mode
scripts/wiki-lint            # Existing checker backend and creative evaluator host; not an agent-facing lint path
scripts/wiki-maintain        # --report aliases wiki health
scripts/efficiency-trace.py  # Accept record_kind=command and lint fix command
 
tools/wiki_ops/
├── cli.py                   # Existing emit_json / resolve_vault
├── worklist.py              # Existing lint summary/detail shaping
├── lint_cache.py            # Existing versioned per-file checker cache
├── health.py                # Existing Layer A + trends + focus/next composition
├── timing.py                # Existing duration + command record
├── pretty.py                # Existing --pretty renderers
└── repair_plans.py          # Add explicit safe-fixer registry and mutation planning

tests/test_wiki_cli.py       # Extend behavioral CLI tests
tests/test_wiki_ops.py       # Extend fixer/registry seam tests

.agents/skills/wiki-lint/SKILL.md
.agents/skills/wiki-lint/evals/evals.json
.agents/skills/wiki-status/SKILL.md
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/session-recap/SKILL.md
AGENTS.md                    # Standing lint/query/health command examples
alternate harness wiki-lint skill copies (.kiro/.pi/.windsurf/.cursor)

**Structure Decision**: Keep the public command in `scripts/wiki`. Extend the existing repair-plan boundary with an explicit fixer registry rather than adding a new abstraction before a second consumer exists. Generate `MutationOp` batches only from exact registered actions; validate scope and preconditions, commit through existing atomic mutation/transaction seams, then rerun the selected scope. Command timings stay in `.local/efficiency/traces.jsonl`. The dispatcher invokes every configured checker; no alternate agent lint command or omission flag is part of the surface.

## Post-Design Constitution Check

Same table as above. Design artifacts resolve the remaining choices: exact nested invocation, compact fix result, explicit registry boundary, conservative scope-safe mutation policy, post-fix rerun, exit semantics, and synchronized agent guidance. Gate still PASS; no `NEEDS CLARIFICATION` remains.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| VI: machine errors on stdout | Agents load one stream (`emit_error` already) | stderr-only errors force a second parse; spec Assumptions name the split |
