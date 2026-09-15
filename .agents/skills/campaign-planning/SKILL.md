---
name: campaign-planning
description: >-
  Campaign contract, season map, horizon, and re-planning. Use when
  starting a campaign, closing a season, choosing length or level range,
  or aligning DM and agents on architecture before prep.
---

# Campaign Planning
## Work gate

Prep only. Follow `docs/agents/work.md`.

If the DM wants loose riffs before architecture, hand off to `campaign-brainstorming`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Output durable pages under `wiki/` (entities/journal as appropriate); templates live in `wiki/templates/`.

Do not replace geographic “river bank” or “far bank”; use `wiki` for knowledge references.

Point at `docs/agents/work.md` rather than restating its glossary.

Keep the craft procedure.

---


Establish or revise the campaign's **architecture**: the shared contract
between the DM and every agent that later creates material.

Leading words:

- **anchors** — DM commitments that survive planning revisions
- **horizon** — detail decreases with distance from current play
- **season** — a campaign-scale chapter with a function and a question

The contract lives on the existing `type: campaign` hub and `hot.md`.
Chapters live in the existing story, hot, and session-prep notes. This skill owns the DM
conversation that produces those decisions.

Ambiguity about the DM's intention is a defect. Uncertainty about what
players will do is a feature.

---

## Workflow

### 1. Load

For an existing campaign, read before proposing:

- the `campaign-plan` page with subtype `full-campaign`
- the current campaign story and active session-prep pages
- active front notes
- PC pages and the campaign-plan Party Goals

For a new campaign, begin with the DM's stated concept.

**Complete when** every campaign-level commitment is represented or
identified as uncertain.

### 2. Grill the DM

Chain-load `grilling`. Seed the design tree from
`references/campaign-contract.md` — identity, scope, runtime, and
ending intent are the root decisions.

Between rounds, apply three frames to settled answers and bring what
they surface to the next frontier:

**Classify** — every future-facing statement is an **anchor**, a
**possibility**, or **player-owned**. A player-dependent outcome
phrased as established fact goes back to the frontier.

**Season map** — build or revise seasons using
`references/season-architecture.md`. Each season needs a narrative
function, season question, approximate range, and transition
conditions. Season decisions that need the DM's call go to the
frontier.

**Horizon** — current season at high resolution, next at medium,
later at low, endgame as silhouette. A later season with more detail
than an earlier one is a violation — bring the correction to the
frontier.

**Stress-test** — *What player decision could make this false?* Many
answers → reclassify as possibility. *If the party ignores this
season, can the campaign continue coherently?* Prefer causal
structures (*If left unchecked, faction A pressures region B*).

**Complete when** the frontier is empty — every campaign-scale
decision settled or marked provisional.

### 3. Write

Decisions feed existing kinds through existing templates and the type enum:

| Decision | Target | Schema |
|---|---|---|
| Premise, promise, tone, anchors, ending intent, runtime | `campaign-plan` subtype `full-campaign` | `wiki/templates/` |
| Season function, question, range, transitions | campaign story or session-prep note in `wiki/<slug>/` | `wiki/templates/` |
| Faction fronts surfaced | front note / faction pages | `wiki/templates/`, `wiki/templates/` |
| Named place anchor with no page | spatial kind via `place-design` | `wiki/templates/` (or settlement, region, route) |
| Named dungeon complex with no page | `dungeon` via `dungeon-design` | `templates/` |
| Named notable object with no page | `item` via `dnd-5e-magic-item-design` | `templates/` |
| Named conveyance with no page | `vehicle` via `vehicle-design` | `templates/` |

Update the existing full-campaign plan in place. Never mint a second
`full-campaign` page for one campaign.

**Complete when** an unfamiliar agent could answer: what this campaign
is, what experience it promises, how long it is meant to run, how far
scope can grow, and what — if anything — is committed about its ending.

---

## Replanning

Re-plan when the architecture changes — not on every small event.
Triggers and procedure: `references/replanning.md`.

## Quality gate

`references/quality-gate.md` before declaring planning complete.

## GM-prep gates

Campaign architecture is a **situation toolbox**, not a screenplay: keep actors,
locations, and motivations in tension so play can produce dominoes. Before a
session, spend roughly 30-40 minutes on only what the DM is not comfortable
improvising:

1. Review each PC's goals and abilities for limelight opportunities.
2. Choose a strong, purposeful start from the cliffhanger or agreed plan.
3. Bank about ten floating secrets/clues; do not glue each to one location.
4. List likely hiccups, one limelight moment per PC, and a parachute file of
   off-map one-shots.
5. Leave the session as a skeleton/framework, not a plotted sequence.

Keep notes modular and findable in under 30 seconds. One topic per atomic note;
link the nearest hub/MOC and leave index structure to Organizer.

## References

| File | Content |
|---|---|
| `references/campaign-contract.md` | Identity, scope, runtime, ending intent |
| `references/season-architecture.md` | Season construction, horizon, transitions |
| `references/replanning.md` | When and how to re-plan |
| `references/quality-gate.md` | Verification checklist |

## Backstory and tone gates

Treat PC-interview answers as campaign bones: who wronged or loved each PC,
who hunts them, and what they owe can seed optional rails, public stakes, and
living relationships. Keep the player's response open; a backstory rail is a
pressure source, not a required destination. Confirm Session 0 tone and table
boundaries before architecture, and do not let cinematic framing smuggle in a
promise the group did not agree to.
