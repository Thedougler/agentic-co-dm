---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 15 undead lord with legendary resistance, restoration, and necrotic curses."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Mummy Lord"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: fa5b3dab-063b-41b9-90bd-9ed7fe487274
---

# Mummy Lord

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Mummy Lord"
size: Small
type: undead
alignment: "Lawful Evil"
ac: 17
hp: 187
hit_dice: "25d8 + 75"
speed: "30 ft."
stats: [18, 10, 17, 11, 19, 16]
saves:
  - int: 5
  - wis: 9
damage_vulnerabilities: "Fire"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "truesight 60 ft.; Passive Perception 19"
languages: "Common plus three other languages"
cr: 15
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the mummy fails a saving throw, it can choose to succeed instead."
  - name: "Magic Resistance"
    desc: "The mummy has Advantage on saving throws against spells and other magical effects."
  - name: "Undead Restoration"
    desc: "If destroyed, the mummy gains a new body in 24 hours if its heart is intact, reviving with all its Hit Points. The new body appears in an unoccupied space within the mummy's lair. The heart is a Tiny object that has AC 17, HP 10, and Immunity to all damage except Fire."
actions:
  - name: "Multiattack"
    desc: "The mummy makes one Rotting Fist or Channel Negative Energy attack, and it uses Dreadful Glare."
  - name: "Rotting Fist"
    desc: "*Melee Attack Roll:* +9, reach 5 ft. 15 (2d10 + 4) Bludgeoning damage plus 10 (3d6) Necrotic damage. If the target is a creature, it is cursed. While cursed, the target can't regain Hit Points, it gains no benefit from finishing a Long Rest, and its Hit Point maximum decreases by 10 (3d6) every 24 hours that elapse. A creature dies and turns to dust if reduced to 0 Hit Points by this attack."
  - name: "Channel Negative Energy"
    desc: "*Ranged Attack Roll:* +9, range 60 ft. 25 (6d6 + 4) Necrotic damage."
  - name: "Dreadful Glare"
    desc: "*Wisdom Saving Throw*: DC 17, one creature the mummy can see within 60 feet. *Failure:* 25 (6d6 + 4) Psychic damage, and the target has the Paralyzed condition until the end of the mummy's next turn."
  - name: "Spellcasting"
    desc: "The mummy casts one of the following spells, requiring no Material components and using Wisdom as the spellcasting ability (spell save DC 17, +9 to hit with spell attacks): - **At Will:** *Dispel Magic*, *Thaumaturgy* - **1e/Day Each:** *Animate Dead*, *Harm*, *Insect Plague*"
legendary_actions:
  - name: "Glare"
    desc: "The mummy uses Dreadful Glare. The mummy can't take this action again until the start of its next turn."
  - name: "Necrotic Strike"
    desc: "The mummy makes one Rotting Fist or Channel Negative Energy attack."
  - name: "Dread Command"
    desc: "The mummy casts *Command* (level 2 version), using the same spellcasting ability as Spellcasting. The mummy can't take this action again until the start of its next turn."
```
