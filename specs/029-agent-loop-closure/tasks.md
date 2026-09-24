---
description: "Dependency-ordered implementation tasks for agent loop closure"
---

# Tasks: Agent Loop Closure

**Input**: Design documents from `/specs/029-agent-loop-closure/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/capability-loop.md`, `quickstart.md`

**Tests**: Required by the specification. Public-seam tests and cold behavioral evaluations precede each implementation slice.

**Organization**: Tasks are grouped by user story so each story remains independently testable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it uses a disjoint file and has no incomplete predecessor
- **[Story]**: Maps the task to a user story in `spec.md`
- Every task names its exact target path

## Phase 1: Setup (Accountability and Baseline)

**Purpose**: Establish the required issue surface and freeze comparable pre-change evidence.

- [X] T001 Link or create the accountable implementation issue and record its URL in `specs/029-agent-loop-closure/plan.md`
- [X] T002 Define at least ten comparable baseline/replay case IDs, categories, success/stall variants, and weakest-sufficient executor assignments in `specs/029-agent-loop-closure/quickstart.md`
- [ ] T003 Capture pre-change cold trajectory records for the cases defined by T002 in the existing named-owner `.agents/skills/*/evals/evals.json` files, recording outcome, observations, actions, turns, tool calls, retrieval attempts, duplicate equivalent actions, handoffs, validation passes, tokenizer-identified trajectory tokens, termination reason, hard gates, and semantic review

---

## Phase 2: Foundational (Shared Loop Authority)

**Purpose**: Establish the common loop contract before owner-specific implementation.

**⚠️ CRITICAL**: T001–T003 and this phase block all user story implementation.

- [X] T004 Add the canonical route → observe → act → re-observe → continue/change-path/complete/block invariant, owner-relative progress rules, and specific-blocker fields to `docs/agents/hybrid-sdd.md`
- [X] T005 Add only the compact always-loaded loop invariant and canonical pointer to `AGENTS.md`, preserving the full procedure in `docs/agents/hybrid-sdd.md`
- [X] T006 Reconcile the wiki semantic pointer with the canonical loop authority without duplicating common procedure in `wiki/AGENTS.md`
- [X] T007 Update durable Capability Iteration and Progress Evidence terminology only where required, without changing the existing Execution Graph definition, in `CONTEXT.md`

**Checkpoint**: Common authority is stable; story-specific slices may begin in dependency order.

---

## Phase 3: User Story 1 — Close Every Capability Branch (Priority: P1) 🎯 MVP

**Goal**: Every representative branch continues only on meaningful owner-relative progress and ends at its completion guard or a specific blocker.

**Independent Test**: Run cold successful and deliberately stalled representative jobs; every action starts from current evidence, no equivalent action repeats against unchanged evidence, successful branches pass owner guards, and unsuccessful branches report all blocker fields.

### Behavioral Tests for User Story 1

- [X] T008 [P] [US1] Add cold success, premature-completion, equivalent-action stall, and specific-blocker assertions to the representative owner `.agents/skills/*/evals/evals.json` files named by the T002 case matrix
- [X] T009 [P] [US1] Add contract examples for current observation, owner-sanctioned action, same-boundary re-observation, meaningful progress, completion, change-path, and blocking to `specs/029-agent-loop-closure/contracts/capability-loop.md`

### Implementation for User Story 1

- [X] T010 [US1] Reconcile T008 failures by tightening the common iteration, completion, equivalent-action, and blocker rules in `docs/agents/hybrid-sdd.md`
- [ ] T011 [US1] Run the T008 cold cases with the weakest sufficient executor and record passing outcome plus owner, boundary, surviving observation, attempted paths, reason, and parent effect for every blocker in the same `.agents/skills/*/evals/evals.json` records

**Checkpoint**: The common loop independently converges or blocks with evidence.

---

## Phase 4: User Story 2 — Preserve Correct Guards and Scope (Priority: P1)

**Goal**: Remove the four confirmed guard contradictions before broader loop promotion.

**Independent Test**: Query leaves canonical state unchanged; scoped lint never expands scope; faction Done accepts `wiki/entities/faction/`; user-stated place canon files immediately without a second acceptance wait.

### Behavioral Tests for User Story 2

- [X] T012 [P] [US2] Add read-isolation and selected-scope coherence cases to `.agents/skills/wiki-query/evals/evals.json` and `.agents/skills/wiki-lint/evals/evals.json`
- [X] T013 [P] [US2] Add current faction-path and immediate user-said place-canon cases to `.agents/skills/faction-design/evals/evals.json` and `.agents/skills/place-design/evals/evals.json`

### Implementation for User Story 2

- [X] T014 [P] [US2] Remove canonical `log.md` mutation from read-only completion and preserve QMD-first synthesis behavior in `.agents/skills/wiki-query/SKILL.md`
- [X] T015 [P] [US2] Preserve the selected path through lint observation, deterministic fix, semantic repair, and re-observation in `.agents/skills/wiki-lint/SKILL.md`
- [X] T016 [P] [US2] Replace the legacy faction completion path with the canonical `wiki/entities/faction/` owner path in `.agents/skills/faction-design/SKILL.md`
- [X] T017 [P] [US2] Remove the separate acceptance wait for user-said canon while retaining owner completion and filing guards in `.agents/skills/place-design/SKILL.md`
- [ ] T018 [US2] Run quickstart V-001 and record the four passing coherence results in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Loop guards target current authority and requested scope.

---

## Phase 5: User Story 3 — Converge Deterministic Maintenance (Priority: P1)

**Goal**: Expose truthful same-scope repair progress and prevent unchanged repair loops.

**Independent Test**: Focused `scripts/wiki lint fix <path>` cases resolve, skip, or preserve findings while emitting the complete progress object and never retrying an unchanged unsupported repair.

### Tests for User Story 3

- [X] T019 [US3] Add failing public-seam tests for selected-scope retention and `progress.before_total`, `after_total`, `resolved`, `changed_files`, `next_changed`, and `state_changed` in `tests/test_wiki_cli.py`
- [X] T020 [P] [US3] Add failing cold cases for unsupported deterministic repair, unchanged semantic repair, and complete blocker fields to `.agents/skills/wiki-lint/evals/evals.json`

### Implementation for User Story 3

- [X] T021 [US3] Compose the progress delta from existing pre-fix and post-fix same-scope worklists while preserving existing result fields in `scripts/wiki`
- [X] T022 [US3] Update the public lint-fix progress and scope contract in `specs/027-wiki-agent-cli/contracts/wiki-cli.md`
- [X] T023 [P] [US3] Add the progress result shape to `specs/027-wiki-agent-cli/data-model.md` with these exact constraints: `before_total` and `after_total` are non-negative integers; `resolved` is an array; `changed_files` is an array of vault-relative paths; `next_changed` and `state_changed` are booleans
- [X] T024 [US3] Add no-repeat handling for unchanged skipped/unsupported fixes and reread/change-path/block handling for identical semantic findings in `.agents/skills/wiki-lint/SKILL.md`
- [X] T025 [US3] Run focused `tests/test_wiki_cli.py` cases and quickstart V-004/V-005 against a disposable configured vault, then record the observed results in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Deterministic maintenance exposes progress and terminates without spinning.

---

## Phase 6: User Story 4 — Deepen Retrieval Without Spinning (Priority: P2)

**Goal**: Query and context-pack retrieval deepen only into focused unexplored evidence and remain read-only.

**Independent Test**: First-hit, one-deepening, unchanged-candidate, and silent/failing-collection cases stop at sufficiency or a specific blocker without duplicate retrieval or canonical mutation.

### Behavioral Tests for User Story 4

- [X] T026 [P] [US4] Add sufficient-first-hit, focused-deepening, unchanged-candidate, and canonical-read-isolation cases to `.agents/skills/wiki-query/evals/evals.json`
- [X] T027 [P] [US4] Add bounded-pack, documented-fallback, unchanged-terminal-retrieval, and canonical-read-isolation cases to `.agents/skills/wiki-context-pack/evals/evals.json`

### Implementation for User Story 4

- [X] T028 [P] [US4] Add evidence-sufficiency, unexplored-path, unchanged-candidate, and evidenced-gap termination rules to `.agents/skills/wiki-query/SKILL.md`
- [X] T029 [P] [US4] Add evidence-budget completion, documented fallback, unchanged-candidate, and specific-blocker rules to `.agents/skills/wiki-context-pack/SKILL.md`
- [ ] T030 [US4] Run quickstart V-006/V-007 and record passing retrieval convergence and read-isolation evidence in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Read owners gather enough evidence and stop without mutation or repeated retrieval.

---

## Phase 7: User Story 5 — Resume Parent Work After Bounded Handoffs (Priority: P2)

**Goal**: Session, place, and run-guide parents advance only from bounded child completion evidence while preserving their original objective.

**Independent Test**: Complete, incomplete, stalled, and compacted child-return cases update relevant dependencies or block; unrelated child context is absent after resumption.

### Behavioral Tests for User Story 5

- [X] T031 [P] [US5] Add complete/incomplete typed-beat return, objective preservation, and context-reset cases to `.agents/skills/session-beats/evals/evals.json`
- [X] T032 [P] [US5] Add bounded faction/narration return, blocked child, and same-seam stall cases to `.agents/skills/place-design/evals/evals.json`
- [X] T033 [P] [US5] Add four-pass completion, missing owner/path/section, and later-pass blocking cases to `.agents/skills/run-guide/evals/evals.json`

### Implementation for User Story 5

- [X] T034 [P] [US5] Require typed-beat child evidence to change a dependency, artifact state, or completion evidence before parent resumption in `.agents/skills/session-beats/SKILL.md`
- [X] T035 [P] [US5] Require bounded child evidence, preserve the place objective, and block unchanged seam re-entry in `.agents/skills/place-design/SKILL.md`
- [X] T036 [P] [US5] Require each guide pass to satisfy its completion evidence before the next pass and stop missing-owner/path/section cases precisely in `.agents/skills/run-guide/SKILL.md`
- [ ] T037 [US5] Run quickstart V-010/V-011/V-012 and record passing parent-resumption, dependency, context-reset, and blocker evidence in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Composed parents retain objectives and advance only on complete child evidence.

---

## Phase 8: User Story 6 — Finalize Bounded Write Work Once (Priority: P2)

**Goal**: Ingest, capture, and update advance bounded work and invoke existing tracking and retrieval finalization exactly once.

**Independent Test**: Multi-child ingest, full/quick capture, update/no-op, and terminal recovery cases shrink work or sharpen blockers; incomplete children prevent finalization and completed operations finalize once.

### Behavioral Tests for User Story 6

- [X] T038 [P] [US6] Add multi-child completion, incomplete-child blocking, and exactly-once finalization cases to `.agents/skills/wiki-ingest/evals/evals.json`
- [X] T039 [P] [US6] Add full/quick mode progress, validation, and exactly-once finalization cases to `.agents/skills/wiki-capture/evals/evals.json`
- [X] T040 [P] [US6] Add changed-delta, no-op termination, transient fallback, and terminal-blocker cases to `.agents/skills/wiki-update/evals/evals.json`

### Implementation for User Story 6

- [X] T041 [P] [US6] Make source/destination progress and parent-owned exactly-once manifest/index/log/hot/QMD finalization explicit in `.agents/skills/wiki-ingest/SKILL.md`
- [X] T042 [P] [US6] Make mode-relative progress and exactly-once tracking/finalization explicit without changing quick-capture ownership in `.agents/skills/wiki-capture/SKILL.md`
- [X] T043 [P] [US6] Make delta/no-op termination, documented recovery, and exactly-once finalization explicit in `.agents/skills/wiki-update/SKILL.md`
- [ ] T044 [US6] Run quickstart V-008/V-009/V-013 and record bounded progress, incomplete-child blocking, exactly-once finalization, and tool-recovery evidence in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Write parents account for every bounded destination and finalize once.

---

## Phase 9: User Story 7 — Promote from Paired Trajectory Evidence (Priority: P3)

**Goal**: Promote only from comparable cold baseline/replay evidence that preserves semantic quality and eliminates spinning.

**Independent Test**: At least ten baseline/replay pairs expose all required trajectory fields, accept valid alternative strategies, pass every hard gate, and make no token claim unless the existing threshold is met.

### Behavioral Tests for User Story 7

- [X] T045 [US7] Add paired grading assertions for outcome, invariant compliance, alternative valid strategies, hard gates, and semantic non-inferiority to `.agents/skills/skill-creator/evals/evals.json`
- [ ] T046 [US7] Replay the T002 case matrix with the weakest sufficient executor and store comparable post-change trajectory evidence beside each baseline in the existing named-owner `.agents/skills/*/evals/evals.json` files
- [ ] T047 [US7] Perform blind paired fixed-rubric review of playability, specificity, continuity, player agency, and DM usefulness and record results in the matching `.agents/skills/*/evals/evals.json` records
- [X] T048 [US7] Count trajectory tokens with `scripts/token-count.py`, record tokenizer/model compatibility, and record either a qualified five-percent median improvement claim or explicitly no token-improvement claim in `specs/029-agent-loop-closure/quickstart.md`
- [ ] T049 [US7] Record promotion results for at least ten pairs, including zero duplicate equivalent actions, lost objectives, duplicate finalizations, read mutations, and unspecific intentional stalls, in `specs/029-agent-loop-closure/quickstart.md`

**Checkpoint**: Promotion is backed by comparable trajectory and semantic-quality evidence.

---

## Phase 10: Polish & Cross-Cutting Verification

**Purpose**: Verify compatibility, remove temporary evidence, and confirm the implementation stayed inside scope.

- [X] T050 Run all focused `tests/test_wiki_cli.py` and any changed owner eval validation commands, recording command outcomes in `specs/029-agent-loop-closure/quickstart.md`
- [X] T051 [P] Run `specify integration status --json` and record the `ok` default-OMP four-integration result in `specs/029-agent-loop-closure/quickstart.md`
- [X] T052 [P] Run `scripts/check-omp-baseline.sh` and record the exit result in `specs/029-agent-loop-closure/quickstart.md`
- [X] T053 Review changed paths for forbidden orchestration, persistent state, progress commands, global iteration limits, proactive carve-outs, campaign content, unrelated templates/rules/skills, or generated Spec Kit adapter changes and record the result in `specs/029-agent-loop-closure/quickstart.md`
- [X] T054 Remove throwaway baseline/replay scratch artifacts while retaining the required redacted evaluation evidence in the existing `.agents/skills/*/evals/evals.json` files

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Starts immediately; T001 is the implementation gate, T002 precedes T003.
- **Foundational (Phase 2)**: Depends on T001–T003; T004 → T005/T006/T007.
- **US1 (Phase 3)**: Depends on Phase 2; proves the common contract.
- **US2 (Phase 4)**: Depends on Phase 2 and must complete before US3–US7 promotion evidence is trusted.
- **US3 (Phase 5)**: Depends on US2 scope coherence; T019 must fail before T021; T021 precedes T022/T023/T024/T025.
- **US4 (Phase 6)**: Depends on US1 and US2; query and context-pack slices are independent.
- **US5 (Phase 7)**: Depends on US1; session, place, and run-guide slices are independent except place work also depends on T017.
- **US6 (Phase 8)**: Depends on US1; ingest, capture, and update slices are independent.
- **US7 (Phase 9)**: Depends on US1–US6 and compares replay against T003 baselines.
- **Polish (Phase 10)**: Depends on every desired story; T054 runs last.

### User Story Completion Order

```text
Setup → Foundation → US1
                   ├→ US2 → US3
                   ├→ US2 → US4
                   ├→ US2 → US5
                   └→ US6
US1 + US2 + US3 + US4 + US5 + US6 → US7 → Polish
```

### Within Each User Story

- Behavioral or public-seam tests are written first and observed failing before implementation.
- Shared authority and public contracts stabilize before owner-local guidance consumes them.
- Each owner slice runs its focused cold evaluation after its guidance changes.
- A phase closes only at its stated independent-test boundary.

## Parallel Execution Examples

### User Story 1

```text
T008 owner cold cases || T009 contract examples
```

### User Story 2

```text
T012 query/lint cases || T013 faction/place cases
T014 query || T015 lint || T016 faction || T017 place
```

### User Story 3

```text
T019 public CLI tests || T020 cold lint cases
T022 CLI contract || T023 CLI data model after T021
```

### User Story 4

```text
T026 query cases || T027 context-pack cases
T028 query guidance || T029 context-pack guidance
```

### User Story 5

```text
T031 session cases || T032 place cases || T033 run-guide cases
T034 session guidance || T035 place guidance || T036 run-guide guidance
```

### User Story 6

```text
T038 ingest cases || T039 capture cases || T040 update cases
T041 ingest guidance || T042 capture guidance || T043 update guidance
```

### User Story 7

```text
T047 blind semantic review can proceed per completed pair while T046 continues remaining independent replays
```

## Implementation Strategy

### MVP First

1. Complete Setup and Foundational phases.
2. Complete US1.
3. Stop and validate US1 independently: successful branches reach owner guards; stalled branches produce complete specific blockers; no equivalent action repeats.

### Incremental Delivery

1. Land US2 guard coherence before trusting further evidence.
2. Land US3 as the deterministic proof at the existing CLI seam.
3. Land independent US4, US5, and US6 owner slices after their prerequisites.
4. Complete US7 paired promotion only after all selected owner slices pass.
5. Run cross-cutting verification and remove scratch artifacts.

### Parallel Team Strategy

- One writer owns each shared authority or contract file.
- Disjoint owner skill/eval pairs may proceed in parallel after their common predecessor stabilizes.
- No parallel wave writes the same canonical file, including `quickstart.md`.

## Notes

- `[P]` means disjoint files and no dependency on unfinished tasks.
- Every trajectory record remains evaluation evidence, never runtime execution state.
- No new dependency, orchestrator, registry, workflow engine, ledger, progress command, or persistent loop state is permitted.
- Campaign pages and unrelated templates, validation rules, skills, and generated Spec Kit adapters remain unchanged absent demonstrated in-scope failure.
