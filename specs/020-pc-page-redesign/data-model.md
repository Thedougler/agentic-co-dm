# Data Model: PC Page Redesign

## PC owner page

The canonical record for one player character is `wiki/entities/pc/<kebab-slug>.md` with `type: pc`.

### Frontmatter

| Field | Required | Meaning and validation |
|---|---:|---|
| `title` | yes | Display name; may contain spaces/apostrophes. |
| `category` | yes | `entities`. |
| `tags` | yes | Existing campaign/type tags; preserve them. |
| `sources` | yes | All evidence supporting the page, including archived satellites and ingest sources; preserve lineage. |
| `created` / `updated` | yes | Existing dates; update as normal file maintenance. |
| `type` | yes | Exactly `pc`. |
| `lifecycle` | yes | Existing value; structure-only conformance does not change it. |
| `reveal` | yes | Existing value; structure-only conformance does not change it. |
| `campaign` / `visibility` | yes | Existing campaign and audience; preserve them. |
| `summary` | yes | One concise DM-readable sentence. Not a prescribed play pattern. |
| `player` | yes for a live PC | Player handle only; never real-player PII. |
| `class_levels` | yes when known | Human-readable single- or multiclass levels. |
| `level`, `ac`, `hp_max`, `init_mod`, `pp` | yes when known | Scalar identity/reference values. Unknown values remain explicit unknowns. |
| `speed` | yes when known | Walk and conditional movement as a string. |
| `status` | yes when known | Existing character status; do not infer a change. |
| `aliases`, `foundry_id`, `provenance`, `base_confidence`, `tier`, `lifecycle_changed` | optional | Preserve when present; omit when absent. |

`ac`, `hp_max`, `init_mod`, `pp`, and `speed` mirror Combat Stats. Combat Stats is the human-readable authority. Current HP is state in Combat Stats, not a new identity field.

A newer supplied source that disagrees with a mirrored number overwrites both the body home and the matching frontmatter mirror. Structure-only conformance does not.

## PC section spine

A filed page uses one H1 and this D&D Beyond-ordered spine:

1. Player-safe `Narration` callout.
2. `Identity` — player, class/level, and other DDB identity facts when known (species/race, background). Home ship or current base when known.
3. `Combat Stats` — AC, current/max HP, initiative, passive perception, speed, and related combat numbers when known.
4. `Ability Scores` — STR–CHA scores, modifiers, and saves.
5. `Skills` — known skill bonuses and proficiencies.
6. `Actions` — attacks, actions, bonus actions, reactions; omit empty subsections.
7. Conditional `Spells` — spellcasting, cantrips, prepared/known, slots or other casting resources; omit for a non-caster.
8. `Inventory` — attuned, carried, stowed, currency; omit empty subsections.
9. `Features` — traits, class features, feats; omit empty subsections.
10. `Connections` — named ties and table consequences when ties exist.
11. Conditional `Session Log` — concise dated or session-numbered current-play changes.
12. Conditional `Art` — existing approved embeds.

There is no `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, or required DM thesis. Lists record available options and numbers. They do not script the player's action.

## Scan layout

- `Identity` and `Combat Stats` form the DDB header pair.
- `Ability Scores` and `Skills` form the DDB left-column pair.
- Each required pair uses nested fenced `col` / `col-md` blocks with the parent fence longer than child fences.
- Narration stays outside column fences.
- Headings inside child columns and ordinary tables preserve a linear fallback.
- `Actions`, `Spells`, `Inventory`, `Features`, and `Art` remain full-width.
- `Connections` and `Session Log` MAY use the same column pair when both exist; otherwise they are full-width.

## Source satellite, ingest, and conformance

Archived facet pages are evidence attached through `sources`, not live PC representations.

| Fact kind | Home |
|---|---|
| Identity (player, class/level, species, background, base) | `Identity` |
| Combat numbers and current HP/conditions | `Combat Stats` |
| Ability scores, modifiers, saves | `Ability Scores` |
| Skills and passive perception if not in Combat Stats | `Skills` |
| Attacks, actions, bonus actions, reactions | `Actions` |
| Spell calculations and slots | `Spells` |
| Item ownership and location | `Inventory`, with item-owner links |
| Traits, class features, feats | `Features` |
| Relationship and table consequence | `Connections` |
| Durable session changes | `Session Log` |
| Approved identity art | `Art` |
| Internal one-source disagreement | affected home with `[verify]` and source reference |
| Newer supplied source vs live wiki number | newer source overwrites the wiki number |
| Player-performance voice choices | source evidence only unless they change a ruling or relationship |

Structure-only conformance maps facts into these homes without changing campaign facts or lifecycle. Ingest from a newer PDF, prose, Foundry actor, or other DM-supplied file is not structure-only.

## PC-owning skill

Not a wiki entity. The skill `player-characters` is the sole skill owner for recording `type: pc` pages from supplied source. It is not an NPC design workflow.

State: idle → record (source supplied for a player-created character) → refuse (no source, or a request to invent/generate/prescribe).

## Relationships

- A PC links to named party members, ships, factions, places, items, and spells with Obsidian wikilinks.
- The PC page states the relationship or table consequence; the linked owner retains the detailed fact.
- An absent owner remains an explicit unresolved link or stated unknown under current wiki rules.
- A source satellite may support the owner page but must not be presented as a second live PC page.

## Invariants

1. Every live PC owner has `type: pc` under `wiki/entities/pc/` and valid required frontmatter.
2. Each conformed page has one H1 and no nested facet-title H1 dump.
3. No optional section or subsection is left empty or as a placeholder table.
4. No player-safe narration contains secrets, DCs, unearned names, or DM-only thesis.
5. Exact numbers have one readable body home; frontmatter mirrors only the specified identity values.
6. Structure-only conformance never silently changes campaign facts or lifecycle fields.
7. A newer supplied source overwrites a conflicting wiki number; an internal single-source conflict stays explicit.
8. No `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, or DM voice-performance instruction appears on a filed PC page.
9. Columns are presentation hints; headings and tables alone remain sufficient for agent parsing and linear reading.
10. Agents use `player-characters` for `type: pc` work. They do not use `npc-design` to fill a PC page.
11. The skill does not invent a PC, generate stats, or write the player's actions.
