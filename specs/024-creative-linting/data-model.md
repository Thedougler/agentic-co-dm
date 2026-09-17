# Data Model: Creative Linting

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Entities

### Rule

The canonical definition of a lint rule. Lives in `rules/registry.yml` (PyYAML-parsed). Each entry owns the rule's identity, metadata, and behavior contract. For static rules, the executable evaluator is the corresponding Vale YAML in `styles/CoDM/<id>.yml`.

```yaml
id: AGENCY001                  # Stable ID: CATEGORY + zero-padded number
title: "Authored PC decision"  # Human-readable name
category: agency               # Family: wiki | canon | temporal | agency | retrieval | scene | diversity
scope: content                 # What the rule examines: content | frontmatter | corpus | file
severity: BLOCK                # Inherent severity: BLOCK | REPAIR | REVIEW | WARN | INFO
evaluator: vale                # Evaluator type: vale | symbolic | retrieval | semantic | human
lifecycle: ACTIVE              # DRAFT | SHADOW | ACTIVE
vale_style: "CoDM/AGENCY001"  # Vale style reference (evaluator: vale only)
message: "Narration authors a player-character decision"
repair: "Rewrite to describe the situation without prescribing the PC's response"
tags: [player-agency, narration]
conflicts: []                  # Rule IDs this may conflict with
depends: []                    # Rule IDs that must pass first
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable ID: `CATEGORY` + zero-padded number (e.g., `AGENCY001`) |
| `title` | string | yes | Human-readable rule name |
| `category` | enum | yes | `wiki` \| `canon` \| `temporal` \| `agency` \| `retrieval` \| `scene` \| `diversity` |
| `scope` | enum | yes | `content` \| `frontmatter` \| `corpus` \| `file` |
| `severity` | enum | yes | `BLOCK` \| `REPAIR` \| `REVIEW` \| `WARN` \| `INFO` |
| `evaluator` | enum | yes | `vale` \| `symbolic` \| `retrieval` \| `semantic` \| `human` |
| `lifecycle` | enum | yes | `DRAFT` \| `SHADOW` \| `ACTIVE` |
| `vale_style` | string | conditional | Vale style path (required when `evaluator: vale`) |
| `message` | string | yes | Finding message template |
| `repair` | string | no | Repair guidance for agents |
| `tags` | list[string] | no | Classification tags |
| `conflicts` | list[string] | no | IDs of rules that may conflict |
| `depends` | list[string] | no | IDs of prerequisite rules |

**Validation rules**:
- `id` must be unique across the entire registry
- `id` format: `^[A-Z]+\d{3}$`
- `severity` ceiling for `category: scene` and `category: diversity` is `WARN`
- `vale_style` must reference an existing file when `evaluator: vale`
- `conflicts` and `depends` must reference valid rule IDs

### Finding

A structured result from evaluating a rule against content. Produced by all evaluator types. This is the universal output contract.

```json
{
  "rule_id": "AGENCY001",
  "result": "fail",
  "severity": "BLOCK",
  "location": {
    "file": "wiki/journal/sessions/shattered-sea/12/Session-12-01-The-Arrival.md",
    "line": 42,
    "col": 5,
    "end_line": 42,
    "end_col": 38,
    "text": "You decide the risk is worth it"
  },
  "evidence": "Pattern match: 'You decide' — authored PC decision",
  "reason": "Narration authors a player-character decision",
  "repair_target": "Rewrite to describe the situation without prescribing the PC's response",
  "evaluator": "vale",
  "waiver": null
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `rule_id` | string | yes | Stable rule ID |
| `result` | enum | yes | `pass` \| `fail` \| `abstain` |
| `severity` | enum | yes | Effective severity (after bundle gate) |
| `location` | object | yes | File path, line, column, matched text |
| `location.file` | string | yes | Relative path from vault root |
| `location.line` | int | yes | 1-based line number |
| `location.col` | int | no | 1-based column |
| `location.end_line` | int | no | End line for multi-line matches |
| `location.end_col` | int | no | End column |
| `location.text` | string | no | Matched text excerpt |
| `evidence` | string | yes | What triggered the finding |
| `reason` | string | yes | Why this is a finding |
| `repair_target` | string | no | Repair guidance |
| `evaluator` | string | yes | Which evaluator produced this |
| `waiver` | object \| null | no | Waiver metadata if suppressed |

### Bundle

A named collection of rule categories scoped to a task type. Determines which rules run and at what effective severity.

```yaml
session-prep:
  description: "Rules for session preparation output"
  block: [agency, canon, wiki]
  review: [retrieval, temporal]
  diagnostics: [scene, diversity]
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Bundle identifier (e.g., `session-prep`) |
| `description` | string | no | Human-readable description |
| `block` | list[string] | yes | Categories whose rules enforce at BLOCK/REPAIR |
| `review` | list[string] | no | Categories enforced at max REVIEW |
| `diagnostics` | list[string] | no | Categories enforced at max WARN |

**Severity gate logic**: A rule's effective severity in a bundle = `min(rule.severity, gate_ceiling)` where `gate_ceiling` is BLOCK for `block` categories, REVIEW for `review`, WARN for `diagnostics`. Rules in categories not listed in the bundle are excluded.

### Waiver

A time-boxed suppression of a specific rule for a specific target. Stored in `rules/waivers.json`.

```json
{
  "rule_id": "NPC003",
  "target": "npc:archivist-vel",
  "reason": "Archivist Vel intentionally breaks knowledge boundaries as a plot device",
  "owner": "DM",
  "granted": "2026-09-17",
  "expires": "session-15"
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `rule_id` | string | yes | Rule to waive |
| `target` | string | yes | Scope: `file:<path>`, `npc:<name>`, `session:<N>`, or `*` |
| `reason` | string | yes | Why the waiver is granted |
| `owner` | string | yes | Who approved (e.g., `DM`) |
| `granted` | string | yes | ISO date or session reference |
| `expires` | string | yes | ISO date or session reference. No permanent waivers. |

**Validation**: `expires` is required (reject waivers without it). On evaluation, expired waivers are skipped. Waiver match: `rule_id` exact match AND `target` pattern match against finding location.

### LintResult

Aggregate result from a lint run. Wraps all findings and computes status.

```json
{
  "status": "repair_required",
  "bundle": "session-prep",
  "files_checked": 3,
  "rules_evaluated": 12,
  "findings": [...],
  "summary": {
    "BLOCK": 1,
    "REPAIR": 0,
    "REVIEW": 2,
    "WARN": 3,
    "INFO": 1,
    "waived": 0
  },
  "shadow": [...]
}
```

**Status computation**:
- `repair_required`: any finding at BLOCK or REPAIR severity
- `review_needed`: any REVIEW finding and no BLOCK/REPAIR
- `clean`: only WARN/INFO findings (or no findings)

### ConsolidationPlan


A deterministic, reviewable set of safe structural repair actions derived from one lint snapshot. It is emitted by `wiki-lint --consolidate` before any write.

```json
{
  "vault": "wiki",
  "snapshot": "sha256:…",
  "actions": [
    {
      "kind": "fix_broken_link",
      "file": "entities/example.md",
      "line": 12,
      "before": "[[OldTarget]]",
      "after": "[[new-target]]"
    }
  ],
  "requires_approval": true,
  "approved": false
}
```

**Validation rules**:
- `actions` must be deterministic for an unchanged lint snapshot.
- `requires_approval` is always `true` for a write-capable plan.
- `approved: true` is valid only when the command received explicit `--approve` and the current lint snapshot still matches.
- No action may invent canon, merge pages, or rewrite judgment-only content.


## State Transitions

### Rule Lifecycle

```
DRAFT → SHADOW → ACTIVE
```

- **DRAFT**: Rule defined but not evaluated. Visible via `wiki-lint rule <ID>`.
- **SHADOW**: Rule evaluates and records telemetry but findings are excluded from agent-facing output. Promotion requires measured precision.
- **ACTIVE**: Rule evaluates and findings appear in output.

Creative-diagnostic rules (`category: scene`, `category: diversity`) cannot exceed WARN severity at any lifecycle stage.

### Waiver Lifecycle

```
granted → active → expired
```

Waivers are active between `granted` and `expires` dates/sessions. Expired waivers remain in the JSON file for audit trail but are not matched.

## Relationships

```
Rule  1 ──── * Finding       (a rule produces zero or more findings per run)
Rule  * ──── * Bundle         (rules belong to bundles via category membership)
Rule  1 ──── 0..1 Vale YAML   (static rules have a Vale style file)
Finding 1 ──── 0..1 Waiver    (a finding may be suppressed by a waiver)
Bundle 1 ──── * Rule          (a bundle includes rules from its listed categories)
```
