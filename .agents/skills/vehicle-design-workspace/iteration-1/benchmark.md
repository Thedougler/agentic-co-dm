# Benchmark — vehicle-design iteration 1 (Batch B re-score)

**Re-score after:** #149 + #148 · **evals:** 9
**with_skill mean pass rate:** 1.000  
**without_skill mean pass rate:** 0.057  
**delta:** +94.3%  
**mean duration:** with 107.6s / without 72.6s (+48.2%)

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| uncertainty-improve | 10/10 (1.000) | 1/10 (0.100) |
| uncertainty-resist-invent | 5/5 (1.000) | 0/5 (0.000) |
| cobalt-receipt-from-scratch | 8/8 (1.000) | 1/8 (0.125) |
| glass-debt-flesh | 7/7 (1.000) | 2/7 (0.286) |
| create-a-full-durable | 4/4 (1.000) | 0/4 (0.000) |
| uncertainty-resist-invent-dreadnought | 4/4 (1.000) | 0/4 (0.000) |
| fill-every-unknown-on | 4/4 (1.000) | 0/4 (0.000) |
| on-the-vehicle-page | 4/4 (1.000) | 0/4 (0.000) |
| skip-the-proposal-gate | 4/4 (1.000) | 0/4 (0.000) |

## Analyst observations

- Re-score after #149 assertion tighten + #148 quality-bar uplift; suite now 9 evals (was 4). With-skill passes 100% of assertions across all nine; without-skill mean pass rate ~0.057 — large discriminating delta.
- Craft refusals evals 5–9 are perfect discriminators (all with 1.0 / without 0.0): one-line ferry durable gate, flying dreadnought overwrite, fill-Unknowns silent canon, PC authorship, silent Glass Debt↔Velvet Noose merge.
- Eval-2 resist-invent (hidden cannons/ram/enchanted sails) remains sharpest template-suite discriminator among evals 1–4 (5/5 vs 0/5).
- Eval-1 split content assertions (#149) still pass with_skill 10/10; without fails Surety/crew/Aruhe–Ordinance/Thunk≠Weapons separately (1/10) — split improves failure locality without hurting skill pass.
- Eval-4 #149 no-conspiracy-reframing tighten works: without_skill now fails content preservation (was soft pass when keywords alone counted) by explaining patrol break as Admiralty conspiracy — with 7/7, without 2/7.
- Eval-3 structure+substance + Combat omit-reason / body-scale access: without drops to 1/8 (empty headings + vault-canon claim).
- Durable process locus (process-notes.md) required by #149: with_skill writes identity/work-gate there; without omits. Graders must read process artifacts, not only page files.
- Timing/tokens are inline-executor estimates (total_tokens null). Graders scored output template conformance + process locus, not vault lint-clean. No live wiki writes; no SKILL.md edits; Batch A untouched.
