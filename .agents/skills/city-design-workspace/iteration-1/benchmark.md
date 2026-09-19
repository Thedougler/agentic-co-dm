# city-design benchmark — Batch A re-score post-#145

Rescore time: 2026-09-19 ~01:10 PT (Batch A re-score post-#145)

Branch: `evals/batch-a-rescore-pr145` (includes #145 @ ae11c9c)


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 140.8 |
| without_skill | 0.169 | 0.130 | 86.2 |
| delta | +83.1% |  | +63.3% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| Mercatura-improve | 8/8 (1.0) | 2/8 (0.25) |
| Mercatura-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| saltspire-haven-from-scratch | 6/6 (1.0) | 2/6 (0.333) |
| calven-and-calveno-flesh | 11/11 (1.0) | 1/11 (0.091) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #145: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.169.
- Process asserts now require durable locus (process-notes.md / transcript.md); with_skill records identity sentence + work gate there; without_skill still omits them.
- Structure+substance companions: with_skill fills Orientation ≥2 districts and Gazetteer; without_skill often still clears the floor (headings+some fill) — discrimination remains in process/guardrail/content.
- Eval-2 resist-invent still sharpest discriminator (1.0 vs 0.0).
- Eval-1 DM-thesis negative (must NOT be S1 Otar/Solange/bombs history) fails without_skill plague-arc thesis; with_skill pressure-forward function thesis passes.
- Eval-4 split content asserts (5): with_skill 5/5; without_skill 0/5 — splitting removes all-or-nothing compound and still fully discriminates.
- No new Author-blocking failures on with_skill; soft note: bare structure floor remains weak discriminator alone (both configs can pass).
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only.
