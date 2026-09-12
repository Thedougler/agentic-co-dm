---
name: encounter-prep
description: Design a combat, social, skill-challenge, or hybrid encounter, plus any one-off creature stat block a fight needs, in a Campaign OS repo (vault/ present). Use for "design an encounter", "I need a fight", "balance this fight", "social encounter with [NPC]", "skill challenge for [obstacle]". Not a recurring antagonist (npc GUIDE) or bestiary entry (monster GUIDE).
---

# Encounter Prep

Lives at
`.claude/skills/encounter-prep/`, alongside the other content-scoped
`vault/` prep skills (`.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/location.md`, `.claude/skills/draft-content/references/monster.md`, …) —
one `vault/` page type end to end. Canonical home for combining creatures,
the party, and terrain into a fight, and running or tuning it once it
starts. `.claude/skills/draft-content/references/monster.md` cites this skill's `references/` for the fight
around its own creature's stat block; `draft-run-guide` loads
`references/running-the-encounter.md` for any combat branch point rather
than housing that guidance itself.

Empirical difficulty calibration: `references/combat-calibration.md`. Cites
`.claude/skills/composing-beats/references/runtime-surface.md` and `.claude/skills/composing-beats/references/audits.md`
throughout instead of restating their rules.

## Wiki placement

Every encounter gets its own file, `vault/campaigns/shattered-sea/encounters/<slug>.md`, even a
one-off tied to a single session — never inline on a draft-run-guide
page. Whether a foe or creature gets its own page or stays inline here →
§ Named foe vs. generic creature fork, below. Full placement rationale
(W5 heading rules, `type: session` non-collision):
`references/named-foe-fork.md` § Wiki placement detail.

## Standard queries

Run before creating anything, before writing prose naming an existing
entity, before finalizing any stat block/difficulty call (party read), and
when a faction from `vault/campaigns/shattered-sea/factions/` is involved:

```bash
grep -ril "<encounter/creature/NPC name>" vault/ 2>/dev/null
grep -rl --include=transcript.md -i "<name>" vault/episodes/ 2>/dev/null
grep -rn "^player:\|^class_levels:\|^hp_max:\|^ac:" vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -rA5 "## Session Log" vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -A20 "### Front:" vault/campaigns/shattered-sea/factions/<slug>.md 2>/dev/null
```

Zsh glob pitfall, reading the result, absence escalation:
`vault/refs/vault/_common/queries.md`.

## Owned paths

Instantiated from `vault/_templates/_campaigns/_encounter.md` — copy it, don't retype it from
memory. Writes directly to `vault/campaigns/shattered-sea/encounters/<slug>.md` (`type: encounter` for
standalone encounter pages; a one-off creature's stat block stays inline
on that same page, never its own file), `status: draft` while assembling,
`status: pending` once table-ready — edited in place from there, never
moved. Never sets `status: canon` or `publish: true` (`transcript-ingest`'s
and PUBLISH's exclusive moves). Never writes to `vault/campaigns/shattered-sea/pcs/` directly, an NPC page
(the npc guide's owned path), or a reusable creature page (`.claude/skills/draft-content/references/monster.md`'s
owned path) — hands off and quotes instead.

## Hard rules

Shared rules (Stub Check, PC-Connection Requirement, Toy Field Discipline,
Player Character Boundary, Status Gate, [[degrade|Degrade By Asking]], Reuse
Before Inventing, Calibrate Against The Real Party) bind via
`vault/refs/vault/_common/hard-rules.md`, cited not restated. Full text and
citations below, incl. which shared rule each one extends: `references/hard-rules-detail.md`.

1. About to fill in `link_of_relevance` → name the specific PC and the
   mechanism — non-negotiable; lands in the Toy table's `link_of_relevance`
   row.
2. About to write any Toy field → `primary_goal`/`consistent_method`/
   `active_problem` map to thematic proof / opposition behavior / the
   situation already in motion, never traits or feelings.
3. About to author a named foe or reusable creature's page content here →
   hand off to `.claude/skills/draft-content/references/npc.md` or `.claude/skills/draft-content/references/monster.md` instead, then quote, unless
   it's a genuine one-off.
4. About to calibrate difficulty by CR alone → stop, read the party's
   actual stats and Session Log, run `references/combat-calibration.md`'s procedure.
5. About to invent new creature math → prefer a reskinned published
   creature instead.
6. About to exceed three distinct creature types in one encounter → stop,
   cap is three.
7. About to finalize an encounter with no *if ignored* consequence → stop,
   it's a resolved set-piece, not a sandbox situation.
8. About to set the CR budget for two or more enemy groups present but
    not coordinated against the party → discount it ~25%.
9. About to guess instead of asking → stop, degrade by asking —
    `references/degrade-by-asking.md`.
10. About to write a resolvable check → stop, full-anatomy `[!check]` or
    DC-menu table only, never attack-as-DC.
11. About to write a fight with a sibling scene file → this page owns the
    operative numbers; the scene file transcludes, never restates.
12. About to finalize a combat encounter with no Run Sheet → stop, ship one.
13. About to leave a stated-odds branch with no written text → stop,
    `## Endings` covers it, plot-defense needs a fallback.
14. About to gate progress on an objective/puzzle with no hint ladder →
    stop, ship `## If They're Stuck`.
15. About to close a unit with no `## Transition`, or open with no
    Dramatic Question → stop, both required.

## Interview

If the user's message doesn't already answer these, ask all at once —
never one at a time:

- Encounter type — combat, social, skill challenge, or hybrid?
- Which PC thread does this pull on, and how? (Hard Rule 1)
- Where does it take place — existing location or new?
- What faction or NPC drives the opposition — existing or new? Named or
  generic?
- Desired difficulty — easy, medium, hard, deadly?

## Encounter Type Router

Classify before designing — the type shapes which output sections carry
the weight: `references/encounter-type-router.md`.

## The Toy (write as a body table, not frontmatter)

One table, under the opening brief (frontmatter-key rationale:
`references/quality-guidance.md`):

| Field | What goes here |
|---|---|
| `primary_goal` | What this encounter proves, thematically — not tactically. |
| `consistent_method` | Opposition behavior and tactics — table-doable, not personality. |
| `active_problem` | The situation already in motion before the party arrives. |
| `performance_hooks` | One vibe reference + one tic for the lead antagonist, if any. |
| `link_of_relevance` | Hard Rule 1's connection — which PC, and the mechanism. Required. |
| `terrain_shift` | One specific, timed change mid-encounter. |
| `objective` | What "winning" this encounter requires beyond defeating every enemy, if not simply that (`references/encounter-composition.md` § Set-piece checklist's "A Goal"). |

## Quality guidance, mapped onto the template

`vault/_templates/_campaigns/_encounter.md`'s headings are fixed; the Toy table (above) goes
before `## Enemy Roster`. Full per-heading mapping: `references/
quality-guidance.md`.

## Named foe vs. generic creature — the fork

Decide before writing Enemy Roster — full decision detail and naming
guidance: `references/named-foe-fork.md`.

## Cross-skill coordination

Hand-off boundaries with `.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/monster.md`, `.claude/skills/draft-content/references/location.md`,
`.claude/skills/draft-content/references/item.md`, `world-update`, `draft-run-guide`, `dnd5e-scene-narration`,
and `visual-aids`: `references/cross-skill-coordination.md`.

## Degrade by asking

Never invent difficulty, opposition, the PC connection, or a recurrence
call — ask. Full trigger list: `references/degrade-by-asking.md`.

## Checklist

Run before calling the encounter done — full list: `references/checklist.md`.

## Worked example

Full fixture (smuggler ambush, placeholder names, not real campaign
content) including the "skip the hand-off" failure case:
`references/worked-example.md`.

## Creative-domain rider

Facts, canon, structure, and visibility are bound (Hard Rules above, all
ten CLAUDE.md project rules; `.claude/skills/composing-beats/references/runtime-surface.md`'s own creative-domain
rider, cited not restated). **Prose style is free.** A generic "bandits
attack" encounter or a timid Raising the Stakes dial that never pressures
anyone is a contract violation, not a safe default — push for the
specific, table-tested version.

## Out of scope

Named/recurring antagonist or reusable creature pages, other prep skills'
page types, the run guide itself, read-aloud prose, faction clocks,
`status: canon`, `vault/campaigns/shattered-sea/pcs/`, flipping `status`/`publish`. Full list with
owning skill per item: `references/out-of-scope.md`.

## Reference files

| File | Read when |
|---|---|
| `references/combat-calibration.md` | Finalizing Challenge Calibration — the empirical-not-CR difficulty method for this specific encounter |
| `references/encounter-composition.md` | Choosing composition shape, the creature-type cap, the set-piece checklist, boss/minion pairing, tiers-of-play calibration, terrain (zone-based + [[gameplay-toolbox\|Gameplay Toolbox]]), and a standard-baseline difficulty number (XP budget or Lazy Encounter Benchmark) before or without `combat-profiles` data |
| `references/running-the-encounter.md` | Writing Tactical Notes/Run Sheet/Raising the Stakes/Lowering the Stakes, or adjudicating any combat branch point at the table — role placement/tactics, tactical personality, difficulty dials, running hordes, positioning/targeting/improvised numbers, zone movement, initiative/cinematic-advantage tricks, flee/surrender/waves |
| `references/quality-guidance.md` | Filling in each template heading beyond its one-line prompt |
| `references/named-foe-fork.md` | Deciding named-vs-generic hand-off, naming a flavor-only foe, or the full wiki-placement rationale |
| `references/cross-skill-coordination.md` | Checking a hand-off boundary with a sibling skill |
| `vault/refs/vault/_common/queries.md` | The rationale behind the Standard queries grep shapes |
| `references/worked-example.md` | Seeing the full shape of a finished encounter page and a common failure case |
| `references/hard-rules-detail.md` | Full text and citations for each Hard rule |
| `references/degrade-by-asking.md` | Full trigger list for asking instead of guessing |
| `references/out-of-scope.md` | Full out-of-scope list with owning skill per item |
| `references/checklist.md` | Final pre-done checklist |
| `references/encounter-type-router.md` | Classifying encounter type (combat/social/skill/ambush/hybrid) and which output sections carry the weight |
| `vault/refs/vault/monster/references/cr-design.md` | Designing a one-off creature's stat block from scratch, or validating its CR (`.claude/skills/draft-content/references/monster.md` owns the method; this skill cites it for inline, non-page creatures) |
| `vault/refs/vault/monster/references/statblock-format.md` | Writing or fixing a one-off creature's `statblock` codeblock (Fantasy Statblocks plugin, confirmed installed) |
