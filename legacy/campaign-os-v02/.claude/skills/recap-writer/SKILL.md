---
name: recap-writer
description: >-
  Draft the table's recap/highlights pages plus the DM's private retrospective, in a Campaign OS
  repo (vault/ present) — turns fresh canon into player-facing prose right after INGEST.
  Fires on "write the recap", "recap session NN", "run RECAP", "session retro", or an
  `ingest(sNN)` commit with no recap pages yet. Sole writer of sNN-recap.md, sNN-highlights.md,
  retrospective.md.
---

# Recap Writer

Phase 5 of the session pipeline (`vault/refs/runbook-recap.md`; runbook
`vault/refs/runbook-recap.md`). Turns this session's just-ingested `status:
canon` pages (the `ingest(sNN)` commit's touched pages) plus the frozen
transcript into two player-facing pages: `vault/episodes/NNN/sNN-recap.md` (prose, 300–450
words) and `vault/episodes/NNN/sNN-highlights.md` (3–8 verbatim
quotes + 1–3 one-line moments, L-number cited) — the sole writer of both (`vault/refs/runbook-wiki.md` § Who writes
what). `vault/episodes/NNN/sNN-recap.md`'s closing line is the draft source for the next
session's run-guide Recap box, which hands straight into that session's opening moment
(`vault/_templates/_episodes/_session_recap.md`,
`.claude/skills/draft-content/references/run-guide.md` § Recap → opener coupling) — write it as a handoff, not an ending.

Drafts staged by `draft-story` (step 2 in `draft-story`'s handoff checklist)
land in `vault/episodes/NNN/recap-draft.md` for this skill to promote (§ Two ways in).

## Scope boundary (read this first)

This skill never cascades updates into situation files or
the repo-root `CLAUDE.md` party block. That cascade — clock advances,
situation status, the CLAUDE.md arc line — belongs to `world-update` and
`transcript-ingest` exclusively. If you notice CLAUDE.md drifting from what
the recap says, name the gap to the user and point at `world-update`; do
not write that file yourself, even "just this once." This skill produces
three files: `vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md`
(mandatory, player-facing) and `vault/episodes/NNN/retrospective.md`
(optional, DM-only — see § Retrospective).

## Gate (check before touching anything)

```bash
git log --oneline | grep "ingest(sNN)"
```

Paste the hit. No hit → stop, tell the user INGEST is the missing upstream
step, offer to run it. `vault/episodes/NNN/ingest-review.md` may still carry a
`REVIEWED-BY-HUMAN: <date>` spot-check line at this point — a bonus
signal, not the gate itself: per `vault/refs/runbook-ingest.md`, that file is
deleted at the same step the `ingest(sNN)` commit lands, so its absence is
the normal end state, not a stalled review. Do not draft "just a quick
pass" ahead of the gate — the human can override explicitly ("write it
anyway"), in which case note `GATE-OVERRIDDEN by user` in your response.

## Standard queries

```bash
git log --oneline | grep "ingest(sNN)"
git show --stat <ingest(sNN) commit hash>
cat vault/episodes/NNN/ingest-review.md 2>/dev/null
cat vault/episodes/NNN/recap-draft.md 2>/dev/null
find vault/campaigns/shattered-sea/episodes -name "s*-recap.md" 2>/dev/null | sort | tail -3
grep -ril "<entity-name>" vault/ 2>/dev/null
grep -rl "<entity-name>" vault/ --include="*.md" 2>/dev/null | xargs grep -l "^aliases:" 2>/dev/null
```

Query 2 builds the pool `vault/episodes/NNN/sNN-recap.md` may draw from: every `vault/`
page the `ingest(sNN)` commit's diff touched carries this session's new
facts at `status: canon` — that's the evidence trail. Query 3 falls back
to `vault/episodes/NNN/ingest-review.md`'s
`Pages touched` worklist when the file hasn't been deleted yet (see Gate).
Query 4 checks for a staged draft before starting from scratch; query 5
pulls the most recent prior recap for voice/tone continuity; queries 6–7
resolve every named entity to a wikilink before it goes in either file.

## Two ways in

Either **fresh** (no `vault/episodes/NNN/recap-draft.md` — read this session's canon pages and
transcript directly) or **promote a staged draft** (`vault/episodes/NNN/recap-draft.md`
already exists from `draft-story` —
read it, re-verify every claim yourself, fold into `vault/episodes/NNN/sNN-recap.md`, delete the
draft once promoted). A legacy-sourced session (`vault/episodes/NNN/transcript.md` starts
`LEGACY-SOURCE: <path>`) is a fresh-path variant — adapt the existing
prose rather than reconstructing new prose from scratch. Full branch
detail: `references/two-ways-in.md`.
`vault/episodes/NNN/sNN-highlights.md` is always originated by this skill either way — no sibling
skill stages highlights content.

## Hard rules

Full text and rationale for each rule: `references/hard-rules-detail.md`.

1. **`vault/episodes/NNN/sNN-recap.md` is canon-derived, not memory-derived.**
2. **`vault/episodes/NNN/sNN-highlights.md` quotes are transcript-derived and verbatim.**
3. **`vault/episodes/NNN/sNN-recap.md` is 900–1350 words** —
   hook by sentence two on the session's sharpest image; scene-quality beats
   for the full time; close on tonight's hook. Under 300 is thin. Over 450
   lost the room. The `recap` QC profile's SPEAKING-TIME / ATTENTION / BREVITY rows own it.
4. **3–8 quotes, 1–3 moments on `vault/episodes/NNN/sNN-highlights.md`.**
5. **Never flip `publish: true` or set `status: canon`.**
6. **`vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md`: both or neither.**
7. **In-world filter applies to highlights, not recap.**
8. **Wikilink every named entity on first mention**, in both files.
9. **Correct `created`/`updated` frontmatter.**
10. **Degrade by asking**, not guessing (see below).

## Workflow

1. **Gate check.** Run the gate query above, paste the hit. No hit → stop
   (see Gate).
2. **Gather inputs.** Run the standard queries. Read every page the
   `ingest(sNN)` commit touched in full (each carries a wikilink back to
   the transcript — that's your evidence trail). Read
   `vault/episodes/NNN/transcript.md` around each cited passage for color
   and exact wording. If `vault/episodes/NNN/recap-draft.md` exists, read it too (see Two ways in).
   Read the most recent prior `vault/episodes/NNN/sNN-recap.md` for voice and tone continuity —
   this skill writes prose, but stays a consistent narrator session to
   session.
3. **About to write `## Recap` prose → `writing-style` apply.** Write
   `vault/episodes/NNN/sNN-recap.md` — read
   `vault/refs/stories/register.md` (a never-do correction goes in `vault/refs/stories/banned-patterns.md`) first and emit its `REGISTER:` line for the
   session's heaviest beat before the first sentence (a session where a
   character died is recapped at the weight of that death, never summarized
   past it) — frontmatter, `## Recap`, `## Highlights link`,
   `## Ingest review link`. Close `## Recap` on the hook the next session's run-guide Recap
   box reuses to cut into its opening moment (recap-opener coupling). Full
   field-by-field spec: `references/recap-format.md`.
4. **Find and write the highlights** — three-step filter (in-world,
   natural sentence boundary, speaker already resolved) plus the
   adversarial continuity pass. Full spec: `references/recap-format.md`.
5. **Lint to zero — before any QC dispatch.** Run
   `npm run lint -- <recap path> <highlights path>` and fix until it reports
   zero findings. The rewrites it forces land on the same sentences a checker
   would score, so a QC round opened now is a round thrown away.
6. **Quality review.** Only with step 5 at zero, and never in the same message
   as an agent still editing these files: spawn `content-quality-checker` with
   the `recap`
   profile (`vault/refs/qc-recap.md`) over the
   finished `vault/episodes/NNN/sNN-recap.md`; fix findings, re-lint (step 5), then re-run once if it failed by resuming
   that instance (`SendMessage`, never a fresh dispatch — agent spec § Rounds).
7. **Publish proposal.** Do not touch either file's `publish:` key (see
   Hard Rule 5).
8. **Commit.** `recap(sNN): <slug>` — `publish-site`'s own gate greps
   `git log --oneline | grep "recap(sNN)"` before it will proceed, so this
   prefix is load-bearing, not decorative.
9. **Done-check.** Paste `RECAP: recap.md N words, highlights.md M quotes /
   K moments` as your marker line. That is your evidence — not a paraphrase
   of either.
10. **Retrospective, only if asked** (see § Retrospective) — never part of
   an ordinary RECAP pass unless the user requested it.

## Owned paths

Writes `vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md`
(`vault/refs/runbook-wiki.md` § Who writes what) — both
ship `status: pending`, `publish: false`, both mandatory every RECAP pass.
Also writes `vault/episodes/NNN/retrospective.md` (see § Retrospective) — DM-
only, optional, never `publish: true` because it never ships to players at
all, not even proposed. May delete `vault/episodes/NNN/recap-draft.md` after
promoting it (see Two ways in) — that is the only file this skill removes.
Never writes to other `vault/` pages, `vault/campaigns/shattered-sea/pcs/`, situation
files, or the repo-root `CLAUDE.md` (see Scope boundary). Never sets `status:
canon` or `publish: true` anywhere.

## Retrospective (DM-only, optional)

The DM's own private read on how the session ran, never shown to players.
Trigger: the user asks explicitly ("session retro", "retrospective", "how
did that go") — never generated unprompted. Three questions asked
together, DM's own words recorded, no `publish:` key. Full template and
rationale: `references/retrospective.md`.

## Degrade by asking

Never guess a quote, a session number, or which side of a conflict is
right — ask. Full trigger list: `references/degrade-by-asking.md`.

## Reference files

| File | Read for |
|---|---|
| `references/two-ways-in.md` | Full branch detail: legacy-sourced session handling, promoting a staged draft. |
| `references/recap-format.md` | Full field-by-field spec for `vault/episodes/NNN/sNN-recap.md` (frontmatter, headings) and `vault/episodes/NNN/sNN-highlights.md` (filter steps, adversarial continuity pass). |
| `references/retrospective.md` | DM-only retrospective template, trigger conditions, and question set. |
| `references/checklist.md` | Full pre-done checklist. |
| `references/worked-example.md` | Fixture walkthrough end to end: gate check through highlights, plus a failure-case example. |
| `references/hard-rules-detail.md` | Full text and rationale for each Hard rule. |
| `references/degrade-by-asking.md` | Full trigger list for asking instead of guessing. |
