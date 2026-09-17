# Data Model: Wiki Bulk Operations

**Feature**: 023-wiki-bulk-ops | **Date**: 2026-09-17

## Entities

### Operation

A single bulk action invoked by the agent.

| Field | Type | Description |
|---|---|---|
| `command` | `rename` \| `replace` \| `frontmatter` | Which subcommand |
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
