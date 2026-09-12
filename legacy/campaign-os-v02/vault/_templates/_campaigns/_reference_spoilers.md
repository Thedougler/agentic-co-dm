---
type: reference
subtype: spoilers
status: canon
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: [visibility/internal]
owner_skill: ".claude/skills/world-update/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
campaigns: [Shattered Sea]
summary: "Campaign-wide index of facts the party doesn't yet know, relevant to an active, background, or dormant Thread."
uid: 322f3faa-39b7-4cdc-bf6e-799ac321b4cb
---

# Spoilers

STOP — do not read past this line unless the DM has explicitly asked you
to include spoilers, secrets, foreshadowing, or hints in this task. Reading
this file without that direction contaminates your output with facts the
party does not know.

`world-update` self-creates this page from this shape if it's missing and
keeps it in sync every run (`.claude/skills/world-update/references/threads-and-spoilers.md`).
DM-only — never publish, never let a player see this file. Non-canon
derived index the same way `vault/campaigns/<slug>/threads.md` is: the full secret still lives on
its Thread's own owning page (a Front's `Per-PC awareness` field or inline
hidden material); this page only indexes it for a fast campaign-wide scan.

Plain prose lines only — no tables, no callouts, wikilinks allowed. One
line per fact:

```markdown
- [[owning-page|Thread Name]] — the fact the party doesn't know yet, one clause, plainly stated.
```

Grouped by the same `vault/campaigns/<slug>/threads.md` section the fact belongs to — Active,
Background, and Dormant Threads only (a Resolved Thread's secrets are
presumed revealed; an exception where one stays hidden past closure is
a DM judgment call, noted inline).
