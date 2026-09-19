# region-design benchmark — Batch A re-score post-#145

Rescore time: 2026-09-19 ~01:10 PT (Batch A re-score post-#145)

Branch: `evals/batch-a-rescore-pr145` (includes #145 @ ae11c9c)


## Aggregate

| Config | mean pass rate | stddev | mean tokens | mean duration (s) |
| --- | ---: | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 57555 | 116.8 |
| without_skill | 0.329 | 0.206 | 34388 | 65.0 |
| delta | +203.6% |  | +67.4% | +79.7% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| aruhe-improve | 9/9 (1.0) | 5/9 (0.556) |
| aruhe-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| brine-ladder-from-scratch | 7/7 (1.0) | 3/7 (0.429) |
| Midchain-flesh | 6/6 (1.0) | 2/6 (0.333) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)


## Analyst observations

- Re-score after #145: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.329.
- Process asserts now require durable locus (process-notes.md / agent_report.md / transcript.md); with_skill agent_report.md satisfies; without_skill still omits them.
- Eval-1 new Feared-for assert (F3): with_skill cites taking/razer-grass; without_skill fails on vague 'island waking'.
- Eval-2 new ban on threat-embedded rewrite (F2): with_skill 5/5 (response-only); without_skill 0/5 (aruhe-threat-update.md embeds evil+warlord).
- Eval-3 new parent-region invent label (F4): with_skill leaves Parent unassigned/proposed; without_skill asserts Midchain as fact.
- Eval-4 kernel ban wording (F5): with_skill full region.md; without_skill retains ## Five-sentence kernel (retained).
- Structure+substance companions: both configs can still clear the floor when template headings are visible and partially filled — discrimination remains in process/guardrail/quality.
- No new Author-blocking failures on with_skill; tokens/duration retained from prior run timings (estimated executor).
- Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only. SKILL.md and live wiki untouched.
