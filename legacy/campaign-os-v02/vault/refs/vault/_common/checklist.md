---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Every check a page passes before it is called done — stub, template, headings, PC connection, toys, wikilinks, calibration, prose pass, optional-heading deletion."
created: "2026-08-03"
updated: "2026-08-10"
tags: [craft]
uid: 6b7679c5-9a7b-4143-abb1-e779ff63e250
---

# Draft — Shared Checklist

Run before calling any page done. A per-type guide adds its own items and
never restates one from here.

- [ ] The Stub Check (`vault/refs/vault/_common/hard-rules.md`) run and
      **pasted**; clean, or expansion of an existing page confirmed —
      never a silent duplicate.
- [ ] Page instantiated from `_templates/<type>.md`
      (`vault/refs/vault/_common/lifecycle.md`), not composed freehand.
- [ ] Template headings present, in order, nothing added or removed (the
      Template Heading Lock, `vault/refs/vault/_common/hard-rules.md`).
- [ ] PC-Connection Requirement (`vault/refs/vault/_common/hard-rules.md`)
      named with its mechanism, wikilinked where it resolves to a page.
- [ ] Every Toy field present, each a vector, behavior, or situation —
      never a trait (the Toy Field Discipline,
      `vault/refs/vault/_common/hard-rules.md`).
- [ ] Every named entity is a resolvable `[[wikilink]]`, verified against a
      real grep hit — never prose naming an entity without linking it.
- [ ] Any stat block, CR range, or difficulty number calibrated against
      real `vault/campaigns/shattered-sea/pcs/*.md` frontmatter, pasted
      (Calibrate Against The Real Party,
      `vault/refs/vault/_common/hard-rules.md`).
- [ ] Read-aloud and quoted prose read back once before shipping (the
      Prose Pass, `vault/refs/vault/_common/hard-rules.md`).
- [ ] `## Session Log` absent, or left empty — never pre-filled.
- [ ] An OPTIONAL heading whose condition does not hold is **deleted
      outright** -> never left empty (W38) and never filled with a
      placeholder line like `(none)` or `N/A` (W48). An absent heading is
      the record that the condition does not hold.
- [ ] `created:` and `updated:` carry today's real date, not the template's
      `"{date}"` placeholder.
- [ ] `status:` and `publish:` satisfy the status ladder
      (`vault/refs/vault/_common/lifecycle.md`) — `draft`/`pending` only,
      `publish:` untouched.
- [ ] `npm run lint -- <path>` reported zero findings.

The lint run is the last item and it is not optional -> a page that has not
been linted is not done, whatever the rest of the list says.
