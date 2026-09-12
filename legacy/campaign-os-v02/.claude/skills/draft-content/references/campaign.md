
# Draft — Campaign

Turns "what's this campaign about" or "I need a one-shot for next week"
into a template-conforming `type: campaign` page. Owns both forks of
`vault/_templates/_campaigns/_campaign.md`:

- **`subtype: ongoing`** — pitch, Six Truths, Icons, starting situation,
  how sessions run, Safety & Tone, GM framing (inspiration, themes, tone).
- **`subtype: one-shot`** — pitch, rumors, background, gameplay
  procedures, encounters, treasure, monsters — including a published
  one-shot imported via `llm-wiki-ingest`.

Six Truths (Sly Flourish's technique — "six" names the convention, not a
hard count) and Icons (a non-mechanical adaptation of 13th Age's Icons
concept — the name and idea only, never 13th Age's relationship-dice
mechanic) surface in the Interview and Output sections below.

What the campaign is anchored *to* is Brennan Lee Mulligan's Player Gravity
(`vault/refs/blm-player-gravity.md`): the session-zero pass reads each
character's goals and fears, and the campaign's conflicts are built where
those already point, so the party pushes on them without being steered.
Six Truths stays the tool for stating what is true of the world — Mulligan's
method has no component covering campaign-level truths, so gravity decides
what a campaign is about and Six Truths decides what it is made of.

## Template

`vault/_templates/_campaigns/_campaign.md` — copy it, never retype it
from memory.

## Story-first entry (default)

A campaign overview or one-shot built from scratch is narrative-scale:
the default entry is the `draft-story` skill — a flowing chapter at
`vault/stories/campaign-<slug>.md`, QC'd and DM-approved, that this
guide then derives the page from (premise, Truths, Icons, and the
starting situation come out of its fiction; the story's *Derived pages*
line gains this page's wikilink). An `llm-wiki-ingest` import
transcribes its source instead — no story. The DM may skip the story on
their word, not by default.

## Boundary & hand-off (read before doing anything)

Before creating or extending a page, confirm the request is genuinely
campaign-level; once drafting, route anything below to its owning guide
instead of inlining it here:

| Content | Owning guide | Note |
|---|---|---|
| A single setting-wide fact — cosmology, a pantheon, a historical event, a people's customs, a legend, a prophecy | `.claude/skills/draft-content/references/lore.md` | "What's this campaign about" is campaign-level; "what's the myth behind the Black Moon" is lore. |
| An active NPC's or faction's own page | `.claude/skills/draft-content/references/npc.md` / `.claude/skills/draft-content/references/faction.md` | An Icon named on the campaign page gets full Toy Method treatment there, linked from here. |
| A Front (goal-with-a-clock) an Icon runs | `.claude/skills/draft-content/references/faction.md`'s `## Goals & Fronts` | Icons here name who and why only, never the clock/trigger/consequence fields. |
| A campaign-level arc the party will actually pursue | `.claude/skills/draft-content/references/quest.md` | Gets its own quest page, linked from here. |
| A shared group PC-Connection concept (organization ties every PC together) | `.claude/skills/draft-content/references/faction.md` | Also the target for the Front row above. |
| A stat block meant to recur, a named foe who may return, a magic item with real mechanics, or a calibrated fight | `.claude/skills/draft-content/references/monster.md` / `.claude/skills/draft-content/references/npc.md` / `.claude/skills/draft-content/references/item.md` / `encounter-prep` | Cite, don't restate; this page inlines only genuine one-offs. |
| The prose pass, once facts are set | `draft-story` skill | |
| Transcribing an existing source document | `llm-wiki-ingest` | Fidelity-only — a claim with no source backing gets a stub, never an invented detail. A published one-shot import still uses this guide to author the resulting `type: campaign, subtype: one-shot` page; only the *content* is transcribed per llm-wiki-ingest's rules. |

One `vault/campaigns/` page per `campaigns:` value for the ongoing
subtype — a hit on the standard query below for the same value means
expand in place, never create a second ongoing-subtype page for one
campaign. One-shots get one page each, regardless of how many campaigns
they're associated with.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` and
   `.claude/skills/composing-beats/references/audits.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. Standard queries: `grep -rl "type: campaign" vault/campaigns/` and
   `grep -ril "<campaign or adventure name>" vault/`. A hit on the first
   for the same `campaigns:` value (ongoing subtype) means expand in
   place — never create a second ongoing-subtype page for one campaign.
   A hit on the second means the name collides with something already
   established — stop and ask the DM. Empty output: nothing established
   yet, name and invent freely.
4. `vault/refs/vault/_common/queries.md` — the generic entity stub
   check; run it before naming any other established entity (an Icon,
   a location, a faction) in prose, beyond the campaign-level checks
   above.

`DC1: <files read, query output pasted>`.

## Hard rules — this type only

- **Icons Name, Never Detail The Clock.** Writing an Icon (Key Figures /
  ongoing subtype) pursuing something on a timeline -> name who and why
  they matter only, never the clock/trigger/consequence fields (owning
  guide: Boundary & hand-off table above).
- **Ask, Never Default To Nothing.** Before shipping Safety & Tone ->
  ask what's sensitive for this table, never default to "nothing."
  Empty only if the table was asked and named nothing — never because
  the question was never raised.
- **Session-Zero Pulls On Something Real.** Writing session-zero
  questions (ongoing) or the party's shared/individual connection
  (one-shot) -> the PC-Connection Requirement
  (`vault/refs/vault/_common/hard-rules.md`) binds this field: name the
  specific PC and mechanism, or an explicit DM call that the hook is
  foundational premise with no single PC pull yet — never a silent
  default.
- **Villain Motivation, Not Just The Pitch.** Writing a one-shot's
  Background -> state the truth, including the villain's real
  motivation, never just repeat the Pitch (what players know walking
  in) (villain-design pointer:
  `vault/refs/vault/faction/references/content.md`).
- **Hand Off Reusable Content.** A stat block meant to recur, a named
  foe who may return, a magic item with real mechanics, or a calibrated
  fight -> hand off, never inline (owning guides: Boundary & hand-off
  table above).

## Interview

Ask these in the same message as
`vault/refs/vault/_common/interview.md`'s shared questions. **Ongoing:** pitch, Six Truths,
starting location/situation, Icons (Front needed →
`.claude/skills/draft-content/references/faction.md`, or backdrop for now),
inspiration/themes/tone, how sessions run, Safety & Tone, session-zero connection.
**One-shot:** pitch/hook, rumors, background incl. villain motivation,
gameplay procedures, encounters/treasure/monsters, Safety & Tone, party
connection. Full question phrasing and spark pointers for either fork:
`vault/refs/vault/campaign/references/interview.md`.

## Output structure

Maps onto the campaign template's three H2s: `## Overview` (subtype
H3s, delete the other fork's entirely), `## Safety & Tone`,
`## GM Notes`. Full section-by-section spec:
`vault/refs/vault/campaign/references/output.md`.

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` and
`vault/refs/vault/campaign/references/checklist.md`.

## Out of scope

Full list with owning guide per item:
`vault/refs/vault/campaign/references/out-of-scope.md`.

## Owned paths

`vault/campaigns/<slug>.md` — `status: draft` while incomplete, `status:
pending` once ready to hit the table. Never writes to
`vault/campaigns/` directly outside this draft/pending flow
(`transcript-ingest` moves prep → canon, once played) and never sets
`status: canon` or `publish: true`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/campaign/references/interview.md` | Full interview question phrasing, both subtypes, with spark pointers into campaign-craft. |
| `vault/refs/vault/campaign/references/craft.md` | Sparking a pitch, Truths, starting location, session-zero flow, character connections, Safety & Tone content, or a one-shot strong start when the DM doesn't have one yet. |
| `vault/refs/vault/faction/references/content.md` | Front archetypes, villain/antagonist design for a one-shot's Background, or group PC-Connection organization concepts. |
| `vault/refs/vault/campaign/references/output.md` | Full section-by-section mapping onto the campaign template. |
| `vault/refs/vault/campaign/references/degrade.md` | An interview answer is missing, ambiguous, or a DM call not yet made. |
| `vault/refs/vault/campaign/references/checklist.md` | Before calling any campaign page done. |
| `vault/refs/vault/campaign/references/out-of-scope.md` | Full out-of-scope list with owning guide per item. |
| `vault/refs/vault/campaign/references/example.md` | Full fixture page (placeholder names, not real campaign content) — an ongoing-subtype campaign, "pirates fighting over a dying sea," from standard queries through interview to every template section. |
