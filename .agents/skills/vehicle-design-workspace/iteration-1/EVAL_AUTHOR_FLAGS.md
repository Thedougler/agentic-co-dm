# EVAL_AUTHOR_FLAGS — vehicle-design Batch B run

Flags from grading + analyst pass. Soft lint / vault completeness correctly out of scope.
Workspace: `.agents/skills/vehicle-design-workspace/iteration-1/` (worktree `/home/box/wt-batch-b-spell`, branch `evals/batch-b-run-pr140`).

## Pass rates (this run)

| Config | mean pass rate |
| --- | ---: |
| with_skill | **1.000** |
| without_skill | **0.201** |
| delta | **+79.9%** |

| Eval | with | without |
| --- | ---: | ---: |
| uncertainty-improve | 8/8 | 1/8 |
| uncertainty-resist-invent | 5/5 | 0/5 |
| cobalt-receipt-from-scratch | 8/8 | 2/8 |
| glass-debt-flesh | 7/7 | 3/7 |

## Discriminating (keep)

- **Resist-invent hidden cannons / ram / enchanted sails as canon** (eval-2): strongest discriminator (1.0 vs 0.0). Keep hostile prompt wording.
- **Unknown honesty on improve** (eval-1 guardrails): baseline fills speed/weapons/helm/movement/DT as silent canon — keep "Unknown or labeled invention" wording.
- **invention: true on from-scratch** (eval-3): baseline claims vault canon / omits flag; keep.
- **Established vs invention split on flesh** (eval-4): baseline invents Admiralty conspiracy + enchanted munitions; keep guardrail.
- **Identity sentence / work gate** (process): discriminate when `process-notes.md` is required evidence. Document that graders must read process-notes, not only the page file.
- **Thunk cannon credit ≠ Weapons row** (eval-1 content/guardrail): keep — baseline promotes credit into sheeted battery.

## Non-discriminating / soft

- **Template structure headings present** (evals 1,3,4): both configs often pass if `wiki/templates/vehicle.md` is visible. Useful as a floor assertion, but alone does not prove skill adherence. Consider requiring specific content (e.g. Hull AC/HP/DT all numeric or Unknown; Handling route choices named).
- **Frontmatter type:vehicle + kind** on flesh/from-scratch: weak when the prompt names the template — baseline can copy frontmatter without the skill. Pair with process/guardrail (already done).
- **Eval-4 content preservation** (Strait / Crown patrol break / velvet-noose): baseline still mentioned all three while inventing conspiracy — soft pass. Tighten to require **no conspiracy reframing** or "patrol break remains unexplained / sighting-only" for sharper discrimination.

## Flaky / evidence-dependent

- **Identity sentence appears before the page draft**: fails if executor forgets `process-notes.md` even when skill was followed. **Assertion text should cite process-notes (or transcript) as the evidence locus.**
- **Shows a chat proposal / work gate before writing under wiki/**: same — needs process artifact. Clarify: "chat proposal before any live `wiki/` path write; workspace outputs allowed."

## Bad / strengthen

- Eval-1 content preservation assertion is long/compound (Surety + AC/HP + six crew + Calveno berth + Aruhe + Ordinance). Prefer splitting into 2–3 assertions so a partial miss does not all-or-nothing — or keep compound but document that **any** major omission fails.
- Eval-3 structure-only pass on without_skill is noisy; require Combat omit-reason or body-scale access sentence for sharper structure discrimination.
- Eval-4 quality assertion ("not ship-of-the-line reskin") worked; keep. Optional: add negative check "no enchanted sails / rocket battery / Admiralty conspiracy as fact."

## Bounds held

- No SKILL.md edits.
- No live wiki writes (no Cobalt Receipt page filed; Uncertainty / Glass Debt live pages untouched).
- Outputs only under vehicle-design-workspace; Batch A untouched.
- Graders scored **output template conformance**, not vault lint-clean.
