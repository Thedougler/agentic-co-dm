---
type: reference
subtype: threads
status: canon
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: [visibility/internal]
owner_skill: ".claude/skills/world-update/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
campaigns: [Shattered Sea]
summary: "Campaign-wide index of every tracked Thread (Front), grouped by Active, Background, Dormant, and Resolved."
uid: a04927d9-0e6b-4385-ac1d-607bb491e547
---

# Threads

`world-update` self-creates this page from this shape if it's missing and
keeps it in sync every run (`.claude/skills/world-update/references/threads-and-spoilers.md`).
Non-canon derived index — every fact here already lives on the Thread's own
owning page (a faction or major/recurring NPC's `## Goals & Fronts`); this
page only mirrors current state so an agent can see the whole campaign's
pressure map without grepping every page.

Plain prose lines only — no tables, no callouts, wikilinks allowed. One
line per Thread:

```markdown
- [[owning-page|Thread Name]] — current state in one clause.
```

## Active

Thread's Lifecycle is `active` and the party is engaged with or aware of
it (this run's HOT or WARM triage tier).

## Background

Thread's Lifecycle is `active` but it's ticking unopposed, off the
party's radar (this run's COLD triage tier).

## Dormant

Thread's Lifecycle is `dormant` — waiting on a named trigger that hasn't
fired.

## Resolved

Thread's Lifecycle is `resolved` — kept as a one-line historical record,
never deleted.
