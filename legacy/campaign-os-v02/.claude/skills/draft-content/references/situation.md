# Draft — Situation

A durable dramatic condition composed from existing campaign atoms. Done means
the DM can see the actors, connections, current lifecycle, and a scannable
Beat Chart without a scripted route.

## Template

`vault/_templates/_campaigns/_situation.md` — copy it. Headings fixed and in
order: Actors, Connections, Beat Chart. `pressure:` and `if_ignored:` live
in frontmatter, not as headings.

## Beat Chart is required

Every Situation page carries a `## Beat Chart` (DM ruling) — never delete
the heading, never leave a subsection empty. Walk all eight sections in
order:

1. **Dramatic Question** — one sentence.
2. **Player Gravity** — `[[PC]] — relevant established investment`, one row per PC.
3. **Current State** — material facts, one per line.
4. **Active Beat** — wikilink to the Beat currently in play.
5. **Beat Spine** — ordered `[[Beat]] — entry trigger or state` rows.
6. **Live Branches** — `**state condition** → [[Beat]]` rows; a divergence
   earns a row only when it passes the collapse test
   (`.claude/skills/composing-beats/references/audits.md` § Branch
   collapse test).
7. **Climax Readiness** — the eight gate conditions, each `ready` or
   `missing <condition>` (`.claude/skills/composing-beats/references/climax-gate.md`).
8. **Unused Possibilities** — `[[Beat]] — what could reactivate it` rows.

Keep full Beat content on its own atomic Beat page; the chart wikilinks,
never restates (`.claude/skills/composing-beats/references/runtime-surface.md`
§ The composition surface).

## Read first — all five, before writing anything

1. `.claude/skills/writing-narrative-islands/SKILL.md` — method gate; state its `NI:`
   line before drafting.
2. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
3. `.claude/skills/composing-beats/references/audits.md` — pressures, if-ignored, clue
   redundancy, player agency.
4. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type,
   never restated below.
5. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the
   output.

`DSIT1: <five files read, NI line stated, stub-check output pasted>`.

## Hard rules — this type only

- **Pressure, Not Plot.** A Situation states a live world condition and what
  pushes it forward. It never prescribes what the party does, discovers, accepts,
  defeats, or chooses.
- **Minimal Until Earned.** Start vague and small. Add table-ready specificity
  only when current canon, world pressure, or player attention makes it useful.
- **Atoms Stay Typed.** NPCs, factions, locations, items, clues, secrets, events,
  threats, and Fronts keep their own pages or owning sections. Link them here;
  do not duplicate their facts.
- **Fronts Stay With Owners.** `fronts:` links to the faction, NPC, location, or
  threat page that owns the clock. This page exposes the pressure; it does not
  become a second Front record.
- **Lifecycle Is Operational.** `lifecycle:` tracks prep state:
  `latent | seeded | discoverable | engaged | resolved | transformed |
  obsolete`. It is not a session order, canon proof, or outcome forecast.
- **Beat Chart Is The Sample Surface.** The Beat Chart (§ Beat Chart is
  required, above) is where tonight's material lives — Active Beat, Beat
  Spine, Live Branches. A Beat earns its own atomic page only when the
  situation is irreversible, decision-bearing, or a peak; the chart
  wikilinks it rather than inlining its content.
- **No Session Graph.** Do not add run buttons or Metabind controls. A
  planned or nearby Situation earns `<slug>-run-guide.md` beside this
  page — that walk is how the DM runs it.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What is the live condition in one sentence?
- What pressure advances it now, and what visible signal shows that pressure?
- Who are the actors, and what does each want?
- What can PCs discover or affect? If there is a hidden conclusion, where are
  the three distinct clue vectors?
- What changes if the party ignores it?
- Which existing atoms does it compose: NPCs, factions, Fronts, clues,
  locations, items, secrets, events, threats?
- Which lifecycle state is true right now?

## Before you ship

- Narrative Islands `NI:` line is still true after drafting.
- `pressure:` and `if_ignored:` are non-empty and observable.
- No sentence requires a specific PC choice or success.
- `actors:`, `fronts:`, `clues:`, and `locations:` use wikilinks when the
  target page exists; unresolved targets become handoffs, not copied facts.
- Hidden conclusions have three distinct clue vectors or are marked as not
  ready for table prep.
- The Beat Chart's eight sections are all present and non-empty; `session_log:`
  (frontmatter, OPTIONAL) records only what surfaced, changed, resolved,
  transformed, or became obsolete in play.
- Shared lifecycle, gaps, handoffs, boundaries, and common checklist:
  `vault/refs/vault/_common/lifecycle.md`,
  `vault/refs/vault/_common/degrade.md`,
  `vault/refs/vault/_common/handoffs.md`,
  `vault/refs/vault/_common/out-of-scope.md`,
  `vault/refs/vault/_common/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/writing-narrative-islands/SKILL.md` | Every Situation draft or revision |
| `.claude/skills/composing-beats/references/audits.md` | Checking pressure, if-ignored, clue redundancy, PC agency, or the branch collapse test |
| `vault/refs/vault/faction/references/front.md` | Linking or interpreting a Front |
| `.claude/skills/composing-beats/SKILL.md` | Composing the Beat Chart — Beat Spine, Live Branches, Climax Readiness |
