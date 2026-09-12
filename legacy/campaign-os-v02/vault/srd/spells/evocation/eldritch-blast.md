---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, combat]
summary: "5e SRD spell text for Eldritch Blast."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: c99957f7-fde3-44ba-9699-762b2238c353
---

# Eldritch Blast

**Level:** Cantrip — Evocation ([[warlock|Warlock]])

**Casting Time:** Action

**Range:** 120 feet

**Components:** V, S

**Duration:** Instantaneous

You hurl a beam of crackling energy. Make a ranged spell attack against one creature or object in range. On a hit, the target takes 1d10 Force damage.

**_Cantrip Upgrade._** The spell creates two beams at level 5, three beams at level 11, and four beams at level 17. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.

## Simulation Data

```spell
name: Eldritch Blast
level: 0
school: evocation
classes: [Warlock]
desc: "You hurl a beam of crackling energy at one creature or object in range."
sim:
  attack_type: ranged_spell
  range: 120
  damage: [{ dice: "1d10", type: force }]
  cantrip_scaling:
    5: { attack_count: 2 }
    11: { attack_count: 3 }
    17: { attack_count: 4 }
```
