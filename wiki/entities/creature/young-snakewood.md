---
title: "Young Snakewood"
aliases:
  - Young Snakewood
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Young Snakewood.md"
summary: "CR 4 terrace clonal vine ambusher. One short-range bundle grab carries prey into the low canopy, distinct from Vine Lash and adult Snakewood."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T19:57:00Z
updated: 2026-09-13T19:57:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: ambusher
cr: "4"
relationships:
  - target: "[[snakewood]]"
    type: related_to
  - target: "[[vine-lash]]"
    type: related_to
  - target: "[[old-gardens]]"
    type: related_to
---
# Young Snakewood

> [!narration] Narration
> On the first terraces, ordinary vines hang in the low canopy. Five or six stems tighten together, and tiny flowers show inside a forming wedge. The low branches shake when the stems draw tight.

## Statblock

```statblock
layout: Basic 5e Layout
name: "Young Snakewood"
size: Large
type: plant
alignment: unaligned
ac: "14 (layered stems)"
hp: 68
hit_dice: "8d10 + 24"
speed: "0 ft."
stats: [18, 14, 16, 2, 13, 3]
skillsaves:
  - Perception: 3
  - Stealth: 6
condition_immunities: "prone"
senses: "blindsight 30 ft. while in contact with vegetation, passive Perception 13"
languages: "—"
cr: 4
traits:
  - name: "False Appearance"
    desc: "While the young Snakewood remains motionless among vegetation, it is indistinguishable from an ordinary mass of jungle vines."
  - name: "Root-Anchored"
    desc: "The young Snakewood cannot willingly move its root crown and can't be knocked prone or moved against its will. Its articulated body can strike anywhere within 30 feet of the root crown, provided continuous branches, trunks, or other substantial vegetation connect it to that space."
  - name: "Clonal Bundle"
    desc: "A creature grappled by the young Snakewood can attack the grasping bundle directly (AC 14; 10 hit points). Damage to the bundle doesn't reduce the young Snakewood's hit points. If the bundle is destroyed, that grapple ends; a replacement bundle forms at the beginning of the young Snakewood's next turn."
actions:
  - name: "Multiattack"
    desc: "The young Snakewood makes one Snatching Jaws attack and, if a creature began its turn grappled by it, either uses Constrict or Reel."
  - name: "Snatching Jaws"
    desc: "Melee Weapon Attack: +6 to hit, reach 30 ft., one Large or smaller creature. Hit: 11 (2d6 + 4) piercing damage, and the target is Grappled (escape DC 14). Until this grapple ends, the target is Restrained. The young Snakewood can grapple only one creature at a time."
  - name: "Reel"
    desc: "The young Snakewood pulls its grappled creature up to 10 feet toward the canopy. If this movement leaves the victim unsupported, it hangs suspended."
  - name: "Constrict"
    desc: "One creature grappled by the young Snakewood takes 13 (2d8 + 4) bludgeoning damage."
```

## Behavior


- **Habitat.** First terraces and orchard edges such as [[old-gardens]], where connected low branches provide the skeleton. Adults live farther in.
- **Behavior.** At rest it is ordinary vines. When it strikes, stems braid into a wedge, clap shut, and lift prey into the low canopy.
- **Diet.** Terrace prey plentiful enough to practice the adult feeding loop.
- **Social Structure.** Clonal juvenile of the same liana as adult Snakewood. Keep [[vine-lash]] on narrow trail lanes and young Snakewood on wider canopy lanes.

## Tactics


- **Signs.** Five or six stems tighten. Tiny flowers appear inside the closing jaw. Low canopy shakes.
- **Instincts.** One target. Practice grab-and-lift where vegetation connects.
- **Tactics.** Round 1 Snatching Jaws. Round 2 Constrict or Reel if the grab holds.
- **Weaknesses.** Attack the bundle (AC 14, 10 HP). Escape DC 14. Leave the 30-foot vegetation lane. Burn the stems. It cannot chase.
- **Aftermath.** Cut bundles leave sweet flowers and pale resin. Severed stems remain viable if replanted near connected terrace trees.
