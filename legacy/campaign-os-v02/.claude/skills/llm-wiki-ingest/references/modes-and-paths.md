# Modes and owned paths — full detail

Read this for the migration-mode mechanics and the complete owned-paths listing
that the SKILL.md core only summarizes.

## Migration mode elaboration

**Migration mode is the one place this skill may write `status: canon` directly**,
and only under two conditions, both required: (a) a human-approved disposition
named this source and a disposition in this conversation — paste the approval,
(b) the disposition is `canon` because the content is already-revealed legacy
material, not new prep. Absent both, default to **new-source** mode and
`status: pending`. This is a genuine tension with the shared contract's item 5
("never flip `status: canon`" — `transcript-ingest`/world-update/canon-review/
PUBLISH exclusively); an explicitly-authored, human-approved exception for
exactly this skill's role.

**Migration-mode link deferral.** Migration mode's owned-paths restriction (only
the file(s) named on the ledger line) beats the general writeback step's
create-missing-stubs-first order: never create stub pages for entities the source
merely links to. Write the relationship as plain text (no `[[wikilink]]`), add a
queue-file `## Flags` line per withheld link (`relink: <entity> — once its page
lands`), and move on. The migration's own link-restoration pass
(orchestrator/audit, after ledger lines land) converts the plain-text mentions
back to wikilinks; W3 can't fire on a link you didn't write. Rationale: parallel
ledger lines create the real pages concurrently — a stub you invent races them
and guesses filenames wrong.

**Migration-mode status determination** (reveal evidence comes from the SOURCE
repo — the live campaign's `vault/episodes/` is empty during migration, so project
rule 10's transcript-grep substitutes source-repo evidence). Precedence, first
match wins:
1. Explicit unrevealed marker (a "Not yet encountered" line, a planned/
   directory) → `pending`, always — beats every other signal.
2. Source session logs/scene files show the entity in actual play → `canon`
   (cite the file:line).
3. Genuinely per-file `audience: players` + `publish: true` frontmatter →
   `canon` — but frontmatter uniform across a whole sub-pile is an export
   default, not a signal (`.claude/skills/llm-wiki-ingest/references/claim-buckets.md` § Source types,
   rules-or-homebrew row), and
   `audience: dm`/`publish: false` per-file means `pending`.
4. No signal of any kind — no reveal heading at all, silent frontmatter →
   `pending` (rule 10: unsure means it wasn't).

State which rung decided it, in the page and the queue file.

**Generic ruleset items are never link targets.** SRD/PHB stock gear a source
wikilinks (Healer's kit, Antitoxin, torches...) becomes plain text with NO
per-item relink flags — one collapsed queue-file note covers the lot. Relink
flags are for campaign entities only.

## Owned paths — full listing

- **new-source mode**: `status: draft` while a page is mid-write, `status: pending`
  once its source citations are complete — identical to every other prep skill's
  owned-paths row.
- **migration mode**: may write `status: canon` directly, but only per the
  three-condition gate above, and only the specific file(s) named on the
  `REVIEWED-BY-HUMAN:` ledger line being executed.
- **Migration mode only** (a source handed in from outside `inbox/`, e.g.
  `~/ai-os/shattered-sea/`): `raw/<YYYY-MM>/<source-slug>.md` (current
  year-month) — the batch queue for the source currently being processed (see
  Workflow, Batching). `raw/` sits outside the wiki lint root (`vault/`),
  so this file needs no frontmatter or template — same convention as
  `campaign-grilling`'s decisions file and other process-only queue files.
- **Inbox-sourced content instead uses `npm run inbox:check`/`inbox:archive`**
  (`inbox/CLAUDE.md`) — no queue file, no `raw/INGESTED.tsv`
  entry. A file that arrived via `inbox/` never gets the migration-mode
  bookkeeping above.
- **Character-sheet PDFs only**: `_assets/character-sheets/<pc-slug>-character-sheet.pdf`.
  Never decompose a character sheet's content into `vault/campaigns/shattered-sea/pcs/<name>.md` — that stays
  `dnd5e-character-interview`/`combat-profiles`' to originate, chain-load and hand off.
  This skill's own action is narrower: stub-check `vault/campaigns/shattered-sea/pcs/` (Standard queries) for
  the PC the sheet names, and on a single unambiguous hit, copy the original PDF
  verbatim (never re-encoded, never renamed content) to
  `_assets/character-sheets/<pc-slug>-character-sheet.pdf` — a second, additional
  artifact alongside that PC's page. For the sheet's actual content, load the
  `anthropic-skills:pdf` skill per `.claude/skills/llm-wiki-ingest/references/workflow.md`'s PDF handling —
  never edit the sheet's content as `.md` directly, which loses fillable-form field values.
  Zero hits (PC not created yet)
  or multiple/ambiguous hits → flag it in the queue file and ask the DM (Degrade
  by asking), don't guess which PC page it belongs beside.
- **Never**: `vault/episodes/*/transcript*` (that's CAPTURE/transcript-label's), a
  session's `vault/_templates/_episodes/_session_ingest_review.md`/`vault/_templates/_episodes/_session_recap.md`/`_templates/session-highlights.md` (`transcript-ingest`/
  recap-writer own those), `publish: true` on anything (PUBLISH exclusively,
  contract item 5 — migration mode's `status: canon` exception does not extend to
  publish flags), a new Front on a faction page (`.claude/skills/draft-content/references/faction.md` owns Front
  authoring — see Claim buckets), `vault/campaigns/shattered-sea/pcs/<name>.md` content (PC creation is a
  canon-review-signed event owned by `dnd5e-character-interview`,
  not this skill's to originate) — the verbatim character-sheet PDF copy above is
  the sole exception, and it is an asset copy, never page content.
