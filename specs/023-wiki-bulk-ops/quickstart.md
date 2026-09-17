# Quickstart: Wiki Bulk Operations

**Feature**: 023-wiki-bulk-ops | **Date**: 2026-09-17

## Prerequisites

- Python 3.12+ (project uses 3.14)
- A wiki vault directory with `.md` files (tests use a temp directory)
- No external dependencies

## Validation Scenarios

### 1. Rename — dry run then apply

```bash
# Dry run: see what would change
./scripts/wiki-bulk-ops rename --old korvash --new korveth --dry-run --json --vault wiki

# Verify: output lists file rename + wikilink rewrites, files_modified > 0, no files on disk changed
# Verify: [[Korvash|display]] entries show target rewrite, display preserved

# Apply
./scripts/wiki-bulk-ops rename --old korvash --new korveth --vault wiki

# Verify: wiki/entities/npc/korvash.md no longer exists
# Verify: wiki/entities/npc/korveth.md exists with updated title
# Verify: grep -r 'Korvash' wiki/ --include='*.md' returns zero wikilink hits
# Verify: wiki-lint passes (no broken links)

# Idempotency: run again
./scripts/wiki-bulk-ops rename --old korvash --new korveth --vault wiki --json
# Verify: exit 1 (old-name not found — already renamed)
```

### 2. Rename — collision detection

```bash
# Attempt rename to a name that already exists
./scripts/wiki-bulk-ops rename --old some-npc --new existing-npc --vault wiki
# Verify: exit 1, error message names the collision, zero files changed
```

### 3. Replace — body text only (default safety)

```bash
# Dry run
./scripts/wiki-bulk-ops replace --search "Shattered Sea" --replacement "Sundered Sea" --dry-run --json --vault wiki

# Verify: changes only in body zone, not in frontmatter or wikilink targets
# Verify: [[Shattered Sea]] wikilink targets are NOT changed (safety zone)

# Apply
./scripts/wiki-bulk-ops replace --search "Shattered Sea" --replacement "Sundered Sea" --vault wiki

# Idempotency
./scripts/wiki-bulk-ops replace --search "Shattered Sea" --replacement "Sundered Sea" --vault wiki --json
# Verify: files_modified: 0
```

### 4. Replace — with wikilink targets opted in

```bash
./scripts/wiki-bulk-ops replace --search "Shattered Sea" --replacement "Sundered Sea" --include-links --dry-run --json --vault wiki
# Verify: changes now include wikilink zone entries
```

### 5. Frontmatter — add a field to filtered pages

```bash
# Add connections_reviewed: false to all type: npc pages
./scripts/wiki-bulk-ops frontmatter --action set --field connections_reviewed --value false --filter type=npc --dry-run --json --vault wiki

# Verify: only type: npc pages listed, non-npc pages untouched
# Verify: pages that already have connections_reviewed show no change (idempotent)

# Apply
./scripts/wiki-bulk-ops frontmatter --action set --field connections_reviewed --value false --filter type=npc --vault wiki
```

### 6. Frontmatter — rename a field

```bash
./scripts/wiki-bulk-ops frontmatter --action rename --field relationships --new-field connections --filter type=npc --vault wiki --json
# Verify: old key gone, new key has same value, body unchanged
```

### 7. Error handling — bad UTF-8 file

```bash
# Create a file with invalid encoding in a temp vault
printf '\x80\x81\x82' > /tmp/test-vault/bad.md
./scripts/wiki-bulk-ops replace --search foo --replacement bar --vault /tmp/test-vault --json
# Verify: bad.md appears in records with skipped: true, skip_reason mentions encoding
# Verify: other files processed normally, exit code 2 (partial failure)
```

### 8. Scoped operation — glob filter

```bash
./scripts/wiki-bulk-ops replace --search "old term" --replacement "new term" --glob "entities/npc/*.md" --vault wiki --dry-run --json
# Verify: only files matching the glob are scanned
```

## Running Tests

```bash
cd /Users/nick/agentic-co-dm
python3 -m pytest tests/test_wiki_bulk_ops.py -v
# Or without pytest:
python3 tests/test_wiki_bulk_ops.py
```

## Expected Outcomes

| Scenario | Exit Code | files_modified |
|---|---|---|
| Successful rename | 0 | ≥2 (source + referencing files) |
| Rename collision | 1 | 0 |
| Rename not found | 1 | 0 |
| Replace with matches | 0 | ≥1 |
| Replace no matches | 0 | 0 |
| Idempotent re-run | 0 | 0 |
| File with bad encoding | 2 | ≥0 (others succeed) |
