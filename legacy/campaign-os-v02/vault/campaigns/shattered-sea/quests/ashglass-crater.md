---
type: quest
status: draft
publish: false
title: "Ashglass Crater"
aliases: []
summary: "A treasure rumor pulls salvagers toward a glowing volcanic crater on Ashglass — and toward the young red dragon that's killed everyone who's gone in after it."
created: "2026-08-08"
updated: "2026-08-08"
tags: [exploration, combat]
tier: supporting
quest_status: rumored
campaigns: [Shattered Sea]
uid: 47b01729-a88f-4d51-927b-1d2c4615fa18
---

# Ashglass Crater

*A rumor of treasure glinting in a volcanic island's crater has already killed every salvager who's gone looking for it.*

## Secrets & Clues

**Hook.** Word travels the docks and dive bars: something glints gold in the crater at the heart of [[ashglass|Ashglass]], visible from a boat offshore on a clear day. Nobody who's gone up after it has come back to spend it.

**Stated objective.** Investigate the rumor, survive the ash-slope, and deal with whatever's guarding the treasure — fight it, flee it, or grab what they can and go.

**Structural pattern.** Single-thread, three-act (`vault/refs/vault/quest/references/structure.md` § Three-Act Structure). Season 2 content — not yet scheduled; this quest is available whenever the party picks up the rumor, not slotted to a specific upcoming session.

**True stakes / opposition.** A young red dragon has claimed the crater as its lair and kills anything that climbs into it — territorial, aggressive, uninterested in negotiating. No opposing faction; the danger is the dragon itself. *Strongest objection*: the rumor could be exaggerated by a single unlucky or incompetent salvager rather than a real, repeat threat. Testable: `grep -ril "ashglass" vault/` for any prior salvager account beyond this page — none exists yet, so the repeat-death pattern currently rests on the rumor's own telling, not corroborated witness accounts.

**link_of_relevance.** Open-world side content — no PC-specific hook. The party's stake is whatever they decide it's worth: coin, a magic item, or just an answer to the rumor.

**Prepped reveals.** The physical evidence on the ash-slope (gear, half-buried remains, scorch marks) and the environmental tells building toward the caldera (heat shimmer, a distant roar, ash falling upward once) are real warning signs, not set dressing — a careful party that reads them can retreat before ever meeting the dragon, and that's a good outcome, not a failure state.

## Beats

Seed only — the hook above and the pattern's opening move. `draft-story` continues past this point.

- Session 1 seed: the approach — landing on [[ashglass|Ashglass]], the ash-slope, physical evidence of prior treasure-hunters, and the environmental tells that let a cautious party choose to retreat.
- Session 2 seed: the caldera — the dragon's lair and the fight, per [[ashglass-dragon|Ashglass Dragon]] (terrain and combat mechanics live there; the dragon's stat block is [[young-red-dragon|Young Red Dragon]]), and the fused, molten-slag hoard.

## Outcome

Empty — fills in only once `quest_status` advances past `active`, per session evidence (`transcript-ingest`).
