# Wiki Lint — Consolidate Mode

Triggered by `wiki-lint --consolidate`. Switches from report-only to act-and-report — the vault's periodic self-heal cycle.

## Safety Protocol

FR-002 actions apply without `"Apply these N changes? [yes / no / select]"`. If the user asked to merge duplicates, file the merge. Unattended destructive merge without a user ask still confirms (not a Work wait).

**Always dry-run first:**

1. Run all lint checks (deterministic pass + checks 1–14 from [checks.md](checks.md)).
2. Print planned actions as structured list (see Dry-Run Output below).
3. Apply FR-002 actions without `"Apply these N changes? [yes / no / select]"`: broken-link rewrites, required frontmatter, nearest-valid type/lifecycle, template conformance that relocates existing content, kebab remorph, contradiction flags (do not resolve).
4. If the user asked to merge duplicates, file the merge. Ask `"Apply these N changes? [yes / no / select]"` only for unattended merge, tier demotion, and other non-FR-002 actions without a user ask. Selective application honored.
5. Duplicate pages (Check 14) without a user ask stay confirm-gated.

## Pre-Write Snapshot

Check if the vault is a **standalone** Git repository (`git rev-parse --show-toplevel` matches the resolved vault path). If not standalone, skip silently.

If standalone Git repo:
- Clean tree → record `SNAPSHOT_SHA=$(git rev-parse HEAD)`.
- Dirty tree → `git add -A && git commit -m "pre-wiki-lint snapshot"`. If either command fails, abort without writing vault files.
- Record SHA. Include in final report.

Rollback: `git -C "$OBSIDIAN_VAULT_PATH" reset --hard "$SNAPSHOT_SHA" && git -C "$OBSIDIAN_VAULT_PATH" clean -fd`.

## Actions (in order)

### 1. Fix broken wikilinks

Per broken `[[Target]]` from Check 2:
- Search vault for closest fuzzy match (edit distance ≤ 2 or same root word) → rewrite.
- No match or ambiguous → convert to plain text + `<!-- broken link: no match found -->`.
- Never create pages to satisfy broken links.

### 2. Orphan cross-references

Per orphan from Check 1:
- Grep vault for plain-text mentions of title/aliases (case-insensitive).
- Replace mentions with `[[wikilinks]]`. Cap 3 insertions per orphan.

### 3. Lifecycle corrections

Automatic state-machine enforcement (no human judgment required):
- **`draft` → `reviewed`:** `created` > 30d AND `base_confidence > 0.7`. Set `lifecycle: reviewed`, `lifecycle_changed: <today>`, `lifecycle_reason: "auto-promoted by wiki-lint --consolidate: age>30d, confidence>0.7"`.
- **Stale `verified`:** `(today − updated) > 180 days` → add callout at top of body: `> ⚠️ **Stale**: This page was last updated <date>. Verify before relying on it.` Skip if already present. Not a lifecycle transition — `stale` is computed, not stored.
- No other transitions — `reviewed → verified` is human-only.

### 4. Tier demotion

Pages with `tier: supporting` (or unset), 0 incoming links, 90+ days since update → set `tier: peripheral`. Do not demote `tier: core`. List demotions for review.

### 5. Tag normalization

Read `_meta/taxonomy.md` alias map. Replace alias tags with canonical form in frontmatter. Alias fixes only — not a full tag audit.

### 6. Contradiction callouts

Per contradicting pair (Check 5 or `relationships: contradicts`):
- Check if `> ⚠️ Contradiction flagged with [[Other Page]]` callout already exists.
- If not, add at end of "Key Ideas" (or before "Open Questions"). One line. Flag only — do not resolve.

### 7. Write consolidation report

Write `synthesis/consolidation-<YYYY-MM-DD>.md`:

```yaml
---
title: Consolidation Report <YYYY-MM-DD>
category: synthesis
tags: [maintenance, consolidation]
sources: []
summary: Auto-generated consolidation report from wiki-lint --consolidate run on <date>.
lifecycle: draft
lifecycle_changed: <date>
tier: peripheral
created: <ISO timestamp>
updated: <ISO timestamp>
---
```

Sections: Summary (counts per action type), Broken Link Fixes, Cross-References Added, Lifecycle Updates, Tier Demotions, Tag Normalizations, Contradiction Callouts. Each with specific file paths and changes made.

## Dry-Run Output

Numbered list of planned actions, one per line: `[N] <action-type>: <file:line> <change>`. Split the list: FR-002 items apply without confirm; user-asked merges apply; end the unattended non-FR-002 remainder with `Apply these N changes? [yes / no / select by number]`.

## Log Entry

```
- [TIMESTAMP] LINT_CONSOLIDATE links_fixed=N orphans_rescued=M lifecycle_updates=K tier_demotions=D tag_fixes=T contradiction_callouts=C report=synthesis/consolidation-YYYY-MM-DD.md
```
