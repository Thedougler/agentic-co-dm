---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-07-23"
tags: [craft]
summary: "Reuse per-PC matchups already proven engaging via dndsim, reflavor them to the DM's scene, then simulate and tune the group toward the DM's stated intention."
phase: any
uid: 396b8130-e453-477c-9e91-2c0118126a59
---

# Encounter-tuning runbook (any DM-intent encounter build)

Ties `encounter-prep`, `.claude/skills/draft-content/references/monster.md`, `combat-profiles`, and the
`dndsim` CLI together for one operation none of them owns end to end:
find matchups already proven mechanically engaging for specific PCs,
reflavor them to fit the DM's scene, group them into an encounter, and tune
the whole set until a real Monte-Carlo simulation matches what the DM
actually wants, not just what the XP-budget table says. Orchestrates and
cites each skill's own procedure without restating it (`.claude/rules/docs.md`
§ DRY).

## GATE: precondition

Party character sheets exist and are current under
`vault/campaigns/shattered-sea/pcs/character-sheets/*-sheet.md` (the `## Combatant
Block` `sim:` fence is the actual simulation input). Missing or stale →
build/refresh them first via `.claude/skills/combat-profiles/SKILL.md`'s
own Workflow before continuing.

Spell effects are not modeled. The engine's spell library reads a
` ```spell ` fence, which is a retired pattern — no `vault/srd/spells/` page
carries one and none will be back-filled — so a sheet's
`sim.spellcasting.known:` list contributes nothing to a simulated number.
Read every tuning result as a floor for a caster-heavy party and record that
in § Calibration; never tune the encounter harder to compensate for a
gap the model has rather than the party.

A DM-stated intention exists: a target difficulty band (Easy/Medium/Hard/
Deadly) and/or specific numeric goals (win probability, P(≥1 down), P(TPK),
etc.). No stated intention → this is plain encounter authoring, not tuning;
hand the whole request to `.claude/skills/encounter-prep/SKILL.md`
instead.

## 1. Find matchups already proven mechanically engaging, per PC

The reuse target isn't "closest CR"; it's a matchup already proven
challenging and fun for a specific PC. For each PC the DM wants spotlighted
this encounter, read (or run fresh) that PC's `--sweep-corpus` sweep: the
band-filtered, win%-ascending appendix. This drops Trivial and Deadly-at-≥50%-win
cells using dndsim's own "designable encounters" filter (cited from
`utils/dndsim/CLAUDE.md`, not re-derived) surfaces exactly the
Hard/Medium/deadly-but-winnable opponents that already make a genuinely
engaging 1-on-1 for that PC. The top rows are the candidates.

A different PC will often surface a different creature; expect that,
not a problem to normalize away. It's the point of going PC-by-PC instead
of picking one roster for the party as an average.

Fall back to grepping `vault/srd/monsters/`, `vault/campaigns/shattered-sea/monsters/`
frontmatter (`cr:`, `type:`) or `npm run search:content` only when no PC
has sim history yet (GATE not met) or the DM already wants a specific
narrative creature regardless of sim history.

## 2. Reflavor to the DM's scene

Among a PC's candidate matchups from step 1, pick whichever's mechanical
shape is closest to (or cheapest to reskin into) what the DM's scene/
context/story calls for. Reflavor via
`vault/refs/vault/monster/references/reskin-templates.md`'s own
convention (cited, not restated): same stats, new name/type/flavor text.
The mechanics stay the proven-fun matchup; only the fictional dressing
changes to fit the moment.

Cite `.claude/skills/draft-content/references/monster.md`'s reused-vs-one-off interview
question and its Recurrence Fork hard rule for whether the reflavored
creature gets its own page (reusable beyond this encounter) or stays
inline on the encounter page as a true one-off. Don't re-derive either
rule here.

## 3. Compose the roster

**Bottom-up** (the common case for this runbook): the roster is simply the
set of reflavored creatures chosen in step 2, one per spotlighted PC,
flavored as a cohesive set for the scene. Group them as a set; don't just
concatenate independent picks. Combining several individually-hard 1-on-1s
does not sum to "hard for the party"; that's exactly what step 4's
whole-group simulation and step 5's re-tune are for.

**Top-down** (the DM already has a roster concept in mind): hand off to
`.claude/skills/encounter-prep/SKILL.md` for composition, action
economy, and the Encounter Type Router; steps 1-2 above become the lookup
for filling one roster slot rather than the primary method.

Either way, a composition/action-economy sanity pass belongs to
`encounter-prep`'s own process, cited but not restated.

## 4. Simulate the encounter

`npm run dndsim -- sim-combat <party sheets...> <creature file(s)...> --goals <file.yaml>`
for a goal-scored run, or the validation-only invocation in
`.claude/skills/encounter-prep/references/combat-calibration.md` §
Encounter validation sim for a quick check before a goals file exists.
`npm run dndsim -- sim-combat party <monster.md> --sweep-count` answers "how many of this
monster." `utils/dndsim/CLAUDE.md` is the sole CLI/schema
source of truth. Don't restate any flag table.

## 5. Read the result against the DM's intention

The Effective Difficulty Rating, the Effective CR scalar, and (if you used
`--goals`) the MET/MISSED table are the signal. Compare directly
against what the DM stated at the GATE. Built bottom-up (step 3), expect
the whole-group result to run hotter than any individual matchup. That's
not a design failure. It's why this step exists. Step 4's run already
carries a default difficulty-drivers + difficulty-ladder pass (one tuned
variant per band: easy/medium/hard/deadly-achievable/TPK-inducing, not
just hard). Read the rows in
`utils/dndsim/CLAUDE.md` § Difficulty ladder
before doing anything manual in step 6; the ladder row for the DM's
stated target band already shows the delta needed. A miss is what step 6
exists to fix. A match ends the loop at step 7.

## 6. Tune via mutation, only if composition or count change isn't the fix

The default difficulty ladder from step 4/5 already covers the common
case (one GA run per band, no goals file needed, wall-clock budgeted via
`--budget-ms`). Reach for a manual
`--evolve --goals <file.yaml> --emit-statblock <path>` run instead only
when that default isn't enough. Use it for a custom target outside the 5 canned
bands, several distinct enemies (`--evolve-target <name>` to
disambiguate the difficulty ladder, which skips these as ambiguous), or a
deeper/slower search than the default budget allows. The same generational
search tunes the creature's knobs
(AC, HP, to-hit, save DC, flat damage, damage-die count,
multiattack, recharge, legendary counts), clamped and deterministic per seed
(`utils/dndsim/CLAUDE.md` § Evolve mode).

**Corpus-integrity guard**: `vault/srd/monsters/` and `vault/campaigns/shattered-sea/monsters/`
are also `--sweep-corpus`'s default simulation corpus. `--emit-statblock` may only overwrite a page
that is *this encounter's own* homebrew/reskinned creature. A RAW/SRD or
otherwise shared/reused creature (anything with a `source_url`/
`source` pointing at SRD material, or already used by other
encounters) emits to a **new** page instead. Follow
`vault/refs/vault/monster/references/reskin-templates.md`'s own
variant-naming convention. Don't invent a new one. Silently overwriting a
shared reference page would corrupt every future `--sweep-corpus`/
`--sweep-count` that depends on it. The same protection covers
`vault/srd/spells/` pages: a spell page is shared reference that every caster
in the corpus reads. Never silently edit one to tune a single encounter.

`utils/dndsim/`'s own evolve/tune path enforces the identical guard: it
refuses to write over a page carrying `source_url`/`source`
frontmatter, same rationale that governs this runbook's own dndsim
invocations.

Sanity-check the emitted deltas against the creature's fiction before
adopting them. Cite
`.claude/skills/combat-profiles/references/simulation.md`'s existing
evolve guidance rather than restating it; a numerically-optimal statblock
that no longer reads as the same monster is still the DM's call to reject.

## 7. Re-simulate and record

Confirm the goals are now met, then paste the `[simulated]` result (win %,
P(≥1 down), P(TPK), Effective Difficulty Rating, Effective CR scalar, seed)
into the encounter page's `## Challenge Calibration` section, per
`.claude/skills/encounter-prep/references/combat-calibration.md`'s own convention (cited, not restated).

Done = Challenge Calibration reflects a simulated result matching the DM's
stated intention; any emitted statblock variant is its own committed page,
never an overwritten shared corpus file; place the goals file (if used)
beside the sim command per combat-profiles' Hard Rule 9; commit
`prep: encounter-tuning — <encounter slug> — <what changed>`.
