# Data Model: PC Page Redesign

## PC owner page

The canonical record for one player character is `wiki/entities/pc/<kebab-slug>.md` with `type: pc`.

### Frontmatter

| Field | Required | Meaning and validation |
|---|---:|---|
| `title` | yes | Display name; may contain spaces/apostrophes. |
| `category` | yes | `entities`. |
| `tags` | yes | Existing campaign/type tags; preserve them. |
| `sources` | yes | All evidence supporting the page, including archived satellites; preserve lineage. |
| `created` / `updated` | yes | Existing dates; update only as normal file maintenance. |
| `type` | yes | Exactly `pc`. |
| `lifecycle` | yes | Existing value; structure-only conformance does not change it. |
| `reveal` | yes | Existing value; structure-only conformance does not change it. |
| `campaign` / `visibility` | yes | Existing campaign and audience; preserve them. |
| `summary` | yes | One concise DM-readable sentence. |
| `player` | yes for a live PC | Player handle only; never real-player PII. |
| `class_levels` | yes when known | Human-readable single- or multiclass levels. |
| `level`, `ac`, `hp_max`, `init_mod`, `pp` | yes when known | Scalar identity/reference values. Unknown values remain explicit unknowns. |
| `speed` | yes when known | Walk and conditional movement as a string. |
| `status` | yes when known | Existing character status; do not infer a change. |
| `aliases`, `foundry_id`, `provenance`, `base_confidence`, `tier`, `lifecycle_changed` | optional | Preserve when present; omit when absent. |

`ac`, `hp_max`, `init_mod`, `pp`, and `speed` are machine-readable mirrors of the Sheet combat skim. The Sheet is the human-readable authority. Current HP is state in the Sheet, not a new identity field.

## PC section spine

A filed page uses one H1 and this ordered semantic spine:

1. Player-safe `Narration` callout.
2. `At a Glance` with player, class/level, home ship or current base, and the DM thesis.
3. `Connections` with named links and table consequences when ties exist.
4. `Sheet` with ability scores/modifiers/saves, skills, and the combat skim.
5. `Combat Profile` with behavior, counters, dependencies, and synergy when useful.
6. `Abilities` with only populated `Traits`, `Features`, `Actions`, `Bonus Actions`, `Reactions`, and `Feats` subsections.
7. Conditional `Spells` with only populated casting, cantrip, prepared/known, and slot/resource subsections.
8. `Inventory` with only populated attuned, carried, stowed, and currency subsections.
9. Conditional `Session Log` with concise dated or session-numbered changes.
10. Conditional `Art` with existing approved embeds.

There is deliberately no `Voice` section. Existing voice-script material is retained as source evidence; only decision-relevant behavior or mechanical constraints move into the existing thesis, Connections, or Abilities homes.

## Scan layout

- `At a Glance` and `Connections` form the identity/orientation pair.
- `Sheet` and `Combat Profile` form the mechanical scan pair.
- Each pair uses nested fenced `col` / `col-md` blocks with the parent fence longer than child fences.
- Narration stays outside column fences.
- Headings inside child columns and ordinary tables preserve a linear fallback.
- Abilities, Spells, Inventory, Session Log, and Art remain full-width.

## Source satellite and conformance record

Archived facet pages are evidence attached through `sources`, not entities in the live PC representation. Conformance maps each fact to exactly one destination:

- PC numbers and current state → `Sheet`.
- Feature/action use and recovery → `Abilities`.
- Spell calculations and slots → `Spells`.
- Item ownership and location → `Inventory`, with item-owner links.
- Relationship and pressure → `Connections` or the DM thesis.
- Durable session changes → `Session Log`.
- Approved identity art → `Art`.
- Mechanical or source disagreement → the affected home with an explicit `[verify]` marker and source reference.
- Player-performance voice choices → source evidence only unless they change a ruling or relationship.

## Relationships

- A PC links to named party members, ships, factions, places, items, and spells with Obsidian wikilinks.
- The PC page states the relationship or table consequence; the linked owner retains the detailed fact.
- An absent owner remains an explicit unresolved link or stated unknown under current wiki rules.
- A source satellite may support the owner page but must not be linked or presented as a second live PC page.

## Invariants

1. Every live PC owner has `type: pc` under `wiki/entities/pc/` and valid required frontmatter.
2. Each conformed page has one H1 and no nested facet-title H1 dump.
3. No optional section or subsection is left empty or as a placeholder table.
4. No player-safe narration contains secrets, DCs, unearned names, or DM-only thesis.
5. Exact numbers have one readable body home; frontmatter mirrors only the specified identity values.
6. Conflicts and unknowns remain explicit; conformance never silently changes campaign facts or lifecycle fields.
7. No `Voice` heading or DM voice-performance instruction appears on a filed PC page.
8. Columns are presentation hints; headings and tables alone remain sufficient for agent parsing and linear reading.
