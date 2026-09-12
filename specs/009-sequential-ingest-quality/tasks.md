---
description: "Task list for Sequential Ingest Quality"
---
# Tasks: Sequential Ingest Quality

**Input**: Design documents from `/specs/009-sequential-ingest-quality/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/009-sequential-ingest-quality/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US3 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, store, or `_raw/` rewrite.

- [X] T001 Confirm the files listed under Source Code in `specs/009-sequential-ingest-quality/plan.md` exist (`.agents/skills/wiki-ingest/SKILL.md`, `wiki/AGENTS.md`, `wiki/log.md`, `wiki/.manifest.json`); do not add a skill, ingest-run store, `src/`, or rewrite of `wiki/_raw/` or `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Kind jobs stay in AGENTS.md. Ingest will point here, not copy the job table. Sequential unit is one input file.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Update `wiki/AGENTS.md` Layout: ingest judges filed pages against campaign kinds and jobs in this file, not against an incoming source outline; incoming files are evidence, not exemplary format; `_raw/` illustrates quality and is not a clone target. Keep the existing place/session-prep required treatments. Do not paste `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md` into AGENTS.md. Do not duplicate the Layout job table.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - One file finishes before the next starts (Priority: P1) 🎯 MVP

**Goal**: Multi-file ingest completes or fails one input file before the next starts. No overlapping files.

**Independent Test**: Three approved sources. File 2 produces no wiki pages and no tracking updates until file 1 is complete. Large folders still one-at-a-time.

### Implementation for User Story 1

- [X] T003 [US1] Replace Step 0 parallel subagent dispatch in `.agents/skills/wiki-ingest/SKILL.md` with a sequential file loop per `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md` items 1–5: one input file is `open` at a time; file state is `pending` → `open` → `complete` | `failed`; processing order is the order the DM named, else folder listing order; MUST NOT create or change wiki pages or tracking for a later file while an earlier file is `open`; completing a file means required pages filed or stubbed, tracking updated, file marked `complete` or `failed`; folder size, batch size, and a request for speed MUST NOT authorize overlap; unreadable, empty, or non-source binary → `failed` with a reason, then next file; remaining files still run sequentially; a later file MAY update a page from an earlier file only after the earlier file is `complete` or `failed`; manifest hash updated only on `complete`. `cache-check` may still skip unchanged. Delete “dispatch each batch as a parallel subagent” and “Other files in the same batch continue.” Do not add a new skill.

**Checkpoint**: US1 independently testable (quickstart step 1)

---

## Phase 4: User Story 2 - Campaign formats are the quality bar (Priority: P1)

**Goal**: Filed pages match campaign kinds and jobs. Incoming layouts are not the format to copy.

**Independent Test**: Ingest one foreign-format source that names a complete place (or other kind). The wiki page answers that kind’s jobs. A campaign-shaped place still keeps `[!narration]`.

### Implementation for User Story 2

- [X] T004 [US2] Update `.agents/skills/wiki-ingest/SKILL.md` quality target per `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md` items 6–10 and `wiki/AGENTS.md` Layout: incoming files MUST be treated as evidence of facts, MUST NOT be treated as exemplary page format; a filed wiki page MUST match the campaign kind for its subject and MUST answer that kind’s run jobs; MUST NOT copy a foreign outline, heading list, or density band as the wiki page shape; a source that already matches a campaign kind is still judged against that kind’s jobs and required treatments; campaign-shaped session-prep and place keep 007/008 required treatments (session-prep body; place `[!narration]`); foreign sources of those subjects map into the kind, they are not photocopied. Point at Layout; do not paste the job table. Remove language that incoming or `_raw/` source format is the format to copy.

**Checkpoint**: US2 independently testable (quickstart steps 2–3)

---

## Phase 5: User Story 3 - The DM can see each file complete (Priority: P2)

**Goal**: After a multi-file ingest, the DM can read order, complete/failed, pages, and failure reasons.

**Independent Test**: Three files, middle unreadable. Report lists 1 complete, 2 failed with a reason, 3 complete. No file 3 pages before file 2 is closed.

### Implementation for User Story 3

- [X] T005 [US3] Update `.agents/skills/wiki-ingest/SKILL.md` so each closed file writes a `wiki/log.md` line and the end-of-run report lists every file in processing order as `complete` or `failed`, with the pages that file produced or updated and a reason for each failure, per `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md` items 11–12. A later update to an earlier page is attributed to the later file. Do not add `_meta/ingest-runs.json` or another store. Failed files MUST NOT be hashed as success in `wiki/.manifest.json`.

**Checkpoint**: US3 independently testable (quickstart step 4)

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Prove sequential + quality bar without touching legacy or gold evidence bodies.

- [X] T006 Run `specs/009-sequential-ingest-quality/quickstart.md` steps 1–6 except actual wiki writes if the DM has not approved filing; confirm `.agents/skills/wiki-ingest/SKILL.md` has no parallel file dispatch and points at `wiki/AGENTS.md` Layout as the quality bar
- [X] T007 Confirm the change set does not rewrite bodies of `wiki/_raw/` or `legacy/` solely to match campaign kinds, and that Layout jobs were not duplicated into `.agents/skills/wiki-ingest/SKILL.md` (FR-008, SC-004, Constitution IX)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After T003 (same file `.agents/skills/wiki-ingest/SKILL.md`)
- **US3 (Phase 5)**: After T004 (same file)
- **Polish (Phase 6)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2; T003 alone
- **US2 (P1)**: After T003; same file, not parallel
- **US3 (P2)**: After T004; same file, not parallel

### Parallel Opportunities

- None inside US1/US2/US3 (single skill file)
- T006 then T007 sequential after implementation

---

## Parallel Example: User Story 1

```text
# Single-file story — do not parallelize
Task: sequential file loop in .agents/skills/wiki-ingest/SKILL.md (T003)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 AGENTS.md quality-bar pointer
3. Phase 3 T003 — sequential complete-before-next
4. STOP — dry-run three-file order
5. Demo: file 2 does not start while file 1 is open

### Incremental Delivery

1. Setup + Foundational
2. US1 → sequential ingest
3. US2 → campaign kinds as bar
4. US3 → per-file report
5. Polish → quickstart; no `_raw/` or legacy rewrite

---

## Notes

- [P] unused — stories edit `wiki-ingest` then polish
- No `src/`
- Do not add test files unless a later command asks
- Do not rewrite `_raw/` bodies or legacy
- Commit after each task
- Stop at checkpoints
