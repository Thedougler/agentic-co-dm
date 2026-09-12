# Contract: `specify integration status --json`

CI and `scripts/check-speckit-dry.sh` consume this object. Fail closed.

## Required healthy fields

```json
{
  "status": "ok",
  "default_integration": "omp",
  "installed_integrations": ["codex", "grok", "omp", "claude"],
  "missing_managed_files": 0,
  "modified_managed_files": 0,
  "invalid_manifest_paths": 0,
  "findings": []
}
```

`installed_integrations` is a set: extra non-conflicting installs are allowed; any of the four missing is a failure.

## Fail

- `status` other than `ok`
- default not `omp`
- any of `codex`, `grok`, `omp`, `claude` absent
- unexplained missing or modified managed files
- invalid manifests
- non-empty `findings` unless the check allowlists a documented exception

## Do not assert

- Identical bytes across harness adapters
- That every task must run in Oh My Pi
