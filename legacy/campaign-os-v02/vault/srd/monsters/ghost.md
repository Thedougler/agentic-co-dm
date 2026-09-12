---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 4 incorporeal undead with possession ability and ethereal movement."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ghost"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[sunken-crown|Sunken Crown]]"
uid: e4650a5a-0fb6-4d2b-916c-eca7c9eaed1a
---

# Ghost

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ghost"
size: Medium
type: undead
alignment: "Neutral"
ac: 11
hp: 45
hit_dice: "10d8"
speed: "5 ft., Fly 40 ft. (hover)"
stats: [7, 13, 10, 10, 12, 17]
damage_resistances: "Acid, Bludgeoning, Cold, Fire, Lightning, Piercing, Slashing, Thunder"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained"
senses: "darkvision 60 ft.; Passive Perception 11"
languages: "Common plus one other language"
cr: 4
traits:
  - name: "Ethereal Sight"
    desc: "The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane."
  - name: "Incorporeal Movement"
    desc: "The ghost can move through other creatures and objects as if they were Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an object."
actions:
  - name: "Multiattack"
    desc: "The ghost makes two Withering Touch attacks."
  - name: "Withering Touch"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 19 (3d10 + 3) Necrotic damage."
  - name: "Horrific Visage"
    desc: "*Wisdom Saving Throw*: DC 13, each creature in a 60-foot Cone that can see the ghost and isn't an Undead. *Failure:* 10 (2d6 + 3) Psychic damage, and the target has the Frightened condition until the start of the ghost's next turn. *Success:* The target is immune to this ghost's Horrific Visage for 24 hours."
  - name: "Possession (Recharge 6)"
    desc: "*Charisma Saving Throw*: DC 13, one Humanoid the ghost can see within 5 feet. *Failure:* The target is possessed by the ghost; the ghost disappears, and the target has the Incapacitated condition and loses control of its body. The ghost now controls the body, but the target retains awareness. The ghost can't be targeted by any attack, spell, or other effect, except ones that specifically target Undead. The ghost's game statistics are the same, except it uses the possessed target's Speed, as well as the target's Strength, Dexterity, and Constitution modifiers. The possession lasts until the body drops to 0 Hit Points or the ghost leaves as a Bonus Action. When the possession ends, the ghost appears in an unoccupied space within 5 feet of the target, and the target is immune to this ghost's Possession for 24 hours. *Success:* The target is immune to this ghost's Possession for 24 hours."
  - name: "Etherealness"
    desc: "The ghost casts the *Etherealness* spell, requiring no spell components and using Charisma as the spellcasting ability. The ghost is visible on the Material Plane while on the Border Ethereal and vice versa, but it can't affect or be affected by anything on the other plane. - **At Will:** *Etherealness*"
```
