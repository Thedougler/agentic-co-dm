---
name: transcript-ingest
description: >-
  Turn a frozen, speaker-labeled transcript.md into PC page edits — Phase 4 (INGEST), in a
  Campaign OS repo (vault/ present). Use for "ingest the transcript", "process session NN",
  "mine the session", "extract state changes", "run INGEST", or transcript.md exists with no
  sibling ingest-review.md yet. Writes status: canon directly, never publish: true.
---

# Transcript Ingest

Phase 4 — INGEST, the load-bearing phase (`vault/refs/runbook-ingest.md`: everything
downstream depends on this) and the phase that promotes facts to canon.
Spawns `extractor` (`vault/refs/runbook-agents.md`) once per chunk; each chunk writes
directly to `vault/`/`vault/campaigns/shattered-sea/pcs/` pages at `status: canon` — a transcript is
recorded play, not a guess, so there's no separate promotion step. No
intermediate ledger file — a page IS its own provenance record, wikilinking
the source transcript, never a line-number citation.

## Gate check

```
ls vault/episodes/NNN/transcript.md vault/episodes/NNN/ingest-review.md 2>/dev/null
grep -c '^\*\*[^*]\+:\*\*' vault/episodes/NNN/transcript.md
```

Gate (`vault/refs/runbook-ingest.md`): `vault/episodes/NNN/transcript.md` exists, no sibling
`vault/episodes/NNN/ingest-review.md` yet (or one exists with `Processed through:` short of the
transcript's end — see Resuming below), and the speaker-label count is ≥ 50
hits.

The grep counts genuine `**Name:** ` lines regardless of what's in the name
(`vault/refs/runbook-ingest.md`'s GATE line). Below-threshold: Degrade by
asking below.

**Legacy prose-recap alternative gate.** Ingestable when `vault/episodes/NNN/transcript.md`'s
FIRST line is `LEGACY-SOURCE: <original path or provenance note> — prose
recap, no audio`: the speaker-label threshold is waived and transcript-label
is skipped; extraction, chunking, and review are otherwise identical to
speaker mode. Full detail: `legacy-source-gate.md`.

## Chunking and the extractor agent

Process `vault/episodes/NNN/transcript.md` in chunks of **≤ 400 lines** (L5). Before the first
chunk, check the agent actually exists — `vault/refs/runbook-agents.md` specs it, but
specs aren't builds:

```
test -f .claude/agents/extractor.md && echo present || echo absent
```

For each chunk:

1. If `present`: spawn the `extractor` subagent (`vault/refs/runbook-agents.md`) with
   the chunk's line range, the fact-type table below, and the paths
   `vault/` and `vault/campaigns/shattered-sea/pcs/*.md` for entity resolution (aliases resolve
   through each page's own `aliases:` frontmatter, not a separate index). The agent
   has Read/Grep/Edit/Write and writes the actual page edits itself, always
   at `status: canon`.
   If `absent`: perform the same extraction directly in the main loop, under
   the same discipline (resolve, then write) — same input (line range,
   fact-type table, alias paths), same output shape (real page edits, all
   `status: canon`). Paste `NOTED: extractor agent not present in this repo — ran
   extraction in-loop` once, on the first chunk.
2. Paste the marker: `INGEST: chunk L1-L400, 6 pages touched`.
3. Update `vault/episodes/NNN/ingest-review.md`'s `Processed through:` line to
   this chunk's last line (create the file on the first chunk — see Human
   review below).
4. Continue to the next chunk.

### Resuming after an interruption

`vault/episodes/NNN/ingest-review.md`'s `Processed through: L<n>` line is the
checkpoint. Before starting:

```
grep "Processed through:" vault/episodes/NNN/ingest-review.md 2>/dev/null
```

Resume with the next ≤400-line chunk after that line. Absent file → start
from L1. This file holds only a resume pointer and a review date, not a
second ledger — this skill deletes it itself once the session's pages are
reviewed (see § Human review, Finish).

## Table-notes as a second evidence source

```
ls vault/episodes/NNN/table-notes.md 2>/dev/null
```

If present, `co-dm` wrote it live during RUN (Phase 2) — each `## IMPROV`
block is a live-table fact. Treat the whole file as one final chunk
(extractor or in-loop), citing `[[vault/episodes/NNN/table-notes]]` rather
than the transcript. Absent file → skip, it's optional.

## What each fact becomes (the extraction categories)

Resolve every candidate fact, then act on it directly — there is no verb
grammar to stage first, just the write each row below already names:

| Category | When | Direct action |
|---|---|---|
| Fact | An established world fact changed or was revealed | Edit the target page's body prose or, if it's tied to what happened this session specifically, its `## Session Log` (Kyzil's page is the worked example: evergreen characterization in the body, session play-by-play only in Session Log) |
| Stat | A PC's frontmatter-tracked stat changed (`hp_max`, `class_levels`, `ac` — see `vault/_templates/_campaigns/_pcs/_pc.md`; never current/ephemeral HP, that's not tracked in this repo) | Edit the `vault/campaigns/shattered-sea/pcs/<name>.md` frontmatter field directly |
| Quest | `quest_status` changed | Edit the quest page's frontmatter field directly |
| New | An entity with no existing page needs one | Instantiate the matching `_templates/<type>.md` (CLAUDE.md rule 5) at `status: canon`, chain-load `content-type-scaffold` first if no template matches — type-confidence rule: `extraction-elaborations.md` |
| Appear | A named NPC appeared/acted this session | Append to that NPC's `## Session Log` |
| Review | Genuinely ambiguous (entity resolution can't pin a target, or the fact itself is unclear) | Leave a one-line Review note where you'd otherwise have written — no guess, no page write |

Every edit sets `status: canon` and cites the transcript with a bare
wikilink — `[[vault/episodes/NNN/transcript]]` (check `ls vault/episodes/NNN/`
for the actual filename, don't guess). A page's existing `status: canon`
never blocks a write — it's not a gate, it's just the page's current state.

Resolution rule for any named entity — `grep -ril "<name>" vault/
vault/campaigns/shattered-sea/pcs/` (aliases resolve through each page's own `aliases:`
frontmatter, so this single grep catches a page's canonical name and any
listed alias alike); a hit on a different page's body is a sub-entry hit
(edit directly, flag W9-near-miss, never duplicate). Miss → `New`;
ambiguous → `Review`. Full algorithm + parallel-dispatch caveat:
`entity-resolution.md`.

## What becomes a page edit (and what doesn't)

Classify every line of the chunk IC / OOC / META before extracting — the full
signal table (what's OOC/META/skip vs. a genuine IC candidate) and the
under-extraction-beats-false-canon rule: `ic-ooc-classification.md`.

## Contradictions

A transcript fact beats stale prose — correct the page directly, cite the
transcript, that's a `Fact` edit not a `Review`. Transcript-vs-transcript
disagreement is the one real human call: append a CONTRADICTION block
instead of picking a winner. Full rule + worked block: `contradictions.md`.

## Human review

After the last chunk, `vault/episodes/NNN/ingest-review.md` (created on the first chunk) holds
the resume pointer and a sanity-check record — worked example:
`human-review-example.md`. Present the diff (`git diff --
<pages touched>`; > 40 changed lines → chunks of 20, L5, CLAUDE.md rule 7)
so the human can sanity-check what landed. Since every fact already wrote
straight to `status: canon`, this review is a spot-check, not a gate —
nothing downstream is blocked on it, and the human can correct any page
directly at any time. Write `REVIEWED-BY-HUMAN: <date>` into
`vault/episodes/NNN/ingest-review.md` once they've looked, then move to Finish.

**Finish** (folds in what a separate promotion phase used to do):

1. Delete `vault/episodes/NNN/ingest-review.md` — its job (resume pointer +
   sanity-check record) is done.
2. **Commit**: `ingest(sNN): <slug>`.

## Lint before done

Every page touched (incl. `vault/episodes/NNN/ingest-review.md`) needs W1/W2 (valid
`type`/`status`/`publish`) and W5 (required headings), same as any template
instance — paste the lint result; zero unresolved `WIKI-LINT` blocks is the
done-check (contract item 3).

## Owned paths

Writes `vault/`/`vault/campaigns/shattered-sea/pcs/` pages directly at `status: canon`, `vault/episodes/NNN/ingest-review.md`
(created, then deleted at Finish), and transcript-vs-transcript
CONTRADICTION-block appends. Never sets `publish: true` — that stays a
separate human-approved step (PUBLISH phase). Never touches
`vault/episodes/NNN/transcript.md`/`vault/episodes/NNN/transcript.raw.md`.

## Degrade by asking

- Speaker-label count below 50 on the gate check → tell the human, offer to
  re-run transcript-label, don't extract from a low-confidence transcript.
- Ambiguous entity resolution (an unclear entity-resolution grep hit) →
  `Review` note, never a guessed target.
- Review diff over 40 lines and the human hasn't started reviewing →
  present in chunks of 20, don't dump the whole thing and hope.
- `.claude/agents/extractor.md` missing → extract in-loop instead (Chunking
  above) and paste the `NOTED:` line; never fall through to an
  unrestricted general subagent.

## References

| File | Covers |
|---|---|
| `extraction-elaborations.md` | New-type confidence (pc vs npc), combat extraction (durable consequences only, no round-by-round log), the DM-voicing-an-NPC attribution rule |
| `entity-resolution.md` | Full two-pass entity-resolution algorithm and the parallel-dispatch re-resolve caveat |
| `legacy-source-gate.md` | Speaker-label grep worked example; full detail and rationale on the legacy prose-recap alternative gate |
| `human-review-example.md` | Worked example of a filled-in `vault/episodes/NNN/ingest-review.md` |
| `contradictions.md` | Full contradiction-handling rule and CONTRADICTION block worked example |
| `ic-ooc-classification.md` | Full IC/OOC/META signal table for classifying transcript lines before extraction |
