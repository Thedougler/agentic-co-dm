---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Monster design philosophy (Four Laws), role archetypes, ability tiers, CR math with dndsim validation, boss/elite suites, telegraphing, and final review checklist."
created: "2026-08-03"
updated: "2026-08-10"
tags: [combat]
uid: 227f2c97-f5ab-434e-8a24-0b30f3550237
---

# CR math and monster design method

Load when designing a homebrew creature or monster from scratch, or when
verifying a published/reskinned creature's CR against the party's level.
Also the math source for a named recurring villain statted as a monster
rather than a class-leveled humanoid (legendary actions, a full
traits/actions suite, a CR number) — `vault/refs/vault/npc/references/villains.md`
§ Stat block approach routes here for exactly that case, rather than
re-deriving CR math of its own (DRY). A villain built on effective class
level instead doesn't need this file.

The CR/DPR benchmark tables, HP/ability-score lookups, and creature-type/
condition references live on
`vault/refs/vault/monster/references/cr-tables.md`
— read that page for the actual numbers; this page covers the design
method.

---

## 1. The Four Laws (design philosophy, keep before any math)

1. **One signature moment.** One thing no other monster does — what
   players describe after the session.
2. **Mechanics tell the story.** Every ability must be deducible from its
   flavor in one sentence. Can't? Cut it.
3. **Players are protagonists.** Design monsters that react to player
   choices, not the reverse.
4. **Complexity in decisions, not procedures.** Simple to run, rich to
   fight — the DM shouldn't need a lookup table mid-round.

## 2. Roles and stat priority

Justification: shorthand that turns "make a monster" into a five-second
archetype pick instead of a blank page.

| Role | Priority stats | Notes |
|---|---|---|
| Solo boss | STR + CON primary | Legendary actions, lair actions, multi-phase |
| Elite | High single-round damage | Crowd control, 1 legendary action set |
| Standard | Efficient multiattack | One interesting ability, clear weakness |
| Minion | Low HP, pack tactics | Single attack |
| Skirmisher | High speed, medium stats | Bonus-action mobility |
| Controller | INT or WIS 18+ | Save DC is the weapon; lower AC acceptable |
| Brute | STR 20+, CON 18+ | Low DEX/INT; advantage-on-damage or high single hits |
| Lurker | DEX 18+, low STR | Surprise/stealth/conditions as primary threat |
| Artillery | High DPR at range, lower HP | Needs a repositioning ability or dies round 1 |
| Defender | High AC/saves/HP; lower damage | "Sticky" — punishes attacking anyone else it's engaged |
| Leader | Buffs/heals/moves allies; lower own DPR | Boosts other creatures instead of attacking |

Assign 2–3 saves max, matched to creature type (aberration → INT/WIS;
celestial/fiend → WIS/CHA; construct → CON; dragon → DEX/CON/WIS; undead →
WIS). Skills: only what the creature actually uses at the table.

Where to position a role in a fight and how it behaves once combat
starts is an *encounter* decision, not a per-creature one — see
`.claude/skills/encounter-prep/references/running-the-encounter.md`
§ Role placement and tactics.

## 3. Ability hierarchy — build in this order, stop when it's enough

1. **Tier 1 — core identity.** Multiattack (CR 2+) plus the signature
   ability (one recharge/limited/save-or-suffer effect).
2. **Tier 2 — combat texture (1–2).** A passive trait, reaction, or bonus
   action that changes fight dynamics. § 3a below is a ready-made toolkit
   for this tier — start there before inventing a mechanic from scratch.
3. **Tier 3 — flavor (0–1).** Minor mechanical weight only; skip if Tiers
   1–2 aren't solid yet.

Max 3 unique named abilities on a non-boss. Never save-or-die without a
repeat save and damage on a success.

### 3a. Ten reusable monster features (Tier 2 starting toolkit)

Justification: turns "invent a passive trait" into "pick one, scale the
numbers" — plug-and-play options condensed from
`vault/refs/vault/monster/references/lazy-tricks-for-running-monsters.md`.
Scale each against `vault/refs/vault/monster/references/cr-tables.md`
§ 1 and § 4's DPR-by-CR numbers, not that source's own quick-math
formulas.

- **Damaging Blast** — a single-target ranged attack using the creature's
  own attack bonus/damage, typed to its story.
- **Damage Reflection** — a melee attacker within 5 ft. who hits this
  creature takes half of one of its attacks' damage in return; give the
  creature one fewer attack to compensate.
- **[[misty-step|Misty Step]]** — bonus action, teleport up to 30 ft. to an unoccupied
  seen space.
- **Knockdown** — on a melee hit, target fails a STR save or falls [[prone|prone]].
- **Restraining Grab** — on a melee hit, target is [[grappled|grappled]] (escape DC
  from the creature's STR/DEX mod); while grappled, also [[restrained|restrained]].
- **Damaging Burst** — action, 10-ft.-radius sphere (self or a point
  within 120 ft.); DEX/CON/WIS save or take half this creature's DPR
  (half again on a success).
- **Cunning Action** — bonus action Dash, Disengage, or Hide.
- **Damaging Aura** — anyone starting their turn within 10 ft. takes half
  of one attack's damage; give the creature one fewer attack to
  compensate.
- **Energy Weapons** — weapon attacks deal extra typed damage, added on
  top for a boost or swapped in to replace some physical damage.
- **Damage Transference** — the creature can shunt half or all damage it
  takes onto a willing creature within 30–60 ft.; strong on a boss with an
  expendable ally nearby (pairs with § 5 Solo boss suite).

**Anti-patterns:** more than 3 unique abilities on a non-boss; "once per
day" abilities unlikely to fire in one combat; abilities with no player
counterplay; save-or-die with no repeat save; 3+ simultaneous conditions to
track.

## 4. CR calculation

1. **Defensive CR** — look up effective HP in
   `vault/refs/vault/monster/references/cr-tables.md` § 1; adjust HP first
   using that page's § 6 resistance/immunity multipliers.
2. **Offensive CR** — average damage per round across 3 rounds (÷3 for a
   recharge 5–6 ability, ÷2 for recharge 4–6).
3. **Final CR** = average of defensive and offensive CR.
4. **Adjust:** +1 per 3 legendary actions; +1 for lair actions.
5. **Validate against the actual party** (recommended above CR 2): run the
   `npm run dndsim -- sim-combat` encounter simulation — party sheets vs this
   creature's statblock page (see `utils/dndsim/CLAUDE.md` for CLI usage; loadout
   judgment:
   `.claude/skills/combat-profiles/references/simulation.md`).
   The report's Effective CR scalar should land within ±1 CR of the table
   CR from `vault/refs/vault/monster/references/cr-tables.md` § 1 — a
   bigger gap means revise the stats, or keep them and record the
   divergence (with seed) on the creature page's design notes.

## 5. Solo boss / elite suite

- **Legendary actions (3):** one fast/reactive + one pressure (terrain,
  minion, reveal) + one 2-cost powerful option.
- **Lair actions (3):** one environmental + one repositioning + one
  dramatic.
- **Legendary resistance (3/day):** include on any boss that a single
  failed save would trivially end.
- **Multi-phase (max 2, 3 for a campaign climax):** trigger at 50% HP.
  Phase 2 must feel different — a new threat vector, not just bigger
  numbers. Transition template: *"When [Name] is reduced to [X] HP for the
  first time, [dramatic description]. [Name]'s statistics change as
  follows: [what changes]. Initiative order is not interrupted."*

Matching a boss to a plausible environment and minion type is an
encounter-composition decision — see
`.claude/skills/encounter-prep/references/encounter-composition.md`
§ Boss/environment/minion pairing.

## 6. Telegraphing (include at least one)

- **Environmental** — tracks, smells, damage, remnants; something
  physically wrong with the space.
- **Social** — an NPC reacts: goes quiet, refuses to go further, laughs
  wrong.
- **Mechanical preview** — a previous victim showing the signature
  ability's effect, or a distant glimpse.

Picking this creature's behavior pattern for a given fight (apex
predator, pack hunter, territorial, cunning, relentless, protective,
chaotic) is an encounter-instance decision, not a property of the
reusable creature kind — see
`.claude/skills/encounter-prep/references/running-the-encounter.md`
§ Tactical personality. For a party of 5th level or higher specifically,
also read `vault/refs/vault/monster/references/lightning-rods.md`
before finalizing tactics — it reframes "how hard should this creature
counter the party" into "what should it let them show off."

## 7. Final check before presenting a monster

- [ ] Signature moment describable in one sentence
- [ ] Every mechanic deducible from the flavor
- [ ] Ability count in bounds (non-boss ≤3, boss ≤5 plus legendary suite)
- [ ] At least one telegraph layer present
- [ ] CR validated (defensive + offensive averaged)
- [ ] No anti-pattern from § 3a present

If more than two are missing, revise before shipping.

## 8. Tuning mid-fight

Encounter-level tuning (HP/damage dials, running hordes, party-level calibration) belongs to
`.claude/skills/encounter-prep/` — the creature-design tools above still apply underneath.
