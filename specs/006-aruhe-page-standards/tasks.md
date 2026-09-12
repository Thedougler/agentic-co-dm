---
description: "Task list for Sample Content Guidance"
---
# Tasks: Sample Content Guidance

**Input**: Design documents from `/specs/006-aruhe-page-standards/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/006-aruhe-page-standards/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US5 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US5 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/006-aruhe-page-standards/contracts/sample-page.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, linter, or `src/`.

- [X] T001 Confirm the files listed under Source Code in `specs/006-aruhe-page-standards/plan.md` exist; do not add a skill, scanner, or rewrite of `legacy/` or `wiki/_raw/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One Layout section is the sample default. Skills and templates will point here.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Replace the Layout section in `wiki/AGENTS.md` with run-jobs from `specs/006-aruhe-page-standards/contracts/sample-page.md`. Done-when is jobs + omit-empty, not heading-order match. State: templates are copy-start scaffolds; `wiki/_raw/` illustrates and is not a clone target; campaign `type` stays the closed set (`place` \| `item` \| `creature` \| `npc` \| `faction` \| `session` \| `recap` \| `work`); map early sample labels `location`→`place`, `monster`→`creature`, `lore`→`item` on file; unused identity keys omitted; `lifecycle` default `proposed` until DM accept; `visibility` default `dm` and distinct from `reveal`; `summary` one sentence; legacy content is out of scope and wrapup MUST NOT convert it.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Any sample page is runnable in one pass (Priority: P1) 🎯 MVP

**Goal**: Shared writer skills pass on spoken look + run questions, not cloned outlines.

**Independent Test**: Open one complete `_raw/` page per kind; speak the look (no secret/DC/unearned name); answer that kind's jobs without a second copy of numbers; no empty headings.

### Implementation for User Story 1

- [X] T003 [P] [US1] Update `.agents/skills/copy-writer/SKILL.md`: sample pages succeed on jobs in `wiki/AGENTS.md` Layout; named `_raw/` files are illustrative not clone targets; spoken look is theatre of the mind (no secrets, DCs, unearned names, author thesis); empty sections omitted; unused identity keys omitted
- [X] T004 [P] [US1] Update `.agents/skills/obsidian-markdown/SKILL.md`: campaign `type` `creature` not `monster` on file; do not forbid column density on creatures; do not require heading-order match as done-when
- [X] T005 [P] [US1] Update `.agents/skills/wiki-ingest/SKILL.md`: leave early-dev `_raw/` samples in `_raw/` as illustrations, not “layout source”; wrapup of a legacy page MUST NOT convert that page into a sample

**Checkpoint**: US1 independently testable (quickstart steps 1–2, 6)

---

## Phase 4: User Story 2 - Sample places are a run loop (Priority: P2)

**Goal**: Place writers answer look, situation, consequential moves, presence-or-absence, table objects, connections, purpose.

**Independent Test**: A second DM speaks the look, names a way onward, resolves one consequential move, and says why the site exists, from a sample place alone.

### Implementation for User Story 2

- [X] T006 [P] [US2] Edit `wiki/templates/place.md` into a copy-start scaffold for those place jobs; mark unused sections omit-if-empty; do not treat heading list as pass/fail
- [X] T007 [P] [US2] Update `.agents/skills/place-design/SKILL.md`: file into `wiki/templates/place.md` as scaffold; pass on place jobs; `wiki/_raw/Old Gardens.md` and `wiki/_raw/River Line Bank.md` are illustrations; do not require matching their headings
- [X] T008 [P] [US2] Update `.agents/skills/place-design/references/location-skeleton.md` the same way: check jobs, not a second required outline

**Checkpoint**: US1 + US2 independently testable

---

## Phase 5: User Story 3 - Sample objects resolve in one use (Priority: P3)

**Goal**: Consumable = portrait, classification, one effect, stop. Flora hazard = look + start, notice, cost, careful passage, counterplay.

**Independent Test**: Resolve a consumable use, or notice and refuse a hazard, from that sample page alone; places link the owner instead of copying numbers.

### Implementation for User Story 3

- [X] T009 [P] [US3] Edit `wiki/templates/item.md`: scaffold for portrait, classification, one runnable effect, then stop; omit unused keys including `owner` when unused
- [X] T010 [P] [US3] Edit `wiki/templates/hazard.md`: scaffold for look plus start, notice, contact cost, careful passage, counterplay; extra mechanical rows only when they change the table; omit-if-empty
- [X] T011 [US3] Update `.agents/skills/dnd-5e-magic-item-design/SKILL.md`: copy those templates as scaffolds; `wiki/_raw/Ghost Plum.md` and `wiki/_raw/Razer-Grass.md` illustrate; do not freeze “image → narration → type-line → mechanics” as the only legal outline; numbers live on one owner page

**Checkpoint**: US1–US3 independently testable

---

## Phase 6: User Story 4 - Sample creatures are a hunt (Priority: P4)

**Goal**: Creature pages answer look, runnable sheet, life (habitat, habits, diet, social), hunt (signs, instincts, opening, shut-down, aftermath). Density may vary.

**Independent Test**: Speak the look, name habitat, run the opening move, name one party-doable shut-down, from a sample creature alone.

### Implementation for User Story 4

- [X] T012 [P] [US4] Edit `wiki/templates/creature.md`: scaffold for look, sheet, life, hunt; Visual reference omit-if-empty; do not require linear-only layout
- [X] T013 [US4] Update `.agents/skills/homebrew-monsters-5e/SKILL.md`: pass on creature jobs; `wiki/_raw/Bloodhawk.md`, `wiki/_raw/Deerstalker.md`, and `wiki/_raw/Wolfrabbit.md` illustrate density; do not forbid column wrappers; shut-downs MUST be things the party can do; habitat names ground it uses and ground it refuses when that refusal is true

**Checkpoint**: US1–US4 independently testable

---

## Phase 7: User Story 5 - Sample people are playable, not cloned bands (Priority: P5)

**Goal**: Person pages answer who/want, look, first minutes and posture change, named ties; combat only if they can fight. Named `_raw/` NPCs are density examples, not required classes.

**Independent Test**: Name role, want, first move, and fight handling from a sample person alone; unused extra depth is omitted, not missing.

### Implementation for User Story 5

- [X] T014 [P] [US5] Edit `wiki/templates/npc.md`: scaffold for who/want, look, first minutes and posture change, named ties; Combat omit-if-empty; unused identity keys omitted (`location` `unknown` when unknown; `faction` `none` when unknown; omit `aliases` when unused)
- [X] T015 [US5] Update `.agents/skills/npc-design/SKILL.md`: copy `wiki/templates/npc.md` as scaffold; pass on person jobs in `wiki/AGENTS.md`; `wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`, `wiki/_raw/Nona Black-Jaw.md`, `wiki/_raw/Thunk.md` illustrate density; do not require cloning those outlines or treating landmark/skirmish/patron/contact as frozen classes; Combat only if fightable (encounter rule plus sheet or one pointer)
- [X] T016 [P] [US5] Update `.agents/skills/npc-design/references/npc-templates.md`: same jobs-not-clone rule; `specs/003-npc-page-standard/contracts/npc-page.md` is optional extra depth when facts exist, not a clone target

**Checkpoint**: All five stories independently testable

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Prove the default without touching legacy.

- [X] T017 Run `specs/006-aruhe-page-standards/quickstart.md` steps 1, 2, 5, and 6; do not rewrite `wiki/_raw/` bodies; do not edit `legacy/`
- [X] T018 Confirm the change set has 0 files under `legacy/` and no historical page restyled solely to match sample jobs (SC-006)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2–US5 (Phases 4–7)**: After Foundational; parallel with each other (different files)
- **Polish (Phase 8)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After Phase 2; independent of other stories
- **US3 (P3)**: After Phase 2; T011 after T009–T010
- **US4 (P4)**: After Phase 2; T013 after T012
- **US5 (P5)**: After Phase 2; T015 after T014; T016 parallel with T015

### Parallel Opportunities

- T003, T004, T005 (three skills)
- T006, T007, T008 (place template + two place-design files)
- T009, T010 then T011
- T012 then T013
- T014, then T015 + T016
- After Phase 2, US2–US5 can run in parallel if staffed
- Do not parallelize two edits to the same file

---

## Parallel Example: User Story 1

```text
Task: copy-writer jobs-not-clone in .agents/skills/copy-writer/SKILL.md (T003)
Task: obsidian-markdown type creature + density in .agents/skills/obsidian-markdown/SKILL.md (T004)
Task: wiki-ingest illustrations not layout source in .agents/skills/wiki-ingest/SKILL.md (T005)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `wiki/AGENTS.md` Layout
3. Phase 3 US1 (copy-writer, obsidian-markdown, wiki-ingest)
4. STOP — quickstart steps 1, 2, 6
5. Demo: open five `_raw/` kinds; Layout done-when is jobs

### Incremental Delivery

1. Setup + Foundational
2. US1 → shared default
3. US2 → places
4. US3 → items/hazards
5. US4 → creatures
6. US5 → people
7. Polish → quickstart 1, 2, 5, 6

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — AGENTS.md + templates + existing skills
- Do not add test files unless a later command asks
- Do not rewrite `_raw/` or `legacy/` in this feature
- Commit after each task or logical group
- Stop at checkpoints

## Phase 9: Convergence

- [X] T019 Put default `visibility: dm` (distinct from `reveal`) on sample identity in `wiki/templates/place.md`, `wiki/templates/item.md`, `wiki/templates/hazard.md`, and `wiki/templates/creature.md`, and name `visibility` plus `campaign` in the frontmatter contract in `.agents/skills/obsidian-markdown/SKILL.md` per FR-013 (`partial`)
- [X] T020 State presence-or-absence and do-not-invent-occupants on the Who scaffold in `wiki/templates/place.md` per FR-007 (`partial`)

