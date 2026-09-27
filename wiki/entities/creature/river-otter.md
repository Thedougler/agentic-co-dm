---
title: River Otter
aliases:
  - Aruhe - River Otter
  - River Otter
  - Aruhe River Otter
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (wiki creature.aruhe-river-otter; living-stock 2026-09-05; individual chassis provisional)"
  - "Session 12 refile (2026-09-27)"
created: 2026-09-12
updated: 2026-09-27
type: creature
reveal: revealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: controller
cr: 4
summary: "A CR 4 boat-length river otter that plays with anything in its water, and turns into a coordinated drowning hunter when play stops."
---
# River Otter

![[attachments/shattered-sea/creatures/aruhe-river-otter-reference-sheet.jpg|River Otter reference sheet]]

````col
```col-md
flexGrow=2
===
## At a Glance

A family of river otters owns every still pool and river cut on Aruhe, and anyone who enters their water has joined their game.

- **Habitat.** [[the-river]], [[clear-lake]], and the slack pools such as [[river-slack-basin]], wherever bank, shallows, and deep water meet. They are the island's responders in fresh water ([[taking-on-aruhe]]).
- **Treasure.** Whatever they have stolen: oars, rope, packs, and boots sunk in the mud of their slides.
```

```col-md
flexGrow=1
===
> [!narration] River Otter
> An Aruhe river otter is as long as a rowing boat, sleek and dark brown, with a pale cream patch on its chest whorled like a thumbprint. Long white whiskers fan from a blunt head, and amber eyes watch from just above the waterline. It rolls through the shallows with a length of rope or a broken oar clutched in its webbed claws, and the water around it runs so clear that its whole body shows below.
```
````

## Statblock

```statblock
layout: Basic 5e Layout
name: "River Otter"
size: Large
type: monstrosity
alignment: unaligned
ac: 15
hp: 76
hit_dice: "9d10 + 27"
speed: "20 ft., swim 40 ft."
stats: [18, 16, 16, 6, 14, 8]
skillsaves:
  - athletics: 6
  - perception: 4
  - stealth: 5
senses: "Darkvision 60 ft., Passive Perception 14"
languages: "—"
cr: 4
traits:
  - name: "Hold Breath"
    desc: "The otter can hold its breath for 30 minutes."
  - name: "Play and Hunt"
    desc: "The otter is in play mode until someone harms an adult, touches a pup, or stays in the family's water for 10 minutes. It then switches to hunt mode, and the whole family switches with it. In play mode it uses only Tug Toy and grabs that deal no damage."
  - name: "Watery Ambush"
    desc: "Hunt mode only. The otter has Advantage on attack rolls against a creature in the water if another otter is within 10 feet of that creature."
actions:
  - name: "Multiattack (Hunt Mode)"
    desc: "The otter makes one Bite attack and one Tail attack."
  - name: "Bite"
    desc: "Melee Attack Roll: +6, reach 5 ft. Hit: 14 (2d8 + 4) Piercing damage. If the target is Medium or smaller, it has the Grappled condition (escape DC 14)."
  - name: "Tail"
    desc: "Melee Attack Roll: +6, reach 10 ft. Hit: 11 (2d6 + 4) Bludgeoning damage."
  - name: "Dunk (Recharge 5–6)"
    desc: "One creature Grappled by the otter is pulled up to 20 feet and held underwater. It has the Restrained condition until the grapple ends."
bonus_actions:
  - name: "Tug Toy (Play Mode)"
    desc: "The otter targets one object within 5 feet that a creature holds or wears, or a trailing rope. The holder makes a Strength (Athletics) or Dexterity (Sleight of Hand) check contested by the otter's Strength (Athletics). If the otter wins, it takes the object and swims 10 feet away. This deals no damage."
```

## Tactics

- **Opening.** In play mode the family shares one initiative and tosses swimmers, oars, and packs between them without hurting anyone.
- **Signature.** The switch from play to hunt. Its tell is the whole family going still at once, heads up, with no more splashing.
- **Adapts.** In hunt mode the adults use Watery Ambush and Dunk to split one swimmer from the rest.
- **Weaknesses.** They will not fight on dry land or on a haul-out that traps them away from the current. They grow bored of prey that stops playing, and a clever trick sends them off to a new game.
- **Morale.** A family breaks off when two adults are Bloodied, and leaves bored when nobody plays for a minute.

## Behavior

- **Habits.** They play first. Rope, oars, ankles, trailing packs, and a [[Deer-Stalker]]'s antlered head all become tug toys.
- **Diet.** River animals and bank grazers, and careless predators and Deer-Stalkers as much for sport as for food. They will not haul a kill onto [[razer-grass]].
- **Group.** Families of four to six adults plus pups. Play is for blood kin only.
- **Memory.** The family remembers fire, ropes, and repeated tricks, and does not fall for the same one twice.
- **Signs.** Glass-clear water, polished mud slides on the bank, pale chest flashes under the surface, and ropes drawn tight from under a boat.
- **Aftermath.** Oars and gear bobbing where no current should hold them.

## Art

### Token

![[attachments/shattered-sea/creatures/aruhe-river-otter-token.png|River Otter token]]
