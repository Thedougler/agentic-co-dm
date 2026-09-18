# Contract: Scoped Lint

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## CLI Surface

### `wiki-lint --scope <spec> [--no-template] [--plan] [--from <findings.json>] [--vault <vault>] [--json]`

Run lint with explicit scope and optional repair plan generation. Template conformance runs by default.

**Scope specification**:
- `dir:entities/faction` — directory scope
- `type:faction` — entity type scope
- `files:a.md,b.md` — explicit file list
- `changed:HEAD~1` — git diff scope
- Omit for full vault (existing behavior)

**Flags**:
- `--no-template`: Disable template conformance (default: enabled; see template-contract.md)
- `--plan`: Generate a repair plan from deterministic findings instead of raw findings
- `--from <file>`: Build a plan from previously saved lint output (avoids re-running lint)
- `--vault`: Vault root
- `--json`: Structured JSON output (default for agent consumption)

### Standard Output

```json
{
  "scope": {"kind": "directory", "value": "entities/faction"},
  "files_checked": 31,
  "counts": {"HARD": 5, "REPAIR": 3, "INFO": 12},
  "findings": [
    {
      "key": "broken_links",
      "file": "entities/faction/fisks-fleet.md",
      "line": 42,
      "severity": "HARD",
      "message": "Wikilink [[Old Target]] does not resolve",
      "repair_class": "deterministic_repair",
      "repair_action": { "kind": "rewrite_links", "..." : "..." }
    }
  ]
}
```

### Plan Output (`--plan`)

```json
{
  "scope": {"kind": "directory", "value": "entities/faction"},
  "source_findings": 20,
  "deterministic_actions": 5,
  "human_only": 3,
  "diagnostic_only": 12,
  "actions": [
    {
      "finding_rule": "broken_links",
      "finding_file": "entities/faction/fisks-fleet.md",
      "finding_line": 42,
      "mutation": { "kind": "rewrite_links", "..." : "..." }
    }
  ],
  "hash": "sha256:..."
}
```

**Exit codes**: 0 = clean, 1 = error, 2 = findings/plan generated

## Scope Resolution

1. Parse scope specification into a `Scope` object.
2. Resolve to file list:
   - `dir`: glob `<dir>/**/*.md`, filter by SKIP_DIRS
   - `type`: scan all vault `.md` files, filter by frontmatter `type` field
   - `files`: use directly
   - `changed`: `git diff --name-only <ref>`, filter to `.md` in vault
3. Pass resolved file list to lint engine.

## Integration with Existing Lint

The existing `tools/lint_wiki.py` `load()` function returns all pages. Scoped lint wraps this:

1. If scope is provided: filter the returned pages dict to only matching paths.
2. Run existing HARD checks on the filtered set.
3. Run template conformance on filtered set (unless `--no-template`).
4. Merge findings, classify repair classes, format output.

The existing no-scope behavior is unchanged — `wiki-lint` without `--scope` works exactly as before.

## Repair Class Assignment

Each existing HARD key maps to a repair class:

| HARD Key | Repair Class | Notes |
|---|---|---|
| `broken_links` | `deterministic_repair` | Resolvable via link repair |
| `missing_frontmatter` | `deterministic_repair` | Can add default values |
| `bad_type` | `human_repair` | Needs correct type value |
| `bad_lifecycle` | `human_repair` | Needs correct lifecycle value |
| `spaced_basename` | `deterministic_repair` | Kebab-case rename |
| `duplicate_stems` | `human_repair` | Needs identity resolution first |
| `snake_case_owner_basenames` | `deterministic_repair` | Rename to kebab-case |
| `illegal_basename` | `human_repair` | Needs valid name |
| `aruhe_prefix_basename` | `deterministic_repair` | Remove prefix |
| `typed_relationships` | `diagnostic` | Informational |
| `pc_identity_mismatch` | `human_repair` | Needs correct identity |
