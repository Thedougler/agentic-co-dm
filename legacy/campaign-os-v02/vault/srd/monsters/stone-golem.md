---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "CR 10 large construct with magic resistance; slam and force bolt attacks; can cast Slow."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Stone Golem"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[midchain-east|Midchain East]]"
uid: 70fbe411-9c82-40bc-b7d0-579521a29bff
---

# Stone Golem

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Stone Golem"
size: Large
type: construct
alignment: "Unaligned"
ac: 18
hp: 220
hit_dice: "21d10 + 105"
speed: "30 ft."
stats: [22, 9, 20, 3, 11, 1]
damage_immunities: "Poison, Psychic"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
senses: "darkvision 120 ft.; Passive Perception 10"
languages: "Understands Common plus two other languages but can't speak"
cr: 10
traits:
  - name: "Immutable Form"
    desc: "The golem can't shape-shift."
  - name: "Magic Resistance"
    desc: "The golem has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The golem makes two attacks, using Slam or Force Bolt in any combination."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +10, reach 5 ft. 15 (2d8 + 6) Bludgeoning damage plus 9 (2d8) Force damage."
  - name: "Force Bolt"
    desc: "*Ranged Attack Roll:* +9, range 120 ft. 22 (4d10) Force damage."
bonus_actions:
  - name: "Slow (Recharge 5-6)"
    desc: "The golem casts the *Slow* spell, requiring no spell components and using Constitution as the spellcasting ability (spell save DC 17)."
```
