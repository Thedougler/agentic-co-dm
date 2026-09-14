---
title: "Aruhe - Strangler Fig"
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:strangler-fig.md"
  - "/workspace/midchain-ingest/group-a/monsters/Strangler Fig.md"
summary: "CR 8 strangling fig controller from living-stock ecology."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T20:00:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: "controller"
cr: "8"
relationships:
  - target: "[[Aruhe]]"
    type: related_to
---
# Aruhe - Strangler Fig

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> Single strangler figs grow on game trails already squeezed through stone. Aerial roots hang in curtains and reach; the trunk is hollow, with old kills showing as bones in the bark. The tree does not walk and does not need to.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Strangler Fig"
size: Huge
type: plant
alignment: unaligned
ac: "15 (natural armor)"
hp: 126
hit_dice: "12d12 + 48"
speed: "0 ft."
stats: [20, 6, 18, 1, 10, 1]
damage_vulnerabilities: "fire"
damage_resistances: "bludgeoning, piercing"
condition_immunities: "blinded, deafened, frightened"
senses: "blindsight 60 ft. (blind beyond this radius), passive Perception 10"
languages: "—"
cr: 8
traits:
  - name: "False Appearance"
    desc: "While the strangler fig remains motionless, it is indistinguishable from a normal tree."
  - name: "Rooted"
    desc: "The strangler fig cannot move or be moved by any effect."
actions:
  - name: "Multiattack"
    desc: "The strangler fig makes two Root Lash attacks and, if a creature is already grappled by it, uses Hollow-Trunk Engulf on one grappled creature. Alternatively, it makes three Root Lash attacks."
  - name: "Root Lash"
    desc: "Melee Weapon Attack: +8 to hit, reach 20 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage, and the target is Grappled (escape DC 16). The strangler fig can grapple up to three creatures at a time."
  - name: "Trail-Pinch (Recharge 5–6)"
    desc: "Roots erupt along a 30-foot-long, 10-foot-wide line on the ground that begins at a point within 60 feet of the fig. Each creature in the line must make a DC 16 Dexterity saving throw, taking 18 (4d8) bludgeoning damage and being pulled up to 10 feet toward the fig on a failed save, or taking half as much damage without the pull on a successful one. Until the start of the fig's next turn, the line becomes an aerial-root curtain: it is difficult terrain and lightly obscured. A creature can clear one 5-foot square of curtain as an action."
  - name: "Hollow-Trunk Engulf"
    desc: "One Large or smaller creature grappled by the strangler fig is pulled into its hollow trunk and becomes Restrained. The creature takes 14 (4d6) bludgeoning damage at the start of each of the fig's turns. As an action, the engulfed creature can make a DC 16 Strength (Athletics) or Dexterity (Acrobatics) check, ending the effect on itself on a success. An ally adjacent to the trunk can use an action to make the same check to pull the creature free. The fig can engulf one creature at a time."
```
```
````

## Behavior

- **Habitat.** Single figs grow on game trails already squeezed through stone. The tree does not walk and does not need to. A trail bend, a low ceiling, or a harmless-looking root curtain is enough; leave at least one route that can be cleared or abandoned.
- **Behavior.** Single strangler figs grow on game trails already squeezed through stone. Aerial roots hang in curtains and reach; the trunk is hollow, with old kills showing as bones in the bark. The tree does not walk and does not need to.
- **Diet.** Source is silent unless named above.
- **Social Structure.** Source is silent unless named above.

## Tactics

**Tactic:** let a trail pinch itself → aerial roots reach from the curtain → one victim disappears into the hollow trunk. **Tell:** curtains of roots hang across a game trail already squeezed through stone; old bones show in the bark.
