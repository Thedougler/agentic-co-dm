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
| `pages` | int | Live markdown page count |
| `bytes` | int | Live page bytes |
| `tokens` | int \| null | tiktoken via existing token-count helper |
| `lint` | Worklist without `findings` | Same cache as `wiki lint` |
| `waste` | object | Layer A A2 metrics (hits, hard_hits) |
| `staging` | `{leftover_count}` | `_raw` leftovers |
| `remorph` | `{plan_count, skip_count, error_count}` | A6 dry-run counts |
| `policy` | `{ok, conflict_count}` | Existing policy check |
| `cache` | same as worklist.cache | May live on `lint.cache` only; top-level allowed if identical |

MUST NOT include per-step essays or a full findings dump.

`scripts/wiki-maintain --report` emits this same object.

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
lint/health:
  invoke → resolve vault → resolve paths (fail closed)
        → load cache → run/reuse checkers → rebuild corpus
        → worklist → emit → exit 0|1|2

query:
  invoke → unset CI → qmd query → compact hits → emit → exit 0|2
```
