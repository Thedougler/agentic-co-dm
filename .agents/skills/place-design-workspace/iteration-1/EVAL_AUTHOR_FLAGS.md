# EVAL_AUTHOR_FLAGS — place-design Batch A re-score (post-#145)

Re-scored on `evals/batch-a-rescore-pr145` after assertion tighten (#145 @ ae11c9c). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## New from this re-score

- **No new Author-blocking failures** on with_skill (all 14 evals 100%).
- **Eval-10 five-part moves** (tightened): with_skill 3/3; without_skill 0/3. Negation-only baseline ("No lasting change to routes…") correctly fails the positive five-part shape assert. Keep post-#145 wording.
- **Eval-14 Where discipline** (tightened): with_skill 4/4; without_skill 0/4. Explicit `**North:**`/`**East:**`/`**South:**`/`**West:**` + travel-day language + "only three known neighbors wikilinked; south has neither wikilink nor proper name" now fully discriminate. Prior non-discriminating structure asserts from pre-#145 run are resolved — **withdraw prior eval-14 author flags**.
- **Durable process locus** (process-notes.md / transcript.md): with_skill satisfies kernel/work gate on evals 1–4; without_skill omits them.

## Discriminating (keep)

- **Resist-invent southern dungeon/neighbor as canon** (eval-2): sharp (1.0 vs 0.25). Keep hostile prompt.
- **invention: true on from-scratch** (eval-3).
- **Kernel + work gate** with durable locus (evals 1, 3, 4).
- **Five-part location moves** positive shape (eval-10) — keep.
- **Cardinal Where + south gap + no south proper name** (eval-14) — keep tightened form.
- Craft evals **5–9, 11–13** (kernel/topology/clues/obstacle/factions/high-tier/ruin/planar): all discriminate 1.0 vs 0.0. Keep.

## Non-discriminating / soft

- **Template structure with some fill** (evals 1, 3, 4): without_skill can still clear the substance floor when headings are visible and partially filled. Useful as a floor, weak alone — discrimination remains in process / guardrail / content.
- **Frontmatter type:place** when prompt names `wiki/templates/place.md` (weak alone).

## Withdrawn flags (pre-#145)

The following pre-#145 EVAL_AUTHOR_FLAGS for eval-14 (cardinal presence, weak wikilink+days, bare `## Where`) and the eval-10 negation false-positive note are **addressed by #145 wording** and confirmed discriminating on this re-score. No remaining Author action required for those.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / main.
