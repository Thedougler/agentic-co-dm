# Combat simulation report

- **Engine**: dndsim v0.10.0
- **Seed**: 1
- **Universes**: 50,000
- **Round cap**: 30

## Perrin, Ysolde, Rowan vs. Grung Skirmisher A, Grung Skirmisher B, Grung Chief

## Outcome distribution

- Perrin, Ysolde, Rowan wins: **0.0%** (95% CI 0.0%–0.0%, MC stderr ±0.0%)
- Grung Skirmisher A, Grung Skirmisher B, Grung Chief wins: **100.0%**
- Stalemate rate (round cap hit, counted as a loss): 0.0%
- Rounds: mean 9.48 (median 9.00, p95 13.00)

## Party outcomes

- P(TPK): **100.0%**
- P(≥1 down): **100.0%**
- ≥1 down: 100.0%, ≥2 down: 100.0%, ≥3 down: 100.0%

## Per-PC

| PC | HP remaining (p5/p50/p95) | P(down) |
|---|---|---|
| Perrin | 0.0%/0.0%/0.0% | 100.0% |
| Ysolde | 0.0%/0.0%/0.0% | 100.0% |
| Rowan | 0.0%/0.0%/0.0% | 100.0% |

## Per-combatant output

| Combatant | Side | Mean damage dealt | Mean reactions spent | Mean conc. breaks |
|---|---|---|---|---|
| Perrin | party | 8.40 | 0.00 | 0.00 |
| Ysolde | party | 21.70 | 0.00 | 0.98 |
| Rowan | party | 21.81 | 0.00 | 0.00 |
| Grung Skirmisher A | enemy | 19.71 | 1.10 | 0.00 |
| Grung Skirmisher B | enemy | 32.34 | 1.39 | 0.00 |
| Grung Chief | enemy | 152.73 | 1.39 | 0.00 |

## Positional figures

| Combatant | Mean turns w/o target | Mean opportunity attacks |
|---|---|---|
| Perrin | 0.00 | 0.00 |
| Ysolde | 0.00 | 0.00 |
| Rowan | 0.00 | 0.00 |
| Grung Skirmisher A | 0.06 | 1.10 |
| Grung Skirmisher B | 0.15 | 1.39 |
| Grung Chief | 0.17 | 1.39 |

## Effective Difficulty Rating: **Deadly**

Fired rule: P(win) < 0.75 or P(≥1 down) > 0.5 or P(TPK) ≥ 0.05.
**Policy**: dndsim:policy/greedy
**Edition**: dnd5e_2024
