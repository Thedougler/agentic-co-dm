# Where a leg's material lands — the four-destination test

Run the test per finding, not per leg: one crossing can feed all four.

1. **What happens on this crossing** (the events, roles, toll, arrival) →
   the Route page's `## Read-aloud` / `## Checks`, or one plot-weight
   moment when the gate holds. Never a new passage file. The default;
   most travel is ephemeral and lands only here.
2. **Standing facts of the way itself** — a crossing the party will make
   again, a lane with its own traffic, duration, and hazards → a
   `type: route` page (`vault/_templates/_campaigns/_route.md`), authored
   by `.claude/skills/draft-content/references/route.md`, filed in
   `vault/campaigns/*/locations/`. This skill never writes it: flag the
   gap and hand over the hazards, waypoints, and durations the leg's prep
   surfaced. When the route page already exists, read it first — its
   `travel_time:`, `traffic:`, `hazard_level:`, and `## Hazards` are the
   leg's baseline, never re-invented.
3. **Recurring rolls** — hazards or finds worth a reusable table → a
   `type: table` page authored by `.claude/skills/draft-content/references/table.md`,
   wikilinked from the route page's `## Travel`/`## Hazards` (and its
   `encounter_table:` key). This skill supplies row seeds, never the page.
4. **A named entity with a future** — a rival captain, a recurring
   courier, a vessel, a beast → the npc, ship, or monster drafting guide per
   `travel-cross-skill-coordination.md`. A one-off name with no
   stated future stays inline in the moment.

Genuinely unsure whether a leg recurs or an entity returns → ask the DM
(the skill body’s § Degrade by asking), never coin-flip a page into existence.
