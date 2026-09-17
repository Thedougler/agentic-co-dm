# CLI Contract: wiki-lint Creative Linting Extensions

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Overview

`scripts/wiki-lint` is extended with subcommands for creative linting. Existing no-subcommand behavior is unchanged.

## Commands

### Existing (unchanged)

```bash
wiki-lint [vault] [--json] [--hard|--all]
```

Delegates to `tools/lint_wiki.py`. Returns structural HARD-key findings. Exit 0 = clean, exit 1 = findings.

### `wiki-lint task <bundle> [path...] [--json] [--severity <levels>]`

Run creative lint rules scoped to a task bundle.

**Input**:
- `bundle`: Bundle name from `rules/bundles.yml` (e.g., `session-prep`, `wiki-ingest`, `corpus`)
- `path...`: Optional file or directory paths to limit scope. Default: vault root.
- `--json`: Structured JSON output (default for agent consumption)
- `--severity block,repair`: Comma-separated severity filter

**Output** (JSON):
```json
{
  "status": "repair_required|review_needed|clean",
  "bundle": "session-prep",
  "files_checked": 3,
  "rules_evaluated": 12,
  "findings": [
    {
      "rule_id": "AGENCY001",
      "result": "fail",
      "severity": "BLOCK",
      "location": {"file": "...", "line": 42, "text": "..."},
      "evidence": "...",
      "reason": "...",
      "repair_target": "..."
    }
  ],
  "summary": {"BLOCK": 1, "REPAIR": 0, "REVIEW": 2, "WARN": 3, "INFO": 1}
}
```

**Output** (human-readable, no `--json`):
```
wiki-lint task session-prep: 3 files, 12 rules → repair_required

BLOCK  AGENCY001  Session-12-01-The-Arrival.md:42  Authored PC decision
       "You decide the risk is worth it"
       Repair: Rewrite to describe the situation without prescribing the PC's response

REVIEW TEMP001   Session-12-02-The-Shrine.md:18   Future knowledge leak
       "As you will discover next session"

WARN   SCENE001  Session-12-01-The-Arrival.md      No actionable situation marker

Summary: BLOCK=1 REPAIR=0 REVIEW=2 WARN=3 INFO=1
```

**Exit codes**: 0 = clean or only WARN/INFO. 1 = BLOCK/REPAIR findings. 2 = REVIEW findings (no BLOCK/REPAIR).

### `wiki-lint file <path> [--json] [--severity <levels>]`

Run all active rules against a single file. Runs both structural (lint_wiki.py) and creative (Vale + symbolic) checks.

**Input**: File path (relative or absolute).
**Output**: Same finding schema as `task`. Bundle context is omitted; all active rules evaluate at their inherent severity.

### `wiki-lint corpus [--json] [--severity <levels>]`

Run corpus-level rules against the entire vault. Includes both structural and creative checks.

### `wiki-lint changed [--json] [--severity <levels>]`

Run rules against files changed since the last commit (`git diff --name-only HEAD`).

### `wiki-lint rule <ID>`

Describe a rule from the registry.

**Output**:
```
AGENCY001: Authored PC decision
Category:  agency
Severity:  BLOCK
Evaluator: vale
Lifecycle: ACTIVE
Scope:     content
Message:   Narration authors a player-character decision
Repair:    Rewrite to describe the situation without prescribing the PC's response
Tags:      player-agency, narration
Bundles:   session-prep (block), live-codm (block), corpus (review)
```

### `wiki-lint --consolidate [vault] [--json] [--approve]`

Generate a safe structural repair plan from the existing lint findings.

**Default behavior** (without `--approve`):
- Re-run the deterministic structural checks.
- Emit a `ConsolidationPlan` containing ordered actions, affected files, and the required approval state.
- Perform no writes.
- Exit 0 when the plan is valid, even when repair actions are available.

**Approved behavior** (`--approve`):
- Re-run the checks before writing.
- Abort with exit 2 if the plan changed since the dry run or contains an unsafe action.
- Apply only safe structural repairs, then emit the applied action list.
- Preserve existing report-only behavior for invocations without `--consolidate`.

**JSON output**:
```json
{
  "status": "dry_run|applied|blocked",
  "plan": {
    "vault": "wiki",
    "snapshot": "sha256:…",
    "actions": [],
    "requires_approval": true,
    "approved": false
  }
}
```

**Exit codes**:
- `0`: dry-run plan emitted or approved repairs applied.
- `1`: underlying lint findings prevent a valid plan.
- `2`: invalid arguments, stale plan, unsafe action, or approval failure.

### `wiki-lint queue [--json]`

Emit the bulk dirty-file queue: wiki pages with remaining safe automatic findings, ordered smallest-first by byte size.

**Input**: No required arguments. Scans the full vault.

**Output** (JSON, `--json`):
```json
{
  "queue": [
    {"file": "entities/npc/example.md", "size": 1234, "safe_findings": 3},
    {"file": "entities/place/bigger.md", "size": 5678, "safe_findings": 1}
  ],
  "excluded_judgment_only": 4,
  "total_dirty": 6
}
```

**Output** (human-readable, no `--json`):
```
wiki-lint queue: 2 pages with safe automatic findings (4 judgment-only excluded)

  1. entities/npc/example.md          1,234 bytes   3 safe findings
  2. entities/place/bigger.md         5,678 bytes   1 safe finding
```

**Queue inclusion**: A page appears when it has at least one finding whose rule has `auto_repair: true` in the registry and a non-null `repair_target`. Pages with only judgment-required findings are excluded.

**Agent workflow**: Take `queue[0]`, apply safe automatic repairs, re-lint that single file to confirm zero safe findings remain, then re-request the queue. Stopping with remaining dirty files is not a failure.

**Exit codes**: 0 = queue emitted (even if non-empty). 2 = invalid arguments or registry error.

### `wiki-lint template <path> [--json]`

Run template-conformance lint against a single page. Resolves the applicable template from the page's `type` and `kind` frontmatter, derives a generic profile, and reports structural/formatting mismatches.

**Input**: File path (relative or absolute).

**Output** (JSON):
```json
{
  "template": "wiki/templates/npc.md",
  "page": "entities/npc/example.md",
  "findings": [
    {
      "rule_id": "TMPL001",
      "result": "fail",
      "severity": "REPAIR",
      "location": {"file": "entities/npc/example.md", "line": 1},
      "evidence": "Missing required section: '## At a Glance'",
      "reason": "Page is missing a section required by template wiki/templates/npc.md",
      "repair_target": "Insert '## At a Glance' section stub after the title heading",
      "evaluator": "symbolic"
    }
  ]
}
```

**Exit codes**: 0 = clean or only INFO findings. 1 = REPAIR findings. 2 = no template resolved or invalid arguments.

## Error Handling

| Condition | Behavior |
|---|---|
| Unknown bundle name | Exit 2 with message listing available bundles |
| Unknown rule ID | Exit 2 with message |
| Vale not installed | Skip Vale evaluator, log warning, continue with symbolic only |
| Evaluator unavailable (e.g., no LLM in CI) | Skip rule, record `evaluator_unavailable` status in findings |
| Invalid registry YAML | Exit 2 with parse error |
| Duplicate rule ID in registry | Exit 2 with error identifying the duplicate |

