---

description: "Task list for Agent Autonomy Scope"
---

# Tasks: Agent Autonomy Scope

**Input**: Design documents from `/specs/026-agent-autonomy-scope/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/autonomy-boundary.md, quickstart.md

**Tests**: No new test framework or pytest. Behavioral validation is `specs/026-agent-autonomy-scope/quickstart.md` V-001–V-008 (cold-context, live vault). Skill/instruction diffs use existing `skill-creator` evals. Do not add a review checklist, GitHub PR template, or review skill (FR-007).

**Organization**: Tasks are grouped by user story. `AGENTS.md` has one writer at a time — never parallelize two tasks that edit `AGENTS.md`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

Instruction edits only (plan.md). Canonical table lives in repo-root `AGENTS.md`. Skills defer; they MUST NOT ship a competing table.

```text
AGENTS.md
docs/agents/work.md
docs/agents/wiki-maintenance-loop.md
.agents/skills/wiki-lint/SKILL.md
.agents/skills/wiki-lint/CONSOLIDATE.md
.agents/skills/wiki-ingest/SKILL.md
```

Leave unchanged: `wiki-dedup` merge confirm, `wiki-stage-commit` promotion, creative-skill Work headers, `.agents/skills/skill-creator/SKILL.md` eval loop, constitution.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Bound the implement surface. No new packages, classifier, or docs.

- [X] T001 Confirm the six implement files in `specs/026-agent-autonomy-scope/plan.md` exist (`AGENTS.md`, `docs/agents/work.md`, `docs/agents/wiki-maintenance-loop.md`, `.agents/skills/wiki-lint/SKILL.md`, `.agents/skills/wiki-lint/CONSOLIDATE.md`, `.agents/skills/wiki-ingest/SKILL.md`) and do not create `docs/agents/autonomy.md`, a classifier script, a review checklist, a GitHub PR template, or a new review skill

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Single classification table and wait rule in `AGENTS.md`. Blocks every user story.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete. T002–T005 are sequential on `AGENTS.md`.

- [X] T002 Insert heading **Autonomy classification** in `AGENTS.md` by copying the table from `specs/026-agent-autonomy-scope/contracts/autonomy-boundary.md`; `classification` is `autonomous` | `dm-gated` only (`Derived; no third value`); unlisted operations use the decision rule; no `maybe`; do not use the avoided term "autonomous GM"; `AGENTS.md` is the only table
- [X] T003 Add the wait/decision rule under **Autonomy classification** in `AGENTS.md`: wait only if `user_asked_to_make_something_new` (`Explicit create/invent request (including new creative content on an existing page)`) OR `invents_canon_or_reconciles_contradiction` (`No-source invention, or pick-a-winner among conflicting facts`) → `dm-gated`; else `autonomous`; quote `Operations on existing wiki content that neither invent nor reconcile do not wait`
- [X] T004 Add the done-summary rule under **Autonomy classification** in `AGENTS.md`: after autonomous work, one short done-summary naming what changed and where; the summary MUST NOT ask a question or wait for a reply (FR-009)
- [X] T005 Replace the Helpers wiki-maintenance-loop sentence in `AGENTS.md` (`Never auto lore invent, mass kebab rename, dedup merge, or craft cuts`) so lore invent, dedup merge, and craft cuts stay gated while filename kebab / Aruhe / `00` remorph is autonomous (greenlit 2026-09-14)

**Checkpoint**: Foundation ready — `AGENTS.md` classifies any wiki op as `autonomous` or `dm-gated`

---

## Phase 3: User Story 1 - Autonomous Routine Wiki Maintenance (Priority: P1) 🎯 MVP

**Goal**: Lint, template conformance, named ingest, and Layer A structural repair complete without a Work prompt and end with a done-summary.

**Independent Test**: Cold-context agent lints a page with a broken `[[wikilink]]` and missing required frontmatter; repairs land (live or `_staging/` per `WIKI_STAGED_WRITES`); last message is a short done-summary; no question; no wait (`quickstart.md` V-001).

### Implementation for User Story 1

- [X] T006 [P] [US1] Update page-scoped and bulk repair in `.agents/skills/wiki-lint/SKILL.md` so FR-002 structural repair is autonomous (links, required frontmatter, nearest-valid type/lifecycle, kebab remorph with no extra greenlight); template conformance relocates existing content only and MUST NOT invent missing field body; content with no template field is preserved and flagged; canon contradiction writes `errors.md` and MUST NOT pick a winner (FR-008); After Linting ends with a done-summary; defer to `AGENTS.md` **Autonomy classification** without copying the table
- [X] T007 [P] [US1] Change `.agents/skills/wiki-lint/CONSOLIDATE.md` and the `--consolidate` blurb in `.agents/skills/wiki-lint/SKILL.md` so FR-002 actions apply without `"Apply these N changes? [yes / no / select]"`; keep confirm for merge, tier demotion, and other non-FR-002 actions
- [X] T008 [P] [US1] Update `.agents/skills/wiki-ingest/SKILL.md` so named ingest into `_staging/` does not wait for a second chat accept; invented names not in the source stay Work; ingest vs live canon conflict stages with a visible conflict marker (autonomous) and MUST NOT silently overwrite; end the named-ingest slice with a done-summary; defer to `AGENTS.md` without copying the table
- [X] T009 [P] [US1] Update Layer A in `docs/agents/wiki-maintenance-loop.md` so it MAY apply FR-002 structural repairs unattended; leave Layer C unchanged for lore invent, dedup merge, and contradiction resolution; defer to `AGENTS.md` without copying the table
- [X] T010 [US1] Execute V-001 in `specs/026-agent-autonomy-scope/quickstart.md` on the live vault (lint repair, done-summary, no wait)
- [ ] T011 [US1] Execute V-007 in `specs/026-agent-autonomy-scope/quickstart.md` (named ingest, no second ask)
- [ ] T012 [US1] Execute V-004 in `specs/026-agent-autonomy-scope/quickstart.md` (contradiction flagged in `errors.md`, neither fact rewritten to win)

**Checkpoint**: Maintenance-only sessions finish without a Work prompt and include a done-summary (SC-001, SC-003)

---

## Phase 4: User Story 2 - DM Approval Only for Creative Canon Work (Priority: P1)

**Goal**: Wait only for explicit new creative work, invented canon, or contradiction reconcile. Mixed requests split in one turn. New owners are Work-proposed whole; nothing filed until accept.

**Independent Test**: "Create an NPC named Varn who runs the docks" yields a chat Work proposal and no wiki file (including `_staging/`) until accept (`quickstart.md` V-002).

### Implementation for User Story 2

- [X] T013 [US2] Edit the load sentence in `docs/agents/work.md` so Work loads before prep/wrapup **and** before any FR-003 wait; FR-002 operations MUST NOT enter Propose; keep the Decide bullet that a direct imperative to repair/merge a named existing page is acceptance unless the change invents canon
- [X] T014 [US2] Add one sentence in `docs/agents/work.md` that creative pages still require Work accept before `_staging/` or live write, while FR-002 writes MAY land in `_staging/` without chat propose (`WIKI_STAGED_WRITES` does not change class)
- [X] T015 [US2] Add the mixed-request rule under **Autonomy classification** in `AGENTS.md`: complete the autonomous portion and its done-summary first, then present the Work proposal in the same turn, without waiting for a reply between them (FR-010)
- [X] T016 [US2] Update HARD: entity-before-spoken in `AGENTS.md` so a new named owner with no page that the user asked to introduce is Work-proposed as the whole owner; file nothing until accept (no stub); spoken text that depends on that owner waits; existing wiki content MUST NOT wait
- [ ] T017 [US2] Execute V-002 in `specs/026-agent-autonomy-scope/quickstart.md` (creative NPC stays Work-gated)
- [ ] T018 [US2] Execute V-003 in `specs/026-agent-autonomy-scope/quickstart.md` (mixed Bloodhawk cleanup + quest hook, same turn)
- [ ] T019 [US2] Execute V-008 in `specs/026-agent-autonomy-scope/quickstart.md` (new owner, nothing filed until accept)

**Checkpoint**: Creative requests wait; existing-content maintenance does not; mixed requests do both in one turn (SC-002)

---

## Phase 5: User Story 3 - Project Identity as Agent Infrastructure (Priority: P2)

**Goal**: Skills and instructions are the primary deliverables; review of those diffs uses existing skill-eval, not software metrics.

**Independent Test**: A `SKILL.md`-only diff is reviewed with `skill-creator` eval results (held-out prompts, with-skill vs without-skill, graded assertions); coverage/type-safety are not the primary bar; no new review surface (`quickstart.md` V-006).

### Implementation for User Story 3

- [X] T020 [US3] Add heading **Project identity** in `AGENTS.md`: primary deliverables are skills, agent instructions, and guidance documents; scripts and tooling support those; review of skill/instruction changes uses the existing `skill-creator` eval loop (held-out prompts, with-skill vs without-skill, graded assertions); MUST NOT add a checklist, PR template, or review skill; coverage/type-safety MUST NOT be the primary bar (FR-006, FR-007)
- [ ] T021 [US3] Execute V-006 in `specs/026-agent-autonomy-scope/quickstart.md` against a `SKILL.md`-only diff using `.agents/skills/skill-creator/SKILL.md` evals

**Checkpoint**: Instruction-change review cites skill-eval outcomes as the primary bar (SC-004)

---

## Phase 6: User Story 4 - Clear Autonomy Boundary Definition (Priority: P2)

**Goal**: Classification is mechanical. Two cold-context agents given the same task description agree.

**Independent Test**: Two independent cold-context agents classify ten one-line tasks using only `AGENTS.md` and produce identical classes (`quickstart.md` V-005 / SC-005).

### Implementation for User Story 4

- [X] T022 [US4] Strip any competing autonomy list from `docs/agents/work.md`, `docs/agents/wiki-maintenance-loop.md`, `.agents/skills/wiki-lint/SKILL.md`, `.agents/skills/wiki-lint/CONSOLIDATE.md`, and `.agents/skills/wiki-ingest/SKILL.md` so each file defers to `AGENTS.md` **Autonomy classification** (pointer only; invariant 2)
- [ ] T023 [US4] Execute V-005 in `specs/026-agent-autonomy-scope/quickstart.md` (ten one-line tasks covering both classes plus one unlisted operation; two cold-context agents; identical classes)

**Checkpoint**: Any wiki task classifies as exactly one of `autonomous` | `dm-gated` with no judgment call (SC-005)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Lean agent-facing prose, forbidden term, leave-alone surfaces, full quickstart.

- [X] T024 Apply `.agents/skills/writing-for-agents/SKILL.md` to the six implement files so each change is a positive instruction with a completion criterion and no competing copy of the table
- [X] T025 Confirm `.agents/skills/wiki-dedup/SKILL.md` merge confirm, `.agents/skills/wiki-stage-commit/SKILL.md` promotion review, creative-skill Work headers, and `.agents/skills/skill-creator/SKILL.md` eval loop are unchanged
- [X] T026 Confirm `.specify/memory/constitution.md` is unchanged and none of the six implement files use "autonomous GM"
- [ ] T027 Re-run any not-yet-green scenario in `specs/026-agent-autonomy-scope/quickstart.md` V-001–V-008 on the live vault

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories; T002 → T003 → T004 → T005 on `AGENTS.md`
- **User Stories (Phase 3+)**: All depend on Foundational
  - US1 (P1) and US2 (P1) after foundation; US2 `AGENTS.md` edits (T015, T016) wait until US1 is not writing `AGENTS.md`
  - US3 (P2) after US2 `AGENTS.md` edits (same file)
  - US4 (P2) after US1 satellite files exist so T022 can strip competing lists
- **Polish (Phase 7)**: After desired user stories

### User Story Dependencies

- **User Story 1 (P1)**: After Foundational — skill/loop files only; independently testable via V-001/V-004/V-007
- **User Story 2 (P1)**: After Foundational — `work.md` independent of US1; `AGENTS.md` mixed/owner rules sequential after T005; independently testable via V-002/V-003/V-008
- **User Story 3 (P2)**: After Foundational — **Project identity** heading in `AGENTS.md` sequential after T016; independently testable via V-006
- **User Story 4 (P2)**: After US1 satellite edits — strip competing lists; independently testable via V-005

### Within Each User Story

- Classification table before skill pointers
- Skill deltas before that story’s quickstart scenarios
- Story complete before moving to next `AGENTS.md` writer

### Parallel Opportunities

- T006, T007, T008, T009 after Phase 2 (four files)
- T013 can run in parallel with T006–T009 (`work.md` vs skill/loop files)
- T015/T016 MUST NOT overlap any other `AGENTS.md` task
- Quickstart scenarios within a story are sequential on the live vault

---

## Parallel Example: User Story 1

```bash
# After Phase 2, four files at once:
Task: "Update page-scoped and bulk repair in .agents/skills/wiki-lint/SKILL.md"
Task: "Change .agents/skills/wiki-lint/CONSOLIDATE.md FR-002 confirm gate"
Task: "Update named ingest in .agents/skills/wiki-ingest/SKILL.md"
Task: "Update Layer A in docs/agents/wiki-maintenance-loop.md"
```

---

## Parallel Example: User Story 2

```bash
# After Phase 2, work.md can start with US1 skills:
Task: "Edit the load sentence in docs/agents/work.md"

# AGENTS.md mixed/owner rules only after T005 (and not while another AGENTS.md task is open):
Task: "Add the mixed-request rule under Autonomy classification in AGENTS.md"
Task: "Update HARD: entity-before-spoken in AGENTS.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (`AGENTS.md` table + wait + done-summary)
3. Complete Phase 3: User Story 1 (lint/ingest/loop + V-001/V-004/V-007)
4. **STOP and VALIDATE**: maintenance-only sitting has a done-summary and no Work prompt
5. Demo if ready

### Incremental Delivery

1. Setup + Foundational → classification exists
2. US1 → autonomous maintenance (MVP)
3. US2 → Work gate only for new/invent/reconcile
4. US3 → project identity + skill-eval review bar
5. US4 → two-agent classify (SC-005)
6. Polish → writing-for-agents + leave-alone check + remaining V-00n

### Parallel Team Strategy

1. One writer finishes Phase 2 on `AGENTS.md`
2. Then:
   - Dev A: T006–T012 (US1 skills + V-001/V-004/V-007)
   - Dev B: T013–T014 (`work.md`) then waits for `AGENTS.md` to take T015–T019
3. US3/US4 after `AGENTS.md` and satellite files settle

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to spec user stories US1–US4
- Dedup merge, stage-commit promotion, and invented template-field body stay gated (data-model.md Explicitly not autonomous)
- Staged writes are orthogonal to class
- Commit after each task or logical group
- Stop at any checkpoint to validate the story independently
