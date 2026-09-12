---
description: "Task list for Place Ingest Preserve"
---
# Tasks: Place Ingest Preserve

**Input**: Design documents from `/specs/008-place-ingest-preserve/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/008-place-ingest-preserve/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US2 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/008-place-ingest-preserve/contracts/place-ingest.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, linter, or `_raw/` rewrite.

- [X] T001 Confirm the files listed under Source Code in `specs/008-place-ingest-preserve/plan.md` exist; do not add a skill, scanner, `src/`, or rewrite of `wiki/_raw/Aruhe - Old Gardens.md` or `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Place jobs stay in AGENTS.md. Ingest will point here, not copy the job table.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Confirm `wiki/AGENTS.md` Layout still states place run questions (look; situation now; moves that change the scene; presence or sign of absence; table objects; connections; purpose) and spoken look as theatre of the mind with `[!narration]` only. Add one sentence: ingest of `type: place` preserves that page (does not distill). Do not paste the place-ingest contract into AGENTS.md.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Ingested places still have spoken look (Priority: P1) 🎯 MVP

**Goal**: Ingest keeps the required open `[!narration]` Narration block.

**Independent Test**: Ingest one complete place with filled `[!narration]` Narration. Open the filed wiki page. Speak the look. The callout is still there, filled, player-safe.

### Implementation for User Story 1

- [X] T003 [US1] Update `.agents/skills/wiki-ingest/SKILL.md` Session-prep preserve into a preserve branch that also matches `type: place` per `specs/008-place-ingest-preserve/contracts/place-ingest.md`: copy body unchanged; MUST keep the open `[!narration]` titled **Narration** (typically under Overview); MUST NOT delete it, empty a filled look, or convert it to ordinary prose; a stub place still keeps the titled block even if the body is empty; spoken look MUST remain theatre of the mind (no secrets, difficulty classes, unearned names). Session-prep destination and rules stay as 007. Do not add a new skill.

**Checkpoint**: US1 independently testable (quickstart step 1)

---

## Phase 4: User Story 2 - Ingest does not mutate place format (Priority: P1)

**Goal**: Ingested places stay `type: place` in campaign shape, filed under `wiki/entities/`.

**Independent Test**: Side-by-side source and wiki page. Heading spine, embeds, wikilinks, and `[!narration]` still match. Not a concept note.

### Implementation for User Story 2

- [X] T004 [US2] Update `.agents/skills/wiki-ingest/SKILL.md` preserve branch: `type: place` files to `wiki/entities/` with the source filename; MUST NOT distill into `concepts/` or replace the outline with a knowledge-wiki template; keep Overview, At a glance, If the party, Who, What, Where, Why, and Art when present; omit unused jobs (no empty headings, no invented occupants); owner numbers stay linked not copied; mixed batch still distills ordinary knowledge; re-ingest with no body change MUST NOT rewrite; `_raw/` place evidence stays in `_raw/` with copies filed rather than restyling the evidence set; unaccepted Work does not publish except named ingest of approved sources. Step 2 GUARD already skips distill for preserved sources — include `type: place`.

**Checkpoint**: US2 independently testable (quickstart steps 2–4)

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Prove preserve without touching legacy or gold evidence bodies.

- [X] T005 Run `specs/008-place-ingest-preserve/quickstart.md` steps 1–6 except actual wiki writes if the DM has not approved filing; confirm the preserve GUARD in `.agents/skills/wiki-ingest/SKILL.md` names `type: place` and `[!narration]`
- [X] T006 Confirm the change set does not rewrite bodies of `wiki/_raw/` places or `legacy/` solely to match this format (FR-010, SC-005)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After T003 (same file `.agents/skills/wiki-ingest/SKILL.md`)
- **Polish (Phase 5)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2; T003 alone
- **US2 (P1)**: After T003; same file, not parallel

### Parallel Opportunities

- None inside US1/US2 (single skill file)
- T005 then T006 sequential after implementation

---

## Parallel Example: User Story 1

```text
# Single-file story — do not parallelize
Task: preserve [!narration] on type: place in .agents/skills/wiki-ingest/SKILL.md (T003)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 AGENTS.md one-sentence ingest pointer
3. Phase 3 T003 — place narration preserved
4. STOP — dry-run Old Gardens narration block
5. Demo: callout still present after preserve path

### Incremental Delivery

1. Setup + Foundational
2. US1 → narration survives
3. US2 → shape + `wiki/entities/` + mixed batch
4. Polish → quickstart; no `_raw/` or legacy rewrite

---

## Notes

- [P] unused here — both stories edit `wiki-ingest`
- No `src/`
- Do not add test files unless a later command asks
- Do not rewrite `_raw/` place bodies or legacy
- Commit after each task
- Stop at checkpoints
