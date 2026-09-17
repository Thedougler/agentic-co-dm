# Quickstart: Agent-Safe Wiki Operations

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## Prerequisites

- Python 3.14+ (matches `.venv`)
- PyYAML (installed by 024-creative-linting)
- Existing vault at `wiki/` with `.manifest.json`
- Existing scripts: `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, `scripts/manifest.py`
- QMD: `scripts/qmd-maintain.sh` operational

## Validation Scenarios

### Scenario 1: Identity Resolution

**Purpose**: Verify identity resolution detects ambiguity before any repair.

```bash
# Setup: ensure fisks-captains.md (redirect) and fisks-fleet.md exist
python3 scripts/wiki-identity resolve fisks-fleet --vault wiki --json
# Expected: status=resolved, redirects_from includes fisks-captains.md

python3 scripts/wiki-identity scan --scope type:faction --vault wiki --json
# Expected: exit 0 (no ambiguities — fisks-captains is a redirect, not ambiguous)
```

**Verify**: Exit 0, status `resolved`, redirect relationship detected.

### Scenario 2: Scoped Lint

**Purpose**: Verify lint inspects only in-scope files and returns compact output.

```bash
# Scoped to faction directory
python3 scripts/wiki-lint --scope dir:entities/faction --vault wiki --json
# Expected: files_checked ≤ number of files in entities/faction/

# Full vault for comparison
python3 scripts/wiki-lint --vault wiki --json
# Expected: files_checked = all vault pages
```

**Verify**: Scoped run checks fewer files. Output is compact JSON with counts and grouped findings.

### Scenario 3: Template Conformance

**Purpose**: Verify optional sections don't produce false findings.

```bash
# Lint a faction page against the faction template contract
python3 scripts/wiki-lint --scope files:entities/faction/fisks-fleet.md --template --vault wiki --json
# Expected: no TMPL_missing_required for optional sections
# Expected: no findings for lifecycle-exempt sections on non-active factions
```

**Verify**: Zero false-mandatory findings. Only genuinely missing required sections produce errors.

### Scenario 4: Section Mutation with Hash Precondition

**Purpose**: Verify atomic section replacement with stale-hash rejection.

```bash
# Read a section and get its hash
python3 -c "
from tools.wiki_ops.mutations import parse_sections, section_hash
sections = parse_sections('wiki/entities/faction/fisks-fleet.md')
s = sections.find(['Current State'])
print(section_hash(s.content))
"
# Use the hash in a dry-run mutation
python3 scripts/wiki-bulk-ops mutate replace_section \
  --file entities/faction/fisks-fleet.md \
  --heading-path "Current State" \
  --content-hash <hash-from-above> \
  --content-file /tmp/test-content.md \
  --vault wiki --dry-run --json
# Expected: status=dry_run, diff shown

# Now use a wrong hash
python3 scripts/wiki-bulk-ops mutate replace_section \
  --file entities/faction/fisks-fleet.md \
  --heading-path "Current State" \
  --content-hash 0000000000000000 \
  --content-file /tmp/test-content.md \
  --vault wiki --json
# Expected: status=rejected, error=hash_mismatch, exit 2
```

**Verify**: Correct hash → preview works. Wrong hash → rejection, file untouched.

### Scenario 5: Repair Plan and Transaction

**Purpose**: Verify end-to-end lint → plan → apply pipeline.

```bash
# 1. Check identity
python3 scripts/wiki-identity scan --scope type:faction --vault wiki --json

# 2. Scoped lint with plan generation
python3 scripts/wiki-lint --scope dir:entities/faction --plan --vault wiki --json > /tmp/plan.json

# 3. Preview transaction
python3 scripts/wiki-bulk-ops transact --plan-file /tmp/plan.json --vault wiki --json
# Expected: status=preview, all mutations valid

# 4. Apply (requires --approve)
python3 scripts/wiki-bulk-ops transact --plan-file /tmp/plan.json --approve --vault wiki --json
# Expected: status=finalized, QMD refreshed once
```

**Verify**: Plan generates from lint findings. Transaction applies atomically. QMD runs once at the end, not per-file.

### Scenario 6: Index Entry Operation

**Purpose**: Verify structured index operations without regex on the 107KB file.

```bash
# Replace an index entry by slug
python3 scripts/wiki-bulk-ops mutate replace_index_entry \
  --slug fisks-captains \
  --new-entry '- [[fisks-fleet]] — Consolidated fleet page. ( #shattered-sea #faction)' \
  --vault wiki --dry-run --json
# Expected: shows the old entry and the replacement
```

**Verify**: Entry found by slug, replaced without touching other entries.

### Scenario 7: Batched Finalization Count

**Purpose**: Verify QMD refreshes exactly once, not per-file.

```bash
# Create a 3-mutation transaction and count QMD invocations
# (Test harness wraps qmd-maintain.sh with a counter)
python3 -m pytest tests/test_wiki_ops.py::test_batched_finalization -v
# Expected: qmd_refresh_count == 1
```

**Verify**: Single QMD refresh regardless of mutation count.

## Running Tests

```bash
# All wiki-ops tests
python3 -m pytest tests/test_wiki_ops.py -v

# Specific test classes
python3 -m pytest tests/test_wiki_ops.py::TestIdentityResolution -v
python3 -m pytest tests/test_wiki_ops.py::TestMutations -v
python3 -m pytest tests/test_wiki_ops.py::TestTransactions -v
python3 -m pytest tests/test_wiki_ops.py::TestTemplateConformance -v
python3 -m pytest tests/test_wiki_ops.py::TestScopedLint -v

# Error regression tests
python3 -m pytest tests/test_wiki_ops.py -k "regression" -v
```
