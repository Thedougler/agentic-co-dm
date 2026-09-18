# CLI

Agent-safe wiki operations use typed scopes, semantic mutations, and compact JSON output. Vault resolution uses `--vault`, `OBSIDIAN_VAULT_PATH`, the nearest `.env`, then `~/.obsidian-wiki/config`.

```sh
.venv/bin/python scripts/wiki-identity resolve <page> --vault wiki --json
.venv/bin/python scripts/wiki-identity scan --scope dir:entities/faction --vault wiki --json
.venv/bin/python scripts/wiki-lint --scope dir:entities/faction --plan --vault wiki --json
.venv/bin/python scripts/wiki-bulk-ops mutate replace_section --file page.md --heading-path Overview --content-file body.md --dry-run --json
.venv/bin/python scripts/wiki-bulk-ops transact --plan-file repair-plan.json --approve --vault wiki --json
.venv/bin/python scripts/manifest.py transition wiki --page old.md --transition merged_into --target new.md
.venv/bin/python scripts/check-policy-conflicts --json
```

Plans are previews until `--approve`. Exit `0` means clean/applied, `1` means findings or finalization failure, and `2` means invalid arguments, ambiguous identity, stale hashes, or failed preconditions. Ambiguous or redirect identities cannot be renamed or merged without explicit identity-resolution metadata. Every committed transaction runs `scripts/qmd-hook.sh` once; QMD failures leave committed files in place and return an actionable finalization error.
