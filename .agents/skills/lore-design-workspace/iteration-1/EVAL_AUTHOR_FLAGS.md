# EVAL_AUTHOR_FLAGS — lore-design Batch A re-score (post-#151)

Re-scored on `evals/batch-a-crl-rescore-pr151` after adversarial uplift (#151 @ 5256033). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## New from this re-score

- **No Author-blocking failures** on with_skill (all 9 evals at 1.0).
- **Suite 4→9** with principle-violation resists (e5–e9). All five new resists discriminate 1.0 vs 0.0.
- **Eval-5 promote Kalowe rumour:** without_skill promotes raiders-for-salvage and deletes Dead Lady / Umberlee; with_skill keeps Accounts≠Current Truth. Keep.
- **Eval-6 Session-11 rewrite:** without_skill inverts fallen/living + Matteo + Western Landing; with_skill surfaces contradictions. Keep hostile wording.
- **Eval-7 fill Limits Unknown:** without_skill erases shaking-tree Unknown; with_skill keeps Open Canon + invention label. Keep.
- **Eval-8 skip-gate pantheon dump:** without_skill silent-files multi-truth cosmology; with_skill enforces work gate + one-question + invention. Keep.
- **Eval-9 Glass Debt Concord:** without_skill mints third concept into Current Truth; with_skill labels proposed only. Keep.

## Discriminating (keep)

- Resist-invent metaphysics as Current Truth (eval-2) — still sharp (1.0 vs 0.2).
- invention:true + vault-harbour negative (eval-3).
- Rumour ≠ Current Truth + Discovery proposed wording (eval-4).
- Heading-form vs callout copy-forward (eval-1).
- New e5–e9 refuse gates — strongest new discriminators.

## Non-discriminating / soft

- Template structure with some fill (evals 3, 4): without_skill can still clear substance floor when headings are visible.
- Eval-1 content/guardrail (fallen-vs-living; no metaphysics) when prompt does not ask to invent — baseline often still passes.

## Flaky / evidence-dependent

- Process asserts require `process-notes.md` / `transcript.md`. This re-score wrote both under each run's `outputs/`.
- `### Limits` under Current Truth (template) vs assertion `## Limits`: graders accept template `### Limits`. Optional polish: align assertion wording.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / main / city or region unfinished runs.
