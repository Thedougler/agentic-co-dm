---
description: "Task list for Blind Cold Evaluation of D&D Content"
---
# Tasks: Blind Cold Evaluation of D&D Content

**Input**: Design documents from `/specs/012-blind-content-eval/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/012-blind-content-eval/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US4 only on story phases
- Every task names an exact path

## Path Conventions

Skills: `.agents/skills/<name>/SKILL.md`  
Contract: `specs/012-blind-content-eval/contracts/blind-content-eval.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Stay inside the plan file list. No pytest. No 010 table row.

- [ ] T001 Confirm `.agents/skills/writing-for-agents/SKILL.md` exists; do not add pytest, a runner script, a research/eval row on the `AGENTS.md` stack table, `docs/agents/eval.md`, or a rewrite of `legacy/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Evaluator job exists. Contamination rules bind before axes.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [ ] T002 Create `.agents/skills/blind-content-eval/SKILL.md` with the eval job identity. Quote: Sample is the judged object, not the skill file. Evaluator did not produce the sample. Does not see authoring session, skill diff, or author notes. Verdict is `pass` \| `fail` per applicable axis, then overall. Fail any applicable axis → overall fail. Inapplicable axes omitted, not failed. At least two independent eval jobs; incomplete while they disagree. Automatic file-shape checks are not an eval job. Do not write canon. Do not restate copy-writer or TotM.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Blind cold evaluation is the test (Priority: P1) 🎯 MVP

**Goal**: A D&D content-guidance change is not done until two independent cold evals of sample content pass. File-shape checking alone cannot pass. Author self-review is not this test.

**Independent Test**: Produce sample content from changed guidance. Give it to a second evaluator with no authoring transcript. They can pass or fail it. A file-shape check alone does not treat the change as done.

### Implementation for User Story 1

- [ ] T003 [US1] Write the `description` in `.agents/skills/blind-content-eval/SKILL.md` so it fires on judging sample D&D content cold. Quote: Produces D&D content `true` → this eval is required; `false` → not this feature. Evaluator who saw the authoring session is void. Author judging their own sample is not this test. After T002. Same file — not parallel with T002.
- [ ] T004 [P] [US1] Add a done-gate step to the D&D content guidance section in `.agents/skills/writing-for-agents/SKILL.md`. Quote: Done: two independent cold evaluations of sample content produced from this guidance have passed (`blind-content-eval`). Those evaluators do not see this session. File-shape checking alone is not done. Do not turn `writing-for-agents` into the judge.

**Checkpoint**: US1 independently testable (quickstart steps 1, 6)

---

## Phase 4: User Story 2 - Form is correct and used appropriately (Priority: P2)

**Goal**: Cold eval covers form (layout, format, shape, mechanics) and appropriate use. Decorative or swapped treatments fail. Heading-order match of an unusable page fails.

**Independent Test**: Give an evaluator a sample page and the kind it claims. They can say whether form matches that kind and is used for those jobs — without the author's intent.

### Implementation for User Story 2

- [ ] T005 [US2] Add Form and Appropriate use axes to `.agents/skills/blind-content-eval/SKILL.md`. Quote: Form applies when the sample claims a kind — pass if layout, format, shape, mechanics match that kind; fail if wrong kind-shape. Appropriate use applies when form treatments are present — pass if treatments mean the jobs they mean; fail if decorative or swapped use. Load `obsidian-markdown` and `wiki/AGENTS.md` Layout; do not copy those rubrics. Spoken-only handout: do not fail missing mechanics. After T003. Same file.

**Checkpoint**: US1 + US2 independently testable

---

## Phase 5: User Story 3 - DM copy is a table-ready reference (Priority: P3)

**Goal**: DM-facing bands are complete-sentence table reference. Telegram, slash-stacks, and agent-speak fail. No DM band: omit the axis.

**Independent Test**: Give an evaluator only the DM-facing bands. They can use them as a reference without decoding agent shorthand.

### Implementation for User Story 3

- [ ] T006 [US3] Add the DM copy axis to `.agents/skills/blind-content-eval/SKILL.md`. Quote: Applies when DM-facing bands exist. Pass: complete-sentence table reference. Fail: telegram, slash-stacks, agent-speak, novel-padding. Load `copy-writer`; do not restate it. No DM band: omit, not fail. After T005. Same file.

**Checkpoint**: US1–US3 independently testable

---

## Phase 6: User Story 4 - Spoken look is theatre of the mind (Priority: P4)

**Goal**: Player-facing narration is drawable and speakable, leak-free. Telegram and padding fail. No spoken band: omit the axis.

**Independent Test**: Give a second person only the player-facing passages. They can read them aloud without a secret, DC, unearned name, or process note, and the picture is drawable.

### Implementation for User Story 4

- [ ] T007 [US4] Add the Spoken look axis to `.agents/skills/blind-content-eval/SKILL.md`. Quote: Applies when player-facing narration exists. Pass: theatre of the mind — drawable, speakable, leak-free. Fail: secrets, DCs, unearned names, process notes, telegram, padding. Load `theatre-of-the-mind`; do not restate it. No spoken band: omit, not fail. After T006. Same file.

**Checkpoint**: All four stories independently testable

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: One source of truth for rubrics. No pytest. No legacy rewrite.

- [ ] T008 Confirm `.agents/skills/blind-content-eval/SKILL.md` does not restate copy-writer or TotM prose rules; it only names axes and loads those skills
- [ ] T009 Run `specs/012-blind-content-eval/quickstart.md` steps 1–7 against `specs/012-blind-content-eval/contracts/blind-content-eval.md`
- [ ] T010 Confirm the change set has 0 files under `legacy/` and no historical wiki page restyled solely to prove eval (SC-007)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP. T003 after T002 (same skill file). T004 parallel with T003
- **US2 (Phase 4)**: After T003 (same skill file)
- **US3 (Phase 5)**: After T005 (same skill file)
- **US4 (Phase 6)**: After T006 (same skill file)
- **Polish (Phase 7)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2
- **US2–US4**: After US1's T003; sequential with each other (same file)

### Parallel Opportunities

- T004 (`writing-for-agents`) ∥ T003 (`blind-content-eval` description)
- Do not parallelize T002, T003, T005, T006, T007 (same skill file)

---

## Parallel Example: User Story 1

```text
Task: description in .agents/skills/blind-content-eval/SKILL.md (T003)
Task: done-gate in .agents/skills/writing-for-agents/SKILL.md (T004)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 create `blind-content-eval`
3. Phase 3 US1 (description + writing-for-agents done-gate)
4. STOP — a guidance change is not done without two cold evals
5. Demo: file-shape check alone does not pass

### Incremental Delivery

1. Setup + Foundational
2. US1 → eval is the test
3. US2 → form and appropriate use
4. US3 → DM copy
5. US4 → spoken look
6. Polish → quickstart 1–7; no legacy rewrite

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` — one new skill + one done-gate
- Do not add test files unless a later command asks
- Do not rewrite wiki pages or `legacy/`
- Do not add a pytest suite or runner script
- Do not add a row to the 010 `AGENTS.md` stack table
- Commit after each task or logical group
- Stop at checkpoints
