# Data Model: Agent-Shaped Wiki CLI

Entities are result objects and cache records, not wiki pages.

## Timing

Present on every successful or findings `wiki` stdout object.

| Field | Type | Notes |
|---|---|---|
| `command` | `lint` \| `lint fix` \| `query` \| `health` | |
| `duration_ms` | int | Wall clock, ≥ 0 |
| `cache` | `{hits, misses, vale_skipped}` \| omitted | Lint/health only |

## Worklist (lint overview + complete dump)

Default `wiki lint` returns aggregate counts and the complete finding dump. `--full` is a compatibility no-op.

| Field | Type | Required | Notes |
|---|---|---|---|
| `status` | `clean` \| `findings` \| `error` | yes | `error` only with exit 2 |
| `counts` | map rule → int | yes | Non-zero rules across all configured checkers |
| `hard_fail` | bool | yes | |
| `finding_total` | int | yes | Sum of `counts` |
| `affected_pages` | int | yes | Pages with at least one finding |
| `next_page` | string \| null | yes | Same path as `next.path`, or null |
| `next` | object \| null | yes | `{path, findings, bytes, action}` for the smallest dirty file, or null |
| `cache` | `{hits, misses, vale_skipped}` | yes | Ints |
| `files_checked` | int | yes | |
| `scope` | `{paths: string[]}` | yes | Vault-relative args; `[]` means whole vault |
| `ledger` | object | yes | Open operational failures |
| `timing` | Timing | yes | |
| `unique` | map rule → string[] | yes | Already-deduped targets per rule |
| `backlog` | `{page, findings, bytes}[]` | yes | Dirty pages, sorted bytes then path |
| `files` | File group[] | yes | One block per file with findings, argument/path order |
| `error` | string | status=error | |

`next.path` is the smallest dirty file by byte size; vault-relative path breaks ties. Its `action` tells the agent to run `wiki lint fix <path>`, rerun the affected scope, and use `wiki lint <path>` for remaining findings. Findings are flat records, never nested per-rule maps. Every configured checker and severity contributes to the aggregate counts. `unique` MUST NOT…

### File group

| Field | Type | Notes |
|---|---|---|
| `file` | string | Vault-relative |
| `findings` | Finding record[] | Non-empty |


## Fix result

`wiki lint fix [paths...]` returns one compact machine object after applying eligible fixers and rerunning lint over the same resolved scope.

| Field | Type | Required | Notes |
|---|---|---|---|
| `status` | `clean` \| `findings` \| `error` | yes | Derived from post-fix lint; exit 2 only for rejected invocation/precondition |
| `scope` | `{paths: string[]}` | yes | Original vault-relative arguments; `[]` means whole vault |
| `applied` | Applied fix[] | yes | Each applied or no-op registered fixer, stable finding/action identity, target, changed files, and result |
| `skipped` | Skipped fix[] | yes | Eligible-scope findings not changed, with stable reason (`unsupported`, `unsafe`, `conflict`, or `precondition`) |
| `remaining` | Worklist summary | yes | Post-fix findings; detailed file groups require `--full` if supported |
| `changed_files` | string[] | yes | Sorted vault-relative files changed by this run |
| `cache` | `{hits, misses, vale_skipped}` | yes | Post-fix lint cache accounting |
| `timing` | Timing | yes | `command` is `lint fix` |

Fixers are selected from an explicit registry keyed by finding rule/action. A fixer MUST validate its precondition, use the existing hash-preconditioned atomic mutation seam, and be a no-op when the desired state already holds. Findings without a registered eligible fixer remain in `remaining`.

### Applied fix

| Field | Type | Notes |
|---|---|---|
| `rule` | string | Finding rule |
| `action` | string | Registered fixer action |
| `target` | string | Vault-relative target |
| `status` | `applied` \| `no_op` | |
| `changed_files` | string[] | Sorted vault-relative paths |

### Skipped fix

| Field | Type | Notes |
|---|---|---|
| `rule` | string | Finding rule |
| `action` | string \| null | Registered action when known |
| `target` | string | Vault-relative target |
| `reason` | `unsupported` \| `unsafe` \| `conflict` \| `precondition` | Machine-readable manual-repair reason |
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
| `lint` | Worklist without `files` | Same cache as `wiki lint`; path-scoped; **no finding dump**. The summary also exposes `finding_total`, `affected_pages`, `blocking`, `meaning`, and `action` so checker-finding counts are not mistaken for page counts. |
| `waste` | object | Layer A A2 metrics (hits, hard_hits) |
| `staging` | `{leftover_count}` | `_raw` leftovers |
| `remorph` | `{plan_count, skip_count, error_count}` | A6 dry-run counts |
| `policy` | `{ok, conflict_count}` | Existing policy check |
| `cache` | same as worklist.cache | May live on `lint.cache` only; top-level allowed if identical |
| `trends` | Trends | Whole-tracker; empty/zero if files missing |
| `focus` | Focus item[] | Ordered, cap 5; present even if empty |
| `next` | Focus item \| null | `focus[0]` or null |
| `timing` | Timing | |
| `context` | Context load | First-turn files, ranked skills, efficiency delta, `act` |

## Context load

| Field | Type | Notes |
|---|---|---|
| `encoding` | string | tiktoken encoding |
| `first_turn` | `{total_tokens, files}` | `files` is `{path, tokens}[]` descending; always-loaded: `.omp/AGENTS.md`, repo `AGENTS.md`, vault `AGENTS.md`, vault `hot.md` |
| `skills` | `{name, path, tokens, evals, criteria, coverage}[]` | Installed `SKILL.md` descending; cap 15. `coverage` is `with` if evals and criteria else `without` |
| `skills_total` | int | Count of installed skills |
| `eval_coverage` | `{with, without}` | Skills with vs without eval criteria |
| `efficiency` | `{first_turn_tokens, previous_first_turn_tokens, delta_tokens, trend}` | `trend` is `up` \| `down` \| `flat` \| `new` vs last health command record |
| `act` | string[] | Imperative steps with done-when; no file bodies |


MUST NOT include per-step essays, a full findings dump, raw sittings, raw traces, skill-eval pass/fail, or file bodies.

`scripts/wiki-maintain --report` emits this same object.

Path arguments scope `pages` / `bytes` / `tokens` / `lint` / `focus`. `trends` is always whole-tracker.

## Trends

| Field | Type | Notes |
|---|---|---|
| `sittings` | `{count, by_kind}` | `by_kind` counts `prep` / `wrapup`; missing file → `count` 0 |
| `skills` | `{name, sittings}[]` | Top 5 skill **usage** names from sitting `skills_loaded`; empty if none. Not eval results |
| `errors` | `{open_count, causes, entries?}` | Open ledger only; `causes` is `{cause, count}[]` cap 3. When at most five open records exist, `entries` includes their compact id/cause/path details. |
| `slowest_commands` | `{command, duration_ms, n}[]` | From `record_kind=command` rows; cap 3; highest `duration_ms` first |
| `token_heaviest` | `{sitting_class, job, tokens}[]` | From sitting records; `tokens` = sum of trajectory fields; cap 3; highest first |

Do not embed the full efficiency report or sitting rows.

## Focus item

| Field | Type | Notes |
|---|---|---|
| `path` | string | Vault-relative file or prefix |
| `reason` | string | One objective line; existing rule, remorph/layout plan reason, or tracker name |
| `source` | `lint` \| `remorph` \| `layout` \| `tracker` | |
| `action` | string | Imperative next step for this focus item, ending with a health rerun. |

Fill order (skip empty sources): lint `next_page`, first remorph plan `src`, first remaining layout/remorph prefix already in that plan, first open-error sitting path that is vault-relative. Never invent trees.

## Checker cache

File: `$VAULT/_meta/lint-cache.json`.

| Field | Type | Notes |
|---|---|---|
| `version` | integer | Cache schema version; an unsupported or missing version invalidates the whole document |
| `config_digest` | string | Hash of rules state (Vale styles/config, structural lint sources, template contracts, checker flags) |
| `entries` | map vault-relative path → Cache entry | |

### Cache entry

| Field | Type | Notes |
|---|---|---|
| `content_sha256` | string | File bytes |
| `template_sha256` | string | Bytes of the template selected from the page's current `type`/`kind`; empty when no template applies |
| `config_digest` | string | Must match current or entry is a miss |
| `extracts` | object | Links and named targets needed for corpus refresh |
| `results` | object | Per-checker findings for this file |

Invalidation: unsupported/missing cache version, content sha256 change, resolved template sha256 change, rules-state `config_digest` change, path add/delete/rename (missing path dropped; new path is a miss). Corpus facts always rebuilt from current path set + extracts.

## Command timing record

Appended to `.local/efficiency/traces.jsonl` (same stream as sitting traces).

| Field | Type | Notes |
|---|---|---|
| `record_kind` | `command` | Discriminator; sitting records omit this or are not `command` |
| `schema_version` | 1 | |
| `command` | `lint` \| `lint fix` \| `query` \| `health` | |
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

lint:
  invoke → resolve vault → resolve paths (fail closed)
        → load cache → run/reuse checkers → rebuild corpus
        → summary + files dump → emit + append command record → exit 0|1|2

lint fix:
  invoke → resolve vault → resolve paths (fail closed)
        → lint selected scope → select explicit eligible fixers
        → validate preconditions and apply atomic no-op-safe mutations
        → rerun lint on the same scope → classify applied/skipped/remaining
        → emit + append command record → exit 0|1|2

health:
  invoke → resolve vault → resolve paths (fail closed)
        → same lint path (drop files dump)
        → Layer A numbers (no steps essays)
        → read sittings/errors/traces (empty ok)
        → context (tiktoken first-turn files + ranked skills + act)
        → emit + append command record (health rows may include first_turn_tokens)

query:
  invoke → unset CI → qmd query → compact hits
        → emit + append command record → exit 0|2
```
