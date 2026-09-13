# Implementation Plan: Session Beat Skills

**Branch**: `017-session-beats-skills` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/017-session-beats-skills/spec.md`

## Summary

Split the `session-beats` blob. Keep `session-beats` as the composition skill (plan a session / Beat Chart). Add five model-invoked type skills — `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` — primary when writing, editing, or filling a beat of that type. RTG cards move with their type. Skills load each other only at named seams. One `AGENTS.md` routing table. Callers retarget.

Also add campaign wiki kinds `vehicle` and `spell`: install `wiki/templates/vehicle.md` and `wiki/templates/spell.md`, list them in `wiki/AGENTS.md` Layout, update `vehicle-design` to fill the 5e sheet, create `spell-design` as primary for spell pages. Skills state what to write and when the page is done.

Claude Code only for novel skills, skill redesigns, or major skill-file changes (`claude-opus-4-6 --effort medium`, minimal prompt). Session agent lands `AGENTS.md`, wiki templates, Layout jobs, Spec Kit pattern tweaks, and small edits to established files. A usage limit defers only the Claude-dependent task; independent work continues.

## Technical Context

**Language/Version**: Markdown skills, wiki templates, standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `session-beats`; `run-guide`; `vehicle-design`; `writing-for-agents`; `docs/agents/work.md`; `docs/agents/skill-design-dispatch.md`; `wiki/AGENTS.md`; theatre of the mind; encounter-prep; traps-trials. Method source: *Scripting the Game* as already adapted in `session-beats`. Vehicle/spell scaffolds: the templates provided for this feature.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify contract jobs. Observe primary skill and named-seam loads. Inspect a new vehicle page and a new spell page against their templates. Chart evals stay on composition; type-card evals move with their type. No bulk suite. No rewrite of Session 11 files.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus `.agents/skills/`).

**Project Type**: Agent skill pack + standing instructions + wiki templates.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 15 primary-skill beat jobs. SC-007 — 0 skills contain both the full Beat Chart and all five type-card catalogs. SC-015 — Claude Code, when used, is Opus 4.6 medium with a minimal prompt. SC-016 — usage-limit stop still completes independent tasks.

**Constraints**: FR-004 five beat types, not one skill per card. FR-013/014 cockpit, Work, assembly keep owners. FR-016 no Session 11 rewrite. FR-019–024 wiki kinds and positive skill text. FR-025 Claude Code only when necessary. FR-026 usage-limit deferral. Constitution I domain language. Constitution VII jobs and done-when. Constitution IX one SoT; no seventh beat router. Constitution X git/context autonomy; exclusive writer `claude-opus-4-6 --effort medium` when Claude is used (1.5.1).

**Scale/Scope**: One composition skill (existing, slimmed). Five new beat type skills. One `spell-design` skill. `vehicle-design` updated. Two wiki templates. `wiki/AGENTS.md` type + Layout. One `AGENTS.md` beat routing table. Pointer retargets on beat callers. No `src/`. Leave `.agents/skills/writing-beats` (article journey) as it is.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — Hook, Development, Cliffhanger, Climax, Resolution, Beat Chart, session spine, live beat, Work, Co-DM, DM, vehicle, spell. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P3 plus US6. |
| IV. Tests specify behavior | Pass — quickstart observes primary skill, seam loads, and runnable wiki pages. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — AGENTS.md + skills + templates, no GUI. |
| VII. Do not suffocate agents | Pass — skills name jobs and completion tests. No beat-router skill. `spell-design` is the spell-page owner, same shape as `vehicle-design`. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. |
| IX. Design trends toward token efficiency | Pass — split catalogs; one routing table; minimal Claude Code prompts. |
| X. Agents act autonomously by default | Pass — no human gate for commit/push/context. Claude Code only when necessary. Usage limit defers that job; independent work continues. |

**Post-design re-check**: still pass. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/017-session-beats-skills/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── beat-skill-routing.md
│   └── wiki-kind-pages.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md
wiki/AGENTS.md
wiki/templates/vehicle.md
wiki/templates/spell.md
.agents/skills/session-beats/SKILL.md
.agents/skills/session-beats/references/agency.md
.agents/skills/session-beats/references/session-skeleton.md
.agents/skills/session-beats/evals/evals.json
.agents/skills/hook-beats/
.agents/skills/development-beats/
.agents/skills/cliffhanger-beats/
.agents/skills/climax-beats/
.agents/skills/resolution-beats/
.agents/skills/vehicle-design/SKILL.md
.agents/skills/spell-design/
.agents/skills/run-guide/SKILL.md
.agents/skills/cold-opens/SKILL.md
.agents/skills/narrative-islands/SKILL.md
.agents/skills/sandbox-narrative/SKILL.md
docs/agents/skill-design-dispatch.md
```

Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live with their types. Beat callers that name `session-beats` for typed-beat craft get a pointer retarget. Install vehicle/spell templates from the scaffolds provided for this feature.

**Structure Decision**: Skills stay in `.agents/skills/`. Templates stay in `wiki/templates/`. `session-beats` stays composition. Five beat type skills. `spell-design` is new. `vehicle-design` fills the vehicle template including the sheet. `AGENTS.md` holds the beat routing table. `.omp/AGENTS.md` already imports `AGENTS.md`. `wiki/AGENTS.md` lists `type` and Layout jobs. No beat-router skill.

## Complexity Tracking

> None. No constitution violations.
