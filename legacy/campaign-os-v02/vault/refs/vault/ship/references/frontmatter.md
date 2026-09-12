---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The ship_class, tier, and home_port frontmatter keys and their allowed values."
created: "2026-08-03"
updated: "2026-08-08"
tags: [maritime]
uid: 8d0f1e11-40f0-4f7b-92e2-e604b657bdcc
---

# Frontmatter: ship_class, tier, and home_port

`vault/_templates/_srd/_ship.md` declares three `ship`-specific frontmatter keys: `ship_class` (free
text, open vocabulary — "war proa," "carrack," whatever the setting calls it, not an
enum), `tier` (enum and optionality per the template's own comment — fill it once the
Tier Comes First rule has run), and `home_port` (per the template comment, a wikilink
to a `location` page, unvalidated the same way an npc's `location` key is — a fact
about the world, not a closed set). The template
pre-fills all three as empty placeholders; fill them during the interview, don't leave
them blank on a page you're calling `pending`. No other ship fact gets a frontmatter
key — crew, cost, and acquisition stay in the Ship Toy table and body prose, same
no-frontmatter-duplication reasoning `.claude/skills/draft-content/references/item.md`'s `one_thing`/`rarity_justification`
already established for its own Toy fields.
