# CLI

Agent-safe wiki operations use structured selectors and JSON output.

```sh
python3 scripts/wiki-identity resolve <page> --vault wiki --json
python3 scripts/wiki-identity scan --scope dir:entities/faction --vault wiki --json
python3 scripts/wiki-lint --scope dir:entities/faction --template --plan --vault wiki --json
python3 scripts/wiki-bulk-ops mutate replace_section --file page.md --heading-path Overview --content-file body.md --dry-run --json
python3 scripts/wiki-bulk-ops transact --plan-file repair-plan.json --approve --vault wiki --json
python3 scripts/manifest.py transition wiki --page old.md --transition merged_into --target new.md
python3 scripts/check-policy-conflicts --json
```

Plans are previews until `--approve`. Exit `0` means clean/applied, `1` means findings or finalization failure, and `2` means invalid arguments, ambiguous identity, stale hashes, or failed preconditions.
