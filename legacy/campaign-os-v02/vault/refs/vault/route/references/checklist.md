---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The route-specific checks after the shared checklist — endpoints, mode-agnostic fields, the table-link boundary, waypoints."
created: "2026-08-09"
updated: "2026-08-09"
tags: [exploration]
uid: 50db7ad7-3ae2-4412-a63f-8115984c5bd8
---

# Draft — Route Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
route-only additions.

- [ ] `endpoints:` names at least two real `type: location` pages, each a
      resolvable `[[wikilink]]` — never a single endpoint, never an
      invented placeholder.
- [ ] The Leg-vs-Place Boundary test was actually run — this page
      describes the crossing itself, not a place the party stops and
      stays (that content belongs on the endpoint's own `location` page
      instead).
- [ ] `travel_modes:` names at least one real mode this campaign
      actually uses, never left as the template's placeholder tags.
- [ ] `distance:`/`travel_time:` use whatever unit this setting actually
      uses — never a D&D-mechanical default (miles, DCs, travel pace)
      pasted in without checking it fits.
- [ ] `situations:` wikilinks live Situations on this leg; a Situation
      shared with another Route is the same wikilink, never a copy.
- [ ] `## Travel` and `## Hazards` link to this leg's `type: table` page
      with a `[[wikilink]]` wherever a table exists, never restate its
      rows.
- [ ] `## Waypoints`, if present, lists only real, sourced stops — each a
      wikilink or a spawned stub, never plain text; deleted outright if
      none exist yet.
- [ ] `traffic:` and `hazard_level:` reflect the leg's actual current
      state, not left at the template default by accident.
- [ ] `encounter_table:` is filled with a real `type: table`
      `[[wikilink]]` or deleted outright — never left as `""`.
