# threads.md and spoilers.md — the campaign-level index

Two singleton pages per campaign, both owned by this skill:
`vault/campaigns/<slug>/threads.md` and `vault/campaigns/<slug>/spoilers.md`
(`<slug>` from the Gate — `shattered-sea` for this repo). Both mirror
state that already lives on a Thread's (Front's) own owning page — a
faction or major/recurring NPC's `## Goals & Fronts` — so they carry no
independent canon of their own, the same way `vault/campaigns/shattered-sea/dm-hub.md` carries none.

## The one narrow exception to Hard Rule 2

Hard Rule 2 ("never edit `vault/` directly") still governs every Front's
own page — this skill only ever proposes those edits via the world-turn
ledger. `vault/campaigns/shattered-sea/threads.md` and `vault/campaigns/shattered-sea/spoilers.md`
are the sole exception: write them directly, no ledger line, no `canon-review` step. Nothing asserted on
either page is new — every line traces to a Front already read this run,
so there's nothing for a human to review that the Front's own page (and
this turn's citations) hasn't already carried.

## Self-create if missing

Before Step 1's triage (SKILL.md), check both paths exist:

```bash
ls vault/campaigns/shattered-sea/threads.md vault/campaigns/shattered-sea/spoilers.md 2>/dev/null
```

Missing one or both → instantiate from
`vault/_templates/_campaigns/_reference_threads.md` /
`vault/_templates/_campaigns/_reference_spoilers.md` (copy, don't retype
from memory) before continuing. Say so in the run's output — a first-run
self-creation is worth flagging, not silent.

## Rebuild timing

Rebuild both pages from the Standard queries' read **during Step 1
triage**, before proposing any advance — they reflect current canon/pending
Front state as read this run, not this run's proposed-but-unapplied
advances. They'll read one run stale until the next `world-update` run
after `canon-review` applies this turn's ledger; that's an acceptable
gap, not a bug — never backdate them to a future state nobody's confirmed
yet.

## Building threads.md

One line per Thread collected in the Standard queries, filed under the
section matching Lifecycle + this run's triage tier (`clock-advance-workflow.md`
§ Step 1):

| Section | Condition |
|---|---|
| Active | `Lifecycle: active`, triage tier HOT or WARM |
| Background | `Lifecycle: active`, triage tier COLD |
| Dormant | `Lifecycle: dormant` |
| Resolved | `Lifecycle: resolved` |

Line shape: `- [[owning-page|Thread Name]] — current state in one clause`
(clock position for active/background, the trigger it's waiting on for
dormant, the outcome for resolved). Plain prose, wikilinks only — no
tables, no callouts, no restating the Front's full field set.

## Building spoilers.md

For every Active, Background, or Dormant Thread whose owning page states
something the party doesn't yet know (a `Per-PC awareness` field, inline
hidden material per `.claude/skills/draft-content/references/faction.md`'s Front template), one line: `-
[[owning-page|Thread Name]] — the fact, plainly stated, one clause`. Skip
a Thread with nothing hidden — most Fronts are openly visible and need no
entry. A Resolved Thread is skipped by default (its secrets are presumed
revealed by the resolution); a genuine exception (a secret that outlives
its Front's resolution) gets a line same as any other, noted as such.

## Never touch either page outside this skill

Both pages exist only to save an agent a grep sweep across every faction/NPC
page — never hand-edit them mid-session, never let `.claude/skills/draft-content/references/faction.md` or any
other skill write to them (`.claude/skills/draft-content/references/faction.md` defines a Front on its owning
page; it doesn't touch the index). If either page looks stale or wrong,
the fix is running `world-update` again, not editing the index by hand.

## player-gravity.md — read-only for agents

`vault/campaigns/shattered-sea/player-gravity.md` lists per-player gravity (what
each player consistently bites on). It is DM-curated — never edited by
an agent without explicit DM approval. Read it before prepping a session,
writing a moment, or designing an encounter, but never write to it.
