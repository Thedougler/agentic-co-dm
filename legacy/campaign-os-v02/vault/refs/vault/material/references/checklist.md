---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The material-specific checks that run after the shared checklist — the Item-vs-Material and Poison-vs-Condition boundaries, worth benchmarking, form, and trade."
created: "2026-08-09"
updated: "2026-08-09"
tags: [survival]
uid: 9cd43e00-4dd2-4377-8b89-656c16af8ad7
---

# Draft — Material Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
material-only additions.

- [ ] The Item-vs-Material Boundary test actually ran — this page names a
      raw substance or trade good, not a made, held, single thing (that
      case belongs on `item` instead).
- [ ] A poison page states only the good itself in `## Uses` (dose, price,
      application) and cross-links a `condition` page for the effect on a
      victim, never restating the effect here (the Poison-vs-Condition
      Boundary).
- [ ] `form:` reflects the substance's real category (ore, metal, reagent,
      flora, food, drink, poison, commodity, other), not left at the
      template's `commodity` placeholder by accident.
- [ ] `worth:` was set against a named, comparable real trade good, not
      invented with no benchmark (Worth Needs a Real Benchmark).
- [ ] `unit:` states the real unit this material is bought and sold in.
- [ ] `## Trade`, if present, names who deals in it and whether it moves
      openly, is guarded, or is illegal; deleted outright if no market
      exists yet.
- [ ] `found_at:` lists real wikilinks to where a party could obtain it,
      matching whatever `## Trade` already names.
