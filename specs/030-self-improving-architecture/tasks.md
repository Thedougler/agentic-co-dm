---

description: "Task list for feature 030: Self-Improving Architecture"
---

# Tasks: Self-Improving Architecture

**Input**: Design documents from `/specs/030-self-improving-architecture/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ (wiki-cli, error-ledger, eval-run), quickstart.md, checklists/

**Tests**: The spec asks for them. FR-011 requires a regression for every fixed failure, FR-021 an OMP checker test, and FR-039 one test per CLI rule class. Write each test first and confirm it fails before the fix.

**Organization**: Tasks are grouped by user story. Phase order is binding (spec Assumptions): Phase 1 = US1–US4, Phase 2 = US5–US7, Phase 3 = US8–US9.

**Open gaps**: The checklists and plan "Spec gaps" list gaps owned by Clarify, plus one contract conflict owned by Plan (checklists/wiki-cli.md CHK011). Where a gap applies, the task uses the plan default and says so with "Plan default:". spec.md and plan.md are not edited here.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US9)
- Paths are repo-relative (single repository, no new directories; plan "Structure Decision")

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Box environment and pre-change baselines that later parity checks diff against

- [ ] T001 Provision `.venv/` per quickstart.md "Prerequisites": `uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0 pytest`, then `export PATH="$PWD/.venv/bin:$PATH"` and `export OBSIDIAN_VAULT_PATH="$PWD/wiki"`. No tracked file changes.
- [ ] T002 Capture pre-change identity and lint baselines into `/tmp/030/`. Temporarily remove `CoDM` from `.vale.ini` in the working tree only, as in plan "Measurements taken". Write the V-06 `scan_identities` dump to `/tmp/030/identity-before.json` and whole-vault `scripts/wiki lint` findings to `/tmp/030/lint-before.json`. Then restore `.vale.ini`, `wiki/_meta/lint-cache.json`, and `styles/config/vocabularies/CoDM/accept.txt` with `git checkout --`.
- [ ] T003 [P] Record the pre-change test status: `pytest -q > /tmp/030/pytest-before.txt` (note any failures from the known Vale E100)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Confirm the dependencies the plan relies on before any story lands

- [ ] T004 Confirm that `.specify/memory/constitution.md` is v6.0.1 or later and that principle XIII allows fix-verify-continue (plan Constitution Check, "XIII … dependency met"). Stop and report if it does not, because this blocks US5 and US6.
- [ ] T005 Confirm the codex `--json` event names (research R5 "To verify"). Run `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/030/probe/iteration-1` and inspect `/tmp/030/probe/*/with_skill/run-1/events.jsonl` for `item.completed` (`command_execution`/`file_change`) and `turn.completed.usage`. Write the real names to `/tmp/030/event-names.txt` for T015.

**Checkpoint**: Environment, baselines, and event names are known, so the user stories can start

---

## Phase 3: User Story 1 - Green Baseline Checks (Priority: P1) 🎯 MVP

**Goal**: The OMP checker and scoped Vale lint pass on the correct config, and their ledger entries are drained

**Independent Test**: `scripts/check-omp-baseline.sh` passes on the current `.omp/config.yml`, and scoped `wiki lint` on one page shows no `CoDM` E100 (quickstart V-01–V-04)

### Tests for User Story 1

- [ ] T006 [P] [US1] Create `tests/test_omp_baseline.py` (FR-021, V-02). Run `scripts/check-omp-baseline.sh` against a temp copy of the repo files, once per config. `backend: false`, `backend: "false"`, `backend: off`, and `backend: "off"` pass. A real backend fails with `memory enabled: backend=<value>`. A missing `memory:` block and a missing `backend:` line each fail with `memory key missing`. Confirm the `false` case fails before T007.
- [ ] T007 [P] [US1] Add a Vale regression to `tests/test_wiki_cli.py` (FR-011, V-03). Run `vale --output=line` on a scratch file outside `wiki/` that contains "DM Thesis". Assert there is no `E100` output and that `Deprecated.DMThesis` fires. Skip the test when the `vale` binary is absent. Confirm it fails before T009.

### Implementation for User Story 1

- [ ] T008 [US1] Fix the memory check in `scripts/check-omp-baseline.sh` per research R1: read the `backend:` line under `memory:`. `false`/`off`, quoted or unquoted, pass. Any other value fails with `memory enabled: backend=<value>`. A missing block or line fails with `memory key missing`. Make T006 pass and V-01 print `omp-speckit-baseline: pass`.
- [ ] T009 [US1] Drain OMP entries e-205, e-207, e-209, and e-211 from `errors.md` with `python3 scripts/error-ledger.py error drain --id <id> --cause-fixed true` (current CLI). Do it in the same commit as T006 and T008 (FR-008).
- [ ] T010 [US1] Remove `CoDM` from all 6 `BasedOnStyles` lines in `.vale.ini` (research R2). For the region, creature, and npc sections, the value becomes `Deprecated` alone. Leave `Vocab = CoDM`, `Packages`, `styles/Deprecated/*.yml`, and `tools/creative_lint/vale_vocab.py` unchanged (FR-022, FR-023). Make T007 pass.
- [ ] T011 [US1] Drain Vale entries e-212, e-214, e-215, e-216, and e-218 from `errors.md` with the current `error drain` CLI, in the same commit as T007 and T010 (FR-008)
- [ ] T012 [US1] Verify V-04 (`pytest -q` completes with no Vale E100) and US1-4 (`python3 scripts/error-ledger.py error list` shows no open OMP or `CoDM` entry). Restore any lint side effects in `wiki/_meta/lint-cache.json` and `styles/config/vocabularies/CoDM/accept.txt` before committing. Plan default, gap 6: lint side-effect behavior stays unchanged.

**Checkpoint**: Verification runs are green, so US2–US4 results can be trusted

---

## Phase 4: User Story 2 - One Coherent Evaluator and Corpus (Priority: P1)

**Goal**: `scripts/luna-eval` is the only runner, `skill-creator` calls it, all eval records follow one schema, and the feature 026 docs cite only real surfaces

**Independent Test**: Quickstart V-09, V-10, and V-11

### Implementation for User Story 2

- [ ] T013 [P] [US2] Rewrite the 66 references to `scripts/check-agent-standards.py`, `tests/test_agent_standards.py`, and `AGENT001`–`AGENT003` in `specs/026-agent-autonomy-scope/{spec,plan,research,data-model,quickstart,tasks}.md` and `specs/026-agent-autonomy-scope/contracts/agent-autonomy.md`. Point each one at `luna-eval` evals (agent behavior) or `wiki lint` (wiki structure). Where no current surface exists, remove the reference with a one-line "replaced by" note (FR-018, V-11).
- [ ] T014 [US2] Add repo-root discovery to `scripts/luna-eval` (`git rev-parse --show-toplevel`, falling back to the script's parent) so it runs from any working directory. Keep the existing flags (FR-027, contracts/eval-run.md).
- [ ] T015 [US2] Make `scripts/luna-eval` write `metrics.json` into each `run-<n>/` directory, derived from `events.jsonl` with the names confirmed in T005. The keys are exactly those in data-model §3: `tool_calls` (by kind), `total_tool_calls`, `retries` (a failed command re-run with the same argv), `duplicate_actions`, `tokens` {`input`,`output`,`total`}, `completion_reason` ∈ `ok|no_output|usage_limit|error`, and `skills_read`. An event that is absent is recorded as `null`, never guessed (research R5).
- [ ] T016 [US2] Make `scripts/luna-eval` grade `skill_selected` assertions into `grading.json`. An item passes when the first owner `SKILL.md` in `metrics.json` `skills_read` matches `text`. Write each item as `{text, passed, evidence, type}` (data-model §3).
- [ ] T017 [US2] In `scripts/luna-eval`, keep exit codes 0/3/4/5 unchanged. On exit 3 or 5, keep completed runs. On a rerun, skip any `run-<n>/` that already has `timing.json` with exit 0 (contracts/eval-run.md, spec Edge Case).
- [ ] T018 [P] [US2] Update `.agents/skills/skill-creator/agents/grader.md` to grade `assertions[]` `{type,text}` for every type except `skill_selected`, which `luna-eval` grades. Keep `text`/`passed`/`evidence` on each item and add `type`. Add the top-level `task_outcome` (`pass|fail|blocked`) and `semantic_quality` (1–5 rubric) (data-model §3).
- [ ] T019 [P] [US2] Update `.agents/skills/skill-creator/references/schemas.md`. The evals.json schema becomes data-model §2, and grading/metrics/timing become data-model §3. Remove the `expectations[]` and `{"query","should_trigger"}` shapes.
- [ ] T020 [US2] Update `.agents/skills/skill-creator/SKILL.md` so that "Running and evaluating test cases" calls `scripts/luna-eval` once per eval and config. Delete the "Description optimization" section (FR-012, FR-015, research R5).
- [ ] T021 [US2] Delete `.agents/skills/skill-creator/scripts/run-eval.py`, `run-loop.py`, and `improve-description.py`. Then `rg "run-eval|run-loop|improve-description" .agents/ AGENTS.md docs/` and remove the remaining references. Keep `utils.py` only if `aggregate-benchmark.py` or `generate-report.py` still import it.
- [ ] T022 [US2] Run a one-off conversion over all `.agents/skills/*/evals/evals.json`. The script is not committed (plan: VIII does not apply to one-offs). Each `expectations[]` string `s` becomes `{"type":"behavior","text":s}`, and `expectations` is removed. Rename `qualitative`→`quality` and `structural`→`structure`. Preserve `core`, `subject_skill`, `trajectory_records`, and `principles`. Plan default, gap 4: keep `scope`, `handoff`, and `coverage`. Plan default, gap 3: `expected_output` stays optional, with no text invented.
- [ ] T023 [US2] Add `"skill_name"` (equal to the directory name) to `.agents/skills/{session-beats,wiki-capture,wiki-context-pack,wiki-ingest,wiki-lint,wiki-query,wiki-update}/evals/evals.json` (FR-013)
- [ ] T024 [US2] Edit the Work-gate, chat-proposal approval, read-side mutation, and retired-path wording by hand, record by record, in the 13 files found by `rg -il "work gate|chat proposal|approval" .agents/skills/*/evals/evals.json`. This includes `.agents/skills/place-design/evals/evals.json` eval 1. Keep each assertion and update its behavior to the current behavior (FR-017, spec Edge Cases).
- [ ] T025 [US2] Add at least one `skill_selected` eval (`{"type":"skill_selected","text":"<dir name>"}`) to each of `.agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/evals/evals.json`. Write each prompt from that skill's own ownership text (FR-014, FR-015, SC-005). Plan default, eval-run CHK006: the owner set is the six named in the plan.
- [ ] T026 [US2] Verify V-09. The schema check prints `[]`, and `rg -il "work gate|chat proposal" .agents/skills/*/evals/evals.json` finds no record that asserts that behavior as required.
- [ ] T027 [US2] Verify V-10. Run the `place-design` `skill_selected` record directly with `scripts/luna-eval ... --out /tmp/030/iteration-1`, then through the skill-creator workflow. Both run dirs must have the same files and keys (`timing.json`, `metrics.json`, `grading.json`), and the item must be `passed: true`. Then drain e-210 from `errors.md` in the same commit as T014–T021 (research R3, FR-008).

**Checkpoint**: One evaluator and one schema exist, which is the prerequisite for US3 and US8

---

## Phase 5: User Story 3 - Feature 029 Baseline Evidence (Priority: P1)

**Goal**: A recorded `luna-eval` baseline with at least 10 cases across all nine categories, each carrying every FR-016 metric

**Independent Test**: Quickstart V-12

- [ ] T028 [US3] Select at least 10 existing owner eval records covering all nine US3 categories: owner completion, specific blocking, scope preservation, read isolation, retrieval convergence, child handoff, parent resumption, write finalization, and recovery. List category → `<skill>:<eval id>` in `specs/029-agent-loop-closure/quickstart.md`.
- [ ] T029 [US3] Run each selected case with `scripts/luna-eval --skill <dir> --eval <id> --out /tmp/030/baseline/iteration-1`, using the default weakest sufficient model (constitution XXVI). On exit 3 or 5, rerun only the missing cases (T017).
- [ ] T030 [US3] Record each case in `specs/029-agent-loop-closure/quickstart.md` with task outcome, tool calls, retries, duplicate actions, tokens, latency, completion reason, and semantic quality, taken from `timing.json`, `metrics.json`, and `grading.json` (FR-016, FR-019)
- [ ] T031 [US3] Check off T003, T011, T018, T030, T037, T044, T046, T047, and T049 in `specs/029-agent-loop-closure/tasks.md`, each with a pointer to its evidence (FR-019, SC-006)

**Checkpoint**: A baseline exists for the SC-012 comparisons

---

## Phase 6: User Story 4 - Scoped Lint Costs Scoped Work (Priority: P1)

**Goal**: Identity reads and compares only changed or selected pages and their candidates, using a derived index. Findings are identical.

**Independent Test**: Quickstart V-05, V-06, V-07, and V-08

### Tests for User Story 4

- [ ] T032 [US4] Add identity-index tests to `tests/test_wiki_ops.py`, using a temp vault built in the test:
  - (a) cold and warm `scan_identities` output is identical.
  - (b) editing one page refreshes its row: a `(size, mtime_ns)` change triggers a rehash, and the findings equal a cold run.
  - (c) an index containing `{`, or with a changed `version`, is rebuilt.
  - (d) rows for deleted paths are dropped, and `pairs` for vanished hashes are pruned.
  - (e) a scoped run reports `compared == |selected ∪ candidates|`, which is less than the page count.

  Confirm (e) fails before T033.

### Implementation for User Story 4

- [ ] T033 [US4] Add index load and save to `tools/wiki_ops/identity.py` for `wiki/_meta/identity-index.json`, using data-model §4 exactly:
  - Header: `version`, `manifest_sha256`.
  - Rows keyed by path: `size`, `mtime_ns`, `content_sha256`, `stem`, `title`, `type`, `lifecycle`, `aliases`, `redirects_to`, `body_len`, and `profile` (the body character `Counter`).
  - Scan with an `os.scandir` walk and `stat` only (research R4 steps 1–3).
  - Validity: reuse a row when `(size, mtime_ns)` matches or the rehashed `content_sha256` matches. A changed `version` or a JSON error rebuilds everything, and a changed `manifest_sha256` refreshes the affected state.
- [ ] T034 [US4] Replace the whole-vault read in `tools/wiki_ops/identity.py` with candidate selection from index rows (research R4 steps 4–5). Candidates share the same `type`, have no redirect, and meet one of these: a norm title or alias match, shared provenance with stem ratio > 0.7, a merge transition, or a profile prefilter `2·|A∩B| / (lenA+lenB) > 0.6`. Plan default, gap 1: the cached prefilter counts as a cheap signal. Leave `resolve_identity` and `_path_for` unchanged (performance CHK021: the plan changes only `scan_identities`).
- [ ] T035 [US4] Add the pair-ratio cache to `tools/wiki_ops/identity.py`. Store `SequenceMatcher.ratio()` in `pairs` keyed `"<sha_a>|<sha_b>"` (sorted content hashes). Read only candidate bodies whose pair is uncached, and prune pairs whose hashes match no row on save (research R4 step 6, R7). Make T032 pass.
- [ ] T036 [US4] Add `"identity": {"status","ambiguous","scanned","compared","index":{"hits","misses"}}` to `scripts/wiki-lint --json` output, where `scanned` = selected and `compared` = |selected ∪ candidates| (data-model §4, SC-007)
- [ ] T037 [US4] Track `wiki/_meta/identity-index.json` like `wiki/_meta/lint-cache.json`, which is tracked today, so no `.gitignore` change is needed. Plan default, performance CHK006: data-model §4 "Tracking", one rule for both files.
- [ ] T038 [US4] Verify V-05 (run 1 `timing.duration_ms` < 5000, `identity.compared` far below the page count; run 2 `cache.hits: 1`), V-06 (diff against `/tmp/030/identity-before.json` and `/tmp/030/lint-before.json` from T002), and V-07 (corrupt index rebuilt). Record the V-05 numbers in the `specs/030-self-improving-architecture/quickstart.md` V-05 row.
- [ ] T039 [US4] Run V-08 (`time scripts/wiki health`). Confirm there is no harness timeout, and record the wall time next to the SC-006 baseline in `specs/029-agent-loop-closure/quickstart.md` (after T030)
- [ ] T040 [US4] Drain identity entries e-206, e-208, and e-213 from `errors.md` with the current `error drain` CLI, in the same commit as T032–T037 (FR-008)

**Checkpoint**: Phase 1 is complete: green checks, one evaluator, a baseline, and scoped identity

---

## Phase 7: User Story 5 - Friction Is Fixed at the Source, Then Work Resumes (Priority: P2)

**Goal**: Shared guidance states the friction rule once, as a branch of the capability loop

**Independent Test**: Quickstart V-17 (seeded friction, at least 4/5 cold subjects fix the source, add a regression, and finish)

- [ ] T041 [P] [US5] Add one friction-rule paragraph to `AGENTS.md` next to "Capability loop" (line ~72): act → friction → identify cause → fix the authoritative source (smallest change) → verify → continue the original task. Add no new workflow, command, or skill (FR-001, FR-002, FR-005).
- [ ] T042 [P] [US5] Add the friction branch (act → friction → fix source → re-observe → continue) to the capability loop in `docs/agents/hybrid-sdd.md`, linking to the `AGENTS.md` paragraph rather than restating it (FR-001, constitution XVI)
- [ ] T043 [US5] Run V-17. On a scratch branch, make one owner `SKILL.md` name a retired command path, then run 5 cold `scripts/luna-eval` subjects on one of that owner's evals. At least 4/5 must fix the source, add a regression, and finish the owner task with no new `errors.md` entry. Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-17 row. Discard the scratch branch. This runs after T054 so the new ledger format is in place.

**Checkpoint**: Friction handling is documented in one place and behaviorally proven

---

## Phase 8: User Story 6 - Recurring Causes Trend to Zero (Priority: P2)

**Goal**: `errors.md` holds only open four-field entries. Duplicates attach, fixes drain, and recurrence is measurable.

**Independent Test**: Quickstart V-13, V-14, and V-15

### Tests for User Story 6

- [ ] T044 [US6] Add ledger tests to `tests/test_error_ledger_repairs.py`. Each one drives `scripts/error-ledger.py` via subprocess on a scratch `errors.md` and covers:
  - `append` attaches on the same `source` + `cause_key`, and a scratch copy of the V-14 case gives `attached` then `already_done`.
  - A different `source` creates a new entry (spec Edge Case).
  - `--attach e-N` forces the target.
  - A missing `--source` exits 2 with an example, and `--source` must be an existing repo path or `external:<name>`.
  - `drain` gives `drained` then `already_done`, and `--cause-fixed true` is accepted and ignored.
  - `--dry-run` writes nothing and returns `planned`.
  - `recurrence` totals work.
  - `migrate` gives `migrated` then `already_done`.
  - Commands work from a non-root cwd.

  Plan default, error-ledger CHK011: an "identical occurrence" means the same `sitting` and `detail`.

### Implementation for User Story 6

- [ ] T045 [US6] Rework the entry model in `scripts/error-ledger.py` (data-model §1). Keep the `# Error ledger` heading, a blank line, then one JSON object per line with sorted keys. The fields are exactly `id` (`"e-<n>"`, unique, new ids from `next_error_id`), `cause` (never rewritten), `source` (repo-relative path or `external:<name>`), and `evidence` (a list of `{sitting, detail}`, length ≥ 1). There is no `status` or `cause_fixed`. Add `cause_key` per research R3: casefold, collapse whitespace, drop digits and backtick- or quote-wrapped literals. Plan default, gap 2: match on the same `source` + `cause_key`.
- [ ] T046 [US6] Implement `error append --source S --cause C --sitting X [--detail D] [--attach e-N] [--dry-run]` in `scripts/error-ledger.py`, returning `{"status":"attached"|"created"|"already_done","id","occurrences"}`. `detail` defaults to `C` (contracts/error-ledger.md).
- [ ] T047 [US6] Implement `error drain --id e-N [--dry-run]` (`drained|already_done`, with `--cause-fixed true` as a no-op) and `error list [--ids-only]` in `scripts/error-ledger.py`
- [ ] T048 [US6] Implement `error recurrence` in `scripts/error-ledger.py`, returning `{"total": Σ(len(evidence)−1), "by_sitting": {sitting: non-first occurrences}}` (FR-009)
- [ ] T049 [US6] Implement idempotent `error migrate [--dry-run]` in `scripts/error-ledger.py` (research R3):
  - Drop entries with `status == "drained"`.
  - Map each open entry to `{id, cause, source, evidence:[{sitting, detail: cause}]}`.
  - Merge the OMP, Vale, and identity groups into their lowest id if any are still open.
  - Return `{"status","removed","merged","entries"}`.
- [ ] T050 [US6] Add repo-root discovery to `scripts/error-ledger.py` so `errors.md` is found from any cwd. Add an `--help` Examples block that shows `python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …"` (FR-027, FR-032). Make T044 pass.
- [ ] T051 [US6] Migrate `errors.md`: run `error migrate --dry-run`, run it for real, then run it again and expect `already_done` (V-13). In the same commit, set `source` by hand for the remaining open entries (e-168, e-201, e-202 → `scripts/wiki`, e-203, e-217, and any others still open) from their cause text (research R3).
- [ ] T052 [P] [US6] Rewrite `AGENTS.md` "Error ledger" (line ~196): fix and verify the source, then continue. `append` only when the fix cannot land in the current task, and `drain` goes in the same commit as the verified fix. Remove `--cause-fixed true` from the documented invocations (contracts/error-ledger.md).
- [ ] T053 [P] [US6] Rewrite `.agents/skills/wiki-lint/SKILL.md` line ~47 from "record the mismatch in errors.md" to "reconcile first, record only if unresolved", linking to `AGENTS.md` rather than restating it (constitution XIX)
- [ ] T054 [US6] Verify V-15 (`python3 scripts/error-ledger.py error recurrence` returns `{"total": n, "by_sitting": {...}}`) and SC-009 (no two open entries share `(source, cause_key)`). Record the starting total in the `specs/030-self-improving-architecture/quickstart.md` V-15 row. Plan default, gap 5: the 20-sitting window is tracked after merge and is not a gate.

**Checkpoint**: The ledger is deduplicated, and its agent guidance matches "fix first"

---

## Phase 9: User Story 7 - Wiki Commands Agents Can Drive Headlessly (Priority: P2)

**Goal**: The `scripts/wiki` subcommands meet contracts/wiki-cli.md (FR-027–FR-039)

**Independent Test**: Quickstart V-16 and SC-010

### Tests for User Story 7

- [ ] T055 [US7] Add one subprocess test per rule class to `tests/test_wiki_cli.py` (FR-039):
  - Discovery from a non-repo cwd, the `vault` key, and the `--vault` > `OBSIDIAN_VAULT_PATH` precedence.
  - Bare `wiki` lists exactly `lint`, `lint fix`, `query`, `health`, `mutate`, `repair` and exits 0.
  - `wiki <sub> --help` shows only that subcommand plus an `Examples:` block.
  - No prompts with stdin closed.
  - `--stdin` and `--paths-only`.
  - Options before or after positionals.
  - `wiki lint fix …` parses the same as `wiki lint … fix`.
  - Exit 2 with keys `status`/`error`/`hint`/`example`/`list_valid` for each of: an unknown path, a `wiki/`-prefixed path, a scope without `:`, an unknown scope kind, and an unsupported option.
  - `--dry-run` returns `planned` and writes nothing.
  - A second identical run returns `"changed": []` and `"status": "already_done"`.
  - Success keys `status`, `vault`, `changed`, `counts`, `timing.duration_ms`, `next`.

  Confirm the tests fail before T056.

### Implementation for User Story 7

- [ ] T056 [US7] Implement vault discovery in `tools/wiki_ops/cli.py` in the order `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` > `~/.obsidian-wiki/config`. Find the repo root from the script location, not the cwd, and include `"vault": "<absolute path>"` in every result (FR-027, research R6).
- [ ] T057 [US7] In `scripts/wiki`, make bare `wiki` print one line per subcommand. Give each subcommand its own `--help` with an `Examples:` block that uses the real invocations from contracts/wiki-cli.md "Examples blocks" (FR-031, FR-032).
- [ ] T058 [US7] Make `lint fix` an argparse subparser under `lint` in `scripts/wiki`, and allow options anywhere (intermixed parsing). Plan default, contract conflict wiki-cli CHK011 (owned by Plan): keep the positional `fix` token as an alias that behaves the same, and remove it from the docs (research R6, FR-034).
- [ ] T059 [US7] Add `--stdin` to `scripts/wiki`: newline-separated paths for lint, lint fix, and health, and one JSON payload for mutate and repair. Add `--paths-only` output. No command prompts, and a missing required input is an error (FR-030, FR-033).
- [ ] T060 [US7] Implement the FR-035 error object in `scripts/wiki` and `tools/wiki_ops/cli.py`: exit 2, JSON on stdout with `status`, `error`, `hint`, `example`, and `list_valid`, and the same message on stderr. Cover the five contract cases, and list the allowed scope kinds `files|directory(dir)|entity_type(type)|identity_set|changed|bundle`.
- [ ] T061 [US7] Make `lint fix`, `mutate`, and `repair` in `scripts/wiki` accept `--dry-run`, which returns `"planned": [...]` and writes nothing. A second identical run returns `"changed": []` and `"status": "already_done"`. Add no confirmation prompt, so no `--yes` flag is needed (FR-036, FR-037).
- [ ] T062 [US7] Make every `scripts/wiki` success result include `status`, `vault`, `changed`, `counts` (`before`/`after`), `timing.duration_ms`, and `next`. `health` sets `next` to one concrete command, e.g. `wiki lint fix dir:entities/npc` (FR-038, FR-029 health interpretation). Make T055 pass.
- [ ] T063 [P] [US7] Add an `--help` Examples block to `scripts/luna-eval` showing `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/pd/iteration-1`, and make a missing required flag exit 2 with an example (FR-032, FR-035)
- [ ] T064 [US7] Verify V-16 (bare `wiki`, `wiki lint --help`, a bad path giving exit 2 with `hint`/`example`, `--scope dir`, `lint fix dir:entities/place --dry-run` twice, then `already_done` after one real run). For SC-010, run the `wiki-lint` and `wiki-query` owner evals with cold `scripts/luna-eval` subjects and count invocation errors from `metrics.json` `retries` (target 0).

**Checkpoint**: Phase 2 is complete

---

## Phase 10: User Story 8 - Incumbent vs Candidate Instruction Promotion (Priority: P3)

**Goal**: At least one owner skill is promoted by measurement against the US3 baseline (SC-012)

**Independent Test**: Quickstart V-18

- [ ] T065 [US8] Pick one of the six owners. Draft one small candidate edit to `.agents/skills/<owner>/SKILL.md` in the working tree, drawing on its US3 baseline run dirs under `/tmp/030/baseline/`: the current instruction, failed and successful tasks, tool results, assertion failures, user corrections, and token/tool-call cost (FR-043)
- [ ] T066 [US8] Snapshot the incumbent skill directory from HEAD to `/tmp/030/incumbent/<owner>/` (`git archive HEAD .agents/skills/<owner> | tar -x -C /tmp/030/incumbent`). Run `scripts/luna-eval --config old_skill --subject-skill /tmp/030/incumbent/.agents/skills/<owner>` and `--config with_skill` on the same eval ids, plus the cross-skill baseline cases from T028 (FR-042, spec Edge Case).
- [ ] T067 [US8] Compare the runs with `.agents/skills/skill-creator/scripts/aggregate-benchmark.py`, ranking success, then quality, then tool calls, retries, tokens, latency, and scope (FR-044). Keep the candidate only if it is non-inferior on both success and quality with a lower median of tool calls, retries, or tokens. Otherwise `git checkout -- .agents/skills/<owner>/SKILL.md`. Record the decision in the `specs/030-self-improving-architecture/quickstart.md` V-18 row.

**Checkpoint**: The promotion rule has been exercised end to end

---

## Phase 11: User Story 9 - Skills Stay Small; Procedure Moves into Tools (Priority: P3)

**Goal**: The six owner skills answer the five FR-040 questions and shrink, because the tools now carry the procedure

**Independent Test**: Quickstart V-19

- [ ] T068 [US9] Record `wc -l .agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/SKILL.md` to `/tmp/030/skill-lines-before.txt`, and snapshot those dirs to `/tmp/030/incumbent-us9/` for old_skill runs
- [ ] T069 [US9] Move the manifest reasoning named in recorded trajectories into `scripts/manifest.py`, with a regression in `tests/test_wiki_ops.py` (FR-029, FR-011)
- [ ] T070 [US9] Move repair bookkeeping into `wiki lint fix` in `scripts/wiki` and `tools/wiki_ops/cli.py`, with a regression in `tests/test_wiki_cli.py` (FR-029, FR-011)
- [ ] T071 [P] [US9] Shorten `.agents/skills/place-design/SKILL.md`. Remove the text now covered by T056, T062, T069, and T070 (path discovery, health interpretation, manifest reasoning, repair bookkeeping), and make sure the five FR-040 answers are present.
- [ ] T072 [P] [US9] Shorten `.agents/skills/faction-design/SKILL.md` in the same way as T071
- [ ] T073 [P] [US9] Shorten `.agents/skills/session-beats/SKILL.md` in the same way as T071
- [ ] T074 [P] [US9] Shorten `.agents/skills/run-guide/SKILL.md` in the same way as T071
- [ ] T075 [P] [US9] Shorten `.agents/skills/wiki-query/SKILL.md` in the same way as T071
- [ ] T076 [P] [US9] Shorten `.agents/skills/wiki-lint/SKILL.md` in the same way as T071 (it builds on T053)
- [ ] T077 [US9] Verify V-19. Line counts must not exceed `/tmp/030/skill-lines-before.txt`. Rerun each skill's evals with `scripts/luna-eval` `--config with_skill` against `--config old_skill --subject-skill /tmp/030/incumbent-us9/...`, and compare with `aggregate-benchmark.py` (non-inferior success and quality). Revert any skill that regresses.

**Checkpoint**: Phase 3 is complete

---

## Phase 12: Polish & Cross-Cutting Concerns

- [ ] T078 Update the `<!-- SPECKIT START -->`…`<!-- SPECKIT END -->` block in `AGENTS.md` (line ~584) to point at `specs/030-self-improving-architecture/plan.md` (plan Source Code note)
- [ ] T079 Run the full `pytest -q` and compare it with `/tmp/030/pytest-before.txt`. It must show no new failures and no Vale E100.
- [ ] T080 Run `git diff --stat` and restore lint side effects in `wiki/_meta/lint-cache.json` and `styles/config/vocabularies/CoDM/accept.txt` that are not part of an intended change. Plan default, gap 6: behavior unchanged.
- [ ] T081 Re-run quickstart V-01, V-03, V-09, V-11, V-15, and V-16 on the final tree, and fill in any empty result rows in `specs/030-self-improving-architecture/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup. T004 gates US5 and US6. T005 gates T015.
- **Phase 1 stories (US1–US4)** come before Phase 2 stories (US5–US7), which come before Phase 3 stories (US8–US9). This order is binding (spec Assumptions).
- **Polish (Phase 12)**: After all stories

### User Story Dependencies

- **US1 (P1)**: After Foundational. There are no story dependencies. It is the MVP.
- **US2 (P1)**: After US1, because eval runs need green checks. T013 (026 docs) can start any time.
- **US3 (P1)**: After US2, because it needs `metrics.json` and `grading.json` (T015–T017)
- **US4 (P1)**: After US1 (Vale fixed). It is independent of US2 and US3, except T039, which writes after T030.
- **US5 (P2)**: T041 and T042 are independent. T043 needs US2 (luna-eval) and T054 (new ledger format).
- **US6 (P2)**: After US1, US2, and US4, whose drains must land before migration (T051)
- **US7 (P2)**: After US4 (the `wiki-lint` output shape). T063 needs T014–T017.
- **US8 (P3)**: After US2, US3, and US5
- **US9 (P3)**: After US7 (T056, T062) and US3. T076 comes after T053.

### Within Each User Story

- Tests are written first and must fail. Then comes implementation, then the ledger drain in the same commit as the fix, then quickstart verification.
- Tasks on the same file run in sequence (e.g. T014→T017 `scripts/luna-eval`; T045→T050 `scripts/error-ledger.py`; T057→T062 `scripts/wiki`).

### Parallel Opportunities

- T003 runs alongside T002.
- US1: T006 ∥ T007. The OMP track (T008–T009) is independent of the Vale track (T010–T011), apart from sharing `errors.md` at commit time.
- US2: T013 ∥ T018 ∥ T019 ∥ the `scripts/luna-eval` chain T014–T017.
- US4 can run alongside US2 and US3 once US1 is done.
- US5: T041 ∥ T042. US6: T052 ∥ T053.
- US7: T063 ∥ T056–T062.
- US9: T071–T076 in parallel (one skill each).

---

## Parallel Example: User Story 1

```bash
Task: "T006 Create tests/test_omp_baseline.py"
Task: "T007 Add Vale regression to tests/test_wiki_cli.py"
```

## Parallel Example: User Story 2

```bash
Task: "T013 Rewrite 026 references in specs/026-agent-autonomy-scope/*"
Task: "T018 Update .agents/skills/skill-creator/agents/grader.md"
Task: "T019 Update .agents/skills/skill-creator/references/schemas.md"
```

## Parallel Example: User Story 9

```bash
Task: "T071 Shorten .agents/skills/place-design/SKILL.md"
Task: "T072 Shorten .agents/skills/faction-design/SKILL.md"
Task: "T073 Shorten .agents/skills/session-beats/SKILL.md"
Task: "T074 Shorten .agents/skills/run-guide/SKILL.md"
Task: "T075 Shorten .agents/skills/wiki-query/SKILL.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup and Phase 2 Foundational
2. Phase 3 (US1): green OMP and Vale checks, with 9 ledger entries drained
3. **STOP and VALIDATE**: V-01 to V-04

### Incremental Delivery

1. US1 → US2 → US3 → US4 (Phase 1 coherent baseline; each checkpoint is independently verifiable)
2. US5 → US6 → US7 (Phase 2 close the loop)
3. US8 → US9 (Phase 3 optimize, measured against the US3 baseline)

### Plan defaults applied for open gaps (no spec or plan edits)

- Gap 1 / performance CHK007, CHK013: the cached profile prefilter (> 0.6) counts as a cheap-signal candidate (T034)
- Gap 2 / error-ledger CHK001: same cause = same `source` + normalized `cause_key`, with `--attach` to force (T045)
- Gap 3 / eval-run CHK001: `expected_output` is optional and never invented (T022)
- Gap 4 / eval-run CHK002: keep `scope`, `handoff`, and `coverage`; fold `qualitative` and `structural` (T022)
- Gap 5: the SC-009 20-sitting window is tracked after merge (T054)
- Gap 6 / performance CHK022: the lint side effects on tracked files are unchanged, and they are restored before commits (T012, T080)
- Contract conflict wiki-cli CHK011 (Plan): the positional `fix` alias is kept but undocumented (T058)
- Performance CHK006: `identity-index.json` is tracked like `lint-cache.json` (T037). Performance CHK021: `resolve_identity` and `_path_for` are unchanged (T034).
- Error-ledger CHK011: an identical occurrence means the same `sitting` + `detail` (T044). Eval-run CHK006: the owner set is the six named owners (T025).

---

## Notes

- [P] tasks touch different files and have no dependency on incomplete tasks.
- Every fix lands with its regression and its `errors.md` drain in one commit (FR-008, FR-011).
- Avoid committing scratch output under `/tmp/030/` and lint side effects.
