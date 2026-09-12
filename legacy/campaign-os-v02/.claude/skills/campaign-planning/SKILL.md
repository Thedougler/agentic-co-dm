---
name: campaign-planning
description: >-
  Plan or re-plan a campaign's architecture in a Campaign OS repo — scope,
  runtime, season map, advancement. Use when starting a campaign, re-planning
  after a season closes, deciding campaign length or level range, or aligning
  DM and agents on high-level direction before detailed prep begins.
---

# Campaign Planning

Establish or revise the campaign's **architecture**: the shared contract
between the DM and every agent that later creates material.

Two leading concepts:

- **anchors** — facts the DM has committed to; survive planning revisions
- **horizon** — detail decreases with distance from current play

The architecture lives on existing page types —
`vault/campaigns/shattered-sea/campaign-overview.md` (`type: campaign`)
and season pages (`type: season`) — not a separate plan document. This
skill owns the DM conversation that produces the decisions those pages
capture.

Ambiguity about the DM's intention is a defect. Uncertainty about what
players will do is a feature.

---

## Workflow

### 1. Load

For an existing campaign, read before proposing:

- `vault/campaigns/shattered-sea/campaign-overview.md` — premise, truths, icons, tone
- Active season pages: `grep -rl "season_status: active" vault/campaigns/shattered-sea/seasons/`
- `vault/campaigns/shattered-sea/threads.md` — active fronts
- `vault/campaigns/shattered-sea/player-gravity.md` — what players pursue

For a new campaign, begin with the DM's stated concept.

Proceed when every campaign-level commitment is represented or
identified as uncertain.

### 2. Grill the DM

Chain-load `grilling`. Seed the design tree with the campaign contract
categories from `references/campaign-contract.md` — identity, scope,
runtime, and ending intent are the root decisions.

Between rounds, apply three analysis frames to the DM's settled
answers and bring what they surface to the next frontier:

**Classify** — every future-facing statement is an **anchor** (DM
commitment, survives revision), a **possibility** (attractive future,
may not be reached), or **player-owned** (depends on player choice,
phrased conditionally). A player-dependent outcome phrased as
established fact goes back to the frontier.

**Season map** — build or revise the season architecture using
`references/season-architecture.md`. Each season needs a narrative
function, season question, approximate range, and transition
conditions. Season decisions that need the DM's call go to the
frontier.

**Horizon** — current season at high resolution, next at medium,
later at low, endgame as silhouette only. A later season with more
detail than an earlier one is a violation — bring the correction to
the frontier.

**Stress-test** — for each major future statement: *What player
decision could make this false?* Many answers → reclassify as
possibility. *If the party ignores this season's material, can the
campaign continue coherently?* Favor causal structures (*If left
unchecked, faction A pressures region B*) over scripted ones.

The grill is done when the frontier is empty — every campaign-scale
decision settled or marked provisional.

### 3. Output

Campaign planning produces decisions, not pages. Those decisions feed
existing page types through their guides:

| Decision | Target | Guide |
|---|---|---|
| Premise, truths, icons, tone | `vault/campaigns/shattered-sea/campaign-overview.md` | `.claude/skills/draft-content/references/campaign.md` |
| Season structure, fronts, finale | season pages | `.claude/skills/draft-content/references/season.md` |
| Faction fronts surfaced | faction pages | `.claude/skills/draft-content/references/faction.md` |

Update `vault/campaigns/shattered-sea/campaign-overview.md` in place
for an existing campaign — never create a second `subtype: ongoing`
page for one campaign. Season pages live at
`vault/campaigns/shattered-sea/seasons/`.

Content-creating agents read
`vault/campaigns/shattered-sea/campaign-overview.md` as a campaign
state file by default, so updates here propagate to every downstream
agent without additional wiring.

---

## Replanning

Re-plan when the campaign's architecture changes — not on every small
event. Full triggers and procedure: `references/replanning.md`.

## Quality Gate

Verify before declaring planning complete:
`references/quality-gate.md`.

## Reference files

| File | Content |
|---|---|
| `references/campaign-contract.md` | Identity, scope, runtime, ending intent — the grill's seed questions |
| `references/season-architecture.md` | Season construction, boundary tests, D&D tier heuristic, length estimation, narrative function, transitions |
| `references/replanning.md` | When and how to re-plan |
| `references/quality-gate.md` | Verification checklist |
