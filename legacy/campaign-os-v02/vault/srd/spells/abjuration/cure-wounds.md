---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith, nature, healing]
summary: "5e SRD spell text for Cure Wounds."
subtype: abjuration
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 5b40c5db-132d-4a6f-9e98-662e938d497f
---

# Cure Wounds

**Level:** 1 — Abjuration ([[bard|Bard]], [[cleric|Cleric]], [[druid|Druid]], [[paladin|Paladin]], [[ranger|Ranger]])

**Casting Time:** Action

**Range:** Touch

**Components:** V, S

**Duration:** Instantaneous

A creature you touch regains a number of Hit Points equal to 2d8 plus your spellcasting ability modifier.

**_Using a Higher-Level Spell Slot._** The healing increases by 2d8 for each spell slot level above 1.

## Simulation Data

```spell
name: Cure Wounds
level: 1
school: abjuration
classes: [Bard, Cleric, Druid, Paladin, Ranger]
desc: "A creature you touch regains a number of Hit Points equal to 2d8 plus your spellcasting ability modifier."
sim:
  heal: { dice: "2d8", add_ability_mod: true }
  scaling:
    per_slot_above: { heal_dice: "2d8" }
```
