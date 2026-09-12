---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Where a draft guide hands off when the work belongs to a different content type or a specialist skill, and how to close the loop with a reciprocal link back."
created: "2026-08-03"
updated: "2026-08-10"
tags: [craft]
uid: 8617f4b0-f462-4bcf-895c-e3a6d7c04498
---

# Draft — Cross-Type Handoffs

A page that names another entity links to it and stubs it at most; the
entity's own content belongs to its own guide. When the handoff creates or
touches the target page, add a **reciprocal** link back on it too — item
guides add one under `## Relationships` or `## Provenance`, event guides
under `## What Happened`, the secret guide as `found_at:`. The per-type guide
names its own field; this file only requires the link run both ways.

Every **type** row below resolves through `draft-content`'s router table ->
it is the single place a type maps to its guide, so a type that has not
migrated yet still resolves to whatever currently owns it. The two rows
marked `(skill)` name their owner directly — they have no page type of their
own to resolve.

| The work | Hand to |
|---|---|
| A named individual with relationships and a story role | `npc` |
| A reusable creature kind, and its CR math | `creature` |
| A fight's calibration, terrain, tactics, pacing | `encounter` |
| A place the party can revisit | `location` |
| An organisation with goals and a front clock | `faction` |
| A magic item's mechanics and rarity budget | `item` |
| A multi-session objective with beats | `quest` |
| A vessel's stats, crew, tier, acquisition | `ship` |
| A settled world fact with no active draw | `lore` |
| Unverified gossip with a live question | `rumour` |
| A legacy page being transcribed from a source | `llm-wiki-ingest` (skill) |
| A travel leg's events, derived from the party's own threads (never rolled) | `travel-events` (skill) |
| A route's standing facts — duration, traffic, hazards — the way itself | `.claude/skills/draft-content/references/route.md` (page lives in `vault/campaigns/*/locations/`) |
| A leg's reusable random-encounter table | `.claude/skills/draft-content/references/table.md` |

## Boundary cases the guides already name

- **A one-off fight's stat block** stays inline on the encounter; a creature
  meant to recur earns its own page.
- **A quest versus a faction front**: no party objective, just one side's
  plan -> that is a front, not a quest.
- **A crew member, shopkeeper, or garrison captain** named in passing -> a
  wikilink and a stub; the full page belongs to the `npc` type.

Two guides could plausibly claim the page -> read both boundary sections
before choosing; never split the difference by writing a partial page in
each.
