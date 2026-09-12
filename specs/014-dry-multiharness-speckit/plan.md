# Implementation Plan: DRY Multi-Harness Spec Kit

**Branch**: current working tree (014 artifacts; do not switch branches) | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/014-dry-multiharness-speckit/spec.md`

## Summary

Repair this brownfield repo so human-maintained semantics have one owner. Root `AGENTS.md` is the operating map. Constitution, `specs/`, docs, source, and tests stay the owners they already are. Install native Spec Kit adapters for Codex, Grok, OMP, and Claude using Spec Kit's shipped Python implementation. Claude gets a thin import shim. OMP and Grok stop treating Claude copies as policy. Grok Bot gets an in-repo dispatcher procedure, not a fifth Spec Kit. A check script plus CI fail on integration errors and ownership drift. Do not force-reinit. Do not write custom Spec Kit scripts.

## Technical Context

**Language/Version**: Markdown/YAML agent config + Spec Kit 1.0.6 CLI + bash check script calling `python3` for JSON (same pattern as `scripts/check-omp-baseline.sh`).

**Primary Dependencies**: Spec Kit CLI (`specify`); existing OMP integration; `agent-context` and `git` extensions (already installed). Target installs: `codex`, `grok`, `claude`. Optional runtime CLIs for inspection: `grok`, `omp`, Codex, Claude Code.

**Storage**: Files under `AGENTS.md`, `.specify/`, `.agents/`, `.grok/`, `.omp/`, `.claude/`, `docs/agents/`, `scripts/`, `.github/workflows/`. No database.

**Testing**: [quickstart.md](./quickstart.md) + `scripts/check-speckit-dry.sh` (exit 0/1) + `specify integration status --json`. No bulk suite.

**Target Platform**: Local macOS / GitHub Actions. Direct coding-harness sessions.

**Project Type**: Repository operating baseline (instruction ownership, generated adapters, one check, one workflow).

**Performance Goals**: SC-001 20-fact audit at 100% single owner. SC-003 four native adapters. Status JSON `ok`.

**Constraints**: FR-007 no wipe/force-init first. FR-012/018 generated adapters disposable. FR-029 Spec Kit `--script py` only. FR-027 do not byte-compare adapters. Constitution VII: do not prescribe creative method in AGENTS.md. Constitution IX: no duplicated guidance.

**Scale/Scope**: One repository. Four coding harnesses + one orchestrator procedure. No campaign content rewrite. Copilot instruction twin out of scope.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — no campaign glossary terms added. Harness-ops names stay in this spec/docs. |
| II. Issues are the work surface | Pass — GitHub issues remain tracked work. Spec Kit `tasks.md` is SDLC state only. |
| III. Spec before code | Pass — spec has independently testable P1–P3 stories. |
| IV. Tests specify behavior | Pass — check script and CI observe status JSON, file ownership, shim contents. No adapter internals. |
| V. Single context | Pass — no second bounded context. |
| VI. Software is agent-shaped | Pass — `specify` and `scripts/check-speckit-dry.sh` are args-in / text-or-JSON-out / exit 0 vs 1. |
| VII. Do not suffocate agents | Pass — AGENTS.md stays a map; adapters stay generated; no phase-to-product lock. |
| VIII. Safe automation unattended | Pass — drift check is idempotent CI, not a hidden hook agents must remember. |
| IX. Token efficiency | Pass — delete root `CLAUDE.md` twin; stop copying constitution; one live-context injection site. |

**Post-design re-check**: still pass. Contracts are ownership layout, status JSON, check script, dispatcher procedure. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/014-dry-multiharness-speckit/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── ownership-layout.md
│   ├── specify-status.md
│   ├── check-speckit-dry.md
│   └── harness-dispatch.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md                                            # canonical operating map + SPECKIT markers
.specify/init-options.json                           # script: py; default_integration: omp
.specify/integration.json                            # installed: codex, grok, omp, claude
.specify/extensions/agent-context/agent-context-config.yml  # context_file: AGENTS.md
.specify/scripts/                                    # Spec Kit shipped (python after --script py)
.agents/skills/speckit-*/                            # generated Codex adapters
.grok/skills/speckit-*/                              # generated Grok adapters
.omp/commands/speckit.*                              # generated OMP adapters (already present)
.omp/AGENTS.md                                       # @../AGENTS.md only
.omp/RULES.md                                        # keep; OMP sticky deltas
.omp/config.yml                                      # keep caps; add Claude context disable
.claude/CLAUDE.md                                    # @../AGENTS.md shim
.claude/skills/speckit-*/                            # generated Claude adapters
docs/agents/harness-dispatch.md                      # Grok Bot procedure
scripts/check-speckit-dry.sh                         # new
scripts/check-omp-baseline.sh                        # relax default=omp assertion
.github/workflows/speckit-dry.yml                    # new
```

**Structure Decision**: No `src/`. Generated adapters live where Spec Kit puts them. Human semantics live in `AGENTS.md`, constitution, `specs/`, `docs/agents/harness-dispatch.md`, and genuine harness config. Delete root `CLAUDE.md` after the shim exists.

## Complexity Tracking

> None. No constitution violations.
