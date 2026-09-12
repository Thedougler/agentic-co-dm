# Setting the DC

## Typical ability-check bands (SRD 5.2)

| Task difficulty | DC |
|---|---:|
| Very easy | 5 |
| Easy | 10 |
| Medium | 15 |
| Hard | 20 |
| Very hard | 25 |
| Nearly impossible | 30 |

Use these rungs. Default ordinary adventuring task is **15**. Write `DC 15`,
not 12, 13, 17, 18, or 19, unless a specific procedure or a creature's
`8 + PB + mod` *save* produces that number.

The GM sets *check* DCs. The effect that causes a *save* sets that *DC*
(spellcasting formula, monster stat block, or a named procedure below).

## Named 2024 procedures (use these before the band)

| Situation | Test | DC |
|---|---|---|
| Hide | Dexterity (Stealth) *check* | **15**; record the total as the find-*DC* |
| Influence (hesitant creature) | see `checks.md` | **15 or the monster's Intelligence, whichever is higher** |
| Stabilize / first aid at 0 HP | Help + Wisdom (Medicine) *check* | **10** |
| Knock out recovery first aid | action, Wisdom (Medicine) *check* | **10** |
| Long Jump, low obstacle | Strength (Athletics) *check* | **10** |
| Long Jump, land in Difficult Terrain | Dexterity (Acrobatics) *check* | **10** |
| Concentration, took damage | Constitution *save* | **10 or half damage**, max 30 |
| Death *save* | no ability | **10** to succeed |
| Grapple or Shove (Unarmed Strike) | Strength or Dexterity *save* (target's choice) | **`8 + Strength modifier + PB`** |
| Escape a grapple | Strength (Athletics) or Dexterity (Acrobatics) *check* | the grapple's *DC* |
| Spell or monster feature *save* | ability the effect names | **`8 + relevant ability modifier + PB`** |

## Save DC formula

`Spell save DC` / feature save *DC* = `8 + spellcasting (or relevant) ability modifier + Proficiency Bonus`.

Proficiency Bonus by character level or monster CR:

| Level or CR | PB |
|---|---:|
| 1–4 | +2 |
| 5–8 | +3 |
| 9–12 | +4 |
| 13–16 | +5 |
| 17–20 | +6 |
| 21–24 | +7 |
| 25–28 | +8 |
| 29–30 | +9 |

Example: a CR 5 monster with Strength 19 (+4) grapples at DC 15
(`8 + 4 + 3`). A 5th-level Cleric with Wisdom 16 (+3) has spell save DC 14
(`8 + 3 + 3`).

Use this formula for **imposed *saves***. Do not use it to invent a climb,
lock, recall, or persuasion *DC*. Those use the typical band or a named
procedure.

Monster save *numbers* on a new stat block: choose the *save* type here, then
take the number from `homebrew-monsters-5e` chassis (peer or
`8 + PB + modifier`). Do not stack both.

## Calibration while writing content

Match the fiction first: a rusty padlock is Easy (10); a vault lock is Hard
(20). The *DC* describes the task, not the roller. A specialist succeeds more
often at the same world task as they level; the Easy *rung* for that task
stays 10.

### Party archetypes

Fill three **archetypes** for this skill and confirm each written *rung*
matches the intent below. Named 2024 procedures and `8 + PB + mod` *saves*
skip this check.

Lookup, stop when the three bonuses are known:

1. Foundry `list-characters` / `get-character` — live skill bonuses.
2. Campaign `hot.md` + PC index via `qmd-retrieval` — class, subclass,
   spotlight skills, level.
3. Tier archetypes from the PB table above:

| Level | PB | Untrained | Proficient | Specialist (expertise or primary + PB) |
|---|---:|---|---|---|
| 1–4 | +2 | +0 to +2 | +4 to +6 | +6 to +8 |
| 5–8 | +3 | +1 to +3 | +6 to +8 | +9 to +11 |
| 9–12 | +4 | +2 to +4 | +7 to +9 | +11 to +13 |
| 13–16 | +5 | +2 to +5 | +8 to +10 | +13 to +15 |

| *Rung* | Intent | Sanity-check |
|---|---|---|
| 10 Easy | Floor / participation / consolation | Untrained often makes it; proficient almost always |
| 15 Medium | Default ordinary task | Proficient is a real test; untrained sometimes |
| 20 Hard | Specialist *showcase* | Specialist often; untrained almost never |
| 25 Very Hard | Prize on a good specialist roll | Skip at tier 1 unless the fiction is legendary |
| 30 | Nearly impossible | Ordinary *interactables* do not use this |

Chance to meet or beat the *DC* (d20 + bonus):

| DC | +0 | +5 | +8 | +11 |
|---:|---:|---:|---:|---:|
| 10 | 55% | 80% | 95% | 100% |
| 15 | 30% | 55% | 70% | 85% |
| 20 | 5% | 30% | 45% | 60% |
| 25 | — | 5% | 20% | 35% |

If the feel is wrong, pick a different typical-band *rung*. Setting
`DC = bonus + 8` to force a success rate is the treadmill: the *DC* still
describes the task.

**Owner pages** (location, item, NPC): world-true *rungs*. Sanity-check against
the campaign’s current tier, not a named PC. The page must still play if the
party changes.

**Session / run-guide surfaces:** DCs still come from the task. Sanity-check
against live bonuses when Foundry or sheets exist so the *showcase* *rung* is
reachable by the built-for-it character and the floor is not a brick wall.

Detection and disable can differ. Noticing a tripwire (Search / Perception) is
often easier than understanding the glyph (Study / Arcana).

If the party failed, change the situation (`traps-trials`); leave the *DC*.
Give at least two approaches when the scene would otherwise hang on one
*check*. Passive Perception vs Hide: compare Passive Perception to the hider's
recorded Stealth total when nobody is Searching.

## Advantage and other modifiers

Advantage / Disadvantage: roll two d20s, use the higher or lower. Multiple
sources do not stack. Advantage and Disadvantage on the same roll cancel,
even if the counts are unequal.

Circumstances the GM grants (footing, light, time, tools, cover) should be
Advantage, Disadvantage, or a listed bonus — not a homemade +3 *DC*.

Heroic Inspiration (SRD): expend to reroll any one die just rolled. Not a
reason to skip setting a fair *DC*.
