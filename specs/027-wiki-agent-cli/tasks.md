---
description: "Task list for Agent-Shaped Wiki CLI"
---

# Tasks: Agent-Shaped Wiki CLI

**Input**: Design documents from `/specs/027-wiki-agent-cli/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/wiki-cli.md`, `quickstart.md`

**Tests**: Behavioral pytest coverage is required by the feature plan and Constitution IV. Cold-context agent checks cover SC-008, SC-009, and SC-017.

**Organization**: Tasks are grouped by prioritized user story. Setup and Foundational tasks have no story label.

## Format

Every implementation task uses `- [ ] [TaskID] [P?] [Story?] Description with an exact repository path`.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the single command surface and test seams before story work.

- [ ] T001 [P] Add the temporary-vault and subprocess fixtures needed by CLI behavior tests in `tests/test_wiki_cli.py`.
- [ ] T002 [P] Wire the executable `scripts/wiki` entrypoint to the existing repository Python runtime and command dispatcher in `scripts/wiki`.
- [ ] T003 [P] Define the feature module boundaries and imports for worklist, cache, health, timing, pretty output, and repair planning in `tools/wiki_ops/worklist.py`, `tools/wiki_ops/lint_cache.py`, `tools/wiki_ops/health.py`, `tools/wiki_ops/timing.py`, `tools/wiki_ops/pretty.py`, and `tools/wiki_ops/repair_plans.py`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared behavior required by every subcommand.

**Critical**: Complete this phase before user-story implementation.

- [ ] T004 Implement vault resolution and fail-closed vault-relative scope handling for zero paths, files, prefixes, unions, unknown paths, and out-of-vault paths in `tools/wiki_ops/cli.py` and `scripts/wiki`.
- [ ] T005 Implement shared compact JSON/error emission and explicit `--pretty`, `--full`, and ignored `--json` argument handling in `tools/wiki_ops/cli.py`, `tools/wiki_ops/pretty.py`, and `scripts/wiki`.
- [ ] T006 Extend command timing records and 10-second stderr heartbeats without changing command exit semantics in `tools/wiki_ops/timing.py`, `scripts/efficiency-trace.py`, and `scripts/wiki`.
- [ ] T007 [P] Add foundational CLI assertions for structured errors, exit code 2, timing fields, and trace-append failure tolerance in `tests/test_wiki_cli.py`.

**Checkpoint**: The dispatcher resolves scope safely, emits the shared result shape, and records command timing.

---

## Phase 3: User Story 1 - Agent gets a complete lint worklist (Priority: P1) MVP

**Goal**: Make `wiki lint` run every configured checker while returning aggregate counts and every detailed finding by default.

**Independent Test**: Run whole-vault, prefix, multi-file, single-file, unknown-path, and compatibility `--full` lint against a temporary vault; complete findings remain available by default, `next` selects the smallest dirty file, and unknown paths do not scan.

### Tests for User Story 1

- [ ] T008 [US1] Add behavioral coverage for whole-vault, prefix, multi-file, single-file, unknown-path, and default-complete lint contracts in `tests/test_wiki_cli.py`.

### Implementation for User Story 1

- [ ] T009 [US1] Route structural, template, creative, prose/Vale, and corpus findings through the public lint dispatcher without checker-suppression paths in `scripts/wiki`, `scripts/wiki-lint`, and `tools/wiki_ops/worklist.py`.
- [ ] T010 [US1] Implement aggregate counts, complete finding totals, affected-page totals, cache/scope metadata, and actionable `next` selection by byte size then vault-relative path in `tools/wiki_ops/worklist.py`.
- [ ] T011 [US1] Implement flat 1-based detailed findings, `unique`, `backlog`, and per-file groups in the default result while accepting `--full` as a compatibility no-op in `tools/wiki_ops/worklist.py` and `scripts/wiki`.
- [ ] T012 [US1] Implement lint exit semantics and compact/pretty result rendering for clean, findings, and error states in `scripts/wiki` and `tools/wiki_ops/pretty.py`.

**Checkpoint**: User Story 1 is independently runnable through `scripts/wiki lint`; `scripts/wiki lint --full` is equivalent.

---

## Phase 4: User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

**Goal**: Reuse unchanged per-file checker results while rebuilding corpus facts from the current file set.

**Independent Test**: Lint the same temporary vault twice, then change one page and lint again; the second run reports hits and Vale skips, while the changed page and corpus facts miss correctly.

### Tests for User Story 2

- [ ] T013 [US2] Add cache-hit, Vale-skip, single-page invalidation, checker-configuration invalidation, and add/delete/rename corpus tests in `tests/test_wiki_cli.py`.

### Implementation for User Story 2

- [ ] T014 [US2] Implement versioned per-file cache entries with content hashes, resolved-template hashes, configuration digest invalidation, extracts, and checker results in `tools/wiki_ops/lint_cache.py`.
- [ ] T015 [US2] Integrate cache hits/misses, Vale skips, current path-set corpus rebuilds, and cache metadata into the lint orchestration in `scripts/wiki`, `tools/wiki_ops/worklist.py`, and `tools/wiki_ops/lint_cache.py`.

**Checkpoint**: User Stories 1 and 2 both work through the public lint command, with repeated work avoided safely.

---

## Phase 5: User Story 3 - Agent applies safe lint fixes (Priority: P1)

**Goal**: Apply only explicitly registered deterministic/idempotent repairs, rerun the same scope, and distinguish automatic work from manual findings.

**Independent Test**: Run `wiki lint fix` on one file, multiple files, a prefix, and the whole vault; registered fixes change only selected content, unsupported findings remain, and a second identical run is a no-op.

### Tests for User Story 3

- [ ] T016 [US3] Add registry eligibility, unsupported-finding preservation, precondition rejection, atomicity, changed-file reporting, and idempotence tests in `tests/test_wiki_ops.py`.
- [ ] T017 [US3] Add single-file, multi-file/prefix, whole-vault, post-fix rerun, and compact applied/skipped/remaining result tests in `tests/test_wiki_cli.py`.

### Implementation for User Story 3

- [ ] T018 [US3] Add an explicit fixer registry whose entries validate exact rule/action payloads, scope, deterministic preconditions, and idempotent outcomes; register only `delete_redirect_stub` initially in `tools/wiki_ops/repair_plans.py`.
- [ ] T019 [US3] Implement nested `lint fix` selection, scope-safe mutation planning, atomic hash-preconditioned application, and safe no-op handling through `scripts/wiki`, `tools/wiki_ops/repair_plans.py`, and `tools/wiki_ops/mutations.py`.
- [ ] T020 [US3] Implement post-fix scoped lint, applied/no-op/skipped records, changed-file aggregation, remaining findings, and fix exit semantics in `scripts/wiki` and `tools/wiki_ops/worklist.py`.

**Checkpoint**: User Story 3 is independently runnable through `scripts/wiki lint fix` without heuristic rewriting or unsafe cross-scope mutation.

---

## Phase 6: User Story 4 - Agent queries the wiki with one phrase (Priority: P2)

**Goal**: Provide compact retrieval with safe defaults and explicit collection/count overrides.

**Independent Test**: Run a known-title query without flags, with collection/count overrides, and with a failing backend; results are compact and failures contain no invented hits.

### Tests for User Story 4

- [ ] T021 [US4] Add default collection/count, CI-environment retrieval, override, compact-hit, zero-hit, and backend-failure tests in `tests/test_wiki_cli.py`.

### Implementation for User Story 4

- [ ] T022 [US4] Implement `wiki query <phrase>` retrieval with collection `wiki`, cap 10, environment-safe qmd invocation, and `{title, path, id}` hits in `scripts/wiki` and `tools/wiki_ops/cli.py`.
- [ ] T023 [US4] Implement query argument validation, structured backend errors, query timing records, and query pretty output integration in `scripts/wiki`, `tools/wiki_ops/timing.py`, and `tools/wiki_ops/pretty.py`.

**Checkpoint**: User Story 4 is independently runnable through `scripts/wiki query` with no manual environment preparation.

---

## Phase 7: User Story 5 - One health snapshot for wiki fitness (Priority: P2)

**Goal**: Compose live lint, inventory, Layer A maintenance, compact trends, bounded focus, and one actionable next item.

**Independent Test**: Run `wiki health` with populated and empty trackers, verify the maintenance alias is identical, and give only the health object to a small agent that names `next.path` and its reason.

### Tests for User Story 5

- [ ] T024 [US5] Add health inventory, live-lint/cache reuse, empty-tracker, trend-ranking, focus-order, next, alias, and bounded-output tests in `tests/test_wiki_cli.py`.

### Implementation for User Story 5

- [ ] T025 [US5] Implement the health snapshot composition for page count, bytes, tokens, live lint, cache, Layer A fields, focus, next, context, and timing in `tools/wiki_ops/health.py` and `scripts/wiki`.
- [ ] T026 [US5] Add compact sitting, error, command-speed, token-heavy, and first-turn context aggregates while excluding raw rows and skill-eval results in `tools/wiki_ops/health.py`, `scripts/efficiency-trace.py`, and `scripts/context-waste-scan.py`.
- [ ] T027 [US5] Preserve `scripts/wiki-maintain --report` as an identical health alias and enforce focus source/order/cap and `next = focus[0]` in `scripts/wiki-maintain`, `tools/wiki_ops/health.py`, and `scripts/wiki`.

**Checkpoint**: User Story 5 is independently runnable through `scripts/wiki health` and the legacy report alias.

---

## Phase 8: User Story 6 - Human pretty output on request (Priority: P3)

**Goal**: Make human-readable output explicit without terminal detection or accidental text for agents.

**Independent Test**: Run lint, query, and health with and without `--pretty` in an interactive terminal; default stdout stays compact structured output and pretty output is readable text with the specified grouping.

### Tests for User Story 6

- [ ] T028 [US6] Add interactive/default/pretty/pretty-full rendering and stderr usage-error tests in `tests/test_wiki_cli.py`.

### Implementation for User Story 6

- [ ] T029 [US6] Implement lint scoreboard and grouped `file:line  RULE  message` rendering, including `--full`, in `tools/wiki_ops/pretty.py` and `scripts/wiki`.
- [ ] T030 [US6] Implement one-hit-per-line query rendering, health scoreboard/focus rendering, and one-line pretty usage errors without TTY branching in `tools/wiki_ops/pretty.py` and `scripts/wiki`.

**Checkpoint**: All six user stories are independently observable through the one `scripts/wiki` command.

---

## Phase 9: Polish and Cross-Cutting Concerns

**Purpose**: Synchronize agent guidance, validate real surfaces, and close the feature against the design artifacts.

- [ ] T031 [P] Update the canonical lint, status, ingest, recap, and standing command guidance to teach one whole-vault `wiki lint fix`, then manual one-file `wiki lint <next.path>` repair and `wiki health` followed by `next` in `.agents/skills/wiki-lint/SKILL.md`, `.agents/skills/wiki-lint/evals/evals.json`, `.agents/skills/wiki-status/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/session-recap/SKILL.md`, and `AGENTS.md`.
- [ ] T032 [P] Synchronize equivalent lint guidance in `.kiro/skills/wiki-lint/SKILL.md`, `.pi/skills/wiki-lint/SKILL.md`, `.windsurf/skills/wiki-lint/SKILL.md`, and `.cursor/skills/wiki-lint/SKILL.md`.
- [ ] T033 [P] Add or update the public command and fix-result contract references in `docs/cli.md` and `specs/027-wiki-agent-cli/contracts/wiki-cli.md`.
- [ ] T034 Run the feature quickstart scenarios V-001 through V-011 and record any unavailable qmd/live-vault blocker in `specs/027-wiki-agent-cli/quickstart.md`.
- [ ] T035 Run focused behavioral coverage and the repository harness baseline from `tests/test_wiki_cli.py` and `scripts/check-omp-baseline.sh`.
- [ ] T036 Validate SC-008, SC-009, and SC-017 with cold, focused weakest-sufficient-model subjects using `.agents/skills/wiki-lint/evals/evals.json` and `specs/027-wiki-agent-cli/quickstart.md`.

---

## Dependencies and Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T001–T003 can proceed in parallel because they touch separate files.
- **Foundational (Phase 2)**: Depends on Setup; T004–T006 block all user stories, while T007 follows the shared seams.
- **US1 (Phase 3)**: Depends on Foundational; MVP lint surface.
- **US2 (Phase 4)**: Depends on US1 because cache wraps the completed lint orchestration.
- **US3 (Phase 5)**: Depends on US1 for findings and US2 for cache-safe post-fix reruns.
- **US4 (Phase 6)**: Depends on Foundational only; can proceed independently of lint stories after shared CLI seams exist.
- **US5 (Phase 7)**: Depends on US1 and US2 for live lint/cache; also consumes shared timing/tracker seams.
- **US6 (Phase 8)**: Depends on US1, US4, and US5 because it renders all three subcommands.
- **Polish (Phase 9)**: Depends on the stories being validated; documentation can proceed after the command contracts stabilize.

### User Story Dependencies

- **US1 (P1)**: Foundational only.
- **US2 (P1)**: US1.
- **US3 (P1)**: US1 and US2.
- **US4 (P2)**: Foundational only.
- **US5 (P2)**: US1 and US2.
- **US6 (P3)**: US1, US4, and US5.

### Parallel Opportunities

- T001–T003 can run in parallel during Setup.
- T004 and T005 can run in parallel; T006 depends on their shared dispatcher conventions.
- After Foundational, US1 and US4 can proceed in parallel; serialize edits to `tests/test_wiki_cli.py`.
- After US1, US2 and US3 can proceed in parallel only when their test-file edits are serialized; US3 consumes the completed lint result contract.
- T031–T033 can run in parallel because they touch disjoint guidance/contract files.

### Parallel Example: After Foundational

```text
Worker A: US1 T008–T012 — lint worklist in tools/wiki_ops/worklist.py and scripts/wiki
Worker B: US4 T021–T023 — query path in scripts/wiki and tools/wiki_ops/cli.py
Worker C: US2 T013–T015 — cache path after US1 contract is available
Worker D: US3 T016–T020 — fixer path after US1 findings are available

Serialize all writes to tests/test_wiki_cli.py; tests/test_wiki_ops.py is independent.
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 Setup.
2. Complete Phase 2 Foundational.
3. Complete Phase 3 User Story 1.
4. Run the independent US1 test and quickstart V-001–V-003/V-007 checks.
5. Stop at the compact lint worklist MVP before adding cache, repair, retrieval, health, or pretty surfaces.

### Incremental Delivery

1. Setup + Foundational → one safe dispatcher and shared result/error contract.
2. US1 → compact all-checker lint worklist MVP.
3. US2 → cache repeated lint work.
4. US3 → safe registered repairs and post-fix rerun.
5. US4 → compact qmd retrieval.
6. US5 → health snapshot and legacy alias.
7. US6 → explicit human rendering.
8. Polish → synchronized instructions, cold-agent validation, quickstart, and baseline checks.

### Notes

- Reuse existing vault resolution, checker backends, mutation atomicity, transaction seams, qmd CLI, efficiency tracker, and wiki templates; do not add dependencies.
- Do not make `--full` mutate, infer fixability from prose, guess owners, add fuzzy paths, add checker suppression flags, or create a second telemetry ledger.
- Every story task remains independently testable at `scripts/wiki`; documentation tasks do not replace behavioral validation.
