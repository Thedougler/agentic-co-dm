---
title: Wolfrabbit
aliases:
  - Wolfrabbit
  - Wolfrabbits
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:wolfrabbits.md"
  - "house (wiki creature.wolfrabbit; living-stock 2026-09-05; 2024 CR 4 conversion)"
  - "Session 12 refile (2026-09-27)"
created: 2026-09-12
updated: 2026-09-27
type: creature
reveal: revealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: skirmisher
cr: 4
summary: "A CR 4 pack-hunting rabbit the size of a wolf that knocks prey down with a long bound and tears it apart with its packmates; two answer a claim in Aruhe's grass."
---
# Wolfrabbit

![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-reference-sheet.jpg|Wolfrabbit reference sheet]]
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-v2.jpg|Wolfrabbit of Aruhe]]

````col
```col-md
flexGrow=2
===
## At a Glance

Wolfrabbits are the island's answer in the grass: a pack that bounds in from cover, knocks one body flat, and closes around it.

- **Habitat.** The collapsed first terraces of [[old-gardens]] and Aruhe's grassland, hunting at dawn and dusk. Two answer a claim made in grass or on the terraces ([[taking-on-aruhe]]).
- **Treasure.** None. Their warrens honeycomb the terrace stone.
```

```col-md
flexGrow=1
===
> [!narration] Wolfrabbit
> A wolfrabbit is a rabbit grown to the size of a wolf, with upright ears as long as a forearm and heavy haunches built for the long bound. Its tawny coat is barred with dark stripes and pales at the muzzle and throat, and hooked black claws curl from forepaws where a hare's would be soft. Red-orange eyes sit over a twitching wet nose. A pack lies flat along terrace walls and in the long grass, ears turning, ready to spring.
```
````

## Statblock

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
  - perception: 5
  - stealth: 7
senses: "Darkvision 60 ft., Passive Perception 15"
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
    desc: "Melee Attack Roll: +7, reach 5 ft., one target. Hit: 14 (2d8 + 5) Piercing damage."
  - name: "Raking Claws"
    desc: "Melee Attack Roll: +7, reach 5 ft., one target. Hit: 12 (2d6 + 5) Slashing damage."
  - name: "Pouncing Bound"
    desc: "The wolfrabbit jumps up to 30 feet, without needing a running start, to an unoccupied space it can see, then makes one Raking Claws attack against one creature within 5 feet of where it lands. If it moved at least 20 feet straight toward the target and the attack hits, the target must succeed on a DC 15 Strength saving throw or have the Prone condition. On a successful save, the wolfrabbit can move up to 10 feet without provoking Opportunity Attacks from the target."
bonus_actions:
  - name: "Devour the Pack"
    desc: "The wolfrabbit tears into the corpse of another wolfrabbit within 5 feet that died since the end of its previous turn. A corpse can be targeted only once by this bonus action. The wolfrabbit gains 10 temporary Hit Points and enters a frenzy until the end of its next turn. During the frenzy, its Speed increases by 10 feet and its Bite deals an extra 3 (1d6) Piercing damage."
reactions:
  - name: "Frenzy Toward the Fallen"
    desc: "Trigger: Another wolfrabbit the wolfrabbit can see within 30 feet drops to 0 Hit Points. Response: The wolfrabbit moves up to 15 feet toward that creature's space without provoking Opportunity Attacks."
```

## Tactics

- **Opening.** From a wall, a boat rim, or the edge of long grass, one uses Pouncing Bound to knock a target Prone, and the rest close in so Pack Rend applies.
- **Signature.** The pounce. Its tell is a launch line: a wolfrabbit flattening with its ears back, 20 to 30 feet away. Answers: stand in tight spaces with no landing room, keep packmates apart so Pack Rend fails, or stand behind [[razer-grass]].
- **Adapts.** When a packmate falls, the others leap toward it with Frenzy Toward the Fallen, and the first to reach the corpse devours it and surges back in.
- **Weaknesses.** Separation, tight spaces, razer-grass, broken launch lines, and the smell of a mature [[grubnade]], which breaks a pounce.
- **Morale.** A pack breaks off once half its members are down, carrying nothing.

## Behavior

- **Habits.** Packs of four to six hunt at dawn and dusk and den in warrens between fallen terrace blocks. They will not den past the Old Mouth once daylight leaves the tube.
- **Diet.** Anything bleeding. When one falls, the others eat it from hunger.
- **Group.** A pack hunts as one body, and each member reacts to a fallen packmate.
- **Signs.** Paired claw marks in terrace stone, dark fur caught on wall edges, small warrens between fallen blocks, and tracks that break into long launch lines.
- **Aftermath.** Claw marks in stone, torn fur on terrace edges, blood drawn toward a warren, and packmate remains too mangled for other scavengers.

## Art

### Token

![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-token.jpg|Wolfrabbit token]]
