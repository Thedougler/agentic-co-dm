---
description: "Task list for Theatre of the Mind Authoring"
---
# Tasks: Theatre of the Mind Authoring

**Input**: Design documents from `/specs/013-totm-authoring/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/013-totm-authoring/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US5 → US6 → US7 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US7 only on story phases
- Every task names an exact path

## Path Conventions

Skills: `.agents/skills/<name>/SKILL.md`  
Surfaces: `.agents/skills/theatre-of-the-mind/references/surfaces.md`  
Evals: `.agents/skills/theatre-of-the-mind/evals/evals.json`  
Contract: `specs/013-totm-authoring/contracts/totm-authoring.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, linter, or `src/`.

- [ ] T001 Confirm the files listed under Source Code in `specs/013-totm-authoring/plan.md` exist (`.agents/skills/theatre-of-the-mind/SKILL.md`, `.agents/skills/theatre-of-the-mind/references/surfaces.md`, `.agents/skills/theatre-of-the-mind/evals/evals.json`, `.agents/skills/run-guide/SKILL.md`); do not add a skill, `docs/agents/totm.md`, scanner, TotM row on the `AGENTS.md` stack table, Session 11 cockpit rewrite, or rewrite of `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One owner, one procedure. Prune method sediment so story outcomes are not a second competing standard. Net tokens on `SKILL.md` must not grow.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [ ] T002 Verify `.omp/AGENTS.md` still only imports `AGENTS.md` and that `AGENTS.md` has no TotM-authoring row beyond Reader `players` → theatre of the mind; do not duplicate 013 there
- [ ] T003 In `.agents/skills/theatre-of-the-mind/SKILL.md`, remove required sentence-count floors, per-entity sentence formulas, and “completeness means every currently perceivable thing in the opening.” Keep named failures already present: work gate, situated vs standalone, no secrets/DCs/unearned names, no invented party in portraits, access/hidden-truth. Do not paste the 18-section method. Quote: Length is shortest block that makes a stable picture and performs the job. Not a word-count pass/fail. Outcomes, not a single sentence architecture.
- [ ] T004 In `.agents/skills/theatre-of-the-mind/references/surfaces.md`, remove required “you see / you hear / you feel” and the loaded-first-look dump of every perceivable subject into one opening. Keep the surface routing table and wrappers. Quote: Opening is Layer 1 immediate frame. Layers 2–3 are separate complete reveal blocks (discovery, not method). Pass 3 fills stubs (not pass 2).

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - The DM speaks prepared look without an agent (Priority: P1) 🎯 MVP

**Goal**: Player-facing theatre of the mind for a prepared Beat is complete before the session. Runtime-dependent lines are omitted, not guessed.

**Independent Test**: Hand a prepared Beat to a second DM who was not the author. They can speak the opening picture from that Work alone and return the table to a decision. They do not need the author or an agent to finish the spoken look.

### Implementation for User Story 1

- [ ] T005 [US1] Add prep-complete outcomes to `.agents/skills/theatre-of-the-mind/SKILL.md` (description and/or body). Quote: Reader is Players (spoken or shown by the DM). Runtime is Prep only. Incomplete if it can only be written after players act. Player-facing theatre of the mind for a prepared Beat MUST be complete before the session so the DM can read or paraphrase it without an agent and without inventing the opening picture. Spoken look that depends on runtime player decisions (including turn-by-turn combat and top-of-round battlefield summaries) MUST NOT be prewritten. After T003. Same file — not parallel with later SKILL.md tasks.

**Checkpoint**: US1 independently testable (quickstart step 1)

---

## Phase 4: User Story 2 - Narration never scripts the players (Priority: P1)

**Goal**: Spoken look describes the world. It does not assign PC action, thought, emotion, intent, choice, success, or an unresolved outcome.

**Independent Test**: Give a second person only the player-facing block. They cannot point to a line that assigns a PC action, thought, emotion, intent, success, or unresolved outcome. They can still picture the situation.

### Implementation for User Story 2

- [ ] T006 [US2] Sharpen `.agents/skills/theatre-of-the-mind/SKILL.md` so player-facing narration MUST describe the world. Quote: Incomplete: PC action/thought/emotion/intent/choice/success/unresolved outcome; secrets, DCs, unearned names, hidden causes, agent-process language in the spoken block. Involuntary or emotional reactions MUST be expressed through the environment when they appear, not assigned to a PC. After T005. Same file — not parallel.

**Checkpoint**: US1 + US2 independently testable (quickstart step 1)

---

## Phase 5: User Story 3 - Every block serves its Beat (Priority: P2)

**Goal**: Situated Beat openings name a Beat type and job and perform that job. Decorative prose is incomplete. Portraits do not take a Beat type.

**Independent Test**: Cover the Beat label. A second person names the job the block performs, or correctly rejects it as decorative. Deleting the block would make that Beat harder to run.

### Implementation for User Story 3

- [ ] T007 [US3] Add Beat-serving outcomes to `.agents/skills/theatre-of-the-mind/SKILL.md`. Quote: Beat is Hook \| Development \| Cliffhanger \| Climax \| Resolution, or none (portraits and short updates). Beat job is one sentence. Required when Beat is set. Decorative prose with no job is incomplete. Hook: immediate interest with minimal orientation first. Development: changed information unmistakable. Cliffhanger: danger or instability front-loaded. Climax: opposition, stakes, features, in-motion consequences clear; MUST NOT narrate victory, defeat, sacrifice, surrender, escape, or any other player-controlled outcome. Resolution: visible consequences only; conditional variants when the Climax can end substantially differently. After T006. Same file — not parallel.

**Checkpoint**: US1–US3 independently testable (quickstart step 2)

---

## Phase 6: User Story 4 - The situation is scripted; the response is not (Priority: P2)

**Goal**: Openings stay usable if the approach changes. Layer 1 is the immediate frame. Reveals describe the discovery, not the method. `run-guide` pass 3 stops dumping Layer 2/3 into Initial Narration.

**Independent Test**: Rewrite the party's approach (sneak, talk, wait, split, refuse). The same opening block and reveal blocks still work. A second person can name at least one actionable feature and one relationship among important elements.

### Implementation for User Story 4

- [ ] T008 [US4] Add state-independence and layering outcomes to `.agents/skills/theatre-of-the-mind/SKILL.md`. Quote: State independence: usable if approach changes, unless the Beat guarantees the world state. Hierarchy: most important perceptible thing first. Not an architectural inventory. Relationships: important elements related (beneath, beyond, between, blocking, …). Live ending: openings end on danger, contradiction, question, opportunity, demand, objective, or change — not a chosen response. Layer 1 is the opening. Layers 2–3 are separate complete reveal blocks (discovery, not method). Actionable features that matter now belong in Layer 1 before a player would need them. Isolated inventories without relationships MUST be treated as incomplete. After T007. Same file — not parallel.
- [ ] T009 [P] [US4] Change pass-3 completion in `.agents/skills/run-guide/SKILL.md` so Initial Narration is Layer 1 immediate frame only. Zone rows, clock ticks, and other stubs remain the reveal surface. Do not add Reveal Blocks headings. Do not change four-pass order or empty stubs on passes 1–2. Do not convert Zones from feet/compass.
- [ ] T010 [US4] Align `.agents/skills/theatre-of-the-mind/references/surfaces.md` so session Initial Narration is Layer 1 and `{Place}` / `Tick {n}` / other stubs are reveal or update surfaces. Quote: Reveals describe the finding, not who found it. After T004. Same file — not parallel with T004 or T012.

**Checkpoint**: US1–US4 independently testable (quickstart step 3)

---

## Phase 7: User Story 5 - Combat look preserves decisions without a grid (Priority: P3)

**Goal**: Combat opening is clear without a floor plan or turn script. Spoken distance is Melee / Near / Far. DM zones may keep feet.

**Independent Test**: Give a second DM only the combat opening and tactical facts. They can name threats, who is near what, cover, hazards, the objective, and a reasonable cluster for an area effect, then start the fight. They are not handed a turn script.

### Implementation for User Story 5

- [ ] T011 [US5] Add combat-package outcomes to `.agents/skills/theatre-of-the-mind/SKILL.md`. Quote: Opening: spoken. Threats, relationships, objectives, relational distance, terrain, cover, hazards, opportunities, routes, exceptional conditions. Clarity over flourish. Distance: Melee \| Near \| Far in player-facing look. Exact measure only if a rule or encounter requires it. Cluster: grouping legible enough to answer a reasonable area-effect question. Tactical reference: DM-only. Lives on the existing beat-card slots (zones, action cards, procedure). Not a TotM parallel card. Escalation / reveal: world-triggered. Complete. Does not assume PC behavior. Forbidden: turn-by-turn script; top-of-round summary; hidden-grid coordinates in spoken look. After T008. Same file — not parallel.
- [ ] T012 [US5] Align combat and spatial rows in `.agents/skills/theatre-of-the-mind/references/surfaces.md` to Melee / Near / Far in player-facing look. Quote: Exact measure only if a rule or encounter requires it. Coordinates disguised as prose fail. Combat update surface stays a short runtime line the DM invents at the table — do not prewrite it. After T010. Same file — not parallel.

**Checkpoint**: US1–US5 independently testable (quickstart step 4 combat)

---

## Phase 8: User Story 6 - Wiki portraits stay first impressions, not scenes (Priority: P3)

**Goal**: Owner-page `[!narration]` with no table state is a reusable wiki portrait. No party, no assumed encounter, no unlabeled transient facts.

**Independent Test**: Read a wiki portrait with no session context. A second person can picture and distinguish the subject, and the block still works if no encounter occurs.

### Implementation for User Story 6

- [ ] T013 [US6] Map wiki portrait to the existing standalone mode in `.agents/skills/theatre-of-the-mind/SKILL.md`. Quote: Mode is Situated moment (table or Beat state supplied) \| wiki portrait (standalone; no party/encounter). Subject: place, person, creature, ship, artifact, faction, landmark, region, or equivalent owner. Validity: across sessions. No current party state. No assumed encounter. Transient facts: omitted or clearly labeled. Completeness: recognizable identity anchors. Not every parent heading. Not a Beat. Not a scene script. Do not invent a third mode. After T011. Same file — not parallel.

**Checkpoint**: US1–US6 independently testable (quickstart step 4 portraits)

---

## Phase 9: User Story 7 - Interactive problems are solvable from the fiction (Priority: P4)

**Goal**: Traps, hazards, and trials expose a clue in the fiction. Betrayal and sabotage remain respondable. Prep is not a closed inventory.

**Independent Test**: Give a second DM the visible symptom and any earlier clue. They can name at least one approach that could work. The spoken look does not announce the solution.

### Implementation for User Story 7

- [ ] T014 [US7] Add interactive-problem outcomes to `.agents/skills/theatre-of-the-mind/SKILL.md`. Quote: Visible symptom or clue: in this scene's fiction or an earlier one. Solution: available in play. Not announced in the spoken look. Betrayal / sabotage: detectable, preventable, or respondable before irreversible. Incomplete: solvable only by omitted information; predetermined betrayal with no chance to notice. Reasonable player-created details that fit the established fiction MUST be permitted. Prep MUST NOT be treated as a closed inventory of the only legal facts. After T013. Same file — not parallel.

**Checkpoint**: All seven stories independently testable (quickstart step 4 traps)

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: One cockpit. Method-pinning evals gone. No legacy rewrite.

- [ ] T015 In `.agents/skills/theatre-of-the-mind/SKILL.md`, state that FR-032 facts use existing Session 11 slots (`[!narration]`, Now, zones, zone/tick Narration cells, Be ready for). Quote: Omit empty sections. Do not add a second cockpit. How those facts appear on a Session 11 beat card remains that card's layout. After T014. Same file — not parallel.
- [ ] T016 Drop or retarget rows in `.agents/skills/theatre-of-the-mind/evals/evals.json` that pin sentence architecture, length floors, or Strong-echo structure. Keep or add rows that observe named failures (scripting players, secrets in spoken look, portraits that stage encounters, dump openings, hidden-grid combat). Do not add a bulk suite.
- [ ] T017 Run `specs/013-totm-authoring/quickstart.md` steps 1–6 against `specs/013-totm-authoring/contracts/totm-authoring.md`
- [ ] T018 Confirm the change set has 0 files under `legacy/` and no historical wiki page restyled solely to match this standard (SC-009). Confirm `.agents/skills/theatre-of-the-mind/SKILL.md` is not longer than before T003 (Constitution IX).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After T005 (same `SKILL.md`)
- **US3 (Phase 5)**: After T006 (same `SKILL.md`)
- **US4 (Phase 6)**: After T007 for T008; T009 parallel (different file); T010 after T004
- **US5 (Phase 7)**: After T008 / T010 (same files)
- **US6 (Phase 8)**: After T011 (same `SKILL.md`)
- **US7 (Phase 9)**: After T013 (same `SKILL.md`)
- **Polish (Phase 10)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P1)**: After US1 (same file)
- **US3 (P2)**: After US2 (same file)
- **US4 (P2)**: After US3 for SKILL.md; `run-guide` (T009) after Phase 2 only
- **US5 (P3)**: After US4 SKILL.md / surfaces.md
- **US6 (P3)**: After US5 SKILL.md
- **US7 (P4)**: After US6 (same file)

### Parallel Opportunities

- T009 (`run-guide`) with any SKILL.md story after Phase 2
- T016 (`evals.json`) with T017/T018 after stories (different file from T015)
- Do not parallelize two edits to `.agents/skills/theatre-of-the-mind/SKILL.md`
- Do not parallelize two edits to `surfaces.md`

---

## Parallel Example: User Story 4

```text
Task: layering outcomes in .agents/skills/theatre-of-the-mind/SKILL.md (T008)
Task: pass-3 Layer 1 in .agents/skills/run-guide/SKILL.md (T009)
```

T010 waits on T004 and must not run beside T012.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 prune competing method; no second `AGENTS.md` table
3. Phase 3 US1 (prep-complete openings)
4. STOP — a second DM can speak a prepared opening from Work alone
5. Demo: runtime-dependent combat summaries are absent

### Incremental Delivery

1. Setup + Foundational
2. US1 → prep-complete
3. US2 → world not players
4. US3 → Beat job
5. US4 → layering + run-guide pass 3
6. US5 → combat without a grid
7. US6 → wiki portraits
8. US7 → traps from fiction
9. Polish → one cockpit; evals; quickstart 1–6; no legacy rewrite

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — existing skills only
- Do not add test files unless a later command asks
- Do not rewrite wiki pages or `legacy/` in this feature
- Do not add a seventh skill
- Do not add a TotM-authoring row to the 010 `AGENTS.md` stack table
- Do not replace Session 11 beat-card layout
- Commit after each task or logical group
- Stop at checkpoints
