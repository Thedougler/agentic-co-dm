---

description: "Task list for Agent-Shaped Wiki CLI"
---

# Tasks: Agent-Shaped Wiki CLI

**Input**: Design documents from `/specs/027-wiki-agent-cli/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/wiki-cli.md`, `quickstart.md`

**Tests**: Behavioral pytest coverage is required by the feature specification and constitution; tests target the public CLI seam and the quickstart scenarios.

**Organization**: Tasks are grouped by prioritized user story so each increment is independently implementable and testable.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the new command surface and behavioral-test file without changing the existing creative lint command.

- [X] T001 [P] Create the executable `scripts/wiki` command entrypoint and preserve `scripts/wiki-lint` as the creative-lint surface
- [X] T002 [P] Create the subprocess/temp-vault behavioral test harness in `tests/test_wiki_cli.py` using the fixture conventions from `tests/test_wiki_ops.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement shared invocation, vault resolution, path scoping, output emission, and fail-closed errors required by every subcommand.

**CRITICAL**: No user-story implementation can begin until this phase is complete.

- [X] T003 Implement shared argparse dispatch, configured-vault resolution, vault-relative file/prefix union, and unknown/out-of-vault rejection in `scripts/wiki`; emit one compact `{"status":"error","error":"<message>"}` object on stdout with exit 2 unless `--pretty` is selected

**Checkpoint**: `scripts/wiki` has one command surface, existing vault configuration is authoritative, zero paths mean the whole vault, and scope validation fails before any wiki scan.

---

## Phase 3: User Story 1 - Agent lints a path and gets a worklist (Priority: P1) 🎯 MVP

**Goal**: Make `wiki lint` return a compact, directly actionable worklist for one file, a prefix, or the whole configured vault.

**Independent Test**: In a temp vault, lint a directory and one file; assert required worklist keys, no nested findings on bulk default, flat 1-based findings for one file, complete findings with `--full`, and structured exit-2 failure for an unknown path.

### Tests for User Story 1

- [X] T004 [US1] Add public-contract tests for bulk worklist, single-file findings, `--full`, unknown-path fail-closed behavior, `--json` no-op, and compact default output in `tests/test_wiki_cli.py`

### Implementation for User Story 1

- [X] T005 [P] [US1] Implement worklist aggregation in `tools/wiki_ops/worklist.py` with `status`, `counts`, `hard_fail`, `unique`, `backlog`, `next_page`, `cache`, `files_checked`, and `scope`; dedupe existing finding targets, sort backlog by bytes then path, and omit findings arrays for bulk default
- [X] T006 [US1] Implement structural lint execution in `scripts/wiki` by composing `tools/lint_wiki.py` with Vale/template defaults and `--hard`, `--all`, `--no-vale`, and `--no-template` overrides while preserving exit codes 0, 1, and 2
- [X] T007 [US1] Add single-existing-file flat findings and `--full` dump wiring in `scripts/wiki`, preserving `rule`, vault-relative `file`, 1-based integer `line`, `severity`, and `message` from `specs/027-wiki-agent-cli/contracts/wiki-cli.md`

**Checkpoint**: User Story 1 is independently runnable through `scripts/wiki lint`; bulk output is a worklist and single-file output is line-addressable.

---

## Phase 4: User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

**Goal**: Reuse unchanged per-file checker results while rebuilding corpus facts from current files and cached extracts.

**Independent Test**: Run identical whole-vault lint twice and assert cache hits plus Vale skips; modify one page and assert only that page misses; verify checker overrides skip only their selected checkers.

### Tests for User Story 2

- [X] T008 [US2] Add cache tests for identical reruns, one-file content invalidation, checker-configuration invalidation, corpus refresh after file-set changes, and `--no-vale`/`--no-template` behavior in `tests/test_wiki_cli.py`

### Implementation for User Story 2

- [X] T009 [US2] Implement `$VAULT/_meta/lint-cache.json` load/save and per-file cache records in `tools/wiki_ops/lint_cache.py` with `content_sha256`, `config_digest`, `extracts`, and `results`; invalidate changed content/configuration and drop missing paths
- [X] T010 [US2] Integrate cache hits, misses, and `vale_skipped` accounting into `scripts/wiki`, reusing unchanged checker results while rebuilding links, missing owners, and other corpus facts from current paths plus cached extracts

**Checkpoint**: User Story 2 is independently demonstrated by second-run cache metrics and selective rechecking.

---

## Phase 5: User Story 3 - Agent queries the wiki with one phrase (Priority: P2)

**Goal**: Make `wiki query <phrase>` run retrieval in agent environments and return compact capped hits with overridable collection and count.

**Independent Test**: With a fake or available qmd backend, query a known title without flags and assert `status`, default collection `wiki`, at most ten hits, and only `title`, vault-relative `path`, and retrieval `id`; assert overrides, zero-hit success, and structured backend failure.

### Tests for User Story 3

- [X] T011 [US3] Add query contract tests for `CI=true` retrieval, default collection/cap, collection and `-n` overrides, compact hit fields, zero-hit success, and backend failure in `tests/test_wiki_cli.py`

### Implementation for User Story 3

- [X] T012 [US3] Implement `wiki query` in `scripts/wiki` by invoking `env -u CI qmd query <phrase> -c <collection> -n <cap> --format json`, defaulting to `wiki` and 10, compacting hits to `title`, vault-relative `path`, and retrieval `id`, and routing failures to structured exit-2 errors

**Checkpoint**: User Story 3 is independently usable with one phrase and no environment or backend flags supplied by the caller.

---

## Phase 6: User Story 4 - One health snapshot for wiki fitness (Priority: P2)

**Goal**: Make `wiki health` expose live lint, inventory, Layer A maintenance metrics, compact tracker trends, ordered focus, and one next action while retaining the historical report alias.

**Independent Test**: Compare `scripts/wiki health` and `scripts/wiki-maintain --report` against the same configured/temp vault; assert pages, bytes, tokens, lint worklist/cache, waste, staging, remorph, policy, trends, bounded `focus`, and `next`, with no per-step essays or full findings dump.

### Tests for User Story 4

- [X] T013 [US4] Add health snapshot and alias-equality tests for inventory, lint hard totals/cache, Layer A fields, sitting/skill/error/efficiency trend aggregates, bounded focus ordering, `next == focus[0]`, exit status, and absence of findings/steps/raw tracker rows in `tests/test_wiki_cli.py`

### Implementation for User Story 4

- [X] T014 [US4] Implement health snapshot assembly, existing Layer A composition, retained-tracker trend aggregation, and bounded focus/next selection in `tools/wiki_ops/health.py` according to `specs/027-wiki-agent-cli/data-model.md`; scope inventory/lint/focus by paths, keep trends whole-tracker, cap focus at 5, and never invent layout paths
- [X] T015 [US4] Wire `wiki health` in `scripts/wiki` to count live markdown pages/bytes, obtain tokens through `scripts/token-count.py`, embed the cached lint worklist without findings, and emit the `specs/027-wiki-agent-cli/data-model.md` health shape
- [X] T016 [US4] Change `scripts/wiki-maintain` `--report` handling to delegate to `scripts/wiki health` and preserve an identical compact snapshot plus exit codes 0, 1, and 2

**Checkpoint**: User Story 4 is independently verified by snapshot equality between the new and historical invocations and by a small agent acting on `next`.

---

## Phase 7: User Story 5 - Human pretty output on request (Priority: P3)

**Goal**: Make `--pretty` the explicit human-readable surface while default output remains compact structured JSON regardless of TTY state.

**Independent Test**: Run lint, query, and health with and without `--pretty` in an interactive-like subprocess; assert default one-object JSON, requested text, findings lines for `--pretty --full`, and one-line stderr usage errors.

### Tests for User Story 5

- [X] T017 [US5] Add pretty-output tests for lint scoreboards/findings, query hit lines, health scoreboard/focus, TTY-independent defaults, and pretty usage errors in `tests/test_wiki_cli.py`

### Implementation for User Story 5

- [X] T018 [P] [US5] Implement lint, query, and health text renderers in `tools/wiki_ops/pretty.py` for scoreboards, `file:line  RULE  message`, `path  title  id`, and short health metrics without dumping machine JSON
- [X] T019 [US5] Wire `--pretty` and accepted no-op `--json` through `scripts/wiki`, including stderr-only one-line usage errors and preservation of machine stdout errors when `--pretty` is absent

**Checkpoint**: User Story 5 is independently usable by operators without changing any agent default contract.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Synchronize agent guidance, preserve the creative-lint boundary, and validate the complete feature against real contracts.

- [X] T020 [P] Update structural lint and bulk-repair examples to `scripts/wiki lint` and the default worklist contract in `.agents/skills/wiki-lint/SKILL.md`
- [X] T021 [P] Update pinned lint evaluations from `./scripts/wiki-lint --json wiki/` to the new structural command while retaining creative-lint examples in `.agents/skills/wiki-lint/evals/evals.json`
- [X] T022 [P] Update standing lint/query/health command routing and examples to `scripts/wiki` in `AGENTS.md` and `.omp/AGENTS.md`, including health `next`/`focus` action guidance without changing creative-lint or wiki-query synthesis ownership
- [X] T023 Run `.venv/bin/python -m pytest tests/test_wiki_cli.py -q` and the documented scenarios in `specs/027-wiki-agent-cli/quickstart.md`, including the live-vault bulk-size check
- [X] T024 Validate agent-facing command guidance with the cold-context smol scenario in `specs/027-wiki-agent-cli/quickstart.md`, confirming a small agent can lint one file and name `next_page` without parsing nested finding maps

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 and T002 can run in parallel; both precede shared dispatch work.
- **Foundational (Phase 2)**: T003 depends on T001 and blocks every user story.
- **User Stories (Phases 3–7)**: Each story depends on T003. US2 depends on US1 lint/worklist behavior; US4 depends on US1 and US2 because health shares the live lint/cache path; US5 depends on the result shapes from US1, US3, and US4. US3 can proceed in parallel with US1/US2 after T003.
- **Polish (Phase 8)**: T020–T022 can run in parallel after the command contract is stable; T023 depends on implementation stories; T024 depends on the synchronized command guidance and complete contract.

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Foundational; no other story dependency. MVP.
- **User Story 2 (P1)**: Depends on US1's lint/worklist seam so cache metrics are public.
- **User Story 3 (P2)**: Depends only on Foundational; independent of lint and health.
- **User Story 4 (P2)**: Depends on US1 and US2 for the live lint worklist and shared cache.
- **User Story 5 (P3)**: Depends on lint, query, and health result contracts from US1, US3, and US4.

### Within Each User Story

- Public behavior tests are written before their implementation tasks.
- Result helpers/data shaping precede command wiring.
- Existing checker, token, qmd, and Layer A owners remain composed rather than duplicated.
- A story is complete only when its independent test criteria pass.

### Parallel Opportunities

- **Setup**: T001 and T002.
- **After T003**: US1 and US3 are independent workstreams; serialize edits to the shared `scripts/wiki` file or assign one integration owner.
- **Within US1**: T004 and T005 can proceed in parallel because the test contract and worklist helper touch different files; T006/T007 follow the worklist contract.
- **Within US4/US5**: T014 can be developed before T015; T018 can be developed before T019; no parallel edits to `scripts/wiki` or `scripts/wiki-maintain`.
- **Polish**: T020, T021, and T022 touch separate instruction/evaluation files and can run in parallel.

---

## Parallel Examples by User Story

### User Story 1

```text
T004: Add worklist contract tests in tests/test_wiki_cli.py
T005: Implement worklist aggregation in tools/wiki_ops/worklist.py
```

### User Story 2

```text
T008: Add cache behavior tests in tests/test_wiki_cli.py
T009: Implement cache records in tools/wiki_ops/lint_cache.py after the test contract is fixed
```

### User Story 3

```text
T011: Add query contract tests in tests/test_wiki_cli.py
T012: Implement qmd retrieval in scripts/wiki after the test contract is fixed
```

### User Story 4

```text
T013: Add health and alias contract tests in tests/test_wiki_cli.py
T014: Implement snapshot/trend/focus shaping in tools/wiki_ops/health.py
```

### User Story 5

```text
T017: Add pretty-output contract tests in tests/test_wiki_cli.py
T018: Implement renderers in tools/wiki_ops/pretty.py
```

### Cross-Story Example

```text
After T003:
- US1: scripts/wiki lint + tools/wiki_ops/worklist.py
- US3: scripts/wiki query (serialize shared scripts/wiki edits)
- Polish: instruction/evaluation updates in .agents/skills/wiki-lint/ and AGENTS.md
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational dispatch and fail-closed scope.
3. Complete Phase 3: User Story 1 worklist and single-file findings.
4. Validate bulk, single-file, `--full`, and unknown-path behavior independently.
5. Stop at the MVP checkpoint before adding cache, query, health, or pretty output.

### Incremental Delivery

1. Add User Story 2 cache reuse and invalidation; validate second-run behavior.
2. Add User Story 3 query retrieval; validate defaults, overrides, zero hits, and backend errors.
3. Add User Story 4 health, trends, focus/next, and the historical alias; validate identical snapshots.
4. Add User Story 5 explicit pretty output; validate machine output remains unchanged.
5. Synchronize instructions/evals and run quickstart plus cold-agent validation.

### Notes

- `[P]` marks only tasks that can proceed in parallel without sharing an incomplete file change.
- `[US#]` maps story tasks to the prioritized stories in `spec.md`.
- Existing `scripts/wiki-lint` creative operations remain out of scope for the dispatcher.
