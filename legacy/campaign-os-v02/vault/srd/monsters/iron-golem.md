---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "Large construct with fire absorption, magic resistance, and fiery multiattack (CR 16)."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Iron Golem"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[shelfworks|Shelfworks]]"
uid: 0d19ebda-d4ee-4f44-93d9-3993576d38dd
---

# Iron Golem

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Iron Golem"
size: Large
type: construct
alignment: "Unaligned"
ac: 20
hp: 252
hit_dice: "24d10 + 120"
speed: "30 ft."
stats: [24, 9, 20, 3, 11, 1]
damage_immunities: "Fire, Poison, Psychic"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
senses: "darkvision 120 ft.; Passive Perception 10"
languages: "Understands Common plus two other languages but can't speak"
cr: 16
traits:
  - name: "Fire Absorption"
    desc: "Whenever the golem is subjected to Fire damage, it regains a number of Hit Points equal to the Fire damage dealt."
  - name: "Immutable Form"
    desc: "The golem can't shape-shift."
  - name: "Magic Resistance"
    desc: "The golem has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The golem makes two attacks, using Bladed Arm or Fiery Bolt in any combination."
  - name: "Bladed Arm"
    desc: "*Melee Attack Roll:* +12, reach 10 ft. 20 (3d8 + 7) Slashing damage plus 10 (3d6) Fire damage."
  - name: "Fiery Bolt"
    desc: "*Ranged Attack Roll:* +10, range 120 ft. 36 (8d8) Fire damage."
  - name: "Poison Breath (Recharge 6)"
    desc: "*Constitution Saving Throw*: DC 18, each creature in a 60-foot Cone. *Failure:* 55 (10d10) Poison damage. *Success:* Half damage."
```
