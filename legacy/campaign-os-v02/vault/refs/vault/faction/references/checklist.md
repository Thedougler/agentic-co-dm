---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The faction-specific checks after the shared checklist — front field rules, lifecycle and trigger, the tick test, Three-Clue Audit, quest links, faction_status."
created: "2026-08-03"
updated: "2026-08-08"
tags: [mystery]
uid: ca815000-e904-46e0-a4b8-005257e85326
---

# Draft — Faction Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
faction-only additions.

- [ ] Every front's `primary_goal` is a vector, `consistent_method` a
      table-doable behavior, `off_screen_action` an observable trace —
      none of the three is a static trait or an internal-state claim.
- [ ] Every front has a lifecycle state and, if `dormant`, a named trigger
      that hasn't fired yet.
- [ ] Every front's consequence-at-fill is specific, observable, and
      irreversible — passes the tick test.
- [ ] Hidden-conclusion fronts carry a full Three-Clue Audit (3 clues,
      different nodes, ≥2 reachable without combat) or were explicitly
      marked fully-visible instead.
- [ ] Possible outcomes (where listed) don't all require one specific
      player choice.
- [ ] Quest links point at existing or explicitly-flagged quest pages, not
      invented silently.
- [ ] `faction_status` reflects the faction's actual current state
      (active/dormant/dissolved), not left at the template default by
      accident.
