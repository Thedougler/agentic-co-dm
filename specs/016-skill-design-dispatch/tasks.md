---
description: "Task list for Skill Design Dispatch"
---
# Tasks: Skill Design Dispatch

**Input**: Design documents from `/specs/016-skill-design-dispatch/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/016-skill-design-dispatch/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → US5 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US5 only on story phases
- Every task names an exact path

## Path Conventions

Standing: `AGENTS.md`  
Procedure: `docs/agents/skill-design-dispatch.md`  
Skills: `.agents/skills/skill-creator/SKILL.md`, `.agents/skills/omp-harness/SKILL.md`  
Contract: `specs/016-skill-design-dispatch/contracts/skill-design-dispatch.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No new skill, wrapper CLI, or `src/`.

- [X] T001 Confirm the files listed under Source Code in `specs/016-skill-design-dispatch/plan.md` exist or will be created as listed; do not add a skill, wrapper script, `src/`, scanner, or a second copy of the gate in `.omp/AGENTS.md` or `.claude/CLAUDE.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One always-loaded design-impact gate. Procedure and skills will point here.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [X] T002 Add the design-impact gate to `AGENTS.md` from `specs/016-skill-design-dispatch/contracts/skill-design-dispatch.md`. Quote: Class is `design-impact` \| `not`; Design-impact if the change would alter skill triggering, workflow ownership, standing load, or would create a skill or subagent; Length does not decide; Borderline of those four is design-impact; Writer is designated writer if design-impact (unless owner overrule), else session agent; Overrule is explicit owner skip only, silence is not overrule. Name in-scope kinds (source skill, standing instruction/sticky rule, subagent definition, writing-for-agents) and out-of-scope (constitution, feature specs, generated Spec Kit adapters, campaign wiki). Point design-impact work at `docs/agents/skill-design-dispatch.md`. Do not duplicate the gate in `.omp/AGENTS.md` or `.claude/CLAUDE.md`. Do not prescribe how the designated writer designs.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Classify design-impact before writing (Priority: P1) 🎯 MVP

**Goal**: Before an in-scope file changes, the session agent has classified the edit.

**Independent Test**: Two reviewers classify contract jobs 1–12 without seeing each other and agree with the checklist on every item. Length is not the gate.

### Implementation for User Story 1

- [X] T003 [US1] In `AGENTS.md`, state classify before any in-scope instruction file changes. Quote: "Length MUST NOT be the gate"; "Borderline of those four bullets MUST be treated as design-impact"; "Creating a new skill or subagent MUST be classified as design-impact".

**Checkpoint**: US1 independently testable (quickstart step 1)

---

## Phase 4: User Story 2 - Non-design edits stay with the session agent (Priority: P2)

**Goal**: Typos, paths, values, and clarifying sentences are done in-session. They do not park and do not wait for the designated writer.

**Independent Test**: An in-scope typo or path fix is corrected in that session. No `Parked skill design:` issue exists for it.

### Implementation for User Story 2

- [X] T004 [US2] Create `docs/agents/skill-design-dispatch.md` with the non-design path: if class is `not`, the session agent completes the edit in the same session; do not park. Quote: mixed request MUST be split — non-design work by the session agent, design-impact work dispatched or parked. Do not copy the four bullets (they live in `AGENTS.md`).

**Checkpoint**: US1 + US2 independently testable (quickstart step 2)

---

## Phase 5: User Story 3 - Design-impact work is dispatched (Priority: P3)

**Goal**: Session agent does not write design-impact targets. Scoped prompt + designated writer. Routing fires even when skill-creator was not loaded.

**Independent Test**: A trigger rewrite or new skill: session agent does not modify those targets. A scoped prompt exists, or the job is parked.

### Implementation for User Story 3

- [X] T005 [US3] In `docs/agents/skill-design-dispatch.md`, add the design-impact path. Scoped prompt fields: Outcome (what must be true when done); Files (in-scope targets); Bounds (what must not change); Job (one design job, not an unbounded rewrite). Session agent MUST NOT modify the target instruction files. Invoke designated writer with `claude -p --model opus --effort high` (flags from `claude --help`, do not pin a version string). Designated writer is the sole writer of a change that lands. Do not prescribe skill-design method, voice, or structure; tell the writer to follow writing-for-agents.

**Checkpoint**: US1–US3 independently testable (quickstart step 3)

---

## Phase 6: User Story 4 - Unavailability parks work and leaves files untouched (Priority: P4)

**Goal**: Writer cannot start, stops, refuses, or errors → targets match dispatch-start content; scoped prompt is a GitHub issue a later session can find. Usage limit → that job incomplete with a retry time; do not retry before it.

**Independent Test**: Simulate writer unavailable. Targets unchanged. Issue titled `Parked skill design: …` with `ready-for-agent` contains the scoped prompt. Simulate jobs 17–19: parked issue includes retry time; job is not re-attempted before that time; other in-session work is not marked incomplete.

### Implementation for User Story 4

- [X] T006 [US4] In `docs/agents/skill-design-dispatch.md`, add unavailability. Commit non-design work first; record `HEAD` as dispatch start. On non-success restore the prompt’s target paths to that revision. Park with `gh issue create`: Title `Parked skill design: <outcome>`; Label `ready-for-agent`; Body the scoped prompt. When reason is usage limit, Body also includes the retry time. Quote: Retry time is usage limit only; Reset time from the report when present; if none, 5 hours from the park; if a retry still reports a usage limit with no reset time, 24 hours from that attempt; Do not re-attempt before this time; Other in-session jobs are not marked incomplete for this reason. Search existing `Parked skill design:` issues before creating another for the same job. Session agent MUST NOT write the design-impact change. States: `open` → `resumed` → `done`. Resume of a usage-limit park waits until after retry time.

**Checkpoint**: US1–US4 independently testable (quickstart step 4)

---

## Phase 7: User Story 5 - Session agent verifies, it does not rewrite (Priority: P5)

**Goal**: After a successful designated-writer run, session agent checks scope and outcome, then stops.

**Independent Test**: After successful dispatch, the session agent did not rewrite those files for the same change. A scope check was reported.

### Implementation for User Story 5

- [X] T007 [US5] In `docs/agents/skill-design-dispatch.md`, add verify-and-stop. After success the session agent reports whether touched files were in-scope and whether the prompt outcome was met, and MUST NOT rewrite those files for the same change. Owner overrule remains the only license for the session agent to write design-impact (already in `AGENTS.md`).

**Checkpoint**: All five stories independently testable (quickstart step 5)

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Conflicting “you draft it” paths gone. One source of truth. Quickstart holds.

- [X] T008 [P] In `.agents/skills/skill-creator/SKILL.md`, stop instructing the session agent to draft design-impact skill work; point at `docs/agents/skill-design-dispatch.md`. Do not copy the four bullets.
- [X] T009 [P] In `.agents/skills/omp-harness/SKILL.md`, stop instructing the session agent to draft design-impact omp context, skills, or subagent defs; point at `docs/agents/skill-design-dispatch.md`. Do not copy the four bullets.
- [X] T010 Run `specs/016-skill-design-dispatch/quickstart.md` steps 1–6 against `specs/016-skill-design-dispatch/contracts/skill-design-dispatch.md`
- [X] T011 Confirm `.omp/AGENTS.md` and `.claude/CLAUDE.md` still only import `AGENTS.md`; this change set adds no skill, no wrapper CLI, and no `src/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; procedure file created here; US3–US5 edit that file after
- **US3–US5 (Phases 5–7)**: After US2 (same procedure file — sequential)
- **Polish (Phase 8)**: After desired stories; T008/T009 independent of each other

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After Phase 2; creates the procedure file
- **US3–US5**: After US2; same file `docs/agents/skill-design-dispatch.md` — do not parallelize

### Parallel Opportunities

- T008, T009 (skill-creator and omp-harness)
- Do not parallelize T002/T003 (`AGENTS.md`)
- Do not parallelize T004–T007 (same procedure file)

---

## Parallel Example: Polish

```text
Task: pointer in .agents/skills/skill-creator/SKILL.md (T008)
Task: pointer in .agents/skills/omp-harness/SKILL.md (T009)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 `AGENTS.md` gate
3. Phase 3 US1 (classify-before-write)
4. STOP — classify contract jobs 1–12
5. Demo: table in `AGENTS.md`; length is not the gate

### Incremental Delivery

1. Setup + Foundational
2. US1 → classification is the default
3. US2 → non-design stays local
4. US3 → dispatch
5. US4 → park and restore
6. US5 → verify, no rewrite
7. Polish → skill pointers; quickstart 1–6

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — `AGENTS.md` + one procedure + two skill pointers
- Do not add test files unless a later command asks
- Do not add a dispatch skill or a wrapper around `claude`/`gh`
- Do not prescribe how the designated writer designs
- Commit after each task or logical group
- Stop at checkpoints
