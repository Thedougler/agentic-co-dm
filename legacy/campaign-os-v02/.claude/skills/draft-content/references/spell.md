
# Draft — Spell

A 5e SRD spell transcribed verbatim into the vault's mechanical stat
format. Done means the DM can read the page and cast the spell exactly as
written in the source, with nothing invented and nothing missing.

## Template

`vault/_templates/_srd/_spell.md` — copy it, never retype it from memory.
Fixed stat-line block, in order: **Level**, **Casting Time**, **Range**,
**Components**, **Duration**, then the description paragraph transcribed
verbatim from the source, then the OPTIONAL `_Using a Higher-Level Spell
Slot._` line (delete outright when the source carries no upcast text).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Grounded In The SRD, Not A Wiki.** This type's real standard is the
  5e SRD document itself, not an external narrative wiki — its Forgotten
  Realms Wiki equivalent is in-world lore prose, not the mechanical stat
  format this vault's spell pages reproduce (`vault/_templates/CLAUDE.md`).
  The job is transcription fidelity, never invention.
- **Verbatim, Not Paraphrased.** The description paragraph, and the
  upcast line when present, are transcribed from the source text exactly;
  no source in hand, no page.
- **Homebrew Never Lives Here.** A homebrew spell is `type: rule, subtype:
  spell` and belongs to the `rule-prep` skill, never this template
  (`vault/_templates/CLAUDE.md`).
- **`subtype:` Matches The School Subdirectory.** The spell's school of
  magic (abjuration, conjuration, divination, enchantment, evocation,
  illusion, necromancy, transmutation) must match the
  `vault/srd/spells/<school>/` subdirectory the page lives in.
- **`source:` Is Required.** Set to the sourcebook or document this spell
  comes from; `source_url:` and `license:` follow for a third-party
  source (`.claude/rules/external-guides.md`).
- **One Page At A Time.** The real page volume is 347 vendored SRD spell
  pages — bulk import or re-import is `llm-wiki-ingest`'s job, never this
  guide's. This guide covers authoring or correcting a single page.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Spell name, and the exact source citation (sourcebook/document) it's
  transcribed from?
- SRD or third-party source? Third-party -> also confirm `source_url:`
  and `license:`.
- School of magic, and the class list that can cast it?

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`

## Out of scope

- A homebrew spell, or reviewing one for balance — `rule-prep`'s spell
  subtype, never this guide.
- Bulk importing or re-importing the SRD spell corpus — `llm-wiki-ingest`.
