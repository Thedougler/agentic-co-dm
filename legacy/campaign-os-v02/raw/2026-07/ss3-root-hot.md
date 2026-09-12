# Source ingest queue: ss3-root-hot

Source root: /Users/nick/ai-os/shattered-sea/wiki/hot.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:77 — `root ::
hot.md → map, don't duplicate — campaign-os equivalent is the session-
pipeline-phase tracking that existed at the time; mapping report, no wiki
page expected`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN:
2026-07-13 — same user instruction; blessing covers exactly the 14 lines
below" (Round 3 header, covers this line).
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] hot.md — triage: `internal-equivalent-check`
  (`references/claim-buckets.md` § Source types, row added post-Round-2 from
  this exact skill-gap: `ss-system-interview-guide.md` Flag #1). First
  scheduled use of that row — see verdict below for whether it held up.
  Treated as `skipped — mapping report only, no wiki page`, per the ledger
  line's explicit instruction.

## Claims

- none — mapping-verdict source, no claims list (same precedent as
  `ss-system-interview-guide.md`).

## Mapping verdict: (a) full equivalent exists — no wiki page

**Source content.** `hot.md` (frontmatter `type: system`, `subtype:
hot-file`, `status: active`, `audience: agent`, `publish: false`, summary
"Current world state, open threads, faction clocks, and predictions. Read
first, always.") is a hand-maintained DM cache with 8 sections: Recent
Activity (dated log of prep/cross-link/session edits), Current Arc (one-
paragraph "where the party is right now" prose), Open PC Threads (per-PC
narrative status), Faction Clocks (table: faction / clock / if-ignored /
next-trigger), Live Situations (table: situation / status / party-awareness
/ next-beat), Predictions (10 numbered DM forecast bullets), Spotlight
Tracking (per-PC spotlight-balance narrative), and Navigation (one link to
`hub.md`).

**Campaign-os equivalent — found directly, by name, not inferred.**
`.claude/skills/session-run-guide/SKILL.md:138-142`, Hard Rule 5:

> **There is no `hot.md`.** The legacy skill this one replaces assumed a
> hand-maintained world-state cache (Open PC Threads, Faction Clocks, Live
> Situations, Predictions, Spotlight Tracking); Campaign OS has no such
> file. Ground in current state by grep (Standard queries), never by memory
> of a state file, and never write one.

This is a stronger hit than the dispatch instruction's own hypothesis (the
session-pipeline-phase tracking that existed at the time) — that pair covers
only the *session-pipeline-phase* axis of "current state" (which
CAPTURE/INGEST/RECAP/CANONIZE/PUBLISH step a session is on), not hot.md's
*campaign-content* axis (clocks, situations, predictions, spotlight). The
real, deliberate replacement for the campaign-content axis is
session-run-guide's own architecture, confirmed section-by-section against
hot.md:

| hot.md section | campaign-os replacement | Evidence |
|---|---|---|
| Faction Clocks | Each faction's own `## Goals & Fronts` section (Front clock fields, `source-ingest` SKILL.md Hard Rule 4) | `world/factions/waveservants.md:52-60` — Front data lives on the faction page itself; when the source doesn't state clock mechanics, the page says so explicitly and flags a hand-off to `faction-prep`, rather than caching a snapshot elsewhere |
| Live Situations | Absorbed into the owning faction's Front (`claim-buckets.md`: "situations absorb into faction fronts by design") | Round 2/3 ledger lines executing exactly this absorption, e.g. `situation :: situations/dormant/sentinels-true-head.md` → DONE, folded into `world/factions/sentinels-of-the-eyrie.md`'s Front + DM Only |
| Open PC Threads | `pcs/*.md` Session Log + Arc Notes, read fresh via grep at PREP time | `session-run-guide/SKILL.md:182-184` Standard queries step 2: "active faction fronts, PC Arc Notes + Session Log" |
| Predictions / "what's in motion" | `session-run-guide/SKILL.md:185-188` workflow step 3: "Name what's already in motion... from what you just read" — computed fresh each PREP cycle, never cached, and explicitly barred from inferring past canon ("mark anything uncertain a proposal") | Same file, step 3 |
| Spotlight Tracking | `session-run-guide/SKILL.md:189-193` workflow step 4, "Spotlight check" — same mechanism (find the PC who's gone longest without a beat) rewritten as a live grep over `pcs/*.md` Session Log instead of a hand-maintained table | Same file, step 4 |
| Recent Activity (edit/prep log) | git log / `docs/campaign/MIGRATION-LEDGER.md` and per-session `state-changes.md` ledgers — the project's own "git is the version history" principle (CLAUDE.md, finish-the-job-stay-in-lane rule) | No single file mirrors hot.md's specific dated-bullet format, but the audit-trail *function* is git commit history, which this system treats as authoritative over any hand-written log |
| Current Arc | `session-run-guide/SKILL.md:185-188` step 3 (same "name what's already in motion" step covers this) | Same file, step 3 |
| Faction-clock/situation *session-pipeline* state (which phase a session is on) | the session-pipeline-phase tracking that existed at the time | this is the one slice of hot.md's job (an agent's "where are we" orientation) that the dispatch instruction's hypothesis correctly named, though it's process-phase state, not campaign-content state |
| "At a glance" live view across factions/quests/NPCs | `docs/dashboards/*.base` + `docs/dashboards/dm-hub.md` | `architecture.md:134-148` — frontmatter-only queries (`status`, `quest_status`, `tags`, `touched`); confirmed these never read markdown body text, so they replace hot.md's *browsing* function, not its narrative content |

**Correction to the dispatch instruction's premise.** The task named
`world/_meta` as a dashboard location; that directory (`world/_meta/index.md`,
`aliases.md`, `tags.md`) is an auto-generated orphan/alias/tag index, not a
DM dashboard. The actual DM dashboards live at
`docs/dashboards/*.base` + `dm-hub.md` per `architecture.md:134` (chosen
specifically because `docs/` sits outside the wiki-lint tool's configured
wiki roots).
Flagged here as a one-word location correction, not acted on (this
ledger line's scope is hot.md only).

**Outcome: no wiki page written.** No `world/`, `pcs/`, or `prep/` file
created or modified by this ingestion. No orphaned campaign facts are being
routed as claims: hot.md's actual campaign-content values (e.g. the specific
mid-campaign Faction Clock text for Dravosi Crown, The Passage, Grung/Simone,
Umberlee/Waveservants; the 10 Predictions; the Open PC Threads for Perrin,
Delmar, Jean-Claude, Crissdalynn, Catarina) are table-state snapshots that
belong on entity pages this repo hasn't migrated yet (no `pcs/` pages exist;
`dravosi-crown`, `the-passage`, and the political Grung-faction page — as
opposed to the `grung` species-lore page that already exists — are not
migrated; the two factions that *are* migrated, `waveservants` and
`sentinels-of-the-eyrie`, already carry their own Front data from their own
dedicated source files, not from hot.md) — consistent with the ledger line's
own "mapping report, no wiki page expected" disposition. A future migration
wave that lands `dravosi-crown`, `the-passage`, PC pages, etc. is the correct
place to re-derive their current-state facts from primary session sources
(session logs, not hot.md's secondary rollup), per Hard Rule 5's own
"ground by grep, never by a cache file."

## Internal-equivalent-check row: did it hold up on first scheduled use?

Yes, cleanly — and better than its origin case. `ss-system-interview-guide.md`
(the row's origin) could only compare against an external, uninspectable
plugin skill (`dnd5e-character-interview`, not present on local disk) and
had to reason from a one-line registry paraphrase. Here the comparison
target (`session-run-guide/SKILL.md`) is a local file, fully readable, and
it names `hot.md` by filename and lists its exact section set
verbatim — turning this from an inferred mapping into a confirmed one. The
row's own instruction ("check skills-registry.md and installed skills
first; full match → mapping report only, no page") worked exactly as
written once I searched past the dispatch instruction's own named
candidates (the session-pipeline-state tracking) and grepped more broadly for
`hot.md`/`Predictions`/`Spotlight` across `.claude/skills/`.

## Flags

- none — no relink deferrals (hot.md's wikilinks were never written to any
  page in this repo, since no page was created); no orphaned-claim routing
  (see Outcome above); no skill gap (the triage row worked).
