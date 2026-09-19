# place-design benchmark — iteration 1 (Batch A post-#138)

Workspace: `/home/box/agentic-co-dm/.agents/skills/place-design-workspace/iteration-1`

## Aggregate

| Config | Mean pass rate | Stddev | Mean tokens | Mean duration (s) |
| --- | ---: | ---: | ---: | ---: |
| with_skill | 1.000 | 0.0000 | 38214 | 79.4 |
| without_skill | 0.162 | 0.2488 | 17214 | 36.2 |

**Delta (with − without):** pass_rate +517.3%, tokens +122.0%, duration +119.3%

## Per-eval pass rates

| Eval | with_skill | without_skill | Δ |
| --- | ---: | ---: | ---: |
| high-eyrie-improve | 1.000 (7/7) | 0.429 (3/7) | +0.571 |
| high-eyrie-resist-invent | 1.000 (4/4) | 0.250 (1/4) | +0.750 |
| cinder-ford-from-scratch | 1.000 (6/6) | 0.333 (2/6) | +0.667 |
| river-slack-basin-flesh | 1.000 (6/6) | 0.500 (3/6) | +0.500 |
| design-a-memorable-settlement | 1.000 (4/4) | 0.000 (0/4) | +1.000 |
| map-the-significant-nodes | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| prepare-a-sealed-archive | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| design-an-obstacle-at | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| populate-an-inhabited-landmark | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| write-four-location-moves | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| design-a-high-tier | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| create-a-ruin-that | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| design-a-planar-bazaar | 1.000 (3/3) | 0.000 (0/3) | +1.000 |
| file-a-wilderness-location | 1.000 (4/4) | 0.750 (3/4) | +0.250 |

## Analyst observations

- With-skill mean pass rate is perfect (1.0) across all 14 evals; without-skill mean is substantially lower, driven by process gates (kernel, work gate), invention labeling, and craft anti-patterns.
- Strongest discrimination: eval-2 resist-invent (1.0 vs 0.25), eval-3 from-scratch labeling/kernel (1.0 vs 0.33), and craft evals 5–13 where baseline often produces lore-only / single-solution / reset-state answers.
- Eval-14 structure assertions (four cardinals, travel-day distances, Where conventions) pass for both configs when the baseline still emits a Where section — only the southern canon-gap guardrail discriminates. Flagged in EVAL_AUTHOR_FLAGS.md.
- Eval-10 assertion "Moves alter routes..." can false-positive on negation phrasing in weak baselines; grader corrected for this run. Consider requiring actor/trigger/consequence fields explicitly.
- With-skill costs more tokens (~2×) and time (~2.3×) than baseline on this iteration — expected for kernel + work-gate + reference-shaped craft.
- Wiki-grounded evals 1 and 4: baseline still preserves much content canon (template + page text) but fails process and guardrail assertions — skill value is process discipline more than raw recall.
