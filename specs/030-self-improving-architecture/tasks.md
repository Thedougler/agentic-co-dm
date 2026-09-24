---

description: "Task list for feature 030: Self-Improving Architecture"
---

# Tasks: Self-Improving Architecture

**Input**: Design documents from `/specs/030-self-improving-architecture/` (plan.md at a95238e6, consolidated under FR-046/SC-014 and FR-047/SC-015; spec.md at c6f53f02; constitution v7.0.0 at f489409d). Line numbers are at the branch head after 4d2b68c5 (research R9 notes the shifts); locate by symbol if they drift.

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ (wiki-cli, error-ledger, eval-run), quickstart.md, checklists/

**Tests**: The spec asks for them. FR-011 requires a regression for every fixed failure, FR-021 an OMP checker test, FR-039 one test per CLI rule class, and FR-007 a test for the cross-source `--attach` refusal. Write each test first and confirm it fails before the fix. New tests go in the existing file for each module (plan "Testing"); the only new test file is `tests/test_luna_eval.py`.

**Consolidation (binding, FR-046/SC-014, FR-047/SC-015)**: every task edits the module that owns the concern. Code only detects, measures, checks, indexes, reports, or applies a fix with exactly one correct output; every judgment stays in the skill named in plan "Judgments and their governing skill". 2 files are added and 10 are deleted (plan "Simplify and consolidate"). FR-047 replaces page lifecycle, promotion, and confidence with Nick's three-rule canon, owned only by `.agents/skills/llm-wiki/SKILL.md`; it adds nothing and deletes 10 test fixtures, rules `CANON001` and `CANON002`, and the `canon` rule category (plan "Wiki canon", research R9).

**Open gaps**: The plan's round-1/2 spec gaps 1–6 are resolved by cae8bb44 and b14ea71b, and checklists/wiki-cli.md CHK011 (positional `fix` alias) is resolved by df3e5c7c: there is no alias. Round-3 Clarify gaps 1, 2, 3, and 5 are resolved (plan 922a0796), and gap 4 (consolidate promotion) is superseded by FR-047. Round-4 gaps 1–4 are resolved by Clarify (spec c6f53f02, plan 887e6c47). Nothing else is pending (see "Open gaps" at the end). One item keeps a Plan default: error-ledger CHK011 (T072). spec.md and plan.md are not edited here.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US9)
- Paths are repo-relative (single repository, no new directories; plan "Structure Decision")

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Box environment and pre-change baselines that later parity checks diff against

- [X] T001 Provision `.venv/` per quickstart.md "Prerequisites": `uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0 pytest`, then `export PATH="$PWD/.venv/bin:$PATH"` and `export OBSIDIAN_VAULT_PATH="$PWD/wiki"`. No tracked file changes.
- [X] T002 Capture pre-change baselines into `/tmp/030/`. Temporarily remove `CoDM` from `.vale.ini` in the working tree only, as in plan "Measurements taken". Write the V-06 `scan_identities` dump to `/tmp/030/identity-before.json`, whole-vault `scripts/wiki lint` findings to `/tmp/030/lint-before.json`, `scripts/lint-obsidian-markdown` whole-vault findings to `/tmp/030/obsidian-md-before.txt` (reference 519 table pipes / 21 broken images), and `./scripts/wiki-reveal --count --json` to `/tmp/030/reveal-count-before.json` (V-04d). Then revert `.vale.ini` and the FR-028 bookkeeping files `wiki/_meta/lint-cache.json` and `styles/config/vocabularies/CoDM/accept.txt` with `git checkout --`, because this is scratch measurement state.
- [X] T003 [P] Record the pre-change test status: `pytest -q > /tmp/030/pytest-before.txt` (note any failures from the known Vale E100)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Confirm the dependencies the plan relies on before any story lands

- [X] T004 Confirm that `.specify/memory/constitution.md` is v6.0.1 or later and that principle XIII allows fix-verify-continue (plan Constitution Check, "XIII … dependency met"). Stop and report if it does not, because this blocks US5 and US6.
- [ ] T005 Confirm the codex `--json` event names (research R5 "To verify"). Run `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/030/probe/iteration-1` and inspect `/tmp/030/probe/*/with_skill/run-1/events.jsonl` for `item.completed` (`command_execution`/`file_change`, including the exit code and stdout/stderr fields needed for `invocation_errors`) and `turn.completed.usage`. Also note where the codex `--model`/`--effort` values `luna-eval` passes are available. Write the real names to `/tmp/030/event-names.txt` for T041.

**Checkpoint**: Environment, baselines, and event names are known, so the user stories can start

---

## Phase 3: User Story 1 - Green Baseline Checks (Priority: P1) 🎯 MVP

**Goal**: The OMP checker and scoped Vale lint pass on the correct config, their ledger entries are drained, `Deprecated.*` findings are judgment repairs, and `wiki lint` is the only linter (the side lint scripts and duplicate tools are folded in and deleted), and the wiki runs on the three-rule canon with the lifecycle machinery removed

**Independent Test**: `scripts/check-omp-baseline.sh` passes on the current `.omp/config.yml`, scoped `wiki lint` on one page shows no `CoDM` E100, the folded scripts are gone, no page, template, contract, skill, or code path carries lifecycle/confidence fields, and the canon rule has one owner (quickstart V-01–V-04f)

### Tests for User Story 1

- [X] T006 [P] [US1] Add the OMP checker test to `tests/test_policy_conflicts.py` (FR-021, V-02); create no new test file. Run `scripts/check-omp-baseline.sh` against a temp copy of the repo files, once per config. `backend: false`, `backend: "false"`, `backend: off`, and `backend: "off"` pass. A real backend fails with `memory enabled: backend=<value>`. A missing `memory:` block and a missing `backend:` line each fail with `memory key missing`. Confirm the `false` case fails before T011.
- [X] T007 [P] [US1] Add a Vale regression to `tests/test_wiki_cli.py` (FR-011, V-03). Run `vale --output=line` on a scratch file outside `wiki/` that contains "DM Thesis". Assert there is no `E100` output and that `Deprecated.DMThesis` fires. Skip the test when the `vale` binary is absent. Confirm it fails before T013.
- [X] T008 [P] [US1] Add a `vale_adapter` test to `tests/test_creative_lint.py` (FR-023, V-04b): a finding from a repo-local style (`is_custom`, e.g. `Deprecated.DMThesis`) is emitted with `repair_class: human_repair` and no `repair_action`, and `wiki lint fix --dry-run` on a scratch page containing "DM Thesis" plans no change for it. Confirm it fails before T015 (today it is `deterministic_repair` + `delete_section`).
- [X] T009 [P] [US1] Add tests for the folded rules to `tests/test_wiki_ops.py`, driving `tools/lint_wiki.py` on a temp vault: `md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, `forbidden_tree`, and `literal_newline` (scoped to session pages and Session templates, skipping YAML frontmatter and fenced code/statblocks, as `scripts/lint-literal-newlines` does). Assert `table_wikilink_unescaped_pipe` is `deterministic_repair` (`|` → `\|` inside a table-cell wikilink) and the rest are `human_repair`. Confirm they fail before T016.
- [X] T010 [P] [US1] Adjust the `wiki-reveal --count` regression in `tests/test_wiki_ops.py` (the `scripts/wiki-reveal` test near line 152, next to the CLI contract test at ~line 109): add a page with no frontmatter block to the temp vault and assert it is skipped and `--count --json` totals are unchanged (V-04d). It must pass both before and after T020.

### Implementation for User Story 1

- [X] T011 [US1] Fix the memory check in `scripts/check-omp-baseline.sh` per research R1: read the `backend:` line under `memory:`. `false`/`off`, quoted or unquoted, pass. Any other value fails with `memory enabled: backend=<value>`. A missing block or line fails with `memory key missing`. Make T006 pass and V-01 print `omp-speckit-baseline: pass`.
- [X] T012 [US1] Drain OMP entries e-205, e-207, e-209, and e-211 from `errors.md` with the current CLI, which still requires the flag at this point: `python3 scripts/error-ledger.py error drain --id <id> --cause-fixed true`. This runs before T075 removes `--cause-fixed`; never pass it after that. Do it in the same commit as T006 and T011 (FR-008).
- [X] T013 [US1] Remove `CoDM` from all 6 `BasedOnStyles` lines in `.vale.ini` (research R2). For the region, creature, and npc sections, the value becomes `Deprecated` alone. Leave `Vocab = CoDM`, `Packages`, `styles/Deprecated/*.yml`, and `tools/creative_lint/vale_vocab.py` unchanged (FR-022, FR-023). Make T007 pass.
- [X] T014 [US1] Drain Vale entries e-212, e-214, e-215, e-216, and e-218 from `errors.md` with the current CLI (`error drain --id <id> --cause-fixed true`, before T075), in the same commit as T007 and T013 (FR-008)
- [X] T015 [US1] In `tools/creative_lint/vale_adapter.py`, label findings from repo-local styles (`is_custom`) `human_repair` with no `repair_action`, so `wiki lint fix` never applies them. Removal or relocation of `Deprecated.*` content is the agent's call under `.agents/skills/wiki-lint/SKILL.md` (FR-023, plan "Judgments"). Make T008 pass.
- [X] T016 [US1] Fold the rules of `scripts/lint-obsidian-markdown` (`md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, `forbidden_tree`; its `missing_frontmatter` already exists) and `scripts/lint-literal-newlines` (as `literal_newline`) into `tools/lint_wiki.py` findings, with repair classes as in T009 (plan "One linter", research R8, constitution XXI). Make T009 pass.
- [X] T017 [US1] Delete `scripts/lint-wiki-write`, `scripts/lint-obsidian-markdown`, and `scripts/lint-literal-newlines`. Change `.agents/skills/obsidian-markdown/SKILL.md` line 35 from `./scripts/lint-wiki-write` to `./scripts/wiki lint`, and move `tests/test_error_ledger_repairs.py` lines 46–48 off the three scripts onto `scripts/wiki lint` (same positional-file case).
- [X] T018 [US1] Remove `TMPL_inherited_deprecated_guidance` from `scripts/wiki-lint` (duplicate of Vale `Deprecated.FactionClock`, research R8) and keep `TMPL_deprecated_guidance`. Update any test that asserts the removed rule id.
- [X] T019 [US1] In `package.json`, set `"lint:vale": "./scripts/wiki lint"` (`vale_adapter.run_vale` already refreshes the vocabulary). Delete `scripts/vale-vocab`. `rg -n vale-vocab AGENTS.md docs .agents scripts tools tests package.json README.md` must find nothing (FR-046 rule 2, SC-014 c, V-04d).
- [X] T020 [US1] In `scripts/wiki-reveal`, replace `from tools.check_wiki_pages import frontmatter` with `from tools.lint_wiki import frontmatter`. It returns `(block, fields)`: skip the page when `block is None` and use `fields` as the keys. Delete `tools/check_wiki_pages.py`. Change `README.md` line 105 to `./scripts/wiki lint`. `rg -n check_wiki_pages AGENTS.md docs .agents scripts tools tests package.json README.md` must find nothing, and T010 passes (V-04d).
- [X] T021 [US1] Add a vocabulary regression to `tests/test_creative_lint.py` (Analyze B1, research R2, FR-011): (i) `tools.creative_lint.vale_vocab.render_vocab(<live vault>)` has no line equal to `DM`; (ii) skipped when the `vale` binary is absent: with a temp copy of `.vale.ini`, `styles/`, and the rendered vocab as `styles/config/vocabularies/CoDM/accept.txt`, run Vale on a scratch file containing "DM Thesis" and "faction clock" and assert both `Deprecated.DMThesis` and `Deprecated.FactionClock` fire. Confirm it fails before T022. Not [P]: the canon track (T026, T030) edits the same file afterwards.
- [X] T022 [US1] Exclude rule-token words from the generated Vale vocabulary (Analyze B1, research R2; amends what T007 and T013 did). Leave `Vocab = CoDM`, `Packages`, and `styles/Deprecated/*.yml` unchanged (FR-022). In `tools/creative_lint/vale_vocab.py`, add the documented constant `_RULE_TOKEN_WORDS = {"DM"}` ("words that repo-local `styles/Deprecated` tokens match; accepting them silences those rules") and drop those terms in `proper_nouns`. Remove the strict `xfail` from `test_vale_deprecated_dmthesis_fires_with_live_vocabulary` in `tests/test_wiki_cli.py` (added by 2d3fee38), which now passes. Refresh `styles/config/vocabularies/CoDM/accept.txt` (no bare `DM` line) and commit it with the change (FR-028). Make T021 pass. Depends on T021.
- [X] T023 [P] [US1] In `.agents/skills/wiki-lint/consolidate.md`, delete §3 "Lifecycle corrections" (lines 44–48), the lifecycle text in step 3 (line 13), the `lifecycle*` report frontmatter (lines 75–76), and `lifecycle_updates=K` in the log line (line 92). `consolidate_main` gets no `drafts` report (withdrawn by plan 19e8b18d; this supersedes the implementer's local commit 3be6a266). Afterwards `rg -n 'lifecycle|base_confidence' .agents/skills/wiki-lint/consolidate.md` finds nothing (FR-047, V-04e).
- [X] T024 [US1] Run `scripts/wiki lint fix` on the whole vault (the current CLI's `fix` form; the subparser lands in T084) to apply the 519 `table_wikilink_unescaped_pipe` repairs, then confirm `table_wikilink_unescaped_pipe` = 0 (V-04c). Commit the wiki edits together with the FR-028 bookkeeping they caused. The 21 `broken_image_link` findings stay `human_repair` agent work under `wiki-lint` (round-3 gap 2, resolved; no task here).
- [X] T025 [US1] Put the canon rule in its one owner (FR-047, SC-015 b, V-04f, constitution X): replace `.agents/skills/llm-wiki/SKILL.md` lines 231–313 ("Confidence and Lifecycle") with a short "Canon" section holding the rule verbatim from constitution X ("Something is canon if the DM says so > something is canon if it's present in the wiki in multiple places > something is canon if it doesn't conflict with the wiki.") plus two sentences: agents apply it and code only reports; a DM ruling is cited through the page's existing `sources:` (session log under `wiki/journal/sessions/<campaign>/<NN>/`, recap `## Wiki facts`, or the filed DM statement). Drop the example fields (lines 127–129), the `OBSIDIAN_ALLOWED_LIFECYCLES`/`OBSIDIAN_REQUIRED_TRUST_FIELDS` line (235), and "confidence/lifecycle" in the description (line 5). Point these at it without restating the rule, and drop their canon-proposal/lifecycle text: `AGENTS.md` lines 87 and 126, `wiki/AGENTS.md` lines 54, 62, 64, `docs/agents/work.md` lines 7 and 51, `CONTEXT.md` lines 123 and 248–250, `docs/agents/table-ready.md` lines 99 and 115, and `.agents/skills/plan-session/SKILL.md` line 107. Mark `docs/adr/0003-canon-changes-are-proposals.md` superseded by constitution v7.0.0 X, pointing to `llm-wiki`.
- [X] T026 [US1] Remove the lifecycle/trust/canon-gate code (FR-047, SC-015 a/c). Test first: in `tests/test_wiki_ops.py` and `tests/test_creative_lint.py`, assert that a page with no lifecycle or trust fields lints clean, that `lint_wiki --json` has no `bad_lifecycle`/`missing_trust` findings, no `stale_pages[].lifecycle`, and no `schema.allowed_lifecycles`/`required_trust_fields`, and that neither `CANON001`, `CANON002`, nor the `canon` category is in the registry or bundles; confirm they fail first. Then edit `tools/lint_wiki.py` lines 24–25, 30, 41, 198–208, 320–322, 712–723, 760–764, 794–804, 962, 998 (`OWNER_LIFECYCLES`/`DEFAULT_LIFECYCLES`, `lifecycle` in `CAMPAIGN_REQUIRED` so it becomes `type`, `reveal`, owner-schema lifecycle parsing, `--allow-lifecycle`, `--required-trust-field`, `missing_trust`, `bad_lifecycle`, the `stale_pages` key); `scripts/wiki-lint` lines 111, 129–130 (`--allow-lifecycle` passthrough); `tools/wiki_ops/worklist.py` line 14 (`bad_lifecycle`); `tools/creative_lint/evaluators/symbolic.py` lines 89–90 and 117–118 (lifecycle checks) and the whole CANON block from the `target = pages[targets[0]]` lookup down (lines 152–173: `CANON001` and `CANON002`), plus the then-unused `import datetime as dt` (line 3); `tools/creative_lint/engine.py` lines 145, 150 (lifecycle exemption); `tools/wiki_ops/identity.py` lines 108, 139, 202 (`lifecycle` field); `scripts/wiki-reveal` line 54 (`lifecycle` key); `rules/registry.yml` lines 2–14 (`CANON001`), 15–27 (`CANON002`), and 48–49 (WIKI002 message becomes type only); the now-empty `canon` category in `tools/creative_lint/constants.py` line 7 and `rules/bundles.yml` lines 4, 10, 14, 24; and `docs/creative-linting.md` (rewrite the example at lines 32/42 to use `WIKI001`, change line 65 to `./scripts/wiki-lint rule WIKI001`, drop `CANON001-002` at line 101 and the `CANON001/` and `CANON002/` entries at line 125). Add no new finding: `orphan_pages` is the single-source fact. Keep rule-status `lifecycle: ACTIVE|SHADOW|DRAFT` in `creative_lint`.
- [X] T027 [US1] Fix the faction contract bug (FR-047 item 5, V-04f). Test first: rename `test_template_contract_respects_lifecycle_and_redirect_stubs` (`tests/test_wiki_ops.py` line 496) to a status-keyed name, update the fixture `tests/fixtures/wiki_ops/templates/dormant-faction.md`, and assert `when:` resolves on entity `status` alone (falling back to `default`); confirm it fails first. Then make `tools/wiki_ops/template_contracts.py` line 160 read `status` only, and remove the `accepted`/`proposed` keys from `wiki/templates/contracts/faction.yml` (lines 21–22, 64–65, 74–75). Expect exactly 2 new `TMPL_missing_required` findings ("Active Agenda" in `wiki/entities/faction/tessarine-concordat.md` and `Sunkline.md`); they are agent work under `.agents/skills/faction-design/SKILL.md`, not fixed here.
- [X] T028 [US1] Stop writing the fields: remove the `lifecycle: proposed` defaults in `scripts/wiki-bulk-ops` (lines 971, 974) and `scripts/ingest-raw.py` (line 74), and update `tests/test_wiki_bulk_ops.py` lines 370 and 372 to assert the fields are absent (FR-047).
- [X] T029 [US1] Migrate the data with the existing tool (plan Phase 1 "Wiki canon" step 4; no new script). Dry-run first: `for f in lifecycle lifecycle_changed lifecycle_reason base_confidence canon_status superseded_by; do for v in wiki wiki/templates wiki/_archive; do scripts/wiki-bulk-ops frontmatter --vault "$v" --action remove --field "$f" --dry-run --json; done; done`. Expected counts: live `lifecycle` 833, `lifecycle_changed` 715, `base_confidence` 833, `canon_status` 3, `lifecycle_reason` 0, `superseded_by` 0; templates `lifecycle` 27; `_archive` 15/2/2 (`lifecycle`/`lifecycle_changed`/`base_confidence`). Stop and report on any mismatch. Then run it for real, and by hand in the same commit drop `lifecycle` from the 15 `wiki/templates/contracts/*.yml` `required:` lists and `base_confidence` from `faction.yml` `optional:`. A rerun must report `files_modified: 0`. Leave in-fiction body prose such as `**Lifecycle:** active`. Run `scripts/wiki lint` once and commit the refreshed `wiki/_meta/lint-cache.json` with the migration (FR-028). This must land before every SC-007 timing task (T065, T066, T067, T090) and before the identity index (T059).
- [X] T030 [US1] Update the tests for FR-047: delete the 10 machinery-only fixtures (`tests/fixtures/creative_lint/CANON001/` ×3, `tests/fixtures/creative_lint/CANON002/` ×3, `tests/fixtures/creative_lint/symbolic/invalid_lifecycle.md`, `tests/fixtures/creative_lint/symbolic/dead_reference.md`, `tests/fixtures/creative_lint/symbolic/stale_reference.md`, `tests/fixtures/creative_lint/WIKI002/ambiguous_proposed_state.md`) and `test_symbolic_rules_detect_dead_and_stale_entities` (`tests/test_creative_lint.py` lines 117–131); drop `CANON001` and `CANON002` from the rule set at `tests/test_creative_lint.py` line 47; make `tests/test_creative_lint_cli.py` lines 26 and 28 use `rule WIKI001`; strip the fields from the 17 remaining fixture pages with `scripts/wiki-bulk-ops frontmatter --vault tests/fixtures/<dir> --action remove --field <f>`; and drop the field lines at `tests/test_wiki_ops.py` 128–130, 145, 221, 272, 274, 308, 434, 451, 492, 499, 567, 599, 803, 838, 882, 885, 938, `tests/test_wiki_cli.py` 102, and `tests/test_error_ledger_repairs.py` 37. `pytest -q` passes after this task (T026–T030 land together).
- [X] T031 [P] [US1] Delete the lifecycle/confidence machinery text from skills and docs (FR-047, SC-015 a), using the full file:line list in research R9 "Skill lines" (~288 lines in 39 files). This covers the blocks `.agents/skills/wiki-lint/checks.md` §12 (lines 75–98), `.agents/skills/wiki-ingest/SKILL.md` lines 503–517, and `.agents/skills/wiki-ingest/references/url-sources.md` lines 148–196, plus the 36 other files R9 lists (`lore-design`, the seven `*-history-ingest` skills, `wiki-capture` + `raw-format.md`, `wiki-research`, `wiki-import`, `obsidian-markdown`, `wiki-update`, `wiki-synthesize`, `vault-skill-factory`, `wiki-dedup`, `wiki-export`, `wiki-agent`, `wiki-narrate`, `wiki-lint/SKILL.md:89`, `session-beats:27`, `faction-design:86`, `city-design:89`, `vehicle-design:91`, `region-design:98`, `spell-design:93`, `narrative-islands:54`, `llm-wiki/paper-template.md:7`; `llm-wiki`, `consolidate.md`, `wiki-query`, `wiki-digest`, and the Foundry gates are handled in T025, T023, and T032), and `docs/agents/policy-owners.yml` line 19, `docs/agents/wiki-maintenance-loop.md` line 59, `docs/agents/context-waste-method.md` line 46, `docs/agents/hybrid-sdd.md` line 17, `docs/architecture.md` line 5, and `wiki/templates/work.md` line 30 (body text "`lifecycle` stays `proposed`"). Per spec c6f53f02 (round-4 gap 3), `superseded_by` is removed too: `.agents/skills/llm-wiki/SKILL.md` lines 244, 247, 310 (inside the T025 block), `.agents/skills/wiki-lint/checks.md` §12d line 93 (inside §12), and `.agents/skills/wiki-capture/references/raw-format.md` line 20 (this task also owns the rest of that file's R9 lines, so no other open task edits it; Analyze B2). `tier` is unchanged.
- [X] T032 [P] [US1] Rewrite the readers (FR-047, plan step 5): the Foundry gates in `.agents/skills/foundry-token/SKILL.md` line 16, `.agents/skills/foundry-battlemap/SKILL.md` line 12, and `.agents/skills/foundry-stage/SKILL.md` line 20 become "the source page is canon under the rule (`llm-wiki`)", with their guardrail evals `.agents/skills/foundry-token/evals/evals.json` lines 28–31, `.agents/skills/foundry-battlemap/evals/evals.json` lines 18–21, and `.agents/skills/foundry-stage/evals/evals.json` line 21. Drop the trust annotations in `.agents/skills/wiki-query/SKILL.md` lines 244–261 and the Drafts list in `.agents/skills/wiki-digest/SKILL.md` lines 47, 81, 143. Update the evals `.agents/skills/wiki-import/evals/evals.json:10`, `.agents/skills/wiki-ingest/evals/evals.json:85`, `.agents/skills/vehicle-design/evals/evals.json` 22/88, `.agents/skills/city-design/evals/evals.json:76`, `.agents/skills/spell-design/evals/evals.json` 22/84, `.agents/skills/narrative-islands/evals/evals.json:136`, and `.agents/skills/wiki-dashboard/evals/evals.json:6` to current behavior.
- [X] T033 [US1] Rewrite the 7 remaining "canon proposal" lines to "canon under the rule in `llm-wiki`" (FR-047; round-4 gap 1, resolved): `.agents/skills/place-design/SKILL.md:55`, `.agents/skills/writing-for-humans/SKILL.md:145`, `.agents/skills/wiki-ingest/references/ingest-prompts.md:10`, `.agents/skills/wiki-ingest/evals/evals.json:132`, `.agents/skills/resolution-beats/SKILL.md:103`, `.agents/skills/session-beats/references/agency.md:5`, and `.agents/skills/dungeon-design/SKILL.md:176`. Runs after T032 (shared `wiki-ingest/evals/evals.json`).
- [X] T034 [US1] Verify V-01, V-03 (also `rg -nx 'DM' styles/config/vocabularies/CoDM/accept.txt` is empty and `Deprecated.DMThesis` fires on the scratch file), V-04 (`pytest -q` completes with no Vale E100), V-04b (the `VALE_Deprecated.DMThesis` finding appears once the vocab is refreshed), V-04c, V-04d (both `ls` checks fail, `lint:vale` is `./scripts/wiki lint`, `./scripts/wiki-reveal --count --json` equals `/tmp/030/reveal-count-before.json`, both `rg` checks empty), V-04e (both `rg` checks empty; `rg -n -i --hidden 'CANON001|CANON002|superseded_by|canon proposal' AGENTS.md CONTEXT.md wiki/AGENTS.md wiki/templates docs .agents tools scripts rules tests -g '!docs/adr/**'` returns nothing; the migration dry-run reports `files_modified: 0`; `pytest -q` passes), V-04f (the rule text has exactly one hit, in `.agents/skills/llm-wiki/SKILL.md`; both AGENTS.md files link to it; `scripts/wiki lint entities/faction/Sunkline.md` reports `TMPL_missing_required` for "Active Agenda"), and US1-4 (`python3 scripts/error-ledger.py error list` shows no open OMP or `CoDM` entry). `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` are tracked FR-028 bookkeeping: commit them with the change that caused them, and revert them only after scratch measurement runs.

**Checkpoint**: Verification runs are green and `wiki lint` is the only linter, so US2–US4 results can be trusted

---

## Phase 4: User Story 2 - One Coherent Evaluator and Corpus (Priority: P1)

**Goal**: `scripts/luna-eval` is the only runner, `skill-creator` calls it, all eval records follow one schema that `luna-eval` checks, and the feature 026 docs cite only real surfaces

**Independent Test**: Quickstart V-09, V-10, and V-11

### Tests for User Story 2

- [X] T035 [P] [US2] Add a case to `tests/test_policy_conflicts.py` (SC-008, V-11) that runs `scripts/check-current-commands --json` over `specs/026-agent-autonomy-scope/` and fails on any cited `scripts/…` or `tests/…` path that does not exist, and separately fails on any `AGENT00[1-3]` in those docs. Confirm it fails before T038 and T037.
- [ ] T036 [US2] Create `tests/test_luna_eval.py`, the one new test file (plan "New files"). Cover:
  - The `load_eval` schema check (data-model §2): it passes on all 60 `.agents/skills/*/evals/evals.json`, and on a temp bad file it exits 2 with `{"status":"error","error":"<file>: eval <id>: <problem>","hint":"see data-model §2","example":…}` before any subject run. Cases: missing `skill_name` or one unequal to the directory name, empty or missing `assertions[]`, a leftover `expectations[]`, a `type` outside {`skill_selected`, `behavior`, `quality`, `guardrail`, `process`, `content`, `structure`, `scope`, `handoff`, `coverage`}, and a `skill_selected` `text` that is not an existing directory under `.agents/skills/`.
  - `metrics.json` built from a fixture `events.jsonl`: exactly the data-model §3 keys, including `retries` (a failed command re-run with identical argv), `invocation_errors`, `invocation_error_commands`, `model`, and `effort`, with an absent event recorded as `null`.
  - `invocation_errors` counts a `command_execution` of an FR-027 command (`scripts/wiki`, `scripts/wiki-lint`, `scripts/luna-eval`, `scripts/error-ledger.py`, `scripts/manifest.py`) rejected with the FR-035 error object on stdout (`"status":"error"` plus `example`) or argparse `usage: … error:` on stderr and a non-zero exit, even when later corrected; exit 2 alone (`EXIT_REJECTED`) does not count.
  - `skill_selected` grading: it passes when the first owner `SKILL.md` in `skills_read` matches `text`, written as `{text, passed, evidence, type}`.
  - Work-gate wording (SC-003): fail when any assertion `text` in any evals file contains `Work gate`, `chat proposal`, or `approval before write` (case-insensitive).

  Confirm the schema, metrics, and grading cases fail before T040–T042.

### Implementation for User Story 2

- [X] T037 [P] [US2] Rewrite the 66 references to `scripts/check-agent-standards.py`, `tests/test_agent_standards.py`, and `AGENT001`–`AGENT003` in `specs/026-agent-autonomy-scope/{spec,plan,research,data-model,quickstart,tasks}.md` and `specs/026-agent-autonomy-scope/contracts/agent-autonomy.md`. Point each one at `luna-eval` evals (agent behavior) or `wiki lint` (wiki structure). Where no current surface exists, remove the reference with a one-line "replaced by" note (FR-018, V-11).
- [X] T038 [P] [US2] Extend `scripts/check-current-commands` (research R8): also check cited `scripts/…` and `tests/…` paths, and add `specs/026-agent-autonomy-scope/` to its scan roots. Make T035 pass.
- [X] T039 [US2] Replace the `git rev-parse --show-toplevel` root in `scripts/luna-eval` (line ~47) with `tools/wiki_ops/cli.py` `repo_root`, started from the script's own location, so it runs from any working directory. Keep the existing flags (FR-027, contracts/eval-run.md). T082 later makes the package location the helper's default.
- [X] T040 [US2] Add the evals.json schema check to `load_eval` in `scripts/luna-eval` (plan "Evaluator"; chosen over `quick-validate.py`): validate the whole file against data-model §2 and exit 2 naming each bad record before any subject run, with the error shape in contracts/eval-run.md "Schema check".
- [ ] T041 [US2] Make `scripts/luna-eval` write `metrics.json` into each `run-<n>/` directory, derived from `events.jsonl` with the names confirmed in T005. The keys are exactly those in data-model §3: `tool_calls` (by kind), `total_tool_calls`, `retries` (a failed command re-run with identical argv), `invocation_errors` and `invocation_error_commands` (rule as in T036), `duplicate_actions`, `tokens` {`input`,`output`,`total`}, `completion_reason` ∈ `ok|no_output|usage_limit|error`, `model` and `effort` (the values `luna-eval` actually passed to codex), and `skills_read`. An event that is absent is recorded as `null`, never guessed (research R5).
- [ ] T042 [US2] Make `scripts/luna-eval` grade `skill_selected` assertions into `grading.json`. An item passes when the first owner `SKILL.md` in `metrics.json` `skills_read` matches `text`. Write each item as `{text, passed, evidence, type}` (data-model §3). Make T036 pass.
- [X] T043 [US2] In `scripts/luna-eval`, keep exit codes 0/3/4/5 unchanged. On exit 3 or 5, keep completed runs. On a rerun, skip any `run-<n>/` that already has `timing.json` with exit 0 (contracts/eval-run.md, spec Edge Case).
- [X] T044 [P] [US2] Update `.agents/skills/skill-creator/agents/grader.md` to grade `assertions[]` `{type,text}` for every type except `skill_selected`, which `luna-eval` grades. Keep `text`/`passed`/`evidence` on each item and add `type`. Add the top-level `task_outcome` (`pass|fail|blocked`) and `semantic_quality` = pass rate of that eval's `quality`-type assertions (passed / total, `null` when the eval has none), computed from the graded items. The grader assigns no separate score (data-model §3, FR-016).
- [X] T045 [P] [US2] Update `.agents/skills/skill-creator/references/schemas.md`. The evals.json schema becomes data-model §2, and grading/metrics/timing become data-model §3 (`metrics.json` is this file's existing metrics schema plus `retries`, `invocation_errors`, `model`, `effort`). Remove the `expectations[]` and `{"query","should_trigger"}` shapes.
- [X] T046 [US2] Update `.agents/skills/skill-creator/SKILL.md` so that "Running and evaluating test cases" calls `scripts/luna-eval` once per eval and config. Delete the "Description optimization" section and the `run-loop.py` / `run-eval.py` line (~460) (FR-012, FR-015, research R5).
- [X] T047 [US2] Delete `.agents/skills/skill-creator/scripts/run-eval.py`, `run-loop.py`, `improve-description.py`, and `generate-report.py` (it only renders `run-loop.py` output). Keep `utils.py` (`package-skill.py` uses it). Then `rg --hidden "run-eval|run-loop|improve-description|generate-report" .agents/ AGENTS.md docs/ scripts/ tools/ tests/` and remove the remaining references, including `.agents/skills/vault-skill-factory/SKILL.md` line ~106.
- [X] T048 [US2] Run a one-off conversion over all `.agents/skills/*/evals/evals.json`. The script is not committed (plan: VIII does not apply to one-offs). Each `expectations[]` string `s` becomes `{"type":"behavior","text":s}`, and `expectations` is removed. Rename `qualitative`→`quality` and `structural`→`structure`; keep `scope`, `handoff`, and `coverage` (FR-014). Preserve `core`, `subject_skill`, `trajectory_records`, and `principles`. `expected_output` stays optional, with no text invented (FR-013).
- [X] T049 [US2] Add `"skill_name"` (equal to the directory name) to `.agents/skills/{session-beats,wiki-capture,wiki-context-pack,wiki-ingest,wiki-lint,wiki-query,wiki-update}/evals/evals.json` (FR-013)
- [X] T050 [US2] Edit the Work-gate, chat-proposal approval, read-side mutation, and retired-path wording by hand, record by record, in the 13 files found by `rg -il "work gate|chat proposal|approval" .agents/skills/*/evals/evals.json`. This includes `.agents/skills/place-design/evals/evals.json` eval 1. Keep each assertion and phrase its current behavior positively (e.g. "writes without asking first") (FR-017, spec Edge Cases).
- [X] T051 [US2] Add at least one `skill_selected` eval (`{"type":"skill_selected","text":"<dir name>"}`) to each of the six FR-003 owners fixed by Clarify (cae8bb44): `.agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/evals/evals.json`. Write each prompt from that skill's own ownership text (FR-003, FR-014, FR-015, SC-005).
- [X] T052 [US2] Verify V-09 with `pytest tests/test_luna_eval.py` (schema over all 60 files and the Work-gate wording case pass) and V-11 with `pytest tests/test_policy_conflicts.py`.
- [ ] T053 [US2] Verify V-10. Run the `place-design` `skill_selected` record directly with `scripts/luna-eval ... --out /tmp/030/iteration-1`, then through the skill-creator workflow. Both run dirs must have the same files and keys (`timing.json`, `metrics.json`, `grading.json`), and the item must be `passed: true`. Then drain e-210 from `errors.md` with the current CLI (`error drain --id e-210 --cause-fixed true`, before T075), in the same commit as T039–T047 (research R3, FR-008).

**Checkpoint**: One evaluator and one checked schema exist, which is the prerequisite for US3 and US8

---

## Phase 5: User Story 3 - Feature 029 Baseline Evidence (Priority: P1)

**Goal**: A recorded `luna-eval` baseline with at least 10 cases across all nine categories, each carrying every FR-016 metric and its model/effort pair

**Independent Test**: Quickstart V-12

- [ ] T054 [US3] Select at least 10 existing owner eval records covering all nine US3 categories: owner completion, specific blocking, scope preservation, read isolation, retrieval convergence, child handoff, parent resumption, write finalization, and recovery. List category → `<skill>:<eval id>` in `specs/029-agent-loop-closure/quickstart.md`.
- [ ] T055 [US3] Run each selected case with `scripts/luna-eval --skill <dir> --eval <id> --out /tmp/030/baseline/iteration-1` at `luna-eval`'s default model and effort (constitution XXVI). Confirm each run's `metrics.json` records `model` and `effort` and that all runs share one pair; SC-012 comparisons must reuse it (FR-019). On exit 3 or 5, rerun only the missing cases (T043).
- [ ] T056 [US3] Record each case in `specs/029-agent-loop-closure/quickstart.md` with model, effort, task outcome, tool calls, retries, duplicate actions, tokens, latency, completion reason, and semantic quality. Latency comes from `timing.json`; tool calls, retries, tokens, model, and effort from `metrics.json`; task outcome and semantic quality (the `quality`-assertion pass rate, or `null`) from `grading.json` (FR-016, FR-019).
- [ ] T057 [US3] Check off T003, T011, T018, T030, T037, T044, T046, T047, and T049 in `specs/029-agent-loop-closure/tasks.md`, each with a pointer to its evidence (FR-019, SC-006)

**Checkpoint**: A baseline exists for the SC-012 comparisons

---

## Phase 6: User Story 4 - Scoped Lint Costs Scoped Work (Priority: P1)

**Goal**: Identity reads and compares only changed or selected pages and their candidates, using a derived index loaded through `lint_cache.py`. Findings are identical, and no code picks a canonical page.

**Independent Test**: Quickstart V-05, V-06, V-07, V-08, V-08b, and V-08c

### Tests for User Story 4

- [X] T058 [US4] Add identity-index tests to `tests/test_wiki_ops.py`, using a temp vault built in the test:
  - (a) cold and warm `scan_identities` output is identical.
  - (b) editing one page refreshes its row: a `(size, mtime_ns)` change triggers a rehash, and the findings equal a cold run.
  - (c) an index containing `{`, or with a changed `version`, is rebuilt.
  - (d) rows for deleted paths are dropped, and `pairs` for vanished hashes are pruned.
  - (e) a scoped run reports `compared == |selected ∪ candidates|`, which is less than the page count.
  - (f) `resolve_identity` and `_path_for` return the same results from the index as from a cold walk.
  - (g) a lint rules-digest change invalidates `lint-cache.json` entries but leaves identity rows and `pairs` reused (`index.misses == 0`).
  - (h) an above-threshold pair is only listed in `candidates` with `status: ambiguous`; no winner is chosen.

  Confirm (e) and (g) fail before T059–T061.

### Implementation for User Story 4

- [X] T059 [US4] Add load and save for `wiki/_meta/identity-index.json` to `tools/wiki_ops/lint_cache.py`, reusing its `cache_path`, `sha256_file`, versioned load, and atomic writer (research R8; not in `identity.py`). Use data-model §4 exactly:
  - Rows carry no `lifecycle` (data-model §4 "No lifecycle"; `version` stays 1). This task runs after T029.
  - Header: `version`, `manifest_sha256`.
  - Rows keyed by path: `size`, `mtime_ns`, `content_sha256`, `stem`, `title`, `type`, `aliases`, `redirects_to`, `body_len`, and `profile` (the body character `Counter`).
  - `pairs`: `SequenceMatcher.ratio()` keyed `"<sha_a>|<sha_b>"` (sorted content hashes); "Entries whose hashes no longer match any row are pruned on save."
  - Validity: "a row is reused when `(size, mtime_ns)` matches, or when the rehashed `content_sha256` matches. A changed `version`, a JSON error, or a changed `manifest_sha256` refreshes the affected state; version and parse errors rebuild everything."
- [X] T060 [US4] In `tools/wiki_ops/identity.py`, replace the whole-vault read in `scan_identities` with candidate selection from index rows (research R4 steps 1–5; `os.scandir` + `stat` walk), on top of T026 (no `lifecycle` field). Candidates share the same `type`, have no redirect, and meet one of: a norm title or alias match, a stem match, shared manifest provenance with stem ratio > 0.7, a merge transition, or the cached profile prefilter `2·|A∩B| / (lenA+lenB) > 0.6` (FR-024 as clarified). Make `resolve_identity` (mutation gate) and `_path_for` read the index too. Thresholds only list candidates and set `status: ambiguous`, which gates mutations; resolution goes through `.agents/skills/wiki-dedup/SKILL.md` and `.agents/skills/wiki-lint/SKILL.md` (plan "Judgments").
- [X] T061 [US4] Add the pair-ratio cache to `tools/wiki_ops/identity.py`: read `pairs` through `lint_cache.py`, run `SequenceMatcher` only on candidate pairs that are uncached, and read only those candidate bodies (research R4 step 6, R7). Make T058 pass.
- [X] T062 [US4] Add `"identity": {"status","ambiguous","scanned","compared","index":{"hits","misses"}}` to `scripts/wiki-lint --json` output, where `scanned` = selected and `compared` = |selected ∪ candidates| (data-model §4, SC-007)
- [X] T063 [US4] Delete `scripts/wiki-identity` (research R8). Move `tests/test_wiki_ops.py` line 109 (drop it from the `--help` contract loop), line 115 (`scan --json` ambiguous case → call `scan_identities` or read the `wiki lint` `identity` block), and line 514 (`resolve` case → call `resolve_identity`) onto the library or `wiki lint`.
- [X] T064 [US4] Keep `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` tracked as FR-028 bookkeeping (data-model §4 "Tracking"): no `.gitignore` change, and each is committed with the change that caused it. Commit the first generated `identity-index.json` with T059–T062.
- [X] T065 [US4] Verify V-05 (read run 1 `timing.duration_ms` < 5000, `identity.compared` far below the page count; run 2 `cache.hits: 1`), V-06 (diff against `/tmp/030/identity-before.json` and `/tmp/030/lint-before.json` from T002, allowing only the findings added by T016 and T027, those removed by T018 and T026, and the dropped `lifecycle` field), and V-07 (corrupt index rebuilt). Record the V-05 numbers in the `specs/030-self-improving-architecture/quickstart.md` V-05 row.
- [ ] T066 [US4] Run V-08: with the lint cache and identity index current, edit 1–3 pages on a scratch branch, run `scripts/wiki health`, and read `timing.duration_ms` (< 10 000). Then run V-08c: delete both `wiki/_meta/identity-index.json` and `wiki/_meta/lint-cache.json` on the scratch branch, run `scripts/wiki health`, confirm it finishes with no harness timeout, and record its `timing.duration_ms` next to the SC-006 baseline in `specs/029-agent-loop-closure/quickstart.md` (after T056; no bound).
- [X] T067 [US4] Run V-08b: on a scratch branch with the identity index current, change the rules digest (e.g. add a comment line to `.vale.ini`), run `scripts/wiki health`, and read `timing.duration_ms` (< 50 000), `lint.cache.misses` (≈ page count), and `identity.index.misses` (== 0). Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-08b row (pre-change reference 82.3 s). Discard the scratch branch.
- [X] T068 [US4] Drain identity entries e-206, e-208, and e-213 from `errors.md` with the current CLI (`error drain --id <id> --cause-fixed true`, before T075), in the same commit as T058–T064 (FR-008)

**Checkpoint**: Phase 1 is complete: green checks, one linter, one evaluator, a baseline, and scoped identity

---

## Phase 7: User Story 5 - Friction Is Fixed at the Source, Then Work Resumes (Priority: P2)

**Goal**: Shared guidance states the friction rule once, as a branch of the capability loop

**Independent Test**: Quickstart V-17 (seeded friction, at least 4/5 cold subjects fix the source, add a regression, and finish)

- [X] T069 [P] [US5] Add one friction-rule paragraph to `AGENTS.md` next to "Capability loop" (line ~72): act → friction → identify cause → fix the authoritative source (smallest change) → verify → continue the original task. Add no new workflow, command, or skill (FR-001, FR-002, FR-005).
- [X] T070 [P] [US5] Add the friction branch (act → friction → fix source → re-observe → continue) to the capability loop in `docs/agents/hybrid-sdd.md`, linking to the `AGENTS.md` paragraph rather than restating it (FR-001, constitution XVI)
- [ ] T071 [US5] Run V-17. On a scratch branch, make one owner `SKILL.md` name a retired command path, then run 5 cold `scripts/luna-eval` subjects on one of that owner's evals. At least 4/5 must fix the source, add a regression, and finish the owner task with no new `errors.md` entry. Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-17 row. Discard the scratch branch. This runs after T080 so the new ledger format is in place.

**Checkpoint**: Friction handling is documented in one place and behaviorally proven

---

## Phase 8: User Story 6 - Recurring Causes Trend to Zero (Priority: P2)

**Goal**: `errors.md` holds only open four-field entries. Exact duplicates attach, the agent decides broader same-cause attaches, fixes drain, and recurrence is part of `error list`.

**Independent Test**: Quickstart V-13, V-14, and V-15

### Tests for User Story 6

- [ ] T072 [US6] Add ledger tests to `tests/test_error_ledger_repairs.py`. Each one drives `scripts/error-ledger.py` via subprocess on a scratch `errors.md` and covers:
  - Exact-match auto-attach: `append` with the same `source` and identical whitespace-trimmed `cause` gives `attached`; a reworded cause on the same source gives `created` (a new id); a different `source` gives `created`.
  - The report carries the matched `id` and `occurrence_index` (and `occurrences`); a repeated identical occurrence gives `already_done`.
  - `--attach e-N` on the same source gives `attached`. `--attach` across sources, or for an unknown id, exits 2 with `error`/`hint`/`example` and writes nothing (FR-007 refusal regression).
  - `detach --id e-N --index k` gives `detached`; repeating it gives `already_done`; detaching the only occurrence exits 2 with a hint to use `drain`.
  - `--cause-fixed` on any subcommand is rejected: exit 2 with `"error":"--cause-fixed was removed"`, a hint, and the `error drain --id e-212` example.
  - `list` returns exactly `{entries, recurrence: {total, by_sitting}, missing_sources}` with correct totals, and `--ids-only` prints ids.
  - A missing `--source` exits 2 with an example; `--source` must be an existing repo path or `external:<name>`.
  - `drain` gives `drained` then `already_done`; `--dry-run` on append, drain, and detach writes nothing and returns `planned`.
  - Commands work from a non-root cwd.

  Plan default, error-ledger CHK011: an "identical occurrence" means the same `sitting` and `detail`. Confirm the tests fail before T073.

### Implementation for User Story 6

- [ ] T073 [US6] Rework the entry model in `scripts/error-ledger.py` (data-model §1). Keep the `# Error ledger` heading, a blank line, then one JSON object per line with sorted keys. The fields are exactly `id` (`"e-<n>"`, unique, new ids from `next_error_id`), `cause` ("Never rewritten when an occurrence is added"), `source` (repo-relative path or `external:<name>`), and `evidence` ("list of `{sitting, detail}`, length ≥ 1"). There is no `status` or `cause_fixed`. The only automatic match is the same `source` with `cause.strip()` equal; no normalized key or other heuristic (FR-007, research R3).
- [ ] T074 [US6] Implement `error append --source S --cause C --sitting X [--detail D] [--attach e-N] [--dry-run]` in `scripts/error-ledger.py`, returning `{"status":"attached"|"created"|"already_done","id","occurrence_index","occurrences"}`; `detail` defaults to `C`. Check `--source` deterministically (existing repo path or `external:<name>`). Refuse `--attach e-N` when e-N's `source` differs or e-N is unknown, with the contracts/error-ledger.md error shape and nothing written.
- [ ] T075 [US6] In `scripts/error-ledger.py`: implement `error drain --id e-N [--dry-run]` (`drained|already_done`) and remove the `--cause-fixed` flag, so passing it exits 2 with the contract's hint and example; make `error list [--ids-only]` return `{entries, recurrence, missing_sources}` (FR-009: `total = Σ(len(evidence) − 1)`, `by_sitting` counts non-first occurrences); and add `error detach --id e-N --index k [--dry-run]` (`detached|already_done`, refusing to remove the only occurrence). Add no `recurrence` or `migrate` subcommand.
- [ ] T076 [US6] Switch `scripts/error-ledger.py` to `tools/wiki_ops/cli.py` `repo_root` so `errors.md` is found from any cwd. Add an `--help` Examples block that shows `python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …"` (FR-027, FR-032). Make T072 pass.
- [ ] T077 [US6] Migrate `errors.md` with a one-off, uncommitted conversion (research R3, FR-010, V-13; round-3 gap 3 resolved): drop `status == "drained"` lines, map each open entry to `{id, cause, source, evidence:[{sitting, detail: cause}]}`, and concatenate `evidence` into the kept id for each merge group. The merge groups and `source` values are agent-supplied input data: confirm research R3's proposal against the cause text (any OMP, Vale, or identity entry still open after T012, T014, T068; e-168 → `.agents/skills`, e-201/e-203/e-217 → `.agents/skills/wiki-lint/SKILL.md`, e-202 → `scripts/wiki`), with no group ids hardcoded in `scripts/error-ledger.py`. In the same commit as T073–T076, update the two `error list` callers in `scripts/wiki` (lines ~201 and ~587) to read `entries`.
- [ ] T078 [P] [US6] Rewrite `AGENTS.md` "Error ledger" (line ~196): fix and verify the source, then continue; `append` only when the fix cannot land in the current task; `drain --id e-N` goes in the same commit as the verified fix. Add the same-cause rule (attach with `--attach e-N` when the fix for e-N would also remove this failure; otherwise create) and the undo `error detach --id e-N --index k`. Remove `--cause-fixed true` from every documented invocation (contracts/error-ledger.md, research R3).
- [X] T079 [P] [US6] Rewrite `.agents/skills/wiki-lint/SKILL.md` line ~47 from "record the mismatch in errors.md" to "reconcile first, record only if unresolved", linking to `AGENTS.md` rather than restating it (constitution XIX)
- [ ] T080 [US6] Verify V-13 (`python3 scripts/error-ledger.py error list` loads with no `status`/`cause_fixed`, no drained entry, one id per agent-chosen group, no two entries sharing `(source, cause.strip())`, `missing_sources: []`), V-14 on a scratch copy, and V-15/FR-009 through `error list` `recurrence` (`{"total": n, "by_sitting": {...}}`). Record the starting total in the `specs/030-self-improving-architecture/quickstart.md` V-15 row. The SC-009 20-sitting window stays an assumption tracked after merge (resolved gap 5), not a gate.

**Checkpoint**: The ledger is deduplicated, and its agent guidance matches "fix first"

---

## Phase 9: User Story 7 - Wiki Commands Agents Can Drive Headlessly (Priority: P2)

**Goal**: The `scripts/wiki` subcommands meet contracts/wiki-cli.md (FR-027–FR-039) through one discovery helper, and health reports facts only

**Independent Test**: Quickstart V-16 and SC-010

### Tests for User Story 7

- [ ] T081 [US7] Add one subprocess test per rule class to `tests/test_wiki_cli.py` (FR-039):
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

  Confirm the tests fail before T082.

### Implementation for User Story 7

- [ ] T082 [US7] Make `tools/wiki_ops/cli.py` the only discovery helper: `repo_root` resolves from the package location (not the cwd), and `resolve_vault` uses `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` > `~/.obsidian-wiki/config`, with `"vault": "<absolute path>"` in every result (FR-027, research R6/R8). Switch `scripts/wiki-lint` `consolidate_main` (`Path.cwd() / vault`, line ~352), the `tools/lint_wiki.py` default (`Path("wiki")`, line ~315), and `scripts/luna-eval` (confirm T039 uses the default) to it. Make `scripts/wiki-lint --help` point at `wiki lint --help`, and point lint usage in `docs/creative-linting.md`, `docs/architecture.md`, and `README.md` at `wiki lint`.
- [ ] T083 [US7] In `scripts/wiki`, make bare `wiki` print one line per subcommand. Give each subcommand its own `--help` with an `Examples:` block that uses the real invocations from contracts/wiki-cli.md "Examples blocks" (FR-031, FR-032).
- [ ] T084 [US7] Make `lint fix` an argparse subparser under `lint` in `scripts/wiki` (replacing the positional check at line ~674), and allow options anywhere (intermixed parsing). There is no positional `fix` alias: a bare `fix` token exits 2 with the FR-035 object, `hint` "lint fix is a subcommand", and the example `wiki lint fix <paths>` (`wiki lint fix entities/place/Belumara.md`) (FR-034, contracts/wiki-cli.md "Shape").
- [ ] T085 [US7] Add `--stdin` to `scripts/wiki`: newline-separated paths for lint, lint fix, and health, and one JSON payload for mutate and repair. Add `--paths-only` output. No command prompts, and a missing required input is an error (FR-030, FR-033).
- [ ] T086 [US7] Implement the FR-035 error object in `scripts/wiki` and `tools/wiki_ops/cli.py`: exit 2, JSON on stdout with `status`, `error`, `hint`, `example`, and `list_valid`, and the same message on stderr. Cover the six contract cases, and list the allowed scope kinds `files|directory(dir)|entity_type(type)|identity_set|changed|bundle`.
- [ ] T087 [US7] Make `lint fix`, `mutate`, and `repair` in `scripts/wiki` accept `--dry-run`, which returns `"planned": [...]` and writes nothing. A second identical run returns `"changed": []` and `"status": "already_done"`. Add no confirmation prompt, so no `--yes` flag is needed (FR-036, FR-037).
- [ ] T088 [US7] Make every `scripts/wiki` success result include `status`, `vault`, `changed`, `counts` (`before`/`after`), `timing.duration_ms`, and `next`. For `health`, report facts only: `focus` is `tools/wiki_ops/health.py` `build_focus` (fixed order lint → remorph → layout → open ledger entries, up to 5), and `next` is its first row, reported as a fact. Replace `_tune`'s "Fix that checker this sitting." (line ~231) with the plain report `wiki lint: slowest checker <script> <ms> ms; next <script> <ms> ms` (FR-038, FR-029). Make T081 pass.
- [X] T089 [P] [US7] Add an `--help` Examples block to `scripts/luna-eval` showing `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/pd/iteration-1`, and make a missing required flag exit 2 with an example (FR-032, FR-035)
- [ ] T090 [US7] Verify V-16 (bare `wiki`, `wiki lint --help`, a bad path and a bare `fix` token each giving exit 2 with `hint`/`example`, `--scope dir`, `wiki lint fix dir:entities/place --dry-run` twice with the same plan, then `already_done` after one real run). Then check SC-010 with the `invocation_errors` metric (data-model §3, quickstart V-16): write one task per `scripts/wiki` subcommand (`lint`, `lint fix`, `query`, `health`, `mutate`, `repair`) as records in a scratch, uncommitted `/tmp/030/sc010/evals/evals.json`, each prompt holding only the `scripts/wiki --help` output and the task. Run each with a cold `scripts/luna-eval` subject (`--config without_skill`, default model and effort, no other context). Every run's `metrics.json` must have `invocation_errors: 0` (list `invocation_error_commands` otherwise), and re-running each mutating command must produce 0 additional changes (`already_done`). Do not use owner evals or `retries` for SC-010. Record the result in the `specs/030-self-improving-architecture/quickstart.md` V-16 row.

**Checkpoint**: Phase 2 is complete

---

## Phase 10: User Story 8 - Incumbent vs Candidate Instruction Promotion (Priority: P3)

**Goal**: At least one owner skill is promoted by an agent following `skill-creator`, from a report that states regressions and medians but no verdict (SC-012)

**Independent Test**: Quickstart V-18

- [ ] T091 [US8] Change `.agents/skills/skill-creator/scripts/aggregate-benchmark.py` to report only, per eval, task-outcome regressions and assertions that passed for the incumbent and fail for the candidate, plus the medians of `total_tool_calls`, `retries`, `tokens.total`, and latency (from `timing.json`). It prints no verdict and no mean ± stddev, and refuses a comparison whose runs differ in `model` or `effort` (data-model §3, FR-044, contracts/eval-run.md "Promotion report").
- [ ] T092 [US8] Add the promotion rule to `.agents/skills/skill-creator/SKILL.md` (FR-044, SC-012): one run per config on the same eval ids, with the same `model` and `effort` as the FR-019 baseline; refuse on any worse per-eval task outcome or any incumbent-passing assertion that now fails; promote only on a lower median of tool calls, retries, or tokens with none of the three higher; do not use mean ± stddev. Keep the skill no longer than before (SC-013) by replacing the text it supersedes.
- [ ] T093 [US8] Pick one of the six owners. Draft one small candidate edit to `.agents/skills/<owner>/SKILL.md` in the working tree, drawing on its US3 baseline run dirs under `/tmp/030/baseline/`: the current instruction, failed and successful tasks, tool results, assertion failures, user corrections, and token/tool-call cost (FR-043)
- [ ] T094 [US8] Snapshot the incumbent skill directory from HEAD to `/tmp/030/incumbent/<owner>/` (`git archive HEAD .agents/skills/<owner> | tar -x -C /tmp/030/incumbent`). Run `scripts/luna-eval --config old_skill --subject-skill /tmp/030/incumbent/.agents/skills/<owner>` and `--config with_skill` once each on the same eval ids with the baseline `--model`/`--effort`, plus the cross-skill baseline cases from T054 (FR-042, spec Edge Case).
- [ ] T095 [US8] Run `aggregate-benchmark.py` on the two configs. Decide keep or refuse by following the rule in `skill-creator/SKILL.md` (T092); on refuse, `git checkout -- .agents/skills/<owner>/SKILL.md`. Record the decision and cite the skill in the `specs/030-self-improving-architecture/quickstart.md` V-18 row.

**Checkpoint**: The promotion rule has been exercised end to end

---

## Phase 11: User Story 9 - Skills Stay Small; Procedure Moves into Tools (Priority: P3)

**Goal**: The six owner skills answer the five FR-040 questions and shrink, because deterministic procedure now lives in tools while every judgment stays in the skill

**Independent Test**: Quickstart V-19

- [ ] T096 [US9] Record `wc -l .agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/SKILL.md` to `/tmp/030/skill-lines-before.txt`, and snapshot those dirs to `/tmp/030/incumbent-us9/` for old_skill runs
- [ ] T097 [US9] Make `scripts/manifest.py` report the manifest facts named in recorded trajectories (facts only, no interpretation), with a regression in `tests/test_wiki_ops.py` (FR-029, FR-011)
- [ ] T098 [US9] Move deterministic repair bookkeeping (fixes with exactly one correct output) into `wiki lint fix` in `scripts/wiki` and `tools/wiki_ops/cli.py`, with a regression in `tests/test_wiki_cli.py` (FR-029, FR-011). Repair choices stay in the skills.
- [ ] T099 [P] [US9] Shorten `.agents/skills/place-design/SKILL.md`. Remove only deterministic text now covered by T082, T088, T097, and T098 (path discovery, health facts, manifest facts, repair bookkeeping). Keep every judgment, and make sure the five FR-040 answers are present.
- [ ] T100 [P] [US9] Shorten `.agents/skills/faction-design/SKILL.md` in the same way as T099
- [ ] T101 [P] [US9] Shorten `.agents/skills/session-beats/SKILL.md` in the same way as T099
- [ ] T102 [P] [US9] Shorten `.agents/skills/run-guide/SKILL.md` in the same way as T099
- [ ] T103 [P] [US9] Shorten `.agents/skills/wiki-query/SKILL.md` in the same way as T099
- [ ] T104 [P] [US9] Shorten `.agents/skills/wiki-lint/SKILL.md` in the same way as T099 (it builds on T079, and keeps the `Deprecated.*`, broken-image, and identity judgments)
- [ ] T105 [US9] Verify V-19. Line counts must not exceed `/tmp/030/skill-lines-before.txt`. Rerun each skill's evals with `scripts/luna-eval` `--config with_skill` against `--config old_skill --subject-skill /tmp/030/incumbent-us9/...`, report with `aggregate-benchmark.py`, and apply the `skill-creator` rule (T092). Revert any skill it refuses.

**Checkpoint**: Phase 3 is complete

---

## Phase 12: Polish, Consolidation Check & Cross-Cutting Concerns

- [X] T106 Add a case to `tests/test_policy_conflicts.py` for the new `scripts/hybrid-sdd-check.py diff` subcommand on fixture input: it fails when an added file is missing from a plan's "New files" table, fails when a path from the "Deleted or folded" table is still referenced in a maintained surface (`AGENTS.md`, `docs/`, `.agents/`, `scripts/`, `tools/`, `tests/`, `package.json`, `README.md`; completed specs excluded per round-3 gap 1), and passes otherwise. Confirm it fails before T107.
- [X] T107 Add the `diff --plan <plan.md> --base <ref>` subcommand to `scripts/hybrid-sdd-check.py` (plan "New files", SC-014 a/c; diagnostic only, it reports and decides nothing). Make T106 pass.
- [X] T108 Run V-20 (SC-014): `python3 scripts/hybrid-sdd-check.py diff --plan specs/030-self-improving-architecture/plan.md --base main`. It must pass: the only added files are `wiki/_meta/identity-index.json` and `tests/test_luna_eval.py`, and none of the 10 deleted paths (`scripts/wiki-identity`, `scripts/lint-wiki-write`, `scripts/lint-obsidian-markdown`, `scripts/lint-literal-newlines`, `scripts/vale-vocab`, `tools/check_wiki_pages.py`, and skill-creator's `run-eval.py`, `run-loop.py`, `improve-description.py`, `generate-report.py`) exists or is referenced in maintained surfaces. The check for FR-047 (SC-015 c) also treats the 10 deleted fixtures (including `tests/fixtures/creative_lint/CANON002/` and `tests/fixtures/creative_lint/symbolic/stale_reference.md`), the `CANON001` and `CANON002` rules, and the `canon` category as deleted paths that no maintained surface may reference. Re-run V-04c, V-04d, V-04e, and V-04f on the same tree, and check SC-015: (a) no lifecycle, promotion, or confidence field or rule, including `superseded_by`, in maintained surfaces (V-04e), (b) the rule verbatim only in `.agents/skills/llm-wiki/SKILL.md` with both AGENTS.md files pointing to it (V-04f), (c) no code path assigns or gates on canon. SC-014 (f) is superseded by SC-015. SC-014 (b), (d), and (e) are Review judgments against plan "Simplify and consolidate".
- [X] T109 Confirm the `<!-- SPECKIT START -->`…`<!-- SPECKIT END -->` block in `AGENTS.md` (line ~584) still points at `specs/030-self-improving-architecture/plan.md`
- [X] T110 Run the full `pytest -q` and compare it with `/tmp/030/pytest-before.txt`. It must show no new failures and no Vale E100.
- [ ] T111 Run `git diff --stat`. Only after all scratch timing runs (T065, T066, T067, T090) are done, revert the FR-028 bookkeeping files `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` where their changes are measurement state rather than part of an intended change.
- [ ] T112 Re-run quickstart V-01, V-03, V-04b, V-04c, V-04d, V-04e, V-04f, V-09, V-11, V-15, V-16, and V-20 on the final tree, and fill in any empty result rows in `specs/030-self-improving-architecture/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup. T004 gates US5 and US6. T005 gates T041.
- **Phase 1 stories (US1–US4)** come before Phase 2 stories (US5–US7), which come before Phase 3 stories (US8–US9). This order is binding (spec Assumptions).
- **Polish (Phase 12)**: After all stories

### User Story Dependencies

- **US1 (P1)**: After Foundational. There are no story dependencies. It is the MVP. T007's `Deprecated.DMThesis` outcome depends on T022's vocabulary exclusion, not only on removing `CoDM` from `BasedOnStyles` (T013); T021→T022 run after T020 and before the canon track. Its canon track (T025–T033) is not gated (constitution v7.0.0 meets X) and runs after T016.
- **US2 (P1)**: After US1, because eval runs need green checks. T037 and T035/T038 can start any time.
- **US3 (P1)**: After US2, because it needs `metrics.json` and `grading.json` (T041–T044)
- **US4 (P1)**: After US1 (Vale fixed, lint rules folded, canon migration and cache refresh done, so the index never carries `lifecycle` and SC-007 timings run on migrated pages). It is independent of US2 and US3, except T066, which writes after T056.
- **US5 (P2)**: T069 and T070 are independent. T071 needs US2 (luna-eval) and T080 (new ledger format).
- **US6 (P2)**: After US1, US2, and US4, whose drains (T012, T014, T053, T068) use the current CLI and must land before T075 removes `--cause-fixed` and before migration (T077)
- **US7 (P2)**: After US4 (the `wiki-lint` output shape) and US6 (`scripts/wiki` `error list` callers). T089 needs T039–T043.
- **US8 (P3)**: After US2, US3, and US5
- **US9 (P3)**: After US7 (T082, T088), US3, and US8 (T092). T104 comes after T079.

### Within Each User Story

- Tests are written first and must fail. Then comes implementation, then the ledger drain in the same commit as the fix, then quickstart verification.
- Tasks on the same file run in sequence (e.g. T039→T043 `scripts/luna-eval`; T073→T076 `scripts/error-ledger.py`; T083→T088 `scripts/wiki`; T060→T061 `tools/wiki_ops/identity.py`; T009 and T010 share `tests/test_wiki_ops.py`; T026→T030 edit `tools/lint_wiki.py` and the tests after T016).

### Parallel Opportunities

- T003 runs alongside T002.
- US1: T006 ∥ T007 ∥ T008 ∥ T009 (then T010 in the same file). The OMP track (T011–T012) is independent of the Vale track (T013–T015) and the one-linter track (T016–T020), apart from sharing `errors.md` at commit time. The canon track follows the one-linter fold: T025→T026→T027→T028→T029→T030 in order, then T031 ∥ T032 (then T033); T023 can run any time in US1. All of it finishes before US4.
- US2: T035 ∥ T037 ∥ T038 ∥ T044 ∥ T045 ∥ the `scripts/luna-eval` chain T039–T043.
- US4 can run alongside US2 and US3 once US1 is done.
- US5: T069 ∥ T070. US6: T078 ∥ T079.
- US7: T089 ∥ T082–T088.
- US9: T099–T104 in parallel (one skill each).

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
Task: "T037 Rewrite 026 references in specs/026-agent-autonomy-scope/*"
Task: "T044 Update .agents/skills/skill-creator/agents/grader.md"
Task: "T045 Update .agents/skills/skill-creator/references/schemas.md"
```

## Parallel Example: User Story 9

```bash
Task: "T099 Shorten .agents/skills/place-design/SKILL.md"
Task: "T100 Shorten .agents/skills/faction-design/SKILL.md"
Task: "T101 Shorten .agents/skills/session-beats/SKILL.md"
Task: "T102 Shorten .agents/skills/run-guide/SKILL.md"
Task: "T103 Shorten .agents/skills/wiki-query/SKILL.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup and Phase 2 Foundational
2. Phase 3 (US1): green OMP and Vale checks with 9 ledger entries drained, `Deprecated.*` as judgment repairs, and `wiki lint` as the only linter, and the three-rule canon with the lifecycle machinery removed
3. **STOP and VALIDATE**: V-01 to V-04f

### Incremental Delivery

1. US1 → US2 → US3 → US4 (Phase 1 coherent baseline; each checkpoint is independently verifiable)
2. US5 → US6 → US7 (Phase 2 close the loop)
3. US8 → US9 (Phase 3 optimize, measured against the US3 baseline)
4. Phase 12: SC-014 diff check (V-20), then final reruns

### Open gaps

- Resolved by cae8bb44 and b14ea71b: plan round-1/2 gaps 1–6 (identity prefilter candidates, exact-match same cause, optional `expected_output`, fixed assertion vocabulary, SC-009 window as an assumption, tracked FR-028 bookkeeping), the six-owner set (eval-run CHK006), identity-index tracking (performance CHK006), and `resolve_identity`/`_path_for` scope (performance CHK021). Resolved by df3e5c7c: wiki-cli CHK011 (no positional `fix` alias).
- Plan default kept: error-ledger CHK011, an identical occurrence means the same `sitting` + `detail` (T072).
- Round-3 Clarify gaps, resolved at plan 922a0796 (no extra task): (1) SC-014 (c) covers maintained surfaces only; completed specs such as `specs/024-*` and `specs/025-*` stay as records. (2) The 21 broken image links are `human_repair` agent work under `wiki-lint`, not in this feature's tasks. (3) The one-off, uncommitted migration satisfies FR-010's "first run". (5) `scripts/vale-vocab` and `tools/check_wiki_pages.py` are folded and deleted (T019, T020).
- Round-3 Clarify gap 4 (consolidate promotion): resolved by 27039b9d, then superseded by FR-047 (5ce37294). There is no promotion: `consolidate.md` §3 is deleted (T023) and `consolidate_main` gets no `drafts` report.
- Round-4 Clarify gaps 1–4: resolved by Clarify (spec c6f53f02, plan 887e6c47): (1) the 7 extra "canon proposal" lines become "canon under the rule in `llm-wiki`" (T033); (2) `CANON002` is deleted with `CANON001` and the `canon` category (T026, T030); (3) `superseded_by` is dropped (T029, T031) and `tier` is unchanged; (4) spec citation fixes are applied. Nothing is pending except error-ledger CHK011 as a plan default.
- Constitution principle X: met by v7.0.0 (f489409d), so the canon track is not gated.

---

## Notes

- [P] tasks touch different files and have no dependency on incomplete tasks.
- Every fix lands with its regression and its `errors.md` drain in one commit (FR-008, FR-011).
- Scratch output under `/tmp/030/` is never committed. FR-028 bookkeeping files are committed with the change that caused them and reverted after scratch measurement runs.
