---
title: "Vine Lash"
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:vine-lash.md"
  - "/workspace/midchain-ingest/group-a/monsters/Vine Lash.md"
summary: "CR 3 trail-controller vine that hangs as rope, whips, wraps, and squeezes; fire and breakable bundles are the answers."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T19:59:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: controller
cr: "3"
relationships:
  - target: "[[Young Snakewood]]"
    type: related_to
  - target: "[[Aruhe - Snakewood]]"
    type: related_to
---
# Vine Lash

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> Shoulder-thick leafless hangers drape over a trail like ordinary rope. Five or six rope-thick stems hang together from the canopy in one grasping bundle. The tendrils twitch only after something enters the trail lane.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Vine Lash"
size: Medium
type: plant
alignment: unaligned
ac: "12 (natural armor)"
hp: 52
hit_dice: "8d8 + 16"
speed: "10 ft., climb 10 ft."
stats: [14, 8, 14, 1, 10, 1]
damage_vulnerabilities: "fire"
condition_immunities: "blinded, deafened, frightened"
senses: "blindsight 30 ft. (blind beyond this radius), passive Perception 10"
languages: "—"
cr: 3
traits:
  - name: "False Appearance"
    desc: "While the vine lash remains motionless, it is indistinguishable from ordinary jungle vines."
  - name: "Spider Climb"
    desc: "The vine lash can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
  - name: "Distributed Grip"
    desc: "A creature grappled by the vine lash can use its action to attack the grasping bundle (AC 12; 8 hit points). Damage to the bundle doesn't damage the vine lash; reducing the bundle to 0 hit points ends that grapple."
actions:
  - name: "Multiattack"
    desc: "The vine lash makes two Tendril attacks, or it makes one Tendril attack and uses Constrict against one creature it already grapples."
  - name: "Tendril"
    desc: "Melee Weapon Attack: +4 to hit, reach 15 ft., one creature. Hit: 7 (2d4 + 2) bludgeoning damage, and the target is Grappled (escape DC 12). The vine lash can grapple up to two creatures at a time."
  - name: "Constrict"
    desc: "One creature grappled by the vine lash takes 9 (2d6 + 2) bludgeoning damage. The grapple remains until the target escapes or the grasping bundle is destroyed."
```
```
````

## Behavior

- **Habitat.** First terraces of [[Aruhe]]. Keep these on narrow trail lanes; [[Young Snakewood]] keeps wider canopy lanes.
- **Behavior.** Hang as ordinary rope, then whip, wrap, and squeeze, drinking through roots.
- **Diet.** Prey held under the canopy long enough to feed.
- **Social Structure.** Trail ambush plants; place a second vine on a separate lane, not the same target.

## Tactics

- **Signs.** Shoulder-thick leafless hangers; tendrils twitch after something enters the lane.
- **Instincts.** Establish grapple, then squeeze or grab another.
- **Tactics.** Two Tendrils opening; Tendril plus Constrict while a grab holds.
- **Weaknesses.** Escape DC 12; attack the bundle (AC 12, 8 HP); fire vulnerability; leave the trail lane.
- **Aftermath.** Burned bundles leave sweet-smelling ash and tough wet cord; do not harvest while twitching.
