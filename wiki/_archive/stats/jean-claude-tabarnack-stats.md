---
type: pc-stats
status: canon
publish: false
aliases: []
summary: "Ability scores, saves, and combat stats derived from the RAW-baseline sheet, since Jean-Claude carries no real character sheet on file."
created: 2026-07-30
updated: 2026-08-08
tags: [combat]
pc: "jean-claude-tabarnack"
pc_level: 5
last_synced: "2026-07-25"
uid: 5cc7e0fa-9eae-4b37-a20b-6510c334f4fd
---

# Jean-Claude Tabarnack — Attributes

Mechanical attributes for [[jean-claude-tabarnack|Jean-Claude Tabarnack]],
transcribed from
`vault/campaigns/shattered-sea/pcs/character-sheets/jean-claude-tabarnack-sheet.md`
(a RAW-baseline derivation, not a player-submitted sheet: no PDF exists for
this PC). Every value below carries a `[theoretical]`/`[assumed]` tag
unless marked otherwise; a sheet error stays as printed and gets a
`[verify]` tag instead of a silent fix. This page is the single source of
truth for every per-ability, per-skill, and per-speed value; `ac`,
`hp_max`, `class_levels`, and `level` stay in
[[jean-claude-tabarnack]]'s frontmatter and are never restated here.

Small size, amphibious (breathes air and water), and a climb speed equal to
his walking speed are [[grung|Grung]] species traits (see Combat Stats
below and [[jean-claude-tabarnack-abilities|Abilities]] for the rest of the
species kit).

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| [[strength\|Strength]] | 10 | +0 | +3 | yes |
| [[dexterity\|Dexterity]] | 16 | +3 | +6 | yes |
| [[constitution\|Constitution]] | 14 | +2 | +2 | no |
| [[intelligence\|Intelligence]] | 10 | +0 | +0 | no |
| [[wisdom\|Wisdom]] | 14 | +2 | +2 | no |
| [[charisma\|Charisma]] | 8 | -1 | -1 | no |

`[theoretical]`, unchanged from the level-4 baseline. No Ability Score
Improvement is due at Ranger 5 (the level-4 ASI is already folded into
these scores). Save proficiencies are the Ranger class defaults
(Strength, Dexterity). Proficiency bonus **+3** at level 5.

## Skills

The sheet on file states no skill proficiency list beyond the ability
scores and saves above. Passive Perception, Insight, and Investigation:
`[unknown]` (no proficiency data to calculate from). Mortis grants
advantage on Perception and Survival checks instead of a skill
proficiency (see [[jean-claude-tabarnack-abilities|Abilities]]).

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative | +5 | `[calculated]` DEX +3, plus WIS +2 from Gloom Stalker's Initiative Bonus ([[ranger-gloom-stalker\|Gloom Stalker]] level 3) |
| Speed | 25 ft. walking, 25 ft. climbing | `[pcs-page, grung]` climb speed equal to walking speed, a [[grung\|Grung]] species trait |
| Hit dice | 5d10 | `[srd]` Ranger hit die |
| Proficiency bonus | +3 | `[assumed]` |
| Damage resistances | none stated. Immune to poison damage (species trait, see [[jean-claude-tabarnack-abilities\|Abilities]]) | `[pcs-page, grung]` |
| Condition advantages | immune to the poisoned condition (species trait, see [[jean-claude-tabarnack-abilities\|Abilities]]) | `[pcs-page, grung]` |

AC and max HP live in [[jean-claude-tabarnack]]'s frontmatter (`ac:`,
`hp_max:`) — the roster `.base` views query them there; this table carries
no rows for them.

## Proficiencies & Languages

Armour and weapon proficiencies beyond the studded leather, shortbow, and
dagger used in his attack routine are not stated in the sheet on file.
Species-granted proficiencies ([[poisoners-kit|Poisoner's Kit]]) live on
[[jean-claude-tabarnack-abilities|Abilities]].
