---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 1/2 troll limb with 14 HP, regenerates 5 HP/turn (disabled by acid/fire), can spawn full troll in 24 hours, rend attack."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Troll Limb"
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: a149d8bf-b33d-4fb5-a4cd-c3dd1e39ec3f
---

# Troll Limb

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Troll Limb"
size: Small
type: giant
alignment: "Chaotic Evil"
ac: 13
hp: 14
hit_dice: "4d6"
speed: "20 ft."
stats: [18, 12, 10, 1, 9, 1]
senses: "darkvision 60 ft.; Passive Perception 9"
cr: "1/2"
traits:
  - name: "Regeneration"
    desc: "The limb regains 5 Hit Points at the start of each of its turns. If the limb takes Acid or Fire damage, this trait doesn't function on the limb's next turn. The limb dies only if it starts its turn with 0 Hit Points and doesn't regenerate."
  - name: "Troll Spawn"
    desc: "The limb uncannily has the same senses as a whole troll. If the limb isn't destroyed within 24 hours, roll 1d12. On a 12, the limb turns into a Troll. Otherwise, the limb withers away."
actions:
  - name: "Rend"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 9 (2d4 + 4) Slashing damage."
```
