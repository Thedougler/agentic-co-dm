# Source ingest queue: ss-system-interview-guide

Source root: /Users/nick/ai-os/shattered-sea/wiki/system/character-interview-guide.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:37 — `system :: system/character-interview-guide.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission (procedure item 4 verbatim): ... the user's current instruction to ingest legacy canon IS that blessing for this mission's scope."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] system/character-interview-guide.md — triage: no clean row in
  `references/claim-buckets.md` § Source types (see Flags #1) — closest fit is
  `research-or-guidance`, but the ledger line's own prescribed disposition
  (`map, don't duplicate`) is a fourth verdict class the claim-buckets table
  doesn't enumerate at all. Treated as `skipped — mapping report only, no wiki
  page`, per the ledger line's explicit instruction, not per any SKILL.md rule.

## Claims

- none — mapping-verdict sources get no claims list, same precedent as
  `ss-pc-jean-claude.md`'s hand-off line (SKILL.md § 3 covers `session`/
  `character-sheet` triage explicitly; this source triages to neither, but the
  "no wiki page" outcome is the same shape).

## Mapping verdict: (a) full equivalent exists — no wiki page

**Source content.** `system/character-interview-guide.md` (frontmatter
`type: system`, `subtype: system-guide`, `status: active`, `publish: false`) is
a blank player-facing questionnaire for establishing PC foundations before/
during Session Zero. Structure: a "Fast Rules" block (4 agent-facing
instructions: ask short questions, capture exact answers, convert answers into
"gravity wells, not exhaustive biographies", flag gaps instead of inventing
intent) followed by 6 sections — The Basics (3 Q), Who They Are (4 Q), Where
They've Been (4 Q), Who They Know (3 Q), How They Work (3 Q), For the DM
(4 Q) — 21 questions total, with a closing note: "Questions 18–21 are the most
useful for the DM." Links to `[[session-zero]]` and `[[dm-philosophy]]`.

**Campaign-os equivalent.** `.claude/skills/campaign-os/references/skills-registry.md:45`:

> `character-interview` | `dnd5e-character-interview` | the 20-question
> framework | output lands as/feeds `pcs/<name>.md` (Overview + Backstory),
> status canon-by-nature since it's player-authored — but pc creation is a
> canon-review-signed event, not a silent write

This is a real, installed skill — `anthropic-skills:dnd5e-character-interview`
is present in this session's available-skills listing. It is not a file inside
this repo (`.claude/skills/` has no `character-interview` or `dnd5e-*`
directory — confirmed by `find`); it resolves through the `anthropic-skills`
plugin, which is not materialized on this machine's local filesystem either
(`find / -iname "*dnd5e-character-interview*"` — zero hits outside the skill
name registration itself). I did not invoke it: it is built to interview a
live player, and running it live is out of a mapping-report's scope — the
verdict below rests on the registry's description plus the source-guide's own
structure, not a question-by-question diff against the plugin's SKILL.md
text, which I could not read directly.

**Coverage assessment.**

- Registry names the campaign-os slot's craft as "the 20-question framework."
  The legacy guide's own body is 21 questions across 6 named sections, with an
  explicit closing note pointing at "questions 18–21" — internally consistent
  with a ~20-question count. Purpose, output target (`pcs/<name>.md`,
  Overview + Backstory), and governance (PC creation as a canon-review-signed
  event, never a silent write — `bootstrap-and-audit.md:43`, `SKILL.md:95`,
  and this same ledger's `ss-pc-jean-claude.md` all say so independently) all
  line up.
- Two structural elements in the legacy guide are *not* visible in the
  registry's one-line description and I could not confirm their presence or
  absence in `dnd5e-character-interview` without invoking it: (1) the
  "Fast Rules" preamble (capture-exact-answers / convert-to-gravity-wells /
  flag-gaps-don't-invent — an *agent* behavior contract, not a question), and
  (2) the explicit "For the DM" section (4 questions the player answers but
  the DM alone sees: a reunion NPC, a "questionable" want, a secret, and a
  thematic ask) — framed in the source as deliberately separate from the
  player-facing basics.
- If `dnd5e-character-interview` already has an equivalent DM-only question
  block and its own agent-behavior framing (plausible, since it's the more
  actively maintained skill and the registry credits it as the *source* of
  the campaign-os slot's craft, not the other way around), coverage is
  complete and there is nothing to port. If not, the "Fast Rules" preamble and
  the DM-only question grouping are the two pieces of orphaned craft worth a
  human look — flagged here, not ported (per mapping-report scope: report the
  gap, don't act on it).

**Outcome: no wiki page written.** No `world/`, `pcs/`, or `prep/` file
created or modified by this ingestion.

## Flags

1. **Skill-gap: source-ingest has no triage category for "meta/system doc
   with a suspected campaign-os equivalent."** `references/claim-buckets.md`
   § Source types lists 10 rows (`entity-source`, `location-source`,
   `faction-source`, `quest-source`, `rules-or-homebrew`,
   `handout-or-player-facing`, `session-record`, `character-sheet`, `asset`,
   `research-or-guidance`) — none of them produce a "mapping report, no wiki
   page" outcome. The closest is `research-or-guidance` ("process notes,
   writing standards, meta material... usually skipped"), but "skipped" in
   that row means *not campaign canon, not worth capturing at all* — it does
   not carry the "go check whether an existing skill already does this, then
   report the comparison" instruction that this ledger line's disposition
   (`map, don't duplicate`) actually required. I improvised: triaged as
   closest-fit `skipped` for the Sources-table bookkeeping, then executed the
   ledger line's own verdict menu (a/b/c from the dispatch instructions, not
   from SKILL.md) by hand, outside any table SKILL.md defines. This is a
   genuine skill gap, not a one-off — any future legacy source whose disposition
   is "we probably already built this as a skill, go check" will hit the same
   missing row. Worth a `claim-buckets.md` § Source types addition (e.g. an
   `internal-equivalent-check` row: "meta/process doc describing a workflow →
   check skills-registry.md and installed skills first; full match → mapping
   report only, no page; partial → mapping + orphaned-craft flag; no match →
   gap report") the next time source-ingest itself gets touched.
2. **Could not read the comparison target's actual text.** `dnd5e-character-interview`
   is an `anthropic-skills` plugin skill, not a file under this repo's
   `.claude/skills/` and not present anywhere on local disk (`find /` came back
   empty for the plugin name). The coverage assessment above is therefore
   built from `skills-registry.md`'s one-line paraphrase plus structural
   inference, not a direct diff. Recommend a human (or a session that
   deliberately invokes `dnd5e-character-interview` in inspection mode) verify
   the two flagged gaps — the "Fast Rules" agent-behavior preamble and the
   DM-only question grouping — before deciding they're truly redundant.
3. **relink**: none — this source's only wikilinks (`[[session-zero]]`,
   `[[dm-philosophy]]`) were never written anywhere in this repo (no page was
   created), so there is nothing to defer or restore.
