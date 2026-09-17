# Data Model: Agent-Safe Wiki Operations

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## Entities

### PageIdentity

The resolved identity of a wiki page, produced by the identity resolution layer. Classifies a page as unambiguously resolved, ambiguously duplicated, or distinctly separate from candidates.

```json
{
  "path": "entities/faction/fisks-fleet.md",
  "stem": "fisks-fleet",
  "title": "Fisk's Fleet",
  "type": "faction",
  "lifecycle": "proposed",
  "aliases": ["Fisk's Fleet", "Fisk's Captains"],
  "status": "resolved",
  "candidates": [],
  "signals": {
    "title_match": true,
    "alias_match": true,
    "manifest_provenance": true,
    "qmd_content_similarity": 0.85
  }
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string | yes | Vault-relative path to the canonical page |
| `stem` | string | yes | Filename without extension (kebab-case) |
| `title` | string | yes | Frontmatter `title` value |
| `type` | string | no | Frontmatter `type` value |
| `lifecycle` | string | no | Frontmatter `lifecycle` value |
| `aliases` | list[string] | no | Frontmatter `aliases` + title variations |
| `status` | enum | yes | `resolved` \| `ambiguous` \| `distinct` |
| `candidates` | list[object] | conditional | Other pages that may represent the same entity (required when `ambiguous`) |
| `signals` | object | yes | Identity signals that contributed to classification |

**Status semantics**:
- `resolved`: Unambiguous — one canonical page. Safe for automatic mutation.
- `ambiguous`: Multiple pages may represent the same entity. Blocks automatic mutation. Reports candidates for human decision.
- `distinct`: Page has no identity overlap with any other page. No action needed.

**Validation**:
- `status: ambiguous` requires non-empty `candidates`
- `candidates[].path` must reference existing vault files
- `signals.qmd_content_similarity` is 0.0–1.0 from QMD content similarity

### Scope

A typed specification of which files an operation targets. Accepted by lint, repair, plan, and verification operations.

```json
{
  "kind": "directory",
  "value": "entities/faction",
  "resolved_files": [
    "entities/faction/fisks-fleet.md",
    "entities/faction/chain-council.md"
  ]
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `kind` | enum | yes | `files` \| `directory` \| `entity_type` \| `identity_set` \| `changed` \| `bundle` |
| `value` | string \| list | yes | Kind-specific scope value |
| `resolved_files` | list[string] | yes | Materialized list of vault-relative paths matching the scope |

**Kind semantics**:
| Kind | Value type | Resolution |
|---|---|---|
| `files` | list[string] | Exact file paths |
| `directory` | string | All `.md` files under directory (respecting SKIP_DIRS) |
| `entity_type` | string | All pages with matching frontmatter `type` |
| `identity_set` | list[PageIdentity] | Pages from a resolved identity set |
| `changed` | string | Git diff target (e.g., `HEAD~1`, branch name) |
| `bundle` | string | Bundle name from `rules/bundles.yml` — scope determined by bundle config |

### TemplateContract

Machine-readable schema defining section semantics for a wiki page type. Co-located with templates at `wiki/templates/contracts/<type>.yml`.

```yaml
template: faction.md
type: faction
sections:
  - heading: "{{title}}"
    level: 1
    required: true
  - heading: "At a Glance"
    level: 2
    required: true
  - heading: "At the Table"
    level: 2
    required: true
  - heading: "Current State"
    level: 2
    required: true
  - heading: "Active Agenda"
    level: 2
    when:
      active: required
      dormant: omit
      dissolved: omit
      default: optional
  - heading: "Milestones"
    level: 3
    parent: "Active Agenda"
    required: false
  - heading: "Secondary Agenda"
    level: 3
    parent: "Active Agenda"
    required: false
    note: "Omit unless the faction can genuinely sustain an independent second project"
  - heading: "Assets"
    level: 2
    required: false
  - heading: "People & Structure"
    level: 2
    required: true
  - heading: "Chain of Action"
    level: 3
    parent: "People & Structure"
    required: false
  - heading: "Territory & Touchpoints"
    level: 2
    required: false
  - heading: "Connections"
    level: 2
    required: false
  - heading: "Party"
    level: 3
    parent: "Connections"
    required: false
  - heading: "Signals & Rumors"
    level: 2
    required: false
  - heading: "Running the Faction"
    level: 2
    required: true
  - heading: "Faction Turn"
    level: 2
    when:
      active: optional
      dormant: omit
      dissolved: omit
      default: optional
  - heading: "Current Turn"
    level: 3
    parent: "Faction Turn"
    when:
      active: optional
      dormant: omit
      dissolved: omit
      default: optional
  - heading: "Turn Log"
    level: 3
    parent: "Faction Turn"
    required: false
  - heading: "History"
    level: 2
    required: false
  - heading: "Hidden Agenda"
    level: 2
    required: false
callouts:
  allowed: [narration]
  note: "Faction pages permit only the [!narration] callout form"
frontmatter:
  required: [title, category, tags, sources, created, updated, type, lifecycle, reveal]
  optional: [campaign, visibility, kind, status, scope, region, base, summary, aliases, base_confidence]
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `template` | string | yes | Source template filename |
| `type` | string | yes | Entity type this contract governs |
| `sections` | list[object] | yes | Ordered section definitions |
| `sections[].heading` | string | yes | Expected heading text (`{{title}}` is a placeholder) |
| `sections[].level` | int | yes | Heading level (1–6) |
| `sections[].required` | bool | conditional | Required when no `when` field; static optionality |
| `sections[].when` | dict | conditional | Lifecycle-conditional requirement. Keys are lifecycle values; values are `required` \| `optional` \| `omit` |
| `sections[].parent` | string | no | Parent heading text (for nesting validation) |
| `sections[].note` | string | no | Human-readable context for the requirement |
| `callouts` | object | no | Allowed callout types for this page type |
| `callouts.allowed` | list[string] | yes | Exhaustive list of permitted callout forms |
| `callouts.note` | string | no | Context for the callout restriction |
| `frontmatter` | object | no | Frontmatter field requirements |
| `frontmatter.required` | list[string] | yes | Required fields |
| `frontmatter.optional` | list[string] | no | Known optional fields |

**Section requirement resolution** for a given page:
1. If `when` field exists: look up page's `lifecycle` (or `status`) value. Use the matching key. Fall back to `default`. If no match and no default, treat as `optional`.
2. If `required` field exists: use it directly.
3. `omit` means the section MUST NOT be flagged as missing for this lifecycle.
4. `required` means the section's absence is an error.
5. `optional` means the section's absence produces no finding.

### MutationOp

A typed semantic edit operation with preconditions and atomic application semantics.

```json
{
  "kind": "replace_section",
  "target": "entities/faction/fisks-fleet.md",
  "selector": {
    "heading_path": ["Active Agenda", "Milestones"],
    "content_hash": "a1b2c3d4e5f6..."
  },
  "payload": {
    "content": "* [x] Recruited five captains\n* [ ] Secured letters of marque\n"
  }
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `kind` | enum | yes | Operation type (see table below) |
| `target` | string | yes | Vault-relative path to the target file |
| `selector` | object | yes | How to locate the mutation target within the file |
| `payload` | object | yes | What to write |

**Operation kinds**:
| Kind | Selector | Payload | Description |
|---|---|---|---|
| `replace_section` | `heading_path`, `content_hash` | `content` | Replace section body under a heading path |
| `delete_section` | `heading_path`, `content_hash` | — | Remove a section and its content |
| `insert_section` | `after_heading_path` or `before_heading_path` | `heading`, `level`, `content` | Insert a new section |
| `set_frontmatter` | `field` | `value` | Set or update a frontmatter field |
| `remove_frontmatter` | `field`, `expected_value` | — | Remove a frontmatter field |
| `rewrite_links` | — | `old_target`, `new_target` | Rewrite wikilinks throughout the file |
| `replace_index_entry` | `slug` | `new_entry` | Replace an entry in wiki/index.md |
| `remove_index_entry` | `slug` | — | Remove an entry from wiki/index.md |
| `insert_index_entry` | — | `entry` | Insert a new entry (sorted) into wiki/index.md |
| `update_manifest_identity` | `page_path` | `transition` | Record a page identity transition in manifest |
| `rename_or_merge_page` | — | `canonical_path`, `obsolete_path`, `rewrite_backlinks` (bool) | Merge or rename a page by updating the canonical page, rewriting backlinks, updating index/manifest, and removing the obsolete page without creating a redirect |

**Selector fields**:
| Field | Type | Description |
|---|---|---|
| `heading_path` | list[string] | Ordered heading texts from root to target |
| `content_hash` | string | SHA-256 hex digest of the current section content (precondition) |
| `field` | string | Frontmatter field name |
| `expected_value` | string | Expected current value (precondition for remove) |
| `slug` | string | Wikilink slug for index operations |

**Precondition verification**:
1. Target file must exist (or not exist for insert operations).
2. `content_hash` must match current section content.
3. `heading_path` must resolve to exactly one section.
4. For overlapping mutations in a transaction: reject before any write.
5. For `expected_value`: must match current value.

### LintFinding (extended)

Extension to 024's Finding schema adding `repair_class` and `repair_action`.

```json
{
  "rule_id": "HARD_broken_links",
  "result": "fail",
  "severity": "REPAIR",
  "location": {
    "file": "entities/faction/fisks-fleet.md",
    "line": 42,
    "text": "[[Old Target]]"
  },
  "evidence": "Wikilink target 'Old Target' does not resolve",
  "reason": "Broken wikilink",
  "evaluator": "deterministic",
  "repair_class": "deterministic_repair",
  "repair_action": {
    "kind": "rewrite_links",
    "target": "entities/faction/fisks-fleet.md",
    "selector": {},
    "payload": {
      "old_target": "Old Target",
      "new_target": "old-target"
    }
  }
}
```

**Extended fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `repair_class` | enum | yes | `diagnostic` \| `human_repair` \| `deterministic_repair` |
| `repair_action` | MutationOp \| null | conditional | Typed mutation operation. Required when `repair_class` is `deterministic_repair`. |

**Repair class semantics**:
- `diagnostic`: Informational only. No action possible or needed.
- `human_repair`: Requires judgment. Finding includes `repair_target` guidance but no typed action.
- `deterministic_repair`: Can be automated. Finding includes a `repair_action` that is a valid MutationOp.

### RepairPlan

An ordered set of typed mutations derived from deterministic lint findings. Previewable as a dry run before application.

```json
{
  "scope": {"kind": "directory", "value": "entities/faction"},
  "source_findings": 12,
  "deterministic_actions": 8,
  "human_only": 4,
  "actions": [
    {
      "finding_rule": "HARD_broken_links",
      "finding_file": "entities/faction/fisks-fleet.md",
      "finding_line": 42,
      "mutation": { "kind": "rewrite_links", "..." : "..." }
    }
  ],
  "hash": "sha256:abcdef..."
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `scope` | Scope | yes | The scope that produced these findings |
| `source_findings` | int | yes | Total findings in the lint run |
| `deterministic_actions` | int | yes | Findings with `deterministic_repair` class |
| `human_only` | int | yes | Findings requiring human judgment |
| `actions` | list[object] | yes | Ordered mutation actions |
| `actions[].finding_rule` | string | yes | Rule that produced the finding |
| `actions[].finding_file` | string | yes | File containing the finding |
| `actions[].finding_line` | int | yes | Line of the finding |
| `actions[].mutation` | MutationOp | yes | The typed mutation to apply |
| `hash` | string | yes | SHA-256 of the serialized actions (for stale-plan detection) |

**Validation**:
- Actions must not contain overlapping mutations for the same file section.
- Hash must be recomputed and compared before application to detect stale plans.
- All mutation preconditions must be verified at application time, not just at plan time.

### Transaction

A bounded set of mutations that apply atomically with deferred finalization.

```json
{
  "id": "tx-2026-09-17-001",
  "mutations": [
    {"kind": "replace_section", "target": "entities/faction/fisks-fleet.md", "...": "..."},
    {"kind": "remove_index_entry", "target": "wiki/index.md", "...": "..."},
    {"kind": "update_manifest_identity", "target": ".manifest.json", "...": "..."}
  ],
  "status": "pending",
  "finalization": {
    "index_updated": false,
    "manifest_updated": false,
    "qmd_refreshed": false
  }
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Transaction identifier |
| `mutations` | list[MutationOp] | yes | Ordered set of mutations |
| `status` | enum | yes | `pending` \| `committed` \| `failed` \| `finalized` |
| `finalization` | object | yes | Derived maintenance status |

**Lifecycle**:
1. `pending`: Mutations accumulated, not yet validated.
2. Validation: Check all preconditions, detect overlaps, resolve selectors.
3. `committed`: All file writes applied atomically (or `failed` on any error).
4. `finalized`: Derived maintenance (index, manifest, QMD) completed.

**Finalization** runs once per transaction:
- Index update: Only if any mutation targets index entries.
- Manifest update: Only if any mutation records identity transitions.
- QMD refresh: Always runs after commit (single invocation of `scripts/qmd-maintain.sh`).

### ManifestTransition

A page-level identity transition recorded in the manifest.

```json
{
  "page": "entities/faction/fisks-captains.md",
  "transition": "merged_into",
  "target": "entities/faction/fisks-fleet.md",
  "date": "2026-09-17",
  "reason": "Duplicate faction entity — consolidated to canonical page"
}
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `page` | string | yes | Vault-relative path of the source page |
| `transition` | enum | yes | `merged_into` \| `renamed_to` \| `archived` |
| `target` | string | conditional | Destination page path (required for `merged_into` and `renamed_to`) |
| `date` | string | yes | ISO date of the transition |
| `reason` | string | no | Human-readable explanation |

### PolicyOwner

An entry in the policy ownership registry.

```yaml
- rule: "acceptance_semantics"
  owner: "docs/agents/work.md"
  governs: "When a wiki write requires DM acceptance vs. when an explicit user instruction satisfies the gate"
  consumers:
    - ".agents/skills/faction-design/SKILL.md"
    - ".agents/skills/wiki-ingest/SKILL.md"
```

**Fields**:
| Field | Type | Required | Description |
|---|---|---|---|
| `rule` | string | yes | Short kebab-case name of the policy |
| `owner` | string | yes | Path to the authoritative file |
| `governs` | string | yes | What the policy decides |
| `consumers` | list[string] | no | Files that reference (not restate) this policy |

## State Transitions

### Identity Resolution Flow

```
files_on_disk → identity_scan → classification
                                    ├── resolved  → safe for mutation
                                    ├── ambiguous → blocked (report candidates)
                                    └── distinct  → no action
```

### Mutation Flow

```
read_file → parse_sections → verify_preconditions → resolve_mutations → write_atomically
                                    │                       │
                                    ├── hash mismatch → reject
                                    └── overlap detected → reject entire transaction
```

### Transaction Lifecycle

```
pending → validate → committed → finalize → finalized
              │           │
              └→ failed   └→ failed (rollback writes)
```

### Repair Plan Flow

```
scoped_lint → findings → classify_repair_class → build_plan → preview → apply
                              │                                    │
                              ├── diagnostic: skip                 ├── stale hash: reject
                              ├── human_repair: report only        └── precondition fail: reject
                              └── deterministic: include action
```

## Relationships

```
PageIdentity  1 ──── * MutationOp         (identity resolution gates mutations)
Scope         1 ──── * LintFinding         (scope filters what gets linted)
TemplateContract 1 ──── * LintFinding      (contract defines what conformance checks)
LintFinding   1 ──── 0..1 MutationOp      (deterministic findings produce mutation actions)
RepairPlan    1 ──── * MutationOp          (plan collects deterministic mutations)
Transaction   1 ──── * MutationOp          (transaction groups mutations for atomic apply)
MutationOp    * ──── 1 ManifestTransition  (merge/rename mutations record identity transitions)
PolicyOwner   1 ──── * consumer files      (ownership prevents restated rules)
```
