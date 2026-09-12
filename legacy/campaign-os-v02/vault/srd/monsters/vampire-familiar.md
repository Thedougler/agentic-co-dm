---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, intrigue, undead]
summary: "Small CR 3 humanoid familiar with 65 HP, vampiric telepathy with master, umbral dagger attacks dealing necrotic damage and paralysis."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Vampire Familiar"
found_at:
- "[[doldrums|Doldrums]]"
- "[[shelfworks|Shelfworks]]"
uid: f7e722bd-5bf8-4a2a-b129-2609f3511894
---

# Vampire Familiar

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Vampire Familiar"
size: Small
type: humanoid
alignment: "Neutral Evil"
ac: 15
hp: 65
hit_dice: "10d8 + 20"
speed: "30 ft., Climb 30 ft."
stats: [17, 16, 15, 10, 10, 14]
saves:
  - dex: 5
  - wis: 2
damage_resistances: "Necrotic"
damage_immunities: "Charmed ((except from its vampire master))"
senses: "darkvision 60 ft.; Passive Perception 14"
languages: "Common plus one other language"
cr: 3
traits:
  - name: "Vampiric Connection"
    desc: "While the familiar and its vampire master are on the same plane of existence, the vampire can communicate with the familiar telepathically, and the vampire can perceive through the familiar's senses."
actions:
  - name: "Multiattack"
    desc: "The familiar makes two Umbral Dagger attacks."
  - name: "Umbral Dagger"
    desc: "*Melee or Ranged Attack Roll:* +5, reach 5 ft. or range 20/60 ft. 5 (1d4 + 3) Piercing damage plus 7 (3d4) Necrotic damage. If the target is reduced to 0 Hit Points by this attack, the target becomes Stable but has the Poisoned condition for 1 hour. While it has the Poisoned condition, the target has the Paralyzed condition."
bonus_actions:
  - name: "Deathless Agility"
    desc: "The familiar takes the Dash or Disengage action."
```
