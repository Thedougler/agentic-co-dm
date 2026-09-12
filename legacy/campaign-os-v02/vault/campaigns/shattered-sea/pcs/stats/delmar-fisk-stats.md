---
type: pc-stats
status: canon
publish: false
aliases: []
summary: "Ability scores, saves, skills, and combat stats transcribed from Delmar's character sheet."
created: 2026-07-30
updated: 2026-08-08
tags: [combat]
pc: "delmar-fisk"
pc_level: 5
last_synced: "2026-07-26"
uid: 41253992-3508-439e-a976-e1e3e8a4e889
---

# Delmar Atticus Fisk — Attributes

Mechanical attributes for [[delmar-fisk|Delmar Atticus Fisk]], transcribed
from `_assets/character-sheets/delmar-fisk-character-sheet.pdf`. A value
the sheet states wrongly is transcribed as printed and tagged `[verify]`,
never silently corrected. This page is the single source of truth for
every per-ability, per-skill, and per-speed value; `ac`, `hp_max`,
`class_levels`, and `level` stay in [[delmar-fisk]]'s frontmatter and are
never restated here.

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| [[strength\|Strength]] | 10 | +0 | +0 | no |
| [[dexterity\|Dexterity]] | 20 | +5 | +8 | yes |
| [[constitution\|Constitution]] | 14 | +2 | +2 | no |
| [[intelligence\|Intelligence]] | 11 | +0 | +3 | yes |
| [[wisdom\|Wisdom]] | 12 | +1 | +1 | no |
| [[charisma\|Charisma]] | 15 | +2 | +2 | no |

Save proficiencies (Dexterity, Intelligence) are the Core Rogue Traits
default (PHB-2024 129). The sheet's own "Saving Throw Modifiers" checkbox
column wasn't legible on the rendered image, so this is the class-table
default and not an independently confirmed checkmark.

## Skills

**Expertise (double proficiency):** Investigation (INT) +6, Persuasion
(CHA) +8.

**Full proficiency:** Acrobatics (DEX) +8, Insight (WIS) +4, Perception
(WIS) +4, Sleight of Hand (DEX) +8, Stealth (DEX) +8.

**Untrained (ability mod only):** all other skills.

Passive Perception 14, Passive Insight 14, Passive Investigation 16.

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative | +7 | DEX +5, plus CHA +2 from Rakish Audacity ([[rogue-swashbuckler\|Swashbuckler]] Level 3: adds Charisma modifier to initiative rolls) |
| Speed | 30 ft. walking, 30 ft. flying ([[winged-boots\|Winged Boots]], attuned), 60 ft. swimming ([[delmars-cloak-of-the-manta-ray\|Cloak of the Manta Ray]], attuned) | sheet |
| Hit dice | 5d8 | sheet |
| Proficiency bonus | +3 | sheet |
| Damage resistances | none stated | sheet |
| Condition advantages | none stated | sheet |

AC and max HP live in [[delmar-fisk]]'s frontmatter (`ac:`, `hp_max:`) —
the roster `.base` views query them there; this table carries no rows for
them.

## Proficiencies & Languages

Firearms and martial weapon proficiency (Firearm Specialist feat).
[[thieves-tools|Thieves' Tools]] proficiency. Extra language and extra skill proficiency
from Variant Human traits (detailed on [[delmar-fisk-abilities]]). [[pistol|Pistol]]'s
`[verify]`-flagged to-hit sits on [[delmar-fisk-abilities|Abilities]]'
Actions table alongside the rest of the attack routine.
