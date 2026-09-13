---
title: Jean-Claude Tabarnack
category: entities
tags: [shattered-sea, npc]
sources:
  - "campaign-os:jean-claude-tabarnack-voice-script.md"
  - "campaign-os:jean-claude-tabarnack-stats.md"
  - "campaign-os:jean-claude-tabarnack-spells.md"
  - "campaign-os:jean-claude-tabarnack.md"
  - "campaign-os:jean-claude-tabarnack-inventory.md"
  - "campaign-os:jean-claude-tabarnack-gallery.md"
  - "campaign-os:jean-claude-tabarnack-combat-profile.md"
  - "campaign-os:jean-claude-tabarnack-sheet.md"
  - "campaign-os:jean-claude-tabarnack-abilities.md"
  - "wiki/_raw/Grung clans.md"
summary: Blue Grung from Botukuri whose red beret marks censure and whose sister Simone still hunts him.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-12"
tier: supporting
created: 2026-09-12T00:00:00Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[Grung clans]]"
    type: related_to
  - target: "[[Simone]]"
    type: related_to
  - target: "[[Botukuri]]"
    type: related_to
---
# Jean-Claude Tabarnack

Jean-Claude Tabarnack came from the [[Botukuri]] farming clan and carries blue social signals, while his red beret is read through the censure attached to Twiceborn status. His sister [[Simone]] still holds the Sorn garrison and hunts him.

## Connections

- [[Grung clans]]
- [[Simone]]
- [[Botukuri]]

## Abilities

# Jean-Claude Tabarnack — Abilities

Built from the player's character sheet. One section per action-economy
slot so a table runner can transclude exactly the one they need mid-round
(`![[Jean Claude Tabarnack Abilities]]`) — an ability that costs
an Action goes under Actions and is named, not repeated, anywhere else.

Everything [[Jean-Claude Tabarnack|Jean-Claude]] can do, sorted by what it
costs to do it. See [[Spells]] for the complete spell list; only the class feature that grants
the casting appears here.

## Traits

Species and background traits: always active at zero cost.

| Trait | Source | Effect |
|---|---|---|
| Mortis | Personal (unique to Jean-Claude) | Permanent disadvantage on Persuasion/Deception checks; advantage on Perception/Survival checks; cannot mask his intentions |
| Umbral Sight | [[Gloom Stalker]] (Ranger 3) | 60 ft. darkvision (+60 ft. range if he already has it); invisible to a creature relying on darkvision to see him while he is entirely in darkness or dim light (countered by magical light or [[Blindsight]]/[[Tremorsense]]) |
| Size | [[Grung]] | Small |
| Aquatic Nature | [[Grung]] | Breathes air and water; must submerge at least 1 hour per 24 or gain [[Exhaustion]] until immersed again |
| Standing Leap | [[Grung]] | Long jump 25 ft., high jump 15 ft., with or without a running start |
| Sticky Tongue | [[Grung]] | Snatches small unattended objects or makes a tongue attack in place of a regular attack |
| Poisonous Skin | [[Grung]] | Immune to poison damage and the poisoned condition; proficient with [[poisoner's kit]]; limited venom coating |

## Features

Class and subclass features that are not themselves an Action, Bonus
Action, or Reaction: passives, resource grants, and rest recoveries.

| Feature | Source | Effect | Uses | Recovery |
|---|---|---|---|---|
| Favored Enemy | [[Ranger]] 5 | [[Hunter's Mark]] always prepared, castable without expending a spell slot | 3/long rest | Long Rest |
| Fighting Style: [[Archery]] | Ranger 1 `[assumed]` | +2 to attack rolls with ranged weapons | passive | constant |
| Weapon Mastery | Ranger 1 `[srd]` | Mastery properties on 2 chosen proficient weapon types (which two is `[unknown]`, not stated on the sheet on file) | passive | constant |
| Extra Attack | Ranger 5 | Attacks twice instead of once when he takes the Attack action | passive | constant |
| Dread Ambusher: Ambusher's Leap | [[Gloom Stalker]] 3 | +10 ft. Speed until the end of his first turn in combat | 1/combat | Resets at the start of each combat |
| Dread Ambusher: dreadful strike | Gloom Stalker 3 | +2d6 psychic damage on a weapon hit, once per turn | 2/long rest (= WIS mod, min 1) | Long Rest |

## Actions

Attacks belong here, one row per distinct option, with the full stat line.

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
|---|---|---|---|---|
| +1 Silent Shortbow | +9 | 1d6+4 piercing, range 80/320 ft. | at-will | Archery fighting style bonus baked into the to-hit; bought at [[Casa Lupo]] in Session 04; no item page on file |
| [[Dagger]] | +6 | 1d4+3 piercing, reach 5 ft. | at-will | Fallback melee; Archery doesn't apply |

## Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
|---|---|---|---|---|
| Cast [[Hunter's Mark]] | Bonus Action | Marks a target; +1d6 force damage on hits against it while concentrating | 3/long rest without a slot (Favored Enemy), otherwise a 1st-level slot | Long Rest |

## Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
|---|---|---|---|---|
| [[Opportunity Attack]] | A creature he can see leaves his reach | One melee attack against it (Dagger only; the shortbow can't make an opportunity attack) | at-will | constant |

## Feats

At level 4, he chose [[Ability Score Improvement]] as a stat increase instead of a feat, already folded into the scores on
[[Stats]].

## Character sheet notes

No player sheet exists. This is a Ranger 5 (Gloom Stalker) built from official rules (DM updated 2026-07-22). Spells are DM-approved.

Labels: `[theoretical]` = derived, `[assumed]` or `[srd]` = sourced. **Replace this file when a real sheet arrives**.

## What lives here, and what does not

Character details live on separate pages:

| Topic | Page |
|---|---|
| Stats | [[Stats]] |
| Abilities | [[Abilities]] |
| Spells | [[Spells]] |
| Gear | [[Inventory]] |
| Profile | [[Jean-Claude Tabarnack|Main page]] |

This file holds only the source notes and the statblock below.

The Arc Note mentions "Level 5 Tongue Lash," but we cannot verify it. No Gloom Stalker or [[Grung]] feature matches it in the SRD or his [[Abilities]] page.

## Combatant Block

```statblock
# THEORETICAL BASELINE. No character sheet on file; full RAW Ranger 5
# (Gloom Stalker) kit checked this turn against
# vault/srd/classes/ranger.md and
# 5e-srd-ranger-gloom-stalker.md (not memory), plus DM-approved default
# spell picks. The +1 silent shortbow is session-sourced (session 04
# purchase). Replace wholesale when a real sheet lands.
layout: Basic 5e Layout
name: Jean-Claude Tabarnack
size: Small
type: humanoid
alignment: unaligned
ac: 16
hp: 44
speed: "25 ft., climb 25 ft."
stats: [10, 16, 14, 10, 14, 8]
saves: { str: 3, dex: 6 }
damage_immunities: "poison"
condition_immunities: "poisoned"
actions:
  - name: "+1 Silent Shortbow"
    # [assumed Archery] +2 fighting-style bonus baked in here only. Engine
    # flat_to_hit is global, and Archery is ranged-only (Dagger below is
    # unaffected). DEX+3, prof+3, +1 item, +2 Archery = +9.
    desc: "Ranged Weapon Attack: +9 to hit, range 80/320 ft., one target. Hit: 7 (1d6 + 4) piercing damage."
    sim: { id: silent-shortbow }
  - name: "Dagger"
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage."
    sim: { id: dagger }
sim:
  side: party
  level: 5
  initiative: 5 # [calculated] DEX +3 + WIS +2 (Gloom Stalker Initiative Bonus, 5e-srd-ranger-gloom-stalker.md)
  resources:
    - { id: ranger_slot_1, max: 4, recharge: long_rest } # [srd] 5e-srd-ranger.md level-5 table
    - { id: ranger_slot_2, max: 2, recharge: long_rest } # [srd] 5e-srd-ranger.md level-5 table
    - { id: dread_ambusher_uses, max: 2, recharge: long_rest } # [srd] = WIS mod (min 1), 5e-srd-ranger-gloom-stalker.md
  abilities:
    # [srd 5e-srd-ranger.md] Level 5: Extra Attack. Standing feature, no rounds key
    - { kind: extra_attack_count, value: 1 }
    # [srd 5e-srd-ranger-gloom-stalker.md] Level 3: Dread Ambusher. Dreadful
    # Strike. Not round-gated (corrects the prior compile's "+1d8, round 1
    # only" guess). A resource-limited on-hit rider, once per turn.
    - { kind: extra_damage, id: dreadful-strike, dice: 2d6, type: psychic, when: on_hit,
        once_per_turn: true, cost: { resource: dread_ambusher_uses, spend: 1 } }
  spellcasting:
    # DC/attack_bonus/ability_mod all derive from WIS mod +2 (8+3+2=13 DC;
    # 3+2=5 attack). Dice come from each spell's own SRD page [srd]; the
    # picks are DM-approved defaults [assumed]. Favored Enemy's 3 free
    # Hunter's Mark casts/long rest aren't modeled. Every cast here costs
    # a 1st-level slot instead (see [[Spells]]).
    - { ability: wis, dc: 13, attack_bonus: 5, level: 5, ability_mod: 2,
        slots: { 1: ranger_slot_1, 2: ranger_slot_2 },
        known: ["Hunter's Mark", "Cure Wounds", "Magic Weapon"] }
  routine:
    action: [silent-shortbow]
```

**Not modeled in the sim:**
Ambusher's Leap speed boost, Umbral Sight, Weapon Mastery, Toxic Secretion, Mortis, Favored Enemy free casts, [[Ensnaring Strike]], [[Longstrider]], [[Pass without Trace]], [[Spike Growth]] (see [[Spells]] for DM-approved picks).

## Combat profile

**FIDELITY WARNING:** this profile relies on a theoretical Ranger 5 sheet — no character-sheet PDF exists yet. Every `[simulated]` number is real script output over `[theoretical]` inputs; the inputs, not the math, are the weak link.

> [!dm]
> Built on `jean-claude-tabarnack-sheet.md`, Ranger 5, full RAW kit (Extra Attack, Dreadful Strike, [[Initiative]] Bonus, [[Hunter's Mark]]/[[Cure Wounds]]/[[Magic Weapon]]).

## Fast Read

Ranged ambush striker, darkness scout (Gloom Stalker) · sustained DPR 14.97 vs AC 15 `[simulated]` · nova (p95) 26.0 vs AC 15 `[simulated]` · effective HP 44 `[assumed]`, survives ~6–7 attacks at +7 to-hit/10 dmg, poison-immune · Achilles heel: concentration — his single point of failure. Worst-3 matchups ([[Aboleth]], Adult Black Dragon, Adult Blue Dragon) break it 0.994/0.526/0.572 times per run `[simulated]`; damage drops to bare bow once broken.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 15 / 44 | `[assumed]` |
| Init / Speed | climb + Standing Leap; Umbral Sight (darkvision-invisible in darkness, unmodeled) | `[sheet]` |
| Hit% vs AC ladder | Shortbow +9 (incl. crit): 75.0% vs AC 15, 65.0% vs AC 17. Incoming: +2 40.0% / +5 55.0% / +7 65.0% / +9 75.0% / +12 90.0% | `[simulated]` |
| Save bonuses (weak → strong) | CHA -1, INT +0, WIS +2, CON +2, STR +3, DEX +6 | `[sheet]` |
| Resource pools (per rest) | 1st-level slots ×4, 2nd-level slots ×2, Dreadful Strike ×2 (= WIS mod, min 1) | `[srd]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/jean-claude-tabarnack-sheet.md --seed 1`

Damage/round (shortbow +9, optimal auto-policy): mean 14.97/13.26 at AC 15/17, p50 17.0/16.0, p95 26.0/26.0 `[simulated]`. Extra Attack, Dreadful Strike, and Hunter's Mark follow RAW `[srd]`. Expected attacks survived at +7: 13.0 (5 dmg) / 6.5 (10 dmg) / 4.3 (15 dmg) / 3.3 (20 dmg) `[simulated]`. Immune: poison damage, poisoned condition `[pcs-page, grung]` — every [[Grung]] poison rider and Otar's Foul Miasma are zero against him.

Not modeled: Ambusher's Leap's +10 ft [[Speed]] round-1 boost (no round-gated movement primitive), Umbral Sight (no light-state/darkvision primitive), Weapon Mastery (no weapon-mastery primitive), Toxic Secretion and Mortis (passive, no combat math), Favored [[Enemy]]'s free Hunter's Mark casts (sim costs every cast from the slot pool), [[Ensnaring Strike]]/[[Longstrider]]/[[Pass without Trace]]/[[Spike Growth]] (unfenced picks), Magic Weapon's +1/+2/+3 upcast damage bonus (no combined to-hit-plus-damage or upcast-scaling primitive; typically cast on an ally's weapon but modifiers compile onto the caster only). Arc Note's "Tongue Lash" has no confirmed SRD match. The level-5 2nd-level spell prepared (if any) is unknown.

## Counters & Synergy

Hard counters: bright light and open ground strip his ambush advantage; [[Aboleth]], [[Adult Black Dragon]], [[Adult Blue Dragon]] — near-0% win, dies fast `[simulated]`. Soft counters: sustained damage and tremorsense break his concentration; [[doppelgänger]] 50.4%, [[Ogre Zombie]] 51.6%, [[Pirate Captain]] 52.1%, [[weretiger]] 53.6%, [[Black Pudding]] 55.0% `[simulated]`. No answer for: flying enemies out of reach, dragons, social combat.

Amplifies: any darkness (advantage engine works alone). Depends on: dim light/darkness for peak output, allies on the front line (mid-tier AC/HP). Observed: ceiling scout then ambush attack, the party's surprise opener.

## Session Combat Log

| Session | Encounter | Rounds | Dmg dealt | Dmg taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 04 | Sewer patrol Grung (ambush from ceiling) | 1 | ~24 | 0 | `[unknown]` | Dread Strike instant kill on patrol Grung |
| 04 | Powder-ship demolition | 1 | n/a (mission goal) | 0 | 1/1 | Fire arrow into 8 barrels, ship destroyed |
| 06 | Primary Chamber fight ([[Ozzeth]]) | `[unknown]` | 13 (bow, finishing shot) | 0 noted | 1/1 (17 to hit) | Re-cast Hunter's Mark on Ozzeth, finished him with a 17-to-hit bow shot for 13 piercing/force after Delmar shot his arm off. His Bardic-Inspiration-boosted save (nat 19+inspiration=20) resisted Ozzeth's [[Dominate Person]] on Delmar. Leveled up to Ranger 5 |

## Calibration

Simulated-vs-observed delta: sim's steady ~7.5-vs-current-14.97 DPR vs observed 24-damage round-1 ambush spike (S04) and confirmed 13-damage finishing shot (S06) — Dread Ambusher plus surprise is his real shape; sustained lane undercounts the opener, overcounts staying power. Design implication: performs at max only in darkness with an unbroken Mark; strip that away to pressure him. Confidence: `theoretical` across the board until a real sheet lands; session-04/06 narrative evidence `[low]`. Unsimulable: whatever "Tongue Lash" his Arc Note names (unconfirmed), actual spells prepared, real ability scores.

## Gallery

# Jean-Claude Tabarnack Gallery

Visual reference for [[Jean-Claude Tabarnack]].

## Portraits

![[jean-claude-tabarnack-banner|Jean-Claude Tabarnack banner]]
![[jean-claude-tabarnack-portrait|Jean-Claude Tabarnack portrait]]

## Inventory

# Jean-Claude Tabarnack — Inventory

What [[Jean-Claude Tabarnack|Jean-Claude]] carries, and where the rest of
his gear stays.

## Attuned Magic Items

| Item | Attuned? | Effect in play |
|---|---|---|
| [[Cloak of Elvenkind]] | Yes | Disadvantage on Perception checks to perceive him; advantage on Stealth checks |
| [[Stormwork Quiver]] | Yes | Each arrow fired deals +1d6 lightning damage on a hit |

## Carried Gear

| Item | Qty | Why it matters |
|---|---|---|
| +1 Silent Shortbow | 1 | Primary ranged weapon, bought at [[Casa Lupo]] (Session 04); [[Archery]] fighting style bonus baked into its attack line on [[Abilities]] |
| [[Dagger]] | 1 | Melee fallback and his only opportunity-attack option |
| [[Bracers of Archery]] | 1 | Bought from [[Lavinia Sordi]] at [[La Cenere]] for 100 gold, Session 08. Minor curse: a natural 1 while worn turns him flamingo pink for an hour |
| [[Eyes of the Eagle]] | 1 | Advantage on sight-based Perception checks; reads fine detail at extreme range |
| [[Cloak of Elvenkind]] | 1 | Attunement required; see Attuned Magic Items above |
| [[Stormwork Quiver]] | 1 | Holds 20 arrows; attunement required; see Attuned Magic Items above |

## Stowed & Cached

Twenty vials of [[Simone]]'s tincture, hidden in the
[[Uncertainty|HCS Surety]]'s cargo since Session 02. He has told none of
the crew. He would need a reason serious enough to reveal
Simone's involvement before retrieving or using them openly.

## Currency

| Coin | Amount |
|---|---|
| — | Not stated in the sheet on file |

## Spells

# Jean-Claude Tabarnack — Spells

[[Jean-Claude Tabarnack|Jean-Claude]]'s spell list. Ranger is a half-caster;
these values are `[calculated]`/`[assumed]` from the RAW-baseline sheet
(`vault/campaigns/shattered-sea/pcs/character-sheets/jean-claude-tabarnack-sheet.md`), not from a
player-submitted sheet.

## Spellcasting

| Class | Ability | Save DC | Attack Bonus | Prepared / Known |
|---|---|---|---|---|
| [[Ranger]] | [[Wisdom]] | 13 | +5 | Known (Rangers know a fixed list, not selecting from the whole class list) |

## Cantrips

| Cantrip | Class | Effect at this level |
|---|---|---|

Rangers have no cantrips.

## Known & Prepared

| Level | Spell | Class | Key effect |
|---|---|---|---|
| 1st | [[Hunter's Mark]] | Ranger | Marks a target. +1d6 force damage on hits against it (Favored Enemy grants 3 free casts/long rest; see [[Abilities]]) |
| 1st | [[Cure Wounds]] | Ranger | Heals a touched creature |
| 1st | [[Ensnaring Strike]] | Ranger | Restrains a struck creature in grasping vines |
| 1st | [[Longstrider]] | Ranger | +10 ft. Speed for the duration |
| 2nd | [[Magic Weapon]] | Ranger | +1 to attack and damage rolls on a nonmagical weapon he touches |
| 2nd | [[Pass without Trace]] | Ranger | +10 to Stealth checks and no trackable trail for allies within 30 ft. |
| 2nd | [[Spike Growth]] | Ranger | Turns an area into difficult terrain that damages creatures moving through it |

DM-approved default prepared-spell picks `[assumed]`. No player-submitted
sheet exists to confirm the actual picks against.

## Slots & Pools

| Pool | Slots by level | Recovery |
|---|---|---|
| Ranger spell slots | 1st: 4, 2nd: 2 | Long Rest |
| Favored Enemy free casts (Hunter's Mark only) | 3/long rest, no slot spent | Long Rest |

## Stats

# Jean-Claude Tabarnack — Attributes

Mechanical attributes for [[Jean-Claude Tabarnack]],
transcribed from
`vault/campaigns/shattered-sea/pcs/character-sheets/jean-claude-tabarnack-sheet.md`
(a RAW-baseline derivation, not a player-submitted sheet: no PDF exists for
this PC). Every value below carries a `[theoretical]`/`[assumed]` tag
unless marked otherwise; a sheet error stays as printed and gets a
`[verify]` tag instead of a silent fix. This page is the single source of
truth for every per-ability, per-skill, and per-speed value; `ac`,
`hp_max`, `class_levels`, and `level` stay in
[[Jean-Claude Tabarnack]]'s frontmatter and are never restated here.

Small size, amphibious (breathes air and water), and a climb speed equal to
his walking speed are [[Grung]] species traits (see Combat Stats
below and [[Abilities]] for the rest of the
species kit).

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| [[Strength]] | 10 | +0 | +3 | yes |
| [[Dexterity]] | 16 | +3 | +6 | yes |
| [[Constitution]] | 14 | +2 | +2 | no |
| [[Intelligence]] | 10 | +0 | +0 | no |
| [[Wisdom]] | 14 | +2 | +2 | no |
| [[Charisma]] | 8 | -1 | -1 | no |

`[theoretical]`, unchanged from the level-4 baseline. No Ability Score
Improvement is due at Ranger 5 (the level-4 ASI is already folded into
these scores). Save proficiencies are the Ranger class defaults
(Strength, Dexterity). Proficiency bonus **+3** at level 5.

## Skills

The sheet on file states no skill proficiency list beyond the ability
scores and saves above. Passive Perception, Insight, and Investigation:
`[unknown]` (no proficiency data to calculate from). Mortis grants
advantage on Perception and Survival checks instead of a skill
proficiency (see [[Abilities]]).

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative | +5 | `[calculated]` DEX +3, plus WIS +2 from Gloom Stalker's Initiative Bonus ([[Gloom Stalker]] level 3) |
| Speed | 25 ft. walking, 25 ft. climbing | `[pcs-page, grung]` climb speed equal to walking speed, a [[Grung]] species trait |
| Hit dice | 5d10 | `[srd]` Ranger hit die |
| Proficiency bonus | +3 | `[assumed]` |
| Damage resistances | none stated. Immune to poison damage (species trait, see [[Abilities]]) | `[pcs-page, grung]` |
| Condition advantages | immune to the poisoned condition (species trait, see [[Abilities]]) | `[pcs-page, grung]` |

AC and max HP live in [[Jean-Claude Tabarnack]]'s frontmatter (`ac:`,
`hp_max:`) — the roster `.base` views query them there; this table carries
no rows for them.

## Proficiencies & Languages

Armour and weapon proficiencies beyond the studded leather, shortbow, and
dagger used in his attack routine are not stated in the sheet on file.
Species-granted proficiencies ([[Poisoner's Kit]]) live on
[[Abilities]].

## Voice

*(Try to stay as in character from now on, its okay if you lose character just stop, breathe, and continue. Capturing how you, and/or your character, naturally speak is the point.)*

I am reading for [[Jean-Claude Tabarnack]]

Jean-Claude Tabarnack. Ranger. Scout. The one who watches from the dark so the rest of you don't have to.

Three companions signed on with me. [[Perrin Black-Jaw|Perrin]], Delmar, Crissdalynn. Three names, three debts, three reasons I keep moving forward instead of back.

I count supplies before I count sleep. Boots, bowstrings, salt, bandages, bread. If it keeps us breathing, I know exactly how much of it is left in the hold.

[[Sorn]] to [[Le Paludi]], Le Paludi to the [[Central Strait]] — I have walked routes with names that trip up sailors twice my size, and I say every one of them clean.

Six slick scouts scale a sheer, slippery cliffside before the tide turns — that's the report I filed after [[Kalowe]], word for word.

Botukuri blue-blood, Boh-too-koo-ree by name, born beneath black bands. Small body. Long memory.

[[Pell]] taught me that a good plan survives contact with people who love you. I am still learning what that means.

I am, if nothing else, honest. Painfully, permanently honest.

*(sincere)*

I do not lie. I have never once told a lie in my life.

*(calm)*

I also cannot recall the last time I told anyone everything.

*(commanding)*

Hold the line. Watch the water. Nobody moves until I say.

*(fond)*

Perrin once fell off the rigging on a flat roll of one. I fell right behind him. Difference is, I meant to jump.

*(wry)*

I paid good coin for boots that let a man fly, and Delmar's the one wearing them, because apparently owning feet was a requirement I forgot to check.

*(warm)*

Crissdalynn caught both of us out of the sky that day. I have a complicated relationship with anything that has wings, and exactly one standing exception.

*(delighted)*

I sold three shark eggs for three hundred gold and bought a bow that never makes a sound.

*(sarcastically)*

I called him no threat. He introduced himself with a dagger through my shirt. He was some threat.

*(badly persuasive)*

Trust me. No — truly. Trust me.

*(quietly amused)*

I once poured a dying man a glass of my own blood and called it comfort. He stopped shaking. I've never asked why that worked.

*(terrified)*

Birds. Just — birds. I don't discuss it further.

*(whispering)*

I still hear the screams that covered my exit. I have never said that at full volume before tonight.

*(earnest)*

This disguise works. A red beret. A false moustache. That is the entire operation. [[Grung]] don't tell each other apart by the face, we do it by ornament, and every humanoid I've ever met is so busy staring at a strip of black horsehair glued above my mouth that not one of them has looked twice at the scars, the caste bands, the eyes underneath it. It is the single most elegant piece of tradecraft I have ever executed and I will not hear otherwise. My own family could walk past me in daylight. That is not luck. That is craft.

*(shouting)*

SLAVERS DO NOT GET TO FINISH THEIR SENTENCE IN MY PRESENCE.

*(held tone)*

I. [[Wish]]. You. Could. See. The error. Of your ways.

*(faster)*

Sorn to Le Paludi, Le Paludi to the Central Strait, Central Strait back to Sorn — say that with a blade at your throat and a Botukuri patrol on your tail.

*(sly)*

Ask me what's in my cargo hold. Go on. I'll tell you everything except the twenty bottles I never mention, because apparently "honest" has an asterisk I invented myself.

*(grinning)*

Jumpy Don't Touch, Sticky Tongue Death Skin, Hopstradamus — three names I've been called to my face, and not one of them wrong.

*(satisfied)*

Jean-Claude Tabarnack. Ranger. Scout. The one who watches from the dark — and somehow still the only liar in this crew who's never told a single lie. Four out of five stars. Trust me with your life. Just not with your secrets.
