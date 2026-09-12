# Cross-skill coordination

- **`encounter-prep`** — every Red/combat event and any event whose stakes
  carry real DC-tiered drama. Hands back a Toy table, Enemy Roster, and/or
  Drama Suite; this skill quotes it, never rebuilds it.
- **`.claude/skills/draft-content/references/route.md`** — the way's standing facts
  (duration, traffic, hazards) when a leg recurs: this skill flags the gap
  and hands over what prep surfaced; the guide authors the `type: route`
  page. An existing route page is the leg's baseline, read before any
  event is derived.
- **`.claude/skills/draft-content/references/table.md`** — a leg's reusable encounter
  table (`type: table`), wikilinked from the route page; this skill
  supplies row seeds only.
- **`.claude/skills/draft-content/references/npc.md`** — any named entity (rival captain,
  recurring courier, faction contact) the leg introduces that might
  reappear.
- **`.claude/skills/draft-content/references/ship.md`** — a rival vessel, hazard-worthy
  hull, or the leg's own ship needing a real page (stats, crew, tier).
  This skill flags the need; the ship guide authors the page.
- **`.claude/skills/draft-content/references/location.md`** — a destination or waypoint
  place that needs its own page; this skill owns only what happens on the
  way.
- **`draft-moment`** — authors the leg's travel moment from the finished
  events, journey slots, and roles (`route-escalation.md`,
  path 1).
- **`draft-run-guide`** — decides whether tonight involves a leg at all
  and how many, and hands each leg's situation to `draft-moment` in run
  order; this skill never decides session pacing.
- **`roll-dice`** — every in-fiction resolution roll (role checks, hazard
  checks, opposed rolls), result read and cited per Hard Rule 2. Event
  selection never rolls (the skill body’s § Deriving events from the party).
- **`dnd5e-scene-narration`** — the `[!read-aloud]` box that opens the
  travel moment; this skill states what it must convey (danger level, one
  anchor detail, the landmark); that skill writes the paragraph.
- **`world-update`** — an event outcome that would advance or set back a
  faction's front: flag which front; never advance a clock here.
