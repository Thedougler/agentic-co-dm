---
name: place-design
description: >-
  Design engaging playable places for D&D 5.5e (2024 / SRD 5.2.1): settlements,
  wilderness regions, dungeons and ruins, landmarks, encounter sites, and planar
  or reality-warped locations. Use when creating location kernels, topology,
  affordances, factions, information economies, pressure, location moves, or
  node keys, or when filing those facts into a campaign location note. Prefer
  situations over plots. Do not use for pure narration without structure (use
  theatre-of-the-mind) or for monster/item math alone.
---

# Place design

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, and propose for
  acceptance. No silent canon — including invented neighbors, occupants, pack
  contents, or secret dungeons across a gap.
- **Canon gaps.** Missing cardinal neighbors stay explicit gaps. Do not invent a
  named site to fill a direction and write it as established fact.
- **Template lock.** Copy `wiki/templates/place.md` only. Fill Overview, At a
  Glance, If the party, Who, What, Where, Why with substance — not empty headings.
- **Narration.** Overview spoken look is `[!narration]` — immediately perceivable
  only. No secrets, DCs, hidden history, or unearned names.
- **Kernel before draft.** Write the five-sentence kernel (and identity framing)
  before the page body.
- **No single-lever trap.** Essential truths need ~three independent clue
  vectors. Obstacles get sign, trigger, effect, counterplay, bypass, and
  leverage — not one prescribed method or one check.
- **Respect capabilities.** Do not arbitrarily negate flight, teleportation,
  burrowing, darkvision, or social authority; give honest costs, exposure,
  limits, or opportunities.
- **Enemies-vanished.** The place must stay interesting without an encounter
  quota — exploration, clues, routes, resources, factions, hazards, or change.
- **No reset.** On return, preserve durable history; update what is alive.
- **Hub deferral.** For `kind: city`, load `city-design` as primary. For a region
  job, load `region-design` as primary.

## Central principle

A place is a **situation with topology**, not a lore essay or predetermined
scene sequence. Prepare circumstances and actors; let players determine what
happens. Spend prep on decisions the table will face.

## Build the place

1. **Kernel.** Five sentences — **Function**, **Fantastic element**, **Present
   conflict**, **Player promise**, **Trajectory** (what if nobody intervenes).
2. **References.** 2–4 recognizable handles; record inherit / transform / reject.
3. **Promise.** One or two dominant player promises that decide what deserves
   prep (discovery, danger, intrigue, exploitation, wonder, refuge,
   transformation, mastery). Make them actionable.
4. **3Fs + signatures.** Fantastic / Familiar / Functional; one productive
   contradiction; three concrete actionable signature details.
5. **Structure.** Nodes and edges before room prose. Cardinal NESW neighbors with
   `~ days of travel` or explicit canon gaps. Prefer ≥2 approaches, a loop, a
   bypass, a retreat, a route tradeoff, and reconnection after branches.
6. **Affordances.** Verb test: each significant node invites a useful verb.
   Prepare materials, relationships, constraints — not prescribed solutions.
7. **Life, clues, pressure.** Faction sheets (Want/Fear/Method/Resources/Tell/
   Offer/Response); ~three clue vectors per required secret; 2–4 location moves
   with actor, trigger, visible result, new opportunity, lasting consequence.

## File the wiki note

Copy `wiki/templates/place.md`. Pass place jobs in `wiki/AGENTS.md` Layout — not
heading-order match. Design with
[location-skeleton](references/location-skeleton.md) and
[node-key-and-affordances](references/node-key-and-affordances.md); file **facts**
into the template. Kernel, 3Fs, promise lists, topology audit, and quality
checklist stay in this skill (or process notes) — do not dump the skeleton onto
the wiki page.

| Design work | Place jobs |
|---|---|
| Identity image | After the title when art exists (`visual-aids`) |
| Spoken look | Theatre of the mind `[!narration]` |
| Situation now | What this place is; linked places it sits between |
| Consequential moves | Player verbs that change the scene |
| Presence / absence | Who is here, or the sign they are not |
| Table objects | Features, flora, fauna, objects; wikilink owners |
| Connections | Neighbors + how connected; name canon gaps |
| Purpose | Why a party comes, stays, or cares |

**Where:** explicit **North:** / **East:** / **South:** / **West:** lines with
wikilinks + travel-day distances where known, and explicit canon-gap wording
where unknown.

Rules vocabulary and type adjusters:
[rules-and-place-types](references/rules-and-place-types.md). Living systems and
pressure: [life-info-pressure](references/life-info-pressure.md).

Read `references/place-craft.md` for promise detail, topology/clue/pressure
craft, audit questions, and failure modes.

## Handoffs

Deep dungeon graphs → `dungeon-design`; narration → `theatre-of-the-mind`;
pacing → `session-beats`; cities → `city-design`; regions → `region-design`;
factions → `faction-design`; vault lookup → `.agents/skills/qmd`. Do not invent
setting canon when the vault is silent — mark a stub or gap.

## Done

- Fills `wiki/templates/place.md`; empty sections omitted; skeleton not on-page.
- Kernel + promise clear; topology has real choices; nodes pass the verb test.
- Clues robust (~3 vectors); factions have goals and moves; pressure changes play.
- Where has NESW + travel days or explicit canon gaps; invention labeled/cited/
  proposed; wiki write only after accept.
- Enemies-vanished test passes; consequences persist on return.
- DM recovers actionable facts in under 30 seconds.
