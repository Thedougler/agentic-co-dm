---
title: "Vine Lash"
aliases:
  - Vine Lash
  - vine-lash
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:vine-lash.md"
  - "/workspace/midchain-ingest/group-a/monsters/Vine Lash.md"
  - "Session 12 refile (2026-09-27)"
created: 2026-09-13
updated: 2026-09-27
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: controller
cr: "3"
invention: true
summary: "A CR 3 carnivorous vine that hangs over Aruhe's trails like old rope, then whips, wraps, and squeezes; it is the island's answer to a claim on Quiet trails."
---
# Vine Lash

````col
```col-md
flexGrow=2
===
## At a Glance

A vine lash is the island's hand on its trails: it hangs still until someone walks under it or takes from the island, then grabs and squeezes.

- **Habitat.** Narrow trails through the first terraces of [[old-gardens]] and through [[the-quiet]], and coiled in the great vine's canopy at [[the-pantry]]. [[young-snakewood]] holds the wider canopy lanes.
- **Treasure.** None. Burned bundles leave tough wet cord and sweet ash.
```

```col-md
flexGrow=1
===
> [!narration] Vine Lash
> A vine lash is a bundle of pale, rope-thick stems wound round and round a branch over a trail, with a few loose strands hanging down to the height of a man's face. The stems are leafless and ringed with fine grey bark, and their tips end in thin fraying roots. It hangs so still that it passes for old rigging someone tied and forgot, until a strand twitches.
```
````

## Statblock

![[vine-lash-overview.png|Vine Lash overview: the disguised grasping bundle]]
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
damage_vulnerabilities: "Fire"
condition_immunities: "Blinded, Deafened, Frightened"
senses: "Blindsight 30 ft. (blind beyond this radius), Passive Perception 10"
languages: "—"
cr: "3"
traits:
  - name: "False Appearance"
    desc: "While the vine lash is motionless, it is indistinguishable from ordinary jungle vines."
  - name: "Spider Climb"
    desc: "The vine lash can climb difficult surfaces, including upside down on ceilings, without an ability check."
  - name: "Grasping Bundle"
    desc: "Each creature the vine lash grapples is held by its own bundle of stems (AC 12, 8 Hit Points). A creature can attack a bundle; damage to it doesn't harm the vine lash, and reducing it to 0 Hit Points ends that grapple."
  - name: "Island's Hand"
    desc: "When a creature makes a claim under Aruhe's law within 60 feet, the nearest vine lash wakes at the end of that creature's next turn. It attacks the marked creature first, then the nearest other creature within reach. It never attacks a creature that has eaten fallen fruit on Aruhe and made no claim since. It withdraws into the canopy when reduced to 26 Hit Points or fewer, or after 1 minute."
actions:
  - name: "Multiattack"
    desc: "The vine lash makes two Tendril attacks, or one Tendril attack and one use of Constrict."
  - name: "Tendril"
    desc: "Melee Attack Roll: +4, reach 15 ft. Hit: 7 (2d4 + 2) Bludgeoning damage, and the target has the Grappled condition (escape DC 12). While Grappled, the target's Speed is 0. The vine lash can grapple up to two creatures at a time."
  - name: "Constrict"
    desc: "One creature Grappled by the vine lash takes 9 (2d6 + 2) Bludgeoning damage. The grapple remains until the target escapes or its bundle is destroyed."
```

## Tactics

- **Opening.** Two Tendrils at whatever walks into reach, or at the marked creature when the island wakes it.
- **Signature.** Grab and squeeze. Its tell is a strand twitching after something enters the trail. Answers: escape with **Strength (Athletics)** or **Dexterity (Acrobatics)** `DC 12`, cut the bundle (AC 12, 8 HP), burn it, or leave its 15-foot reach.
- **Adapts.** Once it holds one creature, it Constricts it and reaches for a second.
- **Weaknesses.** Fire, bundles that break, and ground outside its reach. Its Blindsight finds an Invisible creature within 30 feet by touch.
- **Morale.** It withdraws into the canopy at 26 HP or fewer.

> [!narration] In action
> The rope over the path uncoils in one long crack, and a pale strand whips down and wraps twice around a body before anyone can shout.

## Behavior

- **Habits.** It hangs over narrow trail lanes, drinking through roots it sinks into the branch.
- **Diet.** Prey held under the canopy long enough to feed.
- **Group.** One to a lane. A second vine lash takes a separate lane, never the same target.
- **Signs.** Leafless hangers as thick as a wrist over a trail, and strands that twitch after something passes.
- **Aftermath.** Burned bundles leave sweet-smelling ash and tough wet cord, which twitches for an hour after the fire.

## Connections

- [[taking-on-aruhe]] — on Quiet trails, a vine lash is the island's default answer to a claim.
