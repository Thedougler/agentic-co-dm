# Research: Agent-Shaped Wiki CLI

```text
work_class: engineering
route: full-sdd
reason: new public wiki command and default result contract; FR-018 instruction updates (including health → next) ship in the same change
context_used: specs/027-wiki-agent-cli/spec.md, constitution, tools/wiki_ops/cli.py, scripts/wiki-lint, scripts/wiki-maintain, tools/lint_wiki.py, tools/wiki_ops/scope.py, qmd query --help, scripts/error-ledger.py, scripts/efficiency-trace.py, config/efficiency.yaml, sittings.jsonl schema, docs/agents/wiki-maintenance-loop.md, .agents/skills/wiki-lint/SKILL.md, .agents/skills/wiki-query/SKILL.md, tests/test_wiki_ops.py
context_omitted: creative-lint hydra internals, identity-resolution intelligence, Foundry, campaign wiki pages, efficiency promote/canary path
```

## 1. One `wiki` dispatcher

**Decision:** Add `scripts/wiki` with subcommands `lint`, `query`, and `health`. No setuptools console script. Creative hydra stays on `scripts/wiki-lint`.

**Rationale:** Existing agent tools are `scripts/*` with args in and JSON out (`tools/wiki_ops/cli.py`). Spec FR-001/FR-017. `pyproject.toml` has no scripts table; do not add one.

**Alternatives considered:** Three new binaries (`wiki-lint2`, `wiki-query`, `wiki-health`) — violates one-command rule. Replace `scripts/wiki-lint` entirely — breaks creative subcommands and `tests/test_wiki_ops.py`.

## 2. Vault and paths

**Decision:** Reuse `configured_vault` / `resolve_vault`. Path args are vault-relative files or prefixes. Zero args = whole live wiki. Unknown or out-of-vault path → exit 2, structured error, no scan. No fuzzy match, no `--scope` dialect on the new command.

**Rationale:** Spec FR-002/FR-003/SC-007. Current `wiki-lint` takes a vault positional plus `--scope dir:|files:|type:`. Agents fail `entities/npcs` vs `entities/npc` today because they invent owners; fail closed instead.

**Alternatives considered:** Keep `--scope` as the public path language — extra dialect. Treat CWD as vault — spec forbids.

## 3. Default result contract

**Decision:** Default stdout is one compact JSON object (`emit_json`: sorted keys, no indent). `--json` accepted and ignored. `--pretty` is the only human text. No TTY detection.

**Rationale:** Spec FR-004/FR-016/SC-006. Today `wiki-lint` indents unless `--json`; `wiki-maintain --report` always indents and dumps `steps`.

**Alternatives considered:** `isatty()` pretty-print — spec out of scope. Keep indented JSON as “human” — agents still parse it; `--pretty` is text.

## 4. Worklist vs findings dump

**Decision:** Default lint object is a worklist (FR-009). Nested `findings` / `findings_by_file` omitted. Exactly one existing file arg adds flat `findings[]` (FR-010). `--full` adds the complete dump and keeps worklist fields.

**Rationale:** Current `structural_main` already builds `backlog` and `next_page` but still embeds per-rule finding arrays. SC-001/SC-002 fail because of that blob.

**Unique targets:** For each rule with findings, `unique.<rule>` is the sorted unique target strings (missing-link target, broken path, page id — whatever the finding already names). Do not guess owners (FR-012).

**Alternatives considered:** Always include findings and document “ignore them” — still burns tokens. Separate `wiki lint --worklist` flag — default would remain the blob.

## 5. Checker cache

**Decision:** Per-file cache at `$VAULT/_meta/lint-cache.json` (lint already skips `_meta`). Key = content sha256 + checker-config digest (structural rule set, Vale styles/config, template contracts). Hit → reuse that file’s checker results and extracts. Miss → run checkers, write entry. Add/delete/rename: recompute corpus facts (links, missing owners, orphans) from cached extracts plus the current file set. Checker-config change invalidates those checkers’ entries.

**Rationale:** Spec FR-008/SC-003. No cache exists today (`tools/` has no cache). Vale currently runs only when `--scope` is set — FR-007 requires Vale on every `wiki lint` unless `--no-vale`. Caching Vale is the point of SC-003.

**Alternatives considered:** Repo `.cache/` — splits from vault. Content-hash only — stale after Vale style edits. Re-run Vale always — fails SC-003.

## 6. Query

**Decision:** `wiki query <phrase>` runs `env -u CI qmd query <phrase> -c <collection> -n <cap> --format json`. Defaults: collection `wiki` (empty `QMD_WIKI_COLLECTION` still `wiki`), cap 10. Compact hits: `title`, `path` (vault-relative), retrieval id (`#docid` / qmd id from JSON). Backend missing or failing → structured error, exit 2, no invented hits.

**Rationale:** Spec FR-013/SC-004. `qmd query` default `-n` is 5 (20 for json); user-facing default is 10. Harnesses set `CI=true`, which makes qmd refuse query. This is a retrieval wrapper, not a rewrite of wiki-query synthesis.

**Alternatives considered:** Call wiki-query skill steps (graph-query, grep, multi-hop) — out of scope. `qmd search` (BM25, no LLM) — spec says retrieval, which is `query`.

## 7. Health snapshot (compose, no second counter)

**Decision:** `wiki health` is one snapshot: live lint worklist (same cache, no findings dump) plus inventory (`pages`, `bytes`, `tokens`) plus Layer A stats already computed in `scripts/wiki-maintain` (waste, `_raw` leftovers, remorph plan counts, policy) plus compact `trends` from existing trackers plus ordered `focus` and `next`. `scripts/wiki-maintain --report` becomes an alias of that snapshot (same object, not a second counter). Exit 0/1/2 per FR-006 (today `--report` exits 0 whenever JSON is produced).

**Rationale:** Spec FR-014/FR-015/FR-019/SC-005. Current report is a per-step essay (`steps.A1`…`A6`). Promote numbers; drop essays from the default object.

**Alternatives considered:** Keep full `steps` tree and add a summary — still essays. New health counter beside `--report` — spec forbids. Dump raw sittings/traces — spec forbids.

## 8. Exit codes and errors

**Decision:** 0 clean/success, 1 findings present (lint/health not clean), 2 bad invocation or precondition. Machine errors: `{"error":"…","status":"error"}` on stdout, exit 2. `--pretty` errors: one line on stderr, exit 2.

**Rationale:** Spec FR-005/FR-006. Constitution VI says errors on stderr; spec Assumptions already name the stdout machine-error split as the existing wiki-ops convention (`emit_error`). Do not change `tools/wiki_ops.cli.EXIT_*` globally this sitting; the new command uses 0/1/2.

**Alternatives considered:** Force all errors to stderr — agents must splice two streams. Change every wiki-ops script’s exit map — extra blast radius.

## 9. Agent instructions

**Decision:** Update documented lint/query/health invocations to `scripts/wiki` and the worklist/health contract: `.agents/skills/wiki-lint/SKILL.md` (+ evals that pin `./scripts/wiki-lint --json`), wiki-status/wiki-lint standing examples in `AGENTS.md` / `.omp/AGENTS.md`. Health instructions: run `scripts/wiki health`, then act on `next` (then remaining `focus`) without waiting for the DM. wiki-query skill keeps synthesis; retrieval default examples that are “run this CLI” point at `wiki query`. Creative hydra docs stay on `scripts/wiki-lint`.

**Rationale:** FR-018/SC-009. Small agents (Luna/Haiku class) must not need extra interpretation.

**Alternatives considered:** Leave skills and hope agents discover `--help` — SC-008/SC-009 fail.

## 10. Tests

**Decision:** pytest against temp vaults (existing `test_wiki_ops.py` pattern) for path fail-closed, worklist keys, single-file findings, `--full`, cache hits, `--pretty` vs default, health alias equality, empty-tracker trends, `focus`/`next` ordering, no invented layout paths. One live-wiki size check for SC-002 (~100-page prefix < 8 KB). Cold-context smol subject for SC-008 and SC-009. Do not rewrite creative-lint tests.

**Rationale:** Constitution IV/XXIII. `scripts/wiki-lint` tests remain the old surface.

**Alternatives considered:** Fixture-only Vale cache tests without a second run — cannot prove SC-003.

## 11. Health trends (existing trackers)

**Decision:** Compose compact aggregates; do not add a health-only window or a new telemetry store.

Sources (read-only):

- `sittings.jsonl` via `scripts/error-ledger.py sitting list` (repo root)
- `errors.md` via `error list` (open entries only)
- `.local/efficiency/traces.jsonl` via `scripts/efficiency-trace.py report` (retention already 90 days in `config/efficiency.yaml`)

Compact `trends` keys (see data-model): sitting counts by kind; top skills by sitting count (cap 5); open error count + top causes (cap 3); efficiency `records`, `trajectory_tokens.value`, `retrieval.queries.value`, `hard_gate_failure_rate.value`, `dm_acceptance_rate.value`. Missing files → empty/zero aggregates, health still succeeds.

Path args scope live lint, inventory, and `focus`. Trends stay whole-tracker.

**Rationale:** Clarify session 2026-09-19. Trackers already exist; health is the agent surface.

**Alternatives considered:** Last-7-days window — new policy. Full efficiency report object — too large for small agents. Fail health when traces missing — invents a precondition the trackers do not require.

## 12. Focus and next

**Decision:** `focus` is a bounded ordered array (cap 5). Each item: `path`, `reason` (one line, existing rule/plan/tracker name), `source` (`lint` | `remorph` | `layout` | `tracker`). `next` is `focus[0]` or null.

Fill order (skip a source if empty):

1. `lint` — worklist `next_page` / first backlog page
2. `remorph` — first existing remorph plan `src` from Layer A A6 (filename kebab / greenlit remorph only)
3. `layout` — first remaining remorph/layout plan path that is a directory-prefix or layout-kind move already in that plan (not a new tree)
4. `tracker` — first open error `sitting` path if it names a vault-relative file; else omit

Do not invent folder trees. No remorph/layout plan → those sources absent. `--pretty` prints `next` then the `focus` list.

**Rationale:** FR-019/SC-009. Cap 5 is the plan bound (clarify left the number open; `next` is the one action).

**Alternatives considered:** Free-prose advice — spec forbids. Pretty-only focus — small agents load default JSON. Command pointers with no paths — SC-009 fails.
