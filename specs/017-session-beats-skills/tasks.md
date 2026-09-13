---
description: "Task list for Session Beat Skills"
---
# Tasks: Session Beat Skills

**Input**: Design documents from `/specs/017-session-beats-skills/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/017-session-beats-skills/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US6 → US5 → US7 → US8 → US9 → US10 → US11 → Polish.

**Dispatch**: Designated writer (sequential, one instance, `claude -p --model claude-opus-4-6 --effort medium`): T003, T005–T009, T017, T018, T031, T036, T040, T043, T046. Session agent: all other tasks. Usage limit: defer that writer task here with a retry time; finish independent work; carry deferred tasks forward. Codex CLI at ChatGPT 5.5 medium only when every remaining open task is blocked, no other work can be done, and retry time is more than one hour away. Re-check those gates before each remaining blocked skill job; prefer Claude Code if it is usable again.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US11 only on story phases
- Every task names an exact path

## Path Conventions

Standing: `AGENTS.md`
Wiki kinds: `wiki/AGENTS.md`, `wiki/templates/vehicle.md`, `wiki/templates/spell.md`, `wiki/templates/faction.md`, `wiki/templates/lore.md`, `wiki/templates/quest.md`, `wiki/templates/city.md`, `wiki/templates/region.md`, `wiki/templates/place.md`
Composition: `.agents/skills/session-beats/SKILL.md`
Composition refs: `.agents/skills/session-beats/references/agency.md`, `.agents/skills/session-beats/references/session-skeleton.md`
Cards source: `.agents/skills/session-beats/references/beat-types.md`
Type skills: `.agents/skills/hook-beats/`, `.agents/skills/development-beats/`, `.agents/skills/cliffhanger-beats/`, `.agents/skills/climax-beats/`, `.agents/skills/resolution-beats/`
Wiki crafts: `.agents/skills/vehicle-design/SKILL.md`, `.agents/skills/spell-design/`, `.agents/skills/faction-design/`, `.agents/skills/lore-design/`, `.agents/skills/city-design/`, `.agents/skills/region-design/`
Callers: `.agents/skills/run-guide/SKILL.md`, `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, `.agents/skills/sandbox-narrative/SKILL.md`, `.agents/skills/place-design/SKILL.md`, `.agents/skills/world-tick/SKILL.md`, `.agents/skills/session-wrapup/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`
Remove: `.agents/skills/faction-prep/`
Contracts: `specs/017-session-beats-skills/contracts/beat-skill-routing.md`, `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No `src/`, no beat-router skill, no Campaign OS port.

- [X] T001 Confirm the files listed under Source Code in `specs/017-session-beats-skills/plan.md` exist or will be created as listed; do not add a beat-router skill, `src/`, linter, or port of `.claude/skills/composing-beats` or `writing-*-beats`; do not edit `.agents/skills/writing-beats/SKILL.md`; do not rewrite `wiki/_raw/Session-11-*.md`; do not add a `quest-design` skill

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One always-loaded beat routing table. Skills will match it.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Add the beat-skill routing table to `AGENTS.md` from `specs/017-session-beats-skills/contracts/beat-skill-routing.md`. Quote: plan a session, one-shot, adventure arc, or expedition evening → `session-beats`; write, edit, or create content for a Hook → `hook-beats`; Development → `development-beats`; Cliffhanger → `cliffhanger-beats`; Climax → `climax-beats`; Resolution → `resolution-beats`. Quote: "Unknown typed-beat job → classify the type first; do not default to `session-beats` for filling a beat." Point at `specs/017-session-beats-skills/contracts/beat-skill-routing.md` for named seams. Do not copy the table into `.omp/AGENTS.md`.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Planning a session uses the composition skill (Priority: P1) 🎯 MVP

**Goal**: `session-beats` directs Beat Chart assembly only. A planning job does not require type-card catalogs.

**Independent Test**: Quickstart steps 1 (job 1) and 2. Author produces a valid spine without opening type-card catalogs.

### Implementation for User Story 1

- [X] T003 [US1] Rewrite `.agents/skills/session-beats/SKILL.md` as composition only (Claude Code). Description fires on planning a session, one-shot, adventure arc, or expedition evening. Owns: Beat Chart assembly; one Hook; alternate D/C; Climax then Resolution; polarity; ~30 min per beat; Hook+Climax+Resolution ~90 min; threads, escalation, transitions; recompute / agency gates; filed spine jobs. Point typed fill at the five type skills. MUST NOT include the five type-card catalogs. MUST NOT stand-load `.agents/skills/session-beats/references/beat-types.md`. Quote data-model: "Primary when planning a session, one-shot, adventure arc, or expedition evening."
- [X] T004 [US1] Keep `.agents/skills/session-beats/references/agency.md` and `.agents/skills/session-beats/references/session-skeleton.md` as composition references. Skeleton stays the planning form; filed spine remains Session 11-00 shape.

**Checkpoint**: US1 independently testable (quickstart steps 1 job 1, 2)

---

## Phase 4: User Story 2 - Typed beat uses that type's skill (Priority: P1)

**Goal**: Write, edit, or fill a beat of one type with that type skill as primary. Other four card catalogs not required.

**Independent Test**: Quickstart steps 1 (jobs 2–15) and 3. A Development is a Development by the completion test without other type catalogs.

### Implementation for User Story 2

Quote each type's completion test from `specs/017-session-beats-skills/data-model.md`. Each type skill owns purpose, completion test, cards for that type, how to fill this beat. Card fields: Type exactly one of the five; Trigger "when fiction calls for it — not to fill a slot"; Stakes visible; Player options "at least two viable responses"; Agency note "ignoring, failing, or redirecting updates the world". Move cards out of `.agents/skills/session-beats/references/beat-types.md` into the matching type skill. Model-invoked descriptions: write, edit, or create content for that type.

- [X] T005 [P] [US2] Create `.agents/skills/hook-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Party has committed to a response to the opening pressure. One Hook per session." Include Play a Cliffhanger as Hook and Play a Development as Hook as Hook cards.
- [X] T006 [P] [US2] Create `.agents/skills/development-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Players can name what they now know or can decide that they could not before."
- [X] T007 [P] [US2] Create `.agents/skills/cliffhanger-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "The contest resolved; physical situation (position, resources, safety, time) changed."
- [X] T008 [P] [US2] Create `.agents/skills/climax-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Highest-stakes confrontation the middle made inevitable; threads harvested."
- [X] T009 [P] [US2] Create `.agents/skills/resolution-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Players can name what is different and what they want next."

**Checkpoint**: US1 + US2 independently testable (quickstart steps 1, 3)

---

## Phase 5: User Story 3 - Skills load each other only at named seams (Priority: P2)

**Goal**: Extra skills load only for contract seams 16–20. No standing bundle.

**Independent Test**: Quickstart step 4. Play a Cliffhanger as Hook stays one Hook.

### Implementation for User Story 3

- [X] T010 [US3] In `.agents/skills/session-beats/SKILL.md`, load a type skill only when filling a typed slot; after load, that type skill is primary for the fill. Quote seam: "Composition filling a typed slot → That type skill; type becomes primary for the fill."
- [X] T011 [P] [US3] In `.agents/skills/hook-beats/SKILL.md`, load `session-beats` only when chart position, polarity, threads, or transition is in question (not as primary for writing the beat). Play a Cliffhanger as Hook loads `.agents/skills/cliffhanger-beats/` for opening shape only; Play a Development as Hook loads `.agents/skills/development-beats/` for opening shape only; beat remains the session's one Hook.
- [X] T012 [P] [US3] In `.agents/skills/development-beats/SKILL.md`, `.agents/skills/cliffhanger-beats/SKILL.md`, `.agents/skills/climax-beats/SKILL.md`, and `.agents/skills/resolution-beats/SKILL.md`, load `session-beats` only for chart position, polarity, threads, or transition; load the next type skill only when How the Scene Resolves names that type, for the handoff only. Quote: "Any other extra type-card catalog is a defect."

**Checkpoint**: US1–US3 independently testable (quickstart step 4)

---

## Phase 6: User Story 4 - Chart still follows Scripting the Game, with player agency (Priority: P2)

**Goal**: Three Beat Chart rules, polarity, budget, threads, two-plus responses, recompute.

**Independent Test**: Quickstart step 5 against contract chart rules 1–8.

### Implementation for User Story 4

- [X] T013 [US4] In `.agents/skills/session-beats/SKILL.md` and `.agents/skills/session-beats/references/agency.md`, bind chart rules from `specs/017-session-beats-skills/contracts/beat-skill-routing.md`: one Hook to start; Developments and Cliffhangers only in alternating order; one Climax followed by one Resolution; Action Hook → next Development; cerebral Hook → next Cliffhanger; Action Climax preceded by Development; cerebral Climax preceded by Cliffhanger; about thirty minutes per beat; Hook + Climax + Resolution about ninety minutes; every prepared beat advances a live thread; at least two viable player responses; recompute rather than force the next slot. Quote data-model: "Situations not required outcomes; recompute; chart may shrink/branch/pause/end…

**Checkpoint**: US1–US4 independently testable (quickstart step 5)

---

## Phase 7: User Story 6 - Spell and vehicle wiki pages use the new templates (Priority: P2)

**Goal**: `type: vehicle` and `type: spell` pages start from wiki templates and are runnable. `vehicle-design` fills the sheet. `spell-design` is primary for spell pages.

**Independent Test**: Quickstart step 7 against `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`.

### Implementation for User Story 6

- [X] T014 [P] [US6] Create `wiki/templates/vehicle.md` from the provided vehicle scaffold. Jobs: spoken look; sheet (size, type, speed, crew, passengers, cargo); components (hull AC/HP/DT, helm, movement, weapons when armed); crew stations; handling; combat. Omit unused sections.
- [X] T015 [P] [US6] Create `wiki/templates/spell.md` from the provided spell scaffold. Jobs: spoken look of the casting; classification line; runnable 2024 effect block (casting time, range, components, duration, saves, damage, conditions; scaling when it scales); Discovery when placement needed; Lore when history needed. Omit unused sections.
- [X] T016 [US6] In `wiki/AGENTS.md`, add `type` values `vehicle` and `spell`. Layout jobs: Vehicle — Look; sheet; components; crew stations; handling; combat. Spell — Look of the casting; classification; runnable 2024 effect; Discovery when placement needed; Lore when history needed. Quote: "Pass is those jobs."
- [X] T017 [US6] Rewrite `.agents/skills/vehicle-design/SKILL.md` so it fills `wiki/templates/vehicle.md`, including size, type, speed, crew, and hull plus component AC/HP. Quote data-model: "Size, type, speed, crew (min), passengers, cargo filled so the craft can enter play." State what to write and when the page is done. Treat missing crafts as work to do now. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.
- [ ] T018 [US6] Create `.agents/skills/spell-design/SKILL.md`. Primary for write, edit, or create of a spell page. Completes when narration, classification, and a runnable 2024 effect block are filled. Discovery and Lore when the spell needs placement or history. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt. Retry after 2026-09-12 18:30 America/Vancouver.
- [X] T028 [US6] Add the wiki-kind routing table to `AGENTS.md` from `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`. Quote: write/edit/create vehicle → `vehicle-design`; spell → `spell-design`; faction → `faction-design`; lore → `lore-design`; quest → `narrative-islands`; city → `city-design`; region → `region-design`; site place → `place-design`. Quote: "`place-design` is the hub for all places. It defers to `city-design` for `kind: city` and to `region-design` for region jobs." Do not copy the table into `.omp/AGENTS.md`.

**Checkpoint**: US6 independently testable (quickstart step 7)

---

## Phase 8: User Story 5 - Cockpit, Work, and live-beat assembly keep their owners (Priority: P3)

**Goal**: Split does not steal `run-guide`, Work, theatre of the mind, or craft owners. Callers name the right skill.

**Independent Test**: Quickstart step 6. New live beat still reads as a Session 11 cockpit card. Zero Session 11 bodies rewritten.

### Implementation for User Story 5

- [X] T019 [P] [US5] In `.agents/skills/run-guide/SKILL.md`, load `session-beats` when the chart is missing; load the matching type skill when a live beat of that type is missing. Do not move cockpit job order into composition or type skills.
- [X] T020 [P] [US5] In `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, and `.agents/skills/sandbox-narrative/SKILL.md`, retarget typed-beat craft to `session-beats` for the chart and the matching type skill for a typed beat. Work gate stays `docs/agents/work.md`.
- [X] T021 [US5] Confirm `wiki/AGENTS.md` still points the filed spine at `.agents/skills/session-beats/SKILL.md` and cockpit jobs at `.agents/skills/run-guide/SKILL.md`. Type skills MAY hand off to theatre of the mind, encounter-prep, traps-trials, place, monster, vehicle, and spell crafts.

**Checkpoint**: US5 independently testable (quickstart step 6)

---

## Phase 9: User Story 7 - Faction wiki pages use the new template (Priority: P2)

**Goal**: `faction-design` is primary. Pages start from `wiki/templates/faction.md`. `faction-prep` is gone. Current Turn has no roll.

**Independent Test**: Quickstart step 8 (faction). Reviewer can answer what the faction wants, can do, will do next, and how the party can interfere.

### Implementation for User Story 7

- [X] T029 [P] [US7] Create `wiki/templates/faction.md` from the provided faction scaffold. Jobs: public face; DM thesis; current state; one active agenda; table-relevant assets, people, places, and relationships; faction-turn log. Extra headings omit-if-unused. Pass is those jobs.
- [X] T030 [US7] In `wiki/AGENTS.md`, keep `type` value `faction`. Layout jobs for Faction matching FR-028: public face; DM thesis; current state; one active agenda; table-relevant assets/people/places/relationships; faction-turn log. Quote: "Pass is those jobs."
- [ ] T031 [US7] Create `.agents/skills/faction-design/SKILL.md` (Claude Code). Primary for write, edit, or create of a faction page. Completes when FR-028 jobs are filled. Quote: "Current Turn named with no roll at create". Agenda clock lives on the faction page. `hot.md` MAY point; MUST NOT store a second clock. State what to write and when the page is done. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.
- [ ] T032 [US7] Delete `.agents/skills/faction-prep/` after T031. Retarget remaining live callers in `.agents/skills/` and `AGENTS.md` to `faction-design`. Do not keep a stub. Do not rewrite `legacy/`.
- [X] T033 [US7] In `.agents/skills/world-tick/SKILL.md`, append the faction-turn log after a resolved turn; MUST NOT write Current Turn as a rolled result at page create; MUST NOT store a second agenda clock in `hot.md`; MUST NOT advance quest portents.

**Checkpoint**: US7 independently testable (quickstart step 8 faction)

---

## Phase 10: User Story 8 - Lore wiki pages use the new template (Priority: P2)

**Goal**: `lore-design` is primary. `type: lore` is real. Ingest MUST NOT remap `lore`→`item`. Not `canon` until table witness.

**Independent Test**: Quickstart step 8 (lore). Page answers one question and has At a Glance, Current Truth, At the Table.

### Implementation for User Story 8

- [X] T034 [P] [US8] Create `wiki/templates/lore.md` from the provided lore scaffold. Jobs: one durable question; At a Glance (core truth + why it matters); Current Truth; At the Table (notice / explains / enables / warns). Extra headings omit-if-unused. Pass is those jobs.
- [X] T035 [US8] In `wiki/AGENTS.md`, add `type` value `lore`. Layout jobs for Lore matching FR-035. Remove the ingest remap `lore`→`item` from the line that currently maps `location`→`place`, `monster`→`creature`, `lore`→`item`. World-truth notes use `type: lore`. Actual items stay `item`.
- [ ] T036 [US8] Create `.agents/skills/lore-design/SKILL.md` (Claude Code). Primary for write, edit, or create of a lore page. Completes when FR-035 jobs are filled. Unrelated truths split into linked notes. MUST NOT mark lore `canon` until players interact or witness. Canon Log omitted until then. MUST NOT invent table history. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.
- [X] T037 [US8] In `.agents/skills/session-wrapup/SKILL.md` and `.agents/skills/reconciling-session-evidence/SKILL.md`, after players interact with or witness lore: update Current Truth when it changed and append a Canon Log row. Until then the DM may change it freely. MUST NOT own the Quest log (`narrative-islands` owns it).

**Checkpoint**: US8 independently testable (quickstart step 8 lore)

---

## Phase 11: User Story 9 - Quest wiki pages use the new template (Priority: P2)

**Goal**: `narrative-islands` fills `wiki/templates/quest.md`. No `quest-design`. `type: front` and `type: encounter` retired.

**Independent Test**: Quickstart step 8 (quest). Reviewer can run the situation, name walk-away, and point to two independent leads.

### Implementation for User Story 9

- [X] T038 [P] [US9] Create `wiki/templates/quest.md` from the provided quest scaffold. Jobs: summary (objective, why now, deadline); Situation; Stakes including walk-away; World in motion (driver and next move if uninterrupted); at least two independent leads. Resolution omitted while unresolved. Extra headings omit-if-unused. Pass is those jobs.
- [X] T039 [US9] In `wiki/AGENTS.md`, add `type` value `quest`. Layout jobs for Quest matching FR-041. Campaign situation pages use `type: quest`. `type: front` and `type: encounter` MUST NOT be used.
- [ ] T040 [US9] Redesign `.agents/skills/narrative-islands/SKILL.md` (Claude Code) to fill `wiki/templates/quest.md` as primary for write/edit/create of a quest page. Owns later updates including World in motion, portents, rolls, Situation, status, and the Quest log. MUST NOT mint `type: front` or `type: encounter`. MUST NOT add a `quest-design` skill. Keep T020 typed-beat retarget: chart → `session-beats`, typed beat → matching type skill. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.

**Checkpoint**: US9 independently testable (quickstart step 8 quest)

---

## Phase 12: User Story 10 - City wiki pages use the new template (Priority: P2)

**Goal**: `city-design` is primary. Page is `type: place` `kind: city`. `place-design` defers.

**Independent Test**: Quickstart step 9 (city). Reviewer can arrive, find a district, seek a place, name a local rule, and say if-nobody-intervenes.

### Implementation for User Story 10

- [X] T041 [P] [US10] Create `wiki/templates/city.md` from the provided city scaffold. Jobs: Arrival; At a glance including current pressure; Orientation (districts and getting around); Gazetteer enough to intentionally seek a place; rules that matter at the table; at least one active situation with if-nobody-intervenes. Extra headings omit-if-unused. Frontmatter: `type: place`, `kind: city`. Pass is those jobs.
- [X] T042 [US10] In `wiki/AGENTS.md`, Layout jobs for City matching FR-047. Site places keep using `wiki/templates/place.md` and existing Place jobs. Quote: page is `type: place` with `kind: city`.
- [ ] T043 [US10] Create `.agents/skills/city-design/SKILL.md` (Claude Code). Primary for write, edit, or create of a city page. Completes when FR-047 jobs are filled. Faction full agendas stay on faction pages. A pursuable situation links a quest. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.

**Checkpoint**: US10 independently testable (quickstart step 9 city)

---

## Phase 13: User Story 11 - Region wiki pages use the new template (Priority: P2)

**Goal**: `region-design` is primary. `place-design` defers. MUST NOT invent pressure.

**Independent Test**: Quickstart step 9 (region). Reviewer can travel and name who can change the region. A region with no already-stated pressure still passes.

### Implementation for User Story 11

- [X] T044 [P] [US11] Create `wiki/templates/region.md` from the provided region scaffold. Jobs: spoken look; At a glance; Current state; geography/travel enough to choose a route; active powers; change log. Extra headings omit by scale (MACRO / REGIONAL / LOCAL). Pass is those jobs.
- [X] T045 [US11] In `wiki/AGENTS.md`, add `type` value `region`. Layout jobs for Region matching FR-051.
- [ ] T046 [US11] Create `.agents/skills/region-design/SKILL.md` (Claude Code). Primary for write, edit, or create of a region page. Completes when FR-051 jobs are filled. MUST NOT invent pressure. If a pressure is already stated, link that wiki note. MUST NOT revive `type: front`. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.
- [X] T047 [US11] In `.agents/skills/place-design/SKILL.md`, remain the hub for all places; write site places from `wiki/templates/place.md`; defer `kind: city` to `city-design`; defer region jobs to `region-design`; MUST NOT write the city or region page itself.

**Checkpoint**: US10–US11 independently testable (quickstart step 9)

---

## Phase 14: Polish & Cross-Cutting Concerns

**Purpose**: Blob gone. Evals follow owners. Quickstart 1–10 holds. Dispatch flags hold.

- [X] T022 Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live in the five type skills
- [X] T023 Split `.agents/skills/session-beats/evals/evals.json`: chart/agency/alternation/polarity evals stay on composition; type-card evals move with their type skill
- [ ] T024 Run `specs/017-session-beats-skills/quickstart.md` steps 1–10 against `specs/017-session-beats-skills/contracts/beat-skill-routing.md` and `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`
- [ ] T025 Confirm this change set does not rewrite bodies of `wiki/_raw/Session-11-*.md`, does not edit `.agents/skills/writing-beats/SKILL.md`, does not copy routing tables into `.omp/AGENTS.md`, leaves 0 skills that contain both the full Beat Chart and all five type-card catalogs, does not add a `quest-design` skill, has no `.agents/skills/faction-prep/`, does not remap `lore`→`item`, and does not file new durable situations as `type: front` or `type: encounter`
- [ ] T026 Confirm designated-writer jobs T003, T005–T009, T017, T018, T031, T036, T040, T043, T046 used `claude-opus-4-6 --effort medium` with a prompt that names deliverables plus a completion test, per `docs/agents/skill-design-dispatch.md`, except Codex CLI at ChatGPT 5.5 medium when FR-026 gates held; `AGENTS.md` and templates were session-agent work
- [X] T027 Update `docs/agents/skill-design-dispatch.md` so usage-limit wait records retry time on this `tasks.md`, carries deferred tasks forward, and MAY invoke Codex CLI at ChatGPT 5.5 medium when every remaining open task is blocked, no other work can be done, and that retry time is more than one hour away; re-check those gates before each remaining blocked skill job; prefer Claude Code if it is usable again.
- [X] T048 Confirm type skills MAY hand off a named vehicle, spell, faction, lore note, quest, city, or region to that wiki-kind owner without absorbing the page job, in `.agents/skills/hook-beats/SKILL.md`, `.agents/skills/development-beats/SKILL.md`, `.agents/skills/cliffhanger-beats/SKILL.md`, `.agents/skills/climax-beats/SKILL.md`, and `.agents/skills/resolution-beats/SKILL.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; T005–T009 parallel by file (writer sequential)
- **US3 (Phase 5)**: After US1 and US2
- **US4 (Phase 6)**: After US1 (same composition files — after T010 if US3 already started)
- **US6 (Phase 7)**: After Foundational; independent of beat type skills. T014–T015 parallel; T016 after templates; T017–T018 after T016; T028 independent of T017–T018
- **US5 (Phase 8)**: After US2 (callers need type skill names)
- **US7 (Phase 9)**: After Foundational; T029 then T030/T031; T032–T033 after T031
- **US8 (Phase 10)**: After Foundational; T035 after T030 (same `wiki/AGENTS.md`); T037 after T036
- **US9 (Phase 11)**: After Foundational; T039 after T035 (same `wiki/AGENTS.md`); T040 after T020 (keep beat retarget)
- **US10 (Phase 12)**: After Foundational; T042 after T039 (same `wiki/AGENTS.md`)
- **US11 (Phase 13)**: After US10 for T047 (`place-design`); T045 after T042 (same `wiki/AGENTS.md`); T046 then T047
- **Polish (Phase 14)**: After desired stories; T022 after US2; T048 after US2 and US7–US11

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P1)**: After Phase 2; independent of US1 (different files)
- **US3 (P2)**: After US1 + US2
- **US4 (P2)**: After US1; same `session-beats` files as T003/T010 — do not parallelize with those
- **US6 (P2)**: After Phase 2; independent of US1–US5
- **US5 (P3)**: After US2
- **US7 (P2)**: After Phase 2; independent of beat stories
- **US8 (P2)**: After Phase 2; `wiki/AGENTS.md` after US7 Layout
- **US9 (P2)**: After Phase 2; `narrative-islands` after T020; `wiki/AGENTS.md` after US8
- **US10 (P2)**: After Phase 2; `wiki/AGENTS.md` after US9
- **US11 (P2)**: After US10 for hub defer; `wiki/AGENTS.md` after US10

### Parallel Opportunities

- T005, T006, T007, T008, T009 (five type-skill directories; writer still sequential)
- T011 vs T012 (hook vs the other four type skills)
- T014, T015 (two templates, done)
- T017 vs T018 after T016 (vehicle-design vs spell-design; writer sequential)
- T019, T020 (run-guide vs caller trio, done)
- T029, T034, T038, T041, T044 (five wiki templates, different files)
- T031, T036, T040, T043, T046 (new/redesign skills, different directories; writer sequential)
- Do not parallelize T002, T028 (`AGENTS.md`)
- Do not parallelize T003, T010, T013 (same `session-beats/SKILL.md`)
- Do not parallelize T004 with T013's `agency.md` edit
- Do not parallelize T016, T021, T030, T035, T039, T042, T045 (same `wiki/AGENTS.md`)
- Do not parallelize T037 with later wrapup edits
- Do not parallelize T033 with other `.agents/skills/world-tick/SKILL.md` edits
- Do not parallelize T047 with other `.agents/skills/place-design/SKILL.md` edits

---

## Parallel Example: User Story 2

```text
Task: Create .agents/skills/hook-beats/SKILL.md (T005)
Task: Create .agents/skills/development-beats/SKILL.md (T006)
Task: Create .agents/skills/cliffhanger-beats/SKILL.md (T007)
Task: Create .agents/skills/climax-beats/SKILL.md (T008)
Task: Create .agents/skills/resolution-beats/SKILL.md (T009)
```

## Parallel Example: Wiki templates (US7–US11)

```text
Task: Create wiki/templates/faction.md (T029)
Task: Create wiki/templates/lore.md (T034)
Task: Create wiki/templates/quest.md (T038)
Task: Create wiki/templates/city.md (T041)
Task: Create wiki/templates/region.md (T044)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `AGENTS.md` beat table
3. Phase 3 US1 (composition-only `session-beats`)
4. STOP — quickstart step 2
5. Demo: plan a session without type-card catalogs

### Incremental Delivery

1. Setup + Foundational
2. US1 → composition is the planner
3. US2 → five type skills
4. US3 → named seams
5. US4 → chart rules + agency
6. US6 → vehicle/spell templates and skills
7. US5 → callers and owners
8. US7 → faction template + `faction-design`; delete `faction-prep`
9. US8 → lore template + `lore-design`; drop `lore`→`item`
10. US9 → quest template + `narrative-islands` redesign
11. US10 → city template + `city-design`
12. US11 → region template + `region-design`; `place-design` hub defers
13. Polish → delete `beat-types.md`; split evals; quickstart 1–10; dispatch flags

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — skills + `AGENTS.md` + templates + pointer retargets
- Do not add test files unless a later command asks
- Do not add a beat-router skill or a `quest-design` skill
- Do not port Campaign OS composing/writing-*-beats
- Do not rewrite Session 11 to prove the split
- Designated writer: T003, T005–T009, T017, T018, T031, T036, T040, T043, T046 only. Session agent: the rest
- Writer tasks are sequential even when marked [P] for files
- Usage limit: defer that writer task on this file with a retry time; complete remaining independent tasks; carry deferred tasks forward. Codex CLI at ChatGPT 5.5 medium only when every remaining open task is blocked, no other work can be done, and retry time is more than one hour away
- Deferred writer jobs T003, T005–T009, T017, T018 keep retry after 2026-09-12 18:30 America/Vancouver
- Commit after each task or logical group
- Stop at checkpoints
