---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The ship-specific checks that run after the shared checklist — tier justification, crew headcount, acquisition, bounded variants."
created: "2026-08-03"
updated: "2026-08-08"
tags: [maritime]
uid: cf697b68-eae7-4f06-9ccc-dafb4fa5a4d1
---

# Draft — Ship Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
ship-only additions.

- [ ] `tier:` frontmatter set to a real value with a stated justification,
      decided **before** crew and cost were designed, not after.
- [ ] Crew composition stated explicitly — which roles are PC-held,
      hireling-held, or open — with headcount against the tier's minimum,
      and the below-minimum penalty noted where it applies.
- [ ] Acquisition method named and resolved through the fiction; for Steal,
      Mutiny, or Prize, the plan or relationship is stated, not just the
      outcome.
- [ ] Every variant and enhancement `[HB]`/`[RAW]`-labeled and bounded with
      range, duration, and recovery.
- [ ] `pc_connection` may name the whole party, not just one PC, when the
      vessel is shared — the PC-Connection Requirement
      (`vault/refs/vault/_common/hard-rules.md`) otherwise applies
      unchanged.
- [ ] Flavor description run against `vault/refs/vault/location/references/tips.md`'s
      six-point checklist — a ship is a mobile location.
- [ ] DM Review Gate run and passed before `status:` left `draft`.
- [ ] Multi-file family: every child page lints individually and back-links
      the parent.
