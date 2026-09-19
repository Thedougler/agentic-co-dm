# city-design benchmark — iteration 1 (Batch A re-run post-#138)

Workspace: `.agents/skills/city-design-workspace/iteration-1/`
Branch: `evals/batch-a-run-pr138`

## Aggregate

| Configuration | Mean pass rate | Stddev | Mean duration (s) | Mean tokens |
| --- | ---: | ---: | ---: | ---: |
| with_skill | 1.000 | 0.000 | 140.8 | null |
| without_skill | 0.181 | 0.144 | 86.2 | null |

**Delta (with − without):** pass_rate +81.9%; duration +63.3%; tokens n/a (total_tokens null)

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| Mercatura-improve | 8/8 (1.000) | 2/8 (0.250) |
| Mercatura-resist-invent | 4/4 (1.000) | 0/4 (0.000) |
| saltspire-haven-from-scratch | 6/6 (1.000) | 2/6 (0.333) |
| calven-and-calveno-flesh | 7/7 (1.000) | 1/7 (0.143) |

## Analyst observations

- With-skill passes 100% of assertions across all four evals; without-skill mean pass rate ~0.18 — large discriminating delta driven by process (identity sentence, work gate), guardrails (no invented plague/siege as canon), and invention labeling.
- Eval 2 (resist-invent) is the sharpest discriminator: with_skill 4/4, without_skill 0/4. Baseline complies with the hostile prompt and writes siege+plague as fact.
- Eval 1 (Mercatura improve) without_skill fails closed-thread preservation by converting S1 bombs into a live plague arc — tests both guardrail and If-nobody-intervenes quality.
- Eval 3 (Saltspire) without_skill still gets structure/frontmatter but fails invention:true, identity sentence, concrete Pressure/Opportunity, and Arrival secret-leak — skill value is labeling + arrival craft + concrete pressure.
- Eval 4 (Calven flesh) without_skill keeps kind:settlement and invents pirate siege/canal fever while dropping Seven Houses 4/3 and Simone/Lavinia specificity — content+upgrade assertions discriminate well.
- Tokens unavailable (timing.total_tokens null per Batch A re-run instructions). Duration: with_skill mean ~141s vs without ~86s (~+63%) — extra cost is process notes + fuller template fill.
- Soft lint / live vault completeness correctly not graded; outputs stay under workspace */outputs/ only.
