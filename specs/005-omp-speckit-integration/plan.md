# Implementation Plan: OMP Spec Kit Integration

**Branch**: `005-omp-speckit-integration` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/005-omp-speckit-integration/spec.md`

## Summary

Finish this repo’s native Spec Kit ↔ OMP baseline. Spec Kit keeps SDLC artifacts and generated commands. OMP keeps routing, specialists, caps, isolation, and verification. Live feature context lives in `.omp/AGENTS.md` (Spec Kit-managed block; imports root `AGENTS.md`). Sticky rules live in `.omp/RULES.md`. One thin `/feature-fast` command sequences unmodified Spec Kit commands plus bounded implementer waves. One check script observes the baseline.

## Technical Context

**Language/Version**: Markdown (OMP commands, agents, context) + YAML + bash. No new compiled language.

**Primary Dependencies**: Spec Kit 1.0.6 (`integration: omp`); OMP; `agent-context` and `git` extensions (already installed).

**Storage**: Files under `.omp/` and `.specify/`. No database.

**Testing**: [quickstart.md](./quickstart.md) + `scripts/check-omp-baseline.sh` (exit 0/1). No bulk suite.

**Target Platform**: Local macOS. Direct OMP CLI session (not RPC/ACP).

**Project Type**: Agent harness baseline (commands, context, specialists, one check script).

**Performance Goals**: SC-004 — at most four concurrent implementers; zero worker-spawned workers.

**Constraints**: FR-001 native omp only. FR-012 recursion depth 1. FR-018 do not edit generated `speckit.*`. FR-020 no RPC primary path. FR-022 additive. Constitution II: `tasks.md` is not a second issue tracker.

**Scale/Scope**: One repository. Three specialists. One orchestrator command. No new MCP file. No cross-client instruction twins.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — no new campaign glossary. Harness-ops names stay in `.omp` / this spec. CONTEXT.md **Redesign** forbids operational grain as domain language. |
| II. Issues are the work surface | Pass — GitHub issues remain tracked work. Spec Kit `tasks.md` is feature SDLC state only. `/feature-fast` does not replace `gh`. |
| III. Spec before code | Pass — spec has independently testable stories P1–P4. |
| IV. Tests specify behavior | Pass — check script and quickstart observe files, keys, structured reports, and command presence. No internals. |
| V. Single context | Pass — no second bounded context. No `CONTEXT-MAP.md`. |
| VI. Tools are agent-shaped | Pass — `scripts/check-omp-baseline.sh` and `/feature-fast` are args-in / text-or-JSON-out / exit distinguishes done vs failed. No GUI. Follow `writing-for-agents`. |

**Post-design re-check**: still pass. Contracts are command + JSON report + check script. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/005-omp-speckit-integration/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── check-omp-baseline.md
│   ├── feature-fast.md
│   └── worker-report.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.specify/init-options.json                         # already integration: omp — do not re-init
.specify/extensions/agent-context/agent-context-config.yml  # context_file: .omp/AGENTS.md
.omp/AGENTS.md                                     # @../AGENTS.md + SPECKIT markers
.omp/RULES.md                                      # sticky safety constraints
.omp/config.yml                                    # roles, caps, isolation, advisor/memory off
.omp/agents/spec-auditor.md
.omp/agents/implementer.md
.omp/agents/verifier.md
.omp/commands/feature-fast.md                      # new; do not edit speckit.*
scripts/check-omp-baseline.sh
AGENTS.md                                          # unchanged wiki routing; imported, not copied
```

**Structure Decision**: Config and specialists at repo `.omp/`. No `src/`. No `.omp/mcp.json`. Generated `.omp/commands/speckit.*` stay untouched.

## Complexity Tracking

> None. No constitution violations.
