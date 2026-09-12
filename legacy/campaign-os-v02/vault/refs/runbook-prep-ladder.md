---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-08-15"
tags: [survival, travel]
summary: "Routes prep to campaign, season, quest/arc, session, or scene scope, including cold opens as borrowed NPC perspective."
phase: any
uid: 24611b8e-3dad-4fbb-aae3-010ef363352f
---

# Prep-ladder runbook (any campaign/season/quest/session/scene scope)

The PREP family spans five scopes nested inside one another, largest to
smallest: campaign, season, quest/arc, session, scene. This runbook
routes a prep request to the right rung. It never authors content itself.
Each rung's own skill (or, for session/scene, its own existing runbook)
owns the work once identified.

## The ladder

| Rung | Owning skill | Trigger phrases | Disambiguation |
|---|---|---|---|
| **Campaign** (setting-wide, rare) | `.claude/skills/draft-content/references/campaign.md` | "write up the campaign", "campaign overview", "session-zero primer", "campaign pitch", "the six truths", "what's this campaign about", "prep a one-shot/module", "I'm importing a published adventure", or names the setting itself (or a bounded adventure) rather than one fact within it | Not for one fact within the setting (cosmology, a pantheon, a legend). Use `.claude/skills/draft-content/references/lore.md` for those. Not for an active NPC's or faction's own page (`.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/faction.md`), nor for transcribing an existing source document verbatim (`llm-wiki-ingest`'s fidelity-only job) |
| **Season** (a run of sessions, ends on a GM-planned Finale) | `.claude/skills/draft-content/references/season.md` | "start a new season", "season 2", "this session ended the season", "season finale", "close out the season", "what season are we in", "what tier is the party at", or after a session recap names a boss defeat/level-up/planned-finale event matching an open season's Finale; also fires when the party levels into a new 5e tier of play (1→2 at level 5, 2→3 at level 11, 3→4 at level 17) and no open season covers it | Not for a single session's own recap (session-recap template, `recap-writer` skill), the setting-wide campaign overview (`.claude/skills/draft-content/references/campaign.md`), or a specific storyline/mystery within the season (`.claude/skills/draft-content/references/quest.md`). A season is the chronological container where multiple quests unfold together, each distinct from the season itself. |
| **Quest/arc** (a throughline spanning many scenes, lives inside a season) | `.claude/skills/draft-content/references/quest.md` | "prep a quest", "I need a quest line for [thing]", "design a mystery", "this needs a multi-session arc", "how should this plot escalate", "set up a mystery box", "this quest feels stalled", or names any objective, mystery, or throughline meant to span more than one scene | Not for the beat-by-beat prose itself once the shape is picked (`draft-story`'s DS4 step fills `## Beats`) and not for a faction's own clock. `.claude/skills/draft-content/references/faction.md`'s [[front\|Front]] counts as a quest only when the party has a separate objective tied to it. |
| **Session** (one game session) | `vault/refs/runbook-session.md` (existing) | Session-scope prep: "prep", "next session", or any narrative-scale, multi-scene request scoped to one session | Existing rung. Cite its own steps. Never restate them |
| **Scene** (one beat inside a session) | `.claude/skills/writing-cold-opens/SKILL.md` (cold open); `.claude/skills/composing-beats/SKILL.md` (beat composition) | Cold open: "prep a cold open", "cold open scene", "cold open for [NPC]", "prep a vignette" (legacy phrase), "side vignette", "the party plays [NPC] for this one", "opener that isn't tied to the main plot". A cold open may borrow a friendly, allied, neutral, hostile, unknown, or mixed NPC perspective. Direct beat: "prep a scene", "write this scene", "scene file for [event]", "prep scene <N> for session <NN>", "rework this beat", "this scene/beat needs a player role", "the party just watches here", "give the players something to do/interact with" | Cold open is a Hook beat borrowing NPC perspective, owned end to end by `.claude/skills/writing-cold-opens/SKILL.md`; a direct beat is composed against its situation's Beat Chart, not for options/outcomes maps, run-guide graduation, read-aloud paragraph craft (`dnd5e-scene-narration`), callout containers (`callouts`), or encounter math (`encounter-prep`) |

Both existing rungs (session, scene) are cited here, not restated. Their
own `GATE:`/numbered-step/`Done` procedures stand as written.

## draft-story: the universal entry point

`draft-story` fires BEFORE composing-beats run guides, composing-beats moments,
`.claude/skills/draft-content/references/quest.md`, `.claude/skills/draft-content/references/season.md`, or `.claude/skills/draft-content/references/campaign.md` instantiates a template.
It precedes every rung of this ladder except a pure entity page (an NPC,
item, location, etc.) that would go to `.claude/skills/draft-content/references/npc.md` and siblings. Exception:
an entity born inside a story gets handled through this skill instead. Its own trigger phrases: "prep the next session",
"prep session NN", "write the story", "story first", "draft the
narrative", or starting any session, quest, arc, season, or campaign-scale
piece with no matching story yet at its target path (session stories at
`vault/episodes/NNN/`, other scopes at `vault/stories/`).
Not the narrative-devices mindset layer (`.claude/skills/composing-beats/references/composition.md`,
which layers alongside), not raw idea capture (`draft-story`'s DS2 step handles fragments).

Routing a request onto any ladder rung above means checking for
an existing story first. A missing one routes to `draft-story`, not
straight to the rung's own prep skill.

The ladder tops out at campaign: the setting page itself
(`vault/worlds/<slug>.md`) is not a rung — route it to
`.claude/skills/draft-content/references/world.md` via `draft-content`, like any other
entity page.

## Cross-cutting: encounter-prep, travel-events, and .claude/skills/draft-content/references/location.md

`encounter-prep`, `travel-events`, and `.claude/skills/draft-content/references/location.md` are not rungs of
this ladder. They are sub-steps invoked from *inside* whichever rung is
already being authored, at any scope:

- `encounter-prep`: one calibrated fight/social/skill-challenge. Also
  invoked by `.claude/skills/composing-beats/SKILL.md`, `.claude/skills/draft-content/references/location.md`, or `.claude/skills/draft-content/references/item.md` when a
  scene needs one. Not for a named recurring antagonist's own page
  (`.claude/skills/draft-content/references/npc.md`, which it hands off to) or a reusable bestiary entry meant
  to recur across encounters (`.claude/skills/draft-content/references/monster.md` owns that page).
- `travel-events`: any journey leg, crossing, or voyage the party will
  actually play — mandatory even for a routine leg (a leg is a moment,
  never a transition line). The route's standing facts stay with
  `.claude/skills/draft-content/references/route.md`; this sub-step designs what happens
  on the way.
- `.claude/skills/draft-content/references/location.md`: any settlement, region, building, shop, or dungeon
  that will appear at the table, at any scale from a single tavern to a
  multi-district capital — a district is a settlement nested `within:` a
  larger settlement and an island is a region nested `within:` a larger
  region or the sea, not a separate type. The guide decides internally how
  many pages the content needs.

Neither is ever the answer to "which rung does this request belong to."
Route to a ladder rung first, and that rung's own skill calls into these
as needed.

## GATE: which rung applies

Given a user request, work top-down:

1. Names the setting itself, or a bounded one-shot/module, rather than one
   fact within it? → **Campaign** (`.claude/skills/draft-content/references/campaign.md`).
2. Opens or closes a run of consecutive sessions under one throughline
   ("this session ended on a planned finale", a level-up into a new tier,
   "what season are we in")? → **Season** (`.claude/skills/draft-content/references/season.md`).
3. Spans more than one scene but isn't the whole campaign, and the party
   has an actual objective (not just one side's plan)? → **Quest/arc**
   (`.claude/skills/draft-content/references/quest.md`).
4. Scoped to one game session (loose threads, run guide, that session's
   scenes)? → **Session** (`vault/refs/runbook-session.md`).
5. Scoped to a single beat inside a session? → **Scene**
   (`.claude/skills/composing-beats/SKILL.md`, beat composition).
6. Names a single fight, social encounter, or skill challenge, a journey
   leg the party will play, or a place that will appear at the table? →
   This is not a rung. It's a cross-cutting sub-step (`encounter-prep`,
   `travel-events`, or `.claude/skills/draft-content/references/location.md`) called from whichever rung above
   is already in progress.
7. Names a single entity (NPC, item, creature, faction, ship, rule) with
   no narrative scope of its own? → that entity's own prep skill directly,
   skipping `draft-story` unless the entity is being born inside a story.

At any rung reached by steps 1-5 with no story yet on file, route through
`draft-story` first (§ above) before the rung's own skill instantiates a
template.

Done = the correct skill for the request has been identified. This can be a rung's own
skill or the session/scene runbook cited above. This runbook's job ends
at routing. That skill's own Workflow takes over from here.
