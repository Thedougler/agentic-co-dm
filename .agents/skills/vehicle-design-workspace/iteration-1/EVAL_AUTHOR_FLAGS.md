# EVAL_AUTHOR_FLAGS — vehicle-design Batch B re-score (post-#149+#148)

Re-scored on `evals/batch-b-rescore-pr149` after assertion tighten (#149 @ 6d53ff9) and quality-bar uplift (#148 @ d3f2f04). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

Workspace: `.agents/skills/vehicle-design-workspace/iteration-1/` (worktree `/home/box/wt-batch-b-rescore`)
Skill: `.agents/skills/vehicle-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Graders score **output** template conformance + process locus (not vault lint / live-page shape).

## Pass rates (this re-score)

| Config | mean pass rate |
| --- | ---: |
| with_skill | **1.000** (50/50) |
| without_skill | **0.057** (4/50) |
| delta | **+94.3%** |

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 10 | 10/10 | 1/10 | Split content + process locus + structure substance |
| 2 resist-invent (armament) | 5 | 5/5 | 0/5 | Primary template guardrail |
| 3 from-scratch | 8 | 8/8 | 1/8 | invention:true + body-scale / Combat omit |
| 4 flesh | 7 | 7/7 | 2/7 | No-conspiracy reframing tighten works |
| 5 one-line ferry | 4 | 4/4 | 0/4 | Durable-gate refusal |
| 6 resist-invent (dreadnought) | 4 | 4/4 | 0/4 | Overwrite refusal |
| 7 fill Unknowns | 4 | 4/4 | 0/4 | Unknown honesty |
| 8 PC authorship | 4 | 4/4 | 0/4 | Contingencies not outcomes |
| 9 silent merge | 4 | 4/4 | 0/4 | Work gate + open questions |

**Totals:** with_skill 50/50; without_skill 4/50.

## New from this re-score

- **No new Author-blocking failures** on with_skill (50/50).
- **Suite grew 4 → 9** via #148 adversarial craft evals (5–9); all five are perfect discriminators (1.0 vs 0.0).
- **#149 durable process locus** (process-notes.md / agent_report.md / transcript.md): with_skill satisfies identity + work gate; without omits. Graders must read those artifacts.
- **Eval-1 content split** (Surety/AC-HP · crew/berth · Aruhe/Ordinance/Thunk≠Weapons): with still 10/10; without failure locality improved (no longer one compound all-or-nothing).
- **Eval-4 conspiracy reframing ban**: without that explains patrol break as Admiralty doctrine now **fails** content (prior soft keyword pass closed). Keep wording.
- **Eval-3 structure+substance**: empty copied headings no longer clear structure; without 1/8.

## Discriminating (keep)

1. **Eval-2 resist-invent hidden cannons / ram / enchanted sails** — strongest template delta (1.0 vs 0.0). Keep hostile prompt.
2. **Craft evals 5–9 anti-pattern refusals** — all 1.0 vs 0.0. Main discrimination engine post-#148. Keep as written.
3. **Unknown honesty** (evals 1, 7) + **Thunk credit ≠ Weapons** — baseline fills silent canon / promotes credit to battery.
4. **invention: true** (eval-3) — baseline claims vault canon.
5. **Eval-4 established vs invention + no conspiracy/enchanted munitions** — #149 tighten discriminates.
6. **Process: identity sentence + work gate** with durable locus (evals 1, 3, 4, 7, 9).

## Non-discriminating / soft

| Assertion locus | Issue |
| --- | --- |
| Eval-1/3/4 structure floor | without can still clear some filled headings when it invents freely (eval-1 structure 1/10; eval-4 structure+frontmatter 2/7). Useful floor; weak alone — already paired with guardrails. |
| Frontmatter type:vehicle + kind | Weak when prompt names template; keep paired with process/guardrail. |

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `process-notes.md` / `transcript.md` are required executor outputs. This re-score wrote them under template + craft evals' `outputs/`.

## Non-issues / do not inflate

- Do **not** add assertions that live `Uncertainty.md` / `glass-debt.md` already fill every template section — grade the **output**.
- Do **not** edit production SKILL.md or live wiki based on this run.
- Craft prompts that *invite* anti-patterns should continue to expect refusal/redesign (user bound).
- Do **not** soften eval-4 to accept conspiracy reframing if keywords remain.

## Bounds held

- No SKILL.md edits.
- No live wiki writes (no Cobalt Receipt filed; Uncertainty / Glass Debt / Velvet Noose live pages untouched; no silent delete).
- Outputs only under `vehicle-design-workspace/iteration-1/*/{with,without}_skill/outputs/`.
- Batch A untouched. Main not checked out.
- Graders scored **output template conformance** + process locus, not vault lint-clean.
