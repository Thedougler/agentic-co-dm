---
description: "Task list for Agent Autonomy Scope"
---

# Tasks: Agent Autonomy Scope

**Input**: Design documents from `/specs/026-agent-autonomy-scope/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/agent-autonomy.md, quickstart.md

**Tests**: Plan requires one pytest (`tests/test_agent_standards.py`) plus `scripts/check-agent-standards.py`. Behavioral validation is `specs/026-agent-autonomy-scope/quickstart.md` V-001–V-008 (cold-context, live vault). Skill/instruction diffs use existing `skill-creator` evals. Do not add a review checklist, GitHub PR template, or review skill (FR-007).

**Organization**: Tasks are grouped by user story. Constitution, `AGENTS.md`, and `rules/registry.yml` have one writer at a time — never parallelize two tasks that edit the same of those files. Skills MUST NOT copy the four-line canon. Do not say "autonomous GM".

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US5, US6 — spec has no US4)
- Include exact file paths in descriptions

## Path Conventions

```text
.specify/memory/constitution.md
AGENTS.md
wiki/AGENTS.md
.omp/AGENTS.md
docs/agents/work.md
docs/agents/wiki-maintenance-loop.md
docs/agents/hybrid-sdd.md
docs/agents/policy-owners.yml
.agents/skills/**/SKILL.md
rules/registry.yml
scripts/check-agent-standards.py
tests/test_agent_standards.py
```

Canon owner after implement: constitution principle X. Executable rules: `AGENT001` `AGENT002` `AGENT003` via `scripts/check-agent-standards.py`. `AGENTS.md` is why/examples only.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Bound the implement surface. No new packages, classifier, review surface, or lint framework.

- [X] T001 Confirm the implement files named in `specs/026-agent-autonomy-scope/plan.md` exist and do not create `docs/agents/autonomy.md`, a classifier script, a review checklist, a GitHub PR template, a new review skill, or a new lint framework; reuse `scripts/check-policy-conflicts` shape for the later checker

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Constitution owns the four-line canon; `AGENTS.md` points; registry ids exist. Blocks every user story (XVI).

**⚠️ CRITICAL**: No user story work can begin until this phase is complete. T002 then T003 then T004 are sequential (constitution → `AGENTS.md` → registry).

- [X] T002 Amend `.specify/memory/constitution.md` MAJOR `3.0.0` (`2.12.0` → `3.0.0`, Last Amended `2026-09-18`, Sync Impact Report): principle X is exactly "If the user said it, it is canon. If the user said it more recently, that is more canon. If a transcript says it, after ASR issues are fixed, it is canon. DM-placed ingest files are canon as long as they do not contradict 1–3." (`user_said`, `more_recent_user_said`, `corrected_transcript`, `dm_placed_ingest`); Co-DM files what those lines make canon; do not invent what the user did not say (XII); do not pick a winner among contradictions unless the user picked; principle XV: agents complete requested work and unattended maintenance with no approval wait and a done-summary after green; principle XVII: wiki files user/transcript/non-contradicting ingest immediately; Operating Boundaries delete campaign-facts-remain-DM-gated
- [X] T003 In `AGENTS.md` delete heading **Autonomy classification**, the `autonomous` / `dm-gated` table, and the wait rule; point at constitution X for canon (do not copy the four lines); point at `AGENT001`–`AGENT003` / wiki-lint for the contract; keep **Project identity** (skills/instructions/guidance primary; scripts support; `skill-creator` eval bar; MUST NOT add a checklist, PR template, or review skill); state done-summary shape (what changed, where; no question; no wait); replace `Load docs/agents/work.md` so it is not "wiki write after DM accept"; HARD entity-before-spoken files the named owner then spoken (not a wait for accept); mixed request does both then one done-summary after green; Helpers: FR-002 unattended, unsaid invention is not canon; dedup merge without user ask still confirms
- [X] T004 Register `AGENT001`, `AGENT002`, and `AGENT003` in `rules/registry.yml` with `evaluator: symbolic`, `scope: instruction`, `severity: BLOCK`, `lifecycle: ACTIVE`; `AGENT001` encodes FR-001/FR-005 (fail on `## Work gate`, `dm-gated`, `file nothing until accept`, `wiki write after DM accept`, `Work-propose`, `wait for accept`); `AGENT002` encodes FR-013 (paths `.agents/skills/<kebab>/SKILL.md`, `.agents/skills/<kebab>/<kebab>.md`, `docs/agents/<kebab>.md`, `docs/agents/<kebab>.yml`, `AGENTS.md`, `wiki/AGENTS.md`, `.omp/AGENTS.md`); `AGENT003` encodes FR-004/FR-011 (a `specs/*/spec.md` Functional Requirement containing `agent-facing` MUST cite at least one `rules/registry.yml` id)

**Checkpoint**: Foundation ready — constitution X is the canon owner; `AGENTS.md` has no competing gate; registry ids exist

---

## Phase 3: User Story 1 - Autonomous Routine Wiki Maintenance (Priority: P1) 🎯 MVP

**Goal**: Lint, template conformance, named ingest, and Layer A structural repair complete without an approval wait and end with one done-summary after green.

**Independent Test**: Cold-context agent lints a page with a broken `[[wikilink]]` and missing required frontmatter; repairs land on live wiki paths; applicable wiki-lint is green; last message is a short done-summary; no question; no wait (`quickstart.md` V-001).

### Implementation for User Story 1

- [X] T005 [P] [US1] Update page-scoped and bulk repair in `.agents/skills/wiki-lint/SKILL.md` so FR-002 structural repair (links, required frontmatter, nearest-valid type/lifecycle) files without a wait; template conformance relocates existing content only and MUST NOT invent missing field body; content with no template field is preserved; After Linting ends with a done-summary after green; delete the `AGENTS.md` **Autonomy classification** pointer; do not copy canon
- [X] T006 [P] [US1] Change `.agents/skills/wiki-lint/consolidate.md` and the `--consolidate` blurb in `.agents/skills/wiki-lint/SKILL.md` so FR-002 actions apply without `"Apply these N changes? [yes / no / select]"`; if the user asked to merge duplicates, file the merge; unattended destructive merge without a user ask keeps confirm (not a Work gate); delete the Autonomy classification pointer
- [X] T007 [P] [US1] Update `.agents/skills/wiki-ingest/SKILL.md` so named ingest files to the live wiki without a second chat accept; `dm_placed_ingest` that contradicts user/transcript is not canon (do not file that contradiction as truth; no ask); end the named-ingest slice with a done-summary after green; delete the Autonomy classification pointer
- [X] T008 [P] [US1] Update `docs/agents/wiki-maintenance-loop.md`: delete the Autonomy classification pointer; Layer A MAY apply FR-002 structural repairs unattended; Layer C MUST NOT invent lore the user did not say; user-asked new content files under canon
- [X] T009 [US1] Execute V-001 in `specs/026-agent-autonomy-scope/quickstart.md` on the live vault (lint repair, green, done-summary, no wait)

**Checkpoint**: Maintenance-only sessions finish without a Work prompt and include a done-summary (SC-001)

---

## Phase 4: User Story 2 - Canon (Priority: P1)

**Goal**: Four-line canon is the whole workflow. File what the user said. No Work gate, no DM-approval pause, no extra canon steps.

**Independent Test**: User says “create an NPC named Varn who runs the docks.” Agent files the page, rules go green, short done-summary (`quickstart.md` V-002).

### Implementation for User Story 2

- [X] T010 [US2] Edit `docs/agents/work.md`: remove Propose / Decide acceptance waits; file what constitution X makes canon; keep table aim and reflection only if they do not reintroduce a pause; delete the Autonomy classification pointer
- [X] T011 [P] [US2] Rewrite **Approval (FR-019)** in `wiki/AGENTS.md` so wiki facts the user said file immediately on the live path; delete `lifecycle` defaults to `proposed` until the DM accepts and "Wiki facts change only after the DM accepts"; HARD entity-before-spoken files the owner then spoken
- [X] T012 [P] [US2] Update `docs/agents/hybrid-sdd.md` so `dm_acceptance` is not required for user-said canon
- [X] T013 [P] [US2] Update `docs/agents/policy-owners.yml` so `acceptance_semantics` and `mutation_approval` MUST NOT require mutation acceptance as a chat gate
- [X] T014 [P] [US2] Strip competing gate restatements from `.omp/AGENTS.md` (and check `CODEX.md`, `CLAUDE.md`, `GROK.md`) so harness files do not restate shared canon/wait behavior (XVI); point, do not copy the four lines
- [X] T015 [US2] Delete every `## Work gate` section and remaining forbidden procedure language (`dm-gated`, `file nothing until accept`, `wiki write after DM accept`, `Work-propose`, `wait for accept`) from `.agents/skills/campaign-planning/SKILL.md`, `.agents/skills/cold-opens/SKILL.md`, `.agents/skills/dnd-5e-magic-item-design/SKILL.md`, `.agents/skills/dnd5e-mechanics/SKILL.md`, `.agents/skills/dungeon-design/SKILL.md`, `.agents/skills/encounter-prep/SKILL.md`, `.agents/skills/homebrew-monsters-5e/SKILL.md`, `.agents/skills/npc-design/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/place-design/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/run-guide/SKILL.md`, `.agents/skills/sandbox-narrative/SKILL.md`, `.agents/skills/session-recap/SKILL.md`, `.agents/skills/theatre-of-the-mind/SKILL.md`, `.agents/skills/traps-trials/SKILL.md`, `.agents/skills/travel-events/SKILL.md`, `.agents/skills/visual-aids/SKILL.md`, `.agents/skills/visual-references/SKILL.md`, `.agents/skills/world-tick/SKILL.md`, `.agents/skills/writing-beats/SKILL.md`; if a pointer is required, point at `AGENTS.md` only; do not copy canon; session-recap files the recap when the user asked — no accept pause
- [X] T016 [US2] Execute V-002, V-003, V-004, and V-008 in `specs/026-agent-autonomy-scope/quickstart.md` (file Varn; mixed Bloodhawk cleanup + quest hook one summary; more recent user statement wins inner lock; file new owner then spoken)

**Checkpoint**: User-said content is filed; mixed requests one summary; no accept pause (SC-002, SC-003)

---

## Phase 5: User Story 5 - Agent-Facing Standards Are Checkable (Priority: P1)

**Goal**: AGENT001–AGENT003 are the executable contract. Agents iterate until green. `AGENTS.md` is why/examples only. Same checker on agent path and human path (FR-014).

**Independent Test**: `.venv/bin/python scripts/check-agent-standards.py --json` exits 0 when instruction files match; re-insert `## Work gate` → AGENT001 fail (`quickstart.md` V-007). A later feature that adds an agent-facing FR with no registry id is incomplete (AGENT003).

### Tests for User Story 5 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T017 [P] [US5] Add `tests/test_agent_standards.py` copying `tests/test_policy_conflicts.py` shape: run `scripts/check-agent-standards.py --json`; assert exit 0 / `status` clean on a conforming tree; assert exit ≠ 0 when a scanned file contains `## Work gate`; assert AGENT002 fail on `.agents/skills/My Skill/notes.txt`; assert AGENT003 fail when a `specs/*/spec.md` FR contains `agent-facing` with no `rules/registry.yml` id

### Implementation for User Story 5

- [X] T018 [US5] Implement `scripts/check-agent-standards.py` (Python 3 stdlib + PyYAML like `scripts/check-policy-conflicts`): args in, JSON out, exit 0 clean / 1 findings / 2 error; scan `AGENTS.md`, `wiki/AGENTS.md`, `docs/agents/**/*.md`, `.agents/skills/**/*.md` for AGENT001; scan the live agent-facing tree for AGENT002 path/name; scan `specs/*/spec.md` Functional Requirements for AGENT003; no new CI job
- [X] T019 [US5] Cite at least one `rules/registry.yml` id on every Functional Requirement containing `agent-facing` in `specs/*/spec.md`, including `specs/026-agent-autonomy-scope/spec.md` (`AGENT001`, `AGENT002`, `AGENT003`)
- [X] T020 [US5] Execute V-007 in `specs/026-agent-autonomy-scope/quickstart.md` (checker green; negative `## Work gate` and ad-hoc skill path fail)

**Checkpoint**: Lint is the contract; prose is not a substitute (SC-006, SC-007)

---

## Phase 6: User Story 6 - Predictable Agent-Facing Files (Priority: P1)

**Goal**: Every agent-facing file matches AGENT002. This feature bulk-renames the existing tree. No grandfathering. Carve-outs only after a problem already experienced.

**Independent Test**: An agent-facing file that is not at the predicted path or that uses an ad-hoc unsearchable name fails AGENT002, including files that predate this feature (SC-008).

### Implementation for User Story 6

- [X] T021 [US6] Remorph non-conforming companions to kebab and update references in the same pass: `.agents/skills/wiki-lint/checks.md` → `.agents/skills/wiki-lint/checks.md`, `.agents/skills/wiki-lint/consolidate.md` → `.agents/skills/wiki-lint/consolidate.md`, `.agents/skills/llm-wiki/paper-template.md`, `.agents/skills/obsidian-markdown/upstream.md`, `.agents/skills/obsidian-markdown/references/callouts.md`, `columns.md`, `embeds.md`, `properties.md`, `.agents/skills/wiki-capture/references/raw-format.md`, plus every other live agent-facing path that does not match AGENT002 in `specs/026-agent-autonomy-scope/contracts/agent-autonomy.md`; no proactive exclude list
- [X] T022 [US6] Run `.venv/bin/python scripts/check-agent-standards.py --json` and repair remaining AGENT002 (and AGENT001) findings until exit 0

**Checkpoint**: 100% of shipped agent-facing files satisfy the path/name rule (SC-008)

---

## Phase 7: User Story 3 - Project Identity as Agent Infrastructure (Priority: P2)

**Goal**: Skills and instructions are the primary deliverables; review of those diffs uses existing skill-eval, not software metrics.

**Independent Test**: A `SKILL.md`-only diff is reviewed with `skill-creator` eval results (held-out prompts, with-skill vs without-skill, graded assertions); coverage/type-safety are not the primary bar; no new review surface (`quickstart.md` V-006).

### Implementation for User Story 3

- [X] T023 [US3] Confirm **Project identity** in `AGENTS.md` still states: primary deliverables are skills, agent instructions, and guidance documents; scripts and tooling support those; review uses existing `skill-creator` eval loop (held-out prompts, with-skill vs without-skill, graded assertions); MUST NOT add a checklist, PR template, or review skill; coverage/type-safety MUST NOT be the primary bar (FR-006, FR-007)
- [X] T024 [US3] Execute V-006 in `specs/026-agent-autonomy-scope/quickstart.md` against a `SKILL.md`-only diff using `.agents/skills/skill-creator/SKILL.md` evals

**Checkpoint**: Instruction-change review cites skill-eval outcomes as the primary bar (SC-004)

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Lean agent-facing prose, forbidden term, green checker, two-agent completion.

- [X] T025 Apply `.agents/skills/writing-for-agents/SKILL.md` to the files this feature changed so each change is a positive instruction with a completion criterion and no copied four-line canon or Autonomy table
- [X] T026 Confirm none of the scanned instruction files use "autonomous GM"; confirm `.agents/skills/wiki-dedup/SKILL.md` unattended merge without a user ask still confirms; confirm `.agents/skills/skill-creator/SKILL.md` eval loop is unchanged
- [X] T027 Execute V-005 in `specs/026-agent-autonomy-scope/quickstart.md` (two independent cold-context agents, same one-line task, both file lint repair and NPC, green, done-summary, neither waits) (SC-005)
- [X] T028 Re-run any not-yet-green scenario in `specs/026-agent-autonomy-scope/quickstart.md` V-001–V-008 and `.venv/bin/python scripts/check-agent-standards.py --json` until exit 0

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories; T002 → T003 → T004
- **User Stories (Phase 3+)**: All depend on Foundational
  - US1 (P1) after foundation; skill/loop files only
  - US2 (P1) after foundation; `work.md` / `wiki/AGENTS.md` / hybrid-sdd / policy-owners / harness / skill strips; do not write `AGENTS.md` (T003 owns it)
  - US5 (P1) after US2 strips so AGENT001 can go green; checker then spec cites
  - US6 (P1) after US5 checker exists; remorph until AGENT002 green
  - US3 (P2) after T003 Project identity exists
- **Polish (Phase 8)**: After desired user stories

### User Story Dependencies

- **User Story 1 (P1)**: After Foundational — independently testable via V-001
- **User Story 2 (P1)**: After Foundational — independently testable via V-002/V-003/V-004/V-008
- **User Story 5 (P1)**: After US2 instruction strips — independently testable via V-007
- **User Story 6 (P1)**: After US5 checker — independently testable via AGENT002 exit 0
- **User Story 3 (P2)**: After Foundational — independently testable via V-006

### Within Each User Story

- Tests (US5) MUST be written and FAIL before the checker
- Models/owners (constitution, registry) before consumers
- Story complete before moving to the next writer on a shared file
- Green-before-done: do not mark a story done while AGENT001–003 for that work still fail

### Parallel Opportunities

- T005, T006, T007, T008 after Phase 2 (four files)
- T011, T012, T013, T014 after T010 starts (`wiki/AGENTS.md`, hybrid-sdd, policy-owners, harness vs `work.md`)
- T017 can be written in parallel with US1/US2 file edits (new test file)
- T003 MUST NOT overlap any other `AGENTS.md` task
- T002 MUST NOT overlap any other constitution task
- Quickstart scenarios on the live vault are sequential

---

## Parallel Example: User Story 1

```bash
# After Phase 2, four files at once:
Task: "Update page-scoped and bulk repair in .agents/skills/wiki-lint/SKILL.md"
Task: "Change .agents/skills/wiki-lint/consolidate.md FR-002 confirm gate"
Task: "Update named ingest in .agents/skills/wiki-ingest/SKILL.md"
Task: "Update Layer A in docs/agents/wiki-maintenance-loop.md"
```

---

## Parallel Example: User Story 2

```bash
# After Phase 2, satellites in parallel (not AGENTS.md):
Task: "Rewrite Approval in wiki/AGENTS.md"
Task: "Update docs/agents/hybrid-sdd.md dm_acceptance"
Task: "Update docs/agents/policy-owners.yml"
Task: "Strip competing gates from .omp/AGENTS.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (constitution X + `AGENTS.md` pointers + registry ids)
3. Complete Phase 3: User Story 1 (lint/ingest/loop + V-001)
4. **STOP and VALIDATE**: maintenance-only sitting has a done-summary and no wait
5. Demo if ready

### Incremental Delivery

1. Setup + Foundational → canon owner exists
2. US1 → autonomous maintenance (MVP)
3. US2 → file user-said canon; Work gates gone
4. US5 → checker is the contract
5. US6 → path/name remorph green
6. US3 → skill-eval review bar
7. Polish → writing-for-agents + V-005 + remaining V-00n

### Parallel Team Strategy

1. One writer finishes Phase 2 (constitution then `AGENTS.md` then registry)
2. Then:
   - Dev A: T005–T009 (US1)
   - Dev B: T010–T016 (US2 satellites + strips)
3. US5 checker after strips; US6 remorph after checker; US3 anytime after T003

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to spec user stories US1, US2, US3, US5, US6 (no US4)
- Unsaid invention is not canon (XII)
- Dedup merge without user ask stays a destructive confirm; user-asked merge files
- Commit after each task or logical group
- Stop at any checkpoint to validate the story independently
- Avoid: vague tasks, same-file conflicts, copying the four-line canon into skills
