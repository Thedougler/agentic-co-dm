# Quickstart: validating feature 030

This is a validation guide only. The formats it checks are defined in [data-model.md](data-model.md) and [contracts/](contracts/).

## Prerequisites (every run)

```bash
cd <clone>                                    # e.g. /workspace/agentic-co-dm
uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0 pytest
export PATH="$PWD/.venv/bin:$PATH"
export OBSIDIAN_VAULT_PATH="$PWD/wiki"        # REQUIRED until the single discovery helper (FR-027) lands: ~/.obsidian-wiki/config points at /home/box/agentic-co-dm/wiki
```

Timings come from each command's own result (`timing.duration_ms` in the `scripts/wiki` JSON, e.g. `scripts/wiki health | python3 -c 'import json,sys; print(json.load(sys.stdin)["timing"]["duration_ms"])'`), not from a manual `time`.

Lint rewrites the tracked bookkeeping files `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` (FR-028). After a scratch timing run, revert them rather than committing measurement state.

## Phase 1

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-01 | OMP disabled passes (US1-1, SC-001) | `scripts/check-omp-baseline.sh` | `omp-speckit-baseline: pass (… config-caps …)` |
| V-02 | OMP enabled / missing fails | `pytest tests/test_policy_conflicts.py` | Enabled config fails naming `backend=<value>`. Missing block fails with `memory key missing`. |
| V-03 | Vale loads (US1-3, SC-002) | `vale --output=line wiki/entities/place/Belumara.md` | No `E100`. `Deprecated.*` rules are active (e.g. `Deprecated.DMThesis` fires on a scratch file containing "DM Thesis" outside `wiki/`). This passes only after the `vale_vocab.py` `DM` exclusion and a vocab refresh: `rg -nx 'DM' styles/config/vocabularies/CoDM/accept.txt` returns nothing (Analyze B1, research R2). |
| V-04 | Full suite runs (SC-002) | `pytest -q` | Completes. No Vale E100 failures. |
| V-04b | Deprecated is a judgment repair (FR-023) | `scripts/wiki lint <scratch page containing "DM Thesis">`, then `scripts/wiki lint fix <same> --dry-run` | Finding `VALE_Deprecated.DMThesis` has `repair_class: human_repair` and no `repair_action`. `lint fix` plans no change for it. `wiki lint` refreshes the vocab first, so the finding appears only with the `DM` exclusion in place (research R2). |
| V-04c | One linter (XXI, FR-046) | `ls scripts/lint-wiki-write scripts/lint-obsidian-markdown scripts/lint-literal-newlines scripts/wiki-identity`; `scripts/wiki lint` | The files do not exist. `wiki lint` reports `table_wikilink_unescaped_pipe` / `broken_image_link` findings (pre-fold reference: 519 / 21). After `wiki lint fix`, `table_wikilink_unescaped_pipe` = 0. |
| V-04d | Folded duplicates (FR-046 rule 2, Clarify gap 5) | `ls scripts/vale-vocab tools/check_wiki_pages.py`; `node -p "require('./package.json').scripts['lint:vale']"`; `./scripts/wiki-reveal --count`; `rg -n 'vale-vocab|check_wiki_pages' AGENTS.md docs .agents scripts tools tests package.json README.md` | Neither file exists. `lint:vale` is `./scripts/wiki lint`. `wiki-reveal --count` exits 0 with the same count as before the change. `rg` finds nothing. |
| V-04e | Canon machinery removed (SC-015 a, c; FR-047) | `rg -n --glob '*.md' '^(lifecycle|lifecycle_changed|lifecycle_reason|base_confidence|canon_status):' wiki -g '!_raw/**'`; `rg -n 'lifecycle|base_confidence|canon_status|TRUST_FIELDS|CANON001' wiki/templates/contracts .agents/skills AGENTS.md wiki/AGENTS.md docs/agents tools scripts rules tests | rg -v 'rule\.lifecycle|lifecycle: (ACTIVE|SHADOW|DRAFT)|"lifecycle": "(ACTIVE|SHADOW)"|SHADOW lifecycle|LIFECYCLES = frozenset|task lifecycle|checkbox lifecycle|hybrid-sdd-check'`; `rg -n -i --hidden 'CANON001|CANON002|superseded_by|canon proposal' AGENTS.md CONTEXT.md wiki/AGENTS.md wiki/templates docs .agents tools scripts rules tests -g '!docs/adr/**'`; rerun `scripts/wiki-bulk-ops frontmatter --vault wiki --action remove --field lifecycle --dry-run --json`; `pytest -q` | All three `rg` return nothing (rule-status and Spec Kit uses are exempt). The dry-run reports `files_modified: 0`. `pytest` passes. No code path reads `lifecycle` from a page. |
| V-04f | One canon owner; faction fix (SC-015 b; FR-047 item 5) | `rg -n -F 'Something is canon if the DM says so' AGENTS.md CONTEXT.md docs .agents wiki/AGENTS.md`; `rg -n 'llm-wiki' AGENTS.md wiki/AGENTS.md`; `scripts/wiki lint entities/faction/Sunkline.md` | Exactly one hit, in `.agents/skills/llm-wiki/SKILL.md`. Both AGENTS.md files link to it. Until an agent adds the section, `Sunkline.md` (`status: active`) reports `TMPL_missing_required` for "Active Agenda", which proves `when:` now keys on `status`. |
| V-05 | Scoped timing (SC-007) | `scripts/wiki lint entities/place/Belumara.md` after editing one character of that page in a scratch branch; run it twice | Run 1 `timing.duration_ms` < 5000, and `identity.compared` equals selected + candidates, far below the page count. Run 2 has `cache.hits: 1`. Record both numbers here and on the maintainer workstation. Box reference 2026-09-24 (Vale on, pre-fix): 3.72 s / 0.28 s. Box 2026-09-24 after T061 (ddc79b4d): run 1 3591 ms, `identity.compared` 179 of 817 pages (`index.misses` 1); run 2 178 ms, `cache.hits: 1`. Maintainer-workstation rerun pending. |
| V-06 | Identity parity (FR-025/026) | `python -c "from tools.wiki_ops.identity import scan_identities as s; import json,sys; json.dump([i.to_dict() for i in s('wiki')], sys.stdout, sort_keys=True)"` once with `wiki/_meta/identity-index.json` deleted and once warm; `diff` the two outputs; repeat with `--scope`-equivalent selection | Identical output. Whole-vault `wiki lint` findings match those at the pre-change commit. |
| V-07 | Corrupt index (Edge Case) | Write `{` into `wiki/_meta/identity-index.json`, then run V-05 | The index is rebuilt and the findings match V-06. |
| V-08 | Health, few pages changed (SC-007) | With the lint cache and identity index current, edit 1–3 pages, then run `scripts/wiki health` and read `timing.duration_ms` | < 10 s. Warm reference 2026-09-24 (spec): 2.6 s. Maintainer workstation 2026-09-24 after the merge of main: 2 pages edited, 4201 ms, `lint.cache` 835 hits / 2 misses. |
| V-08b | Health after a rules change (SC-007) | With the identity index current, change the rules digest (e.g. add a comment line to `.vale.ini` on a scratch branch) so every lint-cache entry misses, then run `scripts/wiki health` and read `timing.duration_ms`; confirm `lint.cache.misses` ≈ page count and `identity.index.misses` = 0 | < 50 s. Pre-change reference 2026-09-24 (no index): 82.3 s, identity 55.1 s. Revert the scratch edit afterwards. Box 2026-09-24 after T061: 45 810 ms, `lint.cache.misses` 837, `identity.index.misses` 0. |
| V-08c | Health from scratch (SC-007) | Delete `wiki/_meta/identity-index.json` and `wiki/_meta/lint-cache.json` on a scratch branch, then run `scripts/wiki health` and read `timing.duration_ms` | Finishes. Wall time is recorded next to the SC-006 baseline (no bound). Maintainer workstation 2026-09-24: finished, 72 648 ms, 837 lint misses. |
| V-09 | One eval schema + Work-gate wording (SC-003) | `pytest tests/test_luna_eval.py` (the schema check in `luna-eval` `load_eval` runs over all 60 files, and the retired-wording case runs over every assertion) | Pass: every file valid, and no assertion text contains `Work gate`, `chat proposal`, or `approval before write`. |
| V-10 | One runner (SC-004, SC-005) | `scripts/luna-eval --skill .agents/skills/place-design --eval <skill_selected id> --out /tmp/030/iteration-1`, then the same record through the skill-creator workflow | Both run dirs contain `timing.json`, `metrics.json`, and `grading.json` with the same keys. The `skill_selected` item has `passed: true`. |
| V-11 | 026 references (SC-008) | `pytest tests/test_policy_conflicts.py` (runs `scripts/check-current-commands --json` over the 026 docs, plus the `AGENT00[1-3]` check) | Pass: every cited `scripts/…`/`tests/…` path exists, and no `AGENT00[1-3]` remains. |
| V-12 | 029 baseline (SC-006) | Inspect `specs/029-agent-loop-closure/quickstart.md` records | ≥10 cases across all 9 categories, each with every FR-016 metric. T003…T049 checked. |

## Phase 2

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-13 | Migration (FR-010, SC-009) | After the one-off conversion (research R3; agent-supplied groups and sources), run `python3 scripts/error-ledger.py error list` | Loads with no legacy field (`status`, `cause_fixed`). No drained entry remains. Each agent-chosen group is one id with concatenated `evidence`. No two entries share `(source, cause.strip())`. `missing_sources` is `[]`. Result 2026-09-24: 18 lines → 5 open entries (e-168, e-201, e-203, e-210, e-217), no legacy fields, `missing_sources: []`; no open same-root groups remained (OMP/Vale/identity drained in US1/US4), and e-202 was drained as already fixed (`scripts/wiki` `parser()` returns the parser). |
| V-14 | Exact attach, forced attach, undo (FR-007) | In a scratch copy: `error append --source .vale.ini --cause "<e-212 cause text, verbatim>" --sitting test`; then the same with reworded cause text; then `--attach e-212` with the reworded text; then `--attach e-212 --source scripts/wiki`; then `error detach --id e-212 --index <k>` | The verbatim run gives `attached` e-212 with `occurrence_index`. Reworded without `--attach` gives `created` (a new id). `--attach` gives `attached`. A cross-source `--attach` exits 2 with a hint. `detach` removes occurrence k, and a repeat gives `already_done`. Result 2026-09-24 (scratch copy, seeded e-218 on `.vale.ini`): verbatim `attached` index 1; reworded `created` e-219; `--attach e-218` `attached` index 2; cross-source exit 2 with hint; `detach --index 2` `detached`, repeat `already_done`. |
| V-15 | Recurrence (FR-009) | `python3 scripts/error-ledger.py error list` | The result includes `recurrence: {"total": n, "by_sitting": {...}}`. Starting total 2026-09-24 after migration: `{"total": 0, "by_sitting": {}}`. |
| V-16 | CLI contract (SC-010) | `wiki`, `wiki lint --help`, `wiki lint wiki/entities/place/Belumara.md`, `wiki lint --scope dir`, `wiki lint entities/place/Belumara.md fix`, `wiki lint fix dir:entities/place --dry-run` (twice); then cold-agent `luna-eval` runs, one per subcommand | Bare `wiki` lists subcommands only. Help shows only lint, with Examples. The bad path and the bare `fix` token each give exit 2 with the `hint` and `example` keys. Every cold-agent run has `metrics.json` `invocation_errors: 0`. The second dry run shows the same plan, and after one real run a rerun reports `already_done`. |
| V-17 | Seeded friction (SC-011) | 5 cold `luna-eval` subjects on a scratch branch where one owner skill names a retired command path | At least 4/5 fix the source, add a regression, and finish the owner task, with no new `errors.md` entry. |

## Phase 3

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-18 | Promotion (SC-012) | Snapshot the incumbent skill, then run `luna-eval --config old_skill --subject-skill <snapshot>` and `--config with_skill` once each on the same ids with the baseline `--model`/`--effort`, then `aggregate-benchmark.py` | The report lists per-eval task-outcome regressions, incumbent-pass → candidate-fail assertions, and medians, with no verdict. The agent decides per `skill-creator/SKILL.md`: refuse on any listed regression; keep only if the median of tool calls, retries, or tokens is lower with none higher. Record the decision and cite the skill. |
| V-19 | Small skills (SC-013) | `wc -l` on touched owner `SKILL.md` before and after; rerun each skill's evals | Line count is not higher. Evals are non-inferior. The five FR-040 answers are present. |

## Consolidation (FR-046, SC-014)

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-20 | SC-014 (a)/(c) mechanical checks | `python3 scripts/hybrid-sdd-check.py diff --plan specs/030-self-improving-architecture/plan.md --base main` | Pass: every added file is in plan.md's "New files" table, and no deleted/folded path in the "Deleted or folded" table is referenced in maintained surfaces. (b), (d), and (e) are Review judgments against the same tables. |
