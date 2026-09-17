# Quickstart: Creative Linting Validation

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Prerequisites

- Python 3.14 (`.venv`) with project dependencies installed from `pyproject.toml`, including PyYAML 6.x
- Node.js >=22 and npm
- Vale 3.13.0 (`vale --version`)
- Repository `package.json`, `.markdownlint-cli2.jsonc`, and committed `package-lock.json`
- Repository-owned Vale styles under `styles/`
- Repo root as CWD

## Setup

```bash
# Install declared Python project dependencies
.venv/bin/python -m pip install -e .

# Install the pinned local markdownlint-cli2 dependency
npm ci

# Verify the external and local lint tools
vale --version
npm exec -- markdownlint-cli2 --version
# → markdownlint-cli2 0.23.2

# Thin aliases delegate directly to the repository commands.
# `.vale.ini` remains the sole Vale package and path-scope authority.
npm run lint:vale -- --help
npm run lint:markdown -- --help

# Verify existing lint still works
./scripts/wiki-lint --json wiki | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'pages={d[\"scope\"][\"pages\"]}')"
```

## Validation Scenarios

### V1: Rule Registry Loads and Validates

```bash
# Load registry and print rule count
.venv/bin/python -c "
from tools.creative_lint.registry import Registry
r = Registry.load('rules/registry.yml')
errors = r.validate()
print(f'rules={len(r.all_ids())} errors={len(errors)}')
for e in errors: print(f'  {e}')
"
```

**Expected**: `rules=14 errors=0`

### V2: Vale Runs CoDM Style Against a Fixture

```bash
# Run Vale against a should-fail fixture
vale --output=JSON --config=.vale.ini tests/fixtures/creative_lint/AGENCY001/fail_authored_decision.md
```

**Expected**: JSON output containing a finding with `Check: "CoDM.AGENCY001"`.
Fixture scope enables only `CoDM`; wiki pages use the package set declared by `.vale.ini`.

```bash
# Run Vale against a should-pass fixture
vale --output=JSON --config=.vale.ini tests/fixtures/creative_lint/AGENCY001/pass_situation_description.md
```

**Expected**: JSON output with no `CoDM.AGENCY001` findings (normally an empty object for this file).

### V3: wiki-lint task Subcommand

```bash
# Run session-prep bundle against a test file
./scripts/wiki-lint task session-prep tests/fixtures/creative_lint/AGENCY001/fail_authored_decision.md --json
```

**Expected**: JSON with `status: "repair_required"`, at least one AGENCY001 finding at BLOCK severity.

### V4: wiki-lint rule Subcommand

```bash
./scripts/wiki-lint rule AGENCY001
```

**Expected**: Prints rule definition — ID, title, category, severity, evaluator, message, repair guidance, bundle memberships.

### V5: Bundle Resolution

```bash
.venv/bin/python -c "
from tools.creative_lint.registry import Registry
from tools.creative_lint.bundles import BundleRegistry
reg = Registry.load('rules/registry.yml')
bun = BundleRegistry.load('rules/bundles.yml')
b = bun.get('session-prep')
for rule, sev in b.resolve(reg):
    print(f'{rule.id:12s} {sev:8s} (inherent={rule.severity})')
"
```

**Expected**: Rules from agency/canon/wiki categories at their inherent severity. Retrieval/temporal are capped at REVIEW. Scene/diversity are capped at WARN.

### V6: Existing wiki-lint Unchanged

```bash
# Existing default mode still works identically
./scripts/wiki-lint --json wiki | python3 -c "
import sys,json
d = json.load(sys.stdin)
assert 'counts' in d
assert 'hard_fail' in d
print('existing mode OK')
"
```

**Expected**: `existing mode OK` — no regression.

### V7: Finding Schema Conformance

```bash
# All findings from a task run match the schema
./scripts/wiki-lint task corpus wiki --json | .venv/bin/python -c "
import sys, json
data = json.load(sys.stdin)
for f in data.get('findings', []):
    assert 'rule_id' in f
    assert 'result' in f
    assert 'severity' in f
    assert 'location' in f
    assert 'evidence' in f
    assert 'reason' in f
    assert 'evaluator' in f
    print(f'{f[\"rule_id\"]:12s} {f[\"severity\"]:8s} {f[\"location\"][\"file\"]}')
print(f'findings={len(data.get(\"findings\",[]))} schema=valid')
"
```

### V8: Severity Filter

```bash
./scripts/wiki-lint task session-prep wiki --json --severity block,repair | .venv/bin/python -c "
import sys, json
data = json.load(sys.stdin)
for f in data.get('findings', []):
    assert f['severity'] in ('BLOCK', 'REPAIR'), f'unexpected severity {f[\"severity\"]}'
print('severity filter OK')
"
```

### V9: Consolidation Dry Run and Explicit Approval

```bash
# Dry run: emits a structured plan and performs no writes.
./scripts/wiki-lint --consolidate wiki --json

# Apply only after reviewing the plan.
./scripts/wiki-lint --consolidate wiki --json --approve
```

**Expected**:

- The first command reports `status: "dry_run"`, includes ordered safe actions, and leaves the fixture vault unchanged.
- The second command revalidates the findings before writing and reports `status: "applied"` or a clear blocked error.
- Running `./scripts/wiki-lint --json wiki` without `--consolidate` retains report-only behavior.

### V10: Bulk Dirty-File Queue

```bash
# Request the smallest-first dirty-file queue
./scripts/wiki-lint queue --json | .venv/bin/python -c "
import sys, json
data = json.load(sys.stdin)
q = data['queue']
if len(q) >= 2:
    assert q[0]['size'] <= q[1]['size'], 'queue not smallest-first'
for entry in q:
    assert 'file' in entry
    assert 'size' in entry
    assert 'safe_findings' in entry
    assert entry['safe_findings'] > 0
print(f'queue={len(q)} excluded_judgment={data[\"excluded_judgment_only\"]} total={data[\"total_dirty\"]}')
"
```

**Expected**: Queue entries ordered by ascending `size`, each with at least one safe finding. Judgment-only pages excluded from `queue`.

### V11: Template-Conformance Lint

```bash
# Run template conformance against a page with a known template mapping
./scripts/wiki-lint template wiki/entities/npc/example-npc.md --json 2>/dev/null | .venv/bin/python -c "
import sys, json
data = json.load(sys.stdin)
assert 'template' in data, 'missing template field'
assert 'findings' in data, 'missing findings field'
for f in data.get('findings', []):
    assert f['rule_id'].startswith('TMPL'), f'unexpected rule: {f[\"rule_id\"]}'
    assert f['evaluator'] == 'symbolic'
print(f'template={data[\"template\"]} findings={len(data[\"findings\"])}')
" || echo "No NPC page available for template conformance test — create one to validate"
```

**Expected**: Template resolved from page's `type`/`kind` frontmatter. Findings use `TMPL*` rule IDs with `symbolic` evaluator. Profile changes when the template changes.

## Test Suite

```bash
.venv/bin/python -m pytest tests/test_creative_lint.py tests/test_creative_lint_cli.py -v
```

**Expected**: All tests pass. Covers:

- Registry loading and validation
- Duplicate ID rejection
- Severity gates
- Vale adapter JSON mapping
- Symbolic evaluator basics
- Fixture harness with `fail_*.md`, `pass_*.md`, and `ambiguous_*.md` cases for static and symbolic rule families
