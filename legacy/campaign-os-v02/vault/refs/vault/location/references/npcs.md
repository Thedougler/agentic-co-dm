---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Resolve or spawn a stub for every NPC named on a location page — the wikilink-or-stub mechanic and the minimal stub content this skill is allowed to write."
created: "2026-08-03"
updated: "2026-08-03"
tags: [exploration]
uid: 1cc6c6ac-00fb-4571-8fbd-97a9371ac2ea
---

# Draft — Location, Notable NPCs

For every NPC named anywhere on this location's page:

1. Run the stub check for that name
   (`vault/refs/vault/_common/queries.md`).
2. **Hit** → wikilink to the existing page under `## Notable NPCs`. Done —
   this guide never edits another page's content.
3. **Miss** → spawn a pending stub:
   - Instantiate `vault/_templates/_campaigns/_npcs/_npc.md`, `status: draft`.
   - Fill only: the `<Name>` heading, `aliases:`, and one line of DM-only
     material on that stub: `Stub spawned by location prep from
     <location-slug>.md — needs a full npc pass (Toy Chest, Voice &
     Delivery, Relationships) before the table sees them.`
   - Leave every other section of the npc template empty. This guide
     never writes an NPC's Toy Chest, Voice & Delivery, or Stats &
     Combat — that minimal stub only guarantees the wikilink resolves
     (`npm run lint -- --rules` W3 hard-fails an unresolved
     link) and hands a clean starting point to
     `.claude/skills/draft-content/references/npc.md`.
   - Wikilink to the new stub from `## Notable NPCs` on this page.
4. Never leave an NPC as plain-text prose with no link — that's the
   violation this mechanic exists to close.
