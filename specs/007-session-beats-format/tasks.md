---
description: "Task list for Session Beat Format"
---
# Tasks: Session Beat Format

**Input**: Design documents from `/specs/007-session-beats-format/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/007-session-beats-format/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US4 → US3 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US4 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contracts: `specs/007-session-beats-format/contracts/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, scanner, or `_raw/` rewrite.

- [X] T001 Confirm the files listed under Source Code in `specs/007-session-beats-format/plan.md` exist; do not add a skill, linter, `src/`, or rewrite of `wiki/_raw/Session-11-*.md` or `wiki/journal/Session 0N - Recap.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Closed type set includes `session-prep`. Session home path is stated once in `wiki/AGENTS.md`.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 In `wiki/AGENTS.md` add `session-prep` to the campaign `type` closed set (do not map it to `session`; `session` remains the post-play log). State the session folder home: path `wiki/journal/sessions/<campaign-slug>/<session-number>/`; Session 11 files to `wiki/journal/sessions/shattered-sea/11/`; folder contains the spine, numbered live beat cards, and that night’s companion notes only; MUST NOT hold owner pages; `_raw/` is staging not the long-term home; two campaigns MUST NOT share one session-number folder. Point beat cockpit at `.agents/skills/run-guide/SKILL.md` and filed spine at `.agents/skills/session-beats/SKILL.md`. Do not paste the run-guide column table here.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - New beats match the Session 11 cockpit (Priority: P1) 🎯 MVP

**Goal**: New live beats use Session 11 job order, markdown shape, and quality. Empty jobs omitted.

**Independent Test**: Hand a newly composed live beat (not copied from a Session 11 filename) to a second DM. They timebox, speak the opening, place the party, roll default-mode numbers, and name the next state from that page alone, and judge it the same kind of card as a Session 11 beat.

### Implementation for User Story 1

- [X] T003 [P] [US1] Update `.agents/skills/run-guide/SKILL.md`: Session 11 job order is required per `specs/007-session-beats-format/contracts/beat-card.md` (identity; optional first-beat recap; overview art if it exists; Scene ends when + At a Glance; Now; Action cards; Initial Narration; Procedure + Secondary objective if a second question exists; Zones; Be ready for; Threat clock + dials if a fuse exists; How the Scene Resolves; Roster if combat-mode sheets will be rolled; Backup; Battlemap at bottom if art exists). Omit a section only when that job is absent — no empty heading. Evidence files `wiki/_raw/Session-11-01-Angry-Birds.md` through `wiki/_raw/Session-11-10-Aftermath.md` illustrate quality; MUST NOT photocopy a named Session 11 title. At a Glance MUST scan as stakes, goal or exit, danger, silence, situation magnets. Scene ends when MUST state the stop condition, a roughly thirty-minute budget, and behind/ahead cuts when pacing is not obvious. Only the first beat may recap. How the Scene Resolves hands to a beat on this session’s skeleton. Filename `Session-<number>-<beat-number>-<Label>` with two-digit beat numbers (`01`, `02`, …) matching skeleton position. Spoken: open `[!narration]` only; highlighted italic conditional cells; no secrets, DCs, unearned names. Default-mode action-card numbers MAY sit on the beat; MUST NOT become a second full owner page.
- [X] T004 [P] [US1] Create `wiki/templates/session-prep.md` as an omit-if-empty copy-start scaffold of that cockpit spine (frontmatter `type: session-prep`, `campaign` required, `session` integer matching folder, `visibility` default `dm`, `summary` one sentence). `wiki/templates/session.md` stays the post-play log. Do not treat the heading list as pass/fail when a job is absent.

**Checkpoint**: US1 independently testable (quickstart steps 1, 5, 7)

---

## Phase 4: User Story 2 - Ingest keeps the beat shape (Priority: P1)

**Goal**: Ingest/promote files session-prep; it does not distill beats into concept pages.

**Independent Test**: Ingest one complete Session 11 beat card and one newly composed beat. Open both wiki pages in Reading view. Layout jobs and markdown treatments still match the source files.

### Implementation for User Story 2

- [X] T005 [US2] Update `.agents/skills/wiki-ingest/SKILL.md` with a preserve-and-file branch per `specs/007-session-beats-format/contracts/ingest-preserve.md`: if the source is `type: session-prep` (beat or spine) or a Session-N file in that shape, copy body markdown treatments unchanged (heading spine, column pairs, tables, `[!narration]`, highlighted narration cells, wikilinks, image embeds) into `wiki/journal/sessions/<campaign-slug>/<session-number>/`; keep filename `Session-<number>-00-<Spine-Title>` or `Session-<number>-<beat-number>-<Label>`; MUST NOT compile into `concepts/` or `entities/`; MUST NOT flatten columns or tables or rewrite callouts; mixed batch still distills ordinary knowledge sources; companion notes for that night file into the same folder and MUST NOT use a live beat number; re-ingest with no body change MUST NOT rewrite the cockpit; unaccepted Work does not publish except named ingest of approved sources; leave `wiki/_raw/Session-11-*.md` as evidence and file copies into the session folder rather than restyling the evidence set. Early-dev sample pages that are not session-prep stay in `_raw/` per existing ingest rules.

**Checkpoint**: US2 independently testable (quickstart step 3)

---

## Phase 5: User Story 4 - One folder is the session home (Priority: P1)

**Goal**: The DM opens one session folder, not a `_raw/` dump. Wrapup does not mint a second tree.

**Independent Test**: Point a second DM at `wiki/journal/sessions/shattered-sea/11/`. They open the spine, then beat 1 through the last beat, in order, without searching the vault root or `_raw/`.

### Implementation for User Story 4

- [X] T006 [US4] Update `.agents/skills/session-wrapup/SKILL.md`: durable session path is `wiki/journal/sessions/<campaign-slug>/<session-number>/` (same home as prep). A session log MAY join that folder and MUST NOT replace the spine or beat cards. MUST NOT create `wiki/<slug>/sessions/` or `campaigns/` as a second root. Attachments stay under `wiki/attachments/`. Owner pages stay outside the session folder.

**Checkpoint**: US4 independently testable (quickstart step 4)

---

## Phase 6: User Story 3 - The session spine stays the chart (Priority: P2)

**Goal**: Filed spine matches Session 11-00 jobs. It is not a tenth cockpit.

**Independent Test**: A second DM names tonight's Hook, the beat order, and where to start from the spine alone, then opens beat 1 and runs from that card.

### Implementation for User Story 3

- [X] T007 [P] [US3] Update `.agents/skills/session-beats/SKILL.md`: the filed spine follows `specs/007-session-beats-format/contracts/session-spine.md` (filename `Session-<number>-00-<Spine-Title>`; jobs: length, tone, prize, opposition, Hook/Climax/Resolution labels, dramatic spine, numbered skeleton with links to each live beat, per-beat purpose / table sees / truth / pressure / if they break / landing). Evidence `wiki/_raw/Session-11-00-Birds-of-a-Feather.md`. Spine MUST NOT duplicate Scene ends when, Zones, or Be ready for. New live beats are composed via `run-guide` in Session 11 cockpit shape. Do not paste the run-guide column table.
- [X] T008 [P] [US3] Update `.agents/skills/session-beats/references/session-skeleton.md`: keep it as the planning form (candidate pools). State that the filed spine the DM opens is the Session 11-00 shape, not this skeleton copied into the wiki.

**Checkpoint**: US3 independently testable (quickstart step 2)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Prove the format without touching older sessions or gold evidence bodies.

- [X] T009 Run `specs/007-session-beats-format/quickstart.md` steps 1–7 except the actual Session 11 ingest if the DM has not approved filing; then confirm agent-path pointers in `wiki/AGENTS.md`, `.agents/skills/run-guide/SKILL.md`, and `.agents/skills/wiki-ingest/SKILL.md`
- [X] T010 Confirm the change set does not rewrite bodies of `wiki/_raw/Session-11-*.md` or restyle `wiki/journal/Session 0N - Recap.md` solely to match the cockpit (FR-013, SC-006)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; uses the folder path from T002
- **US4 (Phase 5)**: After Foundational; ingest destination already in T005
- **US3 (Phase 6)**: After Foundational; parallel with US1/US2/US4 (different files)
- **Polish (Phase 7)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2; T003 and T004 parallel
- **US2 (P1)**: After Phase 2; T005 alone on `wiki-ingest`
- **US4 (P1)**: After Phase 2; T006 alone on `session-wrapup`; folder home already in T002+T005
- **US3 (P2)**: After Phase 2; T007 and T008 parallel

### Parallel Opportunities

- T003, T004 (run-guide + template)
- T007, T008 (session-beats skill + skeleton)
- After Phase 2, US1 / US2 / US4 / US3 can run in parallel (four different files)
- Do not parallelize two edits to the same file

---

## Parallel Example: User Story 1

```text
Task: run-guide Session 11 job order in .agents/skills/run-guide/SKILL.md (T003)
Task: session-prep omit-if-empty scaffold in wiki/templates/session-prep.md (T004)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `wiki/AGENTS.md` type + folder path
3. Phase 3 US1 (`run-guide` + `wiki/templates/session-prep.md`)
4. STOP — compose one new beat; quickstart steps 1, 5, 7
5. Demo: side-by-side with Session 11-01

### Incremental Delivery

1. Setup + Foundational
2. US1 → compose in cockpit
3. US2 → ingest preserve + file to session folder
4. US4 → wrapup shares that folder
5. US3 → filed spine
6. Polish → quickstart 1–7; no `_raw/` or recap rewrite

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — AGENTS.md + one template + existing skills
- Do not add test files unless a later command asks
- Do not rewrite `_raw/` Session 11 bodies or older recaps
- Commit after each task or logical group
- Stop at checkpoints
