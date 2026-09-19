# EVAL_AUTHOR_FLAGS — place-design post-#156 thin VERIFY

Re-scored on `evals/thin-place-pr156` against thinned skill @ `83d6043` / main `442e36d` (#156). Soft lint / vault completeness out of scope. Success bar: with_skill mean **1.000** — **HIT**.

**CoS recommendation: KEEP #156**

Workspace: `.agents/skills/place-design-workspace/iteration-1/`
Skill: `.agents/skills/place-design/` (SKILL.md **not** edited this run; thin form already merged)
Live wiki: **not** edited; outputs under workspace only.

## New from this verify

- **Post-merge thin verify** after #156 moved craft to `references/place-craft.md` while keeping refuse-gates in SKILL (~117 lines).
- with_skill mean **1.000** (all 14 evals 100%); without_skill mean **0.084**.
- with_skill executors followed SKILL and loaded `references/place-craft.md` (plus sibling refs when build steps required). Thinning did **not regress** the suite gate.

- **No Author-blocking with_skill failures.**

## Discriminating (keep)

- Resist-invent southern dungeon/neighbor as canon (eval-2).
- invention: true on from-scratch (eval-3).
- Kernel + work gate with durable locus (evals 1, 3, 4).
- Five-part location moves positive shape (eval-10).
- Cardinal Where + south gap + no south proper name (eval-14).
- Craft evals 5–9, 11–13 (kernel/topology/clues/obstacle/factions/high-tier/ruin/planar).

## Non-discriminating / soft

- Template structure with some fill (evals 1, 3, 4): without_skill can still clear the substance floor — discrimination remains in process / guardrail / content.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch other worktrees. Suite evals.json not edited.
