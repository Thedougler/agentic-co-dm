# Contract: Mutation Operations

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## CLI Surface

### `scripts/wiki-bulk-ops mutate <kind> [options] [--vault <vault>] [--dry-run] [--json]`

Apply a typed semantic mutation to a wiki file.

**Shared options**:
- `--vault`: Vault root (default from config)
- `--dry-run`: Preview the mutation without writing
- `--json`: Structured JSON output

### Section Operations

**replace_section**:
```bash
wiki-bulk-ops mutate replace_section \
  --file entities/faction/fisks-fleet.md \
  --heading-path "Active Agenda" "Milestones" \
  --content-hash a1b2c3d4... \
  --content-file /tmp/new-milestones.md \
  --vault wiki --dry-run --json
```

**delete_section**:
```bash
wiki-bulk-ops mutate delete_section \
  --file entities/faction/fisks-fleet.md \
  --heading-path "Secondary Agenda" \
  --content-hash a1b2c3d4... \
  --vault wiki --json
```

**insert_section**:
```bash
wiki-bulk-ops mutate insert_section \
  --file entities/faction/fisks-fleet.md \
  --after-heading "Running the Faction" \
  --heading "Faction Turn" --level 2 \
  --content-file /tmp/faction-turn.md \
  --vault wiki --json
```

### Frontmatter Operations

**set_frontmatter**:
```bash
wiki-bulk-ops mutate set_frontmatter \
  --file entities/faction/fisks-fleet.md \
  --field lifecycle --value accepted \
  --vault wiki --json
```

**remove_frontmatter**:
```bash
wiki-bulk-ops mutate remove_frontmatter \
  --file entities/faction/fisks-fleet.md \
  --field base_confidence --expected-value 1.0 \
  --vault wiki --json
```

### Page Operations

**rename_or_merge_page**:
```bash
wiki-bulk-ops mutate rename_or_merge_page \
  --obsolete-path entities/faction/fisks-captains.md \
  --canonical-path entities/faction/fisks-fleet.md \
  --rewrite-backlinks \
  --vault wiki --json
```

This operation removes the obsolete file after updating the canonical page, backlinks, index, and manifest. It never creates a redirect stub.

### Index Operations

**replace_index_entry**:
```bash
wiki-bulk-ops mutate replace_index_entry \
  --slug fisks-captains \
  --new-entry '- [[fisks-fleet]] — Five captains privateer fleet. ( #shattered-sea #faction)' \
  --vault wiki --json
```

**remove_index_entry**:
```bash
wiki-bulk-ops mutate remove_index_entry \
  --slug fisks-captains \
  --vault wiki --json
```

### Manifest Operations

**update_manifest_identity**:
```bash
wiki-bulk-ops mutate update_manifest_identity \
  --page entities/faction/fisks-captains.md \
  --transition merged_into \
  --target entities/faction/fisks-fleet.md \
  --vault wiki --json
```

## Output Format

All mutations return:

```json
{
  "status": "applied",
  "kind": "replace_section",
  "target": "entities/faction/fisks-fleet.md",
  "diff": "--- before\n+++ after\n@@ ...",
  "dry_run": false
}
```

**Status values**: `applied`, `rejected`, `dry_run`

**Rejection reasons** (in `error` field):
- `hash_mismatch`: Content hash doesn't match current state
- `selector_not_found`: Heading path or field doesn't exist
- `selector_ambiguous`: Heading path matches multiple sections
- `overlap`: Mutation overlaps with another in the same transaction
- `file_not_found`: Target file doesn't exist
- `identity_ambiguous`: Page identity is ambiguous (blocked by identity resolution)

**Exit codes**: 0 = applied (or dry_run preview), 1 = error, 2 = rejected (precondition failure)

## Precondition Protocol

1. **Read** the target file.
2. **Parse** structure (frontmatter, headings, sections).
3. **Resolve** the selector (heading path → byte range).
4. **Verify** preconditions (content hash, field value, file existence).
5. **Compute** the result (apply mutation to parsed structure).
6. **Validate** invariants (well-formed frontmatter, valid heading nesting).
7. **Write** atomically (via `atomic_write()` — write to temp, rename).

If any step fails, the original file is untouched and a rejection with the reason is returned.

## Library API

```python
from tools.wiki_ops.mutations import (
    MutationOp, apply_mutation, parse_sections, section_hash
)

# Read and hash a section
sections = parse_sections(Path("wiki/entities/faction/fisks-fleet.md"))
target = sections.find(["Active Agenda", "Milestones"])
hash = section_hash(target.content)

# Build and apply a mutation
op = MutationOp(
    kind="replace_section",
    target="entities/faction/fisks-fleet.md",
    selector={"heading_path": ["Active Agenda", "Milestones"], "content_hash": hash},
    payload={"content": "* [x] Done\n"}
)
result = apply_mutation(vault, op, dry_run=True)
```
