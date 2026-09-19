# place-design benchmark — Batch A re-score post-#145

Rescore time: 2026-09-19 ~01:15 PT (Batch A re-score post-#145)

Branch: `evals/batch-a-rescore-pr145` (includes #145 @ ae11c9c)


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 79.4 |
| without_skill | 0.084 | 0.148 | 36.2 |
| delta | +91.6% |  | +119.3% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| high-eyrie-improve | 7/7 (1.0) | 3/7 (0.429) |
| high-eyrie-resist-invent | 4/4 (1.0) | 1/4 (0.25) |
| cinder-ford-from-scratch | 6/6 (1.0) | 1/6 (0.167) |
| river-slack-basin-flesh | 6/6 (1.0) | 2/6 (0.333) |
| design-a-memorable-settlement | 4/4 (1.0) | 0/4 (0.0) |
| map-the-significant-nodes | 3/3 (1.0) | 0/3 (0.0) |
| prepare-a-sealed-archive | 3/3 (1.0) | 0/3 (0.0) |
| design-an-obstacle-at | 3/3 (1.0) | 0/3 (0.0) |
| populate-an-inhabited-landmark | 3/3 (1.0) | 0/3 (0.0) |
| write-four-location-moves | 3/3 (1.0) | 0/3 (0.0) |
| design-a-high-tier | 3/3 (1.0) | 0/3 (0.0) |
| create-a-ruin-that | 3/3 (1.0) | 0/3 (0.0) |
| design-a-planar-bazaar | 3/3 (1.0) | 0/3 (0.0) |
| file-a-wilderness-location | 4/4 (1.0) | 0/4 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #145: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.084.
- Process asserts require durable locus (process-notes.md / transcript.md); with_skill records kernel + work gate there; without_skill omits them on wiki-grounded evals 1–4.
- Eval-10 five-part moves tighten: with_skill states actor/trigger/visible result/new opportunity/lasting consequence positively on all four moves; without_skill negation-only ('No lasting change to routes…') correctly fails.
- Eval-14 Where discipline tighten: with_skill uses explicit **North/East/South/West** + travel-day language + southern canon gap with no south wikilink/proper name (4/4); without_skill invents Port Haven south and lacks cardinal lines (0/4) — former non-discriminating structure asserts now discriminate.
- Eval-2 resist-invent remains sharp (1.0 vs 0.25). Craft evals 5–13 fully discriminate (1.0 vs 0.0).
- No Author-blocking with_skill failures. Soft note: structure floor on evals 1/3/4 can still clear for without_skill when template headings are partially filled.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only. No SKILL.md or live wiki/ edits.
