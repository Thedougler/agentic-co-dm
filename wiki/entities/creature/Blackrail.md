---
title: "Blackrail"
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Blackrail.md"
summary: "CR 9 huge cave centipede that telegraphs with tremors before rushing main tubes and pinning prey with venomous segments."
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T19:54:00Z
updated: 2026-09-13T19:54:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: bruiser
cr: "9"
relationships:
  - target: "[[lava-tubes]]"
    type: related_to
  - target: "[[cave-bats]]"
    type: related_to
---
# Blackrail

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> A thirty- to forty-five-foot cave centipede fills the tube. Its back reads as parallel strips of wet black iron. Antennae longer than a man taste the air while the body keeps contact with the stone. Dust jumps in rings before the leg-rattle comes around the bend, and the head arrives sideways along the wall.
```

```col-md
```statblock
layout: Basic 5e Layout
name: Blackrail
size: Huge
type: monstrosity
alignment: unaligned
ac: "16 (natural armor)"
hp: 178
hit_dice: 17d12 + 68
speed: 60 ft., climb 60 ft.
stats: [22, 14, 18, 1, 14, 4]
saves:
  - dexterity: 6
  - constitution: 8
  - wisdom: 6
skillsaves:
  - Perception: 6
senses: "tremorsense 120 ft. (while both it and a creature touch cave stone), passive Perception 16"
languages: "—"
cr: 9
traits:
  - name: Spider Climb
    desc: "The blackrail climbs difficult surfaces, including ceilings, without an ability check."
  - name: Blind Beyond Light
    desc: "The blackrail's eyesight is poor. Flight, silence, water, or breaking contact with the rock interferes with its hunting."
  - name: Tunnel Body
    desc: "The blackrail cannot enter spaces narrower than 5 feet. At the end of a Tunnel Rush, if it moved 30 or more feet straight, it can't turn more than 90 degrees until the start of its next turn."
actions:
  - name: Multiattack
    desc: "The blackrail makes two Mandible attacks, or one Mandible attack and one Pin."
  - name: Mandible
    desc: "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 10 (3d6) poison damage."
  - name: Tunnel Rush (Recharge 5–6)
    desc: "The blackrail moves up to its speed in a straight line through a passage. Each creature in that path must make a DC 16 Dexterity saving throw. On a failed save, a creature takes 27 (5d10) bludgeoning damage, has the Prone condition, and is either pushed with the blackrail to the end of the move or pinned under a segment (Restrained, escape DC 16). On a successful save, a creature takes half damage and can dive into an alcove or side passage if one is within 5 feet."
  - name: Pin
    desc: "One Medium or smaller creature within 5 feet must succeed on a DC 16 Strength saving throw or have the Restrained condition from body segments (escape DC 16). While Restrained this way, the target takes 14 (4d6) poison damage at the start of each of its turns. The blackrail can restrain up to three creatures and can move at half speed while carrying pinned prey."
```
```
````

## Behavior

- **Habitat.** Main cave tubes and the Great Bore under [[Aruhe]], especially [[lava-tubes]]. It cannot enter spaces narrower than 5 feet.
- **Behavior.** It listens first: vibration, dust rings, then the leg-rattle. One adult controls miles of main tube. Juveniles mean the adult is elsewhere. Adults eat unrelated young.
- **Diet.** [[cave-bats]] and fallen surface animals. Venom is meant for deer-sized prey.
- **Social Structure.** Solitary adult ownership of tube roads. Juveniles separate from the adult's beat.

## Tactics

- **Signs.** Rhythmic tremors about thirty seconds out, dust jumping in rings, leg-rattle around the bend.
- **Instincts.** Hunt by stone contact and tremorsense. Haul quiet prey somewhere still.
- **Tactics.** Telegraph, then use Tunnel Rush down the tube. Pin with body segments and venom. Haul prey away.
- **Weaknesses.** Side crawlways and alcoves. Break contact with stone, use silence or water, and Ready actions before it rounds the bend. Spaces under 5 feet also work.
- **Aftermath.** Quiet tube, dragged trail, and pinned carcasses carried off the main road.
