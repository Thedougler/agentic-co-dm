# Finding Schema Contract

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Universal Finding Schema

All evaluator types (Vale, symbolic, retrieval, semantic, human) produce findings conforming to this schema. Consumers MUST NOT depend on evaluator-specific fields.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["rule_id", "result", "severity", "location", "evidence", "reason", "evaluator"],
  "properties": {
    "rule_id": {
      "type": "string",
      "pattern": "^[A-Z]+\\d{3}$",
      "description": "Stable rule ID from the registry"
    },
    "result": {
      "type": "string",
      "enum": ["pass", "fail", "abstain"],
      "description": "pass = no violation. fail = violation found. abstain = evaluator cannot determine."
    },
    "severity": {
      "type": "string",
      "enum": ["BLOCK", "REPAIR", "REVIEW", "WARN", "INFO"],
      "description": "Effective severity after bundle gate application"
    },
    "location": {
      "type": "object",
      "required": ["file"],
      "properties": {
        "file": { "type": "string", "description": "Path relative to vault root" },
        "line": { "type": "integer", "minimum": 1 },
        "col": { "type": "integer", "minimum": 1 },
        "end_line": { "type": "integer", "minimum": 1 },
        "end_col": { "type": "integer", "minimum": 1 },
        "text": { "type": "string", "description": "Matched text excerpt" }
      }
    },
    "evidence": {
      "type": "string",
      "description": "What triggered the finding — pattern match, cross-reference, etc."
    },
    "reason": {
      "type": "string",
      "description": "Why this is a finding — the rule's message"
    },
    "repair_target": {
      "type": ["string", "null"],
      "description": "Repair guidance for agents. Null when no repair available."
    },
    "evaluator": {
      "type": "string",
      "enum": ["vale", "symbolic", "retrieval", "semantic", "human", "lint_wiki"],
      "description": "Which evaluator produced this finding"
    },
    "waiver": {
      "type": ["object", "null"],
      "description": "Waiver metadata if finding is suppressed. Null when no waiver applies.",
      "properties": {
        "rule_id": { "type": "string" },
        "target": { "type": "string" },
        "reason": { "type": "string" },
        "expires": { "type": "string" }
      }
    }
  }
}
```

## Vale Output Mapping

Vale `--output=JSON` produces:

```json
{
  "path/to/file.md": [
    {
      "Action": { "Name": "", "Params": [] },
      "Check": "CoDM.AGENCY001",
      "Description": "",
      "Line": 42,
      "Link": "",
      "Message": "Narration authors a player-character decision: 'You decide the risk is worth it'",
      "Severity": "error",
      "Span": [5, 38],
      "Match": "You decide the risk is worth it"
    }
  ]
}
```

**Mapping**:
| Vale field | Finding field | Transform |
|---|---|---|
| `Check` | `rule_id` | Strip `CoDM.` prefix |
| — | `result` | Always `fail` (Vale only reports violations) |
| `Severity` | — | Ignored; use registry severity + bundle gate |
| `Line` | `location.line` | Direct |
| `Span[0]` | `location.col` | Direct |
| `Span[1]` | `location.end_col` | Direct |
| file key | `location.file` | Relative to vault |
| `Match` | `location.text` | Direct |
| `Message` | `evidence` | Direct |
| — | `reason` | From registry `message` |
| — | `repair_target` | From registry `repair` |
| — | `evaluator` | `"vale"` |

## lint_wiki.py Finding Wrapping

Existing `tools/lint_wiki.py` findings are optionally wrapped into this schema for unified output. The wrapper maps:

| lint_wiki.py field | Finding field |
|---|---|
| finding key (e.g., `broken_links`) | `rule_id`: `WIKI001` for missing_frontmatter, `RETRIEVAL001` for broken_links, etc. |
| `page` | `location.file` |
| `target` / `value` | `evidence` |
| — | `severity`: BLOCK for HARD keys, REVIEW for soft |
| — | `evaluator`: `"lint_wiki"` |

This wrapping is opt-in — the existing `wiki-lint` (no subcommand) output is unchanged.
