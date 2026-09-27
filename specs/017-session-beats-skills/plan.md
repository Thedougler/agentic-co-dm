# Implementation Plan: Session Beat Skills

**Branch**: `017-session-beats-skills` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/017-session-beats-skills/spec.md`

## Summary

Split the `session-beats` blob. Keep `session-beats` as the composition skill (plan a session / Beat Chart). Add five model-invoked type skills — `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` — primary when writing, editing, or filling a beat of that type. RTG cards move with their type. Skills load each other only at named seams. One `AGENTS.md` routing table. Callers retarget.

New live beats copy that type's draft template. New session plans copy the session-plan draft. Both stay `type: session-prep` with `kind` `hook` | `development` | `cliffhanger` | `climax` | `resolution` | `session-plan`. Shape those six scaffolds into the current wiki-template family (columns, tables, omit unused). Session 11 is scan-quality evidence, not the heading spine. `run-guide` MUST NOT rewrite a typed beat into a Session 11 cockpit.

Also add campaign wiki kinds `vehicle`, `spell`, `faction`, `lore`, `quest`, `city`, and `region`: install the templates provided for this feature, list them in `wiki/AGENTS.md` Layout, fill vehicle sheets, add `spell-design` / `faction-design` / `lore-design` / `city-design` / `region-design`, keep `narrative-islands` as quest owner, make `place-design` the place hub that defers. Skills state what to write and when the page is done.


## Technical Context

**Language/Version**: Markdown skills, wiki templates, standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `session-beats`; `run-guide`; `vehicle-design`; `place-design`; `narrative-islands`; `world-tick`; `session-wrapup`; `reconciling-session-evidence`; `writing-for-agents`; `docs/agents/work.md`; `wiki/AGENTS.md`; theatre of the mind; encounter-prep; traps-trials. Method source: *Scripting the Game* as already adapted in `session-beats`. Wiki scaffolds: vehicle/spell/faction/lore/quest/city/region templates already in `wiki/templates/`; Hook, Development, Cliffhanger, Climax, Resolution, and session-plan drafts supplied for this feature (install as `wiki/templates/{hook,development,cliffhanger,climax,resolution,session-plan}.md`).

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify contract jobs. Observe primary skill and named-seam loads. Inspect one new page per wiki kind against its template jobs. Inspect one new session plan and one new live beat against kind jobs and `type: session-prep`. Chart evals stay on composition; type-card evals move with their type. No bulk suite. No rewrite of Session 11 files.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus `.agents/skills/`).

**Project Type**: Agent skill pack + standing instructions + wiki templates.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 15 primary-skill beat jobs. SC-007 — 0 skills contain both the full Beat Chart and all five type-card catalogs. SC-017–SC-032 — wiki kind pages pass their jobs; wrong primary skill is a fail. SC-006 / SC-033 / SC-034 — new live beats and session plans use typed/session-plan draft jobs, `type: session-prep` plus matching `kind`, not Session 11 heading order.

**Constraints**: FR-004 five beat types, not one skill per card. FR-013/054/055 typed drafts are the live pages; session-plan draft is the chart; `type: session-prep` + `kind`; no `type: beat` / `session-beat` / `session-plan`. FR-014 Work accept-gate. FR-015 theatre of the mind and crafts keep owners; live-beat assembly MUST NOT rewrite a typed beat into a Session 11 cockpit. FR-016 no Session 11 rewrite. FR-019–024 and FR-027–053 wiki kinds, owners, and positive skill text. Constitution I domain language. Constitution VII jobs and done-when. Constitution IX one SoT; no seventh beat router. Constitution X git/context autonomy.

**Scale/Scope**: One composition skill (existing; output retargeted to session-plan draft). Five type skills (existing; fill pointers retargeted to typed templates). New `spell-design`, `faction-design`, `lore-design`, `city-design`, `region-design`. `vehicle-design` updated. `narrative-islands` fills quests. `place-design` hub defers. `faction-prep` removed. Seven wiki-kind templates plus six session-prep kind templates plus existing `place.md`. `wiki/AGENTS.md` type + Layout. One `AGENTS.md` beat routing table plus wiki-kind rows. Pointer retargets. No `src/`. Leave `.agents/skills/writing-beats` (article journey) as it is.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — Hook, Development, Cliffhanger, Climax, Resolution, Beat Chart, session plan, live beat, Work, Co-DM, DM, vehicle, spell, faction, lore, quest, city, region. "Session spine" is the old name for session plan. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P3 plus US6–US11. Clarifications 2026-09-13 encoded as FR-054/055, SC-033/034. |
| IV. Tests specify behavior | Pass — quickstart observes primary skill, seam loads, runnable wiki pages, and session-prep kind pages. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — AGENTS.md + skills + templates, no GUI. |
| VII. Do not suffocate agents | Pass — skills name jobs and completion tests. No beat-router skill. Wiki kinds and session-prep kinds pass on jobs, omit unused. `place-design` hub defers. No required Session 11 heading spine. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. |
| IX. Design trends toward token efficiency | Pass — split catalogs; one routing table; shared session-prep identity (`type` + `kind`); drop useless draft extras (`intensity` and aliases that duplicate body jobs); strip draft research comments on install; |
| X. Agents act autonomously by default | Pass — no human gate for commit/push/context. |

**Post-design re-check**: still pass. Complexity table empty. New wiki kinds reuse the template+jobs+owner pattern. Quest keeps `narrative-islands`. Session-prep kinds reuse that pattern with `kind` instead of a new `type`.

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
│   ├── session-prep-pages.md
│   └── wiki-kind-pages.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md
wiki/AGENTS.md
wiki/templates/vehicle.md
wiki/templates/spell.md
wiki/templates/faction.md
wiki/templates/lore.md
wiki/templates/quest.md
wiki/templates/city.md
wiki/templates/region.md
wiki/templates/place.md
wiki/templates/hook.md
wiki/templates/development.md
wiki/templates/cliffhanger.md
wiki/templates/climax.md
wiki/templates/resolution.md
wiki/templates/session-plan.md
wiki/templates/session-prep.md
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
.agents/skills/faction-design/
.agents/skills/lore-design/
.agents/skills/city-design/
.agents/skills/region-design/
.agents/skills/place-design/SKILL.md
.agents/skills/narrative-islands/SKILL.md
.agents/skills/world-tick/SKILL.md
.agents/skills/session-wrapup/SKILL.md
.agents/skills/reconciling-session-evidence/SKILL.md
.agents/skills/run-guide/SKILL.md
.agents/skills/cold-opens/SKILL.md
.agents/skills/sandbox-narrative/SKILL.md
```

Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live with their types. Delete `.agents/skills/faction-prep/` after callers load `faction-design`. Beat callers that name `session-beats` for typed-beat craft get a pointer retarget. Install wiki-kind templates from the scaffolds provided for this feature. Install the six session-prep kind templates from the drafts supplied for this feature; rewrite draft `type`/`beat` keys to `type: session-prep` + `kind`; drop useless extra keys (`intensity` and aliases that duplicate body jobs); strip design-basis comments. Stop using `wiki/templates/session-prep.md` as copy-start for new beats or session plans.

**Structure Decision**: Skills stay in `.agents/skills/`. Templates stay in `wiki/templates/`. `session-beats` stays composition and fills `wiki/templates/session-plan.md`. Five beat type skills fill `wiki/templates/{hook,development,cliffhanger,climax,resolution}.md`. New kind skills as named. `place-design` hub defers. `narrative-islands` owns quests. `AGENTS.md` holds the beat routing table. `.omp/AGENTS.md` already imports `AGENTS.md`. `wiki/AGENTS.md` lists `type`, `kind` for session-prep, and Layout jobs. Session-prep page identity and jobs: `contracts/session-prep-pages.md`. No beat-router skill. No `quest-design`. No `type: beat`, `type: session-beat`, or `type: session-plan`.

## Complexity Tracking

> None. No constitution violations.
