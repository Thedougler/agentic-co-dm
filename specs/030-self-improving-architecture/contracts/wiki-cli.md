# Contract: Wiki CLI surface (FR-027–FR-039)

This contract covers `scripts/wiki` (`lint`, `lint fix`, `query`, `health`, `mutate`, `repair`), `scripts/luna-eval`, and `scripts/error-ledger.py`. It extends feature 027: default output is compact JSON on stdout, `--pretty` is for humans, and there are no fuzzy paths.

## Discovery (FR-027)
- The repo root is found from the script's own location. The command works from any working directory.
- Vault order: `--vault` > `OBSIDIAN_VAULT_PATH` > repo `.env` > `<repo>/wiki` > `~/.obsidian-wiki/config`.
- Every result includes `"vault": "<absolute path>"`.

## Shape (FR-031, FR-034)
- Bare `wiki` prints one line per subcommand (`lint`, `lint fix`, `query`, `health`, `mutate`, `repair`) and exits 0.
- `wiki <sub> --help` prints only that subcommand's usage, options, and an `Examples:` block.
- `lint fix` MUST be a real subcommand, not a positional `fix` token inside the path list (FR-034). It is an argparse subparser under `lint`, and the only accepted form is `wiki lint fix [paths…] [options]`.
- A bare `fix` token among the lint paths (e.g. `wiki lint entities/place/Belumara.md fix`) exits 2 with the FR-035 error object: `"error":"'fix' is not a lint path"`, `"hint":"lint fix is a subcommand"`, `"example":"wiki lint fix entities/place/Belumara.md"`. Nothing is linted or written.
- Options may appear before or after positionals.

## Inputs (FR-030, FR-033)
- Paths are vault-relative. Scopes are `kind:value` with kind ∈ `files|directory(dir)|entity_type(type)|identity_set|changed|bundle`.
- `--stdin` reads newline-separated paths (lint, lint fix, health) or one JSON payload (mutate, repair).
- `--paths-only` prints one path per line. `--ids-only` does the same for error-ledger.
- No command prompts. A missing required input is an error.

## Errors (FR-035): exit 2, JSON on stdout, message also on stderr
```json
{"status":"error","error":"path not found in vault: 'wiki/entities/place/Belumara.md'",
 "hint":"paths are vault-relative","example":"wiki lint entities/place/Belumara.md",
 "list_valid":"wiki lint --help"}
```
Cases that must produce this error: an unknown path, a `wiki/`-prefixed path, a bare `fix` token in the lint path list, a scope without `:`, an unknown scope kind (list the allowed kinds), and an option the subcommand does not take.

## Mutation safety (FR-036, FR-037)
- `lint fix`, `mutate`, `repair`, `error-ledger error append|drain|migrate` accept `--dry-run`. A dry run returns `"planned": [...]` and writes nothing.
- A second run with the same inputs returns `"changed": []` and `"status": "already_done"`.
- No confirmation prompt exists. If one is ever added, `--yes` bypasses it.

## Success output (FR-038)
Required keys: `status`, `vault`, `changed` (paths or ids), `counts` (`before`/`after` where applicable), `timing.duration_ms`, and `next` (the next actionable target, or `null`). `health` adds `next` as one concrete command, e.g. `wiki lint fix dir:entities/npc`.

## Examples blocks (FR-032). The real invocations each `--help` shows:
- `wiki lint entities/place/Belumara.md`
- `wiki lint dir:entities/place`
- `wiki lint fix dir:entities/place --dry-run`
- `wiki query "Belumara" -n 5`
- `wiki health`
- `wiki mutate --stdin --dry-run < op.json`
- `python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …"`
- `scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/pd/iteration-1`

## Regression tests (FR-039)
One test per rule class above, in `tests/test_wiki_cli.py` (and `tests/test_error_ledger_repairs.py` for the ledger). Each test drives the public command through a subprocess.
