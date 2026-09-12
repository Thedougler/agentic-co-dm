# Implementation Plan: Session Beat Skills

**Branch**: `017-session-beats-skills` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/017-session-beats-skills/spec.md`

## Summary

Split the `session-beats` blob. Keep `session-beats` as the composition skill (plan a session / Beat Chart). Add five model-invoked type skills — `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` — primary when writing, editing, or filling a beat of that type. RTG cards move with their type. Skills load each other only at named seams. One `AGENTS.md` routing table. Callers retarget. No second pacing system. No Session 11 rewrite. Creating the type skills and changing composition ownership is design-impact: designated writer lands it.

## Technical Context

**Language/Version**: Markdown skills and standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `session-beats`; `run-guide`; `writing-for-agents`; `docs/agents/work.md`; `docs/agents/skill-design-dispatch.md`; `wiki/AGENTS.md`; theatre of the mind; encounter-prep; traps-trials. Method source: *Scripting the Game* as already adapted in `session-beats` (agency gates, not a railroad).

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify the contract jobs. Observe primary skill and named-seam loads. Existing `session-beats` evals that test the chart stay on composition; type-card evals move with their type. No bulk suite. No rewrite of Session 11 files.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus `.agents/skills/`).

**Project Type**: Agent skill pack + standing instructions.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 15 primary-skill jobs. SC-007 — 0 skills contain both the full Beat Chart and all five type-card catalogs.

**Constraints**: FR-004 five types, not one skill per card. FR-013/014/015 cockpit, Work, assembly, and crafts keep owners. FR-016 no Session 11 rewrite. Constitution I domain language. Constitution VII no creative-method prescription. Constitution IX one source of truth; six descriptions, not a seventh router. Constitution X git/context autonomy; design-impact still dispatches.

**Scale/Scope**: One composition skill (existing, slimmed). Five new type skills. One `AGENTS.md` table. Pointer retargets on skills that currently name `session-beats` for typed-beat craft. No `src/`. Do not port `.claude/skills/composing-beats` or `writing-*-beats`. Do not touch `.agents/skills/writing-beats` (article journey, unrelated).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — Hook, Development, Cliffhanger, Climax, Resolution, Beat Chart, session spine, live beat, Work, Co-DM, DM. No GM. No knowledge bank. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P3. |
| IV. Tests specify behavior | Pass — quickstart observes primary skill and seam loads, not skill internals. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — AGENTS.md + skills, no GUI, no human-only wrapper. |
| VII. Do not suffocate agents | Pass — skills name jobs and completion tests; they do not prescribe a single plot or voice. No seventh skill. No extra checklist. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. No formatter/index step added to skills. |
| IX. Design trends toward token efficiency | Pass — split so a typed-beat job does not load five card catalogs; composition does not carry cards; one routing table; pointers not copies. |
| X. Agents act autonomously by default | Pass — no human gate for commit/push/context. Design-impact still dispatches (016). |

**Post-design re-check**: still pass. Contract is which skill is primary for a job. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/017-session-beats-skills/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── beat-skill-routing.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md
wiki/AGENTS.md
.agents/skills/session-beats/SKILL.md
.agents/skills/session-beats/references/agency.md
.agents/skills/session-beats/references/session-skeleton.md
.agents/skills/session-beats/evals/evals.json
.agents/skills/hook-beats/
.agents/skills/development-beats/
.agents/skills/cliffhanger-beats/
.agents/skills/climax-beats/
.agents/skills/resolution-beats/
.agents/skills/run-guide/SKILL.md
.agents/skills/cold-opens/SKILL.md
.agents/skills/narrative-islands/SKILL.md
.agents/skills/sandbox-narrative/SKILL.md
```

Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live with their types. Other skills that name `session-beats` for typed-beat craft get a pointer retarget only.

**Structure Decision**: Keep skills in `.agents/skills/`. `session-beats` stays the composition skill. Five new sibling type skills. `AGENTS.md` holds the routing table. `.omp/AGENTS.md` already imports `AGENTS.md` — do not duplicate the table there. Do not add a router skill. Do not copy Campaign OS `.claude/skills/composing-beats` or `writing-*-beats`. Do not edit `legacy/` or rewrite Session 11 wiki/`_raw/` pages.

## Complexity Tracking

> None. No constitution violations.
