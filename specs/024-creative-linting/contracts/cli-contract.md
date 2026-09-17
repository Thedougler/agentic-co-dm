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

## Error Handling

| Condition | Behavior |
|---|---|
| Unknown bundle name | Exit 2 with message listing available bundles |
| Unknown rule ID | Exit 2 with message |
| Vale not installed | Skip Vale evaluator, log warning, continue with symbolic only |
| Evaluator unavailable (e.g., no LLM in CI) | Skip rule, record `evaluator_unavailable` status in findings |
| Invalid registry YAML | Exit 2 with parse error |
| Duplicate rule ID in registry | Exit 2 with error identifying the duplicate |
