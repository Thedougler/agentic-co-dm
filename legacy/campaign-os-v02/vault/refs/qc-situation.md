---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-13"
updated: "2026-08-13"
tags: [craft]
summary: "QC profile for type: situation pages: pressure, actors, affectable material, if-ignored changes, clues, boundaries, connections, and state."
uid: 1c5a8113-9917-46fb-8851-d20b1c0446aa
---

# QC profile: situation

For `vault/campaigns/*/situations/*.md` files (`type: situation`): durable
Narrative Islands source state. A Situation is not a moment, route, fork, or
read-aloud box. It holds the live pressure, actors, table-affectable material,
and if-ignored world change a DM can later turn into table-ready frames.

Template: `vault/_templates/_campaigns/_situation.md`. Owning route:
`.claude/skills/draft-content/references/situation.md`.

| CATEGORY | Contract | How to check |
|---|---|---|
| PRESSURE | The Situation states what pushes now: who or what advances, what sign the table can notice, and why delay costs something. Pressure is a moving force, not background mood or a static premise. | Read `pressure:` and `## Pressure`; name the advancing force, visible signal, and cost of waiting. Any missing part is a finding. |
| ACTORS | Every actor wants something and can act without the party. Actors are NPCs, factions, threats, environments, or events with leverage and a current move, not a cast list. | For each actor, state desire, leverage, and current move from the page. A passive or unnamed actor fails. |
| AFFECTABLE | The page gives PCs material they can learn, touch, change, save, spend, break, expose, or lose. Pure exposition, mood, or future narration fails. | Ask what play can change. Quote any Situation whose only table role is "the DM explains this." |
| IF-IGNORED | `if_ignored:` and `## If Ignored` name a concrete, observable world-state change that happens without PC involvement. "Tension rises" fails unless the page states how, where, and who notices. | Apply the tick test from `.claude/skills/composing-beats/references/audits.md`: name the single visible change the DM can show later. |
| CONNECTIONS | Links point to the atoms the Situation composes: Fronts, clues, locations, related events, NPCs, factions, items, lore, and table frames only when they already exist. The Situation links facts; it does not restate them. | Resolve each wikilink and check whether the page restates a fact the target owns. Restated facts are BLOAT findings. |
| CANON-BOUNDARY | `status: pending` material may frame prep possibilities, but it never asserts unplayed outcomes as canon. Played facts are linked to their owning pages or session logs. | Check status, session_log, and any claim about what already happened. A pending page that speaks like played canon fails. |
| CLUE-REDUNDANCY | Any hidden conclusion the table must reach has three distinct, mechanically discoverable clue vectors across different sources or places, with at least two reachable without combat. A Situation that can run without a hidden conclusion does not need invented clues. | Name the conclusion and list Clue 1-3 with source and discovery mechanic. Fewer than three, or three variants of the same node, fails. |
| PLAYER-BOUNDARY | The Situation never states what a PC decides, feels, thinks, intends, wants, or must do. Prescribed-player-action phrase checks stay advisory until a sweep proves the detector precise; QC still flags any concrete agency violation by evidence. | Quote any line assigning a PC inner state or required action. Treat phrasing-only tells as advisory unless the page also proves an actual prescribed action. |
| STATE | The page reads cold: lifecycle, pressure, if_ignored, actors, clues, locations, and connections are current enough for a DM to decide whether to prepare a derived moment. It has no `## Next`, no `[!read-aloud]`, and no process notes. | Diff frontmatter against the template's non-optional keys; grep for `## Next`, `[!read-aloud]`, and process/meta wording. |
