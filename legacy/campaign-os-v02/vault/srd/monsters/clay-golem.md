---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "Large construct (CR 9) with Acid Absorption, Berserk when bloodied, and Slam attacks that reduce target HP maximum."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Clay Golem"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[shelfworks|Shelfworks]]"
uid: 3f6e761b-ca12-4ce8-947e-29fd032e37d4
---

# Clay Golem

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Clay Golem"
size: Large
type: construct
alignment: "Unaligned"
ac: 14
hp: 123
hit_dice: "13d10 + 52"
speed: "20 ft."
stats: [20, 9, 18, 3, 8, 1]
damage_resistances: "Bludgeoning, Piercing, Slashing"
damage_immunities: "Acid, Poison, Psychic"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 9"
languages: "Common plus one other language"
cr: 9
traits:
  - name: "Acid Absorption"
    desc: "Whenever the golem is subjected to Acid damage, it takes no damage and instead regains a number of Hit Points equal to the Acid damage dealt."
  - name: "Berserk"
    desc: "Whenever the golem starts its turn Bloodied, roll 1d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object. Once the golem goes berserk, it continues to be berserk until it is destroyed or it is no longer Bloodied."
  - name: "Immutable Form"
    desc: "The golem can't shape-shift."
  - name: "Magic Resistance"
    desc: "The golem has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The golem makes two Slam attacks, or it makes three Slam attacks if it used Hasten this turn."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +9, reach 5 ft. 10 (1d10 + 5) Bludgeoning damage plus 6 (1d12) Acid damage, and the target's Hit Point maximum decreases by an amount equal to the Acid damage taken."
bonus_actions:
  - name: "Hasten (Recharge 5-6)"
    desc: "The golem takes the Dash and Disengage actions."
```
