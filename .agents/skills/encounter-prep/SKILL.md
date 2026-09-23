---
name: encounter-prep
description: >-
  Design a runnable combat, social, exploration, skill-challenge, or hybrid encounter grounded
  in the party, location, opposition, and desired stakes. Customized combat mechanics serve a
  named narrative beat (lore, origin, stakes, plot, or character). A named place has mechanical
  pressure that changes a choice. Use for encounter design, fight balance, tense obstacle scenes,
  and travel-event handoffs. Not pasted rules tables, statblock authoring, reconciliation, or a
  scripted sequence of player choices.
---

# Encounter Prep
## Boundary contract

**Input.** Named encounter or session cockpit, party/location/opposition canon, `templates/Encounter.md` when reusable. Classify reusable stock vs session-only cockpit before drafting.

**Work.** Classify primary mode, build goal/opposition/suspense/choices/rulings/resolution. Route creature statblocks to `monster-design`, DCs to `dnd5e-mechanics`, places to `place-design`/`dungeon-design`, tonight's field order to `run-guide`.

**Done.** `## Table-prep gate` below is the completion guard.


File what constitution X makes canon. Follow `docs/agents/work.md`.

## Combat instance

Customized combat mechanics serve a named narrative beat (lore, origin, stakes, plot, or character) a second person can name. Number-only math is incomplete.

When the encounter has a named place (lair, site, battlefield), that place has at least one mechanical pressure that belongs to it and changes a choice. Flavor-only scenery is incomplete. No named place, or an explicit DM request for a featureless skirmish, does not require invented lair mechanics.

Stock opposition used unchanged needs no custom features. Do not author statblocks — `monster-design` owns those.


## Ground and type

Read `hot.md`, session prep, location, front/quest, PC hooks, and existing opposition owners. Use
`qmd-retrieval` for party level, resources, tactics, and constraints. Classify before writing:
combat (initiative/tactics), social (leverage/concessions), skill challenge (obstacle and progress),
or hybrid (name the primary mode). If PC connection, place, opposition, or difficulty is unknown
and consequential, ask rather than guess.

Record: `primary_goal` (what changes, not merely win), `consistent_method` (opposition behavior),
`active_problem` (already in motion), `performance_hooks` (observable tell and handle),
`link_of_relevance` (named PC and connection), and `terrain_shift` (timed escalation).

## Suspense gate

Do not confuse the modes: **mystery** hides information for investigation;
**surprise** withholds the bomb until it lands; **suspense** reveals that a bad
thing is already moving, then makes choices matter under a fuse. For sustained
pressure, default to suspense rather than an opaque mystery or a one-beat
surprise.

Before the scene is ready, answer:

- What bad thing is already in motion, and how do players learn early enough?
- What is the fuse; what worsens if they do nothing?
- What remains unknown (hide the clean answer, not the problem)?
- What real cost attaches to each route: time, HP, spells, relationship, gear,
  future leverage, or moral position?
- Are there at least three materially different response paths?
- What does partial success change, and will an unplanned clever solution be
  accepted? **Always yes**; adjudicate from the fiction and let opposition adapt.
  House **Partial** (miss by 1–4) lives in `run-guide`; do not copy the definition onto the card.

Do not use a hidden step → damage punishment as the scene's substance. The
opposition and world continue acting during delay, travel, shopping, or rest; a
clock is only suspense when players can perceive and influence its direction.

## Output

Use `templates/Encounter.md` for reusable notes. A session-only scene that will be
run tonight is a **cockpit** (`run-guide`); emit only the stock that cockpit
inlines. Field order, lean section choice, image placement, and *procedure* live
in `run-guide`; this skill supplies table-useful stock:

1. **Brief:** who, where, why now, visible pressure and fuse.
2. **Now / positions:** who starts where, in feet from cover; compass directions
   that matter; speeds that matter; what a move vs Dash reaches. The cockpit
   writes this under Now only when Glance would otherwise get crowded.
3. **Action cards:** opposition loop with named actions; compact default-mode
   numbers the DM will roll. Missing owner → `monster-design`.
4. **Roster embeds:** only for creatures or items the DM will roll or spend.
5. **Zones:** named places with distances in feet and compass directions; same
   numbers as Now; features either side can use.
6. **Procedure + threat clock:** one loop. Failures impose listed *rulings* and
   do not also tick. Clock ticks state what becomes visible, usable,
   threatened, blocked, or changed.
7. **Images:** overview or identity art is a top anchor; battlemap art is a
   bottom anchor after the runnable card. Omit missing art.
8. **Tells:** clues only for conclusions the table can act on now. Every tell
   needs a concrete player use; otherwise cut it. Currently visible cover and
   routes belong in Initial Narration, not on tick 1.
9. **Be ready for:** selective ruling table — only intents that change a ruling,
   risk, route, clock, resource, NPC response, or information. Omit ordinary or
   redundant actions. Include **Assess the situation** only when success and
   failure both say what changes. Every cell is a *ruling* (`run-guide` Ruling).
   No Partial definition on the card.
10. **How the Scene Resolves:** the next scene's opening state in feet and RAW
    conditions, plus only the most likely options the beat can actually produce.
    Each option hands off to a beat on the session skeleton — not off-scene.
11. **If ignored:** one-step independent consequence when delay changes play.
12. **Time:** 30-minute budget and *cut lines* only when they change a pacing
    choice. Unbounded travel is the next beat, not this stock.

Do not emit coy hidden-info placeholders, "do not reveal" notes, or negative
facts that do not change a current choice. The cockpit is DM-facing; name the
DM fact plainly, then keep unearned knowledge out of player-facing prose.
14. **Owner image:** reuse any identity image already listed on the owner page (`![[attachments/…]]`). Do not mint art. Do not fill TotM.

For combat compare action economy, burst/sustained damage, control, terrain, escape, and party
resources against the actual group. Cite the current public rules source or approved benchmark;
summarize only needed procedure and mark untested tuning. Never include a generic CR table or
WotC book paste.

## Sandbox and filing

Opposition has goals that predate the party. Support multiple approaches and at least one
non-combat resolution where fiction permits; do not write PC decisions, feelings, or success. For
hidden conclusions, seed three distinct clues, at least two reachable without combat. Reusable/
complex encounters live under the campaign's established encounters bucket; session-only scenes
stay inline. Use `sandbox-narrative` for an anti-railroading pass and `obsidian-markdown` for
structure. Run applicable checks; report changed paths and any deferred owner work.

Ability check, save, and DC choice → `dnd5e-mechanics`. Write those tests with
the at-table grammar in `obsidian-markdown`. `npc-design`, `place-design`,
`dungeon-design`, `item-design`, `run-guide`, and `monster-design`
own their respective handoffs.

## Table-prep gate

For a session-only encounter, include at least one possible limelight angle per
PC when the fiction supports it, a strong/purposeful entry from the current
cliffhanger or agreed plan, and a short hiccup/fallback note. Keep the encounter as a modular cockpit findable in under 30 seconds; do not
script a sequence of player choices. Secrets remain DM-only and out of
`[!narration]`. Hand the finished scene to `run-guide` for field order, empty
TotM stubs, and OFM. TotM fill is a second pass.

## Public-stakes roll gate

When a decision is huge, declare the stakes and consequences before rolling. Use
an open roll when that matches the table's established convention, so everyone
can see what the decision risks; never hide a decisive outcome behind an
unannounced DC or secret punishment. The roll changes the situation either way,
and the players retain the choice to act, wait, bargain, or walk away.
