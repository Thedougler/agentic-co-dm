# Cross-skill coordination

- **`.claude/skills/draft-content/references/npc.md`** — named/recurring antagonists (§ Named foe vs. generic
  creature fork, `.claude/skills/encounter-prep/references/named-foe-fork.md`). Also the source for a
  PC-Connection-bearing location's Notable NPCs, if this encounter's
  opposition already has a page there.
- **`.claude/skills/draft-content/references/monster.md`** — a generic/homebrew creature meant to recur across
  encounters (§ Named foe vs. generic creature fork). It owns both the page
  and the CR/stat-block design method
  (`vault/refs/vault/monster/references/cr-design.md`); this skill only
  cites those files for a one-off creature that stays inline.
- **`.claude/skills/draft-content/references/location.md`** — if the encounter's location has no wiki page and
  is significant enough to revisit, that guide creates it; wikilink it,
  don't inline a location description here.
- **`.claude/skills/draft-content/references/item.md`** — notable loot (named items, faction
  cargo, quest objects) tied to this encounter's outcome routes through that
  guide for DM-reviewed homebrew mechanics; don't invent item mechanics
  inline here.
- **`world-update`** — if the encounter's outcome would advance or set
  back a faction's front, name which front and flag it for that skill.
  Never advance a clock yourself (that skill's exclusive job,
  post-INGEST).
- **`draft-run-guide`** — the usual caller. It links and quotes this
  skill's output; it never re-derives an encounter's substance itself. The
  Standard queries PC-hook grep matches the shape that skill uses for its
  own party-state read, so the read stays consistent across the prep family.
- **`draft-moment`** — authors the moment files a run guide links, including
  cold-open frames, whose craft `writing-cold-opens` owns. Loads its own
  `.claude/skills/composing-beats/references/runtime-surface.md`, which loads this skill's
  `.claude/skills/encounter-prep/references/running-the-encounter.md` for any combat branch point's
  table adjudication (positioning, targeting, monster tuning) instead of
  housing that guidance itself.
- **`dnd5e-scene-narration`** — for the `[!read-aloud]` box that opens the
  encounter, if one is wanted. This skill states what the scene needs to
  convey (danger level, one anchor detail); that skill writes the
  paragraph.
- **`visual-aids`** — combat art (16:9, terrain/tactical layout
  emphasis), if that skill exists in this repo yet (registry's future slot
  for the legacy `ttrpg-visual-aids`). Skip silently if it isn't
  installed — never invent an ad hoc image-generation step in its place.
