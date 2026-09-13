---

description: "Task list for Complete Ingest Context"
---

# Tasks: Complete Ingest Context

**Input**: Design documents from `/specs/018-complete-ingest-context/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No TDD suite. Spec asks for observable ingest outcomes. Plan names one fixture check as the public seam; that lands in Polish, not as failing tests before each story.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

**Writer**: Edits to `.agents/skills/wiki-ingest/SKILL.md` are design-impact. `/speckit.implement` dispatches the designated writer with a scoped prompt (outcome, files, bounds, job) and `writing-for-agents`. Session agent does not write that file. Fixture and spec-artifact tasks are not design-impact.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Include exact file paths in descriptions

## Path Conventions

- Skill owner: `.agents/skills/wiki-ingest/SKILL.md`
- Contract: `specs/018-complete-ingest-context/contracts/complete-ingest-context.md`
- Do not add a second ingest skill. Do not copy ingest-time search into query-time `AGENTS.md` retrieval.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm existing seams before changing ingest.

- [x] T001 Review the current sequential ingest loop and source-read steps in `.agents/skills/wiki-ingest/SKILL.md`
- [x] T002 [P] Review ingest-time vs query-time rules in `specs/004-qmd-search-default/contracts/retrieval-precedence.md`
- [x] T003 [P] Review the sequential unit in `specs/009-sequential-ingest-quality/contracts/sequential-ingest.md`
- [x] T004 [P] Review destination and canon rules in `specs/015-wiki-ingest-polish/contracts/ingest-quality.md`
- [x] T005 [P] Review the completeness contract in `specs/018-complete-ingest-context/contracts/complete-ingest-context.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Add the shared complete-context pass inside the open primary. Blocks all stories.

**CRITICAL**: No user story work begins until this phase is complete.

- [ ] T006 Add a complete-context pass after the primary is read and before extract/compile in `.agents/skills/wiki-ingest/SKILL.md` without creating a second skill
- [ ] T007 Bound discovery in `.agents/skills/wiki-ingest/SKILL.md` to: "Candidates come from the primary’s content (links, embeds, explicit names) and from the primary’s own subject"; "Each identity is considered at most once per primary"
- [ ] T008 Keep related files as corroboration only in `.agents/skills/wiki-ingest/SKILL.md`: "A related source is not an `open` ingest unit unless it is also a later named primary"; related reads must not open a later named file or attribute wiki/tracking writes to it while the current primary is `open`
- [ ] T009 Point ingest-time search at existing collections in `.agents/skills/wiki-ingest/SKILL.md` without restating 004/009/015; ingest-time corroboration "does not use query-time short-circuit (`wiki` silence before legacy)"

**Checkpoint**: Shared pass, discovery bound, sequential non-overlap, and collection pointer exist.

---

## Phase 3: User Story 1 - A primary ingest is complete only with related evidence (Priority: P1) MVP

**Goal**: A named primary is not `complete` until related discovery has run; misses do not stall; no-related still completes.

**Independent Test**: Ingest one approved primary that names or links two related staging drafts. Both are read before the primary is marked complete. A primary with no related files still completes.

### Implementation for User Story 1

- [ ] T010 [US1] Require in `.agents/skills/wiki-ingest/SKILL.md` that "a primary is not `complete` until related discovery has run, each candidate is `read`, `missed`, or `unreadable`, recency has been applied, and 015 destinations exist for extracted ideas"
- [ ] T011 [US1] Require in `.agents/skills/wiki-ingest/SKILL.md` that "Related misses do not by themselves fail the primary" and "Failure of the primary still requires a reason"
- [ ] T012 [US1] Forbid skipping related search for speed in `.agents/skills/wiki-ingest/SKILL.md`; a primary with no related hits still completes from its own content

**Checkpoint**: Completeness is discovery-plus-primary, not primary-alone.

---

## Phase 4: User Story 2 - Staging and legacy are both searched for corroboration (Priority: P1)

**Goal**: Related evidence is searched in `_raw/` and in legacy collections; a hit in one does not skip the other; legacy is not filed as wiki without accept.

**Independent Test**: Ingest a primary whose subject exists as a staging sibling and as an older legacy note. Both are read. The legacy note is not filed as its own wiki page.

### Implementation for User Story 2

- [ ] T013 [US2] Require staging search of `_raw/` in `.agents/skills/wiki-ingest/SKILL.md` with related origin `staging` and status `unread` → `read` | `missed` | `unreadable`
- [ ] T014 [US2] Require legacy-collection search via the existing `qmd` CLI in `.agents/skills/wiki-ingest/SKILL.md` with origin `legacy`; fetch full sources before relying on a fact; do not answer from snippets
- [ ] T015 [US2] Require in `.agents/skills/wiki-ingest/SKILL.md` that a staging hit does not skip legacy search and a legacy hit does not skip staging search; "no filing a legacy hit as a wiki page without DM accept"

**Checkpoint**: Both places are searched; legacy stays campaign-of-record context.

---

## Phase 5: User Story 3 - Newest files win decisions; older files still inform (Priority: P1)

**Goal**: Newest corroborating sources are latest decisions; older variants supply uncontradicted support; compiled wiki stays canon on conflict.

**Independent Test**: Newest primary changes one decision and omits color that exists only in an older variant. The page uses the new decision and keeps the uncontradicted older color. A contradicting older wording is a proposal, not an overwrite.

### Implementation for User Story 3

- [ ] T016 [US3] Rank the primary plus related sources in `.agents/skills/wiki-ingest/SKILL.md` so newest files are latest decisions; recency "defaults to which file is newer" unless "the content itself dates a decision more clearly"
- [ ] T017 [US3] Require in `.agents/skills/wiki-ingest/SKILL.md` that "Uncontradicted older detail remains available as supporting context" and "an older source must not silently replace a newer decision"; surface that conflict as a proposal or explicit unresolved item
- [ ] T018 [US3] Require in `.agents/skills/wiki-ingest/SKILL.md` "no silent overwrite of compiled wiki canon"; named ingest of an approved primary still follows 015 for compiling that primary

**Checkpoint**: Recency ranks sources; wiki canon and older support both hold.

---

## Phase 6: User Story 4 - The DM can see what was read for completeness (Priority: P2)

**Goal**: The ingest record names primary, related reads, origin, misses, empty search, and recency conflicts.

**Independent Test**: Run an ingest with one primary, one staging relative, one legacy variant, and one missing named link. The record lists all four outcomes in under one minute.

### Implementation for User Story 4

- [ ] T019 [US4] Extend the per-file ingest record in `.agents/skills/wiki-ingest/SKILL.md` to list the primary and each related read with identity, origin (`staging` | `legacy`), and role
- [ ] T020 [US4] Require misses (named related identity not found or not readable, with reason) in that record in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T021 [US4] Require recency conflicts in that record in `.agents/skills/wiki-ingest/SKILL.md`; "A “no related hits” search is still recorded, not omitted"

**Checkpoint**: Completeness is visible from the ingest record alone.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Public-seam check and artifact alignment after the skill change.

- [ ] T022 [P] Align final workflow language in `specs/018-complete-ingest-context/contracts/complete-ingest-context.md`
- [ ] T023 [P] Align expected outcomes in `specs/018-complete-ingest-context/quickstart.md`
- [ ] T024 Add the runnable fixture check at `specs/018-complete-ingest-context/fixtures/check.py` covering quickstart scenarios 1–6 (related reads, recency, misses, sequential non-overlap, ingest record). Assert page and record outcomes; do not snapshot skill wording
- [ ] T025 Run every scenario in `specs/018-complete-ingest-context/quickstart.md` via `.venv/bin/python specs/018-complete-ingest-context/fixtures/check.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup; blocks all user stories.
- **User Story 1 (Phase 3)**: Depends on Foundational; MVP.
- **User Story 2 (Phase 4)**: Depends on Foundational; independently testable after the shared pass exists.
- **User Story 3 (Phase 5)**: Depends on Foundational; independently testable after the shared pass exists.
- **User Story 4 (Phase 6)**: Depends on Foundational; independently testable after the shared pass exists.
- **Polish (Phase 7)**: Depends on the desired user stories being complete.

### User Story Dependencies

- **US1**: No dependency on another story after Foundational.
- **US2**: No dependency on another story after Foundational; shares the complete-context pass.
- **US3**: No dependency on another story after Foundational; shares recency on the related set US1/US2 populate.
- **US4**: No dependency on another story after Foundational; shares the ingest record.

### Parallel Opportunities

- T002–T005 can run in parallel.
- T022 and T023 can run in parallel after implementation.
- T006–T021 all edit `.agents/skills/wiki-ingest/SKILL.md` — sequential, one writer. Do not parallelize those.
- US1–US4 can proceed in parallel after Phase 2 only if edits are coordinated; otherwise implement sequentially to avoid same-file conflicts.

### Parallel Example: Setup

```text
T002 Review specs/004-qmd-search-default/contracts/retrieval-precedence.md
T003 Review specs/009-sequential-ingest-quality/contracts/sequential-ingest.md
T004 Review specs/015-wiki-ingest-polish/contracts/ingest-quality.md
T005 Review specs/018-complete-ingest-context/contracts/complete-ingest-context.md
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational.
2. Complete US1 completeness-before-close.
3. Run the US1 independent test from quickstart scenario 1 (and 5 if no-related is in the fixture).
4. Proceed to US2 (both search places) before calling ingest complete in production.

### Incremental Delivery

1. Complete-context pass + discovery bound (Foundational).
2. Primary not complete without related reads (US1).
3. Staging and legacy both searched (US2).
4. Recency and supporting context (US3).
5. Ingest record (US4).
6. Fixture check and contract/quickstart alignment.

### Dispatch

Skill tasks T006–T021: designated writer only. Fixture T024 and artifact T022/T023: session agent.

---

## Notes

- Every task follows the checklist format with a sequential ID and exact file path.
- `[P]` appears only where tasks use different files and have no incomplete dependencies.
- Data-model constraints are quoted in T007, T008, T010, T011, T013, T015, T016, T017, T018, T019, T021.
- No new runtime module, collection, or query-time precedence rewrite.
