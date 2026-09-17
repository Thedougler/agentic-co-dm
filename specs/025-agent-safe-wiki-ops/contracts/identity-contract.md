# Contract: Identity Resolution

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## CLI Surface

### `scripts/wiki-identity resolve <path-or-slug> [--vault <vault>] [--json]`

Resolve the identity of a single page or entity.

**Input**:
- `path-or-slug`: Vault-relative path or filename stem
- `--vault`: Vault root (default from config)
- `--json`: Structured JSON output

**Output** (JSON):
```json
{
  "path": "entities/faction/fisks-fleet.md",
  "status": "resolved",
  "title": "Fisk's Fleet",
  "type": "faction",
  "aliases": ["Fisk's Captains"],
  "redirects_from": ["entities/faction/fisks-captains.md"],
  "signals": {
    "title_match": true,
    "alias_match": true,
    "redirect_match": true,
    "manifest_provenance": true,
    "content_overlap": 0.85
  }
}
```

**Exit codes**: 0 = resolved, 1 = error, 2 = ambiguous (candidates in output)

### `scripts/wiki-identity scan [--scope <scope>] [--vault <vault>] [--json]`

Scan a scope for identity ambiguities.

**Input**:
- `--scope`: Scope specification (e.g., `type:faction`, `dir:entities/faction`, or omit for full vault)
- `--vault`: Vault root
- `--json`: Structured JSON output

**Output** (JSON):
```json
{
  "scanned": 31,
  "resolved": 29,
  "ambiguous": 1,
  "distinct": 1,
  "ambiguities": [
    {
      "candidates": [
        {"path": "entities/faction/fisks-captains.md", "title": "Fisk's Captains"},
        {"path": "entities/faction/fisks-fleet.md", "title": "Fisk's Fleet"}
      ],
      "signals": {"title_similarity": 0.72, "shared_source": true, "redirect_exists": true}
    }
  ]
}
```

**Exit codes**: 0 = no ambiguities, 1 = error, 2 = ambiguities found

## Identity Signals

| Signal | Source | Weight | Description |
|---|---|---|---|
| `title_match` | frontmatter `title` | high | Exact or near-exact title match (case-insensitive, punctuation-normalized) |
| `alias_match` | frontmatter `aliases` | high | One page's title appears in another's aliases |
| `redirect_match` | frontmatter `redirects_to` | definitive | Explicit redirect relationship |
| `manifest_provenance` | `.manifest.json` | medium | Same source produced both pages |
| `type_kind_match` | frontmatter `type`, `kind` | medium | Same entity type and kind |
| `stem_similarity` | filename | low | Levenshtein or SequenceMatcher on kebab-case stems |
| `content_overlap` | body text | medium | SequenceMatcher ratio on body content (excluding frontmatter) |

## Classification Rules

1. If `redirect_match`: source page → `resolved` (redirect to canonical). Canonical page → `resolved`.
2. If `title_match` or `alias_match` AND same `type`: → `ambiguous` (both are candidates).
3. If `content_overlap` > 0.6 AND same `type`: → `ambiguous`.
4. If `manifest_provenance` (same source) AND `stem_similarity` > 0.7: → `ambiguous`.
5. Otherwise: → `distinct`.

Ambiguous results block automatic mutation. The agent must report candidates and wait for human designation of the canonical page.

## Library API

```python
from tools.wiki_ops.identity import resolve_identity, scan_identities

# Single page
result: PageIdentity = resolve_identity(vault, "entities/faction/fisks-fleet.md")

# Scoped scan
results: list[PageIdentity] = scan_identities(vault, scope=Scope(kind="entity_type", value="faction"))
ambiguities = [r for r in results if r.status == "ambiguous"]
```
