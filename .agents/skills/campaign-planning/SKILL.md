---
name: campaign-planning
description: >-
  Campaign contract, season map, horizon, and re-planning. Use when
  starting a campaign, closing a season, choosing length or level range,
  or aligning DM and agents on architecture before prep.
---

# Campaign Planning
File what constitution X makes canon. Follow `docs/agents/work.md`.

## Workflow

### 1. Load

For an existing campaign, read before proposing:

- the campaign **overview** at `wiki/entities/lore/{campaign}-overview.md`
  (Campaign State hub: table aim, live state, index, party goals, contract)
- the current campaign story and active session-prep pages
- active front notes
- PC pages linked from the overview

If that overview is missing, mint it from
`wiki/templates/campaign-state.md` (`type: lore`), then read it. One
overview per campaign; the region page is not the hub.

For a new campaign, begin with the DM's stated concept. Mint the
overview as soon as the campaign slug is known.

**Complete when** the overview page exists and every campaign-level
commitment is represented or identified as uncertain.

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
| Premise, promise, tone, anchors, ending intent, runtime, table aim, party goals | campaign overview | `wiki/templates/campaign-state.md` |
| Season function, question, range, transitions | campaign story or session-prep note in `wiki/<slug>/` | `wiki/templates/` |
| Faction fronts surfaced | front note / faction pages | `wiki/templates/`, `wiki/templates/` |
| Named place anchor with no page | spatial kind via `place-design` | `wiki/templates/` (or settlement, region, route) |
| Named dungeon complex with no page | `dungeon` via `dungeon-design` | `templates/` |
| Named notable object with no page | `item` via `item-design` | `templates/` |
| Named conveyance with no page | `vehicle` via `vehicle-design` | `templates/` |

Fill the overview. Later writes update that page. The region page
(`wiki/entities/region/{campaign}.md`) keeps geography.

**Complete when** an unfamiliar agent could answer from the overview: what this campaign
is, what experience it promises, how long it is meant to run, how far
scope can grow, who is at the table, and what — if anything — is committed about its ending.

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
