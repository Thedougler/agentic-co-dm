---
type: campaign
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: ["<Campaign Nickname>", "<Short Name>"]
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/draft-content/references/campaign.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: core              # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill). A long-running campaign overview is core by definition; a one-shot/module is usually supporting or peripheral
subtype: ongoing        # ongoing | one-shot — which fork this page uses (§ below); delete the other fork's H3s to match
world: ""               # OPTIONAL — wikilink to the `_templates/world.md` page this campaign runs in (e.g. "[[worlds/faerun|Faerûn]]"); absent ⇒ the world is unstated
campaigns: [Shattered Sea]  # OPTIONAL — this page's own campaign; rename to match. A repo tracking more than one campaign gets one of these pages per campaign
uid: 88f16b57-fdc7-4e55-ab27-35d56f7caad5
---

# <Campaign or Adventure Name>

Covers
two shapes — pick the one matching what's actually being documented, set
`subtype:` accordingly, and delete the other fork's H3 subsections
entirely (don't leave empty ones): `subtype: ongoing` uses the "Ongoing
Campaign" H3s below, `subtype: one-shot` (a single-session or short
self-contained adventure) uses the "One-Shot / Module" H3s. Only the three
H2s (Overview, Safety & Tone, GM Notes) are fixed — nothing added
or removed, either subtype.

<One evocative line — the tone and central premise/hook in a sentence, the way a back-of-book blurb would.>

## Overview

### Ongoing Campaign — The Premise

<What's true about this world that every player should walk in knowing — the inciting condition the campaign is built on, not a spoiler. What changed, or is about to.>

### Ongoing Campaign — The <N> Truths

<The setting's non-negotiable premises — the facts that shape every scene at the table, not backstory trivia. One sentence each, wikilinked to the entity/faction/place it names.>

1. <Truth one.>
2. <Truth two.>

### Ongoing Campaign — Key Figures

<The campaign's Icons (a simplified, non-mechanical adaptation of 13th Age's Icons concept — the name and idea only, not its relationship-dice mechanic) — the handful of powerful NPCs or factions whose actions ripple through the whole setting whether or not the party ever meets them. One line each: a title, who they are, what makes them matter. Full Toy Method treatment belongs on their own page — for an NPC Icon, load `_templates/npc.md`; for a faction Icon, load `_templates/faction.md`; follow its instructions exactly and link it here, don't restate it. An Icon that's actively pursuing something on a timeline has a Front (goal-with-a-clock) — that Front's mechanics live entirely on the Icon's own `_templates/faction.md`-built page under `## Goals & Fronts`, never restated here. This list only says who matters and why; a one-line note on *which* Fronts are currently active campaign-wide (not their clock detail) can go under GM Notes § Inspiration & Themes if the DM wants a running tally.>

- **<Title>** [[<name>]] is <one line>.

### Ongoing Campaign — The Starting Situation

<Where the party begins — the starting location (a settlement, ship, outpost, or similar central point the world spirals outward from), the hook, and why the party is together (an existing group patron or shared origin, if any). This is a session-zero primer, not a plot summary.>

**Questions to answer before Session Zero:**

- <Question a player should answer about their PC's stake in this premise.>
- Does the party share a single starting connection (a patron, an organization) or does each PC bring an individual relationship to another PC? Name which, and to what/whom.

### Ongoing Campaign — How Sessions Run

<How this table runs sessions at the table: frequency and schedule, pacing for long-term arcs, what happens between sessions (character advancement, downtime, off-screen events), how the DM telegraphs opportunities and danger, mechanics vs roleplay balance, and anything else the table agrees on about its cadence and style.>

### One-Shot / Module — The Pitch

<The player-facing hook: what draws adventurers here, what everyone at the table knows going in. This is the "welcome to..." blurb, not the solution. Open on a strong start — drop the party into the middle of the action or a striking image rather than a scene-setting preamble.>

### One-Shot / Module — Rumors & Legends

<A table of things the party may have heard before arriving — some true, some false, the DM's call on which. Mark each entry's truth under GM Notes § Background below, not here.>

| D6 | Rumor |
|---|---|
| 1 | <Rumor.> |

## Safety & Tone

<Both subtypes: run this before the table plays, not after something goes wrong. Sensitive topics this campaign/adventure might touch, discussed and agreed with the players — not the DM's private guess. If genuinely nothing sensitive applies, say so explicitly rather than leaving the section silently empty.>

**Sensitive topics discussed:** <list, or "none flagged by the table">

**Hard lines** (never comes up): <list, or "none named">

**Off-screen content** (can happen, described vaguely, not played out): <list, or "none named">

**Safety cue:** <the phrase this table uses to pause and step out of character, if one is agreed>

## GM Notes

### Ongoing Campaign — Inspiration & Themes

**Inspiration.** <The books, games, films, or other campaigns this one draws from.>

**Themes.** <The question(s) this campaign is built to explore at the table.>

**Tone.** <The register — how consequences land, how hope and danger are calibrated, what kind of story this refuses to tell.>

<Any other secrets, withheld truths, or GM-only framing — foreshadowed threats, icon motives not yet public. If genuinely none, say so explicitly rather than leaving the section silently empty.>

### One-Shot / Module — Background

<What actually happened — the truth behind the hook and the rumors table above. This is the answer key, not a repeat of the pitch. Name the villain's motivation plainly — good villains believe what they're doing is right — and what makes them memorable, not just a title and a goal.>

### One-Shot / Module — Gameplay

<Procedural rules for running this at the table: encounter frequency/triggers, any special behavior (what pursues the party, what doesn't), environmental defaults (locked doors, darkness), and anything else a DM needs before opening the first room.>

### One-Shot / Module — Encounters

<A random-encounter table for this adventure, if it has one. A named recurring foe belongs on its own page — load `_templates/npc.md`; a generic creature meant to reappear — load `_templates/_srd/_monster.md`; either way, follow its instructions exactly and wikilink/quote from there rather than restating a stat block inline. A genuine one-off stays inline here, or load `_templates/encounter.md` for a full calibrated encounter.>

| D6 | Encounter |
|---|---|
| 1 | <Encounter.> |

### One-Shot / Module — Treasure

<Named items or rewards tied to this adventure's outcome. A reusable magic item with its own mechanics belongs on its own page — load `vault/_templates/_srd/_item.md`, follow its instructions exactly, and link it here rather than restating its rules.>

### One-Shot / Module — Monsters

<Stat blocks for this adventure's opposition. A generic/homebrew creature meant to recur — load `_templates/_srd/_monster.md`; a named foe who may recur — load `_templates/npc.md`; follow its instructions exactly and link it here. Inline stat blocks here only for genuine one-offs — same convention `_templates/encounter.md` uses.>
