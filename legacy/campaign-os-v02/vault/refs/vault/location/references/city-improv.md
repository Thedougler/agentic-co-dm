---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Build the reusable banks that let a DM improvise a settlement live — culture name lists, location naming patterns, a texture table for its defining feature, three-axis NPC quick-build dice, and per-voice dialect lines."
created: "2026-08-03"
updated: "2026-08-10"
tags: [craft]
uid: 3e9ffe24-b2ee-4b69-85d8-4c16bdd7e7c5
---

# Draft — Location, City Improv Toolkit

Read this once a settlement is far enough along that the party will
spend unscripted time in it — wandering streets, working a crowd, asking
around. The settlement page's own Notable NPCs are the scripted
throughlines; this file is for everything between them, the moments a DM
has to invent a name, a face, or a line of dialogue with no prep behind
it and no time to stop and think.

The failure mode this prevents: reaching for a name mid-scene and
stalling, or reusing the same three NPC voices for a whole session
because improvising a new one from nothing is slow. Building small,
reusable banks *before* the session — not during it — turns "invent an
NPC" into "roll three dice and read," which is fast enough to survive
contact with the table.

Every bank below is settlement-specific flavor and lives on the
settlement's own page, never here. To see how a settlement in this
campaign already did it, run
`npm run search:content -- query "running the city name bank"` and read
the hit — then build the new settlement's own banks from its own
cultures, never porting another place's words across.

## Name Banks (by culture)

Before the session, not during it: for every culture with a speaking
presence in the settlement, write a short table —

| Culture | Root | Feel |
|---|---|---|
| *(one row per culture present)* | *(a real-world linguistic root the DM can draw sounds from)* | *(one phrase — what the names should feel like)* |

— then a given-name list (split male/female if the setting's cultures
make that distinction) and a surname list per culture, 15–20 names each.
Enough that pulling one at random never repeats inside a session, never
so many that writing the list costs more than it saves. A non-human
culture's surnames can encode something the culture cares about instead
of lineage — a visible trait, a trade, a place — so the naming pattern
itself tells a player what that culture measures people by.

## Location Naming

Pick 4–8 short grammatical patterns from the setting's linguistic root
and define what each means, as a table:

| Structure | Example | Meaning |
|---|---|---|
| *(prefix/suffix/compound pattern)* | *(a real or invented instance)* | *(literal translation)* |

Back it with a small vocabulary list (10–15 nouns from the same root) so
a new location name can be assembled on the spot from a structure plus a
noun, rather than invented whole-cloth. The naming logic follows from the
settlement's own theme: a mercantile port names places from observable
facts (what is there, how deep, which bridge), a temple-city names them
from doctrine. Pick the logic first, then the words.

## Texture Tables (dN)

For the setting's single most defining physical or social feature —
canals in a canal city, weather in a mountain pass, crowd density in a
festival square — build a small (d4–d8) random table of concrete
variations, so describing that feature doesn't default to the same
sentence every time it comes up. Each row is a physical variant a DM can
say in one clause, never a mood — pick whichever feature actually recurs
in the settlement being prepped.

## NPC Quick-Build (d12 / d10 / d10)

Three independent axes, each its own small table, rolled or picked and
combined into one NPC with zero improvisation required:

| Axis | Die | What it answers |
|---|---|---|
| Role | d12 | What this person does here — their function in the settlement's economy or social fabric |
| Visible Trait | d10 | The one physical detail a PC notices in the first three seconds, written as something the NPC is seen *doing* |
| Want Right Now | d10 | What this NPC is actively pursuing in this exact scene, not their backstory |

Roll (or hand-pick) one row from each table and read them together —
Role grounds what the NPC can plausibly know or do, Visible Trait gives
the read-aloud line its texture, Want Right Now gives the NPC an active,
sandbox-legal reason to want something from the party
(`.claude/skills/composing-beats/references/audits.md` §1 — an NPC want is a vector,
not a script). Deliver the three as an entrance: the Role supplies a job
they're caught mid-way through, the Visible Trait lands in the middle of
the description rather than opening it, and the NPC speaks first —
asking, so the party has something to answer
(`vault/refs/stories/prose-and-character-craft.md` § NPC entrance). Twelve
roles plus ten traits plus ten wants covers 1,200 distinct combinations
from thirty-two written lines.

Build all three tables' entries from the settlement's actual factions,
locations, and theme — a generic "town guard, tired" role serves nowhere
in particular. Every Role row should name a faction or institution the
settlement page already establishes, so the roll produces someone who
could only exist here.

## Speech Patterns / Dialect Banks

Once a culture or faction present in the settlement has a clear voice
(often derived from what the settlement's own Government/Trade/Culture
sections already establish —
`vault/refs/vault/location/references/settlement.md` § Optional sections),
write 3–6
short example lines per voice: common openings, a hedge or two, a
closing line. These aren't a script — they're a bank a DM can drop into
on-the-fly dialogue so an improvised NPC still sounds like it belongs to
the place, instead of sounding like every other improvised NPC. Derive
the whole bank from one social fact about the settlement, and write each
voice's lines as what that fact would actually produce in that speaker's
mouth — the fact is what makes the voices differ from each other.
