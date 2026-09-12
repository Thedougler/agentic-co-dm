---
type: session
subtype: scene
status: pending
publish: false
aliases: ["Session 01 Scene 8", "The Saltwright Boarding", "Beat 8"]
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
session_number: 01
scene_number: 8
parent_run_guide: ""
summary: "The three-phase boarding fight as Rook's crew finds the party in the hold, escalating from the cargo hold through the open deck to the gangplank standoff with Rook himself."
uid: 1b30f950-1d03-4e88-9ebd-922a298ccf7a
---

# Session 01. The Saltwright Boarding

- [x] Ran

DM beat-script for the three-phase boarding fight that opens the moment the party commits at the end of Scene 07 (The Hold), initiative starting on the first hostile action. The played outcome (ambush in the hold, Cap'n Gorgeous and the deckhands killed, Geoffrey Draves' surrender and recruitment, Rook blasted off the gangplank, the canister reveal) is already landed on [[barnaby-rook|Barnaby Rook]], [[capn-gorgeous|Cap'n Gorgeous]], and [[geoffrey-draves|Geoffrey Draves]]. This page preserves the staged phase budget, terrain, and PC-spotlight design that produced it, not restated there. Phase 3's resolution script continues in [[scene-01-rook-final|Scene 1. Rook Final]].

---

## Opening

[[barnaby-rook|Barnaby Rook]] has left the [[uncertainty|HCS Surety]] and boarded the [[saltwright|Saltwright]], shaking down [[beaumont-sel|Beaumont Sel]] under the pretense of an inspection. The party is below deck. When they're found, the best Rook offers is forty gold Beaumont doesn't have.

## Challenge Calibration

XP Thresholds for 5 PCs, Level 3

| Tier | Threshold |
|---|---|
| Easy | 375 XP |
| Medium | 750 XP |
| Hard | 1,125 XP |
| Deadly | 2,000 XP |

Phase Budget Summary

| Phase | Enemies | Adjusted XP | Rating |
|---|---|---|---|
| 1. The Hold | 2x Deckhand, 1x Enforcer (crossbow) | 225 | Easy |
| 2. Above Deck | 2x Enforcer, 2x Deckhand | 375 | Medium* |
| 3. The Gangplank | Rook (CR 3), 1x Enforcer, 1x Alchemist | 1,500 | Hard** |

\* Pack Tactics on both Enforcers focusing one PC poses real danger. Treat as Medium. \*\* The gangplank bottleneck cuts effective party DPR ~40%, pushing into Hard-to-Deadly in practice.

## Lowering the Stakes

Between-phase breathing room exists. Not a short rest, but enough for a healing potion or tactical reset. Spell slots and ki points don't come back.

## Running It

### Phase 1. The Hold

*Party has every advantage. The Enforcer makes it a real fight.*

Three of Rook's crew descend: two deckhands up front, an Enforcer behind them with a heavy crossbow. Standard inspection. They expect shrimp and provisions, not five armed strangers.

Beaumont's emergency stash: 3x potions of healing (2d4+2 each) behind a false panel in the hold's aft wall, visible to any PC who looks aft.

| Field | Content |
|---|---|
| **Combatants** | 2x Dravosi Deckhands, 1x [[dravosi-enforcer\|Dravosi Enforcer]] (heavy crossbow, effectively melee in here) |
| **Terrain** | Cramped cargo hold. Engagement range up to ~20 ft. Most lanes 5 ft wide. |
| **Lighting** | Dark. The Enforcer has no darkvision, fighting blind unless he reaches a lantern cone. |
| **Loot** | Beaumont's potion stash: 3x [[potion-of-healing\|Potion of Healing]] behind a false panel aft wall. |
| **Surprise** | Party has it. |
| **Pressure** | If any crewman gets off an audible shout, Phase 2 loses surprise. |
| **Win condition** | All three crewmen silenced before they can signal above. |

PC Spotlights. Phase 1

- **Jean-Claude:** umbral sight active. [[invisible|Invisible]] to darkvision creatures, advantage on attacks. Priority target: the Enforcer before he closes to melee.
- **Crissdalynn:** no darkvision. Best position near the hatch to intercept anyone breaking for the ladder.
- **Delmar:** cramped lanes isolate targets. Rakish Audacity fires freely. Burn SA on the Enforcer first, not low-HP deckhands.
- **[[perrin-black-jaw|Perrin]]:** [[vicious-mockery|Vicious Mockery]] costs no attack roll and doesn't need line of sight beyond 60 ft. Good opener to shave the Enforcer's first attack.

| Direction | Lever | Effect |
|---|---|---|
| Easier | Remove the Enforcer, only two deckhands descend | Drops to ~75 XP (Trivial) |
| Easier | Alert Call requires crewman's action, not a reaction | Gives party a full round |
| Harder | Enforcer has a lit hooded lantern on his belt | Collapses Jean-Claude's Umbral Sight in the same zone |
| Harder | One deckhand was already below, watching quietly | No full surprise; he shouts immediately on Round 1 |

### Phase 2. Above Deck

*Pirates have position. Party has momentum.*

The party emerges through the hatch. If Phase 1 was clean, topside crew is watching, not expecting resistance.

| Field | Content |
|---|---|
| **Combatants** | 2x Dravosi Enforcers at the hatch, 2x Dravosi Deckhands at the rail |
| **Terrain** | Open deck, night. [[beaumont-sel\|Beaumont]] is at the wheel. |
| **Lighting** | Dim (full night, only the Saltwright's lanterns). |
| **Pressure** | Deckhands at the rail can signal the gangplank to pull before Phase 3 is possible. |
| **Win condition** | Deck crew defeated or driven back before they pull the gangplank. |

PC Spotlights. Phase 2

- **Crissdalynn:** send airborne toward the rail deckhands immediately. She can intercept before they reach the gangplank.
- **Jean-Claude:** umbral sight still operational in patches near the hull and rigging. Position matters.
- **Delmar:** enforcers at the hatch cluster together. Needs one ally adjacent or isolated target for Sneak Attack.
- **Perrin:** clear sight lines to rail deckhands = [[eldritch-blast|Eldritch Blast]] lanes. Priority: whoever is closer to the gangplank.

| Direction | Lever | Effect |
|---|---|---|
| Easier | Split the Enforcers (one at hatch, one at rail) | Breaks Pack Tactics; reduces to single +4 attacks |
| Easier | Deckhands break for the gangplank on their first turn | Converts to chase goal rather than combatants |
| Harder | Both Enforcers focus the first PC out of the hatch with Pack Tactics | ~75% hit chance; avg 18 damage in one round, enough to drop Perrin or Crissdalynn |
| Harder | Alchemist throws an Incendiary Flask through the open hatch as party emerges | Dex save per mechanic below, 2d6 fire + burning; raises Phase 2 XP to ~575 |

> [!mechanic]
> **Incendiary Flask lever. Alchemist's opening throw.** If used: DC 13 [[dexterity|Dexterity]] save as the flask lands through the open hatch. Fail: 2d6 fire damage and burning. This Harder-difficulty lever raises Phase 2 to ~575 XP.

### Phase 3. The Gangplank

Phase 3 plays in full in [[scene-01-rook-final|Scene 1. Rook Final]]. Session 01 ended mid-Phase 3, unresolved.

## Stakes

Phase 1-2 resolve the boarding crew; Phase 3 (Rook, his Enforcer, and the Alchemist) carries into the next session's central combat. The played outcome for all three phases appears on [[barnaby-rook|Barnaby Rook]], [[capn-gorgeous|Cap'n Gorgeous]], and [[geoffrey-draves|Geoffrey Draves]], not here.

## If Ignored

This is the session's forced boarding fight, not a hook the party can decline.

## Connections

- [[barnaby-rook|Barnaby Rook]]
- [[beaumont-sel|Beaumont Sel]]
- [[capn-gorgeous|Cap'n Gorgeous]]
- [[geoffrey-draves|Geoffrey Draves]]
- [[simone-tabarnack|Simone Tabarnack]]
- [[dravosi-crown|Dravosi Crown]]
- [[uncertainty|HCS Surety]]
- [[scene-01-rook-final|Scene 1. Rook Final]]
- [[scene-07-the-hold|Scene 7. The Hold]]
- [[saltwright|Saltwright]]
- [[flask|Flask]] of Endless Water
