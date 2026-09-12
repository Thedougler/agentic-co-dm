---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "A Small Chaotic Evil will-o'-wisp (CR 2) that's incorporeal, illuminates the dark, and shocks with lightning damage."
found_at:
- "[[doldrums|Doldrums]]"
- "[[midchain-east|Midchain East]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Will-o'-Wisp"
uid: 24fc85e2-10f2-4cb7-9f4e-16fbbe5f3e39
---

# Will-o'-Wisp

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Will-o'-Wisp"
size: Small
type: undead
alignment: "Chaotic Evil"
ac: 19
hp: 27
hit_dice: "11d4"
speed: "5 ft., Fly 50 ft. (hover)"
stats: [1, 28, 10, 13, 14, 11]
damage_resistances: "Acid, Bludgeoning, Cold, Fire, Necrotic, Piercing, Slashing"
damage_immunities: "Lightning, Poison"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 120 ft.; Passive Perception 12"
languages: "Common plus one other language"
cr: 2
traits:
  - name: "Ephemeral"
    desc: "The wisp can't wear or carry anything."
  - name: "Illumination"
    desc: "The wisp sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet."
  - name: "Incorporeal Movement"
    desc: "The wisp can move through other creatures and objects as if they were Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an object."
actions:
  - name: "Shock"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 11 (2d8 + 2) Lightning damage."
bonus_actions:
  - name: "Consume Life"
    desc: "*Constitution Saving Throw*: DC 10, one living creature the wisp can see within 5 feet that has 0 Hit Points. *Failure:* The target dies, and the wisp regains 10 (3d6) Hit Points."
  - name: "Vanish"
    desc: "The wisp and its light have the Invisible condition until the wisp's Concentration ends on this effect, which ends early immediately after the wisp makes an attack roll or uses Consume Life."
```
