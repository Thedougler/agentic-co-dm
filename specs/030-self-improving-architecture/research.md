# Research: Self-Improving Architecture (030)

Each decision names the chosen option, why it was chosen, and what else was considered. Code facts were read on branch `030-self-improving-architecture` @ bf021f03.

## R1 OMP memory check

- **Decision**: In `scripts/check-omp-baseline.sh`, read the `backend:` line under `memory:`. `false` and `off`, quoted or not, pass. Any other value fails with `memory enabled: backend=<value>`. A missing `memory:` block, or a missing `backend:` line, fails with `memory key missing`.
- **Rationale**: `.omp/config.yml` line 54–55 is `memory:` / `backend: false`. The current check is `grep -A1 '^memory:' | grep -qE 'backend: "?off"?'`, so it rejects `false`. That is the root cause of e-205, e-207, e-209, and e-211.
- **Alternatives**: changing the config to `"off"` was rejected, because it hides a checker defect and the spec calls `false` correct (US1-1). A YAML parser in bash was rejected; one `python3 -c` with PyYAML is acceptable but not needed for one key.

## R2 Vale

- **Decision**: remove `CoDM` from the 6 `BasedOnStyles` lines in `.vale.ini`. Nothing else changes: `styles/Deprecated/{DMThesis,FactionClock}.yml`, `Vocab = CoDM`, the `Packages` line, and `tools/creative_lint/vale_vocab.py` all stay.
- **Rationale**: `styles/` has no `CoDM` directory. Vale 3.21.0 exits with `E100 [loadStyles] … style 'CoDM' does not exist on StylesPath` (reproduced 2026-09-24). Nick's decision and constitution v6.0.1 XXIV keep `Deprecated` and the vocabulary in Vale. For region, creature, and npc pages, `BasedOnStyles` becomes `Deprecated` alone, which is what actually loaded before `CoDM` went missing.
- **Alternatives**: recreating a `CoDM` style was rejected, because FR-023 bars new custom Vale styles. Moving `Deprecated` to Python was rejected by Nick's 2026-09-24 decision.

## R3 errors.md format and matching

- **Decision**: store one JSON line per entry, `{"id","cause","source","evidence":[{"sitting","detail"}]}`, keeping the `# Error ledger` heading. `append --source S --cause C --sitting X [--detail D]` attaches to an open entry when `source` is equal and `cause_key(C) == cause_key(entry.cause)`. `cause_key` casefolds, collapses whitespace, and drops digits and backtick- or quote-wrapped literals. `--attach e-N` forces the target over the cause match, but it is refused (exit 2 plus a hint, nothing written) when e-N's `source` differs (FR-007). A regression test covers the refusal. `drain --id e-N` deletes the entry. The `--cause-fixed` flag is removed along with the `cause_fixed` field (FR-006). Passing it exits 2 with a hint and the correct example (`error drain --id e-N`), and `AGENTS.md` line ~200 is updated in the same change.
- **Rationale**: the fields come from the Clarification (Session 2026-09-24). An exact-text match would not have merged e-214, e-215, e-216, and e-218, because their wording differs. A normalized key plus an explicit `--attach` stays deterministic and explainable.
- **Migration** (`error-ledger.py error migrate`, idempotent): drop entries with `status == "drained"`. Map each open entry to `{id, cause, source, evidence:[{sitting, detail: cause}]}`. Merge the named groups into their lowest id:
  - OMP: e-205, e-207, e-209, e-211 → e-205, `source: scripts/check-omp-baseline.sh`
  - Vale: e-212, e-214, e-215, e-216, e-218 → e-212, `source: .vale.ini`
  - Identity: e-206, e-208, e-213 → e-206, `source: tools/wiki_ops/identity.py`

  The other open entries (e-168, e-201, e-202, e-203, e-210, e-217) get a `source` set by hand in the migration commit, taken from their cause text: e-202 → `scripts/wiki`, e-210 → `.agents/skills/skill-creator/scripts/run-eval.py`, and so on. The Phase 1 fixes then drain the OMP, Vale, and e-210 entries in their own commits (FR-008).
- **Recurrence**: `error-ledger.py error recurrence` returns `{"total": Σ(len(evidence)-1), "by_sitting": {sitting: count of non-first occurrences}}`.
- **Alternatives**: keeping `status`/`cause_fixed` was rejected, because only open entries remain (Clarification). A separate recurrence log was rejected, because git history already holds drained entries.

## R4 Scoped identity

- **Findings from code**: `scripts/wiki lint` always calls `scripts/wiki-lint --scope files:<cache misses>`. Whole-vault lint is therefore the scoped path with every miss selected. `scan_identities` always runs `_pages(vault)`: it does `rglob`, reads every page, and builds a `Counter` of body characters for every page. Since 6c374829, only pairs touching the selected pages are compared. Measured today: identity takes 843 ms for 1 page, of which the whole-vault read and profile is the bulk. `resolve_identity` (mutation gate) and `_path_for` also walk the vault.
- **Decision**: keep a derived index, `wiki/_meta/identity-index.json` (data-model §4), with one row per page: the cheap fields plus a compact character profile, keyed by `content_sha256`. On each run:
  1. List paths (`os.scandir` walk; `stat` only).
  2. For each path whose `(size, mtime_ns)` differs from the row, rehash. If the hash differs, re-read that one page and rebuild its row.
  3. Drop rows for missing paths.
  4. Build exact maps from the rows: `norm(title)`, `norm(alias)`, and `stem` → paths. Load the manifest provenance and transitions.
  5. For each selected page, candidates = same `type`, no redirect, and (title/alias match, OR shared provenance with stem ratio > 0.7, OR a merge transition, OR a profile-prefilter pass > 0.6).
  6. Run `SequenceMatcher` only for candidate pairs whose `(sha_a, sha_b)` ratio is not already in the index's `pairs` map; read only those bodies.
  7. Report `compared = |selected ∪ candidates|`.
- **Rationale**: the candidate predicate is exactly the one in today's `_resolve_row_identity`, evaluated from cached data. Scoped, cached, cold, and whole-vault findings stay identical (FR-025/FR-026), and the vault is no longer re-read on every run. The index format version and the `.manifest.json` hash sit in the header. A version mismatch or parse error rebuilds the index (spec Edge Case).
- **Alternatives**: storing identity rows inside `lint-cache.json` `extracts` was rejected, because lint-cache entries are invalidated by the rules digest and exist only for linted pages, while identity needs every page. Dropping the content-similarity candidate path to match FR-024's literal list was rejected, because it changes findings (spec gap 1 in plan.md). A daemon or SQLite store was rejected (XIV).

## R5 Evaluator unification

- **Decision**: `scripts/luna-eval` stays the only runner. It adds three things:
  - repo-root discovery via `git rev-parse` or the script's parent, so it runs from any working directory.
  - `metrics.json`, derived after the run from `events.jsonl` (codex `--json` event stream): `tool_calls` by kind, `total_tool_calls`, `retries` (a failed command re-run with the same argv), `invocation_errors` (FR-027 command calls rejected as usage errors, counted even when corrected; data-model §3; the SC-010 measure), `duplicate_actions` (an identical command or file edit repeated after success), `tokens` (the sum of `turn.completed.usage`), `completion_reason` (exit/usage-limit/no-output code), `model` and `effort` as passed to codex (FR-019), and `skills_read` (`SKILL.md` paths the subject opened).
  - a deterministic `skill_selected` grade in `grading.json`.

  `skill-creator` then invokes `luna-eval` per eval and config. `run-eval.py`, `run-loop.py`, and `improve-description.py` are deleted along with the "Description optimization" section of `SKILL.md`. Skill selection is proven by `skill_selected` records in the same `evals.json` (FR-015).
- **Rationale**: e-210 is the second-runner defect. The viewer and `aggregate-benchmark.py` already read `grading.json` + `timing.json` + `metrics.json`, so extending the luna-eval run directory with those files is the one shared format (spec Assumptions).
- **To verify during implementation**: the codex `--json` event names (`item.completed` with `command_execution`/`file_change`, `turn.completed.usage`) against a real `events.jsonl` from one `luna-eval` run. If they differ, `metrics.json` maps whatever is present and records `null`, never a guess.
- **Alternatives**: keeping `run-eval.py` for description triggering was rejected by FR-015. A new grader script for all types was rejected; semantic grading stays with `agents/grader.md`.

## R6 CLI discovery and shape

- **Decision**: vault resolution order is `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo_root>/wiki` if it exists (from `pyproject.toml` `[tool.agentic-co-dm] vault`) > `~/.obsidian-wiki/config`. Repo root comes from the script location, not the working directory. `lint fix` becomes an argparse subparser under `lint`. FR-034 says `lint fix` MUST be a real subcommand, not a positional `fix` token inside the path list, so no alias is kept. A bare `fix` token among the paths exits 2 with a hint naming the `wiki lint fix …` form, and docs that use the old token are updated in the same change. The full contract is in `contracts/wiki-cli.md`.
- **Rationale**: today the global config outranks the repo's own `wiki/`, so a clone at `/workspace/agentic-co-dm` silently lints `/home/box/agentic-co-dm/wiki`. This was observed on 2026-09-24 and is why quickstart must export `OBSIDIAN_VAULT_PATH`. Repo-relative paths such as `wiki/entities/place/Belumara.md` are rejected with `path not found in vault` (observed). Under FR-035 the error must name the vault-relative form.
- **Alternatives**: accepting `wiki/`-prefixed paths silently was rejected, because feature 027 says "no fuzzy paths". The error names the fix instead.

## R7 Timing and health

- **Measured (2026-09-24, bf021f03, 8-core Linux, Vale 3.21.0, `CoDM` removed in the working tree only)**:
  - one-page cold lint: 3.72 s wall; `wiki-lint` breakdown lint_wiki 1662 ms, engine 772 ms, identity 843 ms, vale 584 ms.
  - rerun from the lint cache: 0.28 s.
  - SC-007's < 5 s is met today with Vale.
- **`wiki health`** (whole vault; the rules digest changed, so 836 of 837 lint targets missed the cache): exit 0, status `findings`, **82.3 s** wall, 80.9 s of it in `health.lint`. Breakdown: identity **55.1 s**, creative engine 15.7 s, vale 13.1 s, lint_wiki 1.9 s, token-count 0.6 s. No harness timeout applied here. This is the cold worst case. In steady state, misses are only the changed pages.
- **Consequence for R4**: with 836 selected pages, identity cost is the pairwise `SequenceMatcher` on prefilter passes, not the vault read. The index therefore also caches pair ratios keyed by the two `content_sha256` values (data-model §4). A ratio is a pure function of the two bodies, so reusing it cannot change findings. After one cold run, whole-vault identity recomputes only pairs that touch changed pages.
- **Side effect observed**: running lint with Vale rewrote the tracked `styles/config/vocabularies/CoDM/accept.txt` (via `tools/creative_lint/vale_vocab.py`) and `wiki/_meta/lint-cache.json`. Both were reverted after measuring. cae8bb44 (FR-028) settles that these files stay tracked as lint bookkeeping.
- **Setup needed on any fresh box**: `uv venv .venv && uv pip install --python .venv/bin/python PyYAML tiktoken vale==3.21.0.0`, `PATH=.venv/bin:$PATH`, `OBSIDIAN_VAULT_PATH=<clone>/wiki`. Earlier notes said pip in the lint venv was broken and `tiktoken` was missing. A fresh `uv` venv avoided both.
- **Maintainer workstation**: SC-007 names the maintainer workstation, so quickstart V-05 is rerun there. The box numbers above are the reference.
