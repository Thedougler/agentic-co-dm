# Quality guidance, mapped onto the template

`vault/_templates/_campaigns/_encounter.md`'s headings are fixed; this maps what each one
needs beyond the template's own one-line prompt. The Toy table goes under
the opening brief, before `## Enemy Roster`.

No encounter-specific frontmatter keys (the npc guide's established reasoning:
a second YAML copy of prose fields is sync-drift risk with no
machine-readable payoff). One table, under the opening brief.

- `## Enemy Roster` — names, stat block refs or citations, and each
  creature's role: ambusher, artillery, bruiser, controller, defender,
  leader, skirmisher (`vault/refs/vault/monster/references/cr-design.md`
  §2 for stat priority; `.claude/skills/encounter-prep/references/running-the-encounter.md` § Role
  placement and tactics for where it stands and how it plays once combat
  starts). Pick the roster's composition shape — solo, matched group, or
  boss+minions — and respect the ≤3-creature-type cap (Hard Rule 6) via
  `.claude/skills/encounter-prep/references/encounter-composition.md` §§ 1–2, 4. Named recurring foes
  and reusable creatures: wikilink + quote from their own page (`.claude/skills/draft-content/references/npc.md`
  or `.claude/skills/draft-content/references/monster.md`), not restated stats. One-off creature, no page:
  `vault/refs/vault/monster/references/cr-design.md` for design,
  `vault/refs/vault/monster/references/statblock-format.md` for the codeblock.
- `## Challenge Calibration` (combat) or `## Skill Track` (skill
  challenge) — `.claude/skills/encounter-prep/references/combat-calibration.md`'s procedure, pasted
  with evidence and a confidence label. No `combat-profiles` data yet, or
  want a fast sanity check first? `.claude/skills/encounter-prep/references/encounter-composition.md`
  §§ 8–9 (the SRD XP-budget table and the Lazy Encounter Benchmark
  formula) are concrete standard baselines — empirical evidence still
  wins once it exists (Hard Rule 4).
- `## Terrain` — draw from `.claude/skills/encounter-prep/references/encounter-composition.md` §§ 3, 6–7:
  the nine-element set-piece checklist (zone effects, traps/hazards,
  positions, objects, cover, terrain, goal — pick what fits, not all of
  it), zone-based terrain definition (1–3 named zones), and Gameplay
  Toolbox's combat features (elevation, defensive positions, reasons to
  move) and trap-writing shape. 2–3 features minimum, each with a stated
  mechanical effect — decorative-only terrain doesn't count.
- `## Tactical Notes` — opening move, escalation, and morale/retreat
  threshold, drawing from `.claude/skills/encounter-prep/references/running-the-encounter.md` §§ 1–2,
  10: role placement, this encounter's tactical personality (an
  instance-level pick, not baked into the creature's own page), and
  flee/surrender/reinforcement-wave options.
- `## Run Sheet` — the operational section, not a restatement of Tactical
  Notes: a foe roster tracker table (one row per foe — init, AC, HP, flee
  threshold, one-line action script) and a round script (bold-led
  R1/R2+/trigger bullets),
  drawing from `.claude/skills/encounter-prep/references/running-the-encounter.md` §§ 1–4. Statblocks
  reached by wikilink or `![[page#Heading]]` transclusion at point of use
  — the ownership rule (Hard Rule 11) makes restating them here a defect,
  not a convenience.
- `## Raising the Stakes` — targets the party's weakness (from the
  Challenge Calibration read); tension without unfairness. Each line
  states a trigger condition and a concrete numeric delta (Hard Rule 10's
  numbers discipline binds here too) — draws from
  `.claude/skills/encounter-prep/references/running-the-encounter.md` §3's difficulty dials.
- `## Lowering the Stakes` — plays to the party's strength; lets them feel
  powerful if they find it. Same trigger-plus-numeric-delta shape as
  Raising the Stakes, opposite direction (foes flee, reinforcements
  cancelled, a terrain effect expires).
- `## If They're Stuck` (objective/puzzle-gated encounters only) — the
  three-rung ladder: free tell, costed nudge, fiction-costed bail-out.
  Delete the section for a straight fight with no gate.
- `## Endings` — win condition per phase (if Run Sheet or Challenge
  Calibration names phases), the defeat/TPK aftermath, and the
  disengage/flee outcome, each written concretely — never plot-defense
  phrasing without a paired let-it-happen fallback (Hard Rule 13).
- `## Drama Suite` (social/hybrid, not in the template — add it) — DC
  table (10/15/20), shenanigan offers, plain prose for the DCs that matter.
- `## Stakes` — what changes in the world based on outcome. Specific,
  not generic ("the Guild's shipment is lost" not "consequences occur").
- `## If Ignored` — Hard Rule 7's tick test, made concrete.
- `## Transition` — condition → explicit goto wikilink with elapsed
  in-fiction time; every written branch skip on its own line. Pairs with
  the Dramatic Question
  line in `## Opening`: once play answers the question, summarize and move
  straight here.
