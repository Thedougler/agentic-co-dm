# Workflow — full per-step mechanics

Read this for the complete substeps behind the SKILL.md core's Workflow skeleton.

### 1. Name the source and the mode
Ask if either is ambiguous (Degrade by asking). Compute a `source-slug`: kebab-case
the source's filename or the folder name if it's a directory of files (e.g.
`old-npc-notebook`, `shattered-sea-wiki-export`).

**Source arrived via `inbox/`?** Steps 2 and 2b below (queue file, `INGESTED.tsv`)
do not apply — run `npm run inbox:check` for the already-ingested check, decompose
the source into claims per the workflow below same as any other source, then
complete it with `npm run inbox:archive` (`inbox/CLAUDE.md`) instead
of steps 2/2b/7's queue-file and manifest mechanics. Skip to step 3.

**Source is a non-markdown, non-text format other than PDF** (DOCX, XLSX,
image, HTML)? A SessionStart hook (`utils/scripts/inbox_to_md_sweep.sh`,
`inbox/CLAUDE.md`) already converted it to a sibling `.md` companion before
this session started — triage and decompose from that `.md` companion, never
the original. Companion missing (file dropped in mid-session) → run
`npm run inbox:to-md -- -f <path>` yourself before triage. This mechanism is
Inbox-scoped only; a migration-mode source from outside `inbox/` has no
companion file — read it directly (the Read tool renders it natively).

**Source is a PDF (Inbox-sourced or migration-mode, either way)?** Never the
sibling `.md` companion and never a plain Read of the PDF — both only surface
the static text layer, silently dropping filled-in form-field values on a
fillable-form PDF (a character-sheet export is exactly this shape). Load the
`anthropic-skills:pdf` skill and extract directly (PyMuPDF/pypdf form-field
read for a fillable form, pdfplumber/pdftotext for plain text/tables) before
triage. A PDF that triages as `character-sheet` follows the verbatim-copy
handling in Owned paths instead of ordinary decomposition.

### 2. Open or create the queue file (migration mode only)
`raw/<YYYY-MM>/<source-slug>.md` (current year-month). Re-read it if it exists
(a prior pass may have left checked and unchecked lines — this is the idempotent
resume point, the same role `vault/episodes/NNN/ingest-review.md`'s `Processed through:` line plays
for transcript-ingest: no separate progress file, the queue itself is the
checkpoint). If new, seed it:

```markdown
# Source ingest queue: <source-slug>

Source root: <path the user gave you>
Mode: new-source | migration (human-approved disposition for <slug>)
Started: YYYY-MM-DD

## Sources (batch order, smallest file first)
- [ ] <path> — triage: <type from source-triage table below>, <ready|blocked|skipped>

## Claims — <path, once triaged ready>
- [ ] <type> :: <name> :: <target page path> (new|expand) — <one-line what>

## Flags
- none
```

### 2b. Already-ingested check (before triage, per file — migration mode only)

```
grep -F "<source path relative to the source root>" raw/INGESTED.tsv
```

A hit means the file is DONE — mark it `skipped — already ingested (see
INGESTED.tsv)` and move on; never re-ingest. On completing a source (step 7),
APPEND its line to `raw/INGESTED.tsv`:
`<source-path>\t<target page or outcome>\t<commit>\t<date>` — and include
`raw/INGESTED.tsv` in your commit pathspec. One file, greppable,
deterministic — this manifest is the system's memory of what's been processed,
and it lives undated at the top of `raw/` (not inside a month bucket) since
it is a single ledger appended to across every month, never itself moved.

The match is **path-keyed** (`grep -F` on the path): a hit means that exact
path was processed, so a source *edited and re-handed under the same path* is
wrongly skipped as done. If the DM says a source changed, re-triage it
regardless of the manifest hit (a silent skip re-ingests nothing and the edit
never lands).

### 3. Triage each untouched source file
For a single file, this is one entry. For a directory, list every file. Classify
each against `.claude/skills/llm-wiki-ingest/references/claim-buckets.md` § Source types (mined from the legacy
skill's triage table); mark `ready`, `blocked`, or `skipped` per that file's §
Ready/Blocked/Skip rules. A file that triages as `session` gets a `skipped — hand
off to <skill>` line, not a claims list (Hard Rule 5) — name the destination skill
in the queue line so the DM can route it. A file that triages as `character-sheet`
gets the same `skipped — hand off to dnd5e-character-interview/combat-profiles` line for
decomposition, but still executes the verbatim-copy step from Owned paths before
moving on — it is never a pure no-op skip.

### 4. Batch
Process **5 ready sources per wave** (L5), smallest-file-first (`ls -la <dir> |
sort -k5 -n` or equivalent) — a fixed number, not a judgment call, so a weak model
doesn't rationalize "just one more" under queue pressure. Finish a wave fully
(every claim checked, every page linted, one commit) before pulling the next 5. A
wave of 1-3 is fine when that's all that's `ready`.

### 5. Per source, decompose into claims
Read the source in place — never rewrite it, never summarize instead of
decomposing. For large sources, read headings/frontmatter first, `grep` for proper
nouns, then read only the sections a claim needs. Break it into durable claims per
`_templates/` (§ Claim buckets) and append each as an unchecked line under this
source's `## Claims` heading in the queue file, before writing any wiki page — the
queue line is the plan, written down before execution, same discipline
the legacy skill's "working plan" enforced, just made durable instead of
chat-only scratch.

### 6. Write back, one claim at a time
For each claim line:
1. Stub check (Standard queries). Existing page → expand in place. No hit → `ls
   _templates/`, open the matching `_templates/<type>.md`, and follow its
   `<!-- AGENT: ... -->` comment to chain-load the owning prep skill
   (`.claude/skills/<type>-prep/SKILL.md`) for its template/structural
   conventions, then instantiate `_templates/<type>.md` — copy it, don't retype
   it from memory (L4). Borrow the prep skill's structure and headings only,
   never its creative-domain invention (Hard Rule 1 still governs what gets
   written).
2. Fill only what the source states, citing it (Hard Rule 2). Leave a field the
   source doesn't cover as a stub note (`.claude/skills/llm-wiki-ingest/references/claim-buckets.md` § Stub
   creation), never a filled-in guess (Hard Rule 1).
2b. Set the LLM-wiki fields (`llm-wiki` skill): write a one-sentence `summary:`
   (≤200 chars, a factual gist of what the source states — not a guess, Hard
   Rule 1); set `tier:` only if the page is clearly a hub (`core`) or a one-off
   walk-on (`peripheral`), else leave the template default `supporting`. Any
   DM-only claim you *extrapolated* rather than read from the source says so in
   plain prose (e.g. "DM note: inferred from the source's map, not stated
   outright" or, if the source is self-contradictory, "DM note: source is
   ambiguous here — <the two readings>") — never presented as flat, unmarked
   fact. **On an *expand*, not just a new page:** if the added claims shift what
   the page is fundamentally about, rewrite its `summary:` to match — a stale
   summary sends every reader and the retrieval ladder to an expensive
   full-page read; leave it unchanged if the page's gist is intact.
3. Add reciprocal wikilinks for durable relationships the source states.
4. Check the claim's line in the queue file.

### 7. Close the source
Once every claim for a source is checked (or NOTED), check the source's own line
under `## Sources`. If it's the last source in the wave, go to step 8; otherwise
return to step 5 for the next `ready` source in the wave.

### 8. Finalize the wave
Commit once per wave:

```
git add raw/<YYYY-MM>/<source-slug>.md vault/...   # only what this wave touched
git commit -m "ingest(<source-slug>): <N> sources, <M> claims"
```

Then pull the next wave (step 4) or, if the queue file shows every source checked
or skipped, report queue clear and stop.
