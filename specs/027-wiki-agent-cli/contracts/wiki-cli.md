# Contract: `scripts/wiki`

Public seam for lint, query, and health. Implementation details live in the plan; this file is the observable interface.

## Invocation

```text
scripts/wiki lint [path ...] [--full] [--pretty] [--json] [--hard] [--all] [--no-vale] [--no-template]
scripts/wiki query <phrase> [--collection NAME] [-n N] [--pretty] [--json]
scripts/wiki health [path ...] [--pretty] [--json]
```

Vault: existing configuration (`OBSIDIAN_VAULT_PATH`, nearest `.env`, `~/.obsidian-wiki/config`). CWD is not the vault selector.

Paths: vault-relative files or prefixes. Zero paths = whole live wiki. Union if several. Unknown or outside vault → exit 2, no scan, no fuzzy match.

`--json` is accepted and ignored. `--pretty` is explicit human text. No terminal detection.

`--full` is accepted on lint and MUST NOT change lint output.

Creative lint (`file`, `task`, `corpus`, `changed`, `rule`, `queue`, `template`, consolidate) is not this command. Use `scripts/wiki-lint`.

`scripts/wiki-maintain --report` is an alias of `scripts/wiki health` (identical snapshot).

## Exit codes

| Code | When |
|---|---|
| 0 | Clean lint/health, or query with a result object (including zero hits if the backend succeeded) |
| 1 | Lint/health completed with findings (`hard_fail` under `--hard`, or any counts under `--all`) |
| 2 | Bad invocation, unknown path, missing vault, retrieval backend failure |

## Default stdout

Exactly one compact JSON object, `sort_keys=True`, no indent. `status` always present. Successful/findings objects include `timing` (`command`, `duration_ms`, and `cache` when lint/health).

### Lint

Required keys: `status`, `counts`, `hard_fail`, `unique`, `backlog`, `next_page`, `cache`, `files_checked`, `scope`, `files`, `timing`.

`files` is an array of `{file, findings}` in argument / path order. `findings` is `{rule, file, line, severity, message}[]` with 1-based `line`. Vale included unless `--no-vale`. Groups with zero findings are omitted.

Two named files → two `files` entries. A prefix → one entry per file that has findings.

No nested per-rule finding maps. `unique` values are already-deduped targets. Lint MUST NOT guess, alias-match, or invent owners.

### Query

`{status, collection, hits, timing}` where `hits` is `{title, path, id}[]`. Default collection `wiki`, default cap 10. Retrieval runs even when `CI=true`. Failure: error object, exit 2, no invented hits.

### Health

One snapshot: `pages`, `bytes`, `tokens`, live lint **summary** (no `files` dump), waste / staging / remorph / policy, `trends` (including `slowest_commands` and `token_heaviest`), ordered `focus` (cap 5), `next`, `context` (first-turn files, ranked skills, first-turn efficiency delta, `act`), `timing`. See [data-model.md](../data-model.md).

Missing sittings/errors/traces → zero/empty `trends`, still exit 0 or 1 from lint/Layer A — not exit 2.

No skill-eval pass/fail keys.

## `--pretty`

| Command | Text |
|---|---|
| lint | Scoreboard of counts / next_page / cache, then findings grouped by file as `file:line  RULE  message` |
| lint `--pretty --full` | Same human findings list |
| query | One hit per line: `path  title  id` |
| health | Short scoreboard (pages, bytes, tokens, lint hard total, quiet-relevant counts, slowest command, token-heaviest sitting, first-turn total) then `context.act`, `next.path`, and the `focus` list (`path  source  reason`) |

Pretty usage errors: one line on stderr, exit 2.

## Machine errors

Stdout: `{"error":"<message>","status":"error"}` exit 2.

## Side effects

Each lint/query/health run appends one `record_kind=command` row to `.local/efficiency/traces.jsonl`. Append failure does not change the wiki command’s exit code.


`lint` and `health` write `wiki <command>: elapsed_s=<n> still=1` to stderr at least every 10 seconds while running. Stdout remains one JSON object (`--pretty`: one human text result). A run under 10 seconds may emit no heartbeat. `query` has no heartbeat requirement.


## Non-goals this sitting

TTY format forks. Identity-resolution intelligence inside lint. Migrating the creative hydra. A second health counter or second benchmark file. Inventing vault folder trees. Skill-eval pass/fail. npm/package.json wrappers.
