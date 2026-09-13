---
name: hook-beats
description: >-
  Write, edit, or create content for a Hook. The session's strong start — one
  opening pressure that demands a response. Cards, completion test, and fill
  procedure for Hook beats.
---

# Hook beats

## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims.

## Purpose

A Hook is the session's **strong start**: the first situation demanding a
response, landing in one spoken delivery. Present an actionable problem, offer,
threat, discovery, or opening. Prefer an opening that connects to the previous
session's ending or an active PC goal. Only this first beat may recap the
previous session.

One Hook per session. A session with two Hooks has a pacing problem, not an
energy surplus.

## Completion test

Party has committed to a response to the opening pressure. The DM can state
what changed and what the next beat's trigger is.

## How to fill a Hook

1. **Choose the pressure.** Read [references/hook-cards.md](references/hook-cards.md)
   and pick the card whose trigger best matches the current fiction. A card is
   chosen because the fiction calls for it — not to fill a slot.

2. **Set the key.** An action Hook (pursuit, fight, crisis, ambush) opens a
   physical key — the middle explores a dangerous situation. A cerebral Hook
   (discovery, offer, revelation) opens an informational key — the middle
   decides what to do with knowledge. The Climax resolves the question the Hook
   opened, transformed by the middle's costs and revelations.

3. **Write the opening pressure.** Name the trigger, actors, stakes, visible
   information, and at least two viable player responses. Theatre of the mind
   owns `[!narration]` for spoken text. The Hook lands in one spoken delivery;
   it does not open with travel or logistics.

4. **Prepare the polarity handoff.** If the Hook is action-heavy, the next beat
   is a Development so the party can process what happened. If the Hook is
   cerebral or conversational, the next beat is a Cliffhanger to raise physical
   stakes. Do not write the next beat — hand off.

5. **Name what happens if they ignore it, fail, or redirect.** The world
   updates; the slot does not replay. Consequences are visible.

Done when: the party has committed to a response. They can name what they are
doing about the opening pressure. The DM can state what changed and what the
next beat's trigger is.

## Card fields

Every card in [references/hook-cards.md](references/hook-cards.md) carries:

| Field | Rule |
|---|---|
| Type | Hook |
| Trigger | When fiction calls for it — not to fill a slot |
| Stakes | Visible |
| Player options | At least two viable responses |
| Agency note | Ignoring, failing, or redirecting updates the world |

## Named seams

Load a second skill only when a named seam fires:

- **Chart question** — chart position, polarity, threads, or transition is
  unclear → load `session-beats` for that question, not as primary for writing
  this beat.
- **Play a Cliffhanger as Hook** → load `cliffhanger-beats` for the opening
  shape only. The beat remains the session's one Hook.
- **Play a Development as Hook** → load `development-beats` for the opening
  shape only. The beat remains the session's one Hook.

Opening another type-card catalog for any other reason is a defect.

## What this skill does not own

Beat Chart assembly, polarity rules, time budget, thread planting, escalation,
recompute, and the filed spine belong to `session-beats`. Cockpit layout belongs
to `run-guide`. Spoken player text belongs to theatre of the mind. Encounter,
trap, place, and monster crafts keep their owners. A named vehicle, spell, faction, lore note, quest, city, or region hands off to that wiki-kind owner without absorbing the page job.
