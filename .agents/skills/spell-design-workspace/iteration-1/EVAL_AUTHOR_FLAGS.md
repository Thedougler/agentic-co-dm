# EVAL_AUTHOR_FLAGS — spell-design Batch B iteration-1

Flags from grading + analyst pass. Soft lint / vault completeness out of scope.
Fixtures are labeled work drafts — **not** vault canon. There is no `wiki/entities/spell/` folder.

## Discriminating (keep)

- **Resist invent ancient-druids / Taking-origin spell as canon** (eval-2): strongest discriminator (1.0 vs 0.0). Keep hostile prompt wording that demands Current Truth provenance.
- **spell-scroll items are not type:spell exemplars** (evals 1, 3, 4 guardrails): baseline repeatedly cites `wiki/entities/item/spell-scroll-*.md`. Keep explicit negative assertions.
- **invention: true / proposed labeling** on from-scratch + fixture material adds (evals 1, 3, 4): baseline files as silent canon or omits labels.
- **Runnable 2024 effect** (eval-1 quality; eval-3 quality): baseline vague obscurement / "protects the document" fails when assertion requires saves/checks, end conditions, scaling.
- **No Taking-on-Aruhe metaphysics bleed** (eval-4): baseline promotes undeclared Umberlee+Taking doctrine as Current Truth. Keep.

## Non-discriminating / soft

- **Template casting-field presence** (Casting Time/Range/Components/Duration filled): eval-3 without_skill passed this alone. Keep as floor but do not treat as skill proof — pair with runnable-effect quality assertion (already present).
- **Stub premise preservation** (eval-4 content): both configs kept 3rd-level necromancy / drowning-mark summary. Guardrails carry discrimination; consider requiring fixture-vs-invention callout as its own scored artifact.
- **Bare structure headings** when `wiki/templates/spell.md` is visible in-repo: baseline can skim headings without skill procedure.

## Flaky / evidence-dependent

- **Identity sentence before page draft** / **chat proposal work gate**: pass only when `process-notes.md` (or transcript) exists. **Assertion text should cite process-notes/transcript as evidence locus** so graders do not hunt the page file. Workspace outputs must not count as live `wiki/` writes.

## Bad / strengthen

- Eval-1 structure assertion can pass thin casting blocks; optionally require narration callout `> [!narration]` explicitly in the assertion text.
- Eval-3 "filled in 2024 terms" is satisfied by labels without peer-anchored numbers — already mitigated by runnable-effect quality assertion; keep both.
- Eval-4 Discovery/Lore quality assertion is fine; optionally require a negative check that Taking-on-Aruhe is **not** explained by the spell (already partially covered by guardrail).

## Retarget / path judgment

- Improve/flesh subjects are **prompt fixtures** (Saltwake Veil, Red Wake Knell), not live pages — do not grade vault completeness.
- Durable path proposals may use `wiki/<campaign>/spells/` (SKILL) or discuss `wiki/entities/` siblings; do **not** hard-fail path choice until campaign convention is decided — assert work gate + `type: spell` + template shape instead.
- Never treat spell-scroll item pages as the spell being authored.

## Stop

Awaiting CoS / parent before optimize. Workspace: `.agents/skills/spell-design-workspace/iteration-1/` under `/home/box/wt-batch-b-spell`.
