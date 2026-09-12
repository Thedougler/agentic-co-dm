---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "Huge monstrosity with five regenerating heads, extra reactions, and multiattack (CR 8)."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Hydra"
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[doldrums|Doldrums]]"
uid: e9bd3eb7-6a3a-4894-be2f-d39508e2ba27
---

# Hydra

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Hydra"
size: Huge
type: monstrosity
alignment: "Unaligned"
ac: 15
hp: 184
hit_dice: "16d12 + 80"
speed: "40 ft., Swim 40 ft."
stats: [20, 12, 20, 2, 10, 7]
damage_immunities: "Blinded, Charmed, Deafened, Frightened, Stunned, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 16"
cr: 8
traits:
  - name: "Hold Breath"
    desc: "The hydra can hold its breath for 1 hour."
  - name: "Multiple Heads"
    desc: "The hydra has five heads. Whenever the hydra takes 25 damage or more on a single turn, one of its heads dies. The hydra dies if all its heads are dead. At the end of each of its turns when it has at least one living head, the hydra grows two heads for each of its heads that died since its last turn, unless it has taken Fire damage since its last turn. The hydra regains 20 Hit Points when it grows new heads."
  - name: "Reactive Heads"
    desc: "For each head the hydra has beyond one, it gets an extra Reaction that can be used only for Opportunity Attacks."
actions:
  - name: "Multiattack"
    desc: "The hydra makes as many Bite attacks as it has heads."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +8, reach 10 ft. 10 (1d10 + 5) Piercing damage."
```
