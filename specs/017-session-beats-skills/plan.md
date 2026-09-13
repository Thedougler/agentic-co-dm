# Implementation Plan: Session Beat Skills

**Branch**: `017-session-beats-skills` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/017-session-beats-skills/spec.md`

## Summary

Split the `session-beats` blob. Keep `session-beats` as the composition skill (plan a session / Beat Chart). Add five model-invoked type skills — `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` — primary when writing, editing, or filling a beat of that type. RTG cards move with their type. Skills load each other only at named seams. One `AGENTS.md` routing table. Callers retarget.

Also add campaign wiki kinds `vehicle`, `spell`, `faction`, `lore`, `quest`, `city`, and `region`: install the templates provided for this feature, list them in `wiki/AGENTS.md` Layout, fill vehicle sheets, add `spell-design` / `faction-design` / `lore-design` / `city-design` / `region-design`, keep `narrative-islands` as quest owner, make `place-design` the place hub that defers. Skills state what to write and when the page is done.

Claude Code only for novel skills, skill redesigns, or major skill-file changes (`claude-opus-4-6 --effort medium`, minimal prompt). Session agent lands `AGENTS.md`, wiki templates, Layout jobs, Spec Kit pattern tweaks, and small edits to established files. A usage limit defers only the Claude-dependent task on `tasks.md` with a retry time; independent work continues. If every remaining open task is blocked, no other work can be done, and that retry time is more than one hour away, the session agent MAY send the same scoped prompt to the Codex CLI at ChatGPT 5.5 medium. Re-check those gates before each remaining blocked skill job; prefer Claude Code if it is usable again. One designated-writer instance at a time.

## Technical Context

**Language/Version**: Markdown skills, wiki templates, standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `session-beats`; `run-guide`; `vehicle-design`; `place-design`; `narrative-islands`; `world-tick`; `session-wrapup`; `reconciling-session-evidence`; `writing-for-agents`; `docs/agents/work.md`; `docs/agents/skill-design-dispatch.md`; `wiki/AGENTS.md`; theatre of the mind; encounter-prep; traps-trials. Method source: *Scripting the Game* as already adapted in `session-beats`. Wiki scaffolds: the templates provided for this feature.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify contract jobs. Observe primary skill and named-seam loads. Inspect one new page per wiki kind against its template jobs. Chart evals stay on composition; type-card evals move with their type. No bulk suite. No rewrite of Session 11 files.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus `.agents/skills/`).

**Project Type**: Agent skill pack + standing instructions + wiki templates.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 15 primary-skill beat jobs. SC-007 — 0 skills contain both the full Beat Chart and all five type-card catalogs. SC-015 — Claude Code, when used, is Opus 4.6 medium with a minimal prompt. SC-016 — usage-limit stop still completes independent tasks; Codex fallback only when FR-026 gates hold; re-check before each remaining blocked job. SC-017–SC-032 — wiki kind pages pass their jobs; wrong primary skill is a fail.

**Constraints**: FR-004 five beat types, not one skill per card. FR-013/014 cockpit, Work, assembly keep owners. FR-016 no Session 11 rewrite. FR-019–024 and FR-027–053 wiki kinds, owners, and positive skill text. FR-025 Claude Code only when necessary. FR-026 usage-limit deferral plus Codex fallback. Constitution I domain language. Constitution VII jobs and done-when. Constitution IX one SoT; no seventh beat router. Constitution X git/context autonomy. Constitution XI one designated writer at a time; exclusive writer `claude-opus-4-6 --effort medium` when Claude is used (1.8.0).

**Scale/Scope**: One composition skill (existing, slimmed). Five new beat type skills. New `spell-design`, `faction-design`, `lore-design`, `city-design`, `region-design`. `vehicle-design` updated. `narrative-islands` fills quests. `place-design` hub defers. `faction-prep` removed. Seven wiki templates plus existing `place.md`. `wiki/AGENTS.md` type + Layout. One `AGENTS.md` beat routing table plus wiki-kind rows. Pointer retargets. No `src/`. Leave `.agents/skills/writing-beats` (article journey) as it is.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — Hook, Development, Cliffhanger, Climax, Resolution, Beat Chart, session spine, live beat, Work, Co-DM, DM, vehicle, spell, faction, lore, quest, city, region. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P3 plus US6–US11. |
| IV. Tests specify behavior | Pass — quickstart observes primary skill, seam loads, and runnable wiki pages. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — AGENTS.md + skills + templates, no GUI. |
| VII. Do not suffocate agents | Pass — skills name jobs and completion tests. No beat-router skill. Wiki kinds pass on jobs, omit unused. `place-design` hub defers instead of absorbing cities/regions. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. |
| IX. Design trends toward token efficiency | Pass — split catalogs; one routing table; minimal Claude Code prompts. |
| X. Agents act autonomously by default | Pass — no human gate for commit/push/context. Claude Code only when necessary. Usage limit defers that job on `tasks.md`; independent work continues; deferred tasks carry over. |
| XI. Designated writer work is serialized | Pass — one Claude Code or Codex instance at a time. Codex only when every remaining open task is blocked, no other work can be done, and retry time is more than one hour away. Re-check before each remaining blocked job. |

**Post-design re-check**: still pass. Complexity table empty. Codex is a gated fallback, not a second standing writer. New wiki kinds reuse the vehicle/spell template+jobs+owner pattern. Quest keeps `narrative-islands`.

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
wiki/templates/faction.md
wiki/templates/lore.md
wiki/templates/quest.md
wiki/templates/city.md
wiki/templates/region.md
wiki/templates/place.md
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
docs/agents/skill-design-dispatch.md
```

Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live with their types. Delete `.agents/skills/faction-prep/` after callers load `faction-design`. Beat callers that name `session-beats` for typed-beat craft get a pointer retarget. Install wiki templates from the scaffolds provided for this feature.

**Structure Decision**: Skills stay in `.agents/skills/`. Templates stay in `wiki/templates/`. `session-beats` stays composition. Five beat type skills. New kind skills as named. `place-design` hub defers. `narrative-islands` owns quests. `AGENTS.md` holds the beat routing table. `.omp/AGENTS.md` already imports `AGENTS.md`. `wiki/AGENTS.md` lists `type` and Layout jobs. No beat-router skill. No `quest-design`.

## Complexity Tracking

> None. No constitution violations.
