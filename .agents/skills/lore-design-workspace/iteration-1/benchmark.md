# lore-design benchmark — Batch A re-score post-#151

Rescore time: 2026-09-19 ~01:20 PT (Batch A re-score post-#151)

Branch: `evals/batch-a-crl-rescore-pr151` (includes #151 @ 5256033)


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 102.8 |
| without_skill | 0.163 | 0.204 | 50.3 |
| delta | +513.5% |  | +104.4% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| taking-on-aruhe-improve | 9/9 (1.0) | 5/9 (0.556) |
| explain-why-aruhe-s | 5/5 (1.0) | 1/5 (0.2) |
| e3-from-scratch | 7/7 (1.0) | 3/7 (0.429) |
| taken-whole-flesh | 7/7 (1.0) | 2/7 (0.286) |
| promote-the-kalowe-dockside | 5/5 (1.0) | 0/5 (0.0) |
| taking-on-aruhe-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| fill-every-limits-unknown | 4/4 (1.0) | 0/4 (0.0) |
| target-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| taken-whole-resist-invent | 5/5 (1.0) | 0/5 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #151: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.163.
- Suite expanded 4→9: added promote-rumour (e5), Session-11 rewrite (e6), fill-Limits-Unknown (e7), skip-gate pantheon dump (e8), Glass Debt Concord mint (e9).
- Evals 1–4 retain post-#145 discriminators (heading-form, resist-invent metaphysics, invention:true + harbour-negative, rumour≠Current Truth).
- New resists all discriminate sharply: with_skill 1.0 vs without_skill 0.0 on e5–e9.
- Durable process locus (process-notes.md / transcript.md) still required; graders must read those artifacts.
- No Author-blocking failures on with_skill across all 9 evals.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only. No SKILL.md or live wiki/ edits.
