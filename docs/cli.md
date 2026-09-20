# CLI

Use `wiki` for agent-facing work. It resolves the vault from `OBSIDIAN_VAULT_PATH`, the nearest `.env`, then `~/.obsidian-wiki/config`; paths are vault-relative.

```sh
wiki lint [path ...] [--full]
wiki query "<phrase>"
wiki health
wiki mutate replace_section --file page.md --heading-path Overview --content-file body.md --dry-run
wiki repair --plan-file repair-plan.json --approve
```

`wiki lint` runs every configured checker and returns aggregate counts plus every flat finding by default. `--full` remains accepted as a compatibility no-op. Mutations require vault-relative targets and semantic preconditions; use `--dry-run` before applying and inspect the structured result before approval.
