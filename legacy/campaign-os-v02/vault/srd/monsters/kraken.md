---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 23 Gargantuan monstrosity with Legendary Resistance, Siege Monster, tentacle grapple, and ranged lightning strikes."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Kraken"
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: dd47b29d-4c67-4a30-a0f6-5994e699bf06
---

# Kraken

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Kraken"
size: Gargantuan
type: monstrosity
alignment: "Chaotic Evil"
ac: 18
hp: 481
hit_dice: "26d20 + 208"
speed: "30 ft., Swim 120 ft."
stats: [30, 11, 26, 22, 18, 20]
saves:
  - str: 17
  - dex: 7
  - con: 15
  - wis: 11
damage_immunities: "Cold, Lightning"
condition_immunities: "Frightened, Grappled, Paralyzed, Restrained"
senses: "truesight 120 ft.; Passive Perception 21"
languages: "Understands Abyssal, Celestial, Infernal, And Primordial but can't speak; telepathy 120 ft."
cr: 23
traits:
  - name: "Amphibious"
    desc: "The kraken can breathe air and water."
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the kraken fails a saving throw, it can choose to succeed instead."
  - name: "Siege Monster"
    desc: "The kraken deals double damage to objects and structures."
actions:
  - name: "Multiattack"
    desc: "The kraken makes two Tentacle attacks and uses Fling, Lightning Strike, or Swallow."
  - name: "Tentacle"
    desc: "*Melee Attack Roll:* +17, reach 30 ft. 24 (4d6 + 10) Bludgeoning damage. The target has the Grappled condition (escape DC 20) from one of ten tentacles, and it has the Restrained condition until the grapple ends."
  - name: "Fling"
    desc: "The kraken throws a Large or smaller creature Grappled by it to a space it can see within 60 feet of itself that isn't in the air. *Dexterity Saving Throw*: DC 25, the creature thrown and each creature in the destination space. *Failure:* 18 (4d8) Bludgeoning damage, and the target has the Prone condition. *Success:* Half damage only."
  - name: "Lightning Strike"
    desc: "*Dexterity Saving Throw*: DC 23, one creature the kraken can see within 120 feet. *Failure:* 33 (6d10) Lightning damage. *Success:* Half damage."
  - name: "Swallow"
    desc: "*Dexterity Saving Throw*: DC 25, one creature Grappled by the kraken (it can have up to four creatures swallowed at a time). *Failure:* 23 (3d8 + 10) Piercing damage. If the target is Large or smaller, it is swallowed and no longer Grappled. A swallowed creature has the Restrained condition, has Cover|XPHB|Total Cover against attacks and other effects outside the kraken, and takes 24 (7d6) Acid damage at the start of each of its turns. If the kraken takes 50 damage or more on a single turn from a creature inside it, the kraken must succeed on a DC 25 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, each of which falls in a space within 10 feet of the kraken with the Prone condition. If the kraken dies, any swallowed creature no longer has the Restrained condition and can escape from the corpse using 15 feet of movement, exiting Prone."
legendary_actions:
  - name: "Storm Bolt"
    desc: "The kraken uses Lightning Strike."
  - name: "Toxic Ink"
    desc: "*Constitution Saving Throw*: DC 23, each creature in a 15-foot Emanation originating from the kraken while it is underwater. *Failure:* The target has the Blinded and Poisoned conditions until the end of the kraken's next turn. The kraken then moves up to its Speed. *Failure or Success*: The kraken can't take this action again until the start of its next turn."
```
