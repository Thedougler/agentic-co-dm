---

description: "Task list for feature 030: Self-Improving Architecture"
---

# Tasks: Self-Improving Architecture

**Input**: Design documents from `/specs/030-self-improving-architecture/` (plan.md at 922a0796, consolidated under FR-046/SC-014; spec.md at b14ea71b)

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ (wiki-cli, error-ledger, eval-run), quickstart.md, checklists/

**Tests**: The spec asks for them. FR-011 requires a regression for every fixed failure, FR-021 an OMP checker test, FR-039 one test per CLI rule class, and FR-007 a test for the cross-source `--attach` refusal. Write each test first and confirm it fails before the fix. New tests go in the existing file for each module (plan "Testing"); the only new test file is `tests/test_luna_eval.py`.

**Consolidation (binding, FR-046/SC-014)**: every task edits the module that owns the concern. Code only detects, measures, checks, indexes, reports, or applies a fix with exactly one correct output; every judgment stays in the skill named in plan "Judgments and their governing skill". 2 files are added and 10 are deleted (plan "Simplify and consolidate").

**Open gaps**: The plan's round-1/2 spec gaps 1–6 are resolved by cae8bb44 and b14ea71b, and checklists/wiki-cli.md CHK011 (positional `fix` alias) is resolved by df3e5c7c: there is no alias. Round-3 Clarify gaps 1, 2, 3, and 5 are resolved (plan 922a0796); gap 4 is pending with Nick, and its default applies without a task (see "Open gaps" at the end). One item keeps a Plan default: error-ledger CHK011 (T060). spec.md and plan.md are not edited here.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US9)
- Paths are repo-relative (single repository, no new directories; plan "Structure Decision")

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Box environment and pre-change baselines that later parity checks diff against

- [ ] T001 Provision `.venv/` per quickstart.md "Prerequisites": `uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0 pytest`, then `export PATH="$PWD/.venv/bin:$PATH"` and `export OBSIDIAN_VAULT_PATH="$PWD/wiki"`. No tracked file changes.
- [ ] T002 Capture pre-change baselines into `/tmp/030/`. Temporarily remove `CoDM` from `.vale.ini` in the working tree only, as in plan "Measurements taken". Write the V-06 `scan_identities` dump to `/tmp/030/identity-before.json`, whole-vault `scripts/wiki lint` findings to `/tmp/030/lint-before.json`, `scripts/lint-obsidian-markdown` whole-vault findings to `/tmp/030/obsidian-md-before.txt` (reference 519 table pipes / 21 broken images), and `./scripts/wiki-reveal --count --json` to `/tmp/030/reveal-count-before.json` (V-04d). Then revert `.vale.ini` and the FR-028 bookkeeping files `wiki/_meta/lint-cache.json` and `styles/config/vocabularies/CoDM/accept.txt` with `git checkout --`, because this is scratch measurement state.
- [ ] T003 [P] Record the pre-change test status: `pytest -q > /tmp/030/pytest-before.txt` (note any failures from the known Vale E100)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Confirm the dependencies the plan relies on before any story lands

- [ ] T004 Confirm that `.specify/memory/constitution.md` is v6.0.1 or later and that principle XIII allows fix-verify-continue (plan Constitution Check, "XIII … dependency met"). Stop and report if it does not, because this blocks US5 and US6.
- [ ] T005 Confirm the codex `--json` event names (research R5 "To verify"). Run `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/030/probe/iteration-1` and inspect `/tmp/030/probe/*/with_skill/run-1/events.jsonl` for `item.completed` (`command_execution`/`file_change`, including the exit code and stdout/stderr fields needed for `invocation_errors`) and `turn.completed.usage`. Also note where the codex `--model`/`--effort` values `luna-eval` passes are available. Write the real names to `/tmp/030/event-names.txt` for T029.

**Checkpoint**: Environment, baselines, and event names are known, so the user stories can start

---

## Phase 3: User Story 1 - Green Baseline Checks (Priority: P1) 🎯 MVP

**Goal**: The OMP checker and scoped Vale lint pass on the correct config, their ledger entries are drained, `Deprecated.*` findings are judgment repairs, and `wiki lint` is the only linter (the side lint scripts and duplicate tools are folded in and deleted)

**Independent Test**: `scripts/check-omp-baseline.sh` passes on the current `.omp/config.yml`, scoped `wiki lint` on one page shows no `CoDM` E100, and the folded scripts are gone (quickstart V-01–V-04d)

### Tests for User Story 1

- [ ] T006 [P] [US1] Add the OMP checker test to `tests/test_policy_conflicts.py` (FR-021, V-02); create no new test file. Run `scripts/check-omp-baseline.sh` against a temp copy of the repo files, once per config. `backend: false`, `backend: "false"`, `backend: off`, and `backend: "off"` pass. A real backend fails with `memory enabled: backend=<value>`. A missing `memory:` block and a missing `backend:` line each fail with `memory key missing`. Confirm the `false` case fails before T011.
- [ ] T007 [P] [US1] Add a Vale regression to `tests/test_wiki_cli.py` (FR-011, V-03). Run `vale --output=line` on a scratch file outside `wiki/` that contains "DM Thesis". Assert there is no `E100` output and that `Deprecated.DMThesis` fires. Skip the test when the `vale` binary is absent. Confirm it fails before T013.
- [ ] T008 [P] [US1] Add a `vale_adapter` test to `tests/test_creative_lint.py` (FR-023, V-04b): a finding from a repo-local style (`is_custom`, e.g. `Deprecated.DMThesis`) is emitted with `repair_class: human_repair` and no `repair_action`, and `wiki lint fix --dry-run` on a scratch page containing "DM Thesis" plans no change for it. Confirm it fails before T015 (today it is `deterministic_repair` + `delete_section`).
- [ ] T009 [P] [US1] Add tests for the folded rules to `tests/test_wiki_ops.py`, driving `tools/lint_wiki.py` on a temp vault: `md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, `forbidden_tree`, and `literal_newline` (scoped to session pages and Session templates, skipping YAML frontmatter and fenced code/statblocks, as `scripts/lint-literal-newlines` does). Assert `table_wikilink_unescaped_pipe` is `deterministic_repair` (`|` → `\|` inside a table-cell wikilink) and the rest are `human_repair`. Confirm they fail before T016.
- [ ] T010 [P] [US1] Adjust the `wiki-reveal --count` regression in `tests/test_wiki_ops.py` (the `scripts/wiki-reveal` test near line 152, next to the CLI contract test at ~line 109): add a page with no frontmatter block to the temp vault and assert it is skipped and `--count --json` totals are unchanged (V-04d). It must pass both before and after T020.

### Implementation for User Story 1

- [ ] T011 [US1] Fix the memory check in `scripts/check-omp-baseline.sh` per research R1: read the `backend:` line under `memory:`. `false`/`off`, quoted or unquoted, pass. Any other value fails with `memory enabled: backend=<value>`. A missing block or line fails with `memory key missing`. Make T006 pass and V-01 print `omp-speckit-baseline: pass`.
- [ ] T012 [US1] Drain OMP entries e-205, e-207, e-209, and e-211 from `errors.md` with the current CLI, which still requires the flag at this point: `python3 scripts/error-ledger.py error drain --id <id> --cause-fixed true`. This runs before T063 removes `--cause-fixed`; never pass it after that. Do it in the same commit as T006 and T011 (FR-008).
- [ ] T013 [US1] Remove `CoDM` from all 6 `BasedOnStyles` lines in `.vale.ini` (research R2). For the region, creature, and npc sections, the value becomes `Deprecated` alone. Leave `Vocab = CoDM`, `Packages`, `styles/Deprecated/*.yml`, and `tools/creative_lint/vale_vocab.py` unchanged (FR-022, FR-023). Make T007 pass.
- [ ] T014 [US1] Drain Vale entries e-212, e-214, e-215, e-216, and e-218 from `errors.md` with the current CLI (`error drain --id <id> --cause-fixed true`, before T063), in the same commit as T007 and T013 (FR-008)
- [ ] T015 [US1] In `tools/creative_lint/vale_adapter.py`, label findings from repo-local styles (`is_custom`) `human_repair` with no `repair_action`, so `wiki lint fix` never applies them. Removal or relocation of `Deprecated.*` content is the agent's call under `.agents/skills/wiki-lint/SKILL.md` (FR-023, plan "Judgments"). Make T008 pass.
- [ ] T016 [US1] Fold the rules of `scripts/lint-obsidian-markdown` (`md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, `forbidden_tree`; its `missing_frontmatter` already exists) and `scripts/lint-literal-newlines` (as `literal_newline`) into `tools/lint_wiki.py` findings, with repair classes as in T009 (plan "One linter", research R8, constitution XXI). Make T009 pass.
- [ ] T017 [US1] Delete `scripts/lint-wiki-write`, `scripts/lint-obsidian-markdown`, and `scripts/lint-literal-newlines`. Change `.agents/skills/obsidian-markdown/SKILL.md` line 35 from `./scripts/lint-wiki-write` to `./scripts/wiki lint`, and move `tests/test_error_ledger_repairs.py` lines 46–48 off the three scripts onto `scripts/wiki lint` (same positional-file case).
- [ ] T018 [US1] Remove `TMPL_inherited_deprecated_guidance` from `scripts/wiki-lint` (duplicate of Vale `Deprecated.FactionClock`, research R8) and keep `TMPL_deprecated_guidance`. Update any test that asserts the removed rule id.
- [ ] T019 [US1] In `package.json`, set `"lint:vale": "./scripts/wiki lint"` (`vale_adapter.run_vale` already refreshes the vocabulary). Delete `scripts/vale-vocab`. `rg -n vale-vocab AGENTS.md docs .agents scripts tools tests package.json README.md` must find nothing (FR-046 rule 2, SC-014 c, V-04d).
- [ ] T020 [US1] In `scripts/wiki-reveal`, replace `from tools.check_wiki_pages import frontmatter` with `from tools.lint_wiki import frontmatter`. It returns `(block, fields)`: skip the page when `block is None` and use `fields` as the keys. Delete `tools/check_wiki_pages.py`. Change `README.md` line 105 to `./scripts/wiki lint`. `rg -n check_wiki_pages AGENTS.md docs .agents scripts tools tests package.json README.md` must find nothing, and T010 passes (V-04d).
- [ ] T021 [US1] Run `scripts/wiki lint fix` on the whole vault (the current CLI's `fix` form; the subparser lands in T072) to apply the 519 `table_wikilink_unescaped_pipe` repairs, then confirm `table_wikilink_unescaped_pipe` = 0 (V-04c). Commit the wiki edits together with the FR-028 bookkeeping they caused. The 21 `broken_image_link` findings stay `human_repair` agent work under `wiki-lint` (round-3 gap 2, resolved; no task here).
- [ ] T022 [US1] Verify V-01, V-03, V-04 (`pytest -q` completes with no Vale E100), V-04b, V-04c, and V-04d (both `ls` checks fail, `lint:vale` is `./scripts/wiki lint`, `./scripts/wiki-reveal --count --json` equals `/tmp/030/reveal-count-before.json`, both `rg` checks empty), and US1-4 (`python3 scripts/error-ledger.py error list` shows no open OMP or `CoDM` entry). `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` are tracked FR-028 bookkeeping: commit them with the change that caused them, and revert them only after scratch measurement runs.

**Checkpoint**: Verification runs are green and `wiki lint` is the only linter, so US2–US4 results can be trusted

---

## Phase 4: User Story 2 - One Coherent Evaluator and Corpus (Priority: P1)

**Goal**: `scripts/luna-eval` is the only runner, `skill-creator` calls it, all eval records follow one schema that `luna-eval` checks, and the feature 026 docs cite only real surfaces

**Independent Test**: Quickstart V-09, V-10, and V-11

### Tests for User Story 2

- [ ] T023 [P] [US2] Add a case to `tests/test_policy_conflicts.py` (SC-008, V-11) that runs `scripts/check-current-commands --json` over `specs/026-agent-autonomy-scope/` and fails on any cited `scripts/…` or `tests/…` path that does not exist, and separately fails on any `AGENT00[1-3]` in those docs. Confirm it fails before T026 and T025.
- [ ] T024 [US2] Create `tests/test_luna_eval.py`, the one new test file (plan "New files"). Cover:
  - The `load_eval` schema check (data-model §2): it passes on all 60 `.agents/skills/*/evals/evals.json`, and on a temp bad file it exits 2 with `{"status":"error","error":"<file>: eval <id>: <problem>","hint":"see data-model §2","example":…}` before any subject run. Cases: missing `skill_name` or one unequal to the directory name, empty or missing `assertions[]`, a leftover `expectations[]`, a `type` outside {`skill_selected`, `behavior`, `quality`, `guardrail`, `process`, `content`, `structure`, `scope`, `handoff`, `coverage`}, and a `skill_selected` `text` that is not an existing directory under `.agents/skills/`.
  - `metrics.json` built from a fixture `events.jsonl`: exactly the data-model §3 keys, including `retries` (a failed command re-run with identical argv), `invocation_errors`, `invocation_error_commands`, `model`, and `effort`, with an absent event recorded as `null`.
  - `invocation_errors` counts a `command_execution` of an FR-027 command (`scripts/wiki`, `scripts/wiki-lint`, `scripts/luna-eval`, `scripts/error-ledger.py`, `scripts/manifest.py`) rejected with the FR-035 error object on stdout (`"status":"error"` plus `example`) or argparse `usage: … error:` on stderr and a non-zero exit, even when later corrected; exit 2 alone (`EXIT_REJECTED`) does not count.
  - `skill_selected` grading: it passes when the first owner `SKILL.md` in `skills_read` matches `text`, written as `{text, passed, evidence, type}`.
  - Work-gate wording (SC-003): fail when any assertion `text` in any evals file contains `Work gate`, `chat proposal`, or `approval before write` (case-insensitive).

  Confirm the schema, metrics, and grading cases fail before T028–T030.

### Implementation for User Story 2

- [ ] T025 [P] [US2] Rewrite the 66 references to `scripts/check-agent-standards.py`, `tests/test_agent_standards.py`, and `AGENT001`–`AGENT003` in `specs/026-agent-autonomy-scope/{spec,plan,research,data-model,quickstart,tasks}.md` and `specs/026-agent-autonomy-scope/contracts/agent-autonomy.md`. Point each one at `luna-eval` evals (agent behavior) or `wiki lint` (wiki structure). Where no current surface exists, remove the reference with a one-line "replaced by" note (FR-018, V-11).
- [ ] T026 [P] [US2] Extend `scripts/check-current-commands` (research R8): also check cited `scripts/…` and `tests/…` paths, and add `specs/026-agent-autonomy-scope/` to its scan roots. Make T023 pass.
- [ ] T027 [US2] Replace the `git rev-parse --show-toplevel` root in `scripts/luna-eval` (line ~47) with `tools/wiki_ops/cli.py` `repo_root`, started from the script's own location, so it runs from any working directory. Keep the existing flags (FR-027, contracts/eval-run.md). T070 later makes the package location the helper's default.
- [ ] T028 [US2] Add the evals.json schema check to `load_eval` in `scripts/luna-eval` (plan "Evaluator"; chosen over `quick-validate.py`): validate the whole file against data-model §2 and exit 2 naming each bad record before any subject run, with the error shape in contracts/eval-run.md "Schema check".
- [ ] T029 [US2] Make `scripts/luna-eval` write `metrics.json` into each `run-<n>/` directory, derived from `events.jsonl` with the names confirmed in T005. The keys are exactly those in data-model §3: `tool_calls` (by kind), `total_tool_calls`, `retries` (a failed command re-run with identical argv), `invocation_errors` and `invocation_error_commands` (rule as in T024), `duplicate_actions`, `tokens` {`input`,`output`,`total`}, `completion_reason` ∈ `ok|no_output|usage_limit|error`, `model` and `effort` (the values `luna-eval` actually passed to codex), and `skills_read`. An event that is absent is recorded as `null`, never guessed (research R5).
- [ ] T030 [US2] Make `scripts/luna-eval` grade `skill_selected` assertions into `grading.json`. An item passes when the first owner `SKILL.md` in `metrics.json` `skills_read` matches `text`. Write each item as `{text, passed, evidence, type}` (data-model §3). Make T024 pass.
- [ ] T031 [US2] In `scripts/luna-eval`, keep exit codes 0/3/4/5 unchanged. On exit 3 or 5, keep completed runs. On a rerun, skip any `run-<n>/` that already has `timing.json` with exit 0 (contracts/eval-run.md, spec Edge Case).
- [ ] T032 [P] [US2] Update `.agents/skills/skill-creator/agents/grader.md` to grade `assertions[]` `{type,text}` for every type except `skill_selected`, which `luna-eval` grades. Keep `text`/`passed`/`evidence` on each item and add `type`. Add the top-level `task_outcome` (`pass|fail|blocked`) and `semantic_quality` = pass rate of that eval's `quality`-type assertions (passed / total, `null` when the eval has none), computed from the graded items. The grader assigns no separate score (data-model §3, FR-016).
- [ ] T033 [P] [US2] Update `.agents/skills/skill-creator/references/schemas.md`. The evals.json schema becomes data-model §2, and grading/metrics/timing become data-model §3 (`metrics.json` is this file's existing metrics schema plus `retries`, `invocation_errors`, `model`, `effort`). Remove the `expectations[]` and `{"query","should_trigger"}` shapes.
- [ ] T034 [US2] Update `.agents/skills/skill-creator/SKILL.md` so that "Running and evaluating test cases" calls `scripts/luna-eval` once per eval and config. Delete the "Description optimization" section and the `run-loop.py` / `run-eval.py` line (~460) (FR-012, FR-015, research R5).
- [ ] T035 [US2] Delete `.agents/skills/skill-creator/scripts/run-eval.py`, `run-loop.py`, `improve-description.py`, and `generate-report.py` (it only renders `run-loop.py` output). Keep `utils.py` (`package-skill.py` uses it). Then `rg --hidden "run-eval|run-loop|improve-description|generate-report" .agents/ AGENTS.md docs/ scripts/ tools/ tests/` and remove the remaining references, including `.agents/skills/vault-skill-factory/SKILL.md` line ~106.
- [ ] T036 [US2] Run a one-off conversion over all `.agents/skills/*/evals/evals.json`. The script is not committed (plan: VIII does not apply to one-offs). Each `expectations[]` string `s` becomes `{"type":"behavior","text":s}`, and `expectations` is removed. Rename `qualitative`→`quality` and `structural`→`structure`; keep `scope`, `handoff`, and `coverage` (FR-014). Preserve `core`, `subject_skill`, `trajectory_records`, and `principles`. `expected_output` stays optional, with no text invented (FR-013).
- [ ] T037 [US2] Add `"skill_name"` (equal to the directory name) to `.agents/skills/{session-beats,wiki-capture,wiki-context-pack,wiki-ingest,wiki-lint,wiki-query,wiki-update}/evals/evals.json` (FR-013)
- [ ] T038 [US2] Edit the Work-gate, chat-proposal approval, read-side mutation, and retired-path wording by hand, record by record, in the 13 files found by `rg -il "work gate|chat proposal|approval" .agents/skills/*/evals/evals.json`. This includes `.agents/skills/place-design/evals/evals.json` eval 1. Keep each assertion and phrase its current behavior positively (e.g. "writes without asking first") (FR-017, spec Edge Cases).
- [ ] T039 [US2] Add at least one `skill_selected` eval (`{"type":"skill_selected","text":"<dir name>"}`) to each of the six FR-003 owners fixed by Clarify (cae8bb44): `.agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/evals/evals.json`. Write each prompt from that skill's own ownership text (FR-003, FR-014, FR-015, SC-005).
- [ ] T040 [US2] Verify V-09 with `pytest tests/test_luna_eval.py` (schema over all 60 files and the Work-gate wording case pass) and V-11 with `pytest tests/test_policy_conflicts.py`.
- [ ] T041 [US2] Verify V-10. Run the `place-design` `skill_selected` record directly with `scripts/luna-eval ... --out /tmp/030/iteration-1`, then through the skill-creator workflow. Both run dirs must have the same files and keys (`timing.json`, `metrics.json`, `grading.json`), and the item must be `passed: true`. Then drain e-210 from `errors.md` with the current CLI (`error drain --id e-210 --cause-fixed true`, before T063), in the same commit as T027–T035 (research R3, FR-008).

**Checkpoint**: One evaluator and one checked schema exist, which is the prerequisite for US3 and US8

---

## Phase 5: User Story 3 - Feature 029 Baseline Evidence (Priority: P1)

**Goal**: A recorded `luna-eval` baseline with at least 10 cases across all nine categories, each carrying every FR-016 metric and its model/effort pair

**Independent Test**: Quickstart V-12

- [ ] T042 [US3] Select at least 10 existing owner eval records covering all nine US3 categories: owner completion, specific blocking, scope preservation, read isolation, retrieval convergence, child handoff, parent resumption, write finalization, and recovery. List category → `<skill>:<eval id>` in `specs/029-agent-loop-closure/quickstart.md`.
- [ ] T043 [US3] Run each selected case with `scripts/luna-eval --skill <dir> --eval <id> --out /tmp/030/baseline/iteration-1` at `luna-eval`'s default model and effort (constitution XXVI). Confirm each run's `metrics.json` records `model` and `effort` and that all runs share one pair; SC-012 comparisons must reuse it (FR-019). On exit 3 or 5, rerun only the missing cases (T031).
- [ ] T044 [US3] Record each case in `specs/029-agent-loop-closure/quickstart.md` with model, effort, task outcome, tool calls, retries, duplicate actions, tokens, latency, completion reason, and semantic quality. Latency comes from `timing.json`; tool calls, retries, tokens, model, and effort from `metrics.json`; task outcome and semantic quality (the `quality`-assertion pass rate, or `null`) from `grading.json` (FR-016, FR-019).
- [ ] T045 [US3] Check off T003, T011, T018, T030, T037, T044, T046, T047, and T049 in `specs/029-agent-loop-closure/tasks.md`, each with a pointer to its evidence (FR-019, SC-006)

**Checkpoint**: A baseline exists for the SC-012 comparisons

---

## Phase 6: User Story 4 - Scoped Lint Costs Scoped Work (Priority: P1)

**Goal**: Identity reads and compares only changed or selected pages and their candidates, using a derived index loaded through `lint_cache.py`. Findings are identical, and no code picks a canonical page.

**Independent Test**: Quickstart V-05, V-06, V-07, V-08, V-08b, and V-08c

### Tests for User Story 4

- [ ] T046 [US4] Add identity-index tests to `tests/test_wiki_ops.py`, using a temp vault built in the test:
  - (a) cold and warm `scan_identities` output is identical.
  - (b) editing one page refreshes its row: a `(size, mtime_ns)` change triggers a rehash, and the findings equal a cold run.
  - (c) an index containing `{`, or with a changed `version`, is rebuilt.
  - (d) rows for deleted paths are dropped, and `pairs` for vanished hashes are pruned.
  - (e) a scoped run reports `compared == |selected ∪ candidates|`, which is less than the page count.
  - (f) `resolve_identity` and `_path_for` return the same results from the index as from a cold walk.
  - (g) a lint rules-digest change invalidates `lint-cache.json` entries but leaves identity rows and `pairs` reused (`index.misses == 0`).
  - (h) an above-threshold pair is only listed in `candidates` with `status: ambiguous`; no winner is chosen.

  Confirm (e) and (g) fail before T047–T049.

### Implementation for User Story 4

- [ ] T047 [US4] Add load and save for `wiki/_meta/identity-index.json` to `tools/wiki_ops/lint_cache.py`, reusing its `cache_path`, `sha256_file`, versioned load, and atomic writer (research R8; not in `identity.py`). Use data-model §4 exactly:
  - Header: `version`, `manifest_sha256`.
  - Rows keyed by path: `size`, `mtime_ns`, `content_sha256`, `stem`, `title`, `type`, `lifecycle`, `aliases`, `redirects_to`, `body_len`, and `profile` (the body character `Counter`).
  - `pairs`: `SequenceMatcher.ratio()` keyed `"<sha_a>|<sha_b>"` (sorted content hashes); "Entries whose hashes no longer match any row are pruned on save."
  - Validity: "a row is reused when `(size, mtime_ns)` matches, or when the rehashed `content_sha256` matches. A changed `version`, a JSON error, or a changed `manifest_sha256` refreshes the affected state; version and parse errors rebuild everything."
- [ ] T048 [US4] In `tools/wiki_ops/identity.py`, replace the whole-vault read in `scan_identities` with candidate selection from index rows (research R4 steps 1–5; `os.scandir` + `stat` walk). Candidates share the same `type`, have no redirect, and meet one of: a norm title or alias match, a stem match, shared manifest provenance with stem ratio > 0.7, a merge transition, or the cached profile prefilter `2·|A∩B| / (lenA+lenB) > 0.6` (FR-024 as clarified). Make `resolve_identity` (mutation gate) and `_path_for` read the index too. Thresholds only list candidates and set `status: ambiguous`, which gates mutations; resolution goes through `.agents/skills/wiki-dedup/SKILL.md` and `.agents/skills/wiki-lint/SKILL.md` (plan "Judgments").
- [ ] T049 [US4] Add the pair-ratio cache to `tools/wiki_ops/identity.py`: read `pairs` through `lint_cache.py`, run `SequenceMatcher` only on candidate pairs that are uncached, and read only those candidate bodies (research R4 step 6, R7). Make T046 pass.
- [ ] T050 [US4] Add `"identity": {"status","ambiguous","scanned","compared","index":{"hits","misses"}}` to `scripts/wiki-lint --json` output, where `scanned` = selected and `compared` = |selected ∪ candidates| (data-model §4, SC-007)
- [ ] T051 [US4] Delete `scripts/wiki-identity` (research R8). Move `tests/test_wiki_ops.py` line 109 (drop it from the `--help` contract loop), line 115 (`scan --json` ambiguous case → call `scan_identities` or read the `wiki lint` `identity` block), and line 514 (`resolve` case → call `resolve_identity`) onto the library or `wiki lint`.
- [ ] T052 [US4] Keep `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` tracked as FR-028 bookkeeping (data-model §4 "Tracking"): no `.gitignore` change, and each is committed with the change that caused it. Commit the first generated `identity-index.json` with T047–T050.
- [ ] T053 [US4] Verify V-05 (read run 1 `timing.duration_ms` < 5000, `identity.compared` far below the page count; run 2 `cache.hits: 1`), V-06 (diff against `/tmp/030/identity-before.json` and `/tmp/030/lint-before.json` from T002, allowing only the findings added by T016 and removed by T018), and V-07 (corrupt index rebuilt). Record the V-05 numbers in the `specs/030-self-improving-architecture/quickstart.md` V-05 row.
- [ ] T054 [US4] Run V-08: with the lint cache and identity index current, edit 1–3 pages on a scratch branch, run `scripts/wiki health`, and read `timing.duration_ms` (< 10 000). Then run V-08c: delete both `wiki/_meta/identity-index.json` and `wiki/_meta/lint-cache.json` on the scratch branch, run `scripts/wiki health`, confirm it finishes with no harness timeout, and record its `timing.duration_ms` next to the SC-006 baseline in `specs/029-agent-loop-closure/quickstart.md` (after T044; no bound).
- [ ] T055 [US4] Run V-08b: on a scratch branch with the identity index current, change the rules digest (e.g. add a comment line to `.vale.ini`), run `scripts/wiki health`, and read `timing.duration_ms` (< 50 000), `lint.cache.misses` (≈ page count), and `identity.index.misses` (== 0). Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-08b row (pre-change reference 82.3 s). Discard the scratch branch.
- [ ] T056 [US4] Drain identity entries e-206, e-208, and e-213 from `errors.md` with the current CLI (`error drain --id <id> --cause-fixed true`, before T063), in the same commit as T046–T052 (FR-008)

**Checkpoint**: Phase 1 is complete: green checks, one linter, one evaluator, a baseline, and scoped identity

---

## Phase 7: User Story 5 - Friction Is Fixed at the Source, Then Work Resumes (Priority: P2)

**Goal**: Shared guidance states the friction rule once, as a branch of the capability loop

**Independent Test**: Quickstart V-17 (seeded friction, at least 4/5 cold subjects fix the source, add a regression, and finish)

- [ ] T057 [P] [US5] Add one friction-rule paragraph to `AGENTS.md` next to "Capability loop" (line ~72): act → friction → identify cause → fix the authoritative source (smallest change) → verify → continue the original task. Add no new workflow, command, or skill (FR-001, FR-002, FR-005).
- [ ] T058 [P] [US5] Add the friction branch (act → friction → fix source → re-observe → continue) to the capability loop in `docs/agents/hybrid-sdd.md`, linking to the `AGENTS.md` paragraph rather than restating it (FR-001, constitution XVI)
- [ ] T059 [US5] Run V-17. On a scratch branch, make one owner `SKILL.md` name a retired command path, then run 5 cold `scripts/luna-eval` subjects on one of that owner's evals. At least 4/5 must fix the source, add a regression, and finish the owner task with no new `errors.md` entry. Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-17 row. Discard the scratch branch. This runs after T068 so the new ledger format is in place.

**Checkpoint**: Friction handling is documented in one place and behaviorally proven

---

## Phase 8: User Story 6 - Recurring Causes Trend to Zero (Priority: P2)

**Goal**: `errors.md` holds only open four-field entries. Exact duplicates attach, the agent decides broader same-cause attaches, fixes drain, and recurrence is part of `error list`.

**Independent Test**: Quickstart V-13, V-14, and V-15

### Tests for User Story 6

- [ ] T060 [US6] Add ledger tests to `tests/test_error_ledger_repairs.py`. Each one drives `scripts/error-ledger.py` via subprocess on a scratch `errors.md` and covers:
  - Exact-match auto-attach: `append` with the same `source` and identical whitespace-trimmed `cause` gives `attached`; a reworded cause on the same source gives `created` (a new id); a different `source` gives `created`.
  - The report carries the matched `id` and `occurrence_index` (and `occurrences`); a repeated identical occurrence gives `already_done`.
  - `--attach e-N` on the same source gives `attached`. `--attach` across sources, or for an unknown id, exits 2 with `error`/`hint`/`example` and writes nothing (FR-007 refusal regression).
  - `detach --id e-N --index k` gives `detached`; repeating it gives `already_done`; detaching the only occurrence exits 2 with a hint to use `drain`.
  - `--cause-fixed` on any subcommand is rejected: exit 2 with `"error":"--cause-fixed was removed"`, a hint, and the `error drain --id e-212` example.
  - `list` returns exactly `{entries, recurrence: {total, by_sitting}, missing_sources}` with correct totals, and `--ids-only` prints ids.
  - A missing `--source` exits 2 with an example; `--source` must be an existing repo path or `external:<name>`.
  - `drain` gives `drained` then `already_done`; `--dry-run` on append, drain, and detach writes nothing and returns `planned`.
  - Commands work from a non-root cwd.

  Plan default, error-ledger CHK011: an "identical occurrence" means the same `sitting` and `detail`. Confirm the tests fail before T061.

### Implementation for User Story 6

- [ ] T061 [US6] Rework the entry model in `scripts/error-ledger.py` (data-model §1). Keep the `# Error ledger` heading, a blank line, then one JSON object per line with sorted keys. The fields are exactly `id` (`"e-<n>"`, unique, new ids from `next_error_id`), `cause` ("Never rewritten when an occurrence is added"), `source` (repo-relative path or `external:<name>`), and `evidence` ("list of `{sitting, detail}`, length ≥ 1"). There is no `status` or `cause_fixed`. The only automatic match is the same `source` with `cause.strip()` equal; no normalized key or other heuristic (FR-007, research R3).
- [ ] T062 [US6] Implement `error append --source S --cause C --sitting X [--detail D] [--attach e-N] [--dry-run]` in `scripts/error-ledger.py`, returning `{"status":"attached"|"created"|"already_done","id","occurrence_index","occurrences"}`; `detail` defaults to `C`. Check `--source` deterministically (existing repo path or `external:<name>`). Refuse `--attach e-N` when e-N's `source` differs or e-N is unknown, with the contracts/error-ledger.md error shape and nothing written.
- [ ] T063 [US6] In `scripts/error-ledger.py`: implement `error drain --id e-N [--dry-run]` (`drained|already_done`) and remove the `--cause-fixed` flag, so passing it exits 2 with the contract's hint and example; make `error list [--ids-only]` return `{entries, recurrence, missing_sources}` (FR-009: `total = Σ(len(evidence) − 1)`, `by_sitting` counts non-first occurrences); and add `error detach --id e-N --index k [--dry-run]` (`detached|already_done`, refusing to remove the only occurrence). Add no `recurrence` or `migrate` subcommand.
- [ ] T064 [US6] Switch `scripts/error-ledger.py` to `tools/wiki_ops/cli.py` `repo_root` so `errors.md` is found from any cwd. Add an `--help` Examples block that shows `python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …"` (FR-027, FR-032). Make T060 pass.
- [ ] T065 [US6] Migrate `errors.md` with a one-off, uncommitted conversion (research R3, FR-010, V-13; round-3 gap 3 resolved): drop `status == "drained"` lines, map each open entry to `{id, cause, source, evidence:[{sitting, detail: cause}]}`, and concatenate `evidence` into the kept id for each merge group. The merge groups and `source` values are agent-supplied input data: confirm research R3's proposal against the cause text (any OMP, Vale, or identity entry still open after T012, T014, T056; e-168 → `.agents/skills`, e-201/e-203/e-217 → `.agents/skills/wiki-lint/SKILL.md`, e-202 → `scripts/wiki`), with no group ids hardcoded in `scripts/error-ledger.py`. In the same commit as T061–T064, update the two `error list` callers in `scripts/wiki` (lines ~201 and ~587) to read `entries`.
- [ ] T066 [P] [US6] Rewrite `AGENTS.md` "Error ledger" (line ~196): fix and verify the source, then continue; `append` only when the fix cannot land in the current task; `drain --id e-N` goes in the same commit as the verified fix. Add the same-cause rule (attach with `--attach e-N` when the fix for e-N would also remove this failure; otherwise create) and the undo `error detach --id e-N --index k`. Remove `--cause-fixed true` from every documented invocation (contracts/error-ledger.md, research R3).
- [ ] T067 [P] [US6] Rewrite `.agents/skills/wiki-lint/SKILL.md` line ~47 from "record the mismatch in errors.md" to "reconcile first, record only if unresolved", linking to `AGENTS.md` rather than restating it (constitution XIX)
- [ ] T068 [US6] Verify V-13 (`python3 scripts/error-ledger.py error list` loads with no `status`/`cause_fixed`, no drained entry, one id per agent-chosen group, no two entries sharing `(source, cause.strip())`, `missing_sources: []`), V-14 on a scratch copy, and V-15/FR-009 through `error list` `recurrence` (`{"total": n, "by_sitting": {...}}`). Record the starting total in the `specs/030-self-improving-architecture/quickstart.md` V-15 row. The SC-009 20-sitting window stays an assumption tracked after merge (resolved gap 5), not a gate.

**Checkpoint**: The ledger is deduplicated, and its agent guidance matches "fix first"

---

## Phase 9: User Story 7 - Wiki Commands Agents Can Drive Headlessly (Priority: P2)

**Goal**: The `scripts/wiki` subcommands meet contracts/wiki-cli.md (FR-027–FR-039) through one discovery helper, and health reports facts only

**Independent Test**: Quickstart V-16 and SC-010

### Tests for User Story 7

- [ ] T069 [US7] Add one subprocess test per rule class to `tests/test_wiki_cli.py` (FR-039):
  - Discovery from a non-repo cwd, the `vault` key, and the `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` precedence; `repo_root` comes from the package location.
  - Bare `wiki` lists exactly `lint`, `lint fix`, `query`, `health`, `mutate`, `repair` and exits 0.
  - `wiki <sub> --help` shows only that subcommand plus an `Examples:` block; `scripts/wiki-lint --help` names `wiki lint --help`.
  - No prompts with stdin closed.
  - `--stdin` and `--paths-only`.
  - Options before or after positionals.
  - A bare `fix` token among lint paths (`wiki lint entities/place/Belumara.md fix`) exits 2 with `"error":"'fix' is not a lint path"`, `"hint":"lint fix is a subcommand"`, and `"example":"wiki lint fix entities/place/Belumara.md"`, and lints or writes nothing.
  - Exit 2 with keys `status`/`error`/`hint`/`example`/`list_valid` for each of: an unknown path, a `wiki/`-prefixed path, a scope without `:`, an unknown scope kind, and an unsupported option.
  - `--dry-run` returns `planned` and writes nothing; a second identical run returns `"changed": []` and `"status": "already_done"`.
  - Success keys `status`, `vault`, `changed`, `counts`, `timing.duration_ms`, `next`; `health` `next` equals the first `build_focus` row.
  - The slow-checker notice on stderr is exactly the plain report `wiki lint: slowest checker <script> <ms> ms; next <script> <ms> ms`, with no instruction.

  Confirm the tests fail before T070.

### Implementation for User Story 7

- [ ] T070 [US7] Make `tools/wiki_ops/cli.py` the only discovery helper: `repo_root` resolves from the package location (not the cwd), and `resolve_vault` uses `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` > `~/.obsidian-wiki/config`, with `"vault": "<absolute path>"` in every result (FR-027, research R6/R8). Switch `scripts/wiki-lint` `consolidate_main` (`Path.cwd() / vault`, line ~352), the `tools/lint_wiki.py` default (`Path("wiki")`, line ~315), and `scripts/luna-eval` (confirm T027 uses the default) to it. Make `scripts/wiki-lint --help` point at `wiki lint --help`, and point lint usage in `docs/creative-linting.md`, `docs/architecture.md`, and `README.md` at `wiki lint`.
- [ ] T071 [US7] In `scripts/wiki`, make bare `wiki` print one line per subcommand. Give each subcommand its own `--help` with an `Examples:` block that uses the real invocations from contracts/wiki-cli.md "Examples blocks" (FR-031, FR-032).
- [ ] T072 [US7] Make `lint fix` an argparse subparser under `lint` in `scripts/wiki` (replacing the positional check at line ~674), and allow options anywhere (intermixed parsing). There is no positional `fix` alias: a bare `fix` token exits 2 with the FR-035 object, `hint` "lint fix is a subcommand", and the example `wiki lint fix <paths>` (`wiki lint fix entities/place/Belumara.md`) (FR-034, contracts/wiki-cli.md "Shape").
- [ ] T073 [US7] Add `--stdin` to `scripts/wiki`: newline-separated paths for lint, lint fix, and health, and one JSON payload for mutate and repair. Add `--paths-only` output. No command prompts, and a missing required input is an error (FR-030, FR-033).
- [ ] T074 [US7] Implement the FR-035 error object in `scripts/wiki` and `tools/wiki_ops/cli.py`: exit 2, JSON on stdout with `status`, `error`, `hint`, `example`, and `list_valid`, and the same message on stderr. Cover the six contract cases, and list the allowed scope kinds `files|directory(dir)|entity_type(type)|identity_set|changed|bundle`.
- [ ] T075 [US7] Make `lint fix`, `mutate`, and `repair` in `scripts/wiki` accept `--dry-run`, which returns `"planned": [...]` and writes nothing. A second identical run returns `"changed": []` and `"status": "already_done"`. Add no confirmation prompt, so no `--yes` flag is needed (FR-036, FR-037).
- [ ] T076 [US7] Make every `scripts/wiki` success result include `status`, `vault`, `changed`, `counts` (`before`/`after`), `timing.duration_ms`, and `next`. For `health`, report facts only: `focus` is `tools/wiki_ops/health.py` `build_focus` (fixed order lint → remorph → layout → open ledger entries, up to 5), and `next` is its first row, reported as a fact. Replace `_tune`'s "Fix that checker this sitting." (line ~231) with the plain report `wiki lint: slowest checker <script> <ms> ms; next <script> <ms> ms` (FR-038, FR-029). Make T069 pass.
- [ ] T077 [P] [US7] Add an `--help` Examples block to `scripts/luna-eval` showing `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/pd/iteration-1`, and make a missing required flag exit 2 with an example (FR-032, FR-035)
- [ ] T078 [US7] Verify V-16 (bare `wiki`, `wiki lint --help`, a bad path and a bare `fix` token each giving exit 2 with `hint`/`example`, `--scope dir`, `wiki lint fix dir:entities/place --dry-run` twice with the same plan, then `already_done` after one real run). Then check SC-010 with the `invocation_errors` metric (data-model §3, quickstart V-16): write one task per `scripts/wiki` subcommand (`lint`, `lint fix`, `query`, `health`, `mutate`, `repair`) as records in a scratch, uncommitted `/tmp/030/sc010/evals/evals.json`, each prompt holding only the `scripts/wiki --help` output and the task. Run each with a cold `scripts/luna-eval` subject (`--config without_skill`, default model and effort, no other context). Every run's `metrics.json` must have `invocation_errors: 0` (list `invocation_error_commands` otherwise), and re-running each mutating command must produce 0 additional changes (`already_done`). Do not use owner evals or `retries` for SC-010. Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-16 row.

**Checkpoint**: Phase 2 is complete

---

## Phase 10: User Story 8 - Incumbent vs Candidate Instruction Promotion (Priority: P3)

**Goal**: At least one owner skill is promoted by an agent following `skill-creator`, from a report that states regressions and medians but no verdict (SC-012)

**Independent Test**: Quickstart V-18

- [ ] T079 [US8] Change `.agents/skills/skill-creator/scripts/aggregate-benchmark.py` to report only, per eval, task-outcome regressions and assertions that passed for the incumbent and fail for the candidate, plus the medians of `total_tool_calls`, `retries`, `tokens.total`, and latency (from `timing.json`). It prints no verdict and no mean ± stddev, and refuses a comparison whose runs differ in `model` or `effort` (data-model §3, FR-044, contracts/eval-run.md "Promotion report").
- [ ] T080 [US8] Add the promotion rule to `.agents/skills/skill-creator/SKILL.md` (FR-044, SC-012): one run per config on the same eval ids, with the same `model` and `effort` as the FR-019 baseline; refuse on any worse per-eval task outcome or any incumbent-passing assertion that now fails; promote only on a lower median of tool calls, retries, or tokens with none of the three higher; do not use mean ± stddev. Keep the skill no longer than before (SC-013) by replacing the text it supersedes.
- [ ] T081 [US8] Pick one of the six owners. Draft one small candidate edit to `.agents/skills/<owner>/SKILL.md` in the working tree, drawing on its US3 baseline run dirs under `/tmp/030/baseline/`: the current instruction, failed and successful tasks, tool results, assertion failures, user corrections, and token/tool-call cost (FR-043)
- [ ] T082 [US8] Snapshot the incumbent skill directory from HEAD to `/tmp/030/incumbent/<owner>/` (`git archive HEAD .agents/skills/<owner> | tar -x -C /tmp/030/incumbent`). Run `scripts/luna-eval --config old_skill --subject-skill /tmp/030/incumbent/.agents/skills/<owner>` and `--config with_skill` once each on the same eval ids with the baseline `--model`/`--effort`, plus the cross-skill baseline cases from T042 (FR-042, spec Edge Case).
- [ ] T083 [US8] Run `aggregate-benchmark.py` on the two configs. Decide keep or refuse by following the rule in `skill-creator/SKILL.md` (T080); on refuse, `git checkout -- .agents/skills/<owner>/SKILL.md`. Record the decision and cite the skill in the `specs/030-self-improving-architecture/quickstart.md` V-18 row.

**Checkpoint**: The promotion rule has been exercised end to end

---

## Phase 11: User Story 9 - Skills Stay Small; Procedure Moves into Tools (Priority: P3)

**Goal**: The six owner skills answer the five FR-040 questions and shrink, because deterministic procedure now lives in tools while every judgment stays in the skill

**Independent Test**: Quickstart V-19

- [ ] T084 [US9] Record `wc -l .agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/SKILL.md` to `/tmp/030/skill-lines-before.txt`, and snapshot those dirs to `/tmp/030/incumbent-us9/` for old_skill runs
- [ ] T085 [US9] Make `scripts/manifest.py` report the manifest facts named in recorded trajectories (facts only, no interpretation), with a regression in `tests/test_wiki_ops.py` (FR-029, FR-011)
- [ ] T086 [US9] Move deterministic repair bookkeeping (fixes with exactly one correct output) into `wiki lint fix` in `scripts/wiki` and `tools/wiki_ops/cli.py`, with a regression in `tests/test_wiki_cli.py` (FR-029, FR-011). Repair choices stay in the skills.
- [ ] T087 [P] [US9] Shorten `.agents/skills/place-design/SKILL.md`. Remove only deterministic text now covered by T070, T076, T085, and T086 (path discovery, health facts, manifest facts, repair bookkeeping). Keep every judgment, and make sure the five FR-040 answers are present.
- [ ] T088 [P] [US9] Shorten `.agents/skills/faction-design/SKILL.md` in the same way as T087
- [ ] T089 [P] [US9] Shorten `.agents/skills/session-beats/SKILL.md` in the same way as T087
- [ ] T090 [P] [US9] Shorten `.agents/skills/run-guide/SKILL.md` in the same way as T087
- [ ] T091 [P] [US9] Shorten `.agents/skills/wiki-query/SKILL.md` in the same way as T087
- [ ] T092 [P] [US9] Shorten `.agents/skills/wiki-lint/SKILL.md` in the same way as T087 (it builds on T067, and keeps the `Deprecated.*`, broken-image, and identity judgments)
- [ ] T093 [US9] Verify V-19. Line counts must not exceed `/tmp/030/skill-lines-before.txt`. Rerun each skill's evals with `scripts/luna-eval` `--config with_skill` against `--config old_skill --subject-skill /tmp/030/incumbent-us9/...`, report with `aggregate-benchmark.py`, and apply the `skill-creator` rule (T080). Revert any skill it refuses.

**Checkpoint**: Phase 3 is complete

---

## Phase 12: Polish, Consolidation Check & Cross-Cutting Concerns

- [ ] T094 Add a case to `tests/test_policy_conflicts.py` for the new `scripts/hybrid-sdd-check.py diff` subcommand on fixture input: it fails when an added file is missing from a plan's "New files" table, fails when a path from the "Deleted or folded" table is still referenced in a maintained surface (`AGENTS.md`, `docs/`, `.agents/`, `scripts/`, `tools/`, `tests/`, `package.json`, `README.md`; completed specs excluded per round-3 gap 1), and passes otherwise. Confirm it fails before T095.
- [ ] T095 Add the `diff --plan <plan.md> --base <ref>` subcommand to `scripts/hybrid-sdd-check.py` (plan "New files", SC-014 a/c; diagnostic only, it reports and decides nothing). Make T094 pass.
- [ ] T096 Run V-20 (SC-014): `python3 scripts/hybrid-sdd-check.py diff --plan specs/030-self-improving-architecture/plan.md --base main`. It must pass: the only added files are `wiki/_meta/identity-index.json` and `tests/test_luna_eval.py`, and none of the 10 deleted paths (`scripts/wiki-identity`, `scripts/lint-wiki-write`, `scripts/lint-obsidian-markdown`, `scripts/lint-literal-newlines`, `scripts/vale-vocab`, `tools/check_wiki_pages.py`, and skill-creator's `run-eval.py`, `run-loop.py`, `improve-description.py`, `generate-report.py`) exists or is referenced in maintained surfaces. Re-run V-04c and V-04d on the same tree. SC-014 (b), (d), and (e) are Review judgments against plan "Simplify and consolidate".
- [ ] T097 Confirm the `<!-- SPECKIT START -->`…`<!-- SPECKIT END -->` block in `AGENTS.md` (line ~584) still points at `specs/030-self-improving-architecture/plan.md`
- [ ] T098 Run the full `pytest -q` and compare it with `/tmp/030/pytest-before.txt`. It must show no new failures and no Vale E100.
- [ ] T099 Run `git diff --stat`. Only after all scratch timing runs (T053, T054, T055, T078) are done, revert the FR-028 bookkeeping files `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` where their changes are measurement state rather than part of an intended change.
- [ ] T100 Re-run quickstart V-01, V-03, V-04b, V-04c, V-04d, V-09, V-11, V-15, V-16, and V-20 on the final tree, and fill in any empty result rows in `specs/030-self-improving-architecture/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup. T004 gates US5 and US6. T005 gates T029.
- **Phase 1 stories (US1–US4)** come before Phase 2 stories (US5–US7), which come before Phase 3 stories (US8–US9). This order is binding (spec Assumptions).
- **Polish (Phase 12)**: After all stories

### User Story Dependencies

- **US1 (P1)**: After Foundational. There are no story dependencies. It is the MVP.
- **US2 (P1)**: After US1, because eval runs need green checks. T025 and T023/T026 can start any time.
- **US3 (P1)**: After US2, because it needs `metrics.json` and `grading.json` (T029–T032)
- **US4 (P1)**: After US1 (Vale fixed, lint rules folded). It is independent of US2 and US3, except T054, which writes after T044.
- **US5 (P2)**: T057 and T058 are independent. T059 needs US2 (luna-eval) and T068 (new ledger format).
- **US6 (P2)**: After US1, US2, and US4, whose drains (T012, T014, T041, T056) use the current CLI and must land before T063 removes `--cause-fixed` and before migration (T065)
- **US7 (P2)**: After US4 (the `wiki-lint` output shape) and US6 (`scripts/wiki` `error list` callers). T077 needs T027–T031.
- **US8 (P3)**: After US2, US3, and US5
- **US9 (P3)**: After US7 (T070, T076), US3, and US8 (T080). T092 comes after T067.

### Within Each User Story

- Tests are written first and must fail. Then comes implementation, then the ledger drain in the same commit as the fix, then quickstart verification.
- Tasks on the same file run in sequence (e.g. T027→T031 `scripts/luna-eval`; T061→T064 `scripts/error-ledger.py`; T071→T076 `scripts/wiki`; T048→T049 `tools/wiki_ops/identity.py`; T009 and T010 share `tests/test_wiki_ops.py`).

### Parallel Opportunities

- T003 runs alongside T002.
- US1: T006 ∥ T007 ∥ T008 ∥ T009 (then T010 in the same file). The OMP track (T011–T012) is independent of the Vale track (T013–T015) and the one-linter track (T016–T020), apart from sharing `errors.md` at commit time.
- US2: T023 ∥ T025 ∥ T026 ∥ T032 ∥ T033 ∥ the `scripts/luna-eval` chain T027–T031.
- US4 can run alongside US2 and US3 once US1 is done.
- US5: T057 ∥ T058. US6: T066 ∥ T067.
- US7: T077 ∥ T070–T076.
- US9: T087–T092 in parallel (one skill each).

---

## Parallel Example: User Story 1

```bash
Task: "T006 OMP checker case in tests/test_policy_conflicts.py"
Task: "T007 Vale regression in tests/test_wiki_cli.py"
Task: "T008 vale_adapter human_repair case in tests/test_creative_lint.py"
Task: "T009 folded lint rules in tests/test_wiki_ops.py"
```

## Parallel Example: User Story 2

```bash
Task: "T025 Rewrite 026 references in specs/026-agent-autonomy-scope/*"
Task: "T032 Update .agents/skills/skill-creator/agents/grader.md"
Task: "T033 Update .agents/skills/skill-creator/references/schemas.md"
```

## Parallel Example: User Story 9

```bash
Task: "T087 Shorten .agents/skills/place-design/SKILL.md"
Task: "T088 Shorten .agents/skills/faction-design/SKILL.md"
Task: "T089 Shorten .agents/skills/session-beats/SKILL.md"
Task: "T090 Shorten .agents/skills/run-guide/SKILL.md"
Task: "T091 Shorten .agents/skills/wiki-query/SKILL.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup and Phase 2 Foundational
2. Phase 3 (US1): green OMP and Vale checks with 9 ledger entries drained, `Deprecated.*` as judgment repairs, and `wiki lint` as the only linter
3. **STOP and VALIDATE**: V-01 to V-04d

### Incremental Delivery

1. US1 → US2 → US3 → US4 (Phase 1 coherent baseline; each checkpoint is independently verifiable)
2. US5 → US6 → US7 (Phase 2 close the loop)
3. US8 → US9 (Phase 3 optimize, measured against the US3 baseline)
4. Phase 12: SC-014 diff check (V-20), then final reruns

### Open gaps

- Resolved by cae8bb44 and b14ea71b: plan round-1/2 gaps 1–6 (identity prefilter candidates, exact-match same cause, optional `expected_output`, fixed assertion vocabulary, SC-009 window as an assumption, tracked FR-028 bookkeeping), the six-owner set (eval-run CHK006), identity-index tracking (performance CHK006), and `resolve_identity`/`_path_for` scope (performance CHK021). Resolved by df3e5c7c: wiki-cli CHK011 (no positional `fix` alias).
- Plan default kept: error-ledger CHK011, an identical occurrence means the same `sitting` + `detail` (T060).
- Round-3 Clarify gaps, resolved at plan 922a0796 (plan default kept, no extra task): (1) SC-014 (c) covers maintained surfaces only; completed specs such as `specs/024-*` and `specs/025-*` stay as records. (2) The 21 broken image links are `human_repair` agent work under `wiki-lint`, not in this feature's tasks. (3) The one-off, uncommitted migration satisfies FR-010's "first run". (5) `scripts/vale-vocab` and `tools/check_wiki_pages.py` are folded and deleted (T019, T020).
- Round-3 Clarify gap 4, pending with Nick: the `wiki-lint --consolidate` `base_confidence > 0.7` threshold stays out of scope by default (FR-046 rule 5 applies only where this feature touches such code). No task.

---

## Notes

- [P] tasks touch different files and have no dependency on incomplete tasks.
- Every fix lands with its regression and its `errors.md` drain in one commit (FR-008, FR-011).
- Scratch output under `/tmp/030/` is never committed. FR-028 bookkeeping files are committed with the change that caused them and reverted after scratch measurement runs.
