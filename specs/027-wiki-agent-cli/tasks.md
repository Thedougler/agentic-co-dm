---

description: "Task list for Agent-Shaped Wiki CLI"
---

# Tasks: Agent-Shaped Wiki CLI

**Input**: Design documents from `/specs/027-wiki-agent-cli/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/wiki-cli.md, quickstart.md

**Tests**: Behavioral pytest coverage is required by the feature specification and constitution; tests target the public CLI seam.

**Organization**: Tasks are grouped by user story so each increment is independently implementable and testable.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the new command and isolated behavioral-test surface without changing the existing creative lint command.

- [ ] T001 [P] Create executable `scripts/wiki` entrypoint and `tools/wiki_ops/` helper module files per `specs/027-wiki-agent-cli/plan.md`, while preserving `scripts/wiki-lint` as the creative-lint surface
- [ ] T002 [P] Create subprocess/temp-vault test harness in `tests/test_wiki_cli.py` using the existing `tests/test_wiki_ops.py` fixture conventions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement shared invocation, configuration, scope, and error behavior required by every subcommand.

**CRITICAL**: No user-story implementation can begin until this phase is complete.

- [ ] T003 Implement shared argparse dispatch, configured-vault resolution, vault-relative file/prefix union, and fail-closed unknown/out-of-vault path handling in `scripts/wiki`, returning compact `{"status":"error","error":"<message>"}` on stdout with exit 2 unless `--pretty` is selected

**Checkpoint**: `scripts/wiki` has one command surface, existing vault configuration is authoritative, zero paths mean the whole vault, and no path scan occurs after scope validation fails.

---

## Phase 3: User Story 1 - Agent lints a path and gets a worklist (Priority: P1) 🎯 MVP

**Goal**: Make `wiki lint` return a compact, directly actionable worklist for one file, prefixes, or the whole configured vault.

**Independent Test**: In a temp vault, lint a directory and one file; assert required worklist keys, no nested findings on bulk default, flat 1-based findings for one file, complete findings with `--full`, and structured exit-2 failure for an unknown path.

### Tests for User Story 1

- [ ] T004 [US1] Add public-contract tests for bulk worklist, single-file findings, `--full`, unknown-path fail-closed behavior, `--json` no-op, and compact default output in `tests/test_wiki_cli.py`

### Implementation for User Story 1

- [ ] T005 [P] [US1] Implement worklist aggregation in `tools/wiki_ops/worklist.py`: required `status`, `counts`, `hard_fail`, `unique`, `backlog`, `next_page`, `cache`, `files_checked`, and `scope` fields; sorted unique existing finding targets only; backlog sorted by bytes then path; omit `findings` and `findings_by_file` for bulk default
- [ ] T006 [US1] Implement structural lint execution in `scripts/wiki` by composing `tools/lint_wiki.py` with Vale/template defaults and `--hard`/`--all`/`--no-vale`/`--no-template` overrides, preserving 0 clean, 1 findings, and 2 invocation/precondition exits
- [ ] T007 [US1] Add single-existing-file flat finding records and `--full` dump wiring in `scripts/wiki`, preserving `rule`, vault-relative `file`, 1-based integer `line`, `severity`, and `message` from `specs/027-wiki-agent-cli/contracts/wiki-cli.md`

**Checkpoint**: User Story 1 is independently runnable through `scripts/wiki lint`; bulk output is a worklist and single-file output is line-addressable.

---

## Phase 4: User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

**Goal**: Reuse unchanged per-file checker results while rebuilding corpus facts from current files and cached extracts.

**Independent Test**: Run identical whole-vault lint twice and assert cache hits plus Vale skips; modify one page and assert only that page misses; verify `--no-vale` and `--no-template` skip only their selected checkers.

### Tests for User Story 2

- [ ] T008 [US2] Add cache behavior tests for identical reruns, one-file content invalidation, checker-config invalidation, corpus refresh after file-set changes, and `--no-vale`/`--no-template` in `tests/test_wiki_cli.py`

### Implementation for User Story 2

- [ ] T009 [US2] Implement `$VAULT/_meta/lint-cache.json` load/save and per-file cache records in `tools/wiki_ops/lint_cache.py` with `content_sha256`, `config_digest`, `extracts`, and `results`; invalidate content/config changes and drop missing paths
- [ ] T010 [US2] Integrate cache hits/misses and `vale_skipped` accounting into `scripts/wiki`, reusing checker results for unchanged bytes/configuration while rebuilding links, missing owners, and other corpus facts from current paths plus cached extracts

**Checkpoint**: User Story 2 is independently demonstrated by the second-run cache metrics and selective recheck behavior.

---

## Phase 5: User Story 3 - Agent queries the wiki with one phrase (Priority: P2)

**Goal**: Make `wiki query <phrase>` run retrieval in agent environments and return compact capped hits with overridable collection and count.

**Independent Test**: With a fake or available qmd backend, query a known title without extra flags and assert `status`, default `collection: "wiki"`, at most ten hits, and only `title`, vault-relative `path`, and retrieval `id`; assert overrides replace defaults and backend failure returns exit 2 without fake hits.

### Tests for User Story 3

- [ ] T011 [US3] Add query contract tests for `CI=true` retrieval, default collection/cap, collection and `-n` overrides, compact hit fields, zero-hit success, and backend failure in `tests/test_wiki_cli.py`

### Implementation for User Story 3

- [ ] T012 [US3] Implement `wiki query` in `scripts/wiki` by invoking `env -u CI qmd query <phrase> -c <collection> -n <cap> --format json`, defaulting to `wiki` and 10, compacting hits to `title`, vault-relative `path`, and qmd retrieval `id`, and routing failures to structured exit-2 errors

**Checkpoint**: User Story 3 is independently usable with one phrase and no environment or backend flags supplied by the caller.

---

## Phase 6: User Story 4 - One health snapshot for wiki fitness (Priority: P2)

**Goal**: Make `wiki health` expose live lint, inventory, and existing Layer A maintenance metrics in one snapshot, while retaining the historical report alias.

**Independent Test**: Compare `scripts/wiki health` and `scripts/wiki-maintain --report` against the same configured/temp vault; assert pages, bytes, tokens, lint worklist/cache, waste, staging, remorph, and policy metrics without per-step essays or a full findings dump.

### Tests for User Story 4

- [ ] T013 [US4] Add health snapshot and alias-equality tests for inventory metrics, lint hard totals/cache, Layer A fields, exit status, no findings dump, and no per-step essay in `tests/test_wiki_cli.py`

### Implementation for User Story 4

- [ ] T014 [US4] Implement health snapshot assembly in `scripts/wiki`, counting live markdown pages and bytes, obtaining tokens through `scripts/token-count.py`, embedding the lint worklist without findings, and promoting existing Layer A waste/staging/remorph/policy metrics into the `specs/027-wiki-agent-cli/data-model.md` shape
- [ ] T015 [US4] Change `scripts/wiki-maintain --report` to delegate to the `scripts/wiki health` implementation and emit the identical compact snapshot and 0/1/2 status contract without maintaining a second counter

**Checkpoint**: User Story 4 is independently verified by snapshot equality between the new and historical invocations.

---

## Phase 7: User Story 5 - Human pretty output on request (Priority: P3)

**Goal**: Make `--pretty` the explicit human-readable surface while default output remains compact structured JSON regardless of TTY state.

**Independent Test**: Run lint, query, and health with and without `--pretty` in an interactive-like subprocess; assert default one-object JSON, scoreboard/text output for `--pretty`, findings lines for `--pretty --full`, and one-line stderr usage errors.

### Tests for User Story 5

- [ ] T016 [US5] Add pretty-output tests for lint scoreboard/findings, query hit lines, health scoreboard, TTY-independent defaults, and pretty usage errors in `tests/test_wiki_cli.py`

### Implementation for User Story 5

- [ ] T017 [P] [US5] Implement lint/query/health text renderers in `tools/wiki_ops/pretty.py`: scoreboards, `file:line  RULE  message`, `path  title  id`, and short health metrics without dumping machine JSON
- [ ] T018 [US5] Wire `--pretty` and accepted no-op `--json` through `scripts/wiki`, including stderr-only one-line usage errors and preservation of machine stdout errors when `--pretty` is absent

**Checkpoint**: User Story 5 is independently usable by operators without changing any agent default contract.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Synchronize instruction surfaces, preserve the creative-lint boundary, and validate the complete feature against its real contracts.

- [ ] T019 [P] Update structural lint and bulk-repair command examples to `scripts/wiki lint` and the default worklist contract in `.agents/skills/wiki-lint/SKILL.md`
- [ ] T020 [P] Update pinned agent-evaluation expectations from `./scripts/wiki-lint --json wiki/` to the new structural command while retaining creative-lint examples in `.agents/skills/wiki-lint/evals/evals.json`
- [ ] T021 [P] Update standing lint/query/health routing and command examples to `scripts/wiki` in `AGENTS.md` and `.omp/AGENTS.md` without changing creative-lint or wiki-query synthesis ownership
- [ ] T022 Run the public behavior suite and quickstart scenarios from `specs/027-wiki-agent-cli/quickstart.md`, including the live-vault bulk-size check, in `tests/test_wiki_cli.py` and the documented CLI commands
- [ ] T023 Validate the agent-facing command guidance with the cold-context smol scenario from `specs/027-wiki-agent-cli/quickstart.md`, confirming an agent can lint one file and name `next_page` without parsing nested finding maps

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 and T002 can run in parallel; both precede shared dispatch work.
- **Foundational (Phase 2)**: T003 depends on T001 and blocks every user story.
- **User Stories (Phases 3–7)**: Each story depends on T003. US2 depends on US1 lint/worklist behavior; US4 depends on US2 cache behavior because health must share the same cache; US5 depends on the result shapes from US1, US3, and US4. US3 can proceed in parallel with US1 after T003.
- **Polish (Phase 8)**: T019–T021 can run in parallel after the command contract is stable; T022 depends on all implementation stories; T023 depends on instruction updates and the complete command contract.

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Foundational; no other story dependency. MVP.
- **User Story 2 (P1)**: Depends on US1's lint/worklist seam so cache metrics are part of the public result.
- **User Story 3 (P2)**: Depends only on Foundational; can run in parallel with US1/US2.
- **User Story 4 (P2)**: Depends on US1 and US2 for the live lint worklist and shared cache.
- **User Story 5 (P3)**: Depends on the lint, query, and health result contracts from US1, US3, and US4.

### Within Each User Story

- Public behavior tests are written before their implementation tasks.
- Helpers/data shaping precede command wiring.
- Existing checker, token, qmd, and Layer A owners remain composed rather than duplicated.
- A story is complete only when its independent test criteria pass.

### Parallel Opportunities

- **Setup**: T001 and T002.
- **After T003**: US1 and US3 are independent workstreams; their test tasks must still precede their implementations.
- **Within US1**: T005 can proceed in parallel with T004; T006/T007 depend on the worklist and test contract.
- **Polish**: T019, T020, and T021 touch separate instruction/evaluation files and can run in parallel.

---

## Parallel Example: User Story 1

```text
T004: Add worklist contract tests in tests/test_wiki_cli.py
T005: Implement worklist aggregation in tools/wiki_ops/worklist.py
```

## Parallel Example: User Story 3

```text
T011: Add query contract tests in tests/test_wiki_cli.py
T012: Implement retrieval wrapper in scripts/wiki
```

## Parallel Example: Cross-Story Work

```text
After T003:
- User Story 1: scripts/wiki lint + tools/wiki_ops/worklist.py
- User Story 3: scripts/wiki query (serialize changes with other scripts/wiki edits)
- Polish: instruction updates in .agents/skills/wiki-lint/SKILL.md and evals/evals.json
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

1. Add User Story 2 cache reuse and invalidation; validate the second-run contract.
2. Add User Story 3 query retrieval; validate defaults and overrides.
3. Add User Story 4 health and the historical alias; validate identical snapshots.
4. Add User Story 5 explicit pretty output; validate default machine output remains unchanged.
5. Synchronize instructions/evals and run quickstart plus cold-agent validation.

### Notes

- `[P]` marks only tasks that can proceed in parallel without sharing an incomplete file change.
- `[US#]` maps story tasks to the prioritized stories in `spec.md`.
- Existing `scripts/wiki-lint` creative operations remain out of scope for the dispatcher.
