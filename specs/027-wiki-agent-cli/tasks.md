---
description: "Task list for 027 wiki agent CLI"
---

# Tasks: Agent-Shaped Wiki CLI

**Input**: Design documents from `/specs/027-wiki-agent-cli/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/wiki-cli.md, quickstart.md

**Tests**: pytest in `tests/test_wiki_cli.py` (constitution IV, plan). Not TDD-first.

**Organization**: By user story. Setup and Foundational have no story label.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete dependencies)
- **[Story]**: US1–US5 from spec.md
- Every task has a checkbox, ID, and file path

## Path Conventions

Repo root: `scripts/wiki`, `tools/wiki_ops/`, `tests/test_wiki_cli.py`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Empty helper modules and test file listed in plan.md

- [ ] T001 Create empty `tools/wiki_ops/worklist.py`, `tools/wiki_ops/lint_cache.py`, `tools/wiki_ops/health.py`, `tools/wiki_ops/timing.py`, `tools/wiki_ops/pretty.py`, and executable `scripts/wiki` (shebang `.venv`/repo python; docstring only)
- [ ] T002 Create `tests/test_wiki_cli.py` with a temp-vault helper matching `tests/test_wiki_ops.py` (no cases yet)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Dispatcher, fail-closed paths, timing/command records. Blocks all stories.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [ ] T003 Implement vault-relative path resolve in `scripts/wiki`: zero args = whole vault; several args = union; unknown or out-of-vault path → stdout `{"error":"<message>","status":"error"}` exit 2, no scan, no fuzzy match (`tools/wiki_ops/cli.py` `configured_vault` / `emit_error`)
- [ ] T004 [P] Extend `scripts/efficiency-trace.py` `validate_record` to accept `record_kind: command` with fields `schema_version`, `command` (`lint` \| `query` \| `health`), `duration_ms`, `cache_hits`, `cache_misses`, `vale_skipped`, `exit`, `timestamp`; sitting `report`/`promote` ignore command rows; implement append + stdout `timing` (`command`, `duration_ms`, `cache` when lint/health) in `tools/wiki_ops/timing.py` (append failure must not change wiki exit code)
- [ ] T005 Add argparse in `scripts/wiki` for `lint|query|health`, flags `--pretty --json --full --hard --all --no-vale --no-template`, `--collection`/`-n` on query; `--json` ignored; default stdout one compact JSON object via `emit_json` (`sort_keys=True`, no indent); exit 0/1/2 per `specs/027-wiki-agent-cli/contracts/wiki-cli.md`

**Checkpoint**: `scripts/wiki lint nosuch` exits 2 with `status=error`. Timing helper exists.

---

## Phase 3: User Story 1 - Agent lints a path and gets every finding, grouped by file (Priority: P1) 🎯 MVP

**Goal**: `scripts/wiki lint` returns summary fields plus complete Vale-included findings grouped by file.

**Independent Test**: Lint a directory, one page, and two named pages. Each result includes `files` groups with 1-based `line`, plus `unique` / `next_page`. Unknown path exits 2.

### Implementation for User Story 1

- [ ] T006 [US1] Implement lint summary + dump in `tools/wiki_ops/worklist.py`: required keys `status` (`clean` \| `findings` \| `error`), `counts`, `hard_fail`, `unique` (already-deduped targets per rule), `backlog` (`page`, `findings`, `bytes`; sort bytes then path), `next_page` (`backlog[0].page` or null), `cache`, `files_checked`, `scope` (`paths`; `[]` = whole vault), `files` (array of `{file, findings}` in argument/path order; omit zero-finding groups); each finding `{rule, file, line, severity, message}` with 1-based `line`; MUST NOT contain nested per-rule finding maps; compose existing `tools/lint_wiki.py` (Vale included unless `--no-vale`)
- [ ] T007 [US1] Wire `lint` in `scripts/wiki` to `worklist.py` + `timing.py`: `--full` accepted and MUST NOT add or remove keys; `--hard` default; two named files → two `files` entries when both have findings
- [ ] T008 [US1] Add pytest in `tests/test_wiki_cli.py` for prefix dump, two-file `files` blocks, `--full` no-op, unknown path <1s exit 2, no nested per-rule maps, `timing.command == "lint"`

**Checkpoint**: `scripts/wiki lint entities/npc` dumps per-file findings. MVP.

---

## Phase 4: User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

**Goal**: Second lint does not re-run checkers on unchanged file bytes + checker config.

**Independent Test**: Lint twice; `cache.hits` > 0; Vale skipped on unchanged pages. Change one file; that path misses.

### Implementation for User Story 2

- [ ] T009 [US2] Implement `$VAULT/_meta/lint-cache.json` in `tools/wiki_ops/lint_cache.py`: key = content sha256 of file bytes + `config_digest`; hit reuses `extracts` and `results`; miss on hash change, config change, or new path; drop deleted paths; rebuild corpus facts from current path set + extracts
- [ ] T010 [US2] Wire cache into `tools/wiki_ops/worklist.py` and `scripts/wiki` lint; populate `cache.hits`, `cache.misses`, `cache.vale_skipped`
- [ ] T011 [US2] Add pytest in `tests/test_wiki_cli.py` for second-run hits, byte-change miss, config-digest miss

**Checkpoint**: Second identical lint skips Vale on cached pages.

---

## Phase 5: User Story 3 - Agent queries the wiki with one phrase (Priority: P2)

**Goal**: `scripts/wiki query <phrase>` returns compact hits without the agent unsetting CI.

**Independent Test**: `CI=true scripts/wiki query "<known title>"` returns `{title, path, id}` hits. Backend down → exit 2, no invented hits.

### Implementation for User Story 3

- [ ] T012 [US3] Implement `query` in `scripts/wiki`: run `env -u CI qmd query <phrase> -c <collection> -n <cap> --format json`; default collection `wiki`, cap 10; stdout `{status, collection, hits, timing}` where `hits` is `{title, path, id}[]` (no snippets); backend missing/failing → `status=error` exit 2, no invented hits
- [ ] T013 [US3] Add pytest in `tests/test_wiki_cli.py` for compact hits (mocked qmd) and backend-failure exit 2

**Checkpoint**: Query works with `CI=true`. Independent of lint dump.

---

## Phase 6: User Story 4 - One health snapshot for wiki fitness (Priority: P2)

**Goal**: `scripts/wiki health` is inventory + lint summary + Layer A + trends (slowest commands, token-heaviest) + `focus`/`next`. No findings dump.

**Independent Test**: One object with `pages`, `bytes`, `tokens`, lint hard-total, `trends.slowest_commands`, `trends.token_heaviest`, `focus`, `next`. `wiki-maintain --report` identical. Small agent can name `next.path`. After two wiki runs, slowest command is named.

### Implementation for User Story 4

- [ ] T014 [US4] Implement snapshot in `tools/wiki_ops/health.py`: live lint **summary** (same cache, **no `files` dump**); `pages`, `bytes`, `tokens` (tiktoken via `scripts/token-count.py`); Layer A `waste` (`hits`, `hard_hits`), `staging.leftover_count`, `remorph` (`plan_count`, `skip_count`, `error_count`), `policy` (`ok`, `conflict_count`); `trends.sittings`, `trends.skills` (usage names cap 5, not evals), `trends.errors` (open only, causes cap 3), `trends.efficiency` sitting subset, `trends.slowest_commands` cap 3 from `record_kind=command`, `trends.token_heaviest` cap 3 (`tokens` = sum of trajectory fields); `focus` ordered cap 5 (`path`, `reason`, `source` `lint` \| `remorph` \| `layout` \| `tracker`); `next` is `focus[0]` or null; MUST NOT include skill-eval pass/fail, missing-skill inventories, raw traces, or per-step essays; missing trackers → zero/empty trends, not exit 2
- [ ] T015 [US4] Wire `health` in `scripts/wiki` and make `scripts/wiki-maintain --report` emit the identical snapshot; path args scope `pages`/`bytes`/`tokens`/`lint`/`focus`; `trends` always whole-tracker
- [ ] T016 [US4] Add pytest in `tests/test_wiki_cli.py` for alias equality, no `files` dump, empty-tracker zeros, `len(focus) <= 5`, `next is focus[0] or None`, slowest-command rank after two timed runs, token-heaviest from a sitting fixture, no skill-eval keys

**Checkpoint**: Health is compact and actionable via `next`.

---

## Phase 7: User Story 5 - Human pretty output on request (Priority: P3)

**Goal**: `--pretty` is the only human text. Default never TTY-detects.

**Independent Test**: Interactive terminal without `--pretty` still compact JSON. `--pretty` is scoreboard + grouped `file:line  RULE  message`. Pretty usage error is one stderr line exit 2.

### Implementation for User Story 5

- [ ] T017 [US5] Implement `--pretty` in `tools/wiki_ops/pretty.py` and `scripts/wiki`: lint scoreboard plus `file:line  RULE  message` grouped by file; query one line `path  title  id`; health scoreboard (pages, bytes, tokens, lint hard total, slowest command, token-heaviest sitting) then `next.path` and `focus` as `path  source  reason`; `--pretty --full` is the same human findings list; pretty usage errors one line on stderr exit 2; no `isatty()`
- [ ] T018 [US5] Add pytest in `tests/test_wiki_cli.py` for default JSON vs `--pretty` text, `--pretty --full` same list, pretty error on stderr

**Checkpoint**: Default stays machine JSON.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: FR-018 instruction retarget; quickstart; agent standards

- [ ] T019 Replace structural lint/query/health examples with `scripts/wiki` in `.agents/skills/wiki-lint/SKILL.md`, `.agents/skills/wiki-lint/evals/evals.json`, `.agents/skills/wiki-query/SKILL.md` (synthesis stays; retrieval examples → `wiki query`), `.agents/skills/wiki-status/SKILL.md` if present, and standing examples in `AGENTS.md` / `.omp/AGENTS.md`: run `scripts/wiki health`, then act on `next` (then remaining `focus`) without a DM wait
- [ ] T020 Run `.venv/bin/python scripts/check-agent-standards.py` until AGENT001–003 are green
- [ ] T021 Run cold-context smol subject for SC-008 (names a finding line + `next_page`) and SC-009 (names `next.path`) per `specs/027-wiki-agent-cli/quickstart.md` V-008/V-009
- [ ] T022 Run `.venv/bin/python -m pytest tests/test_wiki_cli.py -q` and the runnable quickstart V-001–V-007, V-010 checks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Immediate
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After US1 (cache wraps lint)
- **US3 (Phase 5)**: After Foundational — parallel with US1
- **US4 (Phase 6)**: After US1 + US2 (live lint summary + same cache)
- **US5 (Phase 7)**: After US1, US3, US4 (pretty all three subcommands)
- **Polish (Phase 8)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P1)**: After US1
- **US3 (P2)**: After Phase 2; independent of US1
- **US4 (P2)**: After US1 + US2
- **US5 (P3)**: After US1 + US3 + US4

### Parallel Opportunities

- T004 parallel with T003 (different files)
- After Phase 2: US1 and US3 in parallel
- T019 file edits are sequential on shared instruction files (not [P])

---

## Parallel Example: After Foundational

```text
# Story A
T006–T008 US1 lint dump in tools/wiki_ops/worklist.py + scripts/wiki + tests/test_wiki_cli.py

# Story B (same time, different files except tests/test_wiki_cli.py — serialize tests)
T012–T013 US3 query in scripts/wiki
```

Serialize `tests/test_wiki_cli.py` writes.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational
3. Phase 3 US1
4. **STOP**: `scripts/wiki lint entities/npc` dumps per-file findings

### Incremental Delivery

1. Setup + Foundational
2. US1 lint dump → MVP
3. US2 cache
4. US3 query (or parallel with US1)
5. US4 health
6. US5 pretty
7. Polish (skills, AGENT001–003, smol, pytest)

---

## Notes

- Do not migrate `scripts/wiki-lint` creative hydra
- Do not add npm wrappers
- Do not add a second benchmark file
- `focus` layout items only from existing remorph/layout plans
