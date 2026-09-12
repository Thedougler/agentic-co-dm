---
name: obsidian-bases
description: Obsidian Bases (.base files), Obsidian's native database layer, for a Campaign OS repo (vault/dashboards/ present). Use when creating/editing a dynamic table/card/list view over vault notes, writing filters/formulas/summaries, or an overview page embedding a base instead of a hand-written table. Not Dataview syntax.
---

# Obsidian Bases: Obsidian's Database Layer

Obsidian Bases (launched 2025) turns vault notes into queryable, dynamic views. Tables,
cards, lists. Defined in `.base` files. No plugin required — it is a core Obsidian feature
(requires Obsidian v1.9.10+).

Official docs: https://help.obsidian.md/bases/syntax

---

## File Format

`.base` files contain valid YAML. The root keys are `filters`, `formulas`,
`properties`, `summaries`, and `views`.

```yaml
# Global filters: apply to ALL views
filters:
  and:
    - file.inFolder("vault/")
    - 'status != "retired"'

# Computed properties
formulas:
  age_days: '(now() - file.ctime).days.round(0)'
  status_icon: 'if(status == "canon", "✅", "🔄")'

# Display name overrides for properties panel
properties:
  status:
    displayName: "Status"
  formula.age_days:
    displayName: "Age (days)"

# One or more views
views:
  - type: table
    name: "All Pages"
    order:
      - file.name
      - type
      - status
      - touched
      - formula.age_days
```

Filters, formulas, and full view-type examples: `references/filters.md`,
`references/formulas.md`, `references/view-types.md`.

---

## Properties

Three types:
- **Note properties**: from frontmatter — `status`, `type`, `updated`
- **File properties**: metadata — `file.name`, `file.mtime`, `file.size`, `file.ctime`, `file.tags`, `file.folder`
- **Formula properties**: computed — `formula.age_days`

### Property name conventions — a silent-failure gotcha

Which contexts need the `note.` prefix and which take the bare name:

| Context | Form |
|---|---|
| `properties:` keys | `note.<prop>` |
| `filters:` expressions | `note.<prop>` |
| `formulas:` expressions | `note.<prop>` |
| `order:` values | `<prop>` (bare) |
| `groupBy.property:` | `<prop>` (bare) |

`file.name` and `formula.<name>` keep their own prefix in every context.

---

## Embedding in Notes

```markdown
![[MyBase.base]]

![[MyBase.base#View Name]]
```

Vault-specific dashboard recipes: `references/wiki-templates.md`.

---

## When to Use Bases

Bases are **canonical infrastructure**, not optional visualizations. They are the primary
mechanism for keeping overview and aggregation pages DRY (vault/CLAUDE.md rule 8: a fact
lives on exactly one page — a static table duplicates frontmatter that already lives on
each entity's own page).

### Decision Tree

| Content type | Use | Example |
|---|---|---|
| List/roster/table of entities with status, counts, or other frontmatter fields | **Base embed** | `![[npcs.base]]`, `![[factions.base]]` |
| A specific entity's summary, lore excerpt, or read-aloud block shared across pages | **Section embed** (`![[Entity#Section]]`) | `![[Pearl-of-Souls#Lore]]` |
| Cross-reference where the reader navigates to the full page | **Wikilink** (`[[Entity]]`) | `[[The-Dravosi-Crown]]` |
| Content unique to this page, not derivable from entity frontmatter or sections | **Static text** | GM-only commentary, cross-entity synthesis |
| A hand-written table listing entity names + their status/location | **Replace with base embed** — this is the anti-pattern | Static table → `![[npcs.base]]` |

### When creating or updating overview/aggregation pages

1. **Always check** if a `.base` file already covers the data — reference
   corpora live in `vault/dashboards/`, a campaign's own live state lives
   in `vault/campaigns/<slug>/dashboards/`
2. **If a base exists:** embed it instead of writing a static table
3. **If no base exists and the data is frontmatter-queryable:** create a
   `.base` file in the matching tier (§ Where to Save), then embed it from
   that tier's own hub page
4. **If the data is NOT frontmatter-queryable** (e.g., narrative synthesis): static text
   is acceptable, but keep it compressed to 1–2 sentences with wikilinks

### Bases query frontmatter only

Bases **cannot read markdown body text**. They can only query:
- YAML frontmatter properties (`status`, `type`, `quest_status`, `role`, etc.)
- File metadata (`file.name`, `file.mtime`, `file.ctime`, `file.size`, `file.tags`)
- Computed formulas from the above

This means fields that need to appear in base views **must exist in frontmatter** —
never invent a base filter/column on a field that isn't already declared in the
page's `_templates/<type>.md`.

---

## Where to Save

Two tiers, one file per content type in each:

- **Global reference** — `vault/dashboards/`, embedded from
  `vault/dashboards/wiki-hub.md`. Any campaign-agnostic corpus with
  queryable frontmatter: spells, classes, rules, feats, species,
  backgrounds, craft, lore. `ls vault/dashboards/` for the live set.
- **Per-campaign live state** — `vault/campaigns/<slug>/dashboards/`,
  embedded from that campaign's own `vault/campaigns/<slug>/dm-hub.md`.
  NPCs, locations, quests, factions, items, the party, monsters, ships,
  sessions, the prep queue — anything that's this campaign's own evolving
  state, not shared rules text. Each filter additionally scopes on
  `campaigns.contains("<Campaign Name>")` (or `campaigns.isEmpty()`, since
  most pages omit the key and default to every campaign) so the same
  shared `vault/campaigns/shattered-sea/npcs/`-style folder splits cleanly per campaign. `ls
  vault/campaigns/<slug>/dashboards/` for the live set.

Bases aren't limited to live campaign-state types: any corpus with
queryable frontmatter gets one whenever a Base is a more efficient browse
than the vault's default file explorer — the tier above decides only
*where* it goes.

---

## YAML Quoting Rules

- Formulas with double quotes → wrap in single quotes: `'if(done, "Yes", "No")'`
- Strings with colons or special chars → wrap in double quotes: `"Status: Active"`
- Unquoted strings with `:` break YAML parsing

---

## What NOT to Do

- Do not use `from:` or `where:` — those are Dataview syntax, not Obsidian Bases
- Do not use `sort:` at the root level — sorting is per-view via `order:` and `groupBy:`
- Do not put `.base` files outside the vault — they only render inside Obsidian
- Do not reference `formula.X` in `order:` without defining `X` in `formulas:`

---

## Reference files

| File | Covers |
|---|---|
| `references/filters.md` | Full filter syntax — and/or/not, operators, filter functions |
| `references/formulas.md` | Formula recipes, Duration `.days` rule, null-guarding with `if()` |
| `references/view-types.md` | Table/cards/list view examples, groupBy placement |
| `references/wiki-templates.md` | Ready-made Shattered Sea dashboard/tracker `.base` templates |
