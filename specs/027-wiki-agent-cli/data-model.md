# Data Model: Agent-Shaped Wiki CLI

Entities are result objects and cache records, not wiki pages.

## Timing

Present on every successful or findings `wiki` stdout object.

| Field | Type | Notes |
|---|---|---|
| `command` | `lint` \| `query` \| `health` | |
| `duration_ms` | int | Wall clock, ≥ 0 |
| `cache` | `{hits, misses, vale_skipped}` \| omitted | Lint/health only |

## Worklist (lint summary + dump)

Default `wiki lint` object. Always includes grouped findings.

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
| `files` | File group[] | yes | One block per file that has findings, argument/path order |
| `timing` | Timing | yes | |
| `error` | string | status=error | |

Validation: MUST NOT contain nested per-rule finding maps. `unique` MUST NOT invent owners. `--full` does not add or remove keys.

### File group

| Field | Type | Notes |
|---|---|---|
| `file` | string | Vault-relative |
| `findings` | Finding record[] | Non-empty |

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
| `timing` | Timing | |
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
| `lint` | Worklist without `files` | Same cache as `wiki lint`; path-scoped; **no finding dump** |
| `waste` | object | Layer A A2 metrics (hits, hard_hits) |
| `staging` | `{leftover_count}` | `_raw` leftovers |
| `remorph` | `{plan_count, skip_count, error_count}` | A6 dry-run counts |
| `policy` | `{ok, conflict_count}` | Existing policy check |
| `cache` | same as worklist.cache | May live on `lint.cache` only; top-level allowed if identical |
| `trends` | Trends | Whole-tracker; empty/zero if files missing |
| `focus` | Focus item[] | Ordered, cap 5; present even if empty |
| `next` | Focus item \| null | `focus[0]` or null |
| `timing` | Timing | |

MUST NOT include per-step essays, a full findings dump, raw sittings, raw traces, skill-eval pass/fail, or missing-skill inventories.

`scripts/wiki-maintain --report` emits this same object.

Path arguments scope `pages` / `bytes` / `tokens` / `lint` / `focus`. `trends` is always whole-tracker.

## Trends

| Field | Type | Notes |
|---|---|---|
| `sittings` | `{count, by_kind}` | `by_kind` counts `prep` / `wrapup`; missing file → `count` 0 |
| `skills` | `{name, sittings}[]` | Top 5 skill **usage** names from sitting `skills_loaded`; empty if none. Not eval results |
| `errors` | `{open_count, causes}` | Open ledger only; `causes` is `{cause, count}[]` cap 3 |
| `efficiency` | object | Sitting subset of `efficiency-trace report`: `records`, `trajectory_tokens` (int), `retrieval_queries` (int), `hard_gate_failure_rate` (number), `dm_acceptance_rate` (number). Missing traces → `records` 0 and the rest 0 |
| `slowest_commands` | `{command, duration_ms, n}[]` | From `record_kind=command` rows; cap 3; highest `duration_ms` first |
| `token_heaviest` | `{sitting_class, job, tokens}[]` | From sitting records; `tokens` = sum of trajectory fields; cap 3; highest first |

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

Invalidation: content sha256 change, config_digest change, path add/delete/rename (missing path dropped; new path is a miss). Corpus facts always rebuilt from current path set + extracts.

## Command timing record

Appended to `.local/efficiency/traces.jsonl` (same stream as sitting traces).

| Field | Type | Notes |
|---|---|---|
| `record_kind` | `command` | Discriminator; sitting records omit this or are not `command` |
| `schema_version` | 1 | |
| `command` | `lint` \| `query` \| `health` | |
| `duration_ms` | int | |
| `cache_hits` | int | 0 when N/A |
| `cache_misses` | int | 0 when N/A |
| `vale_skipped` | int | 0 when N/A |
| `exit` | int | 0, 1, or 2 |
| `timestamp` | string | ISO-8601 |

Sitting records keep the existing efficiency schema. `promote` / sitting `report` ignore `record_kind=command`.

## Error object

`{"error":"<message>","status":"error"}` on stdout, exit 2. `--pretty`: one stderr line instead.

## State transitions

```text
lint:
  invoke → resolve vault → resolve paths (fail closed)
        → load cache → run/reuse checkers → rebuild corpus
        → summary + files dump → emit + append command record → exit 0|1|2

health:
  invoke → resolve vault → resolve paths (fail closed)
        → same lint path (drop files dump)
        → Layer A numbers (no steps essays)
        → read sittings/errors/traces (empty ok)
        → trends (incl. slowest_commands, token_heaviest) + focus + next
        → emit + append command record → exit 0|1|2

query:
  invoke → unset CI → qmd query → compact hits
        → emit + append command record → exit 0|2
```
