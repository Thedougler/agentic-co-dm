# Saving throws

A *save* is a *d20 test* to **evade or resist a threat already in motion**.
The creature does not choose to attempt it; the effect forces it. The creature
may choose to fail without rolling.

Roll d20 + ability modifier + PB if proficient in that *save*. Meet or beat
the *DC*. The effect that caused the *save* states the result.

If a target is forced to make a *save* and lacks that ability score, it fails.

## Which ability

| Ability | Resist or evade | Typical content |
|---|---|---|
| Strength | Direct physical force | Grapple or Shove imposed on you; being pushed, pinned, or crushed; some restraints |
| Dexterity | Get out of the way | Area blasts, explosions, traps that can be dodged, many dragon breaths |
| Constitution | Endure a bodily hazard | Poison, disease, pain, necrotic drain, holding breath as an imposed effect, concentration when damaged |
| Intelligence | Recognize an illusion as fake | Many illusion and some psychic-pattern effects |
| Wisdom | Mental assault | Charm, fear, most domination and command, many enchantments |
| Charisma | Assert identity | Possession, banishment, some curse or identity-erasure effects |

Area damage the target can **dodge** is Dexterity. A toxin already in the
blood is Constitution. A spell rewriting the mind is Wisdom. A glamour the
target can **disbelieve** is Intelligence.

Write **Dexterity save — `DC 15`** (at-table grammar in `obsidian-markdown`).
Statblock YAML still uses `DC 15 Dexterity saving throw`. On a damaging
*save*, roll damage once for all targets hit by the same effect. Many such
effects deal half damage (round down) on a success.

## Cover (Dexterity *saves* and AC)

| Degree | Benefit | Typical source |
|---|---|---|
| Half | +2 AC and Dexterity *saves* | Another creature, or an object covering at least half the target |
| Three-Quarters | +5 AC and Dexterity *saves* | An object covering at least three-quarters |
| Total | Cannot be targeted directly | An object covering the whole target |

Only the best degree applies. Dodge (the action) grants Advantage on Dexterity
*saves* until the start of the next turn, unless Speed is 0 or the creature is
Incapacitated.

## Grapple and Shove (Unarmed Strike)

These are ***saves***, not Athletics contests.

When a creature hits with the Grapple or Shove option of an Unarmed Strike
(target no more than one size larger):

- Target chooses a **Strength or Dexterity *save***.
- *DC* = `8 + grappler's Strength modifier + grappler's Proficiency Bonus`
  (Monk Martial Arts may substitute Dexterity for that *DC*).
- Grapple also needs a free hand. Success: Grappled (Speed 0).
- Shove: push 5 feet **or** Prone.

Escape: action, Strength (Athletics) or Dexterity (Acrobatics) *check* against
**that same *DC***. Also ends if the grappler is Incapacitated or the distance
exceeds the grapple's range. The grappler may release for free.

Monster special grapples (tentacle, swallow) use the *DC* on the stat block
and still want an escape *check* or other counterplay.

## Concentration

Damage while concentrating: Constitution *save*, *DC* **10 or half the damage
taken (round down), whichever is higher**, maximum 30. Starting another
Concentration effect, becoming Incapacitated, or dying also ends it. The
creator can drop Concentration at any time (no action).

## Death *saves*

Start of turn at 0 HP: roll a d20 with **no ability**. 10 or higher is a
success. Three successes → Stable. Three failures → death. A 1 is two
failures. A 20 restores 1 HP. Damage at 0 HP is one failure (two if the
damage is a Critical Hit). Massive leftover damage ≥ Hit Point maximum is
death.

Stabilize: Help + DC 10 Wisdom (Medicine). A Stable creature at 0 HP makes
no death *saves* until it takes damage; it is still Unconscious and regains
1 HP after 1d4 hours if not healed.

## Attack rolls are not *saves*

Natural 20 always hits and natural 1 always misses **on attack rolls only**.
A 20 on a *check* or *save* is just a high roll unless a feature says otherwise.
