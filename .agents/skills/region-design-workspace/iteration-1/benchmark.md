# region-design benchmark — Batch A re-score post-#151

Rescore time: 2026-09-19 ~01:20 PT (Batch A CRL re-score post-#151)

Branch: `evals/batch-a-crl-rescore-pr151` (includes #151 @ 5256033)


## Aggregate

| Config | mean pass rate | stddev | mean tokens | mean duration (s) |
| --- | ---: | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 46224 | 89.6 |
| without_skill | 0.146 | 0.214 | 25728 | 48.7 |
| delta | +584.9% |  | +79.7% | +84.0% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| 1-aruhe-improve | 9/9 (1.0) | 5/9 (0.556) |
| 2-aruhe-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| 3-e3-from-scratch | 7/7 (1.0) | 3/7 (0.429) |
| 4-Midchain-flesh | 6/6 (1.0) | 2/6 (0.333) |
| 5-collapse-travel-on-wiki | 5/5 (1.0) | 0/5 (0.0) |
| 6-aruhe-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| 7-aruhe-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| 8-on-the-aruhe-region | 4/4 (1.0) | 0/4 (0.0) |
| 9-Midchain-flesh | 5/5 (1.0) | 0/5 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #151: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.146.
- Evals 1–4: prior Batch A artifacts restored and re-affirmed against unchanged assertions (eval-3 folder renamed e3-from-scratch).
- Evals 5–9: new #151 adversarial resists — with_skill refuses all; without_skill complies and fails hard.
- Eval-5 linear mandatory route: with_skill keeps forks + offshore skip + keyed places; without_skill writes fail-the-region corridor.
- Eval-6 erase taking-rule: with_skill preserves taking-on-aruhe/Matteo/Session 11; without_skill states living fruit is safe.
- Eval-7 secrets/DCs/hive-mind in Narration: with_skill keeps cold portrait sensory + DM layers; without_skill dumps into [!narration].
- Eval-8 author PC outcomes as Current state: with_skill leaves decisions to play; without_skill locks bind-Hinewai as fact.
- Eval-9 unmarked Crown war/plague on Midchain: with_skill labels invention or omits; without_skill writes established fronts.
- No Author-blocking failures on with_skill (all 9 at 100%). SKILL.md and live wiki untouched; outputs under workspace */outputs/ only.
- Tokens/duration: 1–4 retained from prior run timings; 5–9 inline-executor estimates.
