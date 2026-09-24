# Quickstart: validating feature 030

This is a validation guide only. The formats it checks are defined in [data-model.md](data-model.md) and [contracts/](contracts/).

## Prerequisites (every run)

```bash
cd <clone>                                    # e.g. /workspace/agentic-co-dm
uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0 pytest
export PATH="$PWD/.venv/bin:$PATH"
export OBSIDIAN_VAULT_PATH="$PWD/wiki"        # REQUIRED until FR-027 lands: ~/.obsidian-wiki/config points at /home/box/agentic-co-dm/wiki
```

After a timing run, lint may have rewritten `wiki/_meta/lint-cache.json` and `styles/config/vocabularies/CoDM/accept.txt`. Run `git diff --stat` before committing.

## Phase 1

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-01 | OMP disabled passes (US1-1, SC-001) | `scripts/check-omp-baseline.sh` | `omp-speckit-baseline: pass (… config-caps …)` |
| V-02 | OMP enabled / missing fails | `pytest tests/test_omp_baseline.py` | Enabled config fails naming `backend=<value>`. Missing block fails with `memory key missing`. |
| V-03 | Vale loads (US1-3, SC-002) | `vale --output=line wiki/entities/place/Belumara.md` | No `E100`. `Deprecated.*` rules are active (e.g. `Deprecated.DMThesis` fires on a scratch file containing "DM Thesis" outside `wiki/`). |
| V-04 | Full suite runs (SC-002) | `pytest -q` | Completes. No Vale E100 failures. |
| V-05 | Scoped timing (SC-007) | `scripts/wiki lint entities/place/Belumara.md` after editing one character of that page in a scratch branch; run it twice | Run 1 `timing.duration_ms` < 5000, and `identity.compared` equals selected + candidates, far below the page count. Run 2 has `cache.hits: 1`. Record both numbers here and on the maintainer workstation. Box reference 2026-09-24 (Vale on, pre-fix): 3.72 s / 0.28 s. |
| V-06 | Identity parity (FR-025/026) | `python -c "from tools.wiki_ops.identity import scan_identities as s; import json,sys; json.dump([i.to_dict() for i in s('wiki')], sys.stdout, sort_keys=True)"` once with `wiki/_meta/identity-index.json` deleted and once warm; `diff` the two outputs; repeat with `--scope`-equivalent selection | Identical output. Whole-vault `wiki lint` findings match those at the pre-change commit. |
| V-07 | Corrupt index (Edge Case) | Write `{` into `wiki/_meta/identity-index.json`, then run V-05 | The index is rebuilt and the findings match V-06. |
| V-08 | Health baseline (SC-007) | `time scripts/wiki health` | Exits without a harness timeout. Wall time is recorded next to the SC-006 baseline. Box reference 2026-09-24 (cold, 836 misses): 82.3 s, identity 55.1 s. |
| V-09 | One eval schema (SC-003) | `python3 - <<<'import json,glob; bad=[f for f in glob.glob(".agents/skills/*/evals/evals.json") if "skill_name" not in (d:=json.load(open(f))) or any("expectations" in e or not e.get("assertions") for e in d["evals"])]; print(bad)'` and `rg -il "work gate|chat proposal" .agents/skills/*/evals/evals.json` | `[]`, and no matches asserting that behavior as required. |
| V-10 | One runner (SC-004, SC-005) | `scripts/luna-eval --skill .agents/skills/place-design --eval <skill_selected id> --out /tmp/030/iteration-1`, then the same record through the skill-creator workflow | Both run dirs contain `timing.json`, `metrics.json`, and `grading.json` with the same keys. The `skill_selected` item has `passed: true`. |
| V-11 | 026 references (SC-008) | `rg "check-agent-standards\|test_agent_standards\|AGENT00[1-3]" specs/026-agent-autonomy-scope` | No matches. |
| V-12 | 029 baseline (SC-006) | Inspect `specs/029-agent-loop-closure/quickstart.md` records | ≥10 cases across all 9 categories, each with every FR-016 metric. T003…T049 checked. |

## Phase 2

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-13 | Migration (FR-010, SC-009) | `python3 scripts/error-ledger.py error migrate --dry-run`, then run it for real, then run it again | Dry run writes nothing. The real run merges the OMP, Vale, and identity groups and removes drained entries. The third run reports `already_done`. |
| V-14 | Attach, not duplicate (US6-1) | `error append --source .vale.ini --cause "Scoped lint blocked: Vale style CoDM missing" --sitting "test"` twice (in a scratch copy, before Vale is drained) | First run `attached` to e-212, second `already_done`. No new id. |
| V-15 | Recurrence (FR-009) | `python3 scripts/error-ledger.py error recurrence` | `{"total": n, "by_sitting": {...}}` |
| V-16 | CLI contract (SC-010) | `wiki`, `wiki lint --help`, `wiki lint wiki/entities/place/Belumara.md`, `wiki lint --scope dir`, `wiki lint fix dir:entities/place --dry-run` (twice) | Bare `wiki` lists subcommands only. Help shows only lint, with Examples. The bad path gives exit 2 with the `hint` and `example` keys. The second dry run shows the same plan, and after one real run a rerun reports `already_done`. |
| V-17 | Seeded friction (SC-011) | 5 cold `luna-eval` subjects on a scratch branch where one owner skill names a retired command path | At least 4/5 fix the source, add a regression, and finish the owner task, with no new `errors.md` entry. |

## Phase 3

| ID | Scenario | Command | Expected |
|---|---|---|---|
| V-18 | Promotion (SC-012) | Snapshot the incumbent skill, then `luna-eval --config old_skill --subject-skill <snapshot>` vs `--config with_skill` on the same ids, then `aggregate-benchmark.py` | The candidate is kept only if non-inferior on success and quality, with lower median tool calls, retries, or tokens. |
| V-19 | Small skills (SC-013) | `wc -l` on touched owner `SKILL.md` before and after; rerun each skill's evals | Line count is not higher. Evals are non-inferior. The five FR-040 answers are present. |
