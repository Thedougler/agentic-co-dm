---
title: Aruhe - River Otter
aliases:
  - Aruhe - River Otter
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (wiki creature.aruhe-river-otter; living-stock 2026-09-05; individual chassis provisional)"
summary: CR 4 controller that shifts from playful gear-tugging to coordinated underwater holds. Pale chest marks identify family members.
provenance:
  extracted: 0.97
  inferred: 0.03
  ambiguous: 0.0
base_confidence: 0.4
lifecycle: canon
lifecycle_changed: 2026-09-12
tier: supporting
created: 2026-09-12T05:40:07Z
updated: 2026-09-12T10:00:00Z
type: creature
reveal: revealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: controller
cr: 4
relationships:
  - target: "[[the-river]]"
    type: related_to
  - target: "[[clear-lake]]"
    type: related_to
  - target: "[[crown-squid]]"
    type: related_to
---
# Aruhe - River Otter

> [!narration] Narration
> Twelve-foot chocolate-black river otters work the river and clear lake in blood-kin families, their pale throat marks as distinct as fingerprints. They roll through the shallows with rope, oars, ankles, or a dead Deer-Stalker's head as if every loose thing in the water has joined their game. Clear water surrounds them, and the whole family goes still when play becomes a hunt.

## Statblock

![[attachments/shattered-sea/creatures/aruhe-river-otter-token.png|Aruhe River Otter Foundry VTT token]]
```statblock
layout: Basic 5e Layout
name: "Aruhe River Otter"
size: Large
type: monstrosity
alignment: unaligned
ac: 15
hp: 76
hit_dice: "9d10 + 27"
speed: "20 ft., swim 40 ft."
stats: [18, 16, 16, 6, 14, 8]
skillsaves:
  - Athletics: 6
  - Perception: 4
  - Stealth: 5
senses: "darkvision 60 ft., passive Perception 14"
languages: "—"
cr: 4
traits:
  - name: "Hold Breath"
    desc: "The otter can hold its breath for 30 minutes."
  - name: "Family Memory"
    desc: "The family remembers fire, ropes, and who enters the water (DM tags)."
  - name: "Watery Ambush"
    desc: "Hunt mode only. The otter has advantage on attack rolls against creatures in the water if at least one other otter is within 10 feet of the target."
actions:
  - name: "Multiattack (Hunt)"
    desc: "The otter makes one Bite attack and one Tail attack."
  - name: "Bite"
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 4) piercing damage, and if the target is Medium or smaller it has the Grappled condition (escape DC 14)."
  - name: "Tail"
    desc: "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."
  - name: "Dunk (Recharge 5–6)"
    desc: "One creature Grappled by the otter is pulled up to 20 feet and shoved underwater, or held under if already in water. The target has the Restrained condition until the grapple ends."
bonus_actions:
  - name: "Tug Toy (Play mode only)"
    desc: "Contested Athletics or Sleight of Hand against a held or worn object within 5 feet, or a trailing rope. On a success, the otter takes the object and swims 10 feet; no damage."
```
## Visual reference

![[attachments/shattered-sea/creatures/aruhe-river-otter-reference-sheet.jpg|Aruhe River Otter character reference sheet]]

## Biology


Aruhe River Otters are twelve-foot, stocky, wet-furred animals with dark chocolate-brown coats and thick tapered tails. Amber-brown eyes, dark noses, small rounded ears, and long pale whiskers sit on blunt heads. Webbed paws end in sharp dark claws. A pale cream throat and chest mark, fingerprint-like, identifies each animal in the family.

## Behavior


- **Habitat.** Families hold [[the-river|the river]] and [[clear-lake|the clear lake]], especially open cuts where bank, shallows, and deep water let them watch both land and current.
- **Behavior.** They play first. Rope, oars, ankles, trailing packs, and a [[Deer-Stalker|Deer-Stalker's]] antlered head can become tug toys in the shallows. The family treats an entry into the water as joining the game. Responding to play gives the family a new game.
- **Diet.** They eat river animals and bank grazers. They also take careless predators and Deer-Stalkers for sport as much as food. They avoid hauling kills onto [[razer-grass|razer-grass]].
- **Social Structure.** Families hold four to six adults plus pups. Play is blood kin only. Harm to an adult or contact with a pup shifts the whole family from game to military silence. Overstaying in claimed water has the same result.

## Tactics


- **Signs.** Glass-clear water, polished slides in mud, pale throat flashes below the waterline, and ropes drawn tight from under a boat. Oars tugged from hands and a recently killed Deer-Stalker head can bob where no current should hold them.
- **Instincts.** The family watches first, then steals gear. It tests reactions before dunking and releasing a trespasser. It commits fully only after a trespasser crosses the line. What comes from the river belongs to the family.
- **Tactics.** In play mode, the family shares initiative and avoids damage. In hunt mode, adults use Watery Ambush and Dunk to split one target from the group. The adults apply the Grappled condition while the others show only wakes.
- **Weaknesses.** They dominate occupied water but are less willing to fight on dry land or any haul-out that traps their bodies away from the current. The family remembers fire, ropes, and repeated tricks. A clever party can bait, redirect, or avoid them.

