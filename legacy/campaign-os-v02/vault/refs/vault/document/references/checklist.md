---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The document-specific checks after the shared checklist — the Handout Boundary, verbatim Text, in-world Origin, and the Effects-Of-Reading cross-link."
created: "2026-08-09"
updated: "2026-08-09"
tags: [intrigue]
uid: cf78b513-46e0-45b8-80a9-f125d14f0114
---

# Draft — Document Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
document-only additions.

- [ ] The Handout Boundary test was actually run — this text has real
      in-world weight beyond one scene (an NPC references it, or it ties
      to a quest/faction), and that is why it's a `document` page rather
      than a `handout` alone.
- [ ] `## Text` holds the document's own verbatim words, or explicitly
      states why it doesn't yet (lost, destroyed, not yet drafted) —
      never a paraphrase and never left silently empty.
- [ ] A `handout` page built from this document transcludes
      `![[<slug>#Text]]` rather than retyping the words.
- [ ] `## Origin` names the specific in-world circumstance that produced
      this document — never a generic "ancient text" gesture, and never
      a note about how or when the DM added the page.
- [ ] `## Effects Of Reading`, if present, cross-links any real numeric or
      mechanical effect to that effect's own `item` or `rule` page rather
      than duplicating stat text.
- [ ] `author:` is a resolvable `[[wikilink]]`, or explicitly states the
      document is anonymous/unattributed in-world.
- [ ] `form:` reflects the document's real genre (book, tome, letter,
      treaty, contract, recording, or inscription) — not left at the
      template default by accident.
