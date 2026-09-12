---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 2 spider monstrosity that climbs and uses webs to restrain prey, dealing poison damage on bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ettercap"
found_at:
- "[[verdant-teeth|Verdant Teeth]]"
- "[[midchain-west|Midchain West]]"
uid: 2a5404d2-6e80-4eb8-b44c-97f212449e2d
---

# Ettercap

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ettercap"
size: Medium
type: monstrosity
alignment: "Neutral Evil"
ac: 13
hp: 44
hit_dice: "8d8 + 8"
speed: "30 ft., Climb 30 ft."
stats: [14, 15, 13, 7, 12, 8]
senses: "darkvision 60 ft.; Passive Perception 13"
cr: 2
traits:
  - name: "Spider Climb"
    desc: "The ettercap can climb difficult surfaces, including along ceilings, without needing to make an ability check."
  - name: "Web Walker"
    desc: "The ettercap ignores movement restrictions caused by webs, and the ettercap knows the location of any other creature in contact with the same web."
actions:
  - name: "Multiattack"
    desc: "The ettercap makes one Bite attack and one Claw attack."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 5 (1d6 + 2) Piercing damage plus 2 (1d4) Poison damage, and the target has the Poisoned condition until the start of the ettercap's next turn."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 7 (2d4 + 2) Slashing damage."
  - name: "Web Strand (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 12, one Large or smaller creature the ettercap can see within 30 feet. *Failure:* The target has the Restrained condition until the web is destroyed (AC 10; HP 5; Vulnerability to Fire damage; Immunity to Bludgeoning, Poison, and Psychic damage)."
bonus_actions:
  - name: "Reel"
    desc: "The ettercap pulls one creature within 30 feet of itself that is Restrained by its Web Strand up to 25 feet straight toward itself."
```
