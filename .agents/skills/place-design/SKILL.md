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

## Boundary contract

### Input

Take a named place owner, the caller's objective, and the relevant brief,
`wiki/templates/place.md`, and linked topology, faction, NPC, route, and
session notes. When the owner is a place, enter this skill directly; select a
more specific local subtype only when the owner is explicitly a city or region.

### Owner-specific Work

Work only the named place: preserve its canon, build the kernel and topology,
fill the place template, and apply the affordance, clue, pressure, and
consequence craft below. Keep the caller's objective intact.

### Capability Handoff

For an explicit city or region subtype, hand off directly to `city-design` or
`region-design`; otherwise hand off only a local seam (such as a faction or
narration) with a bounded packet: owner, parent objective, evidence, template
seam, and requested output. Require return evidence naming the child
artifact/section and completion result; the child does not re-plan the place.
Resume the place draft only after the child result changes required place state
or completion evidence and satisfies its owner contract; if it does not, leave
dependent work open and report the missing evidence or specific blocker.
### Minimum context projection

For a place draft, carry only the named place owner, caller objective, relevant place brief/template, linked topology/faction/NPC/route/session evidence, and any child return packet needed for the current seam. Deliberately omit unrelated artifact groups, prior-child context not needed by this owner, and broad vault pages. Start with this projection; retrieve focused evidence for the same place only when the current evidence cannot support a required claim or topology decision, then stop when sufficient and resume this place draft with the bounded result. Never inherit a parent planner's broad context as place canon.


### Done

Use the existing `## Done` checklist below. Completion is observable when the
named place page path, kernel/topology/template checks, and any child return
evidence are reported.

- **Work gate.** Show a proposal before writing invented or conditional
  additions under `wiki/`; user-said canon is filed immediately.
- **Canon filing.** User-said place facts file immediately on the live owner
  path under constitution X. No separate acceptance wait is used. Invented or
  conditional additions still carry `invention: true` (or proposal markers),
  cite `[[pages]]`, show contradictions, and wait for the DM's decision before
  filing.
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

### Filing patterns

These patterns appear in the strongest vault pages and make the output
immediately runnable at the table:

- **Navigation first.** If the party opens with movement verbs (follow, walk
  back, descend, climb, stay on ridge) before interaction verbs (search, take,
  fish, investigate). The DM reads top-down at the table; exits and routes come
  before activities.
- **Skip entry.** Include what the party loses by bypassing: "Skip hub: lose
  fire ring, mats, fruit, and split." A place that cannot be skipped still
  states the cost of retreat.
- **Relative identity.** At a Glance states what makes this place different from
  its neighbors: "Unlike Print Braid's grass braid or Cutoff Lip's sleep-shelf,
  identity is the radial fire and spoke choices." Neighbors already exist in the
  vault — name the contrast.
- **Owner-page deferral.** When a creature, hazard, or rule appears in If the
  party, wikilink the owner page and say "resolve on owner page" rather than
  restating its full mechanics. The owner page is the source of truth; the
  place page says what triggers contact and what changes.
- **Absence honesty.** Who section states who is **not** here when the place is
  empty: "No campers now; prints show prior survivors." This is DM truth, not
  narration — the DM needs to know at a glance whether to prep an encounter.

**Where:** explicit **North:** / **East:** / **South:** / **West:** lines with
wikilinks + travel-day distances where known, and explicit canon-gap wording
where unknown. When reformatting an existing Where section into NESW, preserve
every established detail — landmarks, route notes, environmental observations —
by folding them into the appropriate cardinal entry or a closing note. Dropping
content during a format conversion is worse than leaving the format loose.

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
