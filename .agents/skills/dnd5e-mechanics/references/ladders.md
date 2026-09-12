# Interactables and quality ladders

Load this file when a *check* is about loot, harvest, a tool, a secret, a
contested resource, or any graded world object — or when a draft is one Easy
*check* that hands over something valuable.

A world object the party would want is an *interactable*. The *check* is how
they take a risk for a reward. 2024 degrees of success: one *d20 test*, several
outcomes from the same total.

## When to write which shape

| Fiction | Shape |
|---|---|
| Trivial take, no grade, no competition | One typical-band *check* with a failure that changes play |
| Valuable **or** contested **or** graded (common / useful / prize) | *Quality ladder* on one attempt |
| Two skills would produce different fiction | Two approaches (already the several-approach mark) |
| Valuable **and** contested **and** graded | *Quality ladder*; add a second approach when the fiction supports it |

A *quality ladder* is one declared attempt. The total meets the highest *rung*
it reaches. It is not a second roll at a higher *DC*, and it is not a
success-count skill challenge (`encounter-prep` / `traps-trials`).

Run-card **Partial** (miss by 1–4) lives in `run-guide`. On owner **If the
party** lists, write ladders. On a Be ready for table, keep Partial as that
skill defines it; graded harvest can still fill the success cell.

## Grade from the fiction

Name rungs from what exists in the world, then pick typical-band DCs:

| Grade | Typical *rung* | Who it is for |
|---|---|---|
| Consolation / fallen / obvious | `DC 10` | Untrained participation |
| Useful / ripe / ordinary secret | `DC 15` | Proficient default |
| Prize / hidden / contested take | `DC 20` | Specialist *showcase* |
| Peak / legendary specimen | `DC 25` | Good specialist roll; skip at tier 1 unless the fiction is legendary |

Rarity, local competition, and the item owner set the top *rung*. A common
windfall tops at 15. A sought-after prize tops at 20 or 25. Party bonuses
choose which *rung* to write (`difficulty.md`); they do not invent a new
number.

## Failure

Every ladder has a failure that changes play. Time only counts when a clock,
noise, or lost opportunity is real. Degree of failure (2024): miss by 5 or more
can be worse than a near miss.

| Failure | Play change |
|---|---|
| Noise | Nearby creatures notice |
| Competition | Local fauna or rivals close on the prize |
| Claim | Taking the living source marks the taker |
| Cost | Specimen ruined, tool spent, injury |
| Clock | The attempt spends the hour; the window closes |

Write one failure line that fits this object. A near miss can still yield the
consolation grade at a cost; a miss by 5+ takes the hard failure.

## Mark

At-table grammar in `obsidian-markdown`. One attempt, stacked `DC n` outcomes:

```markdown
**Wisdom (Survival) — harvest the grove**
- `DC 10` → Fallen ordinary take; no contest.
- `DC 15` → Ripe useful specimen; some noise.
- `DC 20` → Prize grade (wikilink the item).
- Failure → Local fauna close in, or the living source is claimed.
```

Several approaches stay separate **Ability (Skill)** lines. Identify (Study /
Nature) and take (Search / Survival) are different tests when both matter.

## Worked example

A lakeside grove holds common fallen fruit, useful ripe fruit, and a rare
prize the island's animals also want.

- **Wisdom (Survival) — harvest** with rungs 10 / 15 / 20, failure attracts
  foragers or claims a living stem.
- **Intelligence (Nature) — `DC 15`** → Identify which specimens are the prize
  before anyone pulls.
- Taking only what is already on the ground is the Easy *rung*. Stripping a
  living branch is the contested *rung* plus the claim failure.

The prize is never the Easy outcome.
