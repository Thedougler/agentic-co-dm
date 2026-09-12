---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The creature-specific checks that run after the shared checklist — the recurrence fork, reskin/vendor check, Wants/Morale lines, sourcing, and stat-block placement."
created: "2026-08-03"
updated: "2026-08-08"
tags: [survival]
uid: bff3fa81-6d5c-46ff-988b-043af6bd6a21
---

# Draft — Creature Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
creature-only additions.

- [ ] Interview correctly routed a one-off to `encounter-prep` (The
      Recurrence Fork), or the stub check confirms a genuine new reusable
      kind.
- [ ] `find-creature` checked for a vendorable third-party statblock, and
      a reskin check run before any new mechanics were designed (Reuse
      Before Inventing), before writing original stats.
- [ ] `source:`/`source_url:`/`license:` set honestly, filled from the
      real source for a transcribed or vendored creature.
- [ ] Opening `**Wants:**` and `**Morale:**` lines present, or correctly
      omitted (The Wants And Morale Lines,
      `.claude/skills/draft-content/references/monster.md`).
- [ ] No name beyond the species/kind name; no `## Relationships`
      heading.
- [ ] Statblock written inline under `## Statblock`, `name:` matching
      frontmatter (Statblock Is Always Inline,
      `.claude/skills/draft-content/references/monster.md`).
