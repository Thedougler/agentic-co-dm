# Contract: Wiki kind pages (vehicle and spell)

The interface is a campaign wiki page job. Co-DM is the author. Naming the wrong primary skill is a fail. A page that cannot be run at the table is a fail.

## Routing table

| Job | Primary skill |
|---|---|
| Write, edit, or create a named vehicle page | `vehicle-design` |
| Write, edit, or create a named spell page | `spell-design` |

A beat that needs a named craft or a spell hands off to that owner. The beat skill stays primary for the beat.

## Classification jobs

| # | Job | Primary |
|---|---|---|
| 21 | Write a named ship or other vehicle | `vehicle-design` |
| 22 | Edit an existing vehicle page | `vehicle-design` |
| 23 | Write or edit a spell page | `spell-design` |

## Page rules

1. Start from `wiki/templates/vehicle.md` or `wiki/templates/spell.md`.
2. `wiki/AGENTS.md` lists `type: vehicle` and `type: spell` and Layout jobs for those kinds. Pass is those jobs.
3. A vehicle page includes spoken look, a filled 5e sheet (size, type, speed, crew), and hull/component figures. Armed craft include weapons. Handling and combat are filled when the craft enters play.
4. A spell page includes spoken look, classification, and a runnable 2024 effect block.
5. Theatre of the mind owns `[!narration]`.
6. Skills that teach these pages state what to write and when the page is done.

## Claude Code skill updates

Claude Code only for novel `spell-design` and a `vehicle-design` redesign. Dispatch: `claude -p --model claude-opus-4-6 --effort medium`. Prompt is minimal; names deliverables and a completion test. Templates and `wiki/AGENTS.md` Layout are session-agent work. Usage limit: defer the Claude job; complete independent tasks.

## Out of contract

Foundry staging. How the designated writer phrases a skill. Beat Chart assembly (see [beat-skill-routing.md](./beat-skill-routing.md)).
