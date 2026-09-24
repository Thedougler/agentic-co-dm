# Implementation Plan: Self-Improving Architecture

**Branch**: `030-self-improving-architecture` | **Date**: 2026-09-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/030-self-improving-architecture/spec.md` (Clarifications, Session 2026-09-24, all five confirmed by Nick).

## Summary

Collapse, don't add (FR-046). Every change edits the module that owns the concern: `scripts/error-ledger.py` + `errors.md`, `scripts/check-omp-baseline.sh`, `.vale.ini`, `tools/creative_lint/vale_adapter.py`, `tools/wiki_ops/identity.py` + `tools/wiki_ops/lint_cache.py`, `tools/wiki_ops/cli.py` + `scripts/wiki`, `tools/lint_wiki.py`, `scripts/luna-eval`, the `skill-creator` skill, the 60 `evals/evals.json` files, `AGENTS.md`, `.agents/skills/wiki-lint/SKILL.md` + `consolidate.md`, and the feature 026/029 documents. Code only detects, measures, checks, indexes, reports, or applies fixes that have exactly one correct output. Every judgment (duplicate choice, same root cause beyond an exact match, promotion, repair choice, next step) belongs to the agent, and the table in "Simplify and consolidate" names the skill that governs it. The net file count goes down: 1 new data file and 1 new test file; 10 scripts deleted.

The data shapes come first. Each one is defined in [data-model.md](data-model.md):

1. **Error entry**: `{id, cause, source, evidence:[{sitting, detail}]}`. Only open entries exist. Auto-attach happens only on the same `source` with identical, whitespace-trimmed `cause`. Recurrence = occurrences after the first, reported as a field of `error list`.
2. **Eval file**: `{skill_name, evals:[{id, prompt, files?, context?, outputs?, subject_skill?, core?, expected_output, assertions:[{type, text}]}]}`. `skill_selected` and `behavior` are added to the type vocabulary.
3. **Eval run directory** (one result format): the existing `luna-eval` layout plus `metrics.json`, which `luna-eval` derives from `events.jsonl`, plus `grading.json` in the shape the `skill-creator` viewer already reads.
4. **Identity index**: `wiki/_meta/identity-index.json`, one cheap row per page keyed by content hash, loaded and saved by `tools/wiki_ops/lint_cache.py`. It lets a scoped lint stop reading and profiling the whole vault. Its thresholds only report candidates and gate mutations as `ambiguous`.

Phase order is binding (spec Assumptions): Phase 1 = US1–US4, Phase 2 = US5–US7, Phase 3 = US8–US9.

## Technical Context

**Language/Version**: Python 3.12+ (the box venv runs 3.14); Bash for `scripts/check-omp-baseline.sh`

**Primary Dependencies**: stdlib only for new logic. Project-declared: `PyYAML`, `tiktoken`, `vale==3.21.0.0` (PyPI wrapper that installs the Vale binary), dev `pytest`. Vale packages ai-tells, proselint, write-good, and Readability, plus repo-local `styles/Deprecated/`. `codex` CLI (used by `scripts/luna-eval`).

**Storage**: Files. `errors.md` (JSON lines under a heading), `sittings.jsonl`, `.agents/skills/*/evals/evals.json`, eval run dirs under `<skill>-workspace/iteration-N/`, `wiki/_meta/lint-cache.json` (existing), and `wiki/_meta/identity-index.json` (new derived cache, read and written through `lint_cache.py`, tracked as FR-028 bookkeeping).

**Testing**: `pytest` under `tests/`. New tests go in the existing file for each module: `test_error_ledger_repairs.py` (ledger), `test_wiki_cli.py` (`scripts/wiki`), `test_wiki_ops.py` (identity, cache), `test_creative_lint.py` (`vale_adapter`), and `test_policy_conflicts.py` (repo-contract checkers: OMP baseline, cited paths, SC-014 diff check). The one new file is `tests/test_luna_eval.py`, because `scripts/luna-eval` has no test file today. Behavioral evidence runs through `scripts/luna-eval` (constitution IV, XXIII, XXVI).

**Target Platform**: Linux box and the maintainer workstation (macOS). Both run the same CLI.

**Project Type**: Agent-facing CLI tooling plus agent instructions (single repo, no service)

**Performance Goals**: SC-007. Scoped lint of one changed page (cache miss, Vale on) under 5 s. Unchanged page served from the lint cache. `wiki health` finishes under 50 s whenever the identity index is current, including after a lint-rules change that empties the lint cache, and under 10 s when only a few pages changed. A from-scratch rebuild (no index) is recorded, not bounded. The 50 s case depends on the index's cached pair ratios: from the measured cold components, identity drops from 55.1 s to about index-load cost, leaving creative engine 15.7 s + Vale 13.1 s + lint_wiki 1.9 s ≈ 31 s. That is an estimate until V-08b runs.

**Constraints**: Findings stay the same (FR-025/FR-026): cached = cold, and the whole-vault run is unchanged. Commands take no prompts (FR-030). Mutations are idempotent and support `--dry-run` (FR-036/FR-037). The feature 027 result contract stays: agent-shaped default output, `--pretty`, no fuzzy paths.

**Scale/Scope**: About 1,640 non-raw wiki pages. 60 eval files with 533 records (143 use `expectations[]`; 7 have no `skill_name`). 32 `errors.md` lines. 13 eval files carry Work-gate wording. 7 feature 026 docs cite absent executables (66 references).

No NEEDS CLARIFICATION remains. The open design choices are settled in [research.md](research.md). The spec gaps raised by this plan are listed at the end, all resolved by cae8bb44.

## Constitution Check

*GATE: checked before Phase 0 and re-checked after Phase 1. Constitution v6.0.1 (bf021f03).*

| Principle | Status | How the design complies |
|---|---|---|
| III Spec before change | PASS | Spec 030 is clarified. This plan adds no behavior outside it. |
| IV Behavioral tests | PASS | Each tool fix gets a failing-first test at the public seam (FR-011, FR-021, FR-039). Agent-facing changes are proven through `luna-eval` cold subjects (US2, US3, US5, US8). |
| V Single source of truth | PASS | The owning skill is recorded once per eval file (`skill_name`). Ownership is read from each skill, with no separate map (FR-003). The identity index is derived and rebuildable, so it is not a second truth. |
| VI Agent-shaped software | PASS | FR-027–FR-039 contract in [contracts/wiki-cli.md](contracts/wiki-cli.md). Friction gets fixed; `errors.md` is used only when a defect stays unresolved (aligned with v6). |
| VIII Safe automation | PASS | Ledger migration, `lint fix`, and mutation are idempotent and support dry-run. |
| IX / XX Lean | PASS | The design removes the `run-eval.py`/`run-loop.py`/`improve-description.py` trigger path and the stale ledger entries. Skills must not grow (SC-013). |
| XIII Friction rule (v6) | PASS (dependency met) | v6.0.0 (590af34e), kept in v6.0.1, redefines XIII to match FR-006–FR-008 and US5/US6. The blocking prerequisite in spec Assumptions is satisfied. |
| XIV Simplest tool | PASS | Stdlib JSON and argparse. No new dependency. The identity index reuses `lint_cache.py`'s load/save, and checks live in existing tools (see Simplify and consolidate). |
| XVI Layering | PASS | The friction rule is stated once in `AGENTS.md` (FR-002). Skills link to it and do not restate it. |
| XIX Corrections | PASS | `AGENTS.md` line 196 and `wiki-lint/SKILL.md` line 47 are rewritten to "fix and verify; record only if unresolved". |
| XXI One linter | PASS | `wiki lint` becomes the only lint front door. The unique checks in `lint-obsidian-markdown` and `lint-literal-newlines` fold into `tools/lint_wiki.py`, and the three side scripts are deleted. Removing `CoDM` drops no check, because the style never loaded. `TMPL_inherited_deprecated_guidance` is removed as an exact duplicate of `Deprecated.FactionClock` on vault pages (research R8). `TMPL_deprecated_guidance` stays. |
| XXIII Real surfaces | PASS | Timing and identity parity are measured on the live `wiki/`. Evals compose real wiki content. |
| XXIV Synchronized content systems | PASS | v6.0.1 reads "`wiki lint` Python checks, and Vale with the repo-local `Deprecated` style and the `CoDM` vocabulary". That matches FR-022/FR-023, so the only Vale change is removing `CoDM` from `BasedOnStyles`. |
| XXV Uniform path | PASS | One identity path serves scoped and whole-vault runs. There is one vault/root discovery helper (`tools/wiki_ops/cli.py`). No special cases. |
| XXVI Weakest model | PASS | `luna-eval` defaults are kept. The baseline uses the weakest sufficient model and effort. |
| Spec FR-046 / SC-014 (binding) | PASS | Every new file, subcommand, flag, and data store is justified against an existing module. Deleted and folded paths are listed. Each code change is labelled diagnostic or deterministic, and each judgment names its skill (see Simplify and consolidate). |

**Gate result: PASS.** No violations, so Complexity Tracking is empty.

**Post-design re-check (after Phase 1): PASS.** The data model adds one derived cache file (`identity-index.json`, via `lint_cache.py`). `metrics.json` is not new: it is `skill-creator`'s existing `references/schemas.md` metrics file, now written by `luna-eval`. Neither is a competing source.

## Project Structure

### Documentation (this feature)

```text
specs/030-self-improving-architecture/
├── plan.md              # this file
├── research.md          # Phase 0 decisions
├── data-model.md        # error entry, eval file, run dir, identity index
├── quickstart.md        # validation run guide (V-01…V-12)
├── contracts/
│   ├── wiki-cli.md      # FR-027–FR-039 command surface
│   ├── error-ledger.md  # errors.md format + error-ledger CLI
│   └── eval-run.md      # evals.json schema + luna-eval run/result contract
└── tasks.md             # /speckit.tasks (not created here)
```

### Source Code (repository root): affected files

```text
errors.md                                   # one-off migration to 4-field entries; agent-supplied merge groups/sources (FR-010)
scripts/error-ledger.py                     # new format; exact-match auto-attach; --attach source refusal; detach undo; list reports recurrence + missing sources (FR-006–FR-010, FR-036)
scripts/check-omp-baseline.sh               # memory backend false|"off" passes; enabled/missing fails naming value (FR-020)
.vale.ini                                   # remove CoDM from every BasedOnStyles line; Deprecated + Vocab = CoDM unchanged (FR-022)
tools/creative_lint/vale_adapter.py         # Deprecated.* findings labelled human_repair, no repair_action (FR-023)
tools/wiki_ops/identity.py                  # index-backed candidate selection; resolve_identity/_path_for read the index (FR-024–FR-026)
tools/wiki_ops/lint_cache.py                # load/save identity-index.json with the existing atomic writer (FR-025)
tools/wiki_ops/cli.py                       # the one repo/vault discovery helper (FR-027)
tools/lint_wiki.py                          # absorbs lint-obsidian-markdown + lint-literal-newlines rules; default vault via cli.py (FR-046, XXI)
scripts/wiki                                # only lint front door; per-subcommand help/examples; lint fix subparser; stdin; errors; _tune plain report (FR-030–FR-038)
scripts/wiki-lint                           # engine only: identity.compared; drop TMPL_inherited_deprecated_guidance; vault via cli.py; --help points at `wiki lint`; consolidate_main reports per-draft age + base_confidence, actions stay [] (FR-046 rule 5, SC-014 f)
scripts/manifest.py                         # reports manifest facts only (FR-029)
scripts/luna-eval                           # root via cli.py; evals.json schema check in load; metrics.json; skill_selected grade (FR-012–FR-016)
scripts/hybrid-sdd-check.py                 # new `diff` subcommand: SC-014 (a)/(c) mechanical checks
scripts/check-current-commands              # also checks cited scripts/ and tests/ paths in specs/026 (SC-008)
.agents/skills/skill-creator/SKILL.md       # invoke luna-eval; promotion decision rule lives here (FR-012, FR-044); drop description loop
.agents/skills/skill-creator/references/schemas.md   # evals.json = repo schema; grading/metrics = run contract
.agents/skills/skill-creator/agents/grader.md        # grade assertions[] {type,text}; no rubric score
.agents/skills/skill-creator/scripts/aggregate-benchmark.py   # report per-eval regressions + medians; never decides (FR-044)
.agents/skills/*/evals/evals.json           # 60 files: one schema, skill_name, Work-gate wording fixed, skill_selected evals for the six owners (FR-013–FR-017, SC-005)
.agents/skills/obsidian-markdown/SKILL.md   # line 35: `./scripts/lint-wiki-write` -> `./scripts/wiki lint`
AGENTS.md                                   # "Error ledger" (~196): fix first, exact-match attach, same-cause judgment rule, detach undo; friction rule once (FR-002, FR-006–FR-010)
.agents/skills/wiki-lint/SKILL.md           # line ~47 reconcile first, record only if unresolved; Deprecated.* and identity judgments governed here
.agents/skills/wiki-lint/consolidate.md     # §3 (~line 44–48): drop threshold auto-promotion; agent decides each draft -> reviewed and writes its own lifecycle_reason (SC-014 f)
.agents/skills/wiki-dedup/SKILL.md          # governs ambiguous-identity resolution (FR-024); no code picks a winner
.agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/SKILL.md   # five FR-040 answers; remove deterministic text moved into tools (FR-029, FR-040)
docs/agents/hybrid-sdd.md                   # friction branch of the capability loop (FR-001)
docs/creative-linting.md, docs/architecture.md, README.md   # point lint usage at `wiki lint`; README.md:105 `python3 tools/check_wiki_pages.py` -> `./scripts/wiki lint`
package.json                                # lint:vale -> `./scripts/wiki lint` (run_vale already refreshes the vocab); scripts/vale-vocab deleted (FR-046)
scripts/wiki-reveal                         # frontmatter from tools/lint_wiki.py; tools/check_wiki_pages.py deleted (FR-046)
specs/026-agent-autonomy-scope/{spec,plan,research,data-model,quickstart,tasks}.md, contracts/agent-autonomy.md   # FR-018
specs/029-agent-loop-closure/tasks.md, quickstart.md   # T003…T049 evidence (FR-019)
tests/test_error_ledger_repairs.py, test_creative_lint_cli.py (consolidate drafts report), test_wiki_cli.py, test_wiki_ops.py, test_creative_lint.py, test_policy_conflicts.py, test_luna_eval.py (new)
```

**Structure Decision**: This is a single repository with no new directories. There are two new files, `wiki/_meta/identity-index.json` and `tests/test_luna_eval.py`, and ten deleted scripts. The full ledger is in "Simplify and consolidate".

## Design by phase

### Phase 1: coherent baseline (US1–US4)

- **OMP (FR-020/021)**: parse the `memory:` block's `backend:` value. `false`, `"false"`, `off`, and `"off"` count as disabled. Any other value fails with `memory enabled: backend=<value>`. A missing block fails with `memory key missing`. The test goes in `tests/test_policy_conflicts.py` and runs the script against a temp copy of the repo files with each config.
- **Vale (FR-022/023)**: `BasedOnStyles = CoDM, Deprecated, …` becomes `BasedOnStyles = Deprecated, …` in all 6 sections. That includes region, creature, and npc, where only `Deprecated` remains. `styles/Deprecated/*.yml`, `Vocab = CoDM`, and `tools/creative_lint/vale_vocab.py` do not change. No `VALE_Deprecated` test changes. Drain e-212, e-214, e-215, e-216, e-218 in the same commit. In `vale_adapter.py`, repo-local (`is_custom`) findings such as `Deprecated.DMThesis` change from `deterministic_repair` + `delete_section` action to `human_repair` with no `repair_action`, so `wiki lint fix` never applies them. `wiki-lint` governs the removal or relocation (FR-023). Test in `test_creative_lint.py`.
- **One linter (XXI, FR-046)**: fold the rules of `scripts/lint-obsidian-markdown` into `tools/lint_wiki.py` findings: `md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, and `forbidden_tree`. Its `missing_frontmatter` already exists in `lint_wiki.py`. Fold `scripts/lint-literal-newlines` in as `literal_newline`, scoped to session pages and Session templates as today. Delete both scripts and `scripts/lint-wiki-write`, whose `wiki-lint file` step exits 2 today (research R8). `table_wikilink_unescaped_pipe` has one correct output (`|` → `\|` inside a table-cell wikilink), so it is `deterministic_repair`. The rest are `human_repair`. Remove `TMPL_inherited_deprecated_guidance` from `scripts/wiki-lint` and keep `TMPL_deprecated_guidance`.
- **Consolidate promotion (FR-046 rule 5, SC-014 f)**: verified 2026-09-24 at 27039b9d. The threshold promotion lives only in `.agents/skills/wiki-lint/consolidate.md` §3 ("Automatic state-machine enforcement (no human judgment required)": `draft` → `reviewed` when `created` > 30d and `base_confidence > 0.7`, with a fixed `lifecycle_reason`). `scripts/wiki-lint` `consolidate_main` promotes nothing in code: its plan has `actions: []` and a comment that structural findings cannot justify judgment repairs. `consolidate_main` gains a `drafts` list in its existing plan output, one row per `lifecycle: draft` page: `{page, created, age_days, base_confidence}`, sorted by page, read with `tools.lint_wiki.frontmatter`. `age_days` is today minus `created`, and a missing or unparseable value is `null`. It is a report only, so `actions` stays `[]` and has no promotion kind, and `--approve` still applies nothing. §3 is rewritten: the agent reads `drafts`, reads each page, decides whether to promote under `wiki-lint`, and writes its own `lifecycle_reason` naming the evidence. Age and confidence are facts, not thresholds. The stale-`verified` callout and "`reviewed → verified` is human-only" stay. No new file. Test: extend `test_consolidation_is_dry_run_until_approved` in `tests/test_creative_lint_cli.py` with a scratch vault holding one draft page. Today 0 of the 876 live pages with a `lifecycle` are `draft` (822 are `proposed`), so the rule has no current effect.
- **026 references (FR-018)**: rewrite each of the 66 references to the current enforcing surface. That is `luna-eval` evals for agent behavior and `wiki lint` for wiki structure. A reference with no current surface is removed with a one-line "replaced by" note. `scripts/check-current-commands` gains `scripts/…`/`tests/…` path citations and `specs/026-agent-autonomy-scope/` in its scan roots. A `test_policy_conflicts.py` case runs it and also fails on `AGENT00[1-3]` in those docs (SC-008).
- **Work-gate wording (SC-003)**: a `tests/test_luna_eval.py` case fails when any assertion `text` contains the retired terms `Work gate`, `chat proposal`, or `approval before write`, matched case-insensitively. Records that test current behavior phrase it positively ("writes without asking first"), per spec Edge Cases.
- **Evaluator (FR-012–FR-017)**: see [contracts/eval-run.md](contracts/eval-run.md). `luna-eval` stays the only runner. It gains the shared root discovery, an `evals.json` schema check inside `load_eval` (it validates the whole file and exits 2 naming each bad record before any subject run; chosen over `quick-validate.py` because FR-046 names `luna-eval` the eval owner, while `quick-validate.py` validates `SKILL.md` for packaging), a deterministic `metrics.json` built from `events.jsonl`, and a deterministic `skill_selected` grade: the first owner `SKILL.md` the subject reads. `grader.md` grades the other assertion types into `grading.json`, which keeps the viewer's `text`/`passed`/`evidence` fields and adds `type`. The corpus conversion is scripted once and not kept (VIII does not apply to one-offs): each `expectations[]` string becomes `{type: "behavior", text}`, the drift types become `qualitative→quality` and `structural→structure`, and `skill_name` is added to the 7 files missing it. The Work-gate, approval, read-mutation, and retired-path wording in 13 files is edited by hand per record, because the assertion stays and only its behavior is updated (spec Edge Cases).
- **029 baseline (FR-019)**: run the nine categories (at least 10 cases) through `luna-eval` at its default model and effort. Each run's `metrics.json` records both, and SC-012 comparisons reuse the same pair. Record them in `specs/029-agent-loop-closure/quickstart.md`, closing T003…T049. The from-scratch `wiki health` wall time is recorded beside them (SC-007, V-08c).
- **Identity (FR-024–FR-026)**: see research R4 and data-model §4. The index is loaded and saved through `lint_cache.py`, and `resolve_identity` (mutation gate) and `_path_for` read it too. `scripts/wiki-identity` is deleted, because its only callers are 3 tests and the `wiki lint` result already carries the `identity` block. Thresholds (> 0.6 prefilter, > 0.7 shared-source stem ratio) only list candidates and gate mutations as `ambiguous`. Choosing the canonical page is the agent's call under `wiki-dedup` and `wiki-lint`. Rows for unchanged pages come from the index keyed by `content_sha256`, so only changed pages are read and profiled. Candidates for a selected page are pages of the same `type` that share an exact cheap signal (norm title, alias, stem, manifest provenance with stem ratio > 0.7, merge transition), plus pages that pass the existing character-profile prefilter (> 0.6), as FR-024 now states. That prefilter is computed from cached profiles. `SequenceMatcher` runs only on those candidates, and each pair ratio is cached by the two content hashes, so a warm whole-vault or health run recomputes only pairs that touch changed pages. `wiki-lint` reports `identity: {scanned, compared, index: {hits, misses}}`. Whole-vault output is unchanged, because the candidate rule is the current rule evaluated from cached data.

### Phase 2: close the loop (US5–US7)

- **Friction rule (FR-001/002/005)**: add one paragraph to `AGENTS.md` next to the capability loop: act → friction → identify cause → fix source → verify → continue. `docs/agents/hybrid-sdd.md` gains the branch. Skills link to it rather than restating it.
- **Ledger (FR-006–FR-010)**: see [contracts/error-ledger.md](contracts/error-ledger.md). `append` needs `--source` (it must be an existing repo path or `external:<name>`, which is a deterministic check). It auto-attaches only when an open entry has the same `source` and identical whitespace-trimmed `cause`, and reports the matched id and occurrence index. `--attach e-N` is the agent's same-root-cause call and is refused across sources. `detach --id e-N --index k` is the one documented undo. `drain --id` removes the entry. `list` returns `{entries, recurrence, missing_sources}`, and `scripts/wiki`'s two `error list` callers read `entries`. Migration is a one-off, uncommitted conversion (same precedent as the eval conversion). Its merge groups and sources are agent-authored input data, recorded in research R3, and no group ids are hardcoded in `error-ledger.py`. Rewrite `AGENTS.md` "Error ledger" (~196) with the same-cause rule, and `wiki-lint/SKILL.md` line ~47.
- **Regression per fix (FR-011)**: the owning skill's eval or a `tests/` case, landed in the same change as the fix.
- **CLI (FR-027–FR-039)**: see [contracts/wiki-cli.md](contracts/wiki-cli.md). Discovery is the one `tools/wiki_ops/cli.py` helper (repo root from the package location; vault order `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` > `~/.obsidian-wiki/config`). `scripts/wiki-lint`, `tools/lint_wiki.py`, `scripts/luna-eval`, and `scripts/error-ledger.py` call it instead of computing cwd-relative or `git rev-parse` roots. Lint help and discovery live only in `scripts/wiki`. `scripts/wiki-lint` stays the engine that `wiki` calls, and its `--help` names `wiki lint --help`. `_tune`'s "Fix that checker this sitting." becomes a plain report (`wiki lint: slowest checker <script> <ms> ms; next <script> <ms> ms`). `wiki health` reports facts, and `next` is chosen by a fixed documented rule (data in contracts/wiki-cli.md), not a recommendation. SC-010 is checked from the cold-agent `luna-eval` runs: each run's `metrics.json` `invocation_errors` must be 0 (data-model §3), and each mutating command's second run must report `already_done`.

### Phase 3: optimize (US8–US9)

- **Promotion (FR-041–FR-044)**: incumbent = the skill file at HEAD, snapshotted with `luna-eval --subject-skill <snapshot> --config old_skill`. Candidate = the working-tree edit. Each config gets one run on the same eval ids, with the same `model`/`effort` as the FR-019 baseline. `aggregate-benchmark.py` reports, per eval, task-outcome regressions and incumbent-pass → candidate-fail assertions, plus the medians of tool calls, retries, tokens, and latency. It never promotes or refuses. The agent decides keep or refuse following the promotion rule written in `skill-creator/SKILL.md` (FR-044, SC-012). No new script.
- **Small skills (FR-029, FR-040, SC-013)**: for each of the six named owners, move only deterministic procedure (repair bookkeeping, manifest facts, path discovery, health facts) into `wiki lint fix`, `scripts/manifest.py`, and `wiki health`. Keep every judgment in the skill, then delete the moved text and rerun its evals.

## Simplify and consolidate (FR-046, SC-014)

### New files, subcommands, flags, and data (SC-014 a)

| New item | Extends / replaces | Why the existing one cannot simply be improved | Kind (rule 5) |
|---|---|---|---|
| `wiki/_meta/identity-index.json` | `wiki/_meta/lint-cache.json`, via `tools/wiki_ops/lint_cache.py` (same load/save/atomic write) | Lint-cache entries are invalidated by the rules digest. Identity rows must survive a rules change for SC-007's < 50 s bound, and they cover every page, not only linted ones. The spec names the file (FR-028). | derived index |
| `tests/test_luna_eval.py` | the `tests/` suite | `scripts/luna-eval` has no test file. Putting its tests (schema check, `metrics.json`, `skill_selected`, `invocation_errors`, Work-gate wording) in another module's file would split ownership. | test |
| `error detach --id e-N --index k` | `scripts/error-ledger.py` | FR-007 requires one documented undo for an attach. `drain` removes the whole entry, so it cannot serve. | deterministic fix |
| `error append --source`, `--attach`, `--detail`, `--dry-run`; `error list --ids-only` | `scripts/error-ledger.py` | FR-006/FR-007/FR-033/FR-037 fields and flags on the existing subcommands | deterministic |
| `hybrid-sdd-check.py diff --plan <plan.md> --base <ref>` | `scripts/hybrid-sdd-check.py` (existing deterministic SDD checker) | SC-014 (a)/(c) are mechanical: added files missing from this table, and deleted paths still referenced in maintained surfaces. There is no other checker for plan-vs-diff. | diagnostic |
| `wiki lint fix` subparser; `--stdin`, `--paths-only`, `--dry-run` | `scripts/wiki` (replaces the positional `fix` token) | FR-033/FR-034/FR-037 | deterministic |
| `metrics.json` in the run dir | `skill-creator/references/schemas.md` metrics file, now written by `luna-eval` | Not a new format. `luna-eval` fills the existing schema plus `retries`, `invocation_errors`, `model`, `effort`. | diagnostic |
| `grading.json` fields `type`, `task_outcome`, `semantic_quality` | existing `grading.json` | FR-016 metrics. `semantic_quality` is the pass rate of `quality` assertions. | diagnostic |
| `wiki-lint --json` `identity.compared`, `identity.index` | existing `identity` block | SC-007 compared count | diagnostic |
| `wiki-lint --consolidate` plan field `drafts` (`page`, `created`, `age_days`, `base_confidence`) | existing `consolidate_main` plan output in `scripts/wiki-lint` | SC-014 (f) requires the output to report each draft's age and `base_confidence`. It adds a field to the existing plan, not a command. | diagnostic |
| `tools/lint_wiki.py` findings `md_internal_link`, `title_only_frontmatter`, `dc_in_narration`, `broken_image_link`, `table_wikilink_unescaped_pipe`, `forbidden_tree`, `literal_newline` | moved from the deleted `lint-obsidian-markdown` / `lint-literal-newlines` | One linter (XXI). The checks are unique today (research R8). | diagnostic; only the table pipe escape is deterministic |

No new module, skill, config key, or command.

### Deleted or folded (SC-014 c)

| Path | Evidence (research R8) | Replacement |
|---|---|---|
| `scripts/wiki-identity` | Callers: `tests/test_wiki_ops.py` (3) and specs/025 only | `wiki lint` `identity` block; tests call `scan_identities`/`resolve_identity` or `wiki lint` |
| `scripts/lint-wiki-write` | Its `wiki-lint file` step exits 2 (usage error, observed 2026-09-24). Callers: `obsidian-markdown/SKILL.md:35`, `tests/test_error_ledger_repairs.py:46` | `wiki lint` |
| `scripts/lint-obsidian-markdown` | Unique rules; 540 live findings invisible to `wiki lint` (519 table pipes, 21 broken images) | rules in `tools/lint_wiki.py` |
| `scripts/lint-literal-newlines` | Unique rule; 0 current findings over 41 session files | `literal_newline` in `tools/lint_wiki.py` |
| `skill-creator/scripts/run-eval.py`, `run-loop.py`, `improve-description.py` | Second runner (e-210). Referenced only by each other and `skill-creator/SKILL.md` (1 line) | `luna-eval` + `skill_selected` evals |
| `skill-creator/scripts/generate-report.py` | Only consumes `run-loop.py` output (its own docstring) | none (dead with `run-loop.py`) |
| `TMPL_inherited_deprecated_guidance` (`scripts/wiki-lint`) | Same faction/agenda-clock regex over the same vault pages as Vale `Deprecated.FactionClock` | Vale `Deprecated.FactionClock` |
| `scripts/vale-vocab` | Only caller `package.json` `lint:vale`. It calls `refresh_vocab`, which `vale_adapter.run_vale` already calls before every Vale run (`wiki lint` → `wiki-lint` → creative engine). The current `lint:vale` fails anyway (bare `vale --config=.vale.ini` exits 2, E100) | `lint:vale` → `./scripts/wiki lint` |
| `tools/check_wiki_pages.py` | Outdated `TYPES`/`LIFECYCLES` duplicate `lint_wiki.py` `REQUIRED`/`CAMPAIGN_REQUIRED`, `bad_type`, `bad_lifecycle`; manifest checks duplicate `lint_wiki` provenance and `scripts/manifest.py`. Callers: `scripts/wiki-reveal:29` (`frontmatter` only), `README.md:105` | `tools.lint_wiki.frontmatter` in `wiki-reveal` (skip when block is None); `./scripts/wiki lint` in README |
| Threshold auto-promotion in `.agents/skills/wiki-lint/consolidate.md` §3 (`draft` → `reviewed` at `created` > 30d and `base_confidence > 0.7`, "no human judgment required") | A judgment encoded as a rule (FR-046 rule 5). It is an instruction only: `consolidate_main` emits `actions: []` (research R8) | agent decision per draft under `wiki-lint`, using the `drafts` report |
| `wiki-lint` `consolidate_main` cwd vault resolution, `tools/lint_wiki.py` cwd default, `luna-eval` `git rev-parse` root | Three ad hoc root/vault lookups | `tools/wiki_ops/cli.py` helper |
| `_tune` directive text; `error recurrence`; `error migrate`; `tests/test_omp_baseline.py`; `--cause-fixed` | Earlier plan items, now superseded | `_tune` plain report; `error list` field; one-off uncommitted migration; `test_policy_conflicts.py`; removed |

Net result: 2 files added, 10 deleted, and 3 ad hoc discovery paths merged into 1.

### Judgments and their governing skill (SC-014 e)

| Judgment | Code reports | Governing skill |
|---|---|---|
| Which page wins an ambiguous identity | candidates, signals, ratios; mutation gate `ambiguous` | `wiki-dedup`, `wiki-lint` |
| Whether a differently worded cause is the same root cause (`--attach`) | exact-match attach and the matched id | `AGENTS.md` "Error ledger" (FR-007; no skill exists) |
| Keep or refuse a candidate instruction | per-eval regressions and medians | `skill-creator` |
| Removing or relocating `Deprecated.*` content; broken image targets; markdown→wikilink rewrites | `human_repair` findings | `wiki-lint` |
| Whether to promote a `draft` page to `reviewed`, and its `lifecycle_reason` | per-draft `age_days` and `base_confidence` (`wiki-lint --consolidate`) | `wiki-lint` (`consolidate.md` §3) |
| What to work on next after `wiki health` | facts and targets ranked by a fixed rule | `wiki-lint` or the owning skill |
| Merge groups and `source` values for the one-off ledger migration | old entries | `AGENTS.md` "Error ledger" |

## Risks and dependencies

- **XIII dependency**: met by v6.0.0/v6.0.1. US5/US6 can land in Phase 2.
- **Folded lint rules raise the backlog**: `wiki lint` will report the 540 existing obsidian-markdown findings. The 519 table pipes are fixed by `wiki lint fix` (deterministic). The 21 broken images are agent work under `wiki-lint` (spec gap 2, round 3: plan default kept).
- **Identity parity**: FR-025/FR-026 require identical findings. Parity is proven by diffing `scan_identities` output cold vs index-warm on the live vault (quickstart V-06).
- **Where the time goes**: for one page, `lint_wiki.py` is the largest cost (1.66 s of 3.44 s; identity 0.84 s), and SC-007's 5 s is already met with Vale. For a cold whole-vault or health run, identity dominates (55.1 s of 82.3 s), from pairwise ratios. The pair cache targets that. The creative engine (15.7 s) and Vale (13.1 s) stay unchanged unless V-08b shows the 50 s bound is missed.
- **Box setup**: the repo has no committed venv. Timing needs `uv venv .venv && uv pip install tiktoken PyYAML vale==3.21.0.0` (as done 2026-09-24), with `.venv/bin` on `PATH` and `OBSIDIAN_VAULT_PATH` set to the clone's `wiki/`, because `~/.obsidian-wiki/config` points at `/home/box/agentic-co-dm/wiki`. The single discovery helper (repo `wiki/` before the global config) fixes that trap.

## Measurements taken (2026-09-24, /workspace clone @ bf021f03, 8-core Linux box)

Setup: `.venv` with `tiktoken`, `PyYAML`, and `vale==3.21.0.0` (Vale 3.21.0). `OBSIDIAN_VAULT_PATH=/workspace/agentic-co-dm/wiki`. `CoDM` removed from `.vale.ini` in the working tree for the run only; the change was not committed.

| Run | Wall | Breakdown |
|---|---|---|
| `scripts/wiki lint entities/place/Belumara.md` (cache miss, Vale on) | 3.72 s (reported `duration_ms` 3619) | — |
| same page, rerun (cache hit) | 0.28 s | — |
| `scripts/wiki-lint --json wiki --scope files:entities/place/Belumara.md` | 3.44 s | lint_wiki 1662 ms, creative engine 772 ms, identity 843 ms, vale 584 ms, vale_vocab 88 ms |
| `scripts/wiki health` (whole vault, rules digest changed: 836/837 cache misses) | 82.3 s, exit 0, no timeout | identity 55.1 s, creative engine 15.7 s, vale 13.1 s, lint_wiki 1.9 s |

Before the fix, Vale with the unmodified `.vale.ini` fails with `E100 … style 'CoDM' does not exist on StylesPath`, reproducing e-212 and related entries.

## Spec gaps for Clarify (resolved by cae8bb44)

1. **FR-024 vs FR-026 (identity candidates)**: resolved. FR-024 now includes cached character-profile prefilter passes (> 0.6) as candidates, and SC-007's compared count includes them. The plan already did this.
2. **FR-007 "same cause"**: resolved, then tightened by b14ea71b to the same `source` plus identical trimmed `cause`; anything broader is the agent's `--attach` call. A forced attach cannot cross sources (contracts/error-ledger.md).
3. **FR-013 `expected_output`**: resolved. It is optional.
4. **Assertion types**: resolved. FR-014 fixes the vocabulary, keeps `scope`/`handoff`/`coverage`, and folds `qualitative`/`structural`.
5. **SC-009 20-sitting window**: resolved. It stays an assumption.
6. **Lint writes tracked files**: resolved. FR-028 keeps `lint-cache.json`, `identity-index.json`, and `accept.txt` tracked as bookkeeping. FR-017 scopes read-side mutation to canonical pages, manifests, indexes, and logs.

## Spec gaps for Clarify (round 3, from b14ea71b; answered by Clarify and 27039b9d)

1. **SC-014 (c) scope**: resolved by Clarify, plan default kept. Only maintained surfaces count (`AGENTS.md`, `docs/`, `.agents/`, `scripts/`, `tools/`, `tests/`, `package.json`, `README.md`). Completed feature specs (e.g. `specs/025-*` citing `scripts/wiki-identity`, `specs/024-*` citing the lint scripts) stay as records. 026 is the exception under FR-018.
2. **Folded lint findings**: resolved by Clarify, plan default kept. The 519 table pipes are fixed by `wiki lint fix`. The 21 broken image links are `human_repair` agent work under `wiki-lint`, not deterministic code.
3. **FR-010 "on first run of the new format"**: resolved by Clarify, plan default kept. The migration runs once as an uncommitted, agent-driven conversion with agent-supplied groups and sources (research R3). It is not a committed command.
4. **Consolidate promotion**: resolved by 27039b9d (Nick brought it into scope; FR-046 rule 5, SC-014 f). The plan changed. The threshold rule in `.agents/skills/wiki-lint/consolidate.md` §3 is removed, and the agent decides each promotion and writes its own `lifecycle_reason`. `consolidate_main` already promotes nothing in code and now also reports each draft's `age_days` and `base_confidence` (Phase 1 "Consolidate promotion", research R8, quickstart V-04e).
5. **Former rejected duplicates**: resolved by Clarify, and the plan changed. Both are folded under FR-046 rule 2. `scripts/vale-vocab` is deleted and `package.json` `lint:vale` runs `./scripts/wiki lint`. `tools/check_wiki_pages.py` is deleted, `scripts/wiki-reveal` reads frontmatter through `tools/lint_wiki.py`, and `README.md:105` cites `./scripts/wiki lint` (research R8, quickstart V-04d).
