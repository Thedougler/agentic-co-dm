---
description: "Task list for Copy Foundry Config"
---
# Tasks: Copy Foundry Config

**Input**: Design documents from `/specs/002-copy-foundry-config/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/002-copy-foundry-config/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US2 only on story phases
- Every task names an exact path

## Path Conventions

Campaign of record: `Documents/ai-co-dm` (`CONTEXT.md`)  
Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contracts: `specs/002-copy-foundry-config/contracts/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Ignore machine-local table config. Repo and skills already exist.

- [X] T001 Add `mcp.json` and `foundry-data/` to `.gitignore` (table connection settings: tracked = No)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Dest folder for imported art; Foundry skill knows local connection files exist. Blocks both stories.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 [P] Create `wiki/attachments/` (dest `wiki/attachments/<basename>`) so ingest has a place to copy art
- [X] T003 [P] Update `.agents/skills/foundry-stage/SKILL.md`: precondition local `mcp.json` + `foundry-data` symlink to the same Foundry Data directory as `Documents/ai-co-dm/foundry-data`; do not create a second world

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Reach the live development table (Priority: P1) 🎯 MVP

**Goal**: This project talks to the existing development table using campaign-of-record connection settings. Secrets stay local.

**Independent Test**: From this project, list scenes or actors on the running table. No new table. Stage one `lifecycle: accepted` page; refuse `proposed`/`rejected`.

### Implementation for User Story 1

- [X] T004 [US1] Copy `Documents/ai-co-dm/mcp.json` to repo-root `mcp.json` with the same `foundry-mcp` command, args, and `FOUNDRY_HOST` / `FOUNDRY_PORT` env
- [X] T005 [US1] Recreate repo-root `foundry-data` as a symlink whose target equals `Documents/ai-co-dm/foundry-data` (Foundry Data directory)
- [ ] T006 [US1] Prove reach: MCP list scenes or actors against that host/port succeeds (connection error fails)
- [ ] T007 [US1] Confirm `.agents/skills/foundry-stage/SKILL.md` still refuses `draft` | `proposed` | `rejected`; stage one `lifecycle: accepted` page only after T006; wording matches accepted text

**Checkpoint**: US1 independently testable (spec Independent Test / quickstart Story 1)

---

## Phase 4: User Story 2 - Bring linked art with ingest (Priority: P1)

**Goal**: Named ingest searches the campaign of record for exact basenames the source already embeds, copies hits into this vault, reports misses, never invents, never silent-overwrites.

**Independent Test**: Ingest `wiki/_raw/Bloodhawk.md`. `wiki/attachments/bloodhawk-of-aruhe-flight.jpg` and `wiki/attachments/bloodhawk-of-aruhe-token.jpg` exist and embeds open. No `young-bloodhawk-*` unless that source named it. No placeholder for misses.

### Implementation for User Story 2

- [X] T008 [US2] Update `.agents/skills/wiki-ingest/SKILL.md`: on named ingest, collect basenames from `![[file]]`, `![[file|caption]]`, and media wikilinks; search `Documents/ai-co-dm` for **exact basename** (including extension); first hit only
- [X] T009 [US2] Update `.agents/skills/wiki-ingest/SKILL.md`: found + dest absent → copy to `wiki/attachments/<basename>`; found + dest exists → skip and tell the DM; not found → no file, list the basename; never write a placeholder image
- [X] T010 [US2] Re-run named ingest of `wiki/_raw/Bloodhawk.md` only (leave the sample in `_raw/`; keep `type: creature`, linear, no `col`); expect those two jpgs in `wiki/attachments/`; report any misses

**Checkpoint**: US1 + US2 independently testable (quickstart Story 2)

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Quickstart and secret-leak check.

- [ ] T011 Run `specs/002-copy-foundry-config/quickstart.md` Stories 1–2
- [X] T012 [P] Confirm `git check-ignore -v mcp.json foundry-data` matches `.gitignore` (no table passwords/tokens in shared history)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; does not need the table reachable
- **Polish (Phase 5)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P1)**: After Phase 2 only; independently testable without Foundry MCP

### Parallel Opportunities

- T002–T003 (attachments dir vs foundry-stage SKILL.md)
- US1 and US2 after Phase 2 (different files except do not parallelize two edits to `wiki-ingest/SKILL.md`)
- T008 then T009 (same file — sequential)
- T012 with T011

---

## Parallel Example: After Phase 2

```text
Task: Copy mcp.json and recreate foundry-data symlink (US1)
Task: Update wiki-ingest for exact-basename art import (US2)
```

Do not parallelize two edits to the same `SKILL.md`.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational
3. Phase 3 US1
4. STOP — quickstart Story 1
5. Demo: MCP list from this repo hits the existing table

### Incremental Delivery

1. Setup + Foundational
2. US1 → table reachable
3. US2 → Bloodhawk embeds resolve
4. Polish → quickstart + ignore check

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` tree — local config + `wiki-ingest` + `foundry-stage`
- Do not add test files unless a later command asks
- Commit after each task or logical group
- Stop at checkpoints
