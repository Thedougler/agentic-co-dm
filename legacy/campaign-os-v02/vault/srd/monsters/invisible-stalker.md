---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, stealth]
summary: "Large air elemental, always invisible, with wind attacks and grappling vortex (CR 6)."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Invisible Stalker"
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[outer-reach|Outer Reach]]"
uid: d4ead383-5a01-4211-96b5-d5c34017ff72
---

# Invisible Stalker

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Invisible Stalker"
size: Large
type: elemental
alignment: "Neutral"
ac: 14
hp: 97
hit_dice: "13d10 + 26"
speed: "50 ft., Fly 50 ft. (hover)"
stats: [16, 19, 14, 10, 15, 11]
damage_resistances: "Bludgeoning, Piercing, Slashing"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 18"
languages: "Common, Primordial (Auran)"
cr: 6
traits:
  - name: "Air Form"
    desc: "The stalker can enter an enemy's space and stop there. It can move through a space as narrow as 1 inch without expending extra movement to do so."
  - name: "Invisibility"
    desc: "The stalker has the Invisible condition."
actions:
  - name: "Multiattack"
    desc: "The stalker makes three Wind Swipe attacks. It can replace one attack with a use of Vortex."
  - name: "Wind Swipe"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 11 (2d6 + 4) Force damage."
  - name: "Vortex"
    desc: "*Constitution Saving Throw*: DC 14, one Large or smaller creature in the stalker's space. *Failure:* 7 (1d8 + 3) Thunder damage, and the target has the Grappled condition (escape DC 13). Until the grapple ends, the target can't cast spells with a Verbal component and takes 7 (2d6) Thunder damage at the start of each of the stalker's turns."
```
