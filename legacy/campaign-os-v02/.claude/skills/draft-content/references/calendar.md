
# Draft — Calendar

A timekeeping **system**: its units, its holidays, its moons, its
seasons. Absorbs every calendar, month/holiday structure, timekeeping
system, and moon/season cycle concept that used to have nowhere typed to
live. The [[campaigns/shattered-sea/lore/campaign-timeline|campaign timeline]] states its own reckoning, Dalereckoning (DR), as a calendar fact in
passing on a history page. That fact is this type's shape now. Done
means the DM can state any in-fiction date in this calendar's own units
from this page alone.

## Template

`vault/_templates/_campaigns/_calendar.md` — copy it.

Headings fixed and in order: `## Overview` · `## Structure` ·
`## Intercalary Days & Leap Rule` (OPTIONAL, delete outright if every day
falls inside a normal month and no day is ever added or removed on a
cycle) · `## Holidays & Observances` (OPTIONAL, delete outright until a
real holiday has content).

Then `## Moons` (OPTIONAL, delete outright if this setting has no moon
worth tracking) · `## Seasons` (OPTIONAL, delete outright if this
setting has no seasons distinct enough to matter at the table).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this
   type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste
   the output.

`DCL1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **System, Not Sequence: The Calendar/Lore Boundary.** This type owns
  the timekeeping system: months, days, weeks, years, holidays, moons,
  seasons, the structure a date gets expressed in. It never owns the
  sequence of things that actually happened; that stays `type: lore` (a
  `## History` timeline, e.g. the campaign timeline page linked above). A
  page that starts listing dated events in prose has drifted into `lore`
  territory. Wikilink the lore page instead of restating its entries
  here.
- **Never Assume Earth's Units.** No 24-hour day, no 7-day week, no
  12-month year, no single moon, and no four seasons is ever the
  default. Each is this setting's own invented or borrowed count, stated
  in `## Structure` from what the interview actually establishes. A
  blank answer is a question to ask, never a value to assume.
- **One System Per Page.** A culture, faith, or region with its own
  distinct reckoning gets its own calendar page, `within:` the world or
  region it's used in, never a second "alternate calendar" section
  bolted onto an existing page. Multiple calendars in one setting are
  normal; a civil calendar and a religious one rarely agree.
- **`reckoning` And `current_date` Belong To This Page, Not The World's.**
  A `world` page's own `current_date` (`.claude/skills/draft-content/references/world.md`)
  stays a coarse year for orientation. This page's `current_date` is the
  authority for the full date in this calendar's own units. The two
  must never contradict: if the world page states a year, this page's
  date falls in that same year.
- **Holidays State What A Party Feels.** Every row in
  `## Holidays & Observances` names what a party passing through would
  actually see or do, not just what the holiday is called (the
  Creative-domain rider, `vault/refs/vault/_common/hard-rules.md`).

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Whose calendar is this: one culture, one faith, or the whole setting?
  Sets `within:`.
- What is this calendar's epoch, the fixed point it counts years from,
  and why that point? Sets `reckoning`.
- Working up from the smallest unit this setting actually uses (a day,
  or its own name for one) to the largest: what units exist, what are
  they called, and how many of the smaller unit make one of the next?
  Fills `## Structure`. Never assume a week-level grouping or a
  12-month year exists; ask.
- Any days that fall outside the normal month structure, or any rule
  that adds or removes a day on a cycle? Fills
  `## Intercalary Days & Leap Rule`. None yet -> delete the heading.
- Any named holidays yet, and what does each one actually look like at
  street level? Fills `## Holidays & Observances`. None yet -> delete
  the heading.
- Any moons, and does their cycle mean anything at the table, such as a
  tide or a timed ritual window? Fills `## Moons`. None -> delete the
  heading.
- Any seasons distinct enough to change what a party can do? Fills
  `## Seasons`. None -> delete the heading.
- What is the date right now? Sets `current_date`.

## Before you ship

- [[lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Calendar checklist: `vault/refs/vault/calendar/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/draft-content/references/world.md` | Deciding what belongs on the world page's own `## History & Calendar` line versus a full calendar page |
| `.claude/skills/draft-content/references/lore.md` | Deciding whether a dated entry belongs here (the system) or on a `lore` timeline (the sequence) |
| `vault/refs/vault/calendar/references/checklist.md` | Calendar-only checklist additions |
