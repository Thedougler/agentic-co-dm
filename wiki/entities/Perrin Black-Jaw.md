---
title: Perrin Black-Jaw
category: entities
tags: [shattered-sea, npc]
sources:
  - "campaign-os:perrin-black-jaw-voice-script.md"
  - "campaign-os:perrin-black-jaw-stats.md"
  - "campaign-os:perrin-black-jaw-spells.md"
  - "campaign-os:perrin-black-jaw.md"
  - "campaign-os:perrin-black-jaw-inventory.md"
  - "campaign-os:perrin-black-jaw-gallery.md"
  - "campaign-os:perrin-black-jaw-combat-profile.md"
  - "campaign-os:perrin-black-jaw-sheet.md"
  - "campaign-os:perrin-black-jaw-abilities.md"
  - "Nona Black-Jaw"
summary: Nona's grandson and surveyor; he owes an Aruhe survey and carries a sending stone.
lifecycle: canon
created: 2026-09-12T06:23:47Z
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
status: alive
role: contact
location: Calveno
faction: Passage
visibility: dm
---
# Perrin Black-Jaw

[[Nona Black-Jaw]]'s grandson. She asked him for a favor instead of cash, gave him the sending stone, and still waits on his Aruhe survey while his chase toward [[Vestra]] remains partly unshared.

## Abilities

# Perrin Black-Jaw — Abilities

Built from the player's character sheet. One section per action-economy
slot so a table runner can transclude exactly the one they need mid-round
(`![[Perrin Black Jaw Abilities]]`) — an ability that costs an
Action goes under Actions and is named, not repeated, anywhere else.

Everything [[Perrin Black-Jaw]] can do, sorted by what it costs to do it.
Spells are listed on [[Perrin Black Jaw Spells]]; only the class feature that
grants the casting appears here.

## Traits

Species and background traits — always-on, no activation cost.

| Trait | Source | Effect |
|---|---|---|
| Keen Senses | [[Rattkin]] | Advantage on Perception checks relying on hearing/smell |
| Scurry | Rattkin | Move through Large-or-smaller creatures' spaces without Opportunity Attacks when Disengaging |
| Survivor | Rattkin | Advantage vs. poisoned/disease; resistance to poison damage |
| Swimmer | Rattkin | Swim speed equals walking speed |
| Boneless | Rattkin | Squeeze through tight spaces, advantage escaping Grapple/[[Restrained]] |
| The Small | Mortis | Disadvantage on [[Strength]] checks/saves; +2 [[Charisma]] |

## Features

Class and subclass features that are not themselves an Action, Bonus
Action, or Reaction — passives, resource grants, and rest recoveries.

| Feature | Source | Effect | Uses | Recovery |
|---|---|---|---|---|
| Expertise | [[Bard]] | Double bonus to skills (Acrobatics, Persuasion) | | |
| Versatility (Bard) | Bard | Half bonus to ability checks where untrained | | |
| College of Lore, Bonus Proficiencies | Bard (College of Lore) | 3 bonus skill proficiencies | | |
| Pact of the Blade: bond | [[Warlock]] (Pact of the Blade) | CHA replaces STR/DEX for attack/damage on the bonded [[Longsword]]; can deal Necrotic/Psychic/Radiant instead of normal type | | |
| Magical Cunning | Warlock 2 | 1-minute rite, regain up to 1 expended Pact Magic slot | 1 / Long Rest | Long Rest |

Bard and Warlock spellcasting features (Bardic Inspiration's casting-adjacent grant, Pact Magic itself) appear here only for their action-economy cost below. The spells they cast live on [[Perrin Black Jaw Spells]].

## Actions

Attacks belong here, one row per distinct option, with the full stat line.

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
|---|---|---|---|---|
| Longsword (Pact-bonded) | +8 | 1d8+5 slashing | | Martial, Versatile, Sap; CHA via Pact of the Blade |
| Green-Flame Blade (cantrip) | +8 | 1d8+5 slashing | | Same melee strike as the Longsword; sheet notes an extra fire damage rider whose exact target/trigger isn't legible on the export (`[verify]`), see [[Green Flame Blade]] |
| [[Eldritch Blast]] (cantrip) | +8 | 1d10 force | | 2 beams at Warlock 2; Agonizing Blast not confirmed on this export |
| Unarmed Strike | +1 | 0 bludgeoning | | STR -2 floors this at 0 |
| Conjure Pact Weapon | | Bonus Action to conjure, or bond to one touched | | Eldritch Invocations, Pact of the Blade |
| Eldritch Invocations, Pact of the Blade | see above | | | |

## Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
|---|---|---|---|---|
| Bardic Inspiration | Bonus Action | Confer a 1d6 die to a creature within 60 ft | 5 / Long Rest | Long Rest |

## Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
|---|---|---|---|---|
| Cutting Words | An enemy roll (attack/check/damage) within 60 ft | Use a Bardic Inspiration die to subtract it from the roll | shares Bardic Inspiration pool | Long Rest |
| Pack Tactics | An enemy hits an ally within 5 ft | One weapon attack against the creature that hit them | 3 / Short or Long Rest | Short or Long Rest |

## Feats

No feats taken.

## Character sheet notes

Source: `_assets/character-sheets/perrin-black-jaw-character-sheet.pdf` (D&D Beyond export, level 5, replaces the prior level-4 export). Every number below is `[sheet]`, extracted directly from the PDF's fillable form fields (not vision-read text), superseding the earlier DM-directed "safe assumption" compile ([[Bard]] 4/[[Warlock]] 1) that stood in for this real sheet.

`[verify]` Sheet header lists player as "nickdavenock"; `vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md` frontmatter states `player: Kaden`. Transcribed as printed, contradiction not resolved here (not this skill's territory).

`[verify]` Proficiencies box lists known languages as "Common, Dwarvish, Gnomish"; the [[Rattkin]] species trait text on the same sheet describes "Common, Skitter-cant, and one language you choose", which don't match. Transcribed as printed, not reconciled here.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | [[Perrin Black Jaw Stats]] | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | [[Perrin Black Jaw Abilities]] | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | [[Perrin Black Jaw Spells]] | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | [[Perrin Black Jaw Inventory]] | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md` frontmatter | `_templates/pc.md` |

This file carries only what those pages cannot: the source citation, the
`[verify]` flags, and the machine-parseable Combatant Block. Restating a
table that already exists on one of the pages above is a duplication defect;
link to it instead.

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Perrin Black-Jaw
size: Small
type: humanoid
alignment: chaotic good
ac: 18
hp: 49
hit_dice: "2d8 + 3d8"
speed: "30 ft., swim 30 ft."
stats: [6, 18, 15, 11, 11, 20]
saves: { str: -1, dex: 5, con: 3, int: 1, wis: 4, cha: 9 }
damage_resistances: "poison"
actions:
  - name: "Longsword (Pact-bonded)"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage."
    sim: { id: longsword }
  - name: "Green-Flame Blade"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage plus 4 (1d8) fire damage."
    sim: { id: green_flame_blade } # level-5 primary fire rider [sheet+srd vault/srd/spells/evocation/green-flame-blade.md]; splash to a 2nd creature unmodeled
  - name: "Cure Wounds"
    desc: "Perrin touches a creature, restoring 9 (1d8 + 5) hit points."
    sim: { id: cure_wounds, heal: { dice: 1d8+5 }, cost: { resource: bard_slot_1, spend: 1 } }
bonus_actions:
  - name: "Healing Word"
    desc: "Perrin speaks a word of power, restoring 7 (1d4 + 5) hit points to a creature within 60 feet."
    sim: { id: healing_word, heal: { dice: 1d4+5 }, cost: { resource: bard_slot_1, spend: 1 } }
reactions:
  - name: "Cutting Words"
    desc: "When a creature Perrin can see within 60 feet makes an attack roll, ability
      check, or damage roll, he expends a Bardic Inspiration die to subtract it from the roll."
    sim: { id: cutting_words, kind: damage_reduction, die: 1d6, trigger: self_or_ally_hit,
           cost: { resource: bardic_inspiration, spend: 1 } }
  - name: "Pack Tactics Strike"
    desc: "When an enemy hits an ally adjacent to Perrin, he makes one Longsword attack."
    sim: { id: pack_tactics_reaction, kind: extra_attack, attack: longsword,
           trigger: enemy_hits_adjacent_ally, cost: { resource: pack_tactics_reaction, spend: 1 } }
sim:
  side: party
  level: 5
  initiative: 4
  concentration_save: 3
  save_advantage:
    - { vs: poisoned, mode: advantage }
    - { vs: disease, mode: advantage }
    - { vs: str, mode: disadvantage } # Mortis "The Small" — carried from vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md
  resources:
    - { id: bardic_inspiration, max: 5, recharge: long_rest }
    - { id: bard_slot_1, max: 4, recharge: long_rest }
    - { id: bard_slot_2, max: 2, recharge: long_rest }
    - { id: pact_slot_1, max: 2, recharge: long_rest }
    - { id: pack_tactics_reaction, max: 3, recharge: short_rest }
  spellcasting:
    # Two independent pools — bard slots and pact slots never mix.
    # Dice/DCs come from each spell's own SRD page ([srd]); the picks are
    # the sheet's. Heals stay hand-coded above: the sheet's 2014-era
    # export states 1d4+5/1d8+5 and the sheet wins over the 2024 page.
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5, ability_mod: 5,
        source: bard,
        slots: { 1: bard_slot_1, 2: bard_slot_2 },
        known: ["Hideous Laughter"] }
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5, ability_mod: 5,
        source: warlock,
        slots: { 1: pact_slot_1 },
        known: ["Eldritch Blast", "Hex", "Armor of Agathys"] }
  routine:
    action: [longsword]
    bonus: []
    reaction: [cutting_words]
```

Not modeled (listed rather than guessed): Green-Flame Blade's fire splash to a SECOND creature (the engine models the primary target's level-5 fire rider above. The splash needs a two-target-per-swing primitive the engine lacks, and the `[verify]` on the export resolved against [[the spell page]]: 1d8 to the target, 1d8+5 to the second creature); [[Protection from Evil and Good]] (narrow creature-type-conditional defense, no general combat-math value); [[Silent Image]] (no default mechanical combat effect); [[Minor Illusion]], [[Mage Hand]] (no combat application); Magical Cunning (out-of-combat slot recovery, irrelevant to a single-encounter sim). Bardic Inspiration granted to allies (a cross-combatant pool grant the engine lacks. Cutting Words models the same 5-die pool) and Scurry positioning. Newly modeled by the v6 engine + spell library: [[Eldritch Blast]]'s two level-5 beams, [[Armor of Agathys]]' retaliation clause, Hex and [[Hideous Laughter]] as name-referenced library spells with the pact/bard slot economy enforced.

## Combat profile

Built from [[Perrin Black-Jaw|Perrin]]'s actual level-5 D&D Beyond export ([[Bard]] 3 / [[Warlock]] 2). His sheet does not carry [[Vicious Mockery]], [[Command]], or [[Comprehend Languages]].

## Fast Read

Support/control caster with a melee option — Bardic Inspiration is his key damage multiplier, not his own weapon; per his own page's Arc Notes, "the party's decisive force multiplier" · sustained DPR 9.38 vs AC 15 `[simulated]` · nova (p95, own kit, no ally grants) 18.0 vs AC 15 `[simulated]` · effective HP 49 `[sheet]` · Achilles heel: fragile frame, STR -2 with Mortis disadvantage, and a known tactical tell — [[Master Kyzil|Kyzil]] named the drum itself as a target mid-spar (S04); deadliest 1v1 corpus opponent is Ruk, 56.4% win `[simulated]`.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 18 (incl. [[Cloak of Protection]] +1) / 49, 2d8 (Warlock) + 3d8 (Bard) hit dice | `[sheet]` |
| Init / Speed | — | `[sheet]` |
| Hit% vs AC ladder | [[Longsword]] (Pact-bonded)/[[Green-Flame Blade]]/[[Eldritch Blast]], all +8, 5% crit: 80/70/60/50% vs AC 13/15/17/19 | `[simulated]` |
| Save bonuses (weak → strong) | STR -1 (Mortis disadvantage), INT +1, DEX +5, CON +3, WIS +4 (prof), CHA +9 (prof) | `[sheet]` |
| Resource pools (per rest) | Bardic Inspiration (shared w/ Cutting Words) ×5, Bard 1st-level slots ×4 ([[Healing Word]] draws here), Bard 2nd-level slots ×2, Pact Magic slots ×2, Pack Tactics reaction ×3 | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/perrin-black-jaw-sheet.md --seed 1`

Damage/round, whole-turn under `optimal` auto-policy: mean 10.89/9.38/8.24/6.83 at AC 13/15/17/19, p50 12.0/11.0/10.0/0.0, p95 19.0/18.0/18.0/18.0, max up to 33 `[simulated]`. Observed DPR: effectively 0 across six sessions through S06, when he dropped to 0 HP (§ Session Combat Log) — reflects support/control play-style, not build weakness.

Not modeled: [[Protection from Evil and Good]], [[Silent Image]], [[Minor Illusion]], [[Mage Hand]], Magical Cunning (out-of-combat slot recovery), Bardic Inspiration granted to allies, Scurry positioning (no cross-combatant pool-grant primitive). Modeled with caveat: Hex's curses/ability-check disadvantage compile to flat extra damage (debuff-on-others not captured); [[Armor of Agathys]] temp-HP/retaliation don't scale with higher slots, runs only at the slot level used. Green-Flame Blade's fire splash to a second creature models its level-5 primary-target rider. Now modeled by name via the spell library: Hex, [[Hideous Laughter]], [[Eldritch Blast]], Armor of Agathys.

Enemy hit chance: 40% vs +5, 50% vs +7, 60% vs +9, 70% vs +11. Attacks survived vs +7: 18.7 (5 dmg), 9.3 (10), 6.2 (15), 4.7 (20) `[simulated]`. Poison-damage sources: ~2× effective HP via resistance, plus advantage against poisoned/disease conditions. Escape/mitigation: boneless gives advantage escaping wrestling/restrained; Cutting Words subtracts 1d6 from an incoming roll (shared 5-die pool); Armor of Agathys grants 5 temp HP per Pact slot as a pre-fight buff.

## Counters & Synergy

Hard counters (observed): focus-fire on Perrin himself — Kyzil named the drum as a target (S04), removing him removes the party's Inspiration multiplier. Hard counters (theoretical): wrestling/shove attacks — STR -2 with disadvantage ends melee and nova lines. Soft counters: ranged focus (49 HP lasts ~3 rounds vs three +7 attackers), Stun and Chirr-class WIS saves (+4, middling), area damage (no Evasion). Non-counter: poison (resistance + condition advantage). No answer for: a focused attacker closing distance with no Shield reaction, flight beyond 120 ft, isolated high-CR solo threats.

Worst-5 empirical (1v1 solo, band-filtered): Ruk 56.4%, [[Owlbear]] 58.3%, [[Elder Mimic]] 58.5%, [[Mummy]] 59.9%, [[Winter Wolf]] 62.6% `[simulated]`. True hard walls (0.0% win, 1–2 rounds): [[Aboleth]], [[Adult Black Dragon]], [[Adult Blue Dragon]].

Amplifies: the whole party via Bardic Inspiration — each d6 averages ~+2.6 on failed D20 Tests, flipping ~13% of misses; flipped Crissdalynn's failed wrestling contest (15+d6=20 vs Downburst) `[session-04]`; Cutting Words uses the same die against enemy rolls (vs Kyzil, insufficient, S04). Depends on: allies within 60 ft and available charges — his nova line depends on an ally advantage source ([[Faerie-Fire]] or prone); without it, collapses toward the sustained mean. Observed: S03 spread 3 Inspiration pre-fight; S04 touched four pools in one combat (Healing Word ×2, Inspiration, Cutting Words). Simulated resource spend solo vs [[Grung Elite Warrior]]: 4.38/encounter `[simulated]` — pools drain on allies, not himself; bardic inspiration is most constrained, 2nd-level slots and pact magic least.

## Session Combat Log

| Session | Encounter | Rounds active | Damage dealt | Damage taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 01 | [[Saltwright]] boarding | `[unknown]` | `[unknown]` | `[unknown]` | `[unknown]` | Laid Minor Illusion over the hold doorway; emerged from a deck gap during the breach; resisted [[Grung]] toxin gas (save passed, no number given) |
| 02 | Conflict aboard ship (vs. Ket) | `[unknown]` | 0 (drew Longsword, didn't attack. Crissdalynn intervened first) | `[unknown]` | 0/0 | Cast Tasha's Hideous Laughter to drop Ket safely instead |
| 03 | [[Whip Shark]] fight | `[unknown]` | `[unknown]` | `[unknown]` | `[unknown]` | Spent 3 Bardic Inspiration (all three other party members). "Drummed through" the fight. No attack/damage numbers in the source |
| 04 | Kyzil spar + sewers | `[unknown]` | 0 (no attack recorded) | `[unknown]` | 0/0 | Healing Word ×2 (Delmar +7, Crissdalynn +8). Bardic Inspiration saved Crissdalynn's wrestling (15+d6=20 vs. Downburst). Cutting Words attempt vs. Kyzil's attack proved insufficient (failed). Kyzil called out the drum as a target |
| 06 | Primary Chamber fight | `[unknown]` | 0 (no attack recorded) | dropped to 0 HP | 0/0 | Failed death save reached his patron on the deathbed roll (15, needed 10+). Patron intervention allowed him to continue. He stabilized, coughing seawater at 1 HP. He leveled up to Bard 3 (College of Lore) and Warlock 2 (Pact of the Blade) |

> [!dm] Transcription note
> Every "damage dealt" cell above is 0 or `[unknown]`, not a transcription gap. The source simply doesn't record him landing an attack in 6 sessions.

## Calibration

Simulated-vs-observed delta: simulated sustained 9.38 vs AC 15; observed output ~0 over 6 sessions — reflects play-style, not build error. Encounter math should count Perrin as ~0 personal DPR, a defensive/offensive multiplier instead (his die keeps one martial ally functional roughly one extra round per fight). Confidence: mechanical/simulated lines use real sheet inputs, reproducible (high). Resource/synergy observations low confidence (2 sessions with numbers). Offensive observations theoretical (0 attack observations in 6 sessions). Unsimulable: the 18.0 nova figure requires ally advantage AND melee position — Kyzil showed melee as his danger zone, so read it as a low-confidence ceiling, not a table-typical line; cutting words, healing word, [[cure wounds]], and the Pack Tactics reaction are now real schema primitives, no longer flagged unsimulable. Next data point needed: any session recording his actual attack rolls.

## Gallery

# Perrin Black-Jaw Gallery

Visual reference for [[Perrin Black-Jaw]].

## Portraits

![[perrin-black-jaw-banner|Perrin Black-Jaw banner]]

## Reference

![[perrin-black-jaw-reference|Perrin Black-Jaw likeness reference]]
![[perrin-black-jaw-reference|Perrin Black-Jaw likeness reference, source scan]]

## Inventory

# Perrin Black-Jaw — Inventory

What [[Perrin Black-Jaw]] carries and where he keeps the rest.

## Attuned Magic Items

| Item | Attuned? | Effect in play |
|---|---|---|
| [[Cloak of Protection]] | Yes | +1 to AC and all saving throws |
| [[The Snap]] | Not confirmed | Bracer that unfurls into a +2 AC shield without occupying a hand; bought from [[Prospero Morsani]] for 150 gold, Session 08 |

## Carried Gear

| Item | Qty | Why it matters |
|---|---|---|
| [[Longsword]] (Pact-bonded) | 1 | Bonded weapon under Pact of the Blade; CHA replaces STR/DEX for attack/damage |
| Studded Leather | 1 | Part of his AC base with the Cloak and Shield |
| Shield | 1 | Part of his AC base with the Cloak and Studded Leather |
| [[Dagger]] | 2 | Paired daggers |
| Mira's Blade | 1 | Received from the cargo in Session 02 (`vault/episodes/002/`); no mechanical write-up on the sheet beyond the physical weapon |
| Bodhran drum | 1 | The instrument behind his Bardic Inspiration; [[Master Kyzil]] identified it as a tactical threat |
| Orb | 1 | Unidentified |
| [[Algernon Reginald Clyde|Clyde]]'s Bestiary of Oceanic Creatures | 1 | Reference material |
| [[Sending Stone (Nona's)|Nona's sending stone]] | 1 | Gift from [[Nona Black-Jaw]], Session 03 |

Skipped as mundane: [[Backpack]], Oil ×10, [[Parchment]] ×10, [[Tinderbox]], [[Lamp]], [[Ink Pen]], Ink.

## Stowed & Cached

The sheet records no stowed or cached items.

## Currency

| Coin | Amount |
|---|---|
| Gold | Untracked on the sheet; Perrin estimated "I think I only have like 15 gold. I have more than that" in Session 08 (`vault/episodes/008/`) |

## Spells

# Perrin Black-Jaw — Spells

[[Perrin Black-Jaw]]'s spell list. A multiclass caster keeps each class's pool
separate — Pact Magic is not a [[Bard]] slot and the two never merge.

## Spellcasting

| Class | Ability | Save DC | Attack Bonus | Prepared / Known |
|---|---|---|---|---|
| Bard | CHA | 16 | +8 | Known |
| [[Warlock]] | CHA | 16 | +8 | Known |

## Cantrips

| Cantrip | Class | Effect at this level |
|---|---|---|
| [[Minor Illusion]] | Bard | No default mechanical combat effect |
| [[Mage Hand]] | Bard | No combat application |
| [[Eldritch Blast]] | Warlock | 2 beams, 1d10 force each, at Warlock 2 |
| [[Green-Flame Blade]] | Warlock | Melee strike plus a fire rider; exact splash-target legibility flagged `[verify]` — see the Combatant Block on `vault/campaigns/shattered-sea/pcs/character-sheets/perrin-black-jaw-sheet.md` |

## Known & Prepared

| Level | Spell | Class | Key effect |
|---|---|---|---|
| 1 | [[Healing Word]] | Bard | Bonus Action heal, 1d4+5 HP within 60 ft |
| 1 | [[Cure Wounds]] | Bard | Touch heal, 1d8+5 HP |
| 1 | [[Tasha's Hideous Laughter]] | Bard | Incapacitates a creature that fails its save |
| 1 | [[Silent Image]] | Bard | No default mechanical combat effect |
| 1 | [[Hex]] | Warlock | Curses a target, extra necrotic damage on hits |
| 1 | [[Armor of Agathys]] | Warlock | Temp HP, retaliation damage to melee attackers |
| 1 | [[Protection from Evil and Good]] | Warlock | Narrow creature-type-conditional defense |
| 2 | [[Invisibility]] | Bard | Grants invisibility to a touched creature |
| 2 | [[Mirror Image]] | Bard | Creates illusory duplicates to absorb attacks |

## Slots & Pools

| Pool | Slots by level | Recovery |
|---|---|---|
| Bard slots | 1st — 4, 2nd — 2 | Long Rest |
| Pact Magic (Warlock, separate pool) | 1st — 2 | Long Rest (Magical Cunning can regain 1, out-of-combat only) |

## Stats

# Perrin Black-Jaw — Attributes

Mechanical attributes for [[Perrin Black-Jaw]], transcribed from
`_assets/character-sheets/perrin-black-jaw-character-sheet.pdf`. A value the sheet
states wrongly is transcribed as printed and tagged `[verify]`, never
silently corrected. This page is the single source of truth for every
per-ability, per-skill, and per-speed value; `ac`, `hp_max`,
`class_levels`, and `level` stay in [[Perrin Black-Jaw]]'s frontmatter and are
never restated here.

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| [[Strength]] | 6 | -2 | -1 | no |
| [[Dexterity]] | 18 | +4 | +5 | no |
| [[Constitution]] | 15 | +2 | +3 | no |
| [[Intelligence]] | 11 | +0 | +1 | no |
| [[Wisdom]] | 11 | +0 | +4 | **yes** |
| [[Charisma]] | 20 | +5 | +9 | **yes** |

Proficiency bonus +3 (character level 5). Save proficiencies are WIS/CHA ([[Warlock]]'s). The attuned [[Cloak of Protection]] adds +1 to every saving throw above, folded into the Save column.

His Mortis ("The Small") gives disadvantage on Strength checks/saves, carried forward from [[Perrin Black-Jaw|his hub page]].

## Skills

Expertise (double proficiency) covers acrobatics +10 and persuasion +11.
Full proficiency bonus applies to arcana +3, history +3, insight +3,
investigation +3, perception +3, and stealth +7. Jack of All Trades (half
proficiency, rounded down) covers athletics -1, animal handling +1,
deception +6, intimidation +6, medicine +1, nature +1, performance +6,
religion +1, sleight of hand +5, and survival +1.

Passive Perception 13, Passive Insight 13, Passive Investigation 13.

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative | +4 | DEX mod |
| Speed | 30 ft. walking, 30 ft. swimming | Rattkin Swimmer trait |
| Hit dice | 2d8 (Warlock) + 3d8 ([[Bard]]) | sheet |
| Proficiency bonus | +3 | character level 5 |
| Damage resistances | Poison | Rattkin Survivor |
| Condition advantages | Advantage vs. poisoned/disease (Survivor). Advantage vs. Grapple/[[Restrained]] (Boneless) | Rattkin traits |

AC and max HP live in [[Perrin Black-Jaw]]'s frontmatter (`ac:`, `hp_max:`) — the roster `.base` views query them there; this table carries no rows for them.

## Proficiencies & Languages

Languages: common, Dwarvish, Gnomish (sheet's Proficiencies box). A flagged discrepancy against his [[Rattkin]] species trait text lives on `vault/campaigns/shattered-sea/pcs/character-sheets/perrin-black-jaw-sheet.md`, not reconciled here.

Species traits granting proficiencies/senses (Keen Senses, Scurry, Survivor, Swimmer, Boneless) live on [[his abilities page]], not described twice here.

## Voice

*(Try to stay as in character from now on, its okay if you lose character just stop, breathe, and continue. Capturing how you, and/or your character, naturally speak is the point.)*

I am reading for [[Perrin Black-Jaw]]

Three feet of rat, one longsword too big for me, and a drum that keeps better time than most of the men I've sailed with.

Call the roll with me. Delmar Fisk. [[Jean-Claude Tabarnack]]. [[Crissdalynn Khinriss]]. Perrin Black-Jaw. Four names, one Run, and I'm the one who counts them.

I lead by reading currents, reading people, reading exits — the sea decided I wasn't built for hauling rope, so I got better at everything else.

Black-jawed, big-boned, bold-hearted boys bought bread by the bay — that's what they called my grandfather's whole crew, and I've been living up to it since I could talk.

Loyal to my Run, proud of my blood, and I will bribe, bluff, or blackmail my way through a locked door before I ever raise a fist.

I am, by every account that matters, impossible to look away from.

I miss fishing more than I miss most people, and that is the truth whether or not it flatters me.

Whatever put my family's ship on the seafloor is going to learn my name the hard way, one debt at a time.

Swift ships skim slick shoals while sharp-eyed skippers scan the swell — that's the chant I keep on watch, word for word, every single night.

I have carried a bardic drumbeat through a fight that should have killed all four of us, and I intend to carry it through several more.

*(sincerely)*

There is, I'll admit, a version of me that got so used to being the loudest thing in a small package that I forgot to ask anyone if they wanted the volume up.

*(proud of yourself)*

Jean-Claude thinks any two people touching hands is the start of a wedding. I've shaken that hand nine times. Deep down, I think he considers us engaged.

*(commandingly)*

Fall in, [[Uncertainty]] — that's the ship's name now, I picked it myself, off the top of my head, mid-crisis, and I stand by it completely.

*(whispered, like someones sleeping)*

I once climbed into a barrel to make an entrance. A barrel. And it worked, which is somehow worse.

*(sarcastically)*

[[Master Kyzil]] looked at my drum and called it a tactical threat. He's not wrong. He's just never had to carry it up a ladder.

*(delighted, like your seeing a puppy)*

Black-Jaw's big black bodhran barely beats before the blade breaks through — badly, boldly, brilliantly, every blasted time.

*(fondly, to an old friend)*

Delmar's got five dead captains arguing in his skull about which hat to wear, and most mornings the hat loses.

*(startled)*

Say the word abyss near me and watch me forget every clever thing I have ever said in my whole miserable life.

*(furiously winning an argument in the shower later)*

Say whatever you like about my sword being too big for me — I have buried it exactly where I meant to, every single time.

*(earnestly)*

And before anyone says a word — the gangster voice is not a bit, it is my grandfather, and I will talk like a man out of a [[Calveno]] crime serial until the day I die if it means keeping one more piece of him alive at this table, and if that means [[Nona Black-Jaw|Nona]] smiles every time I open my mouth then frankly I have already won, and no, I am not going to explain the barrel again, the barrel worked.

*(proudly and confidently)*

Fine. Fine — I am three feet tall, I climbed out of a barrel to intimidate a man twice my height, I renamed a warship on a whim, and I still won't wear shoes because my little rat feet need to feel the ground. Say that with a straight face.

*(fondly)*

Crissdalynn once caught me clean out of the sky, talons and all, and some animal part of me still flinches at her wings before my brain remembers she's the reason I'm still breathing.

*(like it’s code for getting laid)*

And every single time — every — single — time — it works.

*(chanting)*

BLACK-JAW! BLACK-JAW! BLACK-JAW!

*(flirtatiously)*

Three feet tall, impossible to look away from, and — fine — mostly for the reasons you'd expect. Nine and a half out of ten. I'm deducting half a point for the barrel.
