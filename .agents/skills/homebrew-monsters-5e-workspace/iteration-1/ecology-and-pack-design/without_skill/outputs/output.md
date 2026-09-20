# CR 6 Pack Predator Design: Canopy Stalker

## Ecology and Design Process

### Niche Analysis
The Aruhe predator ecosystem has clear separation:
- **Spiguar (CR 11)**: Solitary ground ambusher, grassland specialist
- **Bloodhawk (CR 11)**: Solitary aerial dominant, hunts from open sky
- **Gap**: Mid-canopy layer lacks a cooperative hunter

### Canopy Stalker Concept
A feline pack predator that hunts the canopy layer cooperatively. Individual Stalkers are CR 6 creatures that gain tactical advantages when hunting in groups (packs of 3-6). They fill the ecological role between mid-sized tree-dwellers and the larger apex predators.

### Prey Strategy
- Primary: Arboreal prey including tree-dwelling mammals, gliding creatures, smaller birds
- Secondary: Juvenile forms of ground predators during canopy seasons
- Reference diet pattern: Combines Spiguar's mammal preference with Bloodhawk's opportunism
- Scale: Hunt prey Medium-sized or smaller (rabbits, small deer analogs, tree apes)

### Habitat and Behavior
- **Habitat**: Dense canopy, branch networks, vine-covered trees, forest transition zones
- **Behavior**: Stalk and pounce from branch cover; use coordinated flanking in packs
- **Social**: Pack-oriented (3-6 members); each pack controls a canopy territory
- **Movement**: Climbing and branch-running equal to ground speed

### Design Elements for Pack Mechanics
1. **Pack Bonus**: Creatures gain advantage on attack rolls when adjacent to 1+ allies
2. **Coordinated Pounce**: Multiple Stalkers can trigger pack tactics during the same turn
3. **Weakness**: Lose effectiveness in open ground or open sky (unlike Spiguar/Bloodhawk)

---

# Aruhe - Canopy Stalker

> [!narration] Narration
> Four tawny shapes coalesce from the leaf-shadow above, each sleek and low-slung as a weasel with a predator's burning eyes. The lead stalker's ears flatten. A chittering call passes through the pack. Branches barely whisper as they begin to circle, cutting off the run toward open ground.

## Statblock

```statblock
layout: Basic 5e Layout
name: Canopy Stalker
size: Medium
type: monstrosity
alignment: unaligned
ac: "14 (natural armor)"
hp: 45
hit_dice: 7d8 + 14
speed: "40 ft., climb 40 ft."
stats: [16, 16, 14, 4, 13, 10]
saves:
  - Dexterity: +5
  - Constitution: +3
skillsaves:
  - Acrobatics: +5
  - Athletics: +5
  - Perception: +3
  - Stealth: +7
senses: "darkvision 60 ft., passive Perception 13"
languages: "—"
cr: 6
traits:
  - name: "Branch Walker"
    desc: "The stalker ignores Difficult Terrain caused by branches, vines, and nonmagical plants. It climbs at its full speed and doesn't require Difficult Terrain when moving along branches or trunks."
  - name: "Pack Tactics"
    desc: "The stalker has advantage on Melee Attack rolls against a creature if at least one other stalker is within 5 feet of the target and the other stalker isn't Incapacitated."
  - name: "Canopy Acrobat"
    desc: "The stalker can move up, down, and across vertical surfaces and upside down along ceilings, leaving no trail. When it moves across a branch or vine, it can move up to 10 feet vertically without expending extra movement."
traits_2:
  - name: "Pounce (Canopy Form)"
    desc: "If the stalker moves at least 20 feet straight toward a creature on the same horizontal plane or branch and then hits it with a Rake attack on the same turn, the target takes an extra 5 (2d4) slashing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or have the Prone condition."
actions:
  - name: "Multiattack"
    desc: "The stalker makes two Rake attacks."
  - name: "Rake"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 3) slashing damage."
  - name: "Coordinated Strike (Recharge 5–6)"
    desc: "One creature within 5 feet must make a DC 13 Dexterity saving throw. The stalker has advantage on this attack if at least one other stalker is within 5 feet of the target. On a hit, the target takes 16 (3d6 + 3) slashing damage, and if the target is a creature, it must succeed on a DC 14 Strength saving throw or have the Grappled condition (escape DC 14). While Grappled by the stalker, the target has the Restrained condition."
bonus_actions:
  - name: "Canopy Dart"
    desc: "The stalker moves up to its speed. If it's within 10 feet of a branch, vine, or tree, it can move up to 10 feet vertically without expending movement and without provoking opportunity attacks."
  - name: "Pack Chirp"
    desc: "The stalker emits a chittering call audible within 60 feet. Other stalkers within range that can hear it gain advantage on their next attack roll before the end of this turn."
```

## Physical Description

A Canopy Stalker resembles a weasel-feline hybrid: sleek and muscular with tawny-brown fur marked with black rosettes. Four limbs are built for climbing, with retractable curved claws. A long tail provides balance and acts as a weapon. Its ears are rounded and alert. Eyes are large, amber, and forward-facing. Whiskers and sensory fur help it navigate the canopy in dim light.

Height: 3-4 feet at shoulder
Weight: 80-120 lb
Build: Low-slung, flexible spine, powerful hindquarters

---

## Behavior

- **Habitat.** Dense canopy regions of [[Aruhe]], especially vine-laden zones, broad-limbed forests, and tree networks that allow rapid transit without touching ground. Stalkers avoid grasslands, open water, and bare stone.
- **Behavior.** A pack stalks prey from branch to branch, using three-dimensional terrain to cut off escape routes. They hunt at dusk and dawn when prey is most active. Diurnal members rest in den-trees high in the canopy. A hunt uses coordinated calls and flanking positions.
- **Diet.** Arboreal mammals (tree rabbits, climbing rodents, small primates), gliding creatures, low-flying birds, and young of larger prey species (juvenile [[Deer-Stalker|Deer-Stalkers]], [[Wolfrabbit|Wolfrabbit]] kits). They prefer prey that weighs 20-60 lb.
- **Social Structure.** Packs of 4-6 adults led by a senior female. Juveniles remain in the pack for 1-2 years before establishing new territories. A single pack controls a canopy range spanning 2-4 square miles. Overlapping territories are defended with ritualized displays and brief combat. Solitary stalkers are outcasts or dispersing juveniles and are more aggressive.

---

## Tactics

- **Signs.** Scratch marks on high bark, midair blood drops on leaves below, fur caught on branches, a high-pitched chittering echo through the canopy, prey killed with parallel rake patterns, bone-dragging trails on branch highways.
- **Instincts.** Hunt at dawn and dusk. Key on movement in the canopy and climbing prey. Break off pursuit if prey reaches open ground or moves below the canopy layer. Avoid diving into tall grass or following into water.
- **Tactics.** The pack separates prey from escape routes using coordinated movement. One stalker drives while others cut flanking positions on surrounding branches. A coordinated strike pins the prey while others rake. Once a target is grappled, the pack works to haul it into the canopy where it cannot call for help. Packs break apart to surround fleeing prey, forcing it into an ambush.
- **Weaknesses.** Open ground and open sky are hostile territory. Canopy Stalkers have poor performance in wide-open areas or above tree-height. Long falls injure them despite their agility; they avoid branches that don't offer safety. Ground predators like Spiguars and heavy creatures that shake the canopy are avoided. Fire in the canopy causes panic. Water and otter territories are avoided.
- **Aftermath.** A kill site shows scratch marks on the attack tree, blood on leaves and branches, parallel rake patterns on bone, and missing sections where the pack dragged the prey into cover. Feeding occurs in den-trees, leaving bones and refuse at significant heights. A disrupted hunt leaves panicked prey animals scattered across the canopy, their trails visible in broken branches and disturbed nests.

---

## Encounter Notes

- **Solo vs Pack:** A single Stalker encountered alone fights defensively and attempts to flee to gather reinforcements. A pack of 4-6 is confident and aggressive.
- **Advantage Terrain:** The canopy is their domain. They gain Pack Tactics bonuses, can use Canopy Dart freely, and can climb at full speed. Open ground and sky strip these advantages.
- **Integration:** Stalkers avoid larger predators (Spiguar, Bloodhawk) but may scavenge kills. They compete with large birds for some prey. Juvenile [[Terror-Bird|Terror-Birds]] are occasional prey.

---

## Monster Type Notes

**Classification:** Monstrosity (pack predator)
**Inspiration:** Feline pack hunters (wild dogs, hyenas, lichen lynx analog) adapted for three-dimensional arboreal hunting
**Comparison:** Lower threat than Spiguar or Bloodhawk individually, but pack tactics make them significantly more dangerous in groups.

---

## CR 6 Justification

A single Canopy Stalker presents CR 6 threat because:
- **Base Damage:** 11 (2d6+3) per Rake attack, or 16 (3d6+3) for Coordinated Strike
- **HP:** 45 (mid-range for CR 6)
- **AC:** 14 (moderate armor)
- **Special Abilities:** Pack Tactics (advantage when allied), Pounce, Grapple potential
- **Mobility:** 40 ft. ground + 40 ft. climb + Canopy Dart bonus action makes it hard to pin down
- **Solo Action Economy:** Two attacks per turn, one bonus action, recharging coordinated ability

When four Stalkers hunt together, the party faces multiple applications of Pack Tactics, coordinated grapples, and tag-team tactics that make the threat level equivalent to CR 7-8 for a party of 4.

---

## Campaign Notes

Canopy Stalkers should serve as:
- A mid-tier threat that tests the party's ability to fight in three-dimensional terrain
- An alternative to groundbound or sky-bound encounters
- Ecology connectors between large arboreal prey and the apex predators
- A source of fear for arboreal travelers (bridges, rope paths, tree routes)

They are distinctly different from both Spiguar (ground/ambush) and Bloodhawk (aerial/stoop), allowing varied predator encounters across Aruhe's ecosystems.
