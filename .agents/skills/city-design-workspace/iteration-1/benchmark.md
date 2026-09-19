# city-design benchmark — Batch A re-score post-#151

Rescore time: 2026-09-19 ~01:20 PT (Batch A CRL re-score post-#151)

Branch: `evals/batch-a-crl-rescore-pr151` (includes #151 @ 5256033)


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 112.0 |
| without_skill | 0.067 | 0.117 | 70.5 |
| delta | +93.3% |  | +58.9% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| eval-1-Mercatura-improve | 8/8 (1.0) | 2/8 (0.25) |
| eval-2-Mercatura-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| eval-3-saltspire-haven-from-scratch | 6/6 (1.0) | 2/6 (0.333) |
| eval-4-calven-and-calveno-flesh | 11/11 (1.0) | 1/11 (0.091) |
| eval-5-Mercatura-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| eval-6-on-wiki-entities-place | 5/5 (1.0) | 0/5 (0.0) |
| eval-7-target-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| eval-8-add-an-active-situation | 5/5 (1.0) | 0/5 (0.0) |
| eval-9-Mercatura-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| eval-10-calven-and-calveno-flesh | 4/4 (1.0) | 0/4 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #151 (5256033): with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.067.
- Suite expanded 4→10 evals with session-beats adversarial catalog (forced rail, PC civic fiat, secrets-in-Arrival, single-lever, skip-gate, combat-only).
- Evals 1–4 craft/resist assertions unchanged from #145 — outputs carried forward and re-confirmed; all with_skill 1.0.
- New evals 5–10: with_skill all 1.0 (refuse-shaped); without_skill all 0.0 — perfect adversarial discrimination.
- Eval-2 + eval-5/8/9 Mercatura resists remain strongest city discriminators alongside Calven eval-6/7/10.
- No new Author-blocking failures on with_skill across 10/10 evals.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only.
- Bounds held: no SKILL.md edits; no live wiki/ writes; did not touch Batch B / main.
