---
description: "Task list for Audience Writing and Visual Skills"
---
# Tasks: Audience Writing and Visual Skills

**Input**: Design documents from `/specs/010-audience-writing-skills/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/010-audience-writing-skills/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US5 → US6 → US7 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US7 only on story phases
- Every task names an exact path

## Path Conventions

Standing: `AGENTS.md`, `docs/agents/work.md`, `wiki/AGENTS.md`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/010-audience-writing-skills/contracts/writing-authorities.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, linter, or `src/`.

- [X] T001 Confirm the files listed under Source Code in `specs/010-audience-writing-skills/plan.md` exist; do not add a skill, `docs/agents/writing.md`, scanner, or rewrite of `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One always-loaded stack table. Skills and work-gates will point here.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Add the six-row stack table to `AGENTS.md` from `specs/010-audience-writing-skills/contracts/writing-authorities.md`. Rows: agent follows text → writing-for-agents; DM reads text → copy-writer; players hear or see text → theatre of the mind; wiki vault note → obsidian-markdown; working with visual references → visual-references; producing a visual aid → visual-aids. State they stack and do not cancel. Quote: Reader is `agent` \| `DM` \| `players`; Unknown reader → `DM`; Vault is `true` if the destination is a wiki vault note else `false`; Authorities are every matching row and incomplete until all are applied. Do not duplicate the table in `.omp/AGENTS.md`. Do not prescribe voice, camera, or method.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - The job decides the writing or visual authority (Priority: P1) 🎯 MVP

**Goal**: Co-DM standing docs point at the stack table instead of hardcoding copy-writer plus obsidian-markdown.

**Independent Test**: Present six jobs (agent instruction, DM Work, player-facing spoken text, wiki vault note, gathering look, producing a visual aid). A second author names the same authorities from `AGENTS.md` without seeing the first list.

### Implementation for User Story 1

- [X] T003 [P] [US1] Replace the hardcoded "Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown` on every vault write" line in `docs/agents/work.md` with a pointer at the stack table in `AGENTS.md`. Keep the Work accept-gate. Quote: Unknown reader → `DM`; Vault `false` until filed as a wiki vault note.
- [X] T004 [P] [US1] Replace "Load `copy-writer` and `obsidian-markdown` on every `.md` write" in `wiki/AGENTS.md` with a pointer at the stack table in `AGENTS.md`. Keep complete-sentence human prose and spoken player text as theatre of the mind. Quote: Vault `true` on wiki vault notes; mixed document classifies per passage then applies vault format to the whole note.

**Checkpoint**: US1 independently testable (quickstart steps 1, 5)

---

## Phase 4: User Story 2 - Agent-consumed text follows writing-for-agents (Priority: P2)

**Goal**: The writing-for-agents description fires on any document an agent will follow, not only skills and `AGENTS.md` / `CLAUDE.md`.

**Independent Test**: Give an author a job whose only reader is an agent. Result follows writing-for-agents and is not scored as wiki copy or theatre of the mind.

### Implementation for User Story 2

- [X] T005 [P] [US2] Rewrite the `description` in `.agents/skills/writing-for-agents/SKILL.md` so the trigger is text an agent will follow (skill, standing instruction, pointed-at procedure, spec, constitution). Quote: Reader `agent` → writing-for-agents; writing-for-agents does not own DM Work, wiki prose, or player-facing text. Leave the body craft unless a sentence claims copy-writer or theatre of the mind.

**Checkpoint**: US1 + US2 independently testable

---

## Phase 5: User Story 3 - DM-consumed text follows copy-writer (Priority: P3)

**Goal**: The copy-writer description fires on DM-consumed Co-DM output, including chat Work not yet filed. It does not own player-facing passages or agent-consumed docs.

**Independent Test**: Give an author DM-facing Work with no player-facing passage. Result is complete-sentence human prose; vault format is not required until filed.

### Implementation for User Story 3

- [X] T006 [P] [US3] Rewrite the `description` in `.agents/skills/copy-writer/SKILL.md` so the trigger is prose the DM will read (Work, wiki, chat proposals). Remove "mandatory on every wiki write" and ownership of `[!narration]` / TotM. Quote: Reader `DM` → copy-writer; copy-writer does not own agent-consumed documents or player-facing passages; Unknown reader → `DM`. Leave body craft except sentences that claim theatre of the mind as copy-writer's job.

**Checkpoint**: US1–US3 independently testable

---

## Phase 6: User Story 4 - Player-facing text follows theatre of the mind (Priority: P4)

**Goal**: The theatre-of-the-mind description is the trigger for text that crosses the DM/player boundary.

**Independent Test**: Give an author a spoken-look job. A second person can read it aloud without a secret, difficulty class, unearned name, or process note.

### Implementation for User Story 4

- [X] T007 [P] [US4] Audit the `description` in `.agents/skills/theatre-of-the-mind/SKILL.md`. Keep or sharpen the trigger as text players will hear or see (spoken look, boxed read-aloud, diegetic handout, player-safe rendered text). Quote: Reader `players` → theatre of the mind; theatre of the mind does not own DM procedure, hidden truth, or agent instruction. Leave body craft. Do not edit the work-gate load line here (T011).

**Checkpoint**: US1–US4 independently testable

---

## Phase 7: User Story 5 - Wiki vault notes follow obsidian-markdown (Priority: P5)

**Goal**: The obsidian-markdown description is format for wiki vault notes only. Reader still decides prose.

**Independent Test**: File a new wiki vault note with DM-facing text and spoken look. Format matches the vault; DM bands and spoken bands still use their own prose authorities. Non-vault writing does not require it.

### Implementation for User Story 5

- [X] T008 [P] [US5] Audit the `description` in `.agents/skills/obsidian-markdown/SKILL.md`. Keep or sharpen the trigger as format for wiki vault notes. Quote: Vault `true` → obsidian-markdown; obsidian-markdown is not required for writing that is not a wiki vault note; skill files and repository docs are not wiki vault notes. Leave body craft.

**Checkpoint**: US1–US5 independently testable

---

## Phase 8: User Story 6 - Working with visual references uses visual-references (Priority: P6)

**Goal**: visual-references is the gather/use-look job. It does not place finished art.

**Independent Test**: Give an author a depiction job for a named owner who already has a look. The author uses that look before any new picture is made, and does not treat placing the finished picture as this job.

### Implementation for User Story 6

- [X] T009 [P] [US6] Audit the `description` in `.agents/skills/visual-references/SKILL.md`. Keep or sharpen the trigger as gathering and using an owner's existing look before depicting them. Quote: Kind `visual-references`; visual-references does not own placing finished art; Missing look → stop; do not invent a face. Leave body craft. Do not edit the work-gate load line here (T011).

**Checkpoint**: US1–US6 independently testable

---

## Phase 9: User Story 7 - Producing visual aids uses visual-aids (Priority: P7)

**Goal**: visual-aids produces or places. It does not replace visual-references when a known owner is depicted. Spoken look stays theatre of the mind.

**Independent Test**: Place or mint a picture for a named owner with an existing look. Result is a visual aid for that owner or moment, not a reused picture of someone else; spoken look is still theatre of the mind.

### Implementation for User Story 7

- [X] T010 [P] [US7] Audit the `description` in `.agents/skills/visual-aids/SKILL.md`. Keep or sharpen the trigger as attaching, grounding, generating, promoting, or placing a visual aid. Quote: Kind `visual-aids`; visual-aids does not gather references in place of visual-references when a known owner is depicted; does not own map rendering or spoken narration; Reference image is durable identity; Illustration is session-scoped and not identity. Leave body craft. Do not edit the work-gate load line here (T011).

**Checkpoint**: All seven stories independently testable

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: One source of truth. No restated load trio. No legacy rewrite.

- [X] T011 Remove the restated "Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown`" vault-write line from these files (keep "Follow `docs/agents/work.md`"): `.agents/skills/campaign-planning/SKILL.md`, `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/dnd-5e-magic-item-design/SKILL.md`, `.agents/skills/dnd5e-mechanics/SKILL.md`, `.agents/skills/dungeon-design/SKILL.md`, `.agents/skills/encounter-prep/SKILL.md`, `.agents/skills/faction-prep/SKILL.md`, `.agents/skills/homebrew-monsters-5e/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, `.agents/skills/npc-design/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/place-design/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/run-guide/SKILL.md`, `.agents/skills/sandbox-narrative/SKILL.md`, `.agents/skills/session-beats/SKILL.md`, `.agents/skills/session-recap/SKILL.md`, `.agents/skills/session-wrapup/SKILL.md`, `.agents/skills/theatre-of-the-mind/SKILL.md`, `.agents/skills/traps-trials/SKILL.md`, `.agents/skills/travel-events/SKILL.md`, `.agents/skills/vehicle-design/SKILL.md`, `.agents/skills/visual-aids/SKILL.md`, `.agents/skills/visual-references/SKILL.md`, `.agents/skills/world-tick/SKILL.md`, `.agents/skills/writing-beats/SKILL.md`
- [X] T012 Run `specs/010-audience-writing-skills/quickstart.md` steps 1–6 against `specs/010-audience-writing-skills/contracts/writing-authorities.md`
- [X] T013 Confirm the change set has 0 files under `legacy/` and no historical wiki page restyled solely to match routing (SC-007)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2–US7 (Phases 4–9)**: After Foundational; parallel with each other (different files)
- **Polish (Phase 10)**: After desired stories; T011 after T007, T009, T010 (same three skill files)

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2–US7**: After Phase 2; independent of other stories

### Parallel Opportunities

- T003, T004 (work.md and wiki/AGENTS.md)
- T005, T006, T007, T008, T009, T010 (six skill descriptions)
- After Phase 2, US1–US7 can run in parallel if staffed
- Do not parallelize two edits to the same file
- T011 is one pass over 26 files after description audits on theatre-of-the-mind, visual-references, and visual-aids

---

## Parallel Example: User Story 1

```text
Task: pointer in docs/agents/work.md (T003)
Task: pointer in wiki/AGENTS.md (T004)
```

---

## Parallel Example: User Stories 2–7

```text
Task: writing-for-agents description in .agents/skills/writing-for-agents/SKILL.md (T005)
Task: copy-writer description in .agents/skills/copy-writer/SKILL.md (T006)
Task: theatre-of-the-mind description in .agents/skills/theatre-of-the-mind/SKILL.md (T007)
Task: obsidian-markdown description in .agents/skills/obsidian-markdown/SKILL.md (T008)
Task: visual-references description in .agents/skills/visual-references/SKILL.md (T009)
Task: visual-aids description in .agents/skills/visual-aids/SKILL.md (T010)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `AGENTS.md` stack table
3. Phase 3 US1 (`docs/agents/work.md`, `wiki/AGENTS.md`)
4. STOP — classify the six jobs in US1 Independent Test
5. Demo: table in `AGENTS.md`; no hardcoded copy-writer + obsidian-markdown pair in work.md / wiki/AGENTS.md

### Incremental Delivery

1. Setup + Foundational
2. US1 → stack table is the default
3. US2 → agent docs
4. US3 → DM prose
5. US4 → player-facing
6. US5 → vault format
7. US6 → visual references
8. US7 → visual aids
9. Polish → delete restated load lines; quickstart 1–6

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — AGENTS.md + existing skills
- Do not add test files unless a later command asks
- Do not rewrite wiki pages or `legacy/` in this feature
- Do not add a seventh skill
- Commit after each task or logical group
- Stop at checkpoints
