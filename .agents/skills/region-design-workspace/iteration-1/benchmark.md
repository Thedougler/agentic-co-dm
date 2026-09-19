# region-design benchmark — iteration 1

**With-skill mean pass rate:** 1.0 (±0.0)
**Without-skill mean pass rate:** 0.364 (±0.235)
**Delta pass rate:** +174.7%
**Delta tokens:** +67.4% (with 57555 vs without 34388)
**Delta duration:** +79.7% (with 116.8s vs without 65.0s)

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| aruhe-improve | 8/8 (1.0) | 5/8 (0.625) |
| aruhe-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| brine-ladder-from-scratch | 6/6 (1.0) | 3/6 (0.5) |
| Midchain-flesh | 6/6 (1.0) | 2/6 (0.333) |

## Analyst observations

- With-skill mean pass_rate 1.0 across 4 evals; without-skill mean ~0.375 — large discriminating delta driven by guardrail/process assertions.
- Eval-2 (resist invent) is the strongest discriminator: with_skill 4/4, without_skill 0/4. Baseline writes ancient evil + warlord as canon.
- Eval-1 baseline still produces usable region.md-shaped content from the template-in-prompt, but fails identity sentence, work gate, and pressure-forward DM thesis.
- Eval-3 baseline gives route tradeoffs but omits invention:true and invents smuggling-war / Crown-inspection fronts as fact.
- Eval-4 baseline keeps named links but invents occupation war + plague as established and retains five-sentence kernel instead of full region.md reshape.
- With-skill costs more tokens/time (~1.7–2× duration). Acceptable: process gates + pressure discipline are the skill value-add.
- Process assertions (identity sentence, work gate) require agent_report.md artifacts — graders should treat those as first-class outputs alongside the page draft.
