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

## 4. Bounded lint overview with explicit detail

**Decision:** Default `wiki lint` returns aggregate counts, total findings, affected-page count, cache/scope metadata, and `next`. `next` is `{path, findings, bytes, action}` for the smallest dirty file by bytes, then vault-relative path. The default omits `unique`, `backlog`, and per-file findings so whole-wiki output stays bounded. `--full` adds the complete Vale-included findings grouped by file; each finding is `{rule, file, line, severity, message}` with 1-based `line`.

Health live lint continues to use the compact overview.

**Rationale:** Bulk linting 2–1000 files should present one actionable work item without forcing the agent to load every finding. The detailed escape hatch keeps repair evidence available for the selected page.

**Alternatives considered:** Always dumping grouped findings — token growth scales with dirty pages. A hard-coded one-file limit — hides aggregate issue coverage and makes scope-dependent behavior surprising.

## 5. Checker cache

**Decision:** Per-file cache at `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Key = unique file (content sha256) + rules state (`digest_rules`: Vale styles/config, `tools/lint_wiki.py`, `scripts/wiki-lint`, creative-lint sources, template contracts, checker flags). Hit → reuse that file’s checker results and extracts. Miss (hash change, rules-state change, new path) → run checkers, write entry. Add/delete/rename: recompute corpus facts from cached extracts plus the current file set.

**Rationale:** Spec FR-008/SC-003. User asked hash identity; rules-state digest is required so Vale style or structural-rule edits are not stale.

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

**Decision:** Update lint/query/health invocations to `scripts/wiki`. Lint examples show the bounded overview and `wiki lint <next.path> --full` for repair detail. Health: run `scripts/wiki health`, then act on `next` (then remaining `focus`) without a DM wait. wiki-query keeps synthesis; CLI retrieval examples point at `wiki query`. Creative hydra stays on `scripts/wiki-lint`.

**Rationale:** FR-018/SC-008/SC-009.

**Alternatives considered:** Keep agent instructions on the backend `scripts/wiki-lint` command — that would preserve the hard/soft omission path and bypass the bounded public worklist.

## 10. Tests

**Decision:** pytest temp vaults for fail-closed paths, bounded whole-wiki and scoped lint summaries, smallest-next ordering, explicit `--full` file groups, cache hits, `--pretty` vs default, health alias equality, empty-tracker trends, `focus`/`next`, command `timing` on stdout, slowest-command ranks, token-heaviest sittings, no skill-eval keys. Cold-context smol for SC-008 (names aggregate counts + `next.path`/action) and SC-009.

**Rationale:** Constitution IV/XXIII. The default result must remain token-bounded as the wiki grows.

**Alternatives considered:** Keep complete findings in the default object — directly contradicts the bounded bulk-lint requirement.

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
