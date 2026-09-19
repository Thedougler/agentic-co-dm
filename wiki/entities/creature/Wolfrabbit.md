---
title: Wolfrabbit
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:wolfrabbits.md"
  - "house (wiki creature.wolfrabbit; living-stock 2026-09-05; 2024 CR 4 conversion)"
summary: "CR 5 pack hunter that knocks targets prone and rends them with nearby packmates before feeding on fallen members."
provenance:
  extracted: 0.98
  inferred: 0.02
  ambiguous: 0.0
base_confidence: 0.4
lifecycle: proposed
lifecycle_changed: 2026-09-12
tier: supporting
created: 2026-09-12T00:00:00Z
updated: 2026-09-12T10:30:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: skirmisher
cr: 4
relationships:
  - target: "[[old-gardens]]"
    type: related_to
  - target: "[[razer-grass]]"
    type: related_to
  - target: "[[grubnade]]"
    type: related_to
---
# Wolfrabbit

> [!narration] Narration
> A dark-striped hunting cat crouches over the boat, its enormous ears pricked above a broad, furred head. Red eyes track you through the terrace brush. A twitching nose glistens with saliva while hooked claws grip the rim. Wolf-sized and built to spring, it can cross the gap before the boat clears the bank.

## Statblock
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-token.jpg|Wolfrabbit of Aruhe Foundry VTT token]]
```statblock
layout: Basic 5e Layout
name: "Wolfrabbit"
size: Medium
type: monstrosity
alignment: unaligned
ac: "15 (natural armor)"
hp: 68
hit_dice: "8d10 + 24"
speed: "50 ft."
stats: [20, 20, 16, 4, 16, 6]
skillsaves:
  - Perception: 5
  - Stealth: 7
senses: "darkvision 60 ft., passive Perception 15"
languages: "—"
cr: 4
traits:
  - name: "Standing Leap"
    desc: "The wolfrabbit can long jump up to 30 feet and high jump up to 15 feet, with or without a running start."
  - name: "Pack Rend"
    desc: "Once per turn when the wolfrabbit hits a Prone creature with its Bite, the attack deals an extra 5 (1d10) Piercing damage if another wolfrabbit is within 5 feet of the target."
  - name: "Blood-Scented"
    desc: "The wolfrabbit has Advantage on Wisdom (Perception) checks that rely on smell to locate a creature that doesn't have all its Hit Points."
actions:
  - name: "Multiattack"
    desc: "The wolfrabbit makes two attacks: one with its Bite and one with its Raking Claws."
  - name: "Bite"
    desc: "Melee Attack Roll: +7, reach 5 feet, one target. Hit: 14 (2d8 + 5) Piercing damage."
  - name: "Raking Claws"
    desc: "Melee Attack Roll: +7, reach 5 feet, one target. Hit: 12 (2d6 + 5) Slashing damage."
  - name: "Pouncing Bound"
    desc: "The wolfrabbit jumps up to 30 feet, without needing a running start, to an unoccupied space it can see, then makes one Raking Claws attack against one creature within 5 feet of where it lands. If it moved at least 20 feet straight toward the target and the attack hits, the target must succeed on a DC 15 Strength saving throw or have the Prone condition. On a successful save, the wolfrabbit can move up to 10 feet without provoking Opportunity Attacks from the target."
bonus_actions:
  - name: "Devour the Pack"
    desc: "The wolfrabbit tears into the corpse of another wolfrabbit within 5 feet that died since the end of its previous turn. A corpse can be targeted only once by this bonus action. The wolfrabbit gains 10 temporary Hit Points and enters a frenzy until the end of its next turn. During the frenzy, its Speed increases by 10 feet and its Bite deals an extra 3 (1d6) Piercing damage."
reactions:
  - name: "Frenzy Toward the Fallen"
    desc: "Trigger: Another wolfrabbit the wolfrabbit can see within 30 feet drops to 0 Hit Points. Response: The wolfrabbit moves up to 15 feet toward that creature's space without provoking Opportunity Attacks."
```

## Visual reference

The supplied reference sheet establishes the Wolfrabbit as a tall, serval-like feline with large upright ears, a tawny coat broken by dark stripes and spots, a pale muzzle and throat, red-orange eyes, dark nose and claws, and a long banded tail. Its low torso and long legs keep the silhouette spring-built rather than like a rabbit.

![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-reference-sheet.jpg|Wolfrabbit character reference sheet]]

## Behavior

- **Habitat.** Packs of four to six hunt the collapsed first terraces of [[old-gardens]] at dawn and dusk. Their warrens honeycomb the terrace stone, and a bound from a terrace wall can cover 30 feet.
- **Behavior.** A Wolfrabbit is a wolf-sized, dark-striped hunting cat with long ears and a body built to spring. When one falls, the others eat it from hunger rather than spite. They will not den past the Old Mouth once daylight dies in the tube. Something below drives them away.
- **Diet.** They avoid [[razer-grass]] and break a pounce for the smell of a mature [[grubnade|Grubnade]]. They drive prey toward [[snakewood]] strike-lanes.
- **Social Structure.** Packs hunt as one body, but each member reacts to a fallen packmate. Corpse-eating is hunger, not spite.

## Tactics

- **Signs.** Paired claw marks in terrace stone, dark fur caught on wall edges, small warrens opening between fallen blocks, and fresh tracks that break into long launch lines mark a pack's ground.
- **Instincts.** The pack isolates anything bleeding and knocks it down with a long bound. It closes around a creature that has lost its footing. It avoids razer-grass and abandons a pounce when it smells a mature Grubnade.
- **Tactics.** A Wolfrabbit begins from a wall, boat rim, or terrace break with Pouncing Bound, then uses Multiattack against a Prone target while another packmate stays close enough to trigger Pack Rend. When a packmate falls, the others leap toward it. A packmate finding the corpse safely devours it and surges back into the hunt.
- **Weaknesses.** Separation removes Pack Rend. Tight spaces or a creature that stands its ground can deny the pounce. Razer-Grass, mature Grubnades, and broken launch lines turn the preferred approach into a liability.
- **Aftermath.** An encounter leaves paired claw marks in stone, torn fur on terrace edges, fresh blood drawn toward a warren, and packmate remains too mangled for ordinary scavengers. The Blight pressures the garden but does not ride the pack.

## Art
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-v2.jpg|Wolfrabbit of Aruhe]]
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-token-stand.jpg|Wolfrabbit of Aruhe token stand]]
