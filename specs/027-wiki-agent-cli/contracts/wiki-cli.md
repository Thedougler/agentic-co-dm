# Contract: `scripts/wiki`

Public seam for lint, query, and health. Implementation details live in the plan; this file is the observable interface.

## Invocation

```text
scripts/wiki lint [path ...] [--full] [--pretty] [--json]
scripts/wiki lint fix [path ...] [--full] [--pretty] [--json]
scripts/wiki query <phrase> [--collection NAME] [-n N] [--pretty] [--json]
scripts/wiki health [path ...] [--pretty] [--json]
```

Vault: existing configuration (`OBSIDIAN_VAULT_PATH`, nearest `.env`, `~/.obsidian-wiki/config`). CWD is not the vault selector.

Paths: vault-relative files or prefixes. Zero paths = whole live wiki. Union if several. Unknown or outside vault → exit 2, no scan, no fuzzy match.

`--json` is accepted and ignored. `--pretty` is explicit human text. No terminal detection.

`--full` is accepted on lint and lint fix as a compatibility no-op. Both commands always return their complete configured findings; the flag does not change fixer eligibility.

The checker backend is internal. Its structural, template, creative, and Vale findings are all surfaced by `wiki lint`; agents do not use evaluator-specific commands.

`scripts/wiki-maintain --report` is an alias of `scripts/wiki health` (identical snapshot).

## Exit codes

| Code | When |
|---|---|
| 0 | Clean lint/health, or query with a result object (including zero hits if the backend succeeded) |
| 1 | Lint/health completed with any findings or maintenance issues |
| 2 | Bad invocation, unknown path, missing vault, retrieval backend failure |

## Default stdout

Exactly one compact JSON object, `sort_keys=True`, no indent. `status` always present. Successful/findings objects include `timing` (`command`, `duration_ms`, and `cache` when lint/health).

### Lint

Required keys: `status`, `counts`, `hard_fail`, `finding_total`, `affected_pages`, `next_page`, `next`, `cache`, `files_checked`, `scope`, `ledger`, `timing`, `unique`, `backlog`, and `files`.

Lint includes aggregate counts and every configured checker finding, including all Vale findings and every severity. `files` is an array of `{file, findings}` in argument / path order. `findings` is `{rule, file, line, severity, message}[]` with 1-based `line`. There is no hard-only default or checker-suppression flag.

No nested per-rule finding maps. `unique` values are already-deduped targets. Lint MUST NOT guess, alias-match, or invent owners.

### Lint fix

`wiki lint fix [path ...]` uses the same path scope and fail-closed resolution as lint. Zero paths select the whole live wiki; multiple files/prefixes form their union. The resolved scope is retained for pre-fix lint, repair, and post-fix lint.

The command selects only explicitly registered fixers whose preconditions are deterministic and whose result is idempotent. It applies eligible mutations through the existing atomic, hash-preconditioned seam, then reruns lint over the same resolved scope.

Required keys: `status`, `scope`, `applied`, `skipped`, `remaining`, `changed_files`, `progress`, `cache`, `timing`.

`progress` is `{before_total, after_total, resolved, changed_files, next_changed, state_changed}`. Totals are non-negative integers from complete same-scope worklists; `resolved` contains stable finding identities present before and absent after; `changed_files` is sorted vault-relative paths; `next_changed` and `state_changed` are booleans. `state_changed` is true when findings, next target, or files changed.

`applied` contains `{rule, action, target, status, changed_files}` records where `status` is `applied` or `no_op`. `skipped` contains `{rule, action, target, reason}` records. `remaining` is the post-fix complete lint result. Unsupported, unsafe, conflicting, or failed-precondition findings are skipped and remain available for manual repair. An unchanged skipped or semantic finding is not retried against the same observation.

Exit code follows the post-fix result: `0` when clean, `1` when findings remain, `2` for bad invocation, unknown scope, or an unrecoverable precondition/error. A second identical run makes no further changes.

### Query

`{status, collection, hits, timing}` where `hits` is `{title, path, id}[]`. Default collection `wiki`, default cap 10. Retrieval runs even when `CI=true`. Failure: error object, exit 2, no invented hits.

### Health

One snapshot: `pages`, `bytes`, `tokens`, live lint summary (no `files` dump; includes finding/page totals, blocking rules, meaning, and repair action), waste / staging / remorph / policy, `trends` (including `slowest_commands`, `token_heaviest`, and small open-ledger entries when at most five exist), ordered `focus` (cap 5; each item includes an action), `next`, `context` (first-turn files, ranked skills, first-turn efficiency delta, `act`), `timing`. See [data-model.md](../data-model.md).

Missing sittings/errors/traces → zero/empty `trends`, still exit 0 or 1 from lint/Layer A — not exit 2.

No skill-eval pass/fail keys.

## `--pretty`

| Command | Text |
| lint | Scoreboard of counts / totals / next action / cache, then findings as `file:line  RULE  message` |
| lint fix | Scoreboard of applied / skipped / remaining findings / changed files, then post-fix findings as `file:line  RULE  message` |
| lint `--pretty --full` | Same human findings list; `--full` is a compatibility no-op |
| query | One hit per line: `path  title  id` |
| health | Short scoreboard (pages, bytes, tokens, lint hard total, quiet-relevant counts, slowest command, token-heaviest sitting, first-turn total) then `context.act`, `next.path`, and the `focus` list (`path  source  reason`) |

Pretty usage errors: one line on stderr, exit 2.

## Machine errors

Stdout: `{"error":"<message>","status":"error"}` exit 2.

## Side effects

Each lint, lint fix, query, and health run appends one `record_kind=command` row to `.local/efficiency/traces.jsonl`. Append failure does not change the wiki command’s exit code.

`lint`, `lint fix`, and `health` write `wiki <command>: elapsed_s=<n> still=1` to stderr at least every 10 seconds while running. Stdout remains one JSON object (`--pretty`: one human text result). A run under 10 seconds may emit no heartbeat. `query` has no heartbeat requirement.


## Non-goals this sitting

TTY format forks. Identity-resolution intelligence inside lint. Migrating the creative hydra. A second health counter or second benchmark file. Inventing vault folder trees. Skill-eval pass/fail. npm/package.json wrappers.
