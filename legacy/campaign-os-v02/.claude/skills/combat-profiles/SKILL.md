---
name: combat-profiles
description: Build or update PC and party combat profiles — simulated DPR, effective HP, save weaknesses, Effective CR Band — in a Campaign OS repo. Use to run the combat sim, refresh a profile after a level-up, or "how hard should this fight be", "what's the party's effective CR". Not the PC's narrative page (dnd5e-character-interview) or encounter design (encounter-prep).
---

# Combat Profiles

This skill produces derived DM intelligence, not wiki content, so the
creative-domain rider and canon-review's oversight don't apply — see
§ Owned paths and § Contract deltas below for exactly which shared-contract
items do.

Replaces generic CR-table assumptions with two things: **script-computed
statistics** (the `utils/dndsim/` Monte-Carlo engine) and this
skill's own **empirical combat data** (real dice, real damage, tracked per
PC). Two output tiers, full shape in `vault/_templates/_campaigns/_pcs/_pc_combat_profile.md` and
`vault/_templates/_campaigns/_pcs/_party_combat_profile.md` (sheet: `vault/_templates/_campaigns/_pcs/_pc_sheet.md`,
tier contents: `references/profiles.md` § Output tiers): the **PC combat
profile** (one per PC) and the **party combat profile** (compiled into the
**Effective CR Band** — `encounter-prep`/`.claude/skills/draft-content/references/monster.md`'s mandatory
difficulty-calibration input).

## Standard queries

```
grep -l "hp_max\|ac:\|class_levels" vault/campaigns/shattered-sea/pcs/*.md
find vault/campaigns/shattered-sea/pcs/combat-profile -maxdepth 1 -name "*-combat-profile.md" 2>/dev/null
ls vault/campaigns/shattered-sea/pcs/combat-profile/party-combat-profile.md 2>/dev/null
ls vault/campaigns/shattered-sea/pcs/combat-profile/loadouts/ 2>/dev/null
```

First query: which PCs exist with frontmatter stats to build from. Second:
does a profile already exist — **update** vs fresh build (Workflow step 1
decides). Third: which loadout files exist. Empty results mean nothing
built yet — proceed to a fresh build.

See `references/governance.md` for owned paths, contract deltas, and the
nine hard rules governing every profile build and update.

## Interview

If the trigger doesn't already specify:

- **Which PC(s)?** (or "the whole party")
- **What triggered this?** Level-up, new session combat data, a specific
  upcoming encounter needing calibration, or a full first-time build?
- **Session number(s)** the new data comes from, if updating.

For a first-time build, also confirm a character sheet exists beyond
`vault/campaigns/shattered-sea/pcs/<name>.md` frontmatter — check
`_assets/character-sheets/{pc-slug}-character-sheet.pdf` first
(`references/data-and-sheets.md` § Character sheet conversion). Neither
exists → build from frontmatter + `## Session Log` alone, mark the block
low-fidelity and the rest `[unknown]` — never block on a missing sheet.

## Workflow

1. **Standard queries** — profile exists and is current (Hard Rule 1)?
   Current → report no-op, stop. Stale or missing → continue.
2. **Interview** (§ above) — gather what's missing.
3. **Attribute pages + Combatant Block** — transcribe the source sheet into
   the four `vault/campaigns/shattered-sea/pcs/` attribute pages (§ Owned paths), then build/update
   `{pc-slug}-sheet.md` per `vault/_templates/_campaigns/_pcs/_pc_sheet.md` — source line,
   `[verify]` flags, and the `## Combatant Block`
   (`references/data-and-sheets.md` § Combatant block), nothing the
   attribute pages already carry. No sheet →
   low-fidelity block from frontmatter, marked.
4. **Declare abilities, author scenario data** (agent judgment —
   `references/simulation.md`): the PC's capabilities (Hex, GWM, Bardic
   Inspiration, Shield...) go in the sheet's Combatant Block `sim.abilities:`
   list — the sim's perfect-play auto-policy decides usage. Loadout files
   (`vault/campaigns/shattered-sea/pcs/combat-profile/loadouts/*.loadouts.yaml`) are now only for
   scenario assumptions, `creature_overrides` (unmodeled statblock prose),
   and named alternate constraint sets; none is required for a default run.
5. **Run per-PC sims** — `npm run dndsim` per `utils/dndsim/CLAUDE.md`;
   record seed + version + command (Hard Rule 9). Also run the PC's default
   screening sweep, `npm run dndsim -- sweep-corpus {pc-slug}` (or the
   sheet's frontmatter `alias:`, e.g. `npm run dndsim -- sweep-corpus pbj`;
   full corpus, additive to the
   closed-form run above, never a replacement) — its
   band-filtered, win%-ascending appendix rows feed § Counters & Synergy
   (Workflow step 7, `references/simulation.md` § Default sweeps).
   Calibrating a specific
   upcoming encounter: translate the DM's qualitative brief into a goals
   YAML and score with `--goals`; tune the statblock toward the goals with
   `--evolve` (`references/simulation.md` § Goals and evolve).
6. **Extract session data**, if updating from a session —
   `references/data-and-sheets.md` § Extraction procedure; append to the
   Session Combat Log (Hard Rule 4), recalculate observed averages.
7. **Build/update the PC combat profile** —
   `vault/_templates/_campaigns/_pcs/_pc_combat_profile.md`, all 5 sections, every number
   sourced (Hard Rules 2/3), unsimulable abilities listed by name.
8. **Compile the party combat profile** if any PC profile, block, or
   loadout changed (flag stale) or requested —
   `vault/_templates/_campaigns/_pcs/_party_combat_profile.md`, ending on the Effective CR Band
   from a curated set of `npm run dndsim -- sweep-count <pc-sheets.md,...>
   <monster.md>` runs, one per season-relevant monster (or a CR-spanning
   sample) — `references/simulation.md` § Default sweeps,
   `references/profiles.md` § Effective CR Band.
9. **Write** to `vault/campaigns/shattered-sea/pcs/combat-profile/` and `vault/campaigns/shattered-sea/pcs/character-sheets/` (§ Owned paths); lint fires via
   the wired hooks. Commit
   `prep: combat-profile — <pc-slug or party> — <trigger summary>`.

## Degrade by asking

- No character sheet and frontmatter lacks what a calculation needs →
  mark `[unknown]`, build a low-fidelity block from what exists, don't
  invent a plausible number.
- Script fails or Node unavailable → labeled `[calculated]` fallback +
  explicit flag to the DM (Hard Rule 9); never a fabricated seed.
- An ability the engine genuinely can't model (narrative control,
  illusions, out-of-combat power — NOT Bardic Inspiration/Cutting
  Words/Sneak Attack/Shield, which are loadout primitives) → sim what's
  simulable, list the exclusion by name in § Calibration.
- Session transcript doesn't state exact damage/round counts → mark `~`
  or `[unknown]` per `references/data-and-sheets.md` — never silently
  round to a clean number.
- Unclear whether party composition changed since the last compile → ask
  before compiling a party profile with a stale roster.

## References

| File | Read when |
|---|---|
| `references/governance.md` | Owned paths, contract deltas, hard rules (nine procedural constraints) |
| `references/data-and-sheets.md` | Sheet/Combatant Block build, session extraction, owned-paths rationale |
| `references/profiles.md` | Effective CR Band derivation, output tiers, `encounter-prep`/`.claude/skills/draft-content/references/monster.md` relationship |
| `references/simulation.md` | Authoring loadouts, default sweeps (`sweep-corpus`/`sweep-count`), reading sim results, `utils/dndsim/` relationship |
| `references/checklist.md` | Final pre-done checklist, run before calling a profile done |
| `references/out-of-scope.md` | What this skill never does, and which skill owns it instead |
