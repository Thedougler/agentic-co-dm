---
description: "Task list for Agentic Co-DM implementation"
---
# Tasks: Agentic Co-DM

**Input**: Design documents from `/specs/001-agentic-co-dm/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/001-agentic-co-dm/quickstart.md`.

**Organization**: Setup → Foundational → US1–US4 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US4 only on story phases
- Every task names an exact path

## Path Conventions

Skills: `.agents/skills/<name>/SKILL.md`  
Wiki: `wiki/`  
Contracts: `specs/001-agentic-co-dm/contracts/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Vault conventions this feature needs. Repo and skills already exist.

- [X] T001 Create `wiki/AGENTS.md` with campaign `type` enum (`npc`, `place`, `faction`, `item`, `creature`, `session`, `recap`, `work`), `lifecycle` enum (`draft` | `proposed` | `accepted` | `rejected` | `canon`), `reveal` enum (`unrevealed` | `revealed`), and FR-018 (complete-sentence human prose; no AI shorthand)
- [X] T002 [P] Add `wiki/templates/work.md` with required frontmatter `title`, `category`, `tags`, `sources`, `created`, `updated`, `type: work`, `lifecycle: proposed`, `reveal`, `grounded_in`, `invention`
- [X] T003 [P] Add `wiki/templates/npc.md` with `type: npc`, same required frontmatter plus `lifecycle` and `reveal`, body sections in complete sentences
- [X] T004 [P] Add `wiki/templates/place.md` with `type: place`, same required frontmatter plus `lifecycle` and `reveal`
- [X] T005 [P] Add `wiki/templates/session.md` with `type: session` for wrapup logs
- [X] T006 Replace "Bank facts" with "wiki facts" in `docs/adr/0003-canon-changes-are-proposals.md`
- [X] T052 [P] Rewrite `wiki/templates/place.md` to Overview, At a glance, If the party, Who, What, Where, Why, Art matching `wiki/_raw/Old Gardens.md` and `wiki/_raw/River Line Bank.md`
- [X] T053 [P] Add `wiki/templates/item.md` matching `wiki/_raw/Ghost Plum.md` (image, `[!narration]`, type-line, mechanics)
- [X] T054 [P] Add `wiki/templates/hazard.md` matching `wiki/_raw/Razer-Grass.md` (`type: item`)
- [X] T055 [P] Add `wiki/templates/creature.md` linear (no `col`) matching `wiki/_raw/Bloodhawk.md`
- [X] T056 Point `.agents/skills/place-design/SKILL.md`, `.agents/skills/copy-writer/SKILL.md`, `.agents/skills/homebrew-monsters-5e/SKILL.md`, `.agents/skills/dnd-5e-magic-item-design/SKILL.md`, and `wiki/AGENTS.md` at those templates

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared Work rules and glossary pointers. Blocks every user story.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T007 Write `docs/agents/work.md` from `specs/001-agentic-co-dm/contracts/work.md`: Co-DM output is Work; lifecycle `draft` → `proposed` → `accepted` | `rejected`; invention required, grounded in wiki pages and/or D&D 5e rules, never a fake wiki fact; canon only after DM accept
- [X] T008 Add a context pointer in root `AGENTS.md` to `docs/agents/work.md` and `wiki/AGENTS.md` (when to load; do not duplicate the glossary)
- [X] T009 Rewrite `.agents/skills/copy-writer/SKILL.md`: rename the Bank band to wiki/owner facts; keep complete grammatical sentences and the telegram-stub failure mode; point at `docs/agents/work.md`; never write silent canon
- [X] T010 Point `.agents/skills/obsidian-markdown/SKILL.md` at `wiki/AGENTS.md` frontmatter (`type`, `lifecycle`, `reveal`) for every vault write
- [X] T047 Rewrite `docs/agents/work.md` from `specs/001-agentic-co-dm/contracts/work.md`: chat proposal before any campaign wiki write (FR-019); reject leaves no page; named ingest is approval for those sources plus thin stubs for names in them

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Distill campaign knowledge into a second brain (Priority: P1) 🎯 MVP

**Goal**: Ingest named sources into `wiki/` as linked, citable, human-prose pages plus thin stubs for names in those sources. Early-dev `_raw/` samples keep their section layout. Co-DM answers from those pages with citations. No invented extra pages.

**Independent Test**: Name one file in `wiki/_raw/` and approve ingest; open the page in Obsidian; confirm the sample's section order and markdown remain (early-dev exception); follow a stub link for a name in that source; confirm no page for a name the source lacks; a creature page stays linear (no `col`); ask a covered fact and get a `[[citation]]`. Telegram copy fails.

### Implementation for User Story 1

- [X] T011 [US1] Set this repo's vault as the ingest target: create `.env` with `OBSIDIAN_VAULT_PATH` pointing at `wiki/` (absolute path)
- [X] T012 [US1] Update `.agents/skills/wiki-ingest/SKILL.md` so every distilled page uses `wiki/AGENTS.md` frontmatter, loads `copy-writer` + `obsidian-markdown`, and is invalid if the body is AI shorthand
- [X] T013 [US1] Update `.agents/skills/wiki-query/SKILL.md` so factual answers retrieve from `wiki/` pages and name those pages; do not present invented material as a wiki fact
- [X] T014 [US1] Update `.agents/skills/llm-wiki/SKILL.md` category guidance so campaign entities use `type` from `wiki/AGENTS.md` rather than only generic llm-wiki categories
- [X] T015 [US1] Run ingest on one file in `wiki/_raw/` and confirm `wiki/.manifest.json`, `wiki/index.md`, and `wiki/log.md` record the source and pages
- [X] T048 [US1] Update `.agents/skills/wiki-ingest/SKILL.md` for FR-019 and research §10: only named approved sources; thin complete-sentence stubs for names in those sources; do not create pages for names the sources do not contain; early-dev `wiki/_raw/` samples keep section order, markdown, callouts, tables, and embeds; general ingest still distills; creature pages stay linear
- [X] T049 [P] [US1] Update `wiki/AGENTS.md` so campaign pages are not written without DM approval except named ingest and named-in-source stubs (FR-019); keep the Layout table mapping sample `location`/`monster`/`lore` to `place`/`creature`/`item`

**Checkpoint**: US1 independently testable (spec Independent Test / quickstart Story 1)

---

## Phase 4: User Story 2 - Agent proposes; DM decides (Priority: P2)

**Goal**: Prep craft shows a chat proposal. DM accepts, edits, or rejects. Wiki page only after approval. Invention is required and grounded. No Co-DM during a session. Full D&D 5e pack is in v1.

**Independent Test**: Ask for a beat covered by the wiki and a new NPC the wiki lacks; both are DM-addressed **chat proposals with no wiki page yet**; the NPC is marked invention, grounded in wiki pages and/or 5e rules; accept one then a page appears; reject one and no page is filed; players see nothing.

### Implementation for User Story 2

Each skill below must: show a chat proposal before any wiki write (FR-019); ground invention in wiki pages and/or D&D 5e rules; never contradict a page without showing the DM; never present invention as a wiki fact; follow `docs/agents/work.md` and `writing-for-agents`.

- [X] T016 [US2] Rewrite `.agents/skills/npc-design/SKILL.md` to the Work gate (new NPCs are proposed Work; `type: npc` only becomes `canon` after accept)
- [X] T017 [P] [US2] Rewrite `.agents/skills/place-design/SKILL.md` to the Work gate
- [X] T018 [P] [US2] Rewrite `.agents/skills/dungeon-design/SKILL.md` to the Work gate
- [X] T019 [P] [US2] Rewrite `.agents/skills/faction-prep/SKILL.md` to the Work gate
- [X] T020 [P] [US2] Rewrite `.agents/skills/encounter-prep/SKILL.md` to the Work gate
- [X] T021 [P] [US2] Rewrite `.agents/skills/homebrew-monsters-5e/SKILL.md` to the Work gate
- [X] T022 [P] [US2] Rewrite `.agents/skills/dnd-5e-magic-item-design/SKILL.md` to the Work gate
- [X] T023 [P] [US2] Rewrite `.agents/skills/dnd5e-mechanics/SKILL.md` so rulings are proposed Work grounded in 5e rules + wiki pages
- [X] T024 [P] [US2] Rewrite `.agents/skills/session-beats/SKILL.md` to the Work gate (prep only)
- [X] T025 [P] [US2] Rewrite `.agents/skills/run-guide/SKILL.md` to the Work gate (prep only)
- [X] T026 [P] [US2] Rewrite `.agents/skills/theatre-of-the-mind/SKILL.md` so spoken copy is Work for the DM, player-safe, `[!narration]` only
- [X] T027 [P] [US2] Rewrite `.agents/skills/cold-opens/SKILL.md` to the Work gate
- [X] T028 [P] [US2] Rewrite `.agents/skills/campaign-planning/SKILL.md` to the Work gate
- [X] T029 [P] [US2] Rewrite `.agents/skills/traps-trials/SKILL.md` to the Work gate
- [X] T030 [P] [US2] Rewrite `.agents/skills/vehicle-design/SKILL.md` to the Work gate
- [X] T031 [P] [US2] Rewrite `.agents/skills/travel-events/SKILL.md` to the Work gate
- [X] T032 [P] [US2] Rewrite `.agents/skills/narrative-islands/SKILL.md` to the Work gate
- [X] T033 [P] [US2] Rewrite `.agents/skills/sandbox-narrative/SKILL.md` to the Work gate
- [X] T034 [P] [US2] Rewrite `.agents/skills/writing-beats/SKILL.md` to the Work gate
- [X] T035 [P] [US2] Rewrite `.agents/skills/pc-interview/SKILL.md` to the Work gate
- [X] T036 [P] [US2] Rewrite `.agents/skills/visual-aids/SKILL.md` and `.agents/skills/visual-references/SKILL.md` to the Work gate (prep art is Work, not auto-canon)

**Checkpoint**: US1 + US2 independently testable (quickstart Story 2)

---

## Phase 5: User Story 3 - Present accepted content at the table (Priority: P3)

**Goal**: Only accepted Work reaches Foundry. Drafts and rejects are refused.

**Independent Test**: Accept one piece; stage it; players see that wording. Staging a rejected page fails.

### Implementation for User Story 3

- [X] T037 [US3] Rewrite `.agents/skills/foundry-stage/SKILL.md`: precondition `lifecycle: accepted`; refuse `draft` | `proposed` | `rejected`; refuse player-visible staging when `reveal: unrevealed` until the DM accepts a reveal; wording matches accepted text; prep only
- [X] T038 [P] [US3] Rewrite `.agents/skills/foundry-battlemap/SKILL.md` with the same accepted-Work gate
- [X] T039 [P] [US3] Rewrite `.agents/skills/foundry-token/SKILL.md` with the same accepted-Work gate

**Checkpoint**: US3 independently testable if Foundry MCP is up; otherwise verify the skill refuses unaccepted pages

---

## Phase 6: User Story 4 - Return table outcomes to the wiki (Priority: P4)

**Goal**: Wrapup proposes what happened, then updates wiki pages after accept. Later answers cite post-session pages.

**Independent Test**: Propose an outcome that contradicts prep; no wiki write until accept; after accept the wiki matches play; a later question cites the outcome page.

### Implementation for User Story 4

- [X] T040 [US4] Rewrite `.agents/skills/session-wrapup/SKILL.md`: remap `campaigns/<slug>/` to `wiki/`; outcomes are `lifecycle: proposed` until accept; then surgical owner-page updates; unused prep is not canon; no silent canon
- [X] T041 [P] [US4] Rewrite `.agents/skills/session-recap/SKILL.md` to file recap as proposed Work, human prose, wiki not bank
- [X] T042 [P] [US4] Rewrite `.agents/skills/reconciling-session-evidence/SKILL.md` so contradictions surface to the DM (FR-011)
- [X] T043 [P] [US4] Rewrite `.agents/skills/world-tick/SKILL.md` so off-screen movement is proposed Work grounded in wiki pages, not silent canon
- [X] T050 [P] [US4] Update `.agents/skills/session-recap/SKILL.md` so recap is a chat proposal first and is not filed to `wiki/` until DM accept (FR-019)
- [X] T051 [P] [US4] Update `.agents/skills/session-wrapup/SKILL.md` so wrapup is a chat proposal first and wiki pages change only after DM accept (FR-019); keep remap to `wiki/` and no silent canon

**Checkpoint**: Full loop in `specs/001-agentic-co-dm/quickstart.md`

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Pack completeness, glossary, quickstart.

- [X] T044 Replace remaining "bank" / "knowledge bank" wording in touched skills under `.agents/skills/` with "wiki" (skip historical quotes)
- [X] T045 Confirm every v1 craft skill listed in `specs/001-agentic-co-dm/data-model.md` points at `docs/agents/work.md` and prep/wrapup windows
- [X] T046 Run `specs/001-agentic-co-dm/quickstart.md` Stories 1–2 (and 3–4 if Foundry is available). Do not invent campaign people. Chat proposal before any wiki write (FR-019). Early-dev `_raw/` ingest keeps sample layout.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; uses US1 wiki pages when present
- **US3 (Phase 5)**: After US2 accepted Work exists
- **US4 (Phase 6)**: After US1 wiki pages exist; wrapup can be tested with a hand-edited outcome
- **Polish (Phase 7)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After Phase 2; independently testable with a hand-written wiki page if US1 ingest is skipped
- **US3 (P3)**: Needs at least one `lifecycle: accepted` page
- **US4 (P4)**: Needs at least one wiki page to update

### Parallel Opportunities

- T047 then T048–T049 (FR-019 ingest gate + early-dev layout)
- T050–T051 (wrapup/recap chat-first, different files)
- T002–T005 (templates)
- T017–T036 (US2 skill rewrites, different `SKILL.md` files)
- T038–T039 (Foundry siblings)
- T041–T043 (wrapup siblings)

---

## Parallel Example: User Story 2

```text
Task: Rewrite .agents/skills/place-design/SKILL.md to the Work gate
Task: Rewrite .agents/skills/dungeon-design/SKILL.md to the Work gate
Task: Rewrite .agents/skills/faction-prep/SKILL.md to the Work gate
Task: Rewrite .agents/skills/encounter-prep/SKILL.md to the Work gate
```

Do not parallelize two edits to the same `SKILL.md`.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational
3. Phase 3 US1
4. STOP — quickstart Story 1
5. Demo: DM opens a distilled page in Obsidian

### Incremental Delivery

1. Setup + Foundational
2. US1 → wiki works without the rest of the pack
3. US2 → Co-DM proposes; DM decides
4. US3 → Foundry from accepted Work
5. US4 → wrapup updates the wiki
6. Polish → remaining pack pointers + quickstart

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` tree — skills + `wiki/`
- Do not add test files unless a later command asks
- Commit after each task or logical group
- Stop at checkpoints
