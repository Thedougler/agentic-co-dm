# Research: Agent-Shaped Wiki CLI

```text
work_class: engineering
route: full-sdd
reason: new public wiki command and default result contract; FR-018 instruction updates (including health → next) ship in the same change
context_used: specs/027-wiki-agent-cli/spec.md, constitution, tools/wiki_ops/cli.py, scripts/wiki-lint, scripts/wiki-maintain, tools/lint_wiki.py, scripts/efficiency-trace.py, config/efficiency.yaml, docs/agents/wiki-maintenance-loop.md
context_omitted: creative-lint hydra internals, identity-resolution intelligence, Foundry, campaign wiki pages, efficiency promote/canary path, skill-creator evals
```

## 1. One `wiki` dispatcher

**Decision:** Add `scripts/wiki` with subcommands `lint`, `query`, and `health`. No setuptools console script. No npm/package.json wrappers. Creative hydra stays on `scripts/wiki-lint`.

**Rationale:** Existing agent tools are `scripts/*` with args in and JSON out (`tools/wiki_ops/cli.py`). Spec FR-001/FR-017. Clarify: npm wrappers are out; `wiki` is the command.

**Alternatives considered:** Three new binaries — violates one-command rule. Replace `scripts/wiki-lint` entirely — breaks creative subcommands. package.json scripts — user declined.

## 2. Vault and paths

**Decision:** Reuse `configured_vault` / `resolve_vault`. Path args are vault-relative files or prefixes. Zero args = whole live wiki. Unknown or out-of-vault path → exit 2, structured error, no scan. No fuzzy match, no `--scope` dialect on the new command.

**Rationale:** Spec FR-002/FR-003/SC-007.

**Alternatives considered:** Keep `--scope` as the public path language — extra dialect. Treat CWD as vault — spec forbids.

## 3. Default result contract

**Decision:** Default stdout is one compact JSON object (`emit_json`: sorted keys, no indent) plus compact `timing`. `--json` accepted and ignored. `--pretty` is the only human text. No TTY detection.

**Rationale:** Spec FR-004/FR-016/SC-006.

**Alternatives considered:** `isatty()` pretty-print — spec out of scope.

## 4. Lint dump grouped by file

**Decision:** Default `wiki lint` always includes summary fields **and** complete Vale-included findings grouped by file. Shape: `files` is an array of `{file, findings}` in argument / path order. Each finding is `{rule, file, line, severity, message}` with 1-based `line`. Omit file groups with zero findings. Nested per-rule maps are forbidden. `--full` is accepted and does not change output.

Two named files → two `files` entries. A prefix → one entry per file that has findings.

Health live lint **does not** copy this dump (FR-014).

**Rationale:** Clarify 2026-09-19 (always dump, grouped by file). SC-002 no longer caps stdout at 8 KB.

**Alternatives considered:** Worklist-only bulk default — rejected in clarify. Always-nested `findings_by_file` map — harder for agents than ordered blocks. `--full` as the only dump — rejected.

## 5. Checker cache

**Decision:** Per-file cache at `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Key = content sha256 of file bytes + checker-config digest (structural rules, Vale styles/config, template contracts). Hit → reuse that file’s checker results and extracts. Miss (hash change, config change, new path) → run checkers, write entry. Add/delete/rename: recompute corpus facts from cached extracts plus the current file set.

**Rationale:** Spec FR-008/SC-003. User asked hash identity; config digest still required so Vale style edits are not stale.

**Alternatives considered:** Repo `.cache/` — splits from vault. Hash-only without config digest — stale after Vale edits. mtime — misses identical-byte rewrites and false-misses on touch.

## 6. Query

**Decision:** `wiki query <phrase>` runs `env -u CI qmd query <phrase> -c <collection> -n <cap> --format json`. Defaults: collection `wiki`, cap 10. Compact hits: `title`, `path`, retrieval id. Backend missing or failing → structured error, exit 2.

**Rationale:** Spec FR-013/SC-004. Harnesses set `CI=true`.

**Alternatives considered:** `qmd search` (BM25) — spec says retrieval (`query`).

## 7. Health snapshot (compose, no second counter)

**Decision:** `wiki health` is one snapshot: live lint **summary** (same cache, no `files` dump) plus inventory plus Layer A stats plus compact `trends` (sitting/efficiency/skill/error, **slowest wiki commands**, **token-heaviest sittings**) plus ordered `focus` and `next`. `scripts/wiki-maintain --report` aliases that snapshot. Skill-eval pass/fail is out.

**Rationale:** Spec FR-014/FR-015/FR-019/FR-021/SC-005.

**Alternatives considered:** Full findings dump on health — spec forbids. Second health counter — spec forbids. Skill-eval dashboard — clarify out.

## 8. Exit codes and errors

**Decision:** 0 clean/success, 1 findings present (lint/health not clean), 2 bad invocation or precondition. Machine errors: `{"error":"…","status":"error"}` on stdout, exit 2. `--pretty` errors: one line on stderr, exit 2.

**Rationale:** Spec FR-005/FR-006. Named VI split in Assumptions.

**Alternatives considered:** Force all errors to stderr — agents splice two streams.

## 9. Agent instructions

**Decision:** Update lint/query/health invocations to `scripts/wiki`. Lint examples show the per-file dump. Health: run `scripts/wiki health`, then act on `next` (then remaining `focus`) without a DM wait. wiki-query keeps synthesis; CLI retrieval examples point at `wiki query`. Creative hydra stays on `scripts/wiki-lint`.

**Rationale:** FR-018/SC-008/SC-009.

**Alternatives considered:** Leave skills pointing at `./scripts/wiki-lint --json wiki/` — SC-008 fails.

## 10. Tests

**Decision:** pytest temp vaults for fail-closed paths, two-file `files` blocks, prefix dump, `--full` no-op, cache hits, `--pretty` vs default, health alias equality, empty-tracker trends, `focus`/`next`, command `timing` on stdout, slowest-command ranks, token-heaviest sittings, no skill-eval keys. Drop the live 8 KB size check. Cold-context smol for SC-008 (names a finding line + `next_page`) and SC-009.

**Rationale:** Constitution IV/XXIII. SC-002 is now two-file groups, not 8 KB.

**Alternatives considered:** Keep 8 KB assertion — contradicts clarified SC-002.

## 11. Health trends (existing trackers)

**Decision:** Compose compact aggregates; no health-only window; no new telemetry **file**.

Sources:

- `sittings.jsonl` via existing sitting list (repo root)
- `errors.md` via error list (open entries only)
- `.local/efficiency/traces.jsonl` via `efficiency-trace` load (90-day retention already)

`trends` keys: sitting counts by kind; top skills by sitting count (cap 5, usage names only); open error count + top causes (cap 3); efficiency sitting subset (`records`, `trajectory_tokens`, `retrieval_queries`, `hard_gate_failure_rate`, `dm_acceptance_rate`); `slowest_commands` (FR-020); `token_heaviest` sittings (FR-021). Missing files → empty/zero. Path args do not scope `trends`.

**Rationale:** Clarify sessions. Skill **usage** on sittings stays; skill **evals** do not.

**Alternatives considered:** Last-7-days window — new policy. Full efficiency report — too large.

## 12. Focus and next

**Decision:** `focus` ordered array, cap 5. Each item: `path`, `reason`, `source` (`lint` | `remorph` | `layout` | `tracker`). `next` is `focus[0]` or null.

Fill order (skip empty): lint `next_page`; first remorph plan `src`; first remaining layout/remorph prefix already in that plan; first open-error sitting path that is vault-relative. Never invent trees.

**Rationale:** FR-019/SC-009. Cap 5 is the plan bound.

**Alternatives considered:** Free-prose advice — forbidden.

## 13. Command timings on the existing efficiency stream

**Decision:** Discriminated records in the **same** `.local/efficiency/traces.jsonl`. Sitting records unchanged (`sitting_class` prep/wrapup, full schema). Command records: `record_kind: command` plus `command`, `duration_ms`, cache ints when applicable, `exit`, `timestamp`. Extend `efficiency-trace.validate_record` / `record` to accept that kind and skip it in sitting `report`/`promote`. `scripts/wiki` appends one command record per lint/query/health via the existing append helper. Health ranks `slowest_commands` from command records (max duration per command name, plus count). Timing failure must not fail the wiki command (best-effort append; stdout `timing` still present).

**Rationale:** FR-020 forbids a second ledger. Fake `prep` sittings would poison promotion (`SITTING_CLASSES` is only prep/wrapup; trajectory is tokens not milliseconds).

**Alternatives considered:** New `commands.jsonl` — second ledger. Stuffing wiki lint as `sitting_class: prep` — breaks same-kind promotion. Stdout-only timing — SC-010 fails.
