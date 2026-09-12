---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e spell text for Armor of Agathys (not in the core SRD; sourced from the Player's Handbook)."
subtype: abjuration
tier: supporting
source: ""
source_url: "https://www.aidedd.org/spell/armor-of-agathys"
uid: f8f1e139-7f09-4ef3-bb16-8d63372bcc3e
---

# Armor of Agathys

**Level:** 1 — Abjuration ([[warlock|Warlock]])

**Casting Time:** Action

**Range:** Self

**Components:** V, S, M (a shard of blue glass)

**Duration:** 1 hour

A protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear. You gain 5 Temporary Hit Points for the duration. If a creature hits you with a melee attack while you have these Temporary Hit Points, the creature takes 5 Cold damage.

**_At Higher Levels._** When you cast this spell using a spell slot of 2nd level or higher, both the Temporary Hit Points and the Cold damage increase by 5 for each slot level above 1st.

## Simulation Data

```spell
name: Armor of Agathys
level: 1
school: abjuration
classes: [Warlock]
desc: "You gain 5 Temporary Hit Points. If a creature hits you with a melee attack while you have these Temporary Hit Points, the creature takes 5 Cold damage."
sim:
  temp_hp: { amount: 5 }
  retaliate: { kind: retaliate, trigger: hit_by_melee, while: temp_hp_remaining, damage: { dice: "5", type: cold } }
  notes: "The upcast +5/+5 per slot level above 1st isn't modeled (retaliate/temp_hp compile from a single flat sim block, not per-slot scaling)."
```
