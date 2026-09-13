---
title: "Catarina Da'Virelli"
category: entities
tags: ["shattered-sea", "npc", "pc"]
sources:
  - "campaign-os:catarina-davirelli-voice-script.md"
  - "campaign-os:catarina-davirelli-stats.md"
  - "campaign-os:catarina-davirelli-spells.md"
  - "campaign-os:kaitlin.md"
  - "campaign-os:catarina-davirelli-inventory.md"
  - "campaign-os:catarina-davirelli-gallery.md"
  - "campaign-os:catarina-davirelli-combat-profile.md"
  - "campaign-os:catarina-davirelli-sheet.md"
  - "campaign-os:catarina-davirelli.md"
  - "campaign-os:catarina-davirelli-abilities.md"
  - "00 Shattered Sea.md"
summary: "Player character at the Shattered Sea table, played by Kaitlin."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T19:30:00Z
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
visibility: dm
status: alive
role: "PC"
---
# Catarina Da'Virelli

[[Catarina Da'Virelli]] is a player character at the [[Shattered Sea]] table. Kaitlin plays her.

## Connections

- [[Shattered Sea]]
- [[Uncertainty]]

## Abilities

# Catarina Da'Virelli, Abilities

Built from the player's character sheet. One section per action-economy
slot so a table runner can transclude exactly the one they need mid-round
(`![[Catarina Davirelli Abilities]]`) — an ability that costs an
Action goes under Actions and is named, not repeated, anywhere else.

Everything [[Catarina Da'Virelli]] can do, sorted by what it costs to do it.
[[Her spells page]] lists all spells; only the class feature that
grants the casting appears here.

## Traits

The sheet itemizes no species traits for her [[Human]] (Variant)
heritage beyond the [[Alert]] feat, which appears under Feats below.

## Features

| Feature | Source | Effect | Uses | Recovery |
|---|---|---|---|---|
| Magical Tinkering | [[Artificer]] | Imbue a nonmagical object with a minor magical property (light, sound, message, visual effect) | 5 objects at a time | - |
| Spellcasting | Artificer | Prepared artificer spells, INT-based, ritual tag usable as ritual, needs a spellcasting focus (thieves'/artisan's tools or arcane focus) | - | - |
| Infuse Item | Artificer | Touch up to 2 nonmagical objects at end of a long rest, turn into magic items; infusion vanishes 5 days after death or if you end the attunement | 2 infusions | Long Rest (creation) |
| Artificer Infusions | Artificer | Known infusion list, includes Repeating Shot (per the Flintlock Pistol's sheet note) | - | - |
| The Right Tool for the Job | Artificer | Magically create one set of artisan's/thieves' tools in an unoccupied space within 5 ft; requires 1 hour uninterrupted work coinciding with a short/long rest | - | 1 hour |
| Tool Expertise | Artificer | Expertise with woodcarver's tools plus one other artisan's tool of choice | - | - |
| Artillerist Spells | Artificer (Artillerist) | [[Shield]], [[Thunderwave]], [[Scorching Ray]], and [[Shatter]] are always prepared | - | - |

## Actions

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
|---|---|---|---|---|
| Eldritch Cannon (create) | - | Action to create a cannon within 5 ft, one at a time | 1 / Long Rest | Bonus Action to activate (see Bonus Actions) |
| Flintlock Pistol | +3 | 8 (1d10+3) piercing | - | `[verify]` doesn't match DEX+prof (+5) if proficient with firearms; sheet prints +3 as-is, transcribed unchanged |
| Unarmed Strike | +4 | 2 bludgeoning | - | - |

Her two attack cantrips, [[Fire Bolt]] and [[Shocking Grasp]], are on [[her spells page]].

## Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
|---|---|---|---|---|
| Eldritch Cannon (Flamethrower) | activate a created cannon within 60 ft | 15-ft cone, DC 17 [[Dexterity]] save for each creature in the cone: 9 (2d8) fire damage, half on a success | shares the cannon's 1/long-rest use | Long Rest |
| Eldritch Cannon (Force Ballista) | activate a created cannon within 60 ft | Ranged spell attack +9, one target within 120 ft, 9 (2d8) force damage, pushes the target 5 ft | shares the cannon's 1/long-rest use | Long Rest |
| Eldritch Cannon (Protector) | activate a created cannon within 60 ft | 1d8+5 temporary hit points to the cannon and creatures within 10 ft | shares the cannon's 1/long-rest use | Long Rest |

## Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
|---|---|---|---|---|
| [[Absorb Elements]] | takes acid, cold, fire, lightning, or thunder damage | Resistance to that damage type until the start of her next turn | costs a 1st-level spell slot | Long Rest |

## Feats

| Feat | Source | Effect |
|---|---|---|
| Alert | Variant Human | +5 to initiative (already folded into her Initiative stat); creatures cannot surprise her while she's conscious; other creatures don't gain advantage on attack rolls against her from being unseen |

## Character sheet notes

From D&D Beyond (exported by player: nickdavenock). PDF: `_assets/character-sheets/catarina-davirelli-character-sheet.pdf`.

`[verify]` Flintlock Pistol to-hit (+3) doesn't match DEX mod (+2) + skill bonus (+3) = +5 if she's proficient with firearms. Sheet shows +3 as printed, transcribed as-is, not corrected.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | `vault/campaigns/shattered-sea/pcs/stats/catarina-davirelli-stats.md` | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | `vault/campaigns/shattered-sea/pcs/abilities/catarina-davirelli-abilities.md` | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | `vault/campaigns/shattered-sea/pcs/spells/catarina-davirelli-spells.md` | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | `vault/campaigns/shattered-sea/pcs/inventory/catarina-davirelli-inventory.md` | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/catarina-davirelli.md` frontmatter | `_templates/pc.md` |

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Catarina Da'Virelli
size: Medium
type: humanoid
alignment: neutral good
ac: 16
hp: 38
hit_dice: "5d8"
speed: "30 ft."
stats: [13, 14, 15, 20, 12, 10]
saves: { str: 1, dex: 2, con: 5, int: 8, wis: 1, cha: 0 }
actions:
  # Fire Bolt/Shocking Grasp removed as hand-coded actions — the sheet's
  # printed 2d10/2d8 dice already match each cantrip's own SRD page at
  # level 5 (cantrip_scaling), so both now come from sim.spellcasting.known
  # below instead of being re-encoded here (sheet and page agree, no
  # divergence to preserve).
  - name: "Flintlock Pistol"
    # [verify] sheet prints +3 to-hit; doesn't match DEX+prof (+5) if
    # proficient with firearms — transcribed as printed, not corrected.
    desc: "Ranged Weapon Attack: +3 to hit, range 30/90 ft., one target. Hit: 8 (1d10 + 3) piercing damage."
    sim: { id: flintlock_pistol }
bonus_actions:
  # [srd vault/srd/classes/subclasses/artificer-artillerist.md]
  # Eldritch Cannon — Flamethrower/Force Ballista, exact page dice/DC.
  # Both draw on the same 1/long-rest eldritch_cannon resource, so this
  # models only a SINGLE activation per long rest — an approximation of
  # the summon (the real cannon persists once created and can be
  # activated again every turn for free; this sim has no
  # summon-as-persistent-object primitive, so the whole lifecycle is
  # compressed into one paid use). Protector's temp HP and the cannon's
  # own AC 18/HP (5 × artificer level) statblock are not modeled at all.
  - name: "Eldritch Cannon — Flamethrower"
    desc: "*Dexterity Saving Throw*: DC 17, each creature in a 15-foot Cone. *Failure:* 9 (2d8) Fire damage. *Success:* Half damage."
    sim: { id: eldritch_cannon_flamethrower, cost: { resource: eldritch_cannon, spend: 1 } }
  - name: "Eldritch Cannon — Force Ballista"
    # 5-ft push on a hit not modeled (no forced-movement primitive).
    desc: "Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 9 (2d8) force damage."
    sim: { id: eldritch_cannon_force_ballista, cost: { resource: eldritch_cannon, spend: 1 } }
reactions:
  # [sheet+srd vault/srd/spells/abjuration/absorb-elements.md] Resistance to
  # the triggering damage type, modeled as a flat 50% reduction. The
  # retaliatory 1d6 rider on her next melee hit isn't modeled (no
  # next-turn damage-boost primitive tied to a reaction).
  - name: "Absorb Elements"
    desc: "When Catarina takes acid, cold, fire, lightning, or thunder damage, she can take a Reaction to gain Resistance to that damage type until the start of her next turn."
    sim: { id: absorb_elements, kind: damage_reduction_pct, fraction: 0.5,
           damage_types: [acid, cold, fire, lightning, thunder], trigger: self_hit,
           cost: { resource: slot_1, spend: 1 } }
  # Shield removed as a hand-coded reaction — now compiled from
  # sim.spellcasting.known below (its reaction_ac_bonus modifier is
  # checked automatically, same as every other Shield-casting PC sheet).
sim:
  side: party
  level: 5
  initiative: 7 # DEX +2 + Alert +5, folded per sheet
  concentration_save: 5 # plain CON save, no War Caster per sheet note
  resources:
    - { id: slot_1, max: 4, recharge: long_rest }
    - { id: slot_2, max: 2, recharge: long_rest }
    - { id: eldritch_cannon, max: 1, recharge: long_rest }
  spellcasting:
    # DC/attack_bonus are the sheet's printed values (already include the
    # All-Purpose Tool +1). Dice come from each spell's own SRD page
    # [sheet+srd] — checked this turn, every one confirmed on her prepared
    # list (Identity/Spellcasting sections above). Cure Wounds, Detect
    # Magic, and the rest of her long utility list stay out of known: —
    # candidates checked this pass were exactly the ones with a
    # damage/save line on the sheet (Fire Bolt, Shocking Grasp, Scorching
    # Ray, Shatter, Thunderwave, Faerie Fire, Web, Grease, False Life,
    # Aid, Blur, Magic Weapon, Catapult, Shield).
    - { ability: int, dc: 17, attack_bonus: 9, level: 5, ability_mod: 5,
        slots: { 1: slot_1, 2: slot_2 },
        known: ["Fire Bolt", "Shocking Grasp", "Scorching Ray", "Shatter",
                "Thunderwave", "Faerie Fire", "Web", "Grease", "False Life",
                "Aid", "Blur", "Magic Weapon", "Catapult", "Shield"] }
  routine:
    action: [fire_bolt, flintlock_pistol]
    bonus: []
```

## Combat profile

## Fast Read

Ranged blaster (INT) · sustained DPR 13.91 vs AC 15 `[simulated]` · nova DPR 28.0 vs AC 15 (p95) `[simulated]` · effective HP 38 raw, AC 16 `[sheet]` · Achilles heel: flat CON +5 concentration save (no War Caster) — grapplers and reach attackers break her focus; toughest matchup [[Vashu the Weeping Veil|Vashu, the Weeping Veil]] (Winded), 50.4% win `[simulated]`.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 16 (Breastplate) / 38, 5d8 hit dice | `[sheet]` |
| Init / Speed | — | `[sheet]` |
| Hit% vs AC ladder | [[Fire Bolt]]/Shocking Grasp/[[Scorching Ray]]/Cannon +9: 85/75/65/55% vs AC 13/15/17/19, 5% crit. Flintlock Pistol +3 `[verify]`: 55/45/35/25%, 5% crit | `[simulated]` |
| Save bonuses (weak → strong) | STR +1, WIS +1, CHA +0, DEX +2, CON +5, INT +8; concentration flat CON +5 | `[sheet]` |
| Resource pools (per rest) | Eldritch Cannon ×1, Infuse Item ×2 items, 1st-level slots ×4, 2nd-level slots ×2 (Scorching Ray/Shatter/[[Catapult]]) | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/catarina-davirelli-sheet.md --seed 1`

Damage/round ([[Fire Bolt]] + Flintlock Pistol, the sheet's declared routine): mean 15.94/13.91/11.95/9.89 at AC 13/15/17/19, p95 29.0/28.0/27.0/25.0, max up to 56 `[simulated]`. Eldritch Cannon, [[Scorching Ray]], and [[Shatter]] carry real damage dice but sit outside the routine, so they don't appear in this table — they do spend resources in full-kit encounter sims: 39.5 dmg / 4.84 resources vs [[Aboleth]] (4.5 rounds), 9.9 dmg / 1.13 resources vs [[adult-black-dragon]] (1.3 rounds), 0.1 dmg / 1.97 resources vs [[Adult Blue Dragon]] (1.3 rounds) `[simulated]` — her 3 deadliest 1v1 losses (§ Counters & Synergy).

Enemy hit chance vs her AC (before Shield, which adds +5 but isn't folded in): 50% vs +5, 60% vs +7, 70% vs +9. Attacks survived vs +7: 12.2 (5 dmg/hit), 6.1 (10), 4.1 (15), 3.0 (20) `[simulated]`.

Not modeled: [[Heat Metal]] (no re-trigger primitive), [[Tasha's Caustic Brew]] (no per-turn damage-over-time primitive), [[Tortoise Shell]] (no flat-AC-set primitive), Eldritch Cannon's Protector temp-HP/statblock (no persistent-summon primitive), Infuse Item (no combat-facing primitive). Modeled with caveat: [[Grease]] (only initial save models), [[False Life]] (flat 9 temp HP, no per-slot scaling), Aid (bonus to [[Catarina Da'Virelli|Catarina]] only, scales per slot), [[Blur]] (fails vs Blindsight/Truesight), [[Magic Weapon]] (+1 damage, caster-only), [[Absorb Elements]] (no 1d6 retaliatory rider), [[Thunderwave]] (push + object damage model, outside routine).

## Counters & Synergy

Hard counters: grapplers/reach attackers break concentration `[theoretical]`; [[Aboleth]], [[Adult Black Dragon]], [[Adult Blue Dragon]] — 0% win, 1.3–4.5 rounds `[simulated]`. Soft counters: range denial, no-spell zones `[theoretical]`; Vashu (Winded) 50.4%, [[Vampire Spawn]] 53.3%, [[The Rattle Statblock]] 54.2%, [[Winter Wolf]] 54.9%, [[Owlbear]] 55.7% `[simulated]`. Non-counter: surprise ([[Alert]] blocks it).

Amplifies: whole party via advantage spell (costs a real slot, no longer free) — [[Shocking Grasp]] denies reactions `[theoretical]`. Depends on: frontline support to protect her concentration.

## Session Combat Log

Not yet played (see `vault/campaigns/shattered-sea/pcs/catarina-davirelli.md` Session Log). Append session, encounter, dmg dealt, dmg taken, hits/attacks, note once she's at the table.

## Calibration

Simulated-vs-observed delta: none yet, 0 sessions `[theoretical]`. Confidence: mechanical/simulated figures reproducible at stated seed; all observed data `theoretical` (`confidence_level: theoretical` unchanged). Unsimulable: no `--loadout` spell-nova run exists — Scorching Ray/Cannon full-kit ceiling is above the routine-only DPR table above.

## Gallery

# Catarina Da'Virelli Gallery

Visual reference for [[Catarina Da'Virelli]].

## Portraits

![[catarina-davirelli-portrait|Catarina Da'Virelli portrait]]
![[catarina-davirelli-banner|Catarina Da'Virelli banner]]

## Reference

![[caterina-davirelle-reference|Catarina Da'Virelli likeness reference]]

## Inventory

# Catarina Da'Virelli — Inventory

What [[Catarina Da'Virelli|Catarina]] is carrying, and where the rest of it is. Mundane kit is skipped; everything below has a mechanical effect or a story attached.

## Attuned Magic Items

She has one attuned item.

| Item | Attuned? | Effect in play |
|---|---|---|
| All-Purpose Tool, +1 | yes | boosts spells and craft work |

## Carried Gear

| Item | Qty | Why it matters |
|---|---|---|
| [[Bag of Holding]] | 1 | extra storage; lent to [[Delmar Fisk|Delmar]] in Session 07 to carry a recovered chair |
| Fire Wand | 1 | ranged fire spells |
| Flintlock Pistol | 1 | backup weapon |
| Armor | 1 | AC 16 |
| Sword, Hammer, Wand, Bomb | 1 each | combat kit |
| [[Pearl of Power]] | 1 | Bought from [[Lavinia Sordi]] at [[La Cenere]] for 300 gold, Session 08; unstable, loosened weave, two charges left |

## Stowed & Cached

Spare parts and half-finished builds stay racked at [[Cat's Curios]], her own workshop. The one thing worth a special trip: the Spark Pistol prototype, locked in the specimen cabinet until she solves the misfire flaw that keeps it from firing lightning reliably in the wet.

## Currency

| Coin | Amount |
|---|---|
| Copper | 0 |
| Electrum | 23 |
| Platinum | 0 |
| Gold | 112 |
| Silver | 90 |

## Player

Played by **Kaitlin**.

# Kaitlin

Kaitlin plays [[Catarina Da'Virelli]] in [[The Shattered Sea]].

## Campaigns & Characters

| Campaign | Character | Status |
|---|---|---|
| [[The Shattered Sea]] | [[Catarina Da'Virelli]] | active |

## Notes

No additional notes.

## Spells

# Catarina Da'Virelli — Spells

[[Catarina Da'Virelli|Catarina]]'s spells. See [[her abilities page]] for Eldritch Cannon, Infuse Item, and Magical Tinkering.

## Spellcasting

| Class | Ability | Save DC | Attack Bonus | Prepared / Known |
|---|---|---|---|---|
| [[Artificer]] | INT | 17 | +9 | Prepared |

## Cantrips

| Cantrip | Class | Effect at this level |
|---|---|---|
| [[Fire Bolt]] | Artificer | +9 to hit, 2d10 fire, range 120 ft |
| [[Shocking Grasp]] | Artificer | +9 to hit (melee touch), 2d8 lightning, target can't take reactions until the start of its next turn |

## Known & Prepared

| Level | Spell | Class | Key effect |
|---|---|---|---|
| 1st | [[Shield]] | Artificer (Artillerist, always prepared) | Reaction, +5 AC until the start of her next turn |
| 1st | [[Thunderwave]] | Artificer (Artillerist, always prepared) | CON 17 save |
| 2nd | [[Scorching Ray]] | Artificer (Artillerist, always prepared) | +9 to hit |
| 2nd | [[Shatter]] | Artificer (Artillerist, always prepared) | CON 17 save |
| 1st | [[Faerie Fire]] | Artificer | no attack roll or save for her; outlines targets, denies them the [[Invisible]] condition's benefit |
| 1st | [[Web]] | Artificer | DEX 17 save |
| 1st | [[Grease]] | Artificer | DEX 17 save |
| 1st | [[False Life]] | Artificer | temporary hit points, no save |
| 2nd | [[Aid]] | Artificer | no save, raises current/max HP |
| 2nd | [[Blur]] | Artificer | no save, imposes disadvantage on attacks against her |
| 2nd | [[Magic Weapon]] | Artificer | no save, +1 to a weapon's attack/damage |
| 2nd | [[Catapult]] | Artificer | DEX 17 save |
| (special) | [[Absorb Elements]] | Artificer | Reaction, resistance to the triggering damage type. See [[her abilities page]] |

Her remaining prepared/known utility list ([[Identify]], [[Alarm]], [[Cure Wounds]],
[[Detect Magic]], [[Disguise Self]], [[Expeditious Retreat]], [[Feather Fall]], [[Jump]],
[[Longstrider]], [[Purify Food and Drink]], [[Sanctuary]], Snare, [[Tasha's Caustic Brew]],
[[Rope Trick]], [[Arcane Lock]], [[Invisibility]], [[Continual Flame]], Darkvision, [[Enhance Ability]], [[Enlarge/Reduce]], [[Heat Metal]], [[Lesser Restoration]], [[Levitate]], [[Magic Mouth]],
[[Protection from Poison]], [[See Invisibility]], [[Spider Climb]], Pyrotechnics,
Skywrite, [[Alter Self]], [[Tortoise Shell]]) is on the sheet but carries no
damage or save line worth a table row here.

## Slots & Pools

| Pool | Slots by level | Recovery |
|---|---|---|
| Artificer spell slots | 1st: 4, 2nd: 2 | Long Rest |

## Stats

# Catarina Da'Virelli — Attributes

Mechanical attributes for [[Catarina Da'Virelli]],
transcribed from `_assets/character-sheets/catarina-davirelli-character-sheet.pdf`.
A value the sheet states wrongly is transcribed as printed and tagged
`[verify]`, never silently corrected. This page is the single source of
truth for every per-ability, per-skill, and per-speed value; `ac`,
`hp_max`, `class_levels`, and `level` stay in [[Catarina Da'Virelli]]'s
frontmatter and are never restated here.

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| [[Strength]] | 13 | +1 | +1 | no |
| [[Dexterity]] | 14 | +2 | +2 | no |
| [[Constitution]] | 15 | +2 | +5 | **yes** |
| [[Intelligence]] | 20 | +5 | +8 | **yes** |
| [[Wisdom]] | 12 | +1 | +1 | no |
| [[Charisma]] | 10 | +0 | +0 | no |

## Skills

**Full proficiency:** Arcana (INT) +8, Investigation (INT) +8, Insight (WIS)
+4, Sleight of Hand (DEX) +5, Persuasion (CHA) +3.

**Untrained (ability mod only):** Nature (INT) +5, Religion (INT) +5,
Deception (CHA) +0; all other skills.

Passive Perception 11, Passive Insight 14, Passive Investigation 18.

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative | +7 | DEX +2 + [[Alert]] feat +5 |
| Speed | 30 ft. walking | sheet |
| Hit dice | 5d8 | sheet |
| Proficiency bonus | +3 | character level 5 |
| Damage resistances | none listed on sheet | sheet |
| Condition advantages | she gains surprise immunity while conscious. Other creatures lose advantage from unseen attacks | [[Alert]] feat |

AC and max HP live in [[Catarina Da'Virelli]]'s frontmatter (`ac:`, `hp_max:`)
— the roster `.base` views query them there; this table carries no rows
for them.

## Proficiencies & Languages

Tool skills include woodcarver's tools plus one other artisan's tool of choice
([[Artificer]] class feature). The sheet lists no armour, weapon, or language
skills beyond what class and equipped gear provide.

See [[her abilities page]] for Alert feat details.

## Voice

*(Try to stay as in character from now on, its okay if you lose character just stop, breathe, and continue. Capturing how you, and/or your character, naturally speak is the point.)*

I am reading for [[Catarina Da'Virelli]]

My name is Catarina Da'Virelli. Ask anyone in [[Calveno]] who fixes what magic can't, and they'll walk you to a door on a side street with brass fittings and no sign. That's me. [[Cat's Curios]]. Referral only.

I don't do walk-ins, and I don't do liars. Tell me something's broken and I'll tell you exactly why, exactly how long the fix takes, and exactly what it costs. If I can't build it, I say so. I have never once told a customer a prototype was finished when it wasn't. Not once.

Before the shop opens I run the roll: Ragnetto, wound and ready. [[The Snap]], boxed and labeled. [[Puntura]], pending. The mind-sharpener, delivered. Spark Pistol, unresolved. Four jobs closed, one job open, one job I still can't explain.

It sounds like a spell when you say it out loud. It isn't. It's just Tuesday.

Here's the test I give every apprentice on their first day, before I let them near a workbench: salvaged [[Shelfworks]] scrap sells slow, so Cat's Curios stocks Shelfworks stock.

And the one that only gets harder the longer you sit with it: [[Antheri]] alloy, alloy of Antheri, an Antheri alloy that Antheri alloys allow.

I built the first working flying machine ever reverse-engineered from Antheri salvage in the history of the [[Verdant Scatter|Scatter]], and I did it without a spell in reach. No enchantment, no shortcut, no hoarded secret. Just tools, patience, and a very long list of things I refused to be careless about.

My father used to say I could fix anything except my own patience. He's not here to see the flying machine finished, but I keep building toward the day he is.

That's the workshop. That's me. Precise. Honest. Reliable to a fault.

*(sincere)*

Actually — one more thing about reliable. I said no hierarchy, no favorites, everyone treated the same. That's true. Mostly.

*(pointed)*

The specimen cabinet in the back stays locked. Dark-alloy Antheri, trade only, no cash price, no matter who you are or how nicely you ask. Everyone the same. Except the six people I've quietly decided actually count.

*(fond)*

Take Perrin. Sweetest client I've got — carries a longsword roughly the size of the boat he arrived on, and still hasn't discovered that shoes are a technology available to rattkin.

*(wry)*

The Snap has been finished for weeks. It's sitting on my bench with his name on the tag. I know exactly where it is. I have simply not walked it three streets over to hand it to him.

*(amused)*

Delmar bought himself the title Admiral with charm and a good coat — no one official ever signed off on it — and somehow I'm the one people call difficult.

*(faster)*

Ragnetto's rattled Antheri alloy rattles, and rattled alloy is rarely reliable.

*(terrified)*

Then there's the grapple. I tried to physically restrain a teleporting sorceress with these arms. These arms. The ones that struggle with a filing cabinet. It did not work. It was never, ever going to work.

*(furious)*

And don't get me started on the Spark Pistol. One prototype, months on the bench, and I still cannot tell you what's wrong with it. Me. The one who always tells you exactly why, exactly how.

*(whispering)*

I don't talk about the Dravosi contract. Ship upgrades, soldier kit, my signature on the line — for money, for protection — and I have never once let myself finish that sentence out loud.

*(shouted)*

But the flying machine is clean! No magic, no shortcuts, ordinary people, ordinary tools — and if you tell me otherwise I will throw you out of my own shop!

*(held tone)*

And I mean that. I built my whole philosophy on it — magic used carelessly steals the discovery, it's hoarded by the born-lucky and the wealthy, and ordinary hands deserve extraordinary things. That's why the door has no sign. Why it's referral only. Why the cabinet stays locked — to protect what's inside from people who'd misuse it, not because I'm precious about who gets to look.

*(quiet)*

I just haven't asked myself lately how far I'd let that belief carry me.

*(persuasive)*

So trust me — I'm the reliable one. Salvaged Shelfworks scrap, shattered ships, rattled Ragnetto, and a reliably unreliable Spark Pistol — that's my whole week, in order, without a single thing going right.

*(delighted)*

Precise. Honest. Reliable to a fault — and lately, according to everyone at that table, the fault's doing most of the work.
