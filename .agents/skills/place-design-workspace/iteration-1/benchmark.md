# place-design benchmark — post-#156 thin VERIFY

Rescore time: 2026-09-19 ~01:25 PT (post-#156 thin place-design VERIFY)

Branch: `evals/thin-place-pr156` tracking `phase3/thin-place-design` @ `83d6043` (merged main `442e36d` #156)

Skill: thinned SKILL.md (~117 lines) + `references/place-craft.md` (and sibling refs). Suite: 14 place-design evals — **not edited**.

## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 62.1 |
| without_skill | 0.084 | 0.148 | 37.1 |
| delta | +91.6% |  | +67.4% |

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

**CoS recommendation: KEEP #156**

## Analyst observations

- Thin skill (#156): refuse-gates + build steps stay in SKILL.md; craft detail moved to `references/place-craft.md`. with_skill runs loaded refs when SKILL instructed.
- Process asserts (kernel / work gate) satisfied via durable locus under with_skill; without_skill omits on wiki-grounded evals.
- Craft evals 5–13 and Where/moves tighten (10, 14) still fully discriminate.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace `*/outputs/` only. No SKILL.md or live wiki/ edits.
