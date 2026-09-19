# Data Model: Agent-Shaped Wiki CLI

Entities are result objects and cache records, not wiki pages.

## Worklist

Default `wiki lint` object. No nested finding arrays unless Single-file or Full dump applies.

| Field | Type | Required | Notes |
|---|---|---|---|
| `status` | `clean` \| `findings` \| `error` | yes | `error` only with exit 2 |
| `counts` | map rule → int | yes | Non-zero rules; `--hard` default omits soft-only |
| `hard_fail` | bool | yes | |
| `unique` | map rule → string[] | yes | Already-deduped targets per rule; empty map if clean |
| `backlog` | `{page, findings, bytes}[]` | yes | Live pages with findings, sort bytes then path |
| `next_page` | string \| null | yes | `backlog[0].page` or null |
| `cache` | `{hits, misses, vale_skipped}` | yes | Ints |
| `files_checked` | int | yes | |
| `scope` | `{paths: string[]}` | yes | Vault-relative args; `[]` means whole vault |
| `findings` | Finding record[] | single-file or `--full` | Absent on bulk default |
| `error` | string | status=error | |

Validation: bulk default MUST NOT contain `findings` or `findings_by_file`. `unique` MUST NOT invent owners.

## Finding record

| Field | Type | Notes |
|---|---|---|
| `rule` | string | |
| `file` | string | Vault-relative |
| `line` | int | 1-based |
| `severity` | string | Existing lint severities |
| `message` | string | |

## Query result

| Field | Type | Notes |
|---|---|---|
| `status` | `ok` \| `error` | |
| `collection` | string | Default `wiki` |
| `hits` | Query hit[] | Cap default 10 |
| `error` | string | On failure |

## Query hit

| Field | Type | Notes |
|---|---|---|
| `title` | string | |
| `path` | string | Vault-relative |
| `id` | string | Retrieval id from qmd JSON |

No snippets in the default object.

## Health snapshot

| Field | Type | Notes |
|---|---|---|
| `status` | `clean` \| `findings` \| `error` | Align with lint when live lint is not clean |
| `pages` | int | Live markdown page count (path-scoped) |
| `bytes` | int | Live page bytes (path-scoped) |
| `tokens` | int \| null | tiktoken via existing token-count helper |
| `lint` | Worklist without `findings` | Same cache as `wiki lint`; path-scoped |
| `waste` | object | Layer A A2 metrics (hits, hard_hits) |
| `staging` | `{leftover_count}` | `_raw` leftovers |
| `remorph` | `{plan_count, skip_count, error_count}` | A6 dry-run counts |
| `policy` | `{ok, conflict_count}` | Existing policy check |
| `cache` | same as worklist.cache | May live on `lint.cache` only; top-level allowed if identical |
| `trends` | Trends | Whole-tracker; empty/zero if files missing |
| `focus` | Focus item[] | Ordered, cap 5; present even if empty |
| `next` | Focus item \| null | `focus[0]` or null |

MUST NOT include per-step essays, a full findings dump, raw sittings, or raw traces.

`scripts/wiki-maintain --report` emits this same object.

Path arguments scope `pages` / `bytes` / `tokens` / `lint` / `focus`. `trends` is always whole-tracker.

## Trends

| Field | Type | Notes |
|---|---|---|
| `sittings` | `{count, by_kind}` | `by_kind` counts `prep` / `wrapup`; missing file → `count` 0 |
| `skills` | `{name, sittings}[]` | Top 5 skill names from sitting `skills_loaded`; empty list if none |
| `errors` | `{open_count, causes}` | Open ledger only; `causes` is `{cause, count}[]` cap 3 |
| `efficiency` | object | Subset of `efficiency-trace report`: `records`, `trajectory_tokens` (int), `retrieval_queries` (int), `hard_gate_failure_rate` (number), `dm_acceptance_rate` (number). Missing traces → `records` 0 and the rest 0 |

Do not embed the full efficiency report or sitting rows.

## Focus item

| Field | Type | Notes |
|---|---|---|
| `path` | string | Vault-relative file or prefix |
| `reason` | string | One objective line; existing rule, remorph/layout plan reason, or tracker name |
| `source` | `lint` \| `remorph` \| `layout` \| `tracker` | |

Fill order (skip empty sources): lint `next_page`, first remorph plan `src`, first remaining layout/remorph prefix already in that plan, first open-error sitting path that is vault-relative. Never invent trees.

## Checker cache

File: `$VAULT/_meta/lint-cache.json`.

| Field | Type | Notes |
|---|---|---|
| `config_digest` | string | Hash of checker configuration |
| `entries` | map vault-relative path → Cache entry | |

### Cache entry

| Field | Type | Notes |
|---|---|---|
| `content_sha256` | string | File bytes |
| `config_digest` | string | Must match current or entry is a miss |
| `extracts` | object | Links and named targets needed for corpus refresh |
| `results` | object | Per-checker findings for this file |

Invalidation: content change, config_digest change, path add/delete/rename (missing path dropped; new path is a miss). Corpus facts always rebuilt from current path set + extracts.

## Error object

`{"error":"<message>","status":"error"}` on stdout, exit 2. `--pretty`: one stderr line instead.

## State transitions

```text
lint:
  invoke → resolve vault → resolve paths (fail closed)
        → load cache → run/reuse checkers → rebuild corpus
        → worklist → emit → exit 0|1|2

health:
  invoke → resolve vault → resolve paths (fail closed)
        → same lint path (no findings dump)
        → Layer A numbers (no steps essays)
        → read sittings/errors/traces (empty ok)
        → trends + focus + next → emit → exit 0|1|2

query:
  invoke → unset CI → qmd query → compact hits → emit → exit 0|2
```
