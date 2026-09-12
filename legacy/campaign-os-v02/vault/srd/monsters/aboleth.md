---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, mystery]
summary: "Large aberration (CR 10) with legendary resistance, telepathic abilities, and psychic domination powers."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
statblock: inline
name: "Aboleth"
subtype: srd
found_at:
- "[[the-drowned-maw|The Drowned Maw]]"
- "[[sunken-crown|Sunken Crown]]"
uid: 4b4963c7-5994-4e9b-b7a4-c87b3b24100d
---

# Aboleth

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Aboleth"
size: Large
type: aberration
alignment: "Lawful Evil"
ac: 17
hp: 150
hit_dice: "20d10 + 40"
speed: "10 ft., Swim 40 ft."
stats: [21, 9, 15, 18, 15, 18]
saves:
  - dex: 3
  - con: 6
  - int: 8
  - wis: 6
senses: "darkvision 120 ft.; Passive Perception 20"
languages: "Deep Speech; telepathy 120 ft."
cr: 10
traits:
  - name: "Amphibious"
    desc: "The aboleth can breathe air and water."
  - name: "Eldritch Restoration"
    desc: "If destroyed, the aboleth gains a new body in 5d10 days, reviving with all its Hit Points in the Far Realm or another location chosen by the DM."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the aboleth fails a saving throw, it can choose to succeed instead."
  - name: "Mucus Cloud"
    desc: "While underwater, the aboleth is surrounded by mucus. *Constitution Saving Throw*: DC 14, each creature in a 5-foot Emanation originating from the aboleth at the end of the aboleth's turn. *Failure:* The target is cursed. Until the curse ends, the target's skin becomes slimy, the target can breathe air and water, and it can't regain Hit Points unless it is underwater. While the cursed creature is outside a body of water, the creature takes 6 (1d12) Acid damage at the end of every 10 minutes unless moisture is applied to its skin before those minutes have passed."
  - name: "Probing Telepathy"
    desc: "If a creature the aboleth can see communicates telepathically with the aboleth, the aboleth learns the creature's greatest desires."
actions:
  - name: "Multiattack"
    desc: "The aboleth makes two Tentacle attacks and uses either Consume Memories or Dominate Mind if available."
  - name: "Tentacle"
    desc: "*Melee Attack Roll:* +9, reach 15 ft. 12 (2d6 + 5) Bludgeoning damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 14) from one of four tentacles."
  - name: "Consume Memories"
    desc: "*Intelligence Saving Throw*: DC 16, one creature within 30 feet that is Charmed or Grappled by the aboleth. *Failure:* 10 (3d6) Psychic damage. *Success:* Half damage. *Failure or Success*: The aboleth gains the target's memories if the target is a Humanoid and is reduced to 0 Hit Points by this action."
  - name: "Dominate Mind (2/Day)"
    desc: "*Wisdom Saving Throw*: DC 16, one creature the aboleth can see within 30 feet. *Failure:* The target has the Charmed condition until the aboleth dies or is on a different plane of existence from the target. While Charmed, the target acts as an ally to the aboleth and is under its control while within 60 feet of it. In addition, the aboleth and the target can communicate telepathically with each other over any distance. The target repeats the save whenever it takes damage as well as after every 24 hours it spends at least 1 mile away from the aboleth, ending the effect on itself on a success."
legendary_actions:
  - name: "Lash"
    desc: "The aboleth makes one Tentacle attack."
  - name: "Psychic Drain"
    desc: "If the aboleth has at least one creature Charmed or Grappled, it uses Consume Memories and regains 5 (1d10) Hit Points."
```
