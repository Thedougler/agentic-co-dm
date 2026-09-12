---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 21 Medium undead with Spirit Jar, Legendary Resistance, and extensive spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Lich"
found_at:
- "[[midchain-east|Midchain East]]"
- "[[shelfworks|Shelfworks]]"
uid: 2af07b0d-4616-45fd-b3c3-4d96b95fb1a5
---

# Lich

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Lich"
size: Medium
type: undead
alignment: "Neutral Evil"
ac: 20
hp: 315
hit_dice: "42d8 + 126"
speed: "30 ft."
stats: [11, 16, 16, 21, 14, 16]
saves:
  - dex: 10
  - con: 10
  - int: 12
  - wis: 9
damage_resistances: "Cold, Lightning"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "truesight 120 ft.; Passive Perception 19"
languages: "All"
cr: 21
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the lich fails a saving throw, it can choose to succeed instead."
  - name: "Spirit Jar"
    desc: "If destroyed, the lich reforms in 1d10 days if it has a spirit jar, reviving with all its Hit Points. The new body appears in an unoccupied space within the lich's lair."
actions:
  - name: "Multiattack"
    desc: "The lich makes three attacks, using Eldritch Burst or Paralyzing Touch in any combination."
  - name: "Eldritch Burst"
    desc: "*Melee or Ranged Attack Roll:* +12, reach 5 ft. or range 120 ft. 31 (4d12 + 5) Force damage."
  - name: "Paralyzing Touch"
    desc: "*Melee Attack Roll:* +12, reach 5 ft. 15 (3d6 + 5) Cold damage, and the target has the Paralyzed condition until the start of the lich's next turn."
  - name: "Spellcasting"
    desc: "The lich casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 20): - **At Will:** *Detect Magic*, *Detect Thoughts*, *Dispel Magic*, *Fireball*, *Invisibility*, *Lightning Bolt*, *Mage Hand*, *Prestidigitation* - **2e/Day Each:** *Animate Dead*, *Dimension Door*, *Plane Shift* - **1e/Day Each:** *Chain Lightning*, *Finger of Death*, *Power Word Kill*, *Scrying*"
reactions:
  - name: "Protective Magic"
    desc: "The lich casts *Counterspell* or *Shield* in response to the spell's trigger, using the same spellcasting ability as Spellcasting."
legendary_actions:
  - name: "Deathly Teleport"
    desc: "The lich teleports up to 60 feet to an unoccupied space it can see, and each creature within 10 feet of the space it left takes 11 (2d10) Necrotic damage."
  - name: "Disrupt Life"
    desc: "*Constitution Saving Throw*: DC 20, each creature that isn't an Undead in a 20-foot Emanation originating from the lich. *Failure:* 31 (9d6) Necrotic damage. *Success:* Half damage. *Failure or Success*: The lich can't take this action again until the start of its next turn."
  - name: "Frightening Gaze"
    desc: "The lich casts *Fear*, using the same spellcasting ability as Spellcasting. The lich can't take this action again until the start of its next turn."
```
