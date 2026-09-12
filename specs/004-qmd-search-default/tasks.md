---
description: "Task list for QMD Search Default"
---
# Tasks: QMD Search Default

**Input**: Design documents from `/specs/004-qmd-search-default/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/004-qmd-search-default/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US3 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contracts: `specs/004-qmd-search-default/contracts/`  
Campaign of record: `Documents/ai-co-dm` (`CONTEXT.md`)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Name the search index in the glossary and publish default collection env names.

- [X] T001 Add **Search index** to `CONTEXT.md`: derived retrieval layer over the wiki (commonly QMD); wiki remains source of truth; _Avoid_: treating the index as a second canon store
- [X] T002 [P] Add `QMD_WIKI_COLLECTION=wiki`, `QMD_LEGACY_COLLECTIONS=shattered-sea,legacy-ss`, `QMD_CLI=qmd`, `QMD_TRANSPORT=cli` to `.env.example` (no secrets; sqlite stays gitignored per `.gitignore` `**/.qmd/*.sqlite`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Project-local index with the primary `wiki` collection. Blocks all stories.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T003 Create tracked `.qmd/index.yml` for a repo-local index (not `~/.cache/qmd/index.sqlite`). Collection `wiki`: path this repo `wiki/`; default query yes; canon yes — compiled pages here
- [X] T004 Run `qmd init` at repo root if `.qmd/` is missing; confirm `qmd` uses the project index from this cwd

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Search is on without a setup ritual (Priority: P1) 🎯 MVP

**Goal**: Agents search this wiki by default. Unset env is not permission to skip.

**Independent Test**: From a clean agent session in this repo, ask for a fact that exists only on a compiled wiki page; the agent finds and cites that page without enabling search.

### Implementation for User Story 1

- [X] T005 [US1] Install the QMD skill into `.agents/skills/qmd` via `qmd skill install` (query/get mechanics; do not rewrite the upstream skill)
- [X] T006 [US1] Update `AGENTS.md`: vault retrieval is on by default against collection `wiki`; do not skip because a collection setting was empty; snippets are leads — `qmd get` / `qmd multi-get` before citing facts
- [X] T007 [US1] Update `.agents/skills/wiki-ingest/SKILL.md` Step 8 (QMD refresh): if `QMD_WIKI_COLLECTION` is empty, use `wiki`; do not skip the whole step as unset

**Checkpoint**: US1 independently testable (quickstart Story 1)

---

## Phase 4: User Story 2 - Legacy collections fill gaps; this wiki wins (Priority: P2)

**Goal**: Search campaign-of-record collections after wiki silence. This wiki is current canon.

**Independent Test**: Fact only in campaign of record → marked legacy context, not a page here. Fact in both → cite this wiki.

### Implementation for User Story 2

- [X] T008 [US2] Add collections to `.qmd/index.yml`: `shattered-sea` path `Documents/ai-co-dm/campaigns/shattered-sea` (legacy live campaign notes; not canon); `legacy-ss` path `/Users/nick/shattered-sea/wiki/shattered-sea` (older Campaign OS; not canon). Do not add `inbox`, `docs`, or `skills`
- [X] T009 [US2] Update `AGENTS.md` with retrieval order from `specs/004-qmd-search-default/contracts/retrieval-precedence.md`: `-c wiki` first; then `-c shattered-sea`; then `-c legacy-ss`; wiki hit = canon; legacy hit = campaign-of-record context, no wiki write without DM accept; wiki vs legacy disagreement → cite wiki
- [X] T010 [P] [US2] Point prep skills that already say `qmd-retrieval` at `.agents/skills/qmd` plus that precedence (do not duplicate the QMD skill body). At minimum `.agents/skills/npc-design/SKILL.md` and `.agents/skills/run-guide/SKILL.md`

**Checkpoint**: US1 + US2 independently testable (quickstart Story 2)

---

## Phase 5: User Story 3 - The index stays current without an agent remembering (Priority: P3)

**Goal**: After wiki writes, search stays usable. Maintenance is a command with exit 0/1.

**Independent Test**: File or update one wiki page, run maintenance, search a unique phrase from that page; it is found. No GUI.

### Implementation for User Story 3

- [X] T011 [US3] Add `scripts/qmd-maintain.sh` per `specs/004-qmd-search-default/contracts/qmd-maintain.md`: ensure `.qmd/` + collections `wiki`, `shattered-sea`, `legacy-ss`; `qmd update`; `qmd embed` if vectors missing; `qmd status`; probe search `-c wiki` for an existing `wiki/` page; exit 0 on ok; exit 1 on missing `qmd`, sqlite ABI load failure, missing collection, update/embed/status fail, or probe miss; stderr one line; do not write wiki pages
- [X] T012 [US3] Call `scripts/qmd-maintain.sh` from `.agents/skills/wiki-ingest/SKILL.md` after pages are written (replace skip-if-unset). On exit 1, report the failure; wiki pages already written stay; do not invent facts
- [X] T013 [US3] Update `AGENTS.md`: if search status fails at session start, run `scripts/qmd-maintain.sh`; do not skip retrieval as unset

**Checkpoint**: All stories independently testable (quickstart Story 3)

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: End-to-end check.

- [X] T014 Run `specs/004-qmd-search-default/quickstart.md` Stories 1–3. Sqlite ABI crash is exit 1, not a silent pass

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; T009 after T006 (same `AGENTS.md`)
- **US3 (Phase 5)**: After Foundational; T012 after T007 (same `wiki-ingest`); T013 after T009 (same `AGENTS.md`)
- **Polish (Phase 6)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After US1 for `AGENTS.md` only; `.qmd/index.yml` T008 after T003
- **US3 (P3)**: After US1/US2 for shared files; script T011 can start after Phase 2

### Parallel Opportunities

- T001 and T002
- T010 with T008 (different files)
- T011 with T008 after Phase 2
- Do not parallelize two edits to `AGENTS.md` or `wiki-ingest/SKILL.md`

---

## Parallel Example: After Phase 2

```text
Task: CONTEXT.md Search index term (T001)
Task: .env.example QMD_* defaults (T002)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational (`.qmd/index.yml` + `wiki`)
3. Phase 3 US1 (skill install, AGENTS, ingest no skip)
4. STOP — quickstart Story 1
5. Demo: search `-c wiki` for Hinewai

### Incremental Delivery

1. Setup + Foundational
2. US1 → default-on wiki search
3. US2 → legacy collections + precedence
4. US3 → maintain script + ingest hook
5. Polish → quickstart

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` tree — index + script + skills
- Do not add test files unless a later command asks
- Do not index ai-co-dm `inbox` / `docs` / `skills`
- Commit after each task or logical group
- Stop at checkpoints
