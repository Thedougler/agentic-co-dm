# lore-design benchmark — Batch A re-score post-#145

Rescore time: 2026-09-19 ~01:10 PT (Batch A re-score post-#145)

Branch: `evals/batch-a-rescore-pr145` (includes #145 @ ae11c9c)


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 121.5 |
| without_skill | 0.367 | 0.136 | 67.5 |
| delta | +172.1% |  | +80.0% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| taking-on-aruhe-improve | 9/9 (1.0) | 5/9 (0.556) |
| taking-on-aruhe-resist-invent | 5/5 (1.0) | 1/5 (0.2) |
| pier-debt-custom-from-scratch | 7/7 (1.0) | 3/7 (0.429) |
| taken-whole-flesh | 7/7 (1.0) | 2/7 (0.286) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #145: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.367.
- Eval-1 heading-form ## At a Glance now fails callout copy-forward (without 5/9); with_skill upgrades to template headings + kind/truth.
- Process asserts require durable locus (process-notes.md / transcript.md); with_skill records durable question + work gate; without_skill omits them.
- Eval-2 resist-invent remains sharpest discriminator (1.0 vs 0.2) — baseline fungal network as Current Truth.
- Eval-3 new vault-harbour negative assert fires on without_skill Kalowe/Midchain claim; invention:true + single-question still discriminate (with 7/7 vs without 3/7).
- Eval-4 new Discovery proposed/invention wording assert fails unlabeled without_skill clues; rumour≠Current Truth still strong (with 7/7 vs without 2/7).
- No new Author-blocking failures on with_skill; soft note: structure+substance floor still passable without skill when headings are filled.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only.
