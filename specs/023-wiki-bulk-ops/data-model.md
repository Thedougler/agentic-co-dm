# Data Model: Wiki Bulk Operations

**Feature**: 023-wiki-bulk-ops | **Date**: 2026-09-17

## Entities

### Operation

A single bulk action invoked by the agent.

| Field | Type | Description |
|---|---|---|
| `command` | `rename` \| `replace` \| `frontmatter` \| `link-repair` \| `tag-normalize` \| `moc-generate` \| `orphan-report` | Which subcommand |
| `dry_run` | `bool` | If true, report changes without writing |
| `vault` | `Path` | Resolved vault directory |
| `scope` | `Scope` | File filter for this operation |

### Scope

Determines which files an operation targets.

| Field | Type | Default | Description |
|---|---|---|---|
| `glob` | `str \| None` | `None` | Glob pattern relative to vault (e.g. `entities/npc/*.md`) |
| `directory` | `str \| None` | `None` | Directory path relative to vault |
| `fm_filter` | `dict[str, str] \| None` | `None` | Frontmatter key=value filter (e.g. `type=npc`) |

When all are `None`, scope is the entire vault (excluding skip dirs: `.obsidian`, `_archive`, `_raw`, `_readouts`, `_meta`, `templates`, `attachments`).

### RenameParams

| Field | Type | Description |
|---|---|---|
| `old_name` | `str` | Current entity page stem (e.g. `korvash`) |
| `new_name` | `str` | Target page stem (e.g. `korveth`) |
| `old_title` | `str \| None` | If provided, also update frontmatter title from this value |
| `new_title` | `str \| None` | If provided, set frontmatter title to this value |

### ReplaceParams

| Field | Type | Description |
|---|---|---|
| `search` | `str` | Literal text to find |
| `replacement` | `str` | Text to substitute |
| `regex` | `bool` | If true, `search` is a Python regex pattern (default false) |
| `include_frontmatter` | `bool` | If true, also replace in frontmatter zone (default false) |
| `include_links` | `bool` | If true, also replace inside wikilink targets (default false) |

### FrontmatterParams

| Field | Type | Description |
|---|---|---|
| `action` | `set` \| `rename` \| `remove` | What to do with the field |
| `field` | `str` | Target frontmatter key |
| `value` | `str \| None` | Value to set (for `set` action) |
| `new_field` | `str \| None` | New key name (for `rename` action) |

### LinkRepairParams

| Field | Type | Description |
|---|---|---|
| `mapping_file` | `Path \| None` | TSV file with `old_stem\tnew_stem` explicit overrides |
| `use_git` | `bool` | Check git log for rename history (default true) |
| `use_aliases` | `bool` | Check frontmatter `aliases` field (default true) |
| `fuzzy` | `bool` | Attempt fuzzy stem matching for unresolved links (default true) |
| `fuzzy_threshold` | `int` | Max Levenshtein edit distance for fuzzy match (default 2) |

### TagNormalizeParams

| Field | Type | Description |
|---|---|---|
| `taxonomy` | `Path \| None` | Path to taxonomy file (default `_meta/taxonomy.md` in vault) |
| `remove_unknown` | `bool` | If true, remove tags not in taxonomy (default false — report only) |

### MocGenerateParams

| Field | Type | Default | Description |
|---|---|---|---|
| `title_map` | `dict[str, str]` | built-in | Folder name → readable folder title; explicit index-title overrides and an `Index` suffix distinguish navigation pages (e.g. `creature` → "Creature Index") |

No user-supplied parameters beyond global vault. The static title map is internal.

### OrphanReportParams

No additional parameters beyond global scope/vault. Reports pages with zero incoming wikilinks.

### ChangeRecord

Per-file report of what was or would be modified.

| Field | Type | Description |
|---|---|---|
| `file` | `str` | Path relative to vault |
| `changes` | `list[Change]` | Individual changes in this file |
| `skipped` | `bool` | If true, file was skipped |
| `skip_reason` | `str \| None` | Why file was skipped (encoding error, etc.) |

### Change

A single substitution within a file.

| Field | Type | Description |
|---|---|---|
| `line` | `int` | 1-indexed line number |
| `old` | `str` | Original text |
| `new` | `str` | Replacement text |
| `zone` | `str` | `body` \| `frontmatter` \| `wikilink` \| `filename` |

### OperationResult

Top-level output of any operation.

| Field | Type | Description |
|---|---|---|
| `command` | `str` | Which subcommand ran |
| `dry_run` | `bool` | Whether this was a dry run |
| `files_scanned` | `int` | Total files examined |
| `files_modified` | `int` | Files that were (or would be) changed |
| `files_skipped` | `int` | Files skipped (with reasons) |
| `total_changes` | `int` | Sum of individual changes |
| `records` | `list[ChangeRecord]` | Per-file details (only files with changes or skips) |

## State Transitions

None — operations are stateless. Each invocation scans, computes, and optionally writes. Idempotency means a second run produces `files_modified: 0`.

## Validation Rules

- `old_name` must match exactly one existing `.md` file stem in vault (rename refuses on zero or multiple matches)
- `new_name` must not collide with an existing file stem (rename refuses on collision)
- `search` must not be empty
- `replacement` that would produce empty wikilink `[[]]` is refused
- Frontmatter `field` must be a valid YAML key (alphanumeric + underscore + hyphen)
- Files that fail UTF-8 decode are skipped with `skip_reason`, not fatal
- `mapping_file` lines must have exactly two tab-separated columns (lines with wrong format are skipped with warning)
- `fuzzy_threshold` must be 1–5 (default 2)
- `taxonomy` file must exist and be readable when `tag-normalize` is invoked
