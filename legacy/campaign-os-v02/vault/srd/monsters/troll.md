---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 5 troll with 94 HP, regenerates 15 HP/turn (acid/fire disable), sheds dangerous limbs when slashed, multiattack rends, charges."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Troll"
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[verdant-teeth|Verdant Teeth]]"
uid: cd792983-5825-42bb-9ee7-e4f5358298b5
---

# Troll

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Troll"
size: Large
type: giant
alignment: "Chaotic Evil"
ac: 15
hp: 94
hit_dice: "9d10 + 45"
speed: "30 ft."
stats: [18, 13, 20, 7, 9, 7]
senses: "darkvision 60 ft.; Passive Perception 15"
languages: "Giant"
cr: 5
traits:
  - name: "Loathsome Limbs (4/Day)"
    desc: "If the troll ends any turn Bloodied and took 15+ Slashing damage during that turn, one of the troll's limbs is severed, falls into the troll's space, and becomes a Troll Limb. The limb acts immediately after the troll's turn. The troll has 1 Exhaustion level for each missing limb, and it grows replacement limbs the next time it regains Hit Points."
  - name: "Regeneration"
    desc: "The troll regains 15 Hit Points at the start of each of its turns. If the troll takes Acid or Fire damage, this trait doesn't function on the troll's next turn. The troll dies only if it starts its turn with 0 Hit Points and doesn't regenerate."
actions:
  - name: "Multiattack"
    desc: "The troll makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 11 (2d6 + 4) Slashing damage."
bonus_actions:
  - name: "Charge"
    desc: "The troll moves up to half its Speed straight toward an enemy it can see."
```
