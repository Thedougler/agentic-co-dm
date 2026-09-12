---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The location-only checks run before calling any location page done, on top of the shared draft checklist."
created: "2026-08-03"
updated: "2026-08-07"
tags: [exploration]
uid: 34cff7ed-ab06-4ad5-ac96-1243358a1e5e
---

# Draft — Location Checklist

Run in addition to `vault/refs/vault/_common/checklist.md`; never
restate one of its items here.

- [ ] `subtype:` frontmatter set to the real value, not the template's
      placeholder.
- [ ] `within:` set, quoted, no alias, resolving to a real page
      (`vault/refs/vault/location/references/placement.md`).
- [ ] All four `north_of`/`east_of`/`south_of`/`west_of` keys set, quoted,
      resolving to real pages — never empty, never "open water"/"none"
      (`vault/refs/vault/location/references/placement.md`).
- [ ] Every space (main location, sub-locations, dungeon rooms) has a
      "no space without a past" answer — no empty entries.
- [ ] Every Notable NPC resolves or was stubbed per
      `vault/refs/vault/location/references/npcs.md` — none left as unlinked
      plain text.
- [ ] Dungeon subtype: phase gates respected, Chokepoint Test run, Three
      Clue Audit present if a hidden conclusion exists
      (`vault/refs/vault/location/references/dungeon.md`).
- [ ] Settlement or region subtype, including a district or island:
      checklist addendum in `vault/refs/vault/location/references/settlement.md`
      or `vault/refs/vault/location/references/region.md` run — every OPTIONAL
      heading kept only where its condition holds, every child page
      carries at least one real fact of its own.
