---
title: Aruhe - Crown Squid
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (wiki creature.aruhe-crown-squid; CR 11 simplification)"
  - "wiki/_archive/aruhe-crown-squid.md"
summary: Gargantuan canopy predator that selects isolated prey, reels it above the forest floor, and pursues through connected crowns.
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.0
base_confidence: 0.4
lifecycle: proposed
lifecycle_changed: 2026-09-12
tier: supporting
created: 2026-09-12T09:30:00Z
updated: 2026-09-12T00:00:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: controller
cr: 17
relationships:
  - target: "[[Aruhe - Quiet Forest]]"
    type: related_to
  - target: "[[Aruhe - The Marshes]]"
    type: related_to
  - target: "[[Aruhe - Terror-Bird]]"
    type: related_to
---
# Aruhe - Crown Squid

![[attachments/shattered-sea/creatures/great-crown-squid-of-aruhe-01.jpg|Great Crown Squid of Aruhe]]

> [!narration] Narration
> The Great Crown Squid hangs between mature trees, its broad translucent mantle held above eight muscular arms. Hooked suckers line the arms, while finer tendrils hang toward the ground and sway with the damp air. Its body stays nearly still as its eyes track movement through the leaves.

## Statblock

```statblock
layout: Basic 5e Layout
name: "Great Crown Squid"
size: Gargantuan
type: monstrosity
alignment: unaligned
ac: 17
hp: 283
hit_dice: "21d20 + 63"
speed: "20 ft., climb 50 ft."
stats: [24, 20, 17, 7, 20, 6]
saves:
  - dexterity: 11
  - constitution: 9
  - wisdom: 11
skillsaves:
  - Athletics: 13
  - Perception: 17
  - Stealth: 11
senses: "darkvision 120 ft., passive Perception 27"
languages: "—"
cr: 17
traits:
  - name: "Canopy Camouflage"
    desc: "While among foliage, branches, or hanging roots, the squid can Hide even when lightly obscured. If it has not moved since the end of its previous turn, it has advantage on Dexterity (Stealth) checks."
  - name: "Eight-Eyed Awareness"
    desc: "The squid has advantage on Wisdom (Perception) checks relying on sight and cannot be surprised while conscious unless the surprising creature is inside its Mouth-Blind Zone."
  - name: "Mouth-Blind Zone"
    desc: "The squid cannot visually perceive a creature within 10 feet directly beneath the center of its mantle unless that creature is grappled by the squid or touching one of its arms. Such a creature is unseen by the squid, and the squid cannot make opportunity attacks against it."
  - name: "Spider-Braced"
    desc: "While at least three primary arms touch solid surfaces, the squid cannot be knocked prone or moved against its will."
  - name: "Buoyant Mantle"
    desc: "The squid takes no falling damage while its gas mantle remains intact and falls no faster than 60 feet per round. It cannot use this trait to fly."
  - name: "Siege Predator"
    desc: "The squid deals double damage to objects and structures. Nonmagical plant growth never costs it additional movement."
  - name: "Selected Prey"
    desc: "The squid has advantage on its first Hookline Tentacle attack each turn against a creature that has no conscious ally within 10 feet."
actions:
  - name: "Multiattack"
    desc: "The squid makes three attacks, only one of which can be a Beak attack."
  - name: "Hookline Tentacle"
    desc: "Melee Weapon Attack: +11 to hit, reach 80 ft., one creature. Hit: 18 (2d10 + 7) slashing damage, and the target has the Grappled and Restrained conditions (escape DC 19). The squid can maintain up to four Hookline grapples at once."
  - name: "Crushing Arm"
    desc: "Melee Weapon Attack: +13 to hit, reach 20 ft., one creature. Hit: 25 (4d8 + 7) bludgeoning damage. The squid can grapple the target (escape DC 19) or push it up to 20 feet."
  - name: "Beak"
    desc: "Melee Weapon Attack: +13 to hit, reach 10 ft., one creature grappled by the squid. Hit: 33 (4d12 + 7) piercing damage."
  - name: "Reel"
    desc: "Each creature grappled by a Hookline is pulled up to 30 feet directly toward the squid."
  - name: "Canopy Pounce (Recharge 5–6)"
    desc: "The squid moves up to its climb speed without provoking opportunity attacks, provided it ends that movement touching a tree or similarly massive structure. At any two points during this movement, it can make a Hookline Tentacle attack."
legendary_actions:
  - name: ""
    desc: "The squid can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The squid regains spent legendary actions at the start of its turn."
  - name: "Skitter"
    desc: "The squid moves up to 20 feet using its climb speed without provoking opportunity attacks."
  - name: "Hookline"
    desc: "The squid makes one Hookline Tentacle attack."
  - name: "Reel"
    desc: "One creature grappled by the squid is pulled up to 20 feet toward it."
  - name: "Rip Through (Costs 2)"
    desc: "The squid tears apart a 10-foot cube of nonmagical wood or vegetation within reach. Creatures in that area make a DC 19 Dexterity saving throw, taking 18 (4d8) bludgeoning damage and falling prone on a failure, or half damage on a success. The destroyed area becomes difficult terrain."
```

## Behavior

- **Habitat.** Adults hold connected mature canopy in [[Aruhe - Quiet Forest|the Quiet]], [[Aruhe - The Marshes|the Marshes]], and the roof of [[Aruhe - The Mangroves|the Mangroves]]. The interrupted trees of [[Aruhe - Old Gardens|the Old Gardens]] support juveniles but usually not adults.
- **Habits.** The squid braces several arms against separate trunks and watches before committing. Its gas-filled mantle makes its weight seem wrong on the branches, allowing it to cross canopy gaps with little movement below.
- **Diet.** It eats large animals, travelers, and anything it can lift into the canopy. Terror-Birds are dangerous prey, Bear-Elk are very dangerous prey, and Wolfrabbits are easy meals.
- **Social structure.** Each adult is solitary and treats other large predators as boundaries rather than allies. It avoids broad grassland, open shoreline, and river water occupied by otter families.

## Hunt

- **Signs.** Look for sucker scars high on trunks, bark stripped upward, broken branches that never fell, polished antler without a nearby carcass, and prey tracks that end above the ground.
- **Opening.** The squid watches the group and targets a straggler, a wounded creature, or anyone carrying meat. Its first Hookline attack has advantage when the target lacks a conscious ally within `10 feet`.
- **Pressure.** It uses Hookline Tentacles to lift and reel prey, then closes with a Beak attack. It crosses connected crowns with Canopy Pounce and destroys vegetation that blocks its route.
- **Shut-down.** Broad open ground, deep occupied water, low terrain, a tight group, and the Mouth-Blind Zone deny it clean attacks. It becomes a committed pursuer only after suffering serious injury; otherwise, a failed grab makes it relocate and select another target.
- **Aftermath.** A hunt leaves torn canopy, sucker rings, sap-wet bark, broken vines, and blood high overhead. There is no planned treasure, although severed hooklines, hide, and mantle tissue may interest a careful harvester.
