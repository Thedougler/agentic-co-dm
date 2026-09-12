---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "World-only checklist additions, run after vault/refs/vault/_common/checklist.md on any vault/worlds/ page."
created: "2026-08-04"
updated: "2026-08-04"
tags: [exploration]
uid: 53e2aa11-0123-46fc-8a41-733072d70fa5
---

# Draft — World Checklist

Runs after `vault/refs/vault/_common/checklist.md`, never instead of it.

- [ ] `subtype` matches what the page actually is (the template's enum,
      `vault/_templates/_world.md`).
- [ ] `current_date` is present and sorts (The World's Clock,
      `.claude/skills/draft-content/references/world.md`).
- [ ] Every region in `## Geography` with real content of its own has its
      own page and is wikilinked; every deity in `## Faith & Pantheon` with
      real presence at the table does too (A World Holds, It Does Not
      Detail, `.claude/skills/draft-content/references/world.md`).
- [ ] `## Campaigns in This World` lists every campaign whose page carries
      `world:` pointing here — and no campaign page pointing here is
      missing from the table.
- [ ] `subtype: published`/`hybrid` -> `## GM Notes` states the inheritance
      boundary and any licensing constraint
      (`.claude/skills/draft-content/references/world.md` § Hard rules).
- [ ] Homebrew added to a published world follows the bordering rule
      (Homebrew Borders Canon, Never Overwrites It,
      `.claude/skills/draft-content/references/world.md`).
- [ ] `### Tenets` holds three to five entries — more than five means the
      world is doing a campaign page's job
      (`.claude/skills/draft-content/references/world.md` § Interview).
