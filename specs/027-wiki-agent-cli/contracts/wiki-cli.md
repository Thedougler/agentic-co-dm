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

Creative lint (`file`, `task`, `corpus`, `changed`, `rule`, `queue`, `template`, consolidate) is not this command. Use `scripts/wiki-lint`.

`scripts/wiki-maintain --report` is an alias of `scripts/wiki health` (identical snapshot).

## Exit codes

| Code | When |
|---|---|
| 0 | Clean lint/health, or query with a result object (including zero hits if the backend succeeded) |
| 1 | Lint/health completed with findings (`hard_fail` under `--hard`, or any counts under `--all`) |
| 2 | Bad invocation, unknown path, missing vault, retrieval backend failure |

## Default stdout

Exactly one compact JSON object, `sort_keys=True`, no indent. `status` always present.

### Lint worklist

Required keys: `status`, `counts`, `hard_fail`, `unique`, `backlog`, `next_page`, `cache`, `files_checked`, `scope`.

Bulk default: no `findings`, no `findings_by_file`.

Exactly one existing file argument: add `findings` as a flat list of `{rule, file, line, severity, message}` with 1-based `line`.

`--full`: complete finding dump **and** worklist keys.

`unique` values are already-deduped targets from findings. Lint MUST NOT guess, alias-match, or invent owners.

### Query

`{status, collection, hits}` where `hits` is `{title, path, id}[]`. Default collection `wiki`, default cap 10. Retrieval runs even when `CI=true`. Failure: error object, exit 2, no invented hits.

### Health

One snapshot: `pages`, `bytes`, `tokens`, live lint worklist (no findings dump), waste / staging / remorph / policy metrics. See [data-model.md](../data-model.md).

## `--pretty`

| Command | Text |
|---|---|
| lint | Scoreboard of counts / next_page / cache. Findings in scope: `file:line  RULE  message` |
| lint `--pretty --full` | Human findings list, not indented JSON |
| query | One hit per line: `path  title  id` |
| health | Short scoreboard (pages, bytes, tokens, lint hard total, quiet-relevant counts) |

Pretty usage errors: one line on stderr, exit 2.

## Machine errors

Stdout: `{"error":"<message>","status":"error"}` exit 2.

## Non-goals this sitting

TTY format forks. Identity-resolution intelligence inside lint. Migrating the creative hydra. A second health counter.
