---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e spell text for Catapult (not in the core SRD; sourced from Xanathar's Guide to Everything, valid in 2024 rules)."
subtype: transmutation
tier: supporting
source: ""
source_url: "https://www.aidedd.org/dnd/sorts.php?vo=catapult"
uid: 5ca8490c-31fb-4cc8-b0ac-d77d84e0648e
---

# Catapult

**Level:** 1 — Transmutation ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 60 feet

**Components:** S

**Duration:** Instantaneous

Choose one unattended object within range that weighs 1 to 5 pounds. The object flies in a straight line up to 90 feet in a direction you choose, then falls, stopping early if it hits a solid surface.

If the object's path would strike a creature, that creature must make a [[dexterity|Dexterity]] saving throw. On a failed save, the object hits the target and stops moving; the object and the target each take 3d8 bludgeoning damage. On a success, the object continues to the end of its path and the creature takes no damage.

**_At Higher Levels._** When you cast this spell using a spell slot of 2nd level or higher, the maximum weight you can target increases by 5 pounds and the damage increases by 1d8 for each slot level above 1st.

## Simulation Data

```spell
name: Catapult
level: 1
school: transmutation
classes: [Sorcerer, Wizard]
desc: "A creature in the object's path must make a Dexterity saving throw or the object hits it."
sim:
  save: { ability: dex }
  half_on_save: false
  damage: [{ dice: "3d8", type: bludgeoning }]
  range: 60
  scaling:
    per_slot_above: { damage_dice: "1d8" }
  notes: "Requires an unattended 1-5 lb object in range — not itself verified by the engine."
```
