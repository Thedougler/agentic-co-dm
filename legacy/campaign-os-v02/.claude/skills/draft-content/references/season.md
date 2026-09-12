
# Draft — Season

Turns "this session felt like it ended something" or "what season are we
in" into a template-conforming `type: season` page. A season groups
consecutive sessions under one throughline; its close is always a GM
decision, from the Method 4 finale check below — never inferred from
pacing or session count. No external genre exists to ground this
construct against: treat the GM-craft arc/front methodology
cited below as the real standard, not a TV-season convention.

## Template

`vault/_templates/_episodes/_season.md` — copy it, never retype it from
memory.

## Story-first entry (default)

Opening a season is narrative-scale: the default entry is the
`draft-story` skill — a flowing chapter at
`vault/stories/season-NN-<slug>.md`, QC'd and DM-approved, that this
guide then derives the page from (throughline, fronts on stage, PC arcs,
and the Finale come out of its fiction; the story's *Derived pages* line
gains this page's wikilink). Updating or closing an existing season needs
no story. The DM may skip the story on their word, not by default.

## Boundary (read before doing anything)

- **Not a quest.** A quest (`.claude/skills/draft-content/references/quest.md`) is one
  storyline/mystery/objective; a season is the chronological span
  several quests can run inside. "The hunt for <the artifact>" is a
  quest; "everything from session 1 to <the artifact>'s fall" is the
  season it closes.
- **Not the campaign overview.** `.claude/skills/draft-content/references/campaign.md` owns the setting-wide
  premise, Truths, and Icons — those don't change per season. A season
  page never restates them, only links the campaign page once in
  Overview.
- **Not a session recap.** `recap-writer` owns what happened in one
  session, ledger-derived. This page only lists sessions and one-line
  outcomes (§ Output structure) — never re-narrates them.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` (PC-Connection Requirement,
   ask-don't-invent) and `.claude/skills/composing-beats/references/audits.md`
   (Pressures-Not-Plots, If-Ignored) — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. `vault/refs/ideas/spiral-campaign-development.md` — the campaign
   Fronts method.
4. Standard queries: `grep -rl "type: season" vault/campaigns/shattered-sea/seasons/`,
   `grep -rl --include="*.md" "season_status: active" vault/campaigns/shattered-sea/seasons/`,
   `grep -rn --include="*.md" "Front" vault/campaigns/shattered-sea/factions/ | grep -i "active\|dormant"`,
   `grep -rl --include="*.md" "quest_status: active" vault/campaigns/shattered-sea/quests/`.
   The last two surface the fronts and quests a season can put on stage.
   An active-season hit means work belongs on that page — never create a
   second season page while one is still active for the same campaign.
   No hit and the campaign has no season pages yet: this is Season 1,
   `number: 1`, starting at session 1. Naming a PC, front, or quest in
   prose also runs the generic entity stub check,
   `vault/refs/vault/_common/queries.md`.

`DS1: <files read, query output pasted>`.

## Hard rules — this type only

- **One Active Season.** Creating a season page -> run § Read first's
  queries — one active season per campaign at a time.
- **Finale Names A Concrete Event.** Flipping `season_status: active` ->
  the Finale/End Condition section must name a concrete planned event
  with a yes/no answer for "has this happened yet" — never "when it
  feels done"; the Finale is a GM decision, never inferred.
- **Complete Only On Evidence.** Setting `season_status: complete` ->
  confirm Finale's Reached field cites the actual session it happened in
  first — never pre-emptively.
- **Sessions Table Is Played-Only.** Adding a row to the Sessions table
  -> only for a session that's already been played, never pre-fill one
  that hasn't happened yet, even if planned.
- **Tier Facts Are Observed, Not Projected.** After each session -> set
  `dnd_tier` and `level_range` from the party's actual level, updating
  `level_range` as sessions land rather than projecting ahead. 5e tier
  boundaries: tier 1→2 at level 5, 2→3 at level 11, 3→4 at level 17 — a
  level crossing one of these with no open season covering it opens a
  new one.
- **Sequential Numbering, No Gaps.** Opening a new season -> confirm the
  prior one is `complete` first.
- **Fronts Link, Never Restate.** A front's clock, ticks, or other detail
  copied onto the season page is the violation Method 2's concrete test
  below catches — link the owning page instead.

## Method

A season is the Narrative Islands archipelago
(`.claude/skills/writing-narrative-islands/SKILL.md`) at season scale: set
pieces held in flexible position, the route between them improvised. What
separates a season page from a session ledger — apply all four before the
page counts as complete:

1. **Throughline as pressure, not plot.** One line framing the question
   the season is built to answer — a pressure that would advance
   without the party ("can <the city> survive <the coming event>?"), never
   a planned party action ("the party stops <the faction>"). Pressures-Not-
   Plots, `.claude/skills/composing-beats/references/audits.md` §1.
2. **Fronts on stage — at most three.** A season names which of the
   campaign's fronts (faction Fronts, active quests, environmental
   threats) are advancing during its span, and where each stands at the
   season's current edge. Up to three at a time, per
   `vault/refs/ideas/spiral-campaign-development.md` § Campaign Fronts.
   Each front links its owning faction/quest page — the clock and its
   ticks live there, never duplicated here. Concrete test: any number
   (clock size, timeline, casualty count) copied from the owning page
   into a season cell is the violation — wikilink that page's section
   instead. One clause per cell. A live pressure with no owning page →
   hand off to `.claude/skills/draft-content/references/faction.md`/
   `.claude/skills/draft-content/references/quest.md` first, then link the result.
3. **PC arcs — one row per PC.** The specific pull this season exerts on
   each PC: backstory, wound, goal, or mystery, with the session where
   it last moved. PC-Connection Requirement,
   `.claude/skills/composing-beats/references/runtime-surface.md` §2 — state the mechanism, not
   "ties into their arc". Opening a season: ask the DM for any PC with
   no evident pull, all open questions batched at once. Updating: derive
   from played recaps, never invent.
4. **Finale that survives the anti-railroading check.** The planned end
   condition plus: **Routes** — at least two distinct player paths that
   could reach it (a finale requiring one specific choice is a railroad,
   `.claude/skills/composing-beats/references/audits.md` top-of-file check) — and
   **If ignored** — the concrete consequence if the party never pursues
   it (`.claude/skills/composing-beats/references/audits.md` §4), one line; when the
   owning location/quest page carries its own If-ignored section,
   wikilink it rather than restating its chain. A finale with no
   if-ignored line is a scene waiting for permission, not a pressure.
   A finale is a tentpole: it moves to meet a party whose path runs elsewhere.

## Output structure

What belongs under each of the template's six H2s, and what this type
leaves to another guide: `vault/refs/vault/season/references/output.md`.

## Before you ship

1. **Opening a season** — no active season exists: instantiate
   `vault/_templates/_episodes/_season.md`, `number:` = prior season's + 1
   (or 1), carry `dnd_tier`/`level_range` forward from the party's
   current level, work § Method 1–4 (throughline, fronts, PC arcs,
   finale), and ask the DM — batched — for the Finale plus any PC pull
   or front standing the wiki can't answer, before setting
   `season_status: active`.
2. **Updating a season** — an active season exists and a new session
   just landed: append one row to `## Sessions`, refresh each front's
   standing in `## Fronts on Stage` and any PC-arc row the session
   moved, refresh `level_range` if the party leveled.
3. **Closing a season** — a session's recap matches the open season's
   planned Finale: fill **Reached** with that session, set
   `season_status: complete`, flip `status:` to `pending` once the page
   reads clean. Ask whether this also crosses a tier boundary before
   the next season opens.
4. **Hand off** — `.claude/skills/draft-content/references/quest.md` for any storyline
   running inside the season; `.claude/skills/draft-content/references/campaign.md` if the setting-wide
   premise itself changed (rare, not a season concern).

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Owned paths

`vault/campaigns/shattered-sea/seasons/season-NN-<slug>.md` (zero-padded,
sequential — `season-01-...`, `season-02-...`). `status: draft` while
incomplete, `status: pending` once table-ready. Never sets `status:
canon` or `publish: true` — but freely updates `season_status: planning
| active | complete` itself, the same way
`.claude/skills/draft-content/references/quest.md` owns `quest_status` on its own pages.
