# Contract: Template Conformance

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## Template Contract Files

Location: `wiki/templates/contracts/<type>.yml`

One YAML file per entity type. Derived from the corresponding template but adds machine-readable section semantics.

## CLI Surface

### `wiki-lint --scope <scope> [--no-template] [--vault <vault>] [--json]`

Run template conformance lint against pages in scope. Template conformance runs by default.

**Input**:
- `--scope`: Scope specification
- `--no-template`: Disable template conformance checking (default: enabled; uses `type` frontmatter to select contract)
- `--vault`: Vault root
- `--json`: Structured JSON output

**Output** (JSON):
```json
{
  "status": "findings",
  "scope": {"kind": "directory", "value": "entities/faction"},
  "files_checked": 31,
  "template_used": "wiki/templates/contracts/faction.yml",
  "findings": [
    {
      "rule_id": "TMPL_missing_required",
      "file": "entities/faction/chain-council.md",
      "severity": "REPAIR",
      "section": "Running the Faction",
      "repair_class": "human_repair",
      "reason": "Required section 'Running the Faction' is missing"
    }
  ],
  "summary": {
    "missing_required": 2,
    "disallowed_callout": 1,
    "missing_frontmatter": 0,
    "lifecycle_exempt": 5
  }
}
```

**Exit codes**: 0 = clean, 1 = error, 2 = findings

## Conformance Rules

### Section Presence

For each section in the contract:

1. Resolve requirement using the page's `lifecycle` (or `status`) value:
   - `when` field → look up lifecycle value → `required` | `optional` | `omit`
   - `required: true/false` → static requirement
2. Check whether the heading exists in the page:
   - Missing + `required` → finding (`TMPL_missing_required`)
   - Missing + `optional` → no finding
   - Missing + `omit` → no finding (lifecycle exemption, counted in summary)
   - Present + `omit` → no finding (having extra sections is not an error)

### Callout Validation

If the contract specifies `callouts.allowed`:
- Scan page body for `> [!type]` patterns
- Any callout type not in the allowed list → finding (`TMPL_disallowed_callout`)

### Frontmatter Validation

If the contract specifies `frontmatter.required`:
- Check each required field exists in the page's frontmatter
- Missing required field → finding (`TMPL_missing_frontmatter`)

## Template Contract Derivation

New contracts are created manually (not auto-generated) by reading the template and its scaffold comments. The key derivation rules:

1. Comments containing "Omit", "omit", "unused", "if unused" → section is `optional`.
2. Comments containing lifecycle conditions (e.g., "Omit this entire section for dormant or dissolved factions") → section gets a `when` field.
3. All remaining sections with substantive scaffold content → `required`.
4. Callout forms mentioned in template comments (e.g., "Faction pages permit only the [!narration] callout form") → `callouts.allowed`.

## Relationship to TemplateProfile (024)

024's `TemplateProfile` (in `tools/creative_lint/template_profile.py`) auto-derives heading trees at runtime. This contract layer replaces auto-derivation with explicit, auditable YAML contracts for the subset of templates where section optionality matters (primarily entity types with lifecycle-conditional sections). The two are complementary:

- `TemplateProfile`: Runtime derivation for basic structure checks. Works for any template without a contract.
- `TemplateContract`: Explicit semantics for lifecycle-conditional, callout-restricted, and complex templates.

When a contract exists, template conformance uses the contract. When no contract exists, it falls back to the profile.

## Library API

```python
from tools.wiki_ops.template_contracts import load_contract, check_conformance

contract = load_contract(vault / "templates" / "contracts" / "faction.yml")
findings = check_conformance(page_path, page_text, contract)
```
