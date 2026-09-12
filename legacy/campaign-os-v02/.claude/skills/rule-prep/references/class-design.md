# Class and Subclass Design Reference

Read this when `rule-prep`'s interview establishes `subtype: class` or
`subtype: subclass`. Mined from the legacy `dnd5e-homebrew` skill's
class and subclass design references, condensed into one file since a
subclass is designed against its base class's anatomy — the two are
rarely read independently. Assumes you've already run the shared
interview and stub check from `.claude/skills/rule-prep/SKILL.md`; this file covers only the
balance math and structural templates.

## Table of contents

1. [The Niche Test (full class only)](#the-niche-test-full-class-only)
2. [Class anatomy](#class-anatomy)
3. [Spellcasting classification](#spellcasting-classification)
4. [Feature distribution map (full class only)](#feature-distribution-map-full-class-only)
5. [Core resource design](#core-resource-design)
6. [20th-level capstone (full class only)](#20th-level-capstone-full-class-only)
7. [Subclass benchmarks by class](#subclass-benchmarks-by-class)
8. [Feature-level power budget](#feature-level-power-budget)
9. [Subclass structural patterns](#subclass-structural-patterns)

## The Niche Test (full class only)

A new base class must answer "yes" to all three before designing anything:

1. Does it have a fantasy not fully covered by an existing class?
2. Does it have a mechanical identity not covered by an existing class?
3. Can it support 3+ meaningfully different subclasses?

A "no" to any means the concept is a subclass, background, or feat wearing
a full class's clothing — route it there instead (`.claude/skills/rule-prep/SKILL.md` § Subtype
routing).

## Class anatomy

Every class needs these set before any feature is designed:

| Stat | Options |
|---|---|
| Hit Die | d6 (fragile casters) · d8 (medium) · d10 (martial) · d12 (rare, Rage-HP synergy only) |
| Armor | None · Light · Light+Medium · Light+Medium+Heavy+Shields |
| Weapons | Simple · Simple+Martial · specific weapons |
| Saving throws | Two abilities — one "mental," one "physical" is the common, safe pairing |
| Skills | 2–3 chosen from a list of 6–8 |

Avoid both-physical (STR+CON) saves for a fragile caster, or both-mental
(INT+WIS) for a pure tank — the pairing should reinforce the class's actual
survivability profile, not contradict it.

## Spellcasting classification

| Type | Examples | Slot progression |
|---|---|---|
| Full caster | Wizard, Cleric, Druid, Bard, Sorcerer | 9th-level spells by 17th; 1st-level spells at 1st |
| Half caster | Paladin, Ranger | 5th-level spells by 17th; 1st-level spells at 2nd |
| Third caster | Arcane Trickster, Eldritch Knight | 4th-level spells via subclass only |
| Pact Magic | Warlock | Short-rest recharge, always highest slot level |
| Non-caster | Barbarian, base Fighter, Monk | No spell slots — compensate with resource/action-economy power instead |

## Feature distribution map (full class only)

The standard level-by-level shape — deviate deliberately, not by accident:

| Level | Feature type | Level | Feature type |
|---|---|---|---|
| 1 | Two features (identity, immediately) | 11 | Major feature (power spike) |
| 2 | One feature | 12 | ASI/Feat |
| 3 | Subclass + one light class feature | 13 | Class feature (often minor) |
| 4 | ASI/Feat | 14 | Subclass feature (significant) |
| 5 | Big power spike (Extra Attack-tier) | 15 | Class feature (capstone-adjacent) |
| 6 | Subclass feature (minor–moderate) | 16 | ASI/Feat |
| 7 | Class feature (moderate) | 17 | Class feature (major) |
| 8 | ASI/Feat | 18 | Class feature (passive upgrade) |
| 9 | Class feature (passive/utility) | 19 | ASI/Feat |
| 10 | Subclass feature (moderate) | 20 | Capstone — must feel legendary |

Most classes get 5 ASI/Feat slots (4/8/12/16/19); Fighters get 7 (adds 6/14).
Give fewer ASIs to a class already strong in raw combat output, more to one
that needs flexibility to stay competitive.

**Extra Attack at 5th level** is the primary martial power spike — give it
to half-casters and full-martial classes at 5th, never to a full caster
(full casters compensate with 3rd-level spell access at the same level).

## Core resource design

| Resource | Example | Rest type | Scaling |
|---|---|---|---|
| Ki | Monk | Short rest | Uses = level |
| Superiority Dice | Battle Master | Short rest | 4 at 1st, up to 12 by 15th |
| Sorcery Points | Sorcerer | Long rest | Uses = level |
| Lay on Hands | Paladin | Long rest | Pool = 5 × level |
| Bardic Inspiration | Bard | Short/long | Uses = CHA modifier |
| Channel Divinity | Cleric | Short rest | 1 use, up to 3 by 18th |

Short-rest resources: smaller per use, more uses — suits an action-economy
class. Long-rest resources: larger per use, fewer uses — suits a
nova/burst class. A hybrid of both suits a versatile class.

## 20th-level capstone (full class only)

Must feel iconic, not "nice but not special" — four patterns:

1. **Raw stat surge** — +X to an ability score, breaking the normal cap.
2. **Free resource** — regains on short/long rest or a specific trigger.
3. **Ultimate transformation** — changed form, transcended mortality.
4. **Permanent passive** — a major always-on effect capping the fantasy.

## Subclass benchmarks by class

Read only the row for the class in play. "Watch out" is the load-bearing
column — it names the specific trap that class's own core kit sets for a
new subclass:

| Class (subclass level) | Core kit | Subclass controls | Watch out |
|---|---|---|---|
| Barbarian (3rd) | Rage, Reckless Attack | Extra rage effects, new action economy | Don't stack more damage on top of GWF+reckless |
| Bard (3rd) | Bardic Inspiration, Jack of All Trades | Spell list, Inspiration uses | Bonus spells shouldn't all be concentration |
| Cleric (1st) | Channel Divinity, Destroy Undead | Domain spells (always prepared), CD options | Always-prepared spells have real slot-cost value — don't undervalue |
| Druid (2nd) | Wild Shape | Wild Shape mods, circle spells | Buffing combat Wild Shape raises the power ceiling fast |
| Fighter (3rd) | Action Surge, Extra Attack | New resource or action economy | Fighters get the most ASIs — don't make the subclass ability-score-dependent |
| Monk (3rd) | Ki, Flurry of Blows, Stunning Strike | New ki spends, elemental damage | Monks are ki-starved — a feature costing more ki feels bad |
| Paladin (3rd) | Divine Smite, Aura of Protection (6th) | Oath spells, CD, aura upgrade | Aura of Protection is one of the strongest features in the game — don't compete with it |
| Ranger (3rd) | Favored Enemy/Tasha's replacements | Offense vs. pet vs. utility | Rangers are already action-economy-strained — don't add more per-turn actions |
| Rogue (3rd) | Sneak Attack, Cunning Action | Bonus proficiencies, new SA uses | Anything that lets SA trigger more often is already very strong |
| Sorcerer (1st) | Metamagic, Sorcery Points | Extra spells known, new metamagic | Sorcerers have the fewest spells known — bonus spells known are extremely valuable |
| Warlock (1st) | Eldritch Blast, Pact Magic, Invocations | Expanded spell list, patron features | Expanded spell lists are half the subclass's power — concentration spells matter most |
| Wizard (2nd) | Arcane Recovery | New school mastery, bonus spells | "Replace a roll" abilities (Portent-style) are uniquely powerful — scope carefully |

## Feature-level power budget

| Budget | Examples |
|---|---|
| 0.5 (ribbon) | A skill/language proficiency, resistance to a rare damage type |
| 1.0 (minor) | Advantage on specific checks, a minor damage rider, a 1/day utility spell |
| 1.5 (moderate) | Bonus-action attack once per turn, a minor aura, a resource expansion |
| 2.0 (major) | A new scaling resource, persistent conditional advantage |
| 2.5 (very strong) | Extra Attack-tier, at-will significant utility |
| 3.0 (capstone-tier) | Rage with flight, free-action resurrection, immunity to a common damage type |

By subclass level: 3rd (or 1st/2nd) sits at 2.0–2.5 — this is the defining
feature. 6th sits at 1.0–1.5. 10th sits at 1.5–2.0. 14th/capstone sits at
2.0–3.0.

## Subclass structural patterns

- **Combat** (Barbarian, Fighter, Paladin): 3rd = offensive nova or
  defensive passive + ribbon; 6th = defensive/utility; 10th =
  defense+offense combo; 14th = game-altering passive.
- **Support** (Cleric, Bard, Druid): 3rd = team buff or expanded toolkit;
  6th = personal defense + aura start; 10th = stronger aura or team spike;
  14th = powerful team/personal capstone.
- **Skill/utility** (Rogue, Ranger, Wizard): 3rd = new proficiencies +
  exploration/social trick; 6th = combat utility; 10th = expanded
  proficiency/expertise; 14th = strong passive or nova + unique trick.

## Full class checklist (in addition to `.claude/skills/rule-prep/SKILL.md`'s)

- [ ] Niche Test passed on all three questions.
- [ ] Hit die, saves, proficiencies set before any feature designed.
- [ ] Core resource has a stated rest type and scaling formula.
- [ ] Feature map covers every level 1–20, matching the distribution shape.
- [ ] Level 5 has a real power spike; level 20 capstone feels earned.
- [ ] Three subclass sketches (combat / support / hybrid) confirm the base
      class has room to breathe — none feels redundant with the base kit.
- [ ] No feature makes an existing class's core identity obsolete.
