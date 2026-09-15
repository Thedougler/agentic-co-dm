---
title: "{{title}}"
category: entities
tags: [shattered-sea, pc]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: pc
lifecycle: proposed
reveal: revealed
campaign: shattered-sea
visibility: dm
cssclasses: [pc-sheet]
summary: ""
player: ""
class_levels: ""
level:
ac:
hp_max:
init_mod:
pp:
speed: ""
status: alive
---
<!-- Copy-start scaffold for a canonical type: pc owner page.

Live owner: wiki/entities/pc/<kebab-slug>.md. Flatten archived sheets, abilities,
spells, inventory, combat profiles, galleries, and session logs into these homes;
do not create a second live facet page. Preserve source lineage, aliases, links,
unknowns, and [verify] markers. Omit an optional section or empty subsection.
The player controls this PC. Narration is player-safe; mechanics stay outside it.
Escape alias pipes as \| inside Markdown table cells so wikilinks remain valid.

Portrait + Identity pair: when at least one picture of the character exists,
use the col/col-md pair below. Left col-md holds only the portrait embed.
Right col-md holds ## Identity. When no art exists, remove the col fences
and render ## Identity full-width with no empty portrait column.
-->

# {{title}}

> [!narration] Narration
> Write a complete-sentence, sensory look that is safe to read aloud. Do not include secrets, DCs, or unearned names.

`````col
````col-md
![[portrait-filename.webp]]
````
````col-md
## Identity

| Field | Value |
| --- | --- |
| Player | {{player}} |
| Class / Level | {{class_levels}} |
| Species / Race | |
| Background | |
| Home ship / base | [[ship-or-base]] |
````
`````

## Combat Stats

| Stat | Value |
| --- | --- |
| AC | |
| HP (current / max) | |
| Initiative | |
| Passive Perception | |
| Speed | |

List character-specific resources and counters when known.

````col
```col-md
## Ability Scores

| Ability | Score | Mod | Save |
| --- | --- | --- | --- |
| Strength | | | |
| Dexterity | | | |
| Constitution | | | |
| Intelligence | | | |
| Wisdom | | | |
| Charisma | | | |
```
```col-md
## Skills

List known skill bonuses and proficiencies. Do not duplicate Combat Stats numbers.
```
````

## Actions

Omit empty subsections. Each populated row states effect, uses, and recovery when applicable.

### Attacks

| Attack | To-Hit / DC | Damage / Effect | Notes |
| --- | --- | --- | --- |
| | | | |

### Actions

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
| --- | --- | --- | --- | --- |
| | | | | |

### Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
| --- | --- | --- | --- | --- |
| | | | | |

### Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
| --- | --- | --- | --- | --- |
| | | | | |

## Spells

Include only for a caster or another castable resource. Omit empty subsections and keep multiclass pools distinct.

### Spellcasting

State ability, save DC, attack bonus, casting focus, and ritual or pool notes.

### Cantrips

| Cantrip | Notes |
| --- | --- |
| [[spell-owner]] | |

### Prepared or Known

| Spell | Level / Pool | Notes |
| --- | --- | --- |
| [[spell-owner]] | | |

### Slots or Casting Resources

| Level / Pool | Current / Max | Recovery |
| --- | --- | --- |
| | | |

## Inventory

Omit empty subsections. Link named item owners and retain quantity, state, and table consequence.

### Attuned

| Item | Notes |
| --- | --- |
| [[item-owner]] | |

### Carried

| Item | Qty | Notes |
| --- | --- | --- |
| [[item-owner]] | | |

### Stowed

| Item | Where | Notes |
| --- | --- | --- |
| [[item-owner]] | | |

### Currency

| Coin | Amount |
| --- | --- |
| gp | |

## Features

Omit empty subsections. Each populated row states effect, uses, and recovery when applicable.

### Traits

| Trait | Effect |
| --- | --- |
| | |

### Class Features

| Feature | Source | Effect | Uses | Recovery |
| --- | --- | --- | --- | --- |
| | | | | |

### Feats

| Feat | Source | Effect |
| --- | --- | --- |
| | | |

## Connections

| Tie | Table consequence |
| --- | --- |
| [[named-owner]] | State what this relationship changes at the table. |

Escape alias pipes as `\|` inside table cells. Omit this section when there are no named ties.

## Stated Goals

Omit when no transcript-supported player-stated goal exists. List only goals the player clearly stated in a game-session transcript, in character or out of character. Cite the session. A session summary may help locate or paraphrase a transcript-supported goal but must not be the sole source. Do not infer from play, connections, or DM thesis. After every session that included that player, refresh: add newly stated goals; remove a goal only if the player said it is done or abandoned.

| Goal | Session | Notes |
| --- | --- | --- |
| | | |

## Session Log

Omit for a new PC with no current changes. Keep only concise dated or session-numbered changes affecting play.

| Session / Date | Encounter | Current-play change |
| --- | --- | --- |
| | | |

## Art

Omit when no approved art exists beyond the featured portrait. Preserve existing attachment embeds and repository attachment names when present. Additional pictures may appear next to the section they illustrate; this section holds leftover approved embeds only.
