---
description: "Task list for Session Beat Skills"
---
# Tasks: Session Beat Skills

**Input**: Design documents from `/specs/017-session-beats-skills/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/017-session-beats-skills/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US6 → US5 → Polish.

**Dispatch**: Claude Code only for novel skills, skill redesigns, or major skill-file changes: T003 (`session-beats` rewrite), T005–T009 (new type skills), T017 (`vehicle-design` redesign), T018 (new `spell-design`). Minimal prompt at `claude -p --model claude-opus-4-6 --effort medium`. Session agent lands T001, T002 (`AGENTS.md`), T004, T010–T016, T019–T026. Usage limit: defer the Claude-dependent task; complete remaining independent tasks. Follow `writing-for-agents`. Skills state what to write and when the page is done.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US6 only on story phases
- Every task names an exact path

## Path Conventions

Standing: `AGENTS.md`  
Wiki kinds: `wiki/AGENTS.md`, `wiki/templates/vehicle.md`, `wiki/templates/spell.md`  
Composition: `.agents/skills/session-beats/SKILL.md`  
Composition refs: `.agents/skills/session-beats/references/agency.md`, `.agents/skills/session-beats/references/session-skeleton.md`  
Cards source: `.agents/skills/session-beats/references/beat-types.md`  
Type skills: `.agents/skills/hook-beats/`, `.agents/skills/development-beats/`, `.agents/skills/cliffhanger-beats/`, `.agents/skills/climax-beats/`, `.agents/skills/resolution-beats/`  
Wiki crafts: `.agents/skills/vehicle-design/SKILL.md`, `.agents/skills/spell-design/`  
Callers: `.agents/skills/run-guide/SKILL.md`, `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, `.agents/skills/sandbox-narrative/SKILL.md`  
Contracts: `specs/017-session-beats-skills/contracts/beat-skill-routing.md`, `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No `src/`, no beat-router skill, no Campaign OS port.

- [X] T001 Confirm the files listed under Source Code in `specs/017-session-beats-skills/plan.md` exist or will be created as listed; do not add a beat-router skill, `src/`, linter, or port of `.claude/skills/composing-beats` or `writing-*-beats`; do not edit `.agents/skills/writing-beats/SKILL.md`; do not rewrite `wiki/_raw/Session-11-*.md`

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

- [ ] T003 [US1] Rewrite `.agents/skills/session-beats/SKILL.md` as composition only (Claude Code). Description fires on planning a session, one-shot, adventure arc, or expedition evening. Owns: Beat Chart assembly; one Hook; alternate D/C; Climax then Resolution; polarity; ~30 min per beat; Hook+Climax+Resolution ~90 min; threads, escalation, transitions; recompute / agency gates; filed spine jobs. Point typed fill at the five type skills. Quote data-model: "Primary when planning a session, one-shot, adventure arc, or expedition evening."
- [X] T004 [US1] Keep `.agents/skills/session-beats/references/agency.md` and `.agents/skills/session-beats/references/session-skeleton.md` as composition references. Skeleton stays the planning form; filed spine remains Session 11-00 shape.

**Checkpoint**: US1 independently testable (quickstart steps 1 job 1, 2)

---

## Phase 4: User Story 2 - Typed beat uses that type's skill (Priority: P1)

**Goal**: Write, edit, or fill a beat of one type with that type skill as primary. Other four card catalogs not required.

**Independent Test**: Quickstart steps 1 (jobs 2–15) and 3. A Development is a Development by the completion test without other type catalogs.

### Implementation for User Story 2

Quote each type's completion test from `specs/017-session-beats-skills/data-model.md`. Each type skill owns purpose, completion test, cards for that type, how to fill this beat. Card fields: Type exactly one of the five; Trigger when fiction calls for it — not to fill a slot; Stakes visible; Player options at least two viable responses; Agency note ignoring, failing, or redirecting updates the world. Move cards out of `.agents/skills/session-beats/references/beat-types.md` into the matching type skill. Model-invoked descriptions: write, edit, or create content for that type.

- [ ] T005 [P] [US2] Create `.agents/skills/hook-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Party has committed to a response to the opening pressure. One Hook per session." Include Play a Cliffhanger as Hook and Play a Development as Hook as Hook cards.
- [ ] T006 [P] [US2] Create `.agents/skills/development-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Players can name what they now know or can decide that they could not before."
- [ ] T007 [P] [US2] Create `.agents/skills/cliffhanger-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "The contest resolved; physical situation (position, resources, safety, time) changed."
- [ ] T008 [P] [US2] Create `.agents/skills/climax-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Highest-stakes confrontation the middle made inevitable; threads harvested."
- [ ] T009 [P] [US2] Create `.agents/skills/resolution-beats/SKILL.md` (and its card reference) (Claude Code). Completes when: "Players can name what is different and what they want next."

**Checkpoint**: US1 + US2 independently testable (quickstart steps 1, 3)

---

## Phase 5: User Story 3 - Skills load each other only at named seams (Priority: P2)

**Goal**: Extra skills load only for contract seams 16–20. No standing bundle.

**Independent Test**: Quickstart step 4. Play a Cliffhanger as Hook stays one Hook.

### Implementation for User Story 3

- [ ] T010 [US3] In `.agents/skills/session-beats/SKILL.md`, load a type skill only when filling a typed slot; after load, that type skill is primary for the fill. Quote seam: "Composition filling a typed slot → That type skill; type becomes primary for the fill."
- [ ] T011 [P] [US3] In `.agents/skills/hook-beats/SKILL.md`, load `session-beats` only when chart position, polarity, threads, or transition is in question (not as primary for writing the beat). Play a Cliffhanger as Hook loads `.agents/skills/cliffhanger-beats/` for opening shape only; Play a Development as Hook loads `.agents/skills/development-beats/` for opening shape only; beat remains the session's one Hook.
- [ ] T012 [P] [US3] In `.agents/skills/development-beats/SKILL.md`, `.agents/skills/cliffhanger-beats/SKILL.md`, `.agents/skills/climax-beats/SKILL.md`, and `.agents/skills/resolution-beats/SKILL.md`, load `session-beats` only for chart position, polarity, threads, or transition; load the next type skill only when How the Scene Resolves names that type, for the handoff only. Quote: "Any other extra type-card catalog is a defect."

**Checkpoint**: US1–US3 independently testable (quickstart step 4)

---

## Phase 6: User Story 4 - Chart still follows Scripting the Game, with player agency (Priority: P2)

**Goal**: Three Beat Chart rules, polarity, budget, threads, two-plus responses, recompute.

**Independent Test**: Quickstart step 5 against contract chart rules 1–8.

### Implementation for User Story 4

- [ ] T013 [US4] In `.agents/skills/session-beats/SKILL.md` and `.agents/skills/session-beats/references/agency.md`, bind chart rules from `specs/017-session-beats-skills/contracts/beat-skill-routing.md`: one Hook to start; Developments and Cliffhangers only in alternating order; one Climax followed by one Resolution; Action Hook → next Development; cerebral Hook → next Cliffhanger; Action Climax preceded by Development; cerebral Climax preceded by Cliffhanger; about thirty minutes per beat; Hook + Climax + Resolution about ninety minutes; every prepared beat advances a live thread; at least two viable player responses; recompute rather than force the next slot. Quote data-model: "Situations not required outcomes; recompute; chart may shrink/branch/pause/end early."

**Checkpoint**: US1–US4 independently testable (quickstart step 5)

---

## Phase 7: User Story 6 - Spell and vehicle wiki pages use the new templates (Priority: P2)

**Goal**: `type: vehicle` and `type: spell` pages start from wiki templates and are runnable. `vehicle-design` fills the sheet. `spell-design` is primary for spell pages.

**Independent Test**: Quickstart step 7 against `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`.

### Implementation for User Story 6

- [X] T014 [P] [US6] Create `wiki/templates/vehicle.md` from the provided vehicle scaffold. Jobs: spoken look; sheet (size, type, speed, crew, passengers, cargo); components (hull AC/HP/DT, helm, movement, weapons when armed); crew stations; handling; combat. Omit unused sections.
- [X] T015 [P] [US6] Create `wiki/templates/spell.md` from the provided spell scaffold. Jobs: spoken look of the casting; classification line; runnable 2024 effect block (casting time, range, components, duration, saves, damage, conditions; scaling when it scales); Discovery when placement needed; Lore when history needed. Omit unused sections.
- [X] T016 [US6] In `wiki/AGENTS.md`, add `type` values `vehicle` and `spell`. Layout jobs: Vehicle — Look; sheet; components; crew stations; handling; combat. Spell — Look of the casting; classification; runnable 2024 effect; Discovery when placement needed; Lore when history needed. Quote: "Pass is those jobs."
- [ ] T017 [US6] Rewrite `.agents/skills/vehicle-design/SKILL.md` so it fills `wiki/templates/vehicle.md`, including size, type, speed, crew, and hull plus component AC/HP. Quote data-model: "Size, type, speed, crew (min), passengers, cargo filled so the craft can enter play." State what to write and when the page is done. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.
- [ ] T018 [US6] Create `.agents/skills/spell-design/SKILL.md`. Primary for write, edit, or create of a spell page. Completes when narration, classification, and a runnable 2024 effect block are filled. Discovery and Lore when the spell needs placement or history. Design-impact: designated writer, `claude-opus-4-6 --effort medium`, minimal prompt.

**Checkpoint**: US6 independently testable (quickstart step 7)

---

## Phase 8: User Story 5 - Cockpit, Work, and live-beat assembly keep their owners (Priority: P3)

**Goal**: Split does not steal `run-guide`, Work, theatre of the mind, or craft owners. Callers name the right skill.

**Independent Test**: Quickstart step 6. New live beat still reads as a Session 11 cockpit card. Zero Session 11 bodies rewritten.

### Implementation for User Story 5

- [X] T019 [P] [US5] In `.agents/skills/run-guide/SKILL.md`, load `session-beats` when the chart is missing; load the matching type skill when a live beat of that type is missing. Do not move cockpit job order into composition or type skills.
- [X] T020 [P] [US5] In `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, and `.agents/skills/sandbox-narrative/SKILL.md`, retarget typed-beat craft to `session-beats` for the chart and the matching type skill for a typed beat. Work gate stays `docs/agents/work.md`.
- [X] T021 [US5] Confirm `wiki/AGENTS.md` still points the filed spine at `.agents/skills/session-beats/SKILL.md` and cockpit jobs at `.agents/skills/run-guide/SKILL.md`. Type skills MAY hand off to theatre of the mind, encounter-prep, traps-trials, place, monster, vehicle, and spell crafts.

**Checkpoint**: All stories independently testable (quickstart steps 6–7)

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Blob gone. Evals follow owners. Quickstart holds. Dispatch flags hold.

- [ ] T022 Delete `.agents/skills/session-beats/references/beat-types.md` after its cards live in the five type skills
- [ ] T023 Split `.agents/skills/session-beats/evals/evals.json`: chart/agency/alternation/polarity evals stay on composition; type-card evals move with their type skill
- [ ] T024 Run `specs/017-session-beats-skills/quickstart.md` steps 1–8 against `specs/017-session-beats-skills/contracts/beat-skill-routing.md` and `specs/017-session-beats-skills/contracts/wiki-kind-pages.md`
- [ ] T025 Confirm this change set does not rewrite bodies of `wiki/_raw/Session-11-*.md`, does not edit `.agents/skills/writing-beats/SKILL.md`, does not copy the beat routing table into `.omp/AGENTS.md`, and leaves 0 skills that contain both the full Beat Chart and all five type-card catalogs
- [ ] T026 Confirm Claude Code was used only for T003, T005–T009, T017, T018; those dispatches used `claude-opus-4-6 --effort medium` with a prompt that names deliverables plus a completion test, per `docs/agents/skill-design-dispatch.md`; `AGENTS.md` and templates were session-agent work

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; T005–T009 parallel (five directories)
- **US3 (Phase 5)**: After US1 and US2
- **US4 (Phase 6)**: After US1 (same composition files — after T010 if US3 already started)
- **US6 (Phase 7)**: After Foundational; independent of beat type skills. T014–T015 parallel; T016 after templates; T017–T018 after T016
- **US5 (Phase 8)**: After US2 (callers need type skill names)
- **Polish (Phase 9)**: After desired stories; T022 after US2

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P1)**: After Phase 2; independent of US1 (different files)
- **US3 (P2)**: After US1 + US2
- **US4 (P2)**: After US1; same `session-beats` files as T003/T010 — do not parallelize with those
- **US6 (P2)**: After Phase 2; independent of US1–US5
- **US5 (P3)**: After US2

### Parallel Opportunities

- T005, T006, T007, T008, T009 (five type-skill directories)
- T011 vs T012 (hook vs the other four type skills)
- T014, T015 (two templates)
- T017 vs T018 after T016 (vehicle-design vs spell-design)
- T019, T020 (run-guide vs caller trio)
- Do not parallelize T002 (`AGENTS.md`) with later `AGENTS.md` edits
- Do not parallelize T003, T010, T013 (same `session-beats/SKILL.md`)
- Do not parallelize T004 with T013's `agency.md` edit
- Do not parallelize T016 with T021 (same `wiki/AGENTS.md`)

---

## Parallel Example: User Story 2

```text
Task: Create .agents/skills/hook-beats/SKILL.md (T005)
Task: Create .agents/skills/development-beats/SKILL.md (T006)
Task: Create .agents/skills/cliffhanger-beats/SKILL.md (T007)
Task: Create .agents/skills/climax-beats/SKILL.md (T008)
Task: Create .agents/skills/resolution-beats/SKILL.md (T009)
```

## Parallel Example: User Story 6

```text
Task: Create wiki/templates/vehicle.md (T014)
Task: Create wiki/templates/spell.md (T015)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `AGENTS.md` table
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
8. Polish → delete `beat-types.md`; split evals; quickstart 1–8; dispatch flags

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — skills + `AGENTS.md` + templates + pointer retargets
- Do not add test files unless a later command asks
- Do not add a beat-router skill
- Do not port Campaign OS composing/writing-*-beats
- Do not rewrite Session 11 to prove the split
- Claude Code: T003, T005–T009, T017, T018 only. Session agent: the rest
- Usage limit: defer that Claude task; complete remaining independent tasks. Queue: `docs/agents/claude-dispatch-queue.md`.
- Commit after each task or logical group
- Stop at checkpoints
