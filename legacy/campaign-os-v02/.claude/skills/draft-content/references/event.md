
# Draft — Event

A discrete world occurrence, played (`status: canon`) or scheduled
(`status: pending`) — not a session, quest, or
[[vault/refs/vault/faction/references/front|Front]]. `battle`,
`disaster`, and `festival` are grounded in a genuine, distinct Forgotten
Realms Wiki article genre each: a battle article is
combatant/casualty-shaped (e.g. Battle of Bones), a disaster article is
cause/effect-shaped (e.g. Spellplague), a festival article is
customs/attendee-shaped (e.g. Shieldmeet) — three structurally different
real exemplars, confirming these are genuine forks, not drift.
`arrival`, `negotiation`, `ritual`, and `disappearance` did not surface
as their own standalone FR Wiki article genres; they're GM-craft
functional shapes instead (an arriving party's reception, a
negotiation's stakes and terms, a rite's steps and effect, a
vanishing's last-seen and leads) — each still carries real, distinct
structure worth its own template, just not one grounded in an external
wiki genre the way the first three are. `war` is grounded the same way
`battle`/`disaster`/`festival` are, confirmed against three real
multi-engagement conflict genres: the Forgotten Realms Wiki's own
`Category:Wars` (e.g. Blood War — Causes, phased History subsections,
per-side Combatants), World Anvil's Conflict article template (Action,
Conflict sides, Repercussions), and Wookieepedia's war articles (e.g.
Galactic Civil War — Prelude, chronological course-of-war sections,
infobox Combatants/Commanders/Outcome). All three separate a war's
sides/commanders and its phased course from a single engagement's
combatants and casualties — the real structural difference `battle`
doesn't cover, confirming `war` as a genuine ninth fork.

## Subtype boundary (read before creating anything)

An event is one discrete happening — a thing that starts and ends. If
the request is actually one of these, hand off instead of instantiating
here:

- **A session's own play-by-play** → `vault/episodes/NNN/sNN-recap.md`
  (`recap-writer`). An event page distills one thing *inside* a session
  into a durable, cross-linkable fact — it isn't the session itself.
- **An objective spanning multiple scenes** (a mystery, a multi-session
  goal) → `.claude/skills/draft-content/references/quest.md`. An event has no beats to
  sequence.
- **An ongoing pressure with a clock** (a faction's agenda, still
  ticking) → `.claude/skills/draft-content/references/faction.md`'s Front. An event is
  finished or dated to a single point — a Front never resolves on its
  own timeline.
- **Reference lore with no date** (cosmology, a people's culture, a
  standing custom) → `.claude/skills/draft-content/references/lore.md`. If it didn't
  happen or isn't scheduled on a specific date, it isn't an event.

Unsure which? Ask: "does this have a date, and an end?" — yes to both is
an event.

## Template — subtype forks

`vault/_templates/_campaigns/_events/_event.md` routes to one of eight
sibling templates based on `subtype:` — instantiate the matching fork
directly instead of the general template. Whichever fork is matched owns
this page's layout — every heading and its order; this guide never adds
or reorders one:

| `subtype:` | Template | Distinctive H2s |
|---|---|---|
| `battle` | `vault/_templates/_campaigns/_events/_event_battle.md` | `## Combatants`, `## Casualties & Outcome` |
| `war` | `vault/_templates/_campaigns/_events/_event_war.md` | `## Sides & Commanders`, `## Campaigns & Phases` |
| `disaster` | `vault/_templates/_campaigns/_events/_event_disaster.md` | `## Cause`, `## Damage & Casualties` |
| `arrival` | `vault/_templates/_campaigns/_events/_event_arrival.md` | `## Who/What Arrived`, `## Reception` |
| `festival` | `vault/_templates/_campaigns/_events/_event_festival.md` | `## Customs & Traditions`, `## Notable Attendees` |
| `negotiation` | `vault/_templates/_campaigns/_events/_event_negotiation.md` | `## Parties & Stakes`, `## Terms & Outcome` |
| `ritual` | `vault/_templates/_campaigns/_events/_event_ritual.md` | `## The Rite`, `## Effect` |
| `disappearance` | `vault/_templates/_campaigns/_events/_event_disappearance.md` | `## Last Seen`, `## Known Leads` |
| everything else (a political event, an unclassified occurrence) | `vault/_templates/_campaigns/_events/_event.md` itself (`subtype: general`) | `## Participants` only |

`war` spans years, phases, and theatres — the same event spine as
`battle`, but `## Campaigns & Phases` tracks the war's shape over time
instead of one engagement's combatants and casualties. A single named
engagement inside the war (a battle with its own date, location, and
casualties) gets its own `subtype: battle` page, `within:` this war
page — wikilink it from `## Campaigns & Phases` rather than restating
its combat math here. A war already underway is this event subtype; a
war that hasn't started yet but is advancing on a clock (troop
buildups, an ultimatum's countdown) is `.claude/skills/draft-content/references/threat.md`'s
territory instead — the moment the first engagement is fought, promote
it here.

Every fork keeps `## What Happened` and `## Consequences` — only the
middle section(s) change. `battle` is the world-scale fact of a fight,
not its round-by-round math: wikilink to a
`vault/campaigns/shattered-sea/encounters/` page instead of restating
combat math, if one exists (`encounter-prep`'s territory). `festival`
is one specific occurrence of a custom on the calendar; `ritual` is the
same: one specific performance of a rite, not the standing custom
itself. `disappearance` is the discrete vanishing only — an investigation
spanning multiple scenes to resolve it is
`.claude/skills/draft-content/references/quest.md`'s territory, linked forward once that
quest page exists.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `grep -ril "<event name/description>" vault/ vault/campaigns/shattered-sea/pcs/`
   and `grep -rl --include=transcript.md -i "<event name/description>" vault/episodes/`.
   A hit expands that page in place — including a "World Tick" block or
   timeline line already describing the same occurrence elsewhere; fold
   it in, don't leave both.

`DE1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Classify Honestly.** Setting `subtype` -> match the real shape (§
  Subtype forks); `general` is a placeholder, never the final value for
  a request that fits a real fork.
- **Battle Is The World-Scale Fact.** `battle` subtype -> the fight's
  round-by-round math lives on its own
  `vault/campaigns/shattered-sea/encounters/` page if one exists
  (`encounter-prep`); wikilink it rather than restating combat math
  here.
- **Festival/Ritual Need A Specific Date.** `festival`/`ritual` subtype
  -> this page is one specific occurrence, never the standing custom
  itself — a dateless custom is `.claude/skills/draft-content/references/lore.md`'s
  territory.
- **Disappearance Stays Discrete.** `disappearance` subtype -> the page
  covers the vanishing itself only; an investigation spanning multiple
  scenes is `.claude/skills/draft-content/references/quest.md`'s territory, linked
  forward once that page exists.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What happened, or is planned to happen — in one sentence?
- `event_date` — the in-fiction date or day, matching
  `vault/campaigns/shattered-sea/lore/campaign-timeline.md`'s format for
  the same era.
- Where, if anywhere fixed — a wikilink target for `location`.
- Who was there or is expected to be there?
- Already played, or still to come? Sets the canon axis this page will
  eventually carry (§ Owned paths) — never guess it.

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Cross-skill coordination

- **Tied to a specific location** → confirm the location page exists
  (`.claude/skills/draft-content/references/location.md`'s stub check), then wikilink it
  in `## What Happened` and add a reciprocal note on the location's own
  page. This guide never authors the location page.
- **A named participant has no page yet** →
  `.claude/skills/draft-content/references/npc.md` first, then wikilink here. This guide
  never authors NPC pages.
- **The event's aftermath opens a new objective** → hand the follow-up
  to `.claude/skills/draft-content/references/quest.md`; link back here from
  `## Consequences`, don't fold beats in.

## Out of scope

- [[vault/refs/vault/location/references/npcs|NPCs]], locations, factions, quests — their own drafting guides;
  advancing a faction's Front or resolving a clock — `world-update`'s
  move, never this guide's.
- Anything already `status: canon`, or writing
  `vault/campaigns/shattered-sea/events/` at `status: canon`, or
  flipping `publish:` — `transcript-ingest`'s, `canon-review`'s, and
  PUBLISH's territory exclusively.

## Owned paths

`vault/campaigns/shattered-sea/events/<slug>.md` — `status: draft` while
incomplete, `status: pending` once the DM has confirmed the event and
its PC connection — never `status: canon`, never `publish: true`. A
played event's promotion to `canon` is `transcript-ingest`'s move (or
`canon-review`'s), triggered by the event actually being recorded in
play — same as every other drafted type.
