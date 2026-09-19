# Benchmark — spell-design iteration-1 (Batch B RE-SCORE)

Branch worktree: `/home/box/wt-batch-b-rescore` (`evals/batch-b-rescore-pr149`).
Post-#149+#148: spell suite now **9** evals (was 4). Pattern: skill-creator with_skill vs without_skill → grade → aggregate.
Bounds held: no SKILL.md edits; no live wiki writes; no `wiki/entities/spell/` seeding; fixtures labeled non-canon; spell-scroll items ≠ type:spell pages.

## Aggregate

| Configuration | Mean pass rate | Stddev | Mean duration (s) | Mean tokens |
| --- | ---: | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 106.7 | n/a |
| without_skill | 0.026 | 0.049 | 51.8 | n/a |
| **delta** | **+97.4%** (pp) | — | +106.0% | n/a |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| spell-scroll-*-improve | 9/9 (1.000) | 1/9 (0.111) |
| create-a-spell-that | 5/5 (1.000) | 0/5 (0.000) |
| ledgerbind-from-scratch | 8/8 (1.000) | 1/8 (0.125) |
| fixture-flesh | 8/8 (1.000) | 0/8 (0.000) |
| design-a-cantrip-that | 4/4 (1.000) | 0/4 (0.000) |
| write-a-spell-whose | 4/4 (1.000) | 0/4 (0.000) |
| copy-a-wizards-of | 4/4 (1.000) | 0/4 (0.000) |
| target-resist-invent | 4/4 (1.000) | 0/4 (0.000) |
| target-resist-invent | 4/4 (1.000) | 0/4 (0.000) |

## Analyst observations

- With-skill passes 100% of assertions across all nine evals; without-skill mean pass rate ~0.0262 — discriminating delta (+97.4 pp) driven by process evidence locus, invention labeling, scroll≠spell guardrail, resist-invent/balance/climax/IP/narration/work-gate refusals.
- New adversarial suite (evals 5–9 from #148 uplift) all discriminate: unbalanced cantrip, climax auto-win, PHB verbatim paste, secrets-in-narration, silent-canon skip-work-gate.
- Eval 2 (ancient-druids / Taking-origin as Current Truth) remains a sharp discriminator: with_skill 5/5, without_skill 0/5.
- Eval 1 structure bar tightened (#149): without_skill now fails filled-narration + runnable substance (was soft pass on casting headings alone in pre-tighten run).
- Eval 4 stub-premise soft alone mitigated: without_skill fails explicit fixture-vs-invention callout and new Taking-on-Aruhe-not-caused-by-spell assertion.
- Eval 3 casting-field presence alone still soft-passes without_skill; runnable-effect quality assertion carries discrimination — keep both.
- Fixtures correctly treated as labeled work drafts — no wiki/entities/spell/ folder created; outputs only under workspace */outputs/.
- Tokens unavailable (timing.total_tokens null; inline-executor). Duration: with_skill mean ~106.7s vs without ~51.8s (~+106.0%) — extra cost is process notes + refusal/redesign briefs.
- Process assertions need process-notes.md (or transcript) as evidence locus — same Batch A/B author flag; #149 text now cites that locus explicitly.
