---
type: route
status: draft
publish: false
title: ""                 # OPTIONAL, display title if it differs from the H1
aliases: []
summary: ""                 # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting           # core | supporting | peripheral
within: "[[campaigns/<campaign>/locations/<containing-location-slug>]]"
endpoints: []               # at least two quoted wikilinks, the places this leg connects; order carries no direction unless ## Path says otherwise
travel_modes: []             # at least one free-text tag — foot, wagon, ship, aerial, rail, portal, jump-drive; never assume one mode
distance: ""                 # OPTIONAL — free text, whatever unit this route actually uses (miles, hexes, parsecs, watches); delete if genuinely unmeasured
travel_time: ""               # free text, no unit or mode assumed — "a day and a half on foot", "three watches by ship", "one jump"
traffic: moderate             # busy | moderate | quiet | derelict
hazard_level: moderate         # low | moderate | high | lethal
geography: []                  # terrain/environment tags this leg passes through, at least one
encounter_table: ""             # OPTIONAL — [[wikilink]] to this leg's type: table page; no table exists yet -> delete this key, never leave it ""
situations: []                  # OPTIONAL — [[wikilink]]s to Situations that can surface on this leg; the same Situation may appear on more than one Route
campaigns: []                   # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/route.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 7f5b0f4d-ce6a-4966-a706-928fd146bcaf
---

# <Route Name>

*One-line description: what this leg is and why anyone crosses it.*

## Path

What this leg concretely is, a road, a sea lane, a rail line, an
underground passage, a jump lane between systems, and where it
physically runs between the `endpoints` named in frontmatter. Who
controls, tolls, or patrols it, and why. This heading holds the leg
itself, never the places at either end; those are their own `type:
location` pages.

## Waypoints

OPTIONAL, keep only when real, sourced stops exist along the way
(a rest camp, a mid-crossing anchorage, a checkpoint); delete outright
otherwise. Each stop resolves to a wikilink or a spawned stub, never
plain-text prose.

## Travel

How `travel_time` actually plays out for each mode in `travel_modes`,
what changes it (weather, season, current, patrol schedules), and
whether the crossing runs a fixed duration or varies. A recurring
random-check or encounter table this leg rolls against is a
[[wikilink]] to its `type: table` page, never restated here.

## Hazards

What can go wrong crossing this leg: terrain and weather dangers,
hostile patrols, monsters, mechanical failure, anomalies. Links to the
relevant `type: table` encounter table where one exists, never repeats
its rows.


![[<slug>-narration-condition]]
