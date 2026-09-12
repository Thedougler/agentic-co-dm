# Worked example (fixture — placeholder name, not real campaign content)

User: "I want to build a new PC — let's do the character interview."

Standard queries come back empty for `"Torvin Ashgale"` across `vault/campaigns/shattered-sea/pcs/
vault/` — clean to create. Interview runs all 20; Q4 gives a Mortis
("Ashborn" — disadvantage on death saves, advantage on fire saves) that
the player wants hidden from the table (Arc Notes, not Overview); Q12
gives a carried item (a cracked hourglass, no existing `vault/campaigns/shattered-sea/items/`
page — stays plain prose). Frontmatter fill: player "Sam", `class_levels:
Fighter 2`, HP/AC not on hand — left blank with a stub note.

```markdown
---
type: pc
status: canon
publish: false
aliases: ["Torvin"]
created: 2026-07-30
updated: 2026-07-30
tags: []
player: Sam
class_levels: Fighter 2
hp_max:
ac:
---

# Torvin Ashgale

## Overview

**Class:** Fighter 2 | **Player:** Sam

No HP/AC stated yet — left blank rather than guessed; a character sheet
will complete both.

**Mortis:** "Ashborn" — visible half only; the disadvantage-on-death-saves
mechanic is public, whether Torvin himself knows the fire-save half is
Arc Notes material (player asked to keep it hidden from the table).

**Core drive:** ...

## Backstory

...

## Arc Notes (DM Only)

**The hidden half of Ashborn:** ...

## Session Log

(empty — fills once Torvin has actually played)
```
