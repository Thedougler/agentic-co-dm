---
title: "Corpsewood"
category: entities
tags: [shattered-sea, creature, aruhe]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Corpsewood.md"
summary: "CR 12 corpsewood bruiser from living-stock ecology."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T20:00:00Z
updated: 2026-09-13T20:00:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: "bruiser"
cr: "12"
relationships:
  - target: "[[Aruhe]]"
    type: related_to
---
# Corpsewood

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> A dead tree walks: forty feet of split bark and dragging roots. It patrols deep [[The Rot]] on a seasonal beat and never leaves the tree line. Fire is the one thing that stops it knitting itself back together. The wood died years ago; what moves it did not.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Corpsewood"
size: Gargantuan
type: plant
alignment: unaligned
ac: "16 (natural armor)"
hp: 195
hit_dice: "13d20 + 65"
speed: "20 ft."
stats: [24, 6, 20, 1, 12, 1]
damage_vulnerabilities: "fire"
damage_resistances: "bludgeoning"
condition_immunities: "frightened, prone"
senses: "blindsight 60 ft. (blind beyond this radius), passive Perception 11"
languages: "—"
cr: 12
traits:
  - name: "Siege Monster"
    desc: "The corpsewood deals double damage to objects and structures."
  - name: "Corrupted Ground"
    desc: "The ground within 15 feet of the corpsewood is difficult terrain for creatures other than plants."
  - name: "Blight-Fed Regeneration"
    desc: "The corpsewood regains 10 hit points at the start of its turn if it has at least 1 hit point. If it took fire damage since the end of its previous turn, this trait doesn't function at the start of this turn. Fire visibly blackens the seams where the wood was knitting."
actions:
  - name: "Multiattack"
    desc: "The corpsewood makes three Slam attacks, or it makes two Slam attacks and uses Uproot if it is available."
  - name: "Slam"
    desc: "Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage."
  - name: "Uproot (Recharge 5–6)"
    desc: "The corpsewood tears the ground in a 20-foot-radius area centered on itself. Each creature in the area must make a DC 17 Dexterity saving throw, taking 36 (8d8) bludgeoning damage and falling Prone on a failed save, or taking half as much damage without falling Prone on a successful one."
```
```
````

## Behavior

- **Habitat.** Deep Rot, always near the tree line. It follows a seasonal beat and does not leave the forest. Silence moths, thornbacks, or ordinary Rot terrain can create movement problems, but the corpsewood should remain the obvious durable target rather than gain a pile of immunities.
- **Behavior.** A dead tree walks: forty feet of split bark and dragging roots. It patrols deep [[The Rot]] on a seasonal beat and never leaves the tree line. Fire is the one thing that stops it knitting itself back together. The wood died years ago; what moves it did not.
- **Diet.** Source is silent unless named above.
- **Social Structure.** Source is silent unless named above.

## Tactics

**Tactic:** patrol the deep Rot like a dead tree that refuses to stay broken; drag roots through the line, slam anything that blocks the beat, and uproot the ground when surrounded. **Tell:** split bark knits visibly until fire blackens the seams.
