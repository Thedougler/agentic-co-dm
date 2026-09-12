# Implementation Plan: Skill Design Dispatch

**Branch**: `016-skill-design-dispatch` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/016-skill-design-dispatch/spec.md`

## Summary

Session agents classify in-scope instruction edits as design-impact or not before writing. Design-impact goes to a designated writer (Claude Code, opus, high effort). Non-design stays with the session agent. Writer unavailable (other than usage limit) → files untouched, scoped prompt parked as a GitHub issue. Usage limit → that job incomplete with a retry time (reset time from the report, else 5 hours from the stop, then 24 hours if still limited); no parked dispatch; a new session retries after that time. One short gate in `AGENTS.md`. Procedure in `docs/agents/skill-design-dispatch.md`. No new skill. No wrapper script.

## Technical Context

**Language/Version**: Markdown standing docs and skills. Host agent executes them. No new compiled language.

**Primary Dependencies**: `AGENTS.md`; `docs/agents/skill-design-dispatch.md`; `skill-creator`; `omp-harness`; `gh`; `claude` CLI (`-p --model opus --effort high`).

**Storage**: Files plus GitHub issues for parked dispatch. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify the contract jobs. Observe dispatch vs session-agent vs parked vs usage-limited. No bulk suite. No live writer required to prove classification.

**Target Platform**: Local workstation. Every coding harness that loads `AGENTS.md` (omp, Claude Code via `.claude/CLAUDE.md` import, others that follow that file).

**Project Type**: Agent standing instructions + one disclosed procedure.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 12 classification jobs.

**Constraints**: FR-002 length is not the gate. FR-008 routing fires without loading a skill-authoring playbook. FR-013 closed in-scope set. FR-017 usage limits are not parked dispatch; they carry a retry time and are not retried before it. Constitution VII — do not prescribe how the designated writer designs. Constitution IX — standing gate stays short; procedure disclosed. Constitution X — do not ask the owner to classify, park, or commit.

**Scale/Scope**: One gate table. One procedure doc. Pointers in `skill-creator` and `omp-harness` only where those skills currently tell the session agent to write. No `src/`. No new skill. No new triage label.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — no `CONTEXT.md` yet; do not invent glossary terms. Feature terms stay in the spec (session agent, designated writer, design-impact, scoped prompt, parked dispatch). |
| II. Issues are the work surface | Pass — parked dispatch is a GitHub issue via `gh`, label `ready-for-agent`. Usage limits are a wait, not tracked work. No new triage label. PRs are not a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P5. |
| IV. Tests specify behavior | Pass — quickstart observes classification and dispatch outcome, not whether a file contains a string. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — `gh` and `claude` are already agent-shaped. No GUI wrapper. No new script that only restates those CLIs. |
| VII. Do not suffocate agents | Pass — gate names when to dispatch; procedure does not prescribe skill-design method, voice, or structure. No extra checklist beyond the four design-impact bullets the spec already named. |
| VIII. Safe automation runs unattended | Pass — classification needs judgment; not a hook. No new unattended chore. |
| IX. Design trends toward token efficiency | Pass — short always-loaded gate justified by FR-008 (sessions that skip `skill-creator` otherwise leak). Procedure disclosed. Do not duplicate the gate in `.omp/AGENTS.md` or `.claude/CLAUDE.md` (they import `AGENTS.md`). |
| X. Agents act autonomously by default | Pass — session agent classifies, dispatches, parks, and verifies without asking. Owner overrule is explicit skip only. |

**Post-design re-check**: still pass. Contract is classification of an in-scope edit plus the dispatch outcome (`session-agent` / `dispatched` / `parked` / `usage-limited` / `out-of-scope`). Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/016-skill-design-dispatch/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── skill-design-dispatch.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md
docs/agents/skill-design-dispatch.md
.agents/skills/skill-creator/SKILL.md
.agents/skills/omp-harness/SKILL.md
```

**Structure Decision**: Keep standing docs + existing skills. `AGENTS.md` holds the design-impact gate (four bullets + who writes). `docs/agents/skill-design-dispatch.md` is the disclosed procedure (scoped prompt, invoke writer, park on non-usage-limit failure, restore, usage-limit wait, verify). `.omp/AGENTS.md` and `.claude/CLAUDE.md` already import `AGENTS.md` — do not duplicate the gate. `skill-creator` and `omp-harness` stop telling the session agent to draft design-impact work; they point at the procedure. Do not add a skill, a wrapper CLI, or a linter.

## Complexity Tracking

> None. No constitution violations.
