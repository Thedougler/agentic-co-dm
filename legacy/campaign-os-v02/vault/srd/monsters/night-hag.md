---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 5 fiend that hunts via spectral dreams, trapping victims' souls in a magical bag."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[midchain-west|Midchain West]]"
statblock: inline
name: "Night Hag"
uid: e677cde6-15aa-41c0-bec8-05c3e045a327
---

# Night Hag

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Night Hag"
size: Medium
type: fiend
alignment: "Neutral Evil"
ac: 17
hp: 112
hit_dice: "15d8 + 45"
speed: "30 ft."
stats: [18, 15, 16, 16, 14, 16]
damage_resistances: "Cold, Fire"
damage_immunities: "Charmed"
senses: "darkvision 120 ft.; Passive Perception 15"
languages: "Abyssal, Common, Infernal, Primordial"
cr: 5
traits:
  - name: "Magic Resistance"
    desc: "The hag has Advantage on saving throws against spells and other magical effects."
  - name: "Soul Bag"
    desc: "The hag has a soul bag. While holding or carrying the bag, the hag can use its Nightmare Haunting action. The bag has AC 15, HP 20, and Resistance to all damage. The bag turns to dust if reduced to 0 Hit Points. If the bag is destroyed, any souls the bag is holding are released. The hag can create a new bag after 7 days."
actions:
  - name: "Multiattack"
    desc: "The hag makes two Claw attacks."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 13 (2d8 + 4) Slashing damage."
  - name: "Spellcasting"
    desc: "The hag casts one of the following spells, requiring no Material components and using Intelligence as the spellcasting ability (spell save DC 14): - **At Will:** *Detect Magic*, *Etherealness*, *Magic Missile* - **2e/Day Each:** *Phantasmal Killer*, *Plane Shift*"
  - name: "Nightmare Haunting (1/Day; Requires Soul Bag)"
    desc: "While on the Ethereal Plane, the hag casts *Dream*, using the same spellcasting ability as Spellcasting. Only the hag can serve as the spell's messenger, and the target must be a creature the hag can see on the Material Plane. The spell fails and is wasted if the target is under the effect of the *Protection from Evil and Good* spell or within a *Magic Circle* spell. If the target takes damage from the *Dream* spell, the target's Hit Point maximum decreases by an amount equal to that damage. If the spell kills the target, its soul is trapped in the hag's soul bag, and the target can't be raised from the dead until its soul is released. - **At Will:** - **1/Day Each:** *Dream*, *Protection from Evil and Good*, *Magic Circle*"
bonus_actions:
  - name: "Shape-Shift"
    desc: "The hag shape-shifts into a Small or Medium Humanoid, or it returns to its true form. Other than its size, its game statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
