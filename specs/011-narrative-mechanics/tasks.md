---
description: "Task list for Expert-Grounded D&D Content Guidance"
---
# Tasks: Expert-Grounded D&D Content Guidance

**Input**: Design documents from `/specs/011-narrative-mechanics/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/011-narrative-mechanics/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US5 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US5 only on story phases
- Every task names an exact path

## Path Conventions

Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/011-narrative-mechanics/contracts/dnd-content-guidance.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, linter, or `src/`.

- [X] T001 Confirm the files listed under Source Code in `specs/011-narrative-mechanics/plan.md` exist (`.agents/skills/writing-for-agents/SKILL.md`, `.agents/skills/homebrew-monsters-5e/SKILL.md`, `.agents/skills/encounter-prep/SKILL.md`); do not add a skill, `docs/agents/narrative.md`, scanner, research row on the `AGENTS.md` stack table, or rewrite of `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Do not mix this loop into the 010 writing/visual table. User stories edit existing skills only.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Verify `.omp/AGENTS.md` still only imports `AGENTS.md` and that `AGENTS.md` has no research-then-integrate row; do not duplicate the loop there

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Research experts before changing D&D content guidance (Priority: P1) 🎯 MVP

**Goal**: `writing-for-agents` fires the research-then-integrate loop when the document is D&D content guidance. Ordinary wiki writes do not re-research.

**Independent Test**: Give an author a job to create or change a D&D content skill. A second reviewer can point to expert-solved outcomes in the guidance, or correctly reject it as vacuum-invented. An ordinary wiki page is not failed for skipping a fresh research pass.

### Implementation for User Story 1

- [X] T003 [US1] Add a D&D content guidance branch to the `description` in `.agents/skills/writing-for-agents/SKILL.md`. Quote: Kind is skill \| standing instruction \| pointed-at procedure that creates D&D wiki content; Research is required when that guidance is created or changed; Ordinary wiki content jobs are not this entity. Keep Reader `agent` → writing-for-agents. Do not own DM Work, wiki prose, or player-facing text.
- [X] T004 [US1] Add a short in-file section to `.agents/skills/writing-for-agents/SKILL.md` for that branch. Quote: Research: Named published designers and documented craft first. High-quality homebrew only if those are silent. None found → invent and flag. Integration: Expert-solved outcomes folded into this one document. Techniques may be cited. Incomplete: Vacuum-invented while experts exist; quote dump; second competing procedure; named person's process required as the only method; proprietary book paste. Do not prescribe voice, camera, or a single creative method. Host web search is the tool — do not add a tool.

**Checkpoint**: US1 independently testable (quickstart steps 1, 5)

---

## Phase 4: User Story 2 - New combat Work serves the story by default (Priority: P2)

**Goal**: First instance. Customized combat mechanics serve a named narrative beat. Number-only math is incomplete. Stock and explicit override are exempt.

**Independent Test**: Give an author a new combat Work job. A second reviewer names the narrative beat the mechanics serve, or correctly rejects the Work as math detached from the story.

### Implementation for User Story 2

- [X] T005 [P] [US2] Add combat-instance outcomes to `.agents/skills/homebrew-monsters-5e/SKILL.md` (description and/or existing Success criteria). Quote: Narrative beat is lore \| origin \| stakes \| plot \| character. A second person can name it. Incomplete: number-only custom features. Opposition stock unchanged is exempt from custom features. Override: explicit DM request for stock/featureless fight. Leave body math craft. Do not require a named person's process. Do not paste proprietary book text.
- [X] T006 [P] [US2] Add combat-instance outcomes to `.agents/skills/encounter-prep/SKILL.md` (description and/or success criteria). Quote: Narrative beat is lore \| origin \| stakes \| plot \| character. Incomplete: number-only custom features. Stock unchanged exempt. Override: explicit DM request for stock/featureless fight. Leave body craft. Do not steal statblock authorship from `homebrew-monsters-5e`.

**Checkpoint**: US1 + US2 independently testable

---

## Phase 5: User Story 3 - Combat features tell who the creature is (Priority: P3)

**Goal**: A custom ability, phase shift, or legendary action communicates lore, origin, or stakes. Removing it would lose a story tell, not only a number.

**Independent Test**: Give an author a custom combat feature. A second person can state what it says about lore, origin, or stakes without being told. A feature that only adds damage or hit points fails.

### Implementation for User Story 3

- [X] T007 [US3] Sharpen `.agents/skills/homebrew-monsters-5e/SKILL.md` so a custom combat feature (ability, phase shift, legendary action, or equivalent tell the Co-DM added or rewrote) MUST communicate lore, origin, or stakes a second person can state. Quote: Incomplete: number-only custom features. Stock published opposition used unchanged MUST NOT be required to receive custom features. After T005. Same file — not parallel with T005 or T009.

**Checkpoint**: US1–US3 independently testable

---

## Phase 6: User Story 4 - The place of the fight acts (Priority: P4)

**Goal**: A named encounter place has at least one mechanical pressure that changes strategy. Flavor-only scenery fails.

**Independent Test**: Give an author an encounter with a named place. A second person can name one mechanical pressure that belongs to that place and would change what the party does.

### Implementation for User Story 4

- [X] T008 [US4] Sharpen `.agents/skills/encounter-prep/SKILL.md` so a named place (lair, site, or battlefield) requires at least one mechanical pressure (hazard, terrain effect, structural change, or similar rule belonging to that place that changes a choice). Quote: Incomplete: flavor-only scenery on a named place. A fight the DM asked to keep as a featureless skirmish, or a job with no named place, does not require invented lair mechanics. After T006. Same file — not parallel with T006.

**Checkpoint**: US1–US4 independently testable

---

## Phase 7: User Story 5 - Homebrew changes manifest a plot beat (Priority: P5)

**Goal**: A substantial homebrew rewrite names the plot or character beat it manifests. Difficulty-only is incomplete. Light reskins do not need a tectonic shift.

**Independent Test**: Give an author a substantial homebrew modification. A second person can name the plot or character beat it manifests. A difficulty-only rewrite with no named beat fails.

### Implementation for User Story 5

- [X] T009 [US5] Sharpen `.agents/skills/homebrew-monsters-5e/SKILL.md` so a substantial homebrew change (a mechanical rewrite that changes how the creature acts, not a light reskin) MUST name the plot or character beat it manifests. Quote: Incomplete: difficulty-only homebrew with no named beat. Light reskins that do not change how a creature acts are not substantial homebrew changes. After T007. Same file — not parallel with T005 or T007.

**Checkpoint**: All five stories independently testable

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: One source of truth. No research on every wiki write. No legacy rewrite.

- [X] T010 Confirm `docs/agents/work.md` does not require expert web research on every vault write (FR-003 / SC-002). Do not add a research pointer there.
- [X] T011 Run `specs/011-narrative-mechanics/quickstart.md` steps 1–6 against `specs/011-narrative-mechanics/contracts/dnd-content-guidance.md`
- [X] T012 Confirm the change set has 0 files under `legacy/` and no historical wiki page restyled solely to match this default (SC-008)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; parallel with US1 if staffed (different files)
- **US3 (Phase 5)**: After T005 (same `homebrew-monsters-5e` file)
- **US4 (Phase 6)**: After T006 (same `encounter-prep` file)
- **US5 (Phase 7)**: After T007 (same `homebrew-monsters-5e` file)
- **Polish (Phase 8)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After Phase 2; independent of US1 (different files)
- **US3 (P3)**: After US2's T005 (same file)
- **US4 (P4)**: After US2's T006 (same file)
- **US5 (P5)**: After US3 (same file)

### Parallel Opportunities

- T005, T006 (two combat craft skills)
- T007 and T008 after their US2 tasks (different files)
- Do not parallelize two edits to the same file
- T003 then T004 on `writing-for-agents` (sequential)

---

## Parallel Example: User Story 2

```text
Task: combat outcomes in .agents/skills/homebrew-monsters-5e/SKILL.md (T005)
Task: combat outcomes in .agents/skills/encounter-prep/SKILL.md (T006)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 no second `AGENTS.md` table
3. Phase 3 US1 (`writing-for-agents`)
4. STOP — classify guidance vs ordinary wiki jobs
5. Demo: D&D content skill requires research-then-integrate outcomes; ordinary wiki write does not

### Incremental Delivery

1. Setup + Foundational
2. US1 → research loop on guidance
3. US2 → combat Work serves a named beat
4. US3 → custom features tell lore/origin/stakes
5. US4 → named place has mechanical pressure
6. US5 → substantial homebrew manifests a plot beat
7. Polish → quickstart 1–6; no legacy rewrite

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — existing skills only
- Do not add test files unless a later command asks
- Do not rewrite wiki pages or `legacy/` in this feature
- Do not add a seventh skill
- Do not add a research row to the 010 `AGENTS.md` stack table
- Commit after each task or logical group
- Stop at checkpoints
