---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 11 Gargantuan flyer with powerful beak and talons that grapple, plus a swoop ability to carry away prey."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Roc"
uid: e8f2ee17-ade6-47cc-8e0e-df9686bd7172
---

# Roc

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Roc"
size: Gargantuan
type: monstrosity
alignment: "Unaligned"
ac: 15
hp: 248
hit_dice: "16d20 + 80"
speed: "20 ft., Fly 120 ft."
stats: [28, 10, 20, 3, 10, 9]
saves:
  - dex: 4
  - wis: 4
senses: "Passive Perception 18"
cr: 11
actions:
  - name: "Multiattack"
    desc: "The roc makes two Beak attacks. It can replace one attack with a Talons attack."
  - name: "Beak"
    desc: "*Melee Attack Roll:* +13, reach 10 ft. 28 (3d12 + 9) Piercing damage."
  - name: "Talons"
    desc: "*Melee Attack Roll:* +13, reach 5 ft. 23 (4d6 + 9) Slashing damage. If the target is a Huge or smaller creature, it has the Grappled condition (escape DC 19) from both talons, and it has the Restrained condition until the grapple ends."
bonus_actions:
  - name: "Swoop (Recharge 5-6)"
    desc: "If the roc has a creature Grappled, the roc flies up to half its Fly Speed without provoking Opportunity Attacks and drops that creature."
```
