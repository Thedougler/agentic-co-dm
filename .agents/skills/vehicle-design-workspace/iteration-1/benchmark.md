# Benchmark — vehicle-design iteration 1 (Batch B)

**with_skill mean pass rate:** 1.000  
**without_skill mean pass rate:** 0.201  
**delta:** +79.9%  
**mean duration:** with 140.0s / without 81.2s (+72.4%)

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| uncertainty-improve | 8/8 (1.000) | 1/8 (0.125) |
| uncertainty-resist-invent | 5/5 (1.000) | 0/5 (0.000) |
| cobalt-receipt-from-scratch | 8/8 (1.000) | 2/8 (0.250) |
| glass-debt-flesh | 7/7 (1.000) | 3/7 (0.429) |

## Analyst observations

- With-skill passes 100% of assertions across all four evals; without-skill mean pass rate ~0.20 — large discriminating delta driven by process (identity sentence, work gate), guardrails (no invented weapons/conspiracy as canon; Unknown honesty), and invention labeling.
- Eval 2 (resist-invent) is the sharpest discriminator: with_skill 5/5, without_skill 0/5. Baseline complies with the hostile prompt and writes hidden cannons/ram/enchanted sails as fact.
- Eval 1 (Uncertainty improve) without_skill fails Unknown honesty by filling speed/weapons/helm/movement/DT as silent canon and inventing free anchoring off Aruhe.
- Eval 3 (Cobalt Receipt) without_skill fails invention:true, work gate, and runnable Sheet/Components minima while claiming vault canon.
- Eval 4 (Glass Debt) without_skill preserves Strait/Velvet-Noose/patrol-break keywords (weak content pass) but invents Admiralty conspiracy + enchanted munitions as fact — guardrail/quality still discriminate.
- Template-heading structure alone is a weak discriminator (baseline often copies headings). Process + guardrail assertions carry the skill delta.
- Timing/tokens are inline-executor estimates (total_tokens null). Graders scored output template conformance, not vault lint-clean. No live wiki writes; no SKILL.md edits.

