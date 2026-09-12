---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "CR benchmark and lookup tables — CR/XP/DPR, HP formula, ability modifiers, damage expressions, creature-type conventions, and condition reference."
created: "2026-08-03"
updated: "2026-08-03"
tags: [combat]
uid: 489c7f06-cb8e-478c-9ee8-e426cd6a0cde
---

# CR benchmark and lookup tables

The numeric companion to
["CR math and monster design method"](vault/refs/vault/monster/references/cr-design.md) —
read that page for the design method (Four Laws, roles, ability hierarchy,
CR calculation steps, solo boss suite); read this page for the actual
numbers those steps look up.

---

## 1. Monster statistics by Challenge Rating

Justification: the single canonical CR↔stats mapping in this repo; without
it, "what HP/AC/DPR fits CR 6" has no answer except guessing.

Combat math (AC/HP/attack/DPR) and rewards/DC (Prof/Save DC/XP) are split
into two tables, both keyed on CR — read the first when statting combat
numbers, the second when setting proficiency, save DC, or XP award.

| CR | AC | HP (Low–High) | Attack | DPR (Low–High) |
|----|----|----|----|-----|
| 0 | ≤13 | 1–6 | +3 | 0–1 |
| 1/8 | 13 | 7–35 | +3 | 2–3 |
| 1/4 | 13 | 36–49 | +3 | 4–5 |
| 1/2 | 13 | 50–70 | +3 | 6–8 |
| 1 | 13 | 71–85 | +3 | 9–14 |
| 2 | 13 | 86–100 | +3 | 15–20 |
| 3 | 13 | 101–115 | +4 | 21–26 |
| 4 | 14 | 116–130 | +5 | 27–32 |
| 5 | 15 | 131–145 | +6 | 33–38 |
| 6 | 15 | 146–160 | +6 | 39–44 |
| 7 | 15 | 161–175 | +6 | 45–50 |
| 8 | 16 | 176–190 | +7 | 51–56 |
| 9 | 16 | 191–205 | +7 | 57–62 |
| 10 | 17 | 206–220 | +7 | 63–68 |
| 11 | 17 | 221–235 | +8 | 69–74 |
| 12 | 17 | 236–250 | +8 | 75–80 |
| 13 | 18 | 251–265 | +8 | 81–86 |
| 14 | 18 | 266–280 | +8 | 87–92 |
| 15 | 18 | 281–295 | +8 | 93–98 |
| 16 | 18 | 296–310 | +9 | 99–104 |
| 17 | 19 | 311–325 | +10 | 105–110 |
| 18 | 19 | 326–340 | +10 | 111–116 |
| 19 | 19 | 341–355 | +10 | 117–122 |
| 20 | 19 | 356–400 | +10 | 123–140 |

| CR | Prof | Save DC | XP |
|----|------|---------|-----|
| 0 | +2 | 13 | 0–10 |
| 1/8 | +2 | 13 | 25 |
| 1/4 | +2 | 13 | 50 |
| 1/2 | +2 | 13 | 100 |
| 1 | +2 | 13 | 200 |
| 2 | +2 | 13 | 450 |
| 3 | +2 | 13 | 700 |
| 4 | +2 | 14 | 1,100 |
| 5 | +3 | 15 | 1,800 |
| 6 | +3 | 15 | 2,300 |
| 7 | +3 | 15 | 2,900 |
| 8 | +3 | 16 | 3,900 |
| 9 | +4 | 16 | 5,000 |
| 10 | +4 | 16 | 5,900 |
| 11 | +4 | 17 | 7,200 |
| 12 | +4 | 17 | 8,400 |
| 13 | +5 | 18 | 10,000 |
| 14 | +5 | 18 | 11,500 |
| 15 | +5 | 18 | 13,000 |
| 16 | +5 | 18 | 15,000 |
| 17 | +6 | 19 | 18,000 |
| 18 | +6 | 19 | 20,000 |
| 19 | +6 | 19 | 22,000 |
| 20 | +6 | 19 | 25,000 |

(CR 21–30 exists for epic/mythic play; omitted here as out of range for
most tables — extend by the same progression if a campaign needs it.)

## 2. HP formula and hit die by size

Justification: needed to build the `hit_dice:` statblock field so it
matches the `hp:` field instead of contradicting it.

`HP = (number of dice × average per die) + (number of dice × CON modifier)`

| Size | Hit die | Avg/die |
|---|---|---|
| Tiny | d4 | 2.5 |
| Small | d6 | 3.5 |
| Medium | d8 | 4.5 |
| Large | d10 | 5.5 |
| Huge | d12 | 6.5 |
| Gargantuan | d20 | 10.5 |

Example: 15d10 + 45 (CON +3) = 15×5.5 + 15×3 = 82.5 + 45 = **127 HP**.

## 3. Ability score to modifier

Justification: the one lookup every stat block and every save DC depends
on; keeping it here avoids a mid-design context switch to an external
source.

| Score | Mod | Score | Mod |
|---|---|---|---|
| 1 | −5 | 16–17 | +3 |
| 2–3 | −4 | 18–19 | +4 |
| 4–5 | −3 | 20–21 | +5 |
| 6–7 | −2 | 22–23 | +6 |
| 8–9 | −1 | 24–25 | +7 |
| 10–11 | 0 | 26–27 | +8 |
| 12–13 | +1 | 28–29 | +9 |
| 14–15 | +2 | 30 | +10 |

## 4. Standard damage expressions and multiattack by CR

Justification: turns "what should the DPR line say" into a lookup instead
of a fresh calculation every time.

| CR | 1-attack DPR | 2-attack, each | 3-attack, each |
|----|---------------|--------------------|-----------------------|
| 1/4 | 5 | — | — |
| 1/2 | 8 | — | — |
| 1 | 14 | 7 | — |
| 2 | 20 | 10 | — |
| 3 | 26 | 13 | — |
| 4 | 32 | 16 | — |
| 5 | 38 | 19 | — |
| 6 | 44 | 22 | 15 |
| 8 | 56 | 28 | 19 |
| 10 | 68 | 34 | 23 |
| 12 | 80 | 40 | 27 |
| 15 | 98 | 49 | 33 |
| 20 | 132 | 66 | 44 |

Multiattack conventions: CR 1–2 mostly single attack or ×2; CR 3–6
standard ×2; CR 7–10 ×2–3; CR 11–15 ×3 plus a special action; CR 16–20 ×3–4
with legendary actions supplementing.

## 5. Creature type conventions

Justification: keeps saves/resistances narratively coherent by type
without re-deriving them from genre convention each time.

| Type | Common stats | Typical saves | Common resist/immune |
|---|---|---|---|
| Aberration | High INT or WIS | INT, WIS | Psychic resistance common |
| Beast | STR or DEX | CON | Usually none |
| Celestial | CHA, WIS, STR | WIS, CHA | Radiant resist; poison immune |
| Construct | STR, CON; low INT | CON | Poison/exhaustion/psychic immune |
| Dragon | STR, CON, CHA | DEX, CON, WIS | Elemental immunity matching breath |
| Elemental | Matching element | STR or CON | Matching elemental immunity |
| Fey | CHA, DEX | CHA, WIS | Often charmed-prone |
| Fiend | STR, CHA | CON, CHA | Fire/poison resist; poison immune |
| Giant | STR, CON | CON | Often none |
| Humanoid | Varies by class | Varies | Rarely any |
| Monstrosity | STR, CON | CON | Varies |
| Ooze | STR, CON; low mental | CON | Acid; exhaustion/prone immune |
| Plant | CON | CON | Poison; often blinded/deafened immune |
| Undead | STR or DEX; low CON | WIS | Poison; exhaustion/poison immune |

## 6. Effective HP adjustment for resistance/[immunity](vault/srd/rules/immunity.md)

Justification: the defensive-CR step above depends on this multiplier —
skipping it makes every resistant/immune creature under-CR'd.

| Condition | Multiplier |
|---|---|
| Resistance to common physical (nonmagical B/P/S) | ×2 |
| Resistance to one damage type | ×1.25 |
| Resistance to two+ damage types | ×1.5 |
| Immunity to one uncommon type (poison, fire) | ×1.5 |
| Immunity to common physical or multiple types | ×2 |
| Regeneration | +regen/round × 4 to effective HP |

## 7. Condition reference (for ability design)

Justification: a design aid, not raw rules text — flags which conditions
are safe to hand out freely vs. which need rationing.

| Condition | Key effect | Best used for |
|---|---|---|
| [Blinded](vault/srd/rules/blinded.md) | Attacks at disadvantage; attacked at advantage | Lurkers, ambushers |
| [Charmed](vault/srd/rules/charmed.md) | Can't attack charmer | Fey, enchanters |
| [Frightened](vault/srd/rules/frightened.md) | Disadvantage near source visible | Fear-based monsters |
| [Grappled](vault/srd/rules/grappled.md) | Speed 0 | Grabbers |
| [Paralyzed](vault/srd/rules/paralyzed.md) | Auto-crit adjacent; auto-fail STR/DEX | High-CR controllers — use sparingly |
| [Poisoned](vault/srd/rules/poisoned.md) | Disadvantage on attacks/checks | Venomous creatures |
| [Prone](vault/srd/rules/prone.md) | Adjacent at advantage, ranged at disadvantage | Trip-focused brutes |
| [Restrained](vault/srd/rules/restrained.md) | Speed 0; attacked at advantage | Web-spinners |
| [Stunned](vault/srd/rules/stunned.md) | [Incapacitated](vault/srd/rules/incapacitated.md), auto-fail STR/DEX | Very powerful — use sparingly |
