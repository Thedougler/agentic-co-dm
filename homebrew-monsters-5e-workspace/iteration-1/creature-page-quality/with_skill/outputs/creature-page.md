---
title: "Lava Asp"
category: entities
tags: [shattered-sea, creature, predator, volcanic, reptile]
sources:
  - "homebrew-monsters-5e skill execution"
created: 2026-09-19
updated: 2026-09-19
type: creature
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: volcanic-islands
role: ambusher/skirmisher
cr: 5
summary: "CR 5 paired volcanic ambusher. Heat shimmer approach and coordinated strikes exploit isolation. Venom creates delayed resource pressure."
---

# Lava Asp

> [!narration] Narration
> The ground beneath the volcanic island trembles with residual heat. Twin forms coil in the lava-tube shadows—sleek, obsidian-black bodies traced with rust-red scales along the spine. As they move, the air ripples around them like water, a heat shimmer so intense that distant outlines blur and refract. The nearest head swings toward an approaching sound, fangs pale against dark skin, eyes glowing amber in the darkness. A low, rhythmic hiss passes between the pair—not threat, but coordination. They move together toward prey already decided, heat-adapted predators descended from warmer ages, now perfected in the volcanic furnace.

## Statblock

```statblock
layout: Basic 5e Layout
name: Lava Asp
size: Small
type: monstrosity
alignment: unaligned
ac: "15"
hp: 82
hit_dice: "11d8 + 33"
speed: "40 ft., climb 30 ft."
stats: [14, 16, 16, 2, 12, 5]
saves:
  - constitution: 5
skillsaves:
  - Perception: 4
  - Stealth: 5
senses: "darkvision 60 ft., passive Perception 14"
languages: "—"
cr: 5
traits:
  - name: Heat Shimmer
    desc: "While the Asp is more than 30 feet away from a creature it can see, the air around it shimmers with retained heat. A creature that attacks the Asp with a ranged weapon attack while the Asp is outside 30 feet makes the attack roll with disadvantage."
  - name: Thermal Vision
    desc: "The Asp can see through magical darkness and nonmagical obscuration caused by volcanic ash, smoke, or steam as if that area were lightly obscured. Heat sources, including warm-blooded creatures, are visible to the Asp even through solid volcanic rock up to 60 feet away."
  - name: Pack Coordination
    desc: "If another lava Asp within 60 feet of this one targets the same creature that this Asp targets with an attack on the same turn, this Asp has advantage on its attack roll against that creature."
  - name: Cold Sensitivity
    desc: "If the Asp takes cold damage, it has disadvantage on attack rolls until the end of its next turn."
actions:
  - name: Multiattack
    desc: "The Asp makes two Fang Strike attacks."
  - name: Fang Strike
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage, and the target must make a DC 14 Constitution saving throw. On a failed save, the target is poisoned. The poison does not deal damage immediately; instead, at the start of the target's next turn, the poisoned creature takes 9 (2d8) poison damage, and the condition ends. A creature can be poisoned by multiple venom strikes; each tracks separately and deals damage on its next turn."
  - name: Venom Spray (Recharge 5–6)
    desc: "Ranged Weapon Attack: +6 to hit, range 15/30 ft., one target. Hit: 13 (2d8 + 3) poison damage, and the target makes a DC 14 Constitution saving throw. On a failed save, the target is poisoned as described in Fang Strike (poison damage at the start of the target's next turn)."
reactions:
  - name: Thermal Coil
    desc: "Trigger: The Asp is hit by an attack while it is at least 30 feet away from the attacker. Response: The Asp moves up to half its speed without provoking opportunity attacks. This movement is silent and difficult to track in the shimmering heat."
```

---

## Behavior

- **Habitat.** Lava Asps lair in volcanic islands' lava-tube networks, preferring heat-vents and deep chambers that maintain high temperatures. They avoid cold water, high altitude, and wind-swept open ground. An Asp pair claims a territory spanning several tube networks, marking it by leaving fang-scarred stone and pools of acidic venom.
- **Behavior.** An Asp spends daylight hours coiled in the deepest, warmest chambers, absorbing heat through its scales. At dusk, the pair emerges to hunt. They move in synchronized patterns, mirroring each other's shifts and stops. When prey approaches, both Asps hiss in a coordinated rhythm—a doubled rattle that echoes through the tubes and across volcanic stone.
- **Diet.** Lava Asps hunt burrowing mammals, lizards, and flushed game that seeks shelter in volcanic crevasses. They prefer warm prey and will pursue warm-blooded creatures across unfamiliar terrain if one is poisoned; a poisoned target becomes the focus of the hunt until the venom takes effect. They will scavenge fresh kills left by larger predators.
- **Social Structure.** Lava Asps mate for life and hunt as bonded pairs. A solitary Asp (widowed, exiled, or juvenile) is cautious and territorial but far less aggressive than a pair. Juvenile Asps are weaned into the volcanic network at 6 months and usually driven from the parent territory by year one. They range into cooler lava tubes and lower altitudes until claiming their own vents.

---

## Tactics

- **Signs.** A tracker finds synchronized fang-mark pairs on prey (both Asps struck the same target), trails that mirror and split in unison, heat-scorched stone where the pair rested, and pools of thin, acidic venom pooled in small hollows near their resting sites. The venom produces a sharp sulfur smell.
- **Instincts.** The pair keys on warmth, vibration, and exposed movement. They break off pursuit when prey enters sustained cold, thick water, or high-altitude wind channels where the shimmering heat fails. The pair will not engage a target if separated more than 60 feet (the range of their coordination sense); a widowed Asp becomes solitary, cautious, and will retreat if pressured by a group.
- **Tactics.** The pair approaches at range, using heat shimmer to blur themselves and reduce the effectiveness of missile attacks. As they close to 30 feet, the shimmer fades and the pair synchronizes—a hiss signals the coordinated strike. Both target the same prey, overwhelming defense through action economy. On the next turn, the pair prioritizes targets poisoned by their venom from the prior round, stacking poison to create resource pressure. If one Asp is killed or separated, the survivor's tactics change: it becomes defensive, uses Thermal Coil to reposition and maintain distance, and attempts to disengage and retreat to the lava tubes.
- **Weaknesses.** Cold damage (spells, potions, abilities) triggers Cold Sensitivity and reduces the Asp's threat. Area-of-effect spells bypass shimmer disadvantage and can catch both Asps if they coordinate. Separation—any feature or spell that moves one Asp 60+ feet away from the other—breaks Pack Coordination and reduces both Asps to independent hunters with standard attack rolls. Water and very cold terrain (glacial caves, flooded chambers) force retreat. The pair's coordination is auditory and chemical; silencing the hiss or obscuring scent (smoke, wind, illusion) can desynchronize their approach.
- **Aftermath.** A lair where Lava Asps died shows burn marks on stone from their bodies, shed obsidian-black and rust-red scales, venom residue that burns skin, and sometimes a carcass wrapped in coils but uneaten (Asps sometimes collect kills to age them for easier consumption).

---

## Art
<!-- Add visual references, tokens, or battlemaps when available. -->
<!-- Art embeds: wiki/attachments/{subject-slug}-{role}.ext — roles: banner|portrait|token|battlemap|overview|reference|handout|teaser -->
