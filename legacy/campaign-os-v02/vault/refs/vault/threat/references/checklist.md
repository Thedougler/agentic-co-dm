---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The threat-specific checks after the shared checklist — the boundary test, Clock field rules, tick test, Three-Clue Audit, quest links, threat_status."
created: "2026-08-09"
updated: "2026-08-09"
tags: [intrigue]
uid: 5dc1113f-3122-43fb-aee9-6a5208a0cb58
---

# Draft — Threat Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
threat-only additions.

- [ ] The Faction-vs-Threat Boundary test was actually run — no single
      faction or NPC clearly owns this danger's clock (or it genuinely
      spans/outlives more than one) — and the result is why this is a
      `threat` page at all.
- [ ] `## Nature` states what the danger concretely is, not a generic
      "growing threat" line.
- [ ] `## Clock`'s [[lifecycle|Lifecycle]], trigger
      conditions, segment count, and consequence-at-fill are all filled —
      consequence passes the tick test (specific, observable,
      irreversible).
- [ ] Escalation timeline present if the threat's approach matters, not
      just its fill; omitted otherwise.
- [ ] Hidden-conclusion threats carry a full Three-Clue Audit (3 clues,
      different nodes, ≥2 reachable without combat), or were explicitly
      marked fully visible instead.
- [ ] Possible outcomes (where listed) don't all require one specific
      player choice.
- [ ] Quest link points at an existing or explicitly-flagged quest page,
      not invented silently.
- [ ] `threat_status` reflects the danger's actual current state
      (active/dormant/resolved), not left at the template default by
      accident.
- [ ] `## Entangled Parties`, if present, lists genuine stakeholders only
      — never a single clear owner (that case is a faction
      [[front|Front]] instead, per the
      Faction-vs-Threat Boundary).
