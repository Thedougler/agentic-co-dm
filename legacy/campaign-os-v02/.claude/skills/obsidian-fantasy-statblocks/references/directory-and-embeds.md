# The vault/campaigns/shattered-sea/monsters/{srd,homebrew}/ directories and embed convention

Every `statblock` fence in this vault lives on its own page under
`vault/srd/monsters/` or `vault/campaigns/shattered-sea/monsters/` (`vault/_templates/_srd/_statblock.md`)
— no other content type carries a fence inline. Two filename patterns, depending on
the page's shape:

- **A bare stat-block page** — `vault/campaigns/shattered-sea/monsters/{srd,homebrew}/<slug>.md`, bare
  slug. The page has nothing but the stat block — a straight monster entry with no
  separate origin page — so the file *is* the page, no suffix needed.
- **An extracted fence** — `vault/campaigns/shattered-sea/monsters/{srd,homebrew}/<slug>-statblock.md`,
  `-statblock` suffixed. A creature page (`vault/campaigns/shattered-sea/monsters/{srd,homebrew}/<slug>.md`)
  or NPC page (`vault/campaigns/shattered-sea/npcs/<slug>.md`) that has real prose beyond its stats —
  ecology, lore, lair/coven actions, relationships — keeps that page where it is;
  only the fence moves out, so the new page needs a distinct filename (the origin
  page already owns the bare slug — W57 flags a duplicate basename anywhere in the
  vault regardless of folder). A creature's extracted fence lands in
  `vault/srd/monsters/` or `vault/campaigns/shattered-sea/monsters/` matching whether that creature is
  SRD or homebrew — `.claude/skills/draft-content/references/monster.md`'s
  The Stat Block Placement Choice; an NPC page carries no such
  split, so an NPC's extracted fence always lands in `vault/srd/monsters/`.

## The embed

The origin page's `## Stats & Combat` section keeps any surrounding prose (a combat
summary, lair-action flavor) and replaces just the fence with a bare-slug embed —
never a directory-prefixed one, since Obsidian resolves `![[...]]` by basename
regardless of folder:

```text
![[<slug>-statblock]]
```

This is a standard Obsidian embed (`![[...]]`), not plugin-specific syntax — it
transclues the target note's rendered content, including the Fantasy Statblocks fence,
in place.

## Why the split

- **One creature, one bestiary entry, one place to edit it** — a lair boss's stat
  block used to sit duplicated or drifted across an encounter page and its own
  creature page; now every reference points at the same statblock page.
- **Bestiary scan and lint scope match exactly** — the plugin's "Bestiary folders"
  setting and the `w-statblock-simulatable` lint rule's scope both cover
  `vault/srd/monsters/` and `vault/campaigns/shattered-sea/monsters/`, so what's scanned/linted
  and what's authored are the same set (no folder mismatch to reason about).
- **`vault/_templates/_srd/_monster.md` and `vault/_templates/_campaigns/_npcs/_npc.md`**
  scaffold the embed line, not a bare fence — a page instantiated from either of these
  already follows this convention.
- The `⚔ Sim vs Party` button (`obsidian-shellcommands`) reads the *active file's*
  fence directly — it lives on `vault/_templates/_srd/_statblock.md`, not the creature/NPC
  template, since that's the only page guaranteed to contain a real fence.
