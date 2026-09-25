# CLI

Use `wiki` for agent-facing work. It runs from any directory: the repository root comes from the script's own location, and the vault is `--vault`, then `OBSIDIAN_VAULT_PATH`, the repository `.env`, `<repo>/wiki`, and finally `~/.obsidian-wiki/config`. Paths are vault-relative. Every result names the resolved `vault`.

```sh
wiki                                   # one line per subcommand
wiki lint entities/place/Belumara.md   # a page, a directory, or a kind:value scope
wiki lint dir:entities/place
wiki lint fix dir:entities/place --dry-run
wiki query "Belumara" -n 5
wiki health
wiki mutate --stdin --dry-run < op.json
wiki repair --plan-file repair-plan.json --approve
```

`wiki <subcommand> --help` shows only that subcommand, with an `Examples:` block. Options may come before or after paths. Scopes are `kind:value` with kind `files`, `directory` (`dir`), `entity_type` (`type`), `identity_set`, `changed`, or `bundle`. `--stdin` reads newline-separated paths (lint, lint fix, health) or one JSON mutation or plan (mutate, repair); `--paths-only` prints one path per line.

`wiki lint` runs every configured checker and returns aggregate counts plus every flat finding. `lint fix` is its own subcommand and applies only repairs with exactly one correct output. `lint fix`, `mutate`, and `repair` take `--dry-run`, which returns `planned` and writes nothing; running the same command again after it applied reports `already_done` with `changed: []`. No command prompts.

Success output always carries `status`, `vault`, `changed`, `counts`, `timing.duration_ms`, and `next`. `wiki health` reports facts: `focus` lists up to five paths in the fixed order lint, remorph, layout, open ledger entries, and `next` is the first of them. Invalid input exits 2 with `{status, error, hint, example, list_valid}` on stdout and the message on stderr.
