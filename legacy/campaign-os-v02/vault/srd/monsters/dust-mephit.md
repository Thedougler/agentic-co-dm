---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 1/2 small elemental that explodes when killed and uses blinding breath and sleep spells."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Dust Mephit"
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[ashwall-islands|Ashwall Islands]]"
uid: 57fff391-3673-4f14-9c10-5e33ffd61ae2
---

# Dust Mephit

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Dust Mephit"
size: Small
type: elemental
alignment: "Neutral Evil"
ac: 12
hp: 17
hit_dice: "5d6"
speed: "30 ft., Fly 30 ft."
stats: [5, 14, 10, 9, 11, 10]
damage_vulnerabilities: "Fire"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 12"
languages: "Primordial (Auran, Terran)"
cr: "1/2"
traits:
  - name: "Death Burst"
    desc: "The mephit explodes when it dies. *Dexterity Saving Throw*: DC 10, each creature in a 5-foot Emanation originating from the mephit. *Failure:* 5 (2d4) Bludgeoning damage. *Success:* Half damage."
actions:
  - name: "Claw"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 4 (1d4 + 2) Slashing damage."
  - name: "Blinding Breath (Recharge 6)"
    desc: "*Dexterity Saving Throw*: DC 10, each creature in a 15-foot Cone. *Failure:* The target has the Blinded condition until the end of the mephit's next turn."
  - name: "Sleep (1/Day)"
    desc: "The mephit casts the *Sleep* spell, requiring no spell components and using Charisma as the spellcasting ability (spell save DC 10). - **At Will:** - **1/Day Each:** *Sleep*"
```
