---
name: llm-wiki-status
description: >-
  The read-only health/status readout of a Campaign OS wiki (vault/ present). Use for "wiki
  status", "is the wiki up to date", "what hasn't been ingested", "how far behind is the
  wiki", "wiki health check", or which pages deserve `tier: core`/demotion. Reports only.
  Not llm-wiki-query.
---

# llm-wiki-status

Read-only: this skill never
edits a page, flips a status, or fixes a finding — every finding names the
owning skill to route to (L6).

Answers one question: **how far behind, and how healthy, is the wiki right
now?** — from the repo alone (ledger checkboxes, frontmatter, git log), never
from chat memory (L1). Paste every check's real command output in the same
turn; a number without its command is a guess.

## The report — run all four checks, paste `STATUS:` lines

1. **Pipeline delta** — per `vault/episodes/NNN/` dir, which phase gate is
   each session stuck at:
   - `ls vault/episodes/*/` — a dir with `transcript*.md` but no labeled
     speakers → CAPTURE done, label pending (`transcript-label`).
   - `vault/episodes/NNN/ingest-review.md` present with `REVIEWED-BY-HUMAN: (pending)` → ingested
     (pages already at `status: canon`), human spot-check owed → route
     `transcript-ingest`.
   - `grep -rln "status: pending" vault/` — pending pages awaiting
     review/promotion; count per session via their transcript wikilink.
   - `vault/episodes/NNN/sNN-recap.md` missing where `vault/episodes/NNN/ingest-review.md` exists → RECAP owed
     (`recap-writer`).
   - `STATUS: pipeline — <N> sessions, <list of session → stuck-at-gate>`.
2. **Frontmatter coverage** — count only, no per-page flags (W14 belongs to
   `llm-wiki-lint` — route there for the worked list):
   `grep -rLl "^summary:" vault/ --include="*.md" | wc -l` and the same
   for `tier:`. `STATUS: coverage — <N> pages missing summary:, <M> missing
   tier: (fix list: lint)`.
3. **Tier suggestions** (report-only — a human or the owning prep skill edits
   `tier:`, never this skill): incoming-link counts via
   `grep -roh "\[\[[^]|#]*" vault/ | sort | uniq -c | sort -rn` mapped to
   pages. ≥5 incoming links and not `tier: core` → suggest promote; ≤1 link,
   untouched 5+ sessions, not `peripheral` → suggest demote (thresholds:
   `llm-wiki` skill's `.claude/skills/llm-wiki/references/pattern.md` § tiering).
   `STATUS: tier — promote: <pages>; demote: <pages>; none`.
4. **Footprint** — `find vault -name "*.md" | xargs wc -w | tail -1`;
   flag when a full `vault/` read would strain a context budget and
   recommend leaning on the `summary:` rung and `peripheral` demotion
   (`llm-wiki` skill § ladder). `STATUS: footprint — <N> words across <M>
   pages`.

5. **Unconnected co-occurrence** (report-only): entity pairs that keep
   appearing together with no connecting canon —
   `grep -rl "\[\[<a>\]\]" vault/episodes/ | xargs grep -l "\[\[<b>\]\]"`
   over the most-linked entities from check 3; a pair co-occurring in ≥3
   session docs whose two pages never wikilink each other is a candidate
   hidden connection. `STATUS: co-occurrence — <pairs>; none`. Route: the
   owning prep skill or `canon-review` decides whether a link is real —
   never write one here.

## What to do next — close every report with this

Rank the findings into a capped action list (≤5 rows, highest first), one
`run:` per row; a healthy wiki gets the empty state, never invented work:

| Priority | Finding | run: |
|---|---|---|
| 1 | session past its gate (un-labeled / un-ingested / un-spot-checked) | the gate's skill (`transcript-label` / `transcript-ingest` / `transcript-ingest`) |
| 2 | open CONTRADICTION blocks | `canon-review` |
| 3 | lint-fixable coverage/link findings | `llm-wiki-lint` |
| 4 | tier promote/demote suggestions | owning prep skill (human call) |
| 5 | co-occurrence candidates | owning prep skill / `canon-review` |

Empty state: `STATUS: healthy — nothing owed; next session's PREP is the
only open loop.` Skipped-but-scored findings below the cap get one
`NOTED (not done):` line each.

## Boundaries

- Never run fixes inline — even a one-character frontmatter add belongs to
  the owning skill (diffuse authorship is failure mode #6).
- Never read page bodies for this report — frontmatter greps and `ls`/git
  suffice (retrieval ladder, cheapest rung).
- A contradiction or duplicate surfaced by accident → report and route
  `canon-review`; never adjudicate.
