---
type: monster
campaign: shattered-sea
region: aruhe
role: skirmisher
cr: 4
source: house (wiki creature.wolfrabbit; living-stock 2026-09-05; 2024 CR 4 conversion)
visibility: dm
tags: [monster, aruhe]
summary: CR 4 pack skirmisher that uses a 30-foot pounce to knock targets prone and lets nearby packmates rend them; the visual reference anchors a tall, tawny, dark-striped feline with oversized ears.
---
# Wolfrabbit
## Statblock

````col
```col-md
flexGrow=3
===
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-v2.jpg|Wolfrabbit of Aruhe]]
![[attachments/shattered-sea/creatures/wolfrabbit-of-aruhe-token.png|Wolfrabbit of Aruhe Foundry VTT token]]

> [!narration] Narration
> A dark-striped hunting cat crouches over the boat, its enormous ears pricked above a broad, furred head. Red eyes track you through the terrace brush, a twitching nose wet with saliva and hooked claws gripping the rim. Wolf-sized and built to spring, it can cross the gap before the boat clears the bank.
```

```col-md
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
    desc: "The wolfrabbit jumps up to 30 feet, without needing a running start, to an unoccupied space it can see, then makes one Raking Claws attack against one creature within 5 feet of where it lands. If the wolfrabbit moved at least 20 feet straight toward the target and the attack hits, the target must succeed on a DC 15 Strength saving throw or have the Prone condition. On a successful save, the wolfrabbit can move up to 10 feet without provoking Opportunity Attacks from the target."
bonus_actions:
  - name: "Devour the Pack"
    desc: "The wolfrabbit tears into the corpse of another wolfrabbit within 5 feet that died since the end of the wolfrabbit's previous turn. A corpse can be targeted only once by this bonus action. The wolfrabbit gains 10 temporary Hit Points and enters a frenzy until the end of its next turn. During the frenzy, its Speed increases by 10 feet and its Bite deals an extra 3 (1d6) Piercing damage."
reactions:
  - name: "Frenzy Toward the Fallen"
    desc: "Trigger: Another wolfrabbit the wolfrabbit can see within 30 feet drops to 0 Hit Points. Response: The wolfrabbit moves up to 15 feet toward that creature's space without provoking Opportunity Attacks."
```
```
````

## Visual reference

The supplied reference sheet establishes the Wolfrabbit as a tall, serval-like feline with very large upright ears, a tawny coat broken by dark stripes and spots, a pale muzzle and throat, red-orange eyes, dark nose and claws, and a long banded tail. Its low torso and long legs keep the silhouette spring-built rather than rabbit-shaped.

![[wolfrabbit-of-aruhe-reference-sheet.jpg|Wolfrabbit character reference sheet]]

## Behavior

**Habitat.** Wolfrabbits keep to the collapsed first terraces of Aruhe, where they can spring from broken walls and vanish into brush. Packs of four to six hunt at dawn and dusk, and a bound from a terrace wall can cover 30 feet.

**Behavior.** A Wolfrabbit is a wolf-sized, dark-striped hunting cat with long ears, a twitching nose, and a body built to spring. The pack's warrens honeycomb the terrace stone. When one falls, the others eat it from hunger rather than spite. They will not den past the Old Mouth once daylight dies in the tube; something below outranks them.

**Diet.** They break a pounce for the smell of a mature [[Aruhe - Grubnade|Grubnade]], and they jump [[Aruhe - Razer-Grass]] stands rather than land in them. They know [[Snakewood]] strike-lanes and will drive prey under those branches on purpose.

**Social Structure.** Packs work as a single hunting body, but each Wolfrabbit still reacts to a fallen packmate. The corpse-eating is hunger, not spite.

## Tactics

**Signs.** Paired claw marks in terrace stone, dark fur caught on wall edges, small warrens opening between fallen blocks, and fresh tracks that break into long launch lines mark a Wolfrabbit pack's ground.

**Instincts.** The pack isolates anything bleeding, knocks it down with a long bound, and closes around a creature that has lost its footing. It avoids [[Aruhe - Razer-Grass]] and abandons a pounce when it smells a mature [[Aruhe - Grubnade|Grubnade]].

**Tactics.** A Wolfrabbit begins from a wall, boat rim, or terrace break with Pouncing Bound, then uses Multiattack against a Prone target while another packmate stays close enough to trigger Pack Rend. When a packmate falls, the others leap toward it; when one can reach the corpse safely, it devours the body and surges back into the hunt.

**Weaknesses.** A Wolfrabbit loses Pack Rend when separated from its pack, and its pounce is easier to deny in tight spaces or against a creature that holds its ground. Razer-Grass, mature Grubnades, and broken launch lines turn its preferred approach into a liability.

**Aftermath.** A Wolfrabbit encounter leaves paired claw marks in stone, torn fur on terrace edges, fresh blood drawn toward a warren, and packmate remains too mangled for ordinary scavengers. Aruhe removes brakes from a known animal; the Blight pressures the garden and does not ride the pack.
