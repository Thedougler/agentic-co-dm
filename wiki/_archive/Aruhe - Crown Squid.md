---
type: monster
campaign: shattered-sea
region: aruhe
role: controller
cr: 11
source: house (wiki creature.aruhe-crown-squid; CR 11 simplification)
visibility: dm
tags: [monster, aruhe]
---
# Great Crown Squid

![[great-crown-squid-of-aruhe-token.jpg|Great Crown Squid FoundryVTT token]]
> [!narration] Narration
> The Great Crown Squid hangs between the trees, its house-sized mantle broad as a roof and translucent enough to show a deep violet glow inside. Thick arms spread from beneath it to grip the trunks, their bark-dark skin ridged and studded with thorny suckers, while a curtain of fine tendrils hangs toward the forest floor. Mist beads on the rubbery body and falls from the trailing tendrils as the whole shape stays almost still above the canopy.

## Statblock
![[attachments/shattered-sea/creatures/great-crown-squid-of-aruhe-01.jpg|Great Crown Squid of Aruhe]]
```statblock
layout: Basic 5e Layout
name: "Great Crown Squid"
size: Gargantuan
type: monstrosity
alignment: unaligned
ac: "15 (rubbery hide)"
hp: 210
hit_dice: 20d20
speed: "20 ft., climb 50 ft."
stats: [24, 14, 20, 7, 16, 6]
saves:
  - dexterity: 6
  - constitution: 9
  - wisdom: 7
skillsaves:
  - Athletics: 11
  - Perception: 11
  - Stealth: 6
senses: "darkvision 60 ft., passive Perception 21"
languages: "—"
cr: 11
traits:
  - name: "Canopy Camouflage"
    desc: "The squid has advantage on Dexterity (Stealth) checks made among foliage, branches, or hanging roots."
  - name: "Blind Space"
    desc: "The squid can't see a creature within 10 feet directly beneath the center of its mantle, and it can't make opportunity attacks against a creature in that space."
  - name: "Buoyant Mantle"
    desc: "The squid takes no falling damage."
actions:
  - name: "Multiattack"
    desc: "The squid makes two attacks, using Crushing Arm and Beak, or two Crushing Arm attacks. It can replace one Crushing Arm attack with Hookline Tentacle if it isn't grappling a creature."
  - name: "Hookline Tentacle"
    desc: "Melee or Ranged Weapon Attack: +11 to hit, reach 15 ft. or range 60/120 ft., one target. Hit: 18 (3d6 + 8) slashing damage, and the target has the Grappled condition (escape DC 19). The squid can grapple only one creature at a time."
  - name: "Crushing Arm"
    desc: "Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 25 (3d10 + 8) bludgeoning damage, and the squid pushes the target up to 10 feet."
  - name: "Beak"
    desc: "Melee Weapon Attack: +11 to hit, reach 10 ft., one creature Grappled by the squid. Hit: 30 (4d10 + 8) piercing damage."
  - name: "Canopy Pounce (Recharge 5–6)"
    desc: "The squid moves up to its climb speed without provoking opportunity attacks, then makes one Crushing Arm or Hookline Tentacle attack."
```

## Behavior

- **Habitat.** The Great Crown Squid owns high, wet canopy in [[Aruhe - Quiet Forest|the Quiet]], [[Aruhe - The Marshes|the Marshes]], and the roof of [[Aruhe - The Mangroves|the Mangroves]]. It favors massive trunks, hanging roots, mist, and broken light where its clear mantle and bark-dark arms can read as part of the trees.
- **Behavior.** It waits above trails and waterways with its mantle braced between trunks and its finer hooklines hanging below. It watches before it commits, choosing isolated prey and shifting through the canopy with almost no weight on the branches. The one the crew saw after the spore plant disturbance stopped at the tree line instead of following into open ground.
- **Diet.** It eats large animals, travelers, and anything it can draw up into the canopy. [[Aruhe - Bear-Elk|Bear-Elk]], wounded hunters, climbing creatures, and people who trail behind a group are good meals. Juveniles sometimes work the upper terraces, while the oldest sit heavier in the Marshes where food is easy and walkers cannot easily reach the roof.
- **Social Structure.** Solitary apex predator. Each adult holds a stretch of canopy and treats other large Aruhe hunters as boundaries rather than allies. Adults do not share a kill unless one is already beaten and leaving.

## Tactics

- **Signs.** Sucker scars high on trunks, bark stripped upward, shredded sixty-foot vines, broken branches that never fell, prey tracks that end going up, polished antler caught in the canopy, wet hookline cuts, and long rootlike lines hanging where no root should move.
- **Instincts.** It wants isolated prey, trailing bodies, wounded creatures, and targets that step under open canopy. It avoids open grassland, occupied [[Aruhe - River Otter|river otter]] water, and prey that clusters tightly enough to cut hooklines or hide under its mouth.
- **Tactics.** It stays above the fight, sends one hookline down through leaves and mist, uses its other arm to shove nearby prey, and bites once a target is held. It uses Canopy Pounce to cross the roof without giving the party an opening, then returns to the canopy route rather than dropping to the ground.
- **Weaknesses.** Open grass, deep occupied water, clustered targets, and the blind space directly beneath the mantle all interfere with its hunt. Its single hookline can hold only one creature, so a group that stays together denies it an easy isolated meal.
- **Aftermath.** A Crown Squid encounter leaves torn canopy, sucker rings, sap-wet bark, broken vines, blood high overhead, and trails that simply stop beneath the trees. There is no treasure expected, though severed hooklines, rubbery hide, and mantle tissue may interest a careful harvester.
