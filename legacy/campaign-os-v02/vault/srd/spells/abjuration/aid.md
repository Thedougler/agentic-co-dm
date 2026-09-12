---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith, nature]
summary: "5e SRD spell text for Aid."
subtype: abjuration
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: c51dbd9a-5bba-4230-a63a-663ec811ecf2
---

# Aid

**Level:** 2 — Abjuration ([[bard|Bard]], [[cleric|Cleric]], [[druid|Druid]], [[paladin|Paladin]], [[ranger|Ranger]])

**Casting Time:** Action

**Range:** 30 feet

**Components:** V, S, M (a strip of white cloth)

**Duration:** 8 hours

Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5 for the duration.

**_Using a Higher-Level Spell Slot._** Each target's Hit Points increase by 5 for each spell slot level above 2.

## Simulation Data

```spell
name: Aid
level: 2
school: abjuration
classes: [Bard, Cleric, Druid, Paladin, Ranger]
desc: "Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5."
sim:
  temp_hp: { amount: 5 }
  range: 30
  notes: "Only the caster's own +5 is modeled as temp_hp (a persistent max-HP increase, not literally temporary); the up-to-three-ally targeting and the real max-HP-increase semantics aren't modeled (no ally-buff primitive)."
```
