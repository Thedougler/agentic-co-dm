# Implementation Plan: Self-Improving Architecture

**Branch**: `030-self-improving-architecture` | **Date**: 2026-09-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/030-self-improving-architecture/spec.md` (Clarifications, Session 2026-09-24, all five confirmed by Nick).

## Summary

Collapse, don't add. Every change edits an existing file: `scripts/error-ledger.py` + `errors.md`, `scripts/check-omp-baseline.sh`, `.vale.ini`, `tools/wiki_ops/identity.py` (+ one derived cache file), `tools/wiki_ops/cli.py` + `scripts/wiki`, `scripts/luna-eval`, the `skill-creator` skill, the 60 `evals/evals.json` files, `AGENTS.md`, `.agents/skills/wiki-lint/SKILL.md`, and the feature 026/029 documents. No new command, skill, workflow, or runtime.

The data shapes come first. Each one is defined in [data-model.md](data-model.md):

1. **Error entry**: `{id, cause, source, evidence:[{sitting, detail}]}`. Only open entries exist. Recurrence = occurrences after the first.
2. **Eval file**: `{skill_name, evals:[{id, prompt, files?, context?, outputs?, subject_skill?, core?, expected_output, assertions:[{type, text}]}]}`. `skill_selected` and `behavior` are added to the type vocabulary.
3. **Eval run directory** (one result format): the existing `luna-eval` layout plus `metrics.json`, which `luna-eval` derives from `events.jsonl`, plus `grading.json` in the shape the `skill-creator` viewer already reads.
4. **Identity index**: `wiki/_meta/identity-index.json`, one cheap row per page keyed by content hash. It lets a scoped lint stop reading and profiling the whole vault.

Phase order is binding (spec Assumptions): Phase 1 = US1–US4, Phase 2 = US5–US7, Phase 3 = US8–US9.

## Technical Context

**Language/Version**: Python 3.12+ (the box venv runs 3.14); Bash for `scripts/check-omp-baseline.sh`

**Primary Dependencies**: stdlib only for new logic. Project-declared: `PyYAML`, `tiktoken`, `vale==3.21.0.0` (PyPI wrapper that installs the Vale binary), dev `pytest`. Vale packages ai-tells, proselint, write-good, and Readability, plus repo-local `styles/Deprecated/`. `codex` CLI (used by `scripts/luna-eval`).

**Storage**: Files. `errors.md` (JSON lines under a heading), `sittings.jsonl`, `.agents/skills/*/evals/evals.json`, eval run dirs under `<skill>-workspace/iteration-N/`, `wiki/_meta/lint-cache.json` (existing), and `wiki/_meta/identity-index.json` (new derived cache, same lifecycle as the lint cache).

**Testing**: `pytest` under `tests/`. The existing files are `test_error_ledger_repairs.py`, `test_wiki_cli.py`, and `test_wiki_ops.py`; new regression tests go in them or in one new `tests/test_omp_baseline.py`. Behavioral evidence runs through `scripts/luna-eval` (constitution IV, XXIII, XXVI).

**Target Platform**: Linux box and the maintainer workstation (macOS). Both run the same CLI.

**Project Type**: Agent-facing CLI tooling plus agent instructions (single repo, no service)

**Performance Goals**: SC-007. Scoped lint of one changed page (cache miss, Vale on) under 5 s. Unchanged page served from the lint cache. `wiki health` finishes without a harness timeout, and its wall time is recorded.

**Constraints**: Findings stay the same (FR-025/FR-026): cached = cold, and the whole-vault run is unchanged. Commands take no prompts (FR-030). Mutations are idempotent and support `--dry-run` (FR-036/FR-037). The feature 027 result contract stays: agent-shaped default output, `--pretty`, no fuzzy paths.

**Scale/Scope**: About 1,640 non-raw wiki pages. 60 eval files with 533 records (143 use `expectations[]`; 7 have no `skill_name`). 32 `errors.md` lines. 13 eval files carry Work-gate wording. 7 feature 026 docs cite absent executables (66 references).

No NEEDS CLARIFICATION remains. The open design choices are settled in [research.md](research.md). The real spec gaps are listed at the end of this plan.

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
| XIV Simplest tool | PASS | Stdlib JSON caches and argparse. No new dependency. Declared deps get installed when missing. |
| XVI Layering | PASS | The friction rule is stated once in `AGENTS.md` (FR-002). Skills link to it and do not restate it. |
| XIX Corrections | PASS | `AGENTS.md` line 196 and `wiki-lint/SKILL.md` line 47 are rewritten to "fix and verify; record only if unresolved". |
| XXI One linter | PASS | Rules are not weakened. Removing the missing `CoDM` style drops no check, because the style never loaded. `Deprecated` stays. |
| XXIII Real surfaces | PASS | Timing and identity parity are measured on the live `wiki/`. Evals compose real wiki content. |
| XXIV Synchronized content systems | PASS | v6.0.1 reads "`wiki lint` Python checks, and Vale with the repo-local `Deprecated` style and the `CoDM` vocabulary". That matches FR-022/FR-023, so the only Vale change is removing `CoDM` from `BasedOnStyles`. |
| XXV Uniform path | PASS | One identity path serves scoped and whole-vault runs. No special cases. |
| XXVI Weakest model | PASS | `luna-eval` defaults are kept. The baseline uses the weakest sufficient model and effort. |

**Gate result: PASS.** No violations, so Complexity Tracking is empty.

**Post-design re-check (after Phase 1): PASS.** The data model adds one derived cache file and one derived per-run file (`metrics.json`). Neither is a competing source.

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
errors.md                                   # migrate to 4-field entries; merge dups; drop drained (FR-010)
scripts/error-ledger.py                     # new format, append-or-attach, drain-by-fix, recurrence (FR-006–FR-010, FR-036)
scripts/check-omp-baseline.sh               # memory backend false|"off" passes; enabled/missing fails naming value (FR-020)
.vale.ini                                   # remove CoDM from every BasedOnStyles line; Deprecated + Vocab = CoDM unchanged (FR-022)
tools/wiki_ops/identity.py                  # identity index + candidate selection (FR-024–FR-026)
tools/wiki_ops/cli.py                       # vault discovery order (FR-027)
scripts/wiki                                # per-subcommand help/examples, `lint fix` subparser, stdin lists, errors (FR-030–FR-038)
scripts/wiki-lint                           # report identity.compared; pass through index (SC-007)
scripts/manifest.py                         # absorbs manifest reasoning named in trajectories (FR-029)
scripts/luna-eval                           # repo-root discovery, metrics.json from events.jsonl, skill_selected grading (FR-012, FR-014, FR-016)
.agents/skills/skill-creator/SKILL.md       # invoke luna-eval; drop run-eval/run-loop description loop (FR-012, FR-015)
.agents/skills/skill-creator/references/schemas.md   # evals.json = repo schema; grading/metrics = run contract
.agents/skills/skill-creator/scripts/run-eval.py, run-loop.py, improve-description.py   # removed (FR-012, FR-015)
.agents/skills/skill-creator/agents/grader.md        # grade assertions[] {type,text}; skill_selected from events
.agents/skills/*/evals/evals.json           # 60 files: one schema, skill_name, Work-gate wording fixed, skill_selected evals (FR-013–FR-017, SC-005)
AGENTS.md                                   # line ~196 "Error ledger" + friction rule once (FR-002, FR-006–FR-010); SPECKIT block → this plan
.agents/skills/wiki-lint/SKILL.md           # line ~47 "record the mismatch in errors.md" → reconcile first, record only if unresolved
.agents/skills/{place-design,faction-design,session-beats,run-guide,wiki-query,wiki-lint}/SKILL.md   # five FR-040 answers; remove text moved into tools (FR-029, FR-040)
docs/agents/hybrid-sdd.md                   # friction branch of the capability loop (FR-001)
specs/026-agent-autonomy-scope/{spec,plan,research,data-model,quickstart,tasks}.md, contracts/agent-autonomy.md   # FR-018
specs/029-agent-loop-closure/tasks.md, quickstart.md   # T003…T049 evidence (FR-019)
tests/test_error_ledger_repairs.py, tests/test_wiki_cli.py, tests/test_wiki_ops.py, tests/test_omp_baseline.py (new)
```

**Structure Decision**: This is a single repository with no new directories. The only new file is the derived `wiki/_meta/identity-index.json`, which sits beside `lint-cache.json`, plus possibly `tests/test_omp_baseline.py` if no existing test file fits.

## Design by phase

### Phase 1: coherent baseline (US1–US4)

- **OMP (FR-020/021)**: parse the `memory:` block's `backend:` value. `false`, `"false"`, `off`, and `"off"` count as disabled. Any other value fails with `memory enabled: backend=<value>`. A missing block fails with `memory key missing`. The test runs the script against a temp copy of the repo files with each config.
- **Vale (FR-022/023)**: `BasedOnStyles = CoDM, Deprecated, …` becomes `BasedOnStyles = Deprecated, …` in all 6 sections. That includes region, creature, and npc, where only `Deprecated` remains. `styles/Deprecated/*.yml`, `Vocab = CoDM`, and `tools/creative_lint/vale_vocab.py` do not change. No `VALE_Deprecated` test changes. Drain e-212, e-214, e-215, e-216, e-218 in the same commit.
- **026 references (FR-018)**: rewrite each of the 66 references to the current enforcing surface. That is `luna-eval` evals for agent behavior and `wiki lint` for wiki structure. A reference with no current surface is removed with a one-line "replaced by" note.
- **Evaluator (FR-012–FR-017)**: see [contracts/eval-run.md](contracts/eval-run.md). `luna-eval` stays the only runner. It gains repo-root discovery, a deterministic `metrics.json` built from `events.jsonl`, and a deterministic `skill_selected` grade: the first owner `SKILL.md` the subject reads. `grader.md` grades the other assertion types into `grading.json`, which keeps the viewer's `text`/`passed`/`evidence` fields and adds `type`. The corpus conversion is scripted once and not kept (VIII does not apply to one-offs): each `expectations[]` string becomes `{type: "behavior", text}`, the drift types become `qualitative→quality` and `structural→structure`, and `skill_name` is added to the 7 files missing it. The Work-gate, approval, read-mutation, and retired-path wording in 13 files is edited by hand per record, because the assertion stays and only its behavior is updated (spec Edge Cases).
- **029 baseline (FR-019)**: run the nine categories (at least 10 cases) through `luna-eval` and record them in `specs/029-agent-loop-closure/quickstart.md`, closing T003…T049. `wiki health` wall time is recorded beside them (SC-007).
- **Identity (FR-024–FR-026)**: see research R4 and data-model §4. Rows for unchanged pages come from the index keyed by `content_sha256`, so only changed pages are read and profiled. Candidates for a selected page are pages of the same `type` that share an exact cheap signal (norm title, alias, stem, manifest provenance with stem ratio > 0.7, merge transition), plus pages that pass the existing character-profile prefilter. That prefilter is computed from cached profiles. `SequenceMatcher` runs only on those candidates, and each pair ratio is cached by the two content hashes, so a warm whole-vault or health run recomputes only pairs that touch changed pages. `wiki-lint` reports `identity: {scanned, compared, index: {hits, misses}}`. Whole-vault output is unchanged, because the candidate rule is the current rule evaluated from cached data.

### Phase 2: close the loop (US5–US7)

- **Friction rule (FR-001/002/005)**: add one paragraph to `AGENTS.md` next to the capability loop: act → friction → identify cause → fix source → verify → continue. `docs/agents/hybrid-sdd.md` gains the branch. Skills link to it rather than restating it.
- **Ledger (FR-006–FR-010)**: see [contracts/error-ledger.md](contracts/error-ledger.md). `append` needs `--source`. It attaches an occurrence when an open entry has the same `source` and the same normalized cause key, and otherwise creates an entry. `drain --id` removes the entry. `recurrence` reports the total and per-sitting counts. `migrate` runs once and is idempotent. Rewrite `AGENTS.md` line ~196 and `wiki-lint/SKILL.md` line ~47.
- **Regression per fix (FR-011)**: the owning skill's eval or a `tests/` case, landed in the same change as the fix.
- **CLI (FR-027–FR-039)**: see [contracts/wiki-cli.md](contracts/wiki-cli.md). SC-010 is checked from the cold-agent `luna-eval` runs: each run's `metrics.json` `invocation_errors` must be 0 (data-model §3), and each mutating command's second run must report `already_done`.

### Phase 3: optimize (US8–US9)

- **Promotion (FR-041–FR-044)**: incumbent = the skill file at HEAD, snapshotted with `luna-eval --subject-skill <snapshot> --config old_skill`. Candidate = the working-tree edit. Both run on the same eval ids and are compared with the existing `aggregate-benchmark.py` on `metrics.json` + `grading.json`. The rule, in order: success, then quality, then tool calls, retries, tokens, latency, scope. The candidate is kept only if it is non-inferior on both success and quality. No new script.
- **Small skills (FR-029, FR-040, SC-013)**: for each of the six named owners, move procedure into `wiki lint fix`, `scripts/manifest.py`, and `wiki health` `next`, then delete that skill text and rerun its evals.

## Risks and dependencies

- **XIII dependency**: met by v6.0.0/v6.0.1. US5/US6 can land in Phase 2.
- **Identity parity**: FR-025/FR-026 require identical findings. Parity is proven by diffing `scan_identities` output cold vs index-warm on the live vault (quickstart V-06).
- **Where the time goes**: for one page, `lint_wiki.py` is the largest cost (1.66 s of 3.44 s; identity 0.84 s), and SC-007's 5 s is already met with Vale. For a cold whole-vault or health run, identity dominates (55.1 s of 82.3 s), from pairwise ratios. The pair cache targets that. The creative engine (15.7 s) and Vale (13.1 s) are out of this feature's scope unless the health baseline shows a harness timeout.
- **Box setup**: the repo has no committed venv. Timing needs `uv venv .venv && uv pip install tiktoken PyYAML vale==3.21.0.0` (as done 2026-09-24), with `.venv/bin` on `PATH` and `OBSIDIAN_VAULT_PATH` set to the clone's `wiki/`, because `~/.obsidian-wiki/config` points at `/home/box/agentic-co-dm/wiki`. FR-027's discovery order fixes that trap.

## Measurements taken (2026-09-24, /workspace clone @ bf021f03, 8-core Linux box)

Setup: `.venv` with `tiktoken`, `PyYAML`, and `vale==3.21.0.0` (Vale 3.21.0). `OBSIDIAN_VAULT_PATH=/workspace/agentic-co-dm/wiki`. `CoDM` removed from `.vale.ini` in the working tree for the run only; the change was not committed.

| Run | Wall | Breakdown |
|---|---|---|
| `scripts/wiki lint entities/place/Belumara.md` (cache miss, Vale on) | 3.72 s (reported `duration_ms` 3619) | — |
| same page, rerun (cache hit) | 0.28 s | — |
| `scripts/wiki-lint --json wiki --scope files:entities/place/Belumara.md` | 3.44 s | lint_wiki 1662 ms, creative engine 772 ms, identity 843 ms, vale 584 ms, vale_vocab 88 ms |
| `scripts/wiki health` (whole vault, rules digest changed: 836/837 cache misses) | 82.3 s, exit 0, no timeout | identity 55.1 s, creative engine 15.7 s, vale 13.1 s, lint_wiki 1.9 s |

Before the fix, Vale with the unmodified `.vale.ini` fails with `E100 … style 'CoDM' does not exist on StylesPath`, reproducing e-212 and related entries.

## Spec gaps for Clarify

1. **FR-024 vs FR-026 (identity candidates)**: FR-024 lists only slug, title, aliases, and manifest identity as cheap signals. Today, content similarity > 0.6 alone makes a candidate. Restricting comparison to the literal list would drop content-only duplicates and change findings, which violates FR-026. The plan treats the existing cached character-profile prefilter as a cheap signal. SC-007's "compared = selected + cheap-signal candidates" should then say that candidates include prefilter passes. Confirm.
2. **FR-007 "same cause"**: the spec does not define how two causes match. The plan uses the same `source` plus a normalized cause key (casefold, collapse whitespace, strip digits and quoted literals), with `--attach e-N` to force a match. Confirm, or pick exact text.
3. **FR-013 `expected_output` required**: the spec does not say whether all 533 records must have `expected_output`, or where it comes from for records that lack one. The plan makes it optional and does not invent text.
4. **Minor assertion types** (`scope`, `handoff`, `coverage`; 7 uses): the spec does not say whether they stay in the vocabulary. The plan keeps them and folds only the `qualitative`/`structural` spellings.
5. **SC-009 20-sitting window** is still an assumption (spec Assumptions); no data sets it.
6. **Lint writes tracked files**: a lint run with Vale regenerates `styles/config/vocabularies/CoDM/accept.txt` and rewrites the tracked `wiki/_meta/lint-cache.json`. The spec does not say whether a read-side lint may change tracked files (compare FR-017, "read-side mutation"). The plan leaves this behavior unchanged.
