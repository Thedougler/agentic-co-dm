# CLI Contract: wiki-bulk-ops

**Feature**: 023-wiki-bulk-ops | **Date**: 2026-09-17

## Invocation

```
scripts/wiki-bulk-ops <command> [options]
```

## Global Options

| Flag | Type | Default | Description |
|---|---|---|---|
| `--vault PATH` | path | `$OBSIDIAN_VAULT_PATH` or `wiki/` | Vault directory |
| `--dry-run` | flag | off | Preview changes without writing |
| `--json` | flag | off | Machine-readable JSON output |
| `--glob PATTERN` | string | none | File glob filter (e.g. `entities/npc/*.md`) |
| `--directory DIR` | string | none | Directory scope relative to vault |

## Commands

### `rename`

Rename an entity page and update all wikilink references across the vault.

```
scripts/wiki-bulk-ops rename --old OLD_STEM --new NEW_STEM [--old-title TEXT] [--new-title TEXT] [global opts]
```

| Argument | Required | Description |
|---|---|---|
| `--old` | yes | Current page file stem (without `.md`) |
| `--new` | yes | Target page file stem |
| `--old-title` | no | Also match/update frontmatter title from this value |
| `--new-title` | no | Set frontmatter title to this value (defaults to title-cased `--new`) |

**Behavior**:
1. Locate `OLD_STEM.md` in the vault (error if zero or multiple matches)
2. Verify `NEW_STEM.md` does not exist (error on collision)
3. Scan all `.md` files for wikilinks referencing `OLD_STEM`
4. In source file: rename to `NEW_STEM.md`, update frontmatter `title`
5. In all files: rewrite `[[OLD_STEM]]` → `[[NEW_STEM]]`, `[[OLD_STEM|X]]` → `[[NEW_STEM|X]]`, `![[OLD_STEM]]` → `![[NEW_STEM]]`, path-qualified variants
6. Body text occurrences of old title outside wikilinks are not changed (body text is prose; only structural references are rewritten)

**Exit codes**: 0 success, 1 validation error (collision, not found), 2 partial failure

### `replace`

Bulk find-and-replace across matching files with markdown safety zones.

```
scripts/wiki-bulk-ops replace --search TEXT --replacement TEXT [--regex] [--include-frontmatter] [--include-links] [global opts]
```

| Argument | Required | Description |
|---|---|---|
| `--search` | yes | Text to find (literal unless `--regex`) |
| `--replacement` | yes | Replacement text |
| `--regex` | no | Treat `--search` as Python regex |
| `--include-frontmatter` | no | Also replace inside YAML frontmatter |
| `--include-links` | no | Also replace inside wikilink targets |

**Behavior**:
1. For each file in scope, split into zones: frontmatter, wikilink targets, body
2. Replace in body zone by default; opt-in to other zones via flags
3. Refuse if replacement would create empty wikilinks `[[]]`
4. Report per-file changes with line numbers

**Exit codes**: 0 success, 1 validation error, 2 partial failure

### `frontmatter`

Bulk frontmatter field mutations on pages matching a filter.

```
scripts/wiki-bulk-ops frontmatter --action ACTION --field KEY [--value VAL] [--new-field KEY] [--filter KEY=VAL] [global opts]
```

| Argument | Required | Description |
|---|---|---|
| `--action` | yes | `set`, `rename`, or `remove` |
| `--field` | yes | Target frontmatter key |
| `--value` | for `set` | Value to set |
| `--new-field` | for `rename` | New key name |
| `--filter` | no | Frontmatter predicate, repeatable (e.g. `--filter type=npc`) |

**Behavior**:
1. Scan files matching scope + frontmatter filter
2. `set`: add key if missing, update if present
3. `rename`: replace key, preserve value
4. `remove`: delete key if present
5. Validate resulting YAML remains parseable

**Exit codes**: 0 success, 1 validation error, 2 partial failure

## Output Format

### Text (default)

```
rename: korvash → korveth
  wiki/entities/npc/korvash.md → wiki/entities/npc/korveth.md (renamed)
  wiki/entities/npc/korveth.md:3  title: Korvash → title: Korveth
  wiki/journal/Session-05-Recap.md:12  [[Korvash]] → [[Korveth]]
  wiki/journal/Session-05-Recap.md:28  [[Korvash|the orc]] → [[Korveth|the orc]]

3 files scanned, 2 files modified, 0 skipped, 4 changes
```

### JSON (`--json`)

```json
{
  "command": "rename",
  "dry_run": false,
  "files_scanned": 3,
  "files_modified": 2,
  "files_skipped": 0,
  "total_changes": 4,
  "records": [
    {
      "file": "entities/npc/korveth.md",
      "changes": [
        {"line": 0, "old": "entities/npc/korvash.md", "new": "entities/npc/korveth.md", "zone": "filename"},
        {"line": 3, "old": "title: Korvash", "new": "title: Korveth", "zone": "frontmatter"}
      ],
      "skipped": false
    },
    {
      "file": "journal/Session-05-Recap.md",
      "changes": [
        {"line": 12, "old": "[[Korvash]]", "new": "[[Korveth]]", "zone": "wikilink"},
        {"line": 28, "old": "[[Korvash|the orc]]", "new": "[[Korveth|the orc]]", "zone": "wikilink"}
      ],
      "skipped": false
    }
  ]
}
```

## Idempotency

Every command is idempotent. A second invocation with the same arguments after a successful first run produces `files_modified: 0` and exit code 0.
