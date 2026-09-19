# EVAL_AUTHOR_FLAGS — npc-design Batch A re-score (post-#145)

Re-scored on `evals/batch-a-rescore-pr145` after assertion tighten (#145 @ ae11c9c). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

Workspace: `.agents/skills/npc-design-workspace/iteration-1/`
Skill: `.agents/skills/npc-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Graders score **output** template conformance + process locus (not vault lint / live-page shape).

## New from this re-score

- **No new Author-blocking failures** on with_skill (53/53).
- **Durable process locus** (process-notes.md / transcript.md): with_skill satisfies function/role framing + work gate (evals 1–3) and grounding/contradictions (eval-2); without_skill omits. Graders must read those artifacts, not only the page file.
- **Eval-1 content compound** (specific Varn signals + role enum + craft-in-body): without_skill drops from prior soft pass to fail when YAML `role` stays `"Inner lock keeper"`. Keep compound; it now discriminates.
- **Eval-1 labeled leverage AND need**: without_skill fails; with_skill passes via Design notes. Keep.
- **Eval-4 specific Velvet Noose canon**: with_skill 1.0; without can scrape partial broker text but still fails overall (1/6). Keep specificity; do not rely on vague "broker" alone.
- **Eval-5 present-tense scene signal**: #145 wording kills baseline biography-flavor scrape (without 0/3). Keep.

## Discriminating (keep)

1. **Eval-2 resist-invent guardrails** — strongest template-suite delta (1.0 vs 0.0). Hostile Crown-betrayal-as-canon prompt cleanly separates skill from baseline. Keep.
2. **Craft evals 5–14 anti-pattern refusals** — all 1.0 vs 0.0. Main discrimination engine. Keep as written.
3. **Process: function/role framing + work gate** (evals 1, 3) with durable locus — baseline skips; skill passes.
4. **Role enum correction (eval-1)** — catches leaving `role: "Inner lock keeper"`. Keep.
5. **Eval-3 `invention: true`** — discriminating; baseline presented Kell as accepted without label.
6. **Eval-4 canon vs invention split** — catches silent long biography + invalid role string.

## Non-discriminating / soft

| Assertion locus | Issue |
| --- | --- |
| Eval-1 structure+substance floor | without_skill can still clear headings+copied canon signals (1/7). Useful floor; weak alone. |
| Eval-4 "Preserves specific Velvet Noose…" | without may keep some stub facts while inventing biography — keep paired with role/structure/guardrails. |

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `process-notes.md` / `transcript.md` are required outputs of the executor. This re-score wrote both under template evals' `outputs/`.

## Non-issues / do not inflate

- Do **not** add assertions that live `varn.md` / `mave-sorn.md` already fill every template section — grade the **output**.
- Do **not** edit production SKILL.md or live wiki based on this run.
- Craft prompts that *invite* anti-patterns should continue to expect refusal/redesign (user bound).

## Suite health (this re-score)

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 7 | 7/7 | 1/7 | Process + role enum + labeled lev/need |
| 2 resist-invent | 4 | 4/4 | 0/4 | Primary template guardrail |
| 3 from-scratch | 6 | 6/6 | 0/6 | Invention label + template + role |
| 4 flesh | 6 | 6/6 | 1/6 | Specific canon + structure/guardrails |
| 5 incidental | 3 | 3/3 | 0/3 | Scene-signal tighten works |
| 6 no lore-dump | 3 | 3/3 | 0/3 | Strong |
| 7 persuasion | 3 | 3/3 | 0/3 | Strong |
| 8 limited ally | 3 | 3/3 | 0/3 | Strong |
| 9 redundant clues | 3 | 3/3 | 0/3 | Strong |
| 10 no cutscene | 3 | 3/3 | 0/3 | Strong |
| 11 rare betrayal | 3 | 3/3 | 0/3 | Strong |
| 12 active plan | 3 | 3/3 | 0/3 | Strong |
| 13 no PC sheet | 3 | 3/3 | 0/3 | Strong |
| 14 no forced redemption | 3 | 3/3 | 0/3 | Strong |

**Totals:** with_skill 53/53; without_skill 2/53.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / main.
