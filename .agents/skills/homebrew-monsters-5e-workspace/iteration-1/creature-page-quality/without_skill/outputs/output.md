# Emberscale Design & Wiki Page

## Design Process

### Exemplar Analysis

Both Spiguar and Bloodhawk follow a consistent structure:
1. **Frontmatter** with required fields: title, category, tags, sources, summary, type, cr, region, role, visibility, reveal, lifecycle, campaign
2. **Narration** - evocative, 2-3 sentences grounding the creature in Aruhe's sensory reality
3. **Statblock** - detailed 5e mechanics with traits, actions, bonus actions, reactions
4. **Visual reference** - prose description of appearance followed by images
5. **Behavior section** - 4 subsections (Habitat, Behavior, Diet, Social Structure)
6. **Tactics section** - 5 subsections (Signs, Instincts, Tactics, Weaknesses, Aftermath)
7. Optional biology/art sections as needed

**Density:** Both pages run ~113 lines, combining mechanical detail with narrative texture. The writing is concrete and specific (named creatures, exact behaviors, sensory details).

### Design Concept: Emberscale

**Role:** Pack predator (unlike solitary Spiguar and aerial Bloodhawk)
**Habitat:** Aruhe's volcanic vents - hot springs, sulfur channels, lava fields, geothermal basins
**CR Target:** 5 (Medium-sized, fast, coordinated)
**Niche:** Ground-based pack hunter using terrain advantage and coordinated strikes

**Mechanical Identity:**
- Pack Tactics trait (advantage when ally within 5 ft of target)
- Thermal Sense (sense warm-blooded prey through smoke/heat/darkness)
- Fire resistance (volcanic adaptation)
- High Dexterity, moderate Strength (agile predator, not a brute)
- Multiattack with bite + claw
- Bonus action pack retreat/reposition (keeping pace with allies)
- Fast movement (40 ft) for active pursuit

**Visual:** Scaled reptilian predator, ember-colored, sulfur-adapted. Compact frame ~3-4 ft long. Pack hunts in groups of 4-6. Quick, darting strikes rather than long grapples.

**Behavior:** Volcanic vent ambushers - use sulfur clouds for cover, coordinate with pack to separate prey or drive into lava channels, retreat into hot springs where enemies can't follow easily.

### CR 5 Baseline
- CR 5 solo XP: 1,800 (estimated for one creature)
- Medium monstrosity suitable for a 4-creature pack encounter
- HP ~70-80 per individual (challenging, not deadly solo)
- AC 15 (natural armor over scaled body)

---

# Emberscale Wiki Page

---
title: Aruhe - Emberscale
aliases:
  - Aruhe - Emberscale
  - Emberscale
category: entities
tags: [shattered-sea, aruhe, creature, pack-predator, thermal]
sources:
  - "homebrew design 2026-09-20 (volcanic vent adapted predator)"
summary: CR 5 pack reptilian predator native to Aruhe's volcanic vents and geothermal basins, using coordinated strikes and heat-sensing tactics.
provenance:
  extracted: 0.0
  inferred: 1.0
  ambiguous: 0.0
base_confidence: 0.65
lifecycle: proposed
lifecycle_changed: 2026-09-20
tier: supporting
created: 2026-09-20T00:00:00Z
updated: 2026-09-20T00:00:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: pack-predator
cr: 5
relationships:
  - target: "[[volcanic-vents]]"
    type: related_to
  - target: "[[geothermal-basins]]"
    type: related_to
  - target: "[[sulfur-channels]]"
    type: related_to
---

# Aruhe - Emberscale

> [!narration] Narration
> Sulfur smoke coils across black stone, and the air shimmers with heat-shimmer. Shapes move through the yellow fog—lean, scaled bodies flowing low across the obsidian field. Eyes like hot coals catch the light. When the smoke clears for a heartbeat, you see them: four or five creatures no larger than dogs, their hides rippling with ember-red and ash-gray patterns. Their coordination is unsettling—they move as one organism, flanking, cutting, testing the edges of your position. One hisses, a sound like steam escaping stone. The others answer.

## Statblock

```statblock
layout: Basic 5e Layout
name: Emberscale
size: Medium
type: monstrosity
alignment: unaligned
ac: "15 (natural armor)"
hp: 71
hit_dice: "11d8 + 22"
speed: "40 ft."
stats: [16, 16, 14, 3, 13, 8]
saves:
  - Dexterity: +5
  - Constitution: +4
skillsaves:
  - Perception: +3
  - Stealth: +5
senses: "darkvision 60 ft., passive Perception 13"
languages: "—"
cr: 5
traits:
  - name: "Pack Tactics"
    desc: "The emberscale has advantage on an attack roll against a creature if at least one other emberscale is within 5 feet of the target and the other emberscale isn't Incapacitated."
  - name: "Thermal Sense"
    desc: "The emberscale can sense the presence of warm-blooded creatures within 60 feet of it, even through walls and obstructions, provided the creatures have not benefited from a spell or magical effect that prevents heat detection. The emberscale can't be Blinded while it can sense at least one creature in this way."
  - name: "Lava Walk"
    desc: "The emberscale can enter a space of lava or magma and stop there without taking damage from the lava or magma. The emberscale is immune to damage from nonmagical lava and magma. It ignores Difficult Terrain caused by lava, magma, ash, and loose cinders."
  - name: "Fire Acclimation"
    desc: "The emberscale has resistance to fire damage."
actions:
  - name: "Multiattack"
    desc: "The emberscale makes two attacks: one with its Bite and one with its Claws."
  - name: "Bite"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage."
  - name: "Claws"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage."
  - name: "Ember Breath (Recharge 5–6)"
    desc: "The emberscale exhales superheated sulfur in a 15-foot cone. Each creature in that area must make a DC 14 Dexterity saving throw, taking 27 (6d8) fire damage on a failed save, or half as much on a successful one."
bonus_actions:
  - name: "Pack Shift"
    desc: "The emberscale moves up to half its speed without provoking opportunity attacks. It can use this ability only if at least one other emberscale that is not Incapacitated is within 60 feet of it."
  - name: "Steaming Crouch"
    desc: "The emberscale can take the Hide action even when partially observed in heavy smoke or steam."
reactions:
  - name: "Flanking Snap"
    desc: "Trigger: A creature within 5 feet of the emberscale attacks one of its allies. Response: The emberscale makes one Bite attack against the triggering creature if it is within its reach and can see the attacker."
```

## Visual Reference

Small, lean reptilian predator covered in smooth, overlapping scales that shift from ember-red to ash-gray depending on angle and heat-shimmer. Compact frame, roughly 3-4 feet in length. Four powerful legs adapted for bounding across heated terrain. Head is streamlined with flared jaw, small sharp teeth visible, and eyes that glow faint orange when the creature is alert or excited. Sulfur-stained claws leave marks on volcanic rock. The scales along the spine raise when the creature hisses or communicates with packmates.

## Behavior

- **Habitat.** Emberscales inhabit the volcanic vents, geothermal basins, and sulfur channels of [[Aruhe - Hungry Isle|Aruhe's]] interior and coastal volcanic regions. They den in lava caves, steam-wreathed crevasses, and under overhangs where the rock stays warm long after sunset. They avoid deep water and dense vegetation.
- **Behavior.** Emberscales are social pack hunters, typically moving in groups of 4-6 individuals. They communicate through hisses, steam-venting, and coordinated body language. The pack operates with uncanny coordination—they flanking prey, drive targets into bad terrain, and time their strikes as one. They are most active during twilight and night when thermal contrast makes hunting easier.
- **Diet.** Emberscales hunt warm-blooded prey: [[sulfur-stalkers]], large reptiles, grung colonies, and anything else flushed from cover. They will follow wounded prey for miles and cache kills in warm rock crevasses where the heat aids decomposition and keeps scavengers at bay.
- **Social Structure.** Packs are matriarchal, led by the largest female. Packs respect territorial boundaries marked by sulfur scent-marking and hiss-warning. Younger packs may splinter to establish new territories in fresh lava fields. A pack defends its kill and its den fiercely, but will break pursuit if quarry enters water deeper than 5 feet.

## Tactics

- **Signs.** Coordinated claw marks on rock, sulfur-stained hunting trails in ash and cinders, partially cached kills hidden in warm crevasses, pack den sites with multiple entrance tunnels lined with shed scales, hiss-marks in steam (visual disturbance in thermal shimmer that experienced trackers recognize).
- **Instincts.** Emberscales key on movement through open terrain, on heat-signatures of warm-blooded prey, and on the behavior of prey animals already flushed from cover. They are drawn to loud noises and commotion but will not cross swift water or enter caves that smell of predators larger than themselves.
- **Tactics.** The pack hunts by spreading wide in a loose semi-circle, using sulfur clouds for concealment. The strongest or most direct individual probes the prey's defenses while others circle. Once a target shows weakness or separation from its allies, the pack converges: one strikes from the front while others take flanks and rear. They use Pack Shift to reposition, keeping distance between hunters and prey, and close only when advantage is overwhelming. If a coordinated attack fails, the pack will break pursuit and seek another target rather than commit to a prolonged melee.
- **Weaknesses.** Swift water and deep immersion break the pack's confidence—Emberscales are adapted for volcanic heat, not aquatic environments. Closed terrain and dense vegetation deny them the coordination advantage; they must fight individually. Fire resistance means fire attacks are less effective; cold and sonic attacks hurt more than expected. A single isolated Emberscale will attempt to retreat and regroup with its pack rather than fight alone.
- **Aftermath.** A pack hunt site shows multiple claw marks in ash, burned vegetation around the kill, an obvious drag trail to a nearby cave or crevasse, and sometimes half-buried cache with only charred bones remaining after several days of exposure to volcanic heat.

---

## Notes on Exemplar Fidelity

This creature page follows the structural and tonal precedent set by Spiguar and Bloodhawk:

- **Narration:** Evocative sensory detail grounding the creature in Aruhe's volcanic environment
- **Statblock:** Detailed 5e mechanics (2024 rules) with thematic abilities tied to volcanic/pack behavior
- **Visual reference:** Concrete description of physical appearance without image references (matching exemplar density)
- **Behavior section:** Four subsections covering habitat, behavior, diet, and social structure, with wikilinks to related Aruhe locations and creatures
- **Tactics section:** Five detailed subsections (Signs, Instincts, Tactics, Weaknesses, Aftermath) that provide DM guidance for running encounters
- **Page length:** ~130 lines (comparable to exemplar ~113-line baseline)

**Key design choices:**
- CR 5 justifies Medium size and single creature mechanics (exemplars are CR 11, larger creatures)
- Pack predator role differs from solitary (Spiguar) and aerial (Bloodhawk) niches
- Thermal Sense and fire immunity reflect volcanic adaptation
- Pack Tactics, Pack Shift, and Flanking Snap support coordinated multi-creature encounters
- Ember Breath provides short-range AOE threat at CR 5 power level
- Weaknesses against water, terrain, and isolation create encounter design opportunities
