# Contract: Transactions and Finalization

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## CLI Surface

### `scripts/wiki-bulk-ops transact --plan-file <plan.json> [--approve] [--vault <vault>] [--json]`

Apply a repair plan as an atomic transaction with deferred finalization.

**Input**:
- `--plan-file`: Path to a JSON repair plan (from `wiki-lint --plan`)
- `--approve`: Required flag to actually write. Without it, validates and previews.
- `--vault`: Vault root
- `--json`: Structured JSON output

**Output** (JSON):
```json
{
  "status": "finalized",
  "mutations_applied": 3,
  "mutations_rejected": 0,
  "files_changed": ["entities/faction/fisks-fleet.md", "entities/faction/fisks-captains.md"],
  "finalization": {
    "index_updated": true,
    "manifest_updated": true,
    "qmd_refreshed": true,
    "qmd_exit_code": 0
  }
}
```

**Without `--approve`**:
```json
{
  "status": "preview",
  "mutations_valid": 3,
  "mutations_invalid": 0,
  "diffs": [
    {"file": "entities/faction/fisks-fleet.md", "diff": "--- a\n+++ b\n..."}
  ]
}
```

**Exit codes**: 0 = success (finalized or preview valid), 1 = error, 2 = validation failure (some mutations rejected)

## Transaction Protocol

### Phase 1: Validate
1. Read all target files.
2. Verify all preconditions (hashes, selectors, identities).
3. Check for overlapping mutations (same file + overlapping byte ranges).
4. If any validation fails: reject entire transaction, report all failures.

### Phase 2: Commit
1. Compute all results (apply mutations in memory).
2. Validate all invariants (well-formed markdown, valid frontmatter).
3. Write all files atomically (temp file → rename, one per target).
4. If any write fails: attempt to restore originals from backup copies made before writes.

### Phase 3: Finalize
1. Index: If any mutation touched index entries, rebuild/update `wiki/index.md`.
2. Manifest: If any mutation recorded identity transitions, update `.manifest.json`.
3. QMD: Run `scripts/qmd-maintain.sh` once.
4. Report compact summary.

### Failure Modes
- **Validation failure**: No files written. All failures reported. Exit 2.
- **Write failure**: Attempt restore of already-written files. Report partial state. Exit 1.
- **Finalization failure**: Files already committed. Report which finalization step failed. Exit 1 with `status: committed` (not `finalized`). Agent can retry finalization.

## Scoped Lint → Repair Plan → Transaction Pipeline

The end-to-end agent workflow:

```bash
# 1. Resolve identity
wiki-identity scan --scope type:faction --vault wiki --json > /tmp/identity.json

# 2. Scoped lint (only if no ambiguities)
wiki-lint --scope dir:entities/faction --vault wiki --json > /tmp/lint.json

# 3. Build repair plan from deterministic findings
wiki-lint --plan --from /tmp/lint.json --json > /tmp/plan.json

# 4. Preview
wiki-bulk-ops transact --plan-file /tmp/plan.json --vault wiki --json

# 5. Apply (with approval)
wiki-bulk-ops transact --plan-file /tmp/plan.json --approve --vault wiki --json
```

## Library API

```python
from tools.wiki_ops.transactions import Transaction

with Transaction(vault) as tx:
    tx.add(MutationOp(kind="replace_section", ...))
    tx.add(MutationOp(kind="remove_index_entry", ...))
    tx.add(MutationOp(kind="update_manifest_identity", ...))
    # Validates, commits, and finalizes on exit
    # Rolls back on exception

# Or manual control:
tx = Transaction(vault)
tx.add(op1)
tx.add(op2)
validation = tx.validate()  # Returns list of failures
if not validation.failures:
    tx.commit()
    tx.finalize()
```
