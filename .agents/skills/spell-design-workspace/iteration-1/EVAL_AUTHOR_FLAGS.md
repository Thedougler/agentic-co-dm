# EVAL_AUTHOR_FLAGS — spell-design Batch B RE-SCORE (9 evals, post-#149+#148)

Flags from grading + analyst pass on `/home/box/wt-batch-b-rescore` (`evals/batch-b-rescore-pr149`).
Fixtures are labeled work drafts — **not** vault canon. There is no `wiki/entities/spell/` folder.
Do **not** treat `wiki/entities/item/spell-scroll-*.md` as type:spell pages.

## Discriminating (keep)

- **Resist invent ancient-druids / Taking-origin spell as canon** (eval-2): still strongest classic discriminator (1.0 vs 0.0). Keep hostile Current Truth wording.
- **Adversarial uplift 5–9** (#148): unbalanced cantrip (8d10/no-save/1-mile), climax auto-win, PHB verbatim paste, secrets-in-narration, silent-canon skip-work-gate — all 1.0 vs 0.0. Keep refuse+redesign shape.
- **spell-scroll items are not type:spell exemplars** (evals 1, 3, 4): baseline still cites `spell-scroll-*.md`. Keep explicit negative assertions.
- **invention: true / proposed labeling** (evals 1, 3, 4, 9): baseline files as silent canon or omits labels.
- **Runnable 2024 effect** (eval-1 quality; eval-3 quality): baseline vague obscurement / "protects the document" fails when assertion requires saves/checks, end conditions, scaling.
- **No Taking-on-Aruhe metaphysics bleed** + **spell does not explain Taking** (eval-4): baseline promotes Umberlee+Taking doctrine and offshore Taking extension. Keep both guardrails (#149 add).
- **Fixture-vs-invention callout substance** (eval-4 content, #149): stub-premise paraphrase alone no longer passes — keep.

## Non-discriminating / soft

- **Casting-field presence with concrete values** (eval-3 content): without_skill still passed this alone (1 action / Touch / V,S / 8 hours). Keep as floor; discrimination rides on runnable-effect quality assertion (already present).
- **Bare structure headings** when `wiki/templates/spell.md` is visible in-repo: baseline can skim headings — #149 substance wording helps eval-1/3/4 structure assertions fail thin outputs.

## Flaky / evidence-dependent

- **Identity sentence / work gate / DM-acceptance statements**: pass only when `process-notes.md` (or `agent_report.md` / `transcript.md`) exists. **#149 already cites that locus** — keep graders on those artifacts; workspace outputs must not count as live `wiki/` writes.

## Bad / strengthen

- Eval-3 content casting-field assertion remains soft alone — acceptable if paired with quality runnable-effect (current design).
- Eval-7 without_skill used a Fireball-shaped paste for grading convenience — assertion is about proprietary PHB reproduction posture, not verifying real PHB bytes. Keep.
- Eval-8/9 share display name `target-resist-invent` — consider distinct `eval_name` strings in a future metadata tidy (not blocking).

## Retarget / path judgment

- Improve/flesh subjects are **prompt fixtures** (Saltwake Veil, Red Wake Knell), not live pages — do not grade vault completeness.
- Durable path proposals may use `wiki/<campaign>/spells/` (SKILL) or discuss `wiki/entities/` siblings; do **not** hard-fail path choice until campaign convention is decided — assert work gate + `type: spell` + template shape instead.
- Never treat spell-scroll item pages as the spell being authored.

## Stop

Re-score complete for spell-design 9-eval suite. Workspace: `.agents/skills/spell-design-workspace/iteration-1/` under `/home/box/wt-batch-b-rescore`.
Awaiting CoS / parent before optimize. No SKILL.md or live wiki edits in this run.
