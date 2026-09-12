---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge dragon (CR 16) with lightning immunity, breath weapon, spellcasting, and legendary resistance."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Blue Dragon"
found_at:
- "[[central-strait|Central Strait]]"
- "[[crown-islands|Crown Islands]]"
uid: 5ad36e83-9948-49d7-a4cd-0187ee035fd5
---

# Adult Blue Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Blue Dragon"
size: Huge
type: dragon
alignment: "Lawful Evil"
ac: 19
hp: 212
hit_dice: "17d12 + 102"
speed: "40 ft., Burrow 30 ft., Fly 80 ft."
stats: [25, 10, 23, 16, 15, 20]
saves:
  - dex: 5
  - wis: 7
damage_immunities: "Lightning"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 22"
languages: "Common, Draconic"
cr: 16
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Shatter*."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +12, reach 10 ft. 16 (2d8 + 7) Slashing damage plus 5 (1d10) Lightning damage."
  - name: "Lightning Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 19, each creature in a 90-foot-long, 5-foot-wide Line. *Failure:* 60 (11d10) Lightning damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 18): - **At Will:** *Detect Magic*, *Invisibility*, *Mage Hand*, *Shatter* - **1e/Day Each:** *Scrying*, *Sending*"
legendary_actions:
  - name: "Cloaked Flight"
    desc: "The dragon uses Spellcasting to cast *Invisibility* on itself, and it can fly up to half its Fly Speed. The dragon can't take this action again until the start of its next turn."
  - name: "Sonic Boom"
    desc: "The dragon uses Spellcasting to cast *Shatter*. The dragon can't take this action again until the start of its next turn."
  - name: "Tail Swipe"
    desc: "The dragon makes one Rend attack."
```
