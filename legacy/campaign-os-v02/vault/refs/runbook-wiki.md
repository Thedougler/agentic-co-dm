---
type: agent-guidance
status: canon
publish: false
aliases: []
created: 2026-07-30
updated: "2026-08-15"
tags: [craft]
summary: "Any wiki edit: new-page/callout/canonical-term rules, page ownership by path, and the tag taxonomy."
uid: afd2f7b2-adcb-4ce7-93a9-36ac8f10b097
---

# WIKI runbook (any wiki edit)

Page-format spec of record: the type's template under `vault/_templates/` (per `vault/_templates/CLAUDE.md`). Type enum, governed keys, and template headings do not live in vault/refs/.

## Rationale

- WK2: vault/refs/runbook-wiki.md is the session-start bootstrap, the
  record-a-write step. vault/CLAUDE.md's own subtree rules take over from
  there — colab/write/content phase routing already lives there.
- WK3: `_templates/**` carries no facts/canon binding — these aren't
  campaign-fact pages.

### You're not sure if this is governed prose or a template/config file

`vault/**` is governed wiki prose (WK2) — facts, canon, and the page-drafting workflow apply. `_templates/**` is structural (WK3) — templates — lint-governed but not campaign-fact pages. `vault/refs/**` (agent-facing runbooks, subagent specs, craft/table reference) is non-canon by construction the same way — lint governs its structure, no facts/canon bind it. `vault/dashboards/**` sits under `vault/**` and follows WK2 mechanically but carries no canon facts of its own — lint governs its structure the same way WK3 governs `_templates/**`.

### The file doesn't exist yet under any of these paths

A new page still routes through WK2's docs/guardrails/PROJECT.md pointer — template instantiation is vault/CLAUDE.md rule 4's job (never freeform), not something this doc adjudicates.

## New pages and edits

- New page: copy the template for its type. Never freeform (rule 5).
  Unsure which skill authors this type → chain-load `draft-content` (its
  table routes every typed page); session prep and beat work →
  `composing-beats`. No template exists yet → chain-load
  `content-type-scaffold` first.
- status: canon page: no gate blocks it. A session transcript writes canon
  directly (rule 3), and canon-review edits it to apply a human ruling.
  Any other source touching a canon page's facts without one of those two
  provenances is a rule-2 violation the model catches itself.
- One fact, one page; elsewhere wikilink (rule 6). Links must resolve (W3).
  The wikilink alone is the cross-reference. State the fact once, on its
  owning page. For facts worth mentioning elsewhere, `[[link]]` them
  inline. Otherwise, drop the mention entirely. Don't leave a pointer to a
  pointer.
- Page prose and names use the canonical term where `vault/srd/rules/rules-glossary.md`
  defines one. Never use a listed `_Avoid_` synonym.
- Wiki prose is in-world. The DM's own plans, prep provenance, and repo
  process (rules, lint, skills, migration, "this repo") never appear in
  `vault/`/`vault/campaigns/shattered-sea/pcs/` prose. DM intent lives in plain-prose handling
  notes or on DM-side prep pages (W52 flags process vocabulary). An
  unrevealed secret or planned twist NEVER appears as in-world prose on a
  player-adjacent page (`vault/campaigns/shattered-sea/pcs/**`, any publish-eligible page). The
  table learns it first. Until then it exists only on its own DM-side page
  and in plain-prose handling notes.
- No page carries a See Also/Related/Sources-shaped footer section (W123).
  A linked page either earns a place in the body prose or doesn't merit
  linking. Provenance narration belongs nowhere on the page.
- Any callout (`> [!`), DC/skill check, DM secret, or hazard being written →
  load `vault/campaigns/.claude/skills/callouts` first for the container and its contract
  (W22/W23 enforce type and case; a DC in bare prose belongs in a
  `[!check]`/`[!mechanic]`). A pre-standard callout or prose-DC already on
  the page you're editing gets converted in the same edit.
- After edits: if a lint hook is wired it fires automatically; if not,
  self-check against the rule table (`npm run lint -- --rules`). Either
  way, obey FIX lines or record the finding as unresolved per
  `docs/guardrails/PROJECT.md` PJ6's notation.

## Who writes what

Ownership is central to this system's integrity. Weak models violate
*implied* ownership constantly. Explicit ownership gets respected. Every
content type in every content-bearing folder has exactly one skill
ultimately responsible for its craft and structure
(`.claude/rules/skills.md` § Directory scoping). A new content type gets
its owning skill in the same pass that adds the type, never deferred to
"whichever skill's closest".

| Path | Written by | Never written by |
|---|---|---|
| `vault/stories/` | `draft-story`, plus the deriving skill filling the *Derived pages* line | ingest, recap, publish |
| `vault/`, `vault/campaigns/shattered-sea/pcs/` | prep skills (`status: pending` in place) + ingest (`status: canon` in place) + canon-review | recap |
| `vault/campaigns/shattered-sea/pcs/{stats,abilities,spells,inventory}/` | `combat-profiles` (transcribed from the character sheet) | `dnd5e-character-interview`, ingest |
| `vault/campaigns/shattered-sea/pcs/<name>.md` | `dnd5e-character-interview` | `combat-profiles` |
| `vault/campaigns/shattered-sea/encounters/` | `encounter-prep`, `status: draft`/`pending`, never `canon`/`publish: true` | anything but `encounter-prep` |
| `vault/episodes/NNN/eNN-overview.md` | `composing-beats` overview route (`status: pending` in place) | ingest, publish, co-dm |
| `vault/episodes/NNN/eNN-run-guide-<slug>.md` | `composing-beats` run-guide route (`status: pending` in place) | ingest, publish, co-dm |
| `vault/campaigns/*/locations/<slug>.md` (`type: route`) | `.claude/skills/draft-content/references/route.md` via `draft-content` (`status: pending` in place) | `travel-events` |
| `vault/episodes/NNN/transcript*` | the speaker-label pass | anything after the `vault/refs/runbook-ingest.md` (INGEST) gate |
| `vault/episodes/NNN/table-notes.md` | `co-dm` (optional, RUN phase only) | anything but `co-dm` |
| `vault/episodes/NNN/ingest-review.md` | ingest (creates, updates, and deletes it itself) | recap |
| `vault/episodes/NNN/world-turn-<date>.md` | `world-update` | ingest, recap |
| `vault/episodes/NNN/sNN-recap.md`, `vault/episodes/NNN/sNN-highlights.md` | `recap-writer` | ingest |
| `utils/site/public/` | `build_site.sh` | hand edits, ever |
| `docs/secrets.md` | the human + `canon-review` | automated pipelines |

A task that seems to require writing outside your row is the signal you are
in the wrong phase. Stop and check the phase's `GATE:` line — each phase
runbook (`vault/refs/runbook-{session,capture,ingest,recap,publish}.md`)
opens with its own. Either switch phases properly or produce the
intermediate artifact instead.

## Operative-mechanics ownership (encounter ↔ scene)

For a fight with both a `vault/campaigns/shattered-sea/encounters/` page and a sibling
`vault/episodes/NNN/` scene file, the encounter page owns the operative-mechanics
facts. Per-round numbers (DCs, HP thresholds, phase triggers) are what the
runner needs mid-round. The scene file never restates or omits them: it
embeds the encounter page's operative blocks via `![[page#Heading]]`
transclusion (vault/CLAUDE.md rule 8) so it still runs cold, with no
lookup hop and no duplication drift. Every block the runner needs mid-round must be present and transcluded.
W114 (`npm run lint -- --rules`) tracks that coverage against the
`OPERATIVE_HEADINGS` list in `wiki.toml` `[thresholds]`.

The encounter page and its sibling scene file cross-link both directions
and declare the ownership: the encounter page states it owns the fight's
numbers, the scene file states which blocks it transcludes and from where.

## Single-source rules

- **Aliases resolve through frontmatter.** Every page lists its `aliases:` —
  a repo-wide grep for the name resolves "the Foul One" →
  `vault/campaigns/shattered-sea/npcs/otar-the-foul.md`.
- **Stats have exactly one home.** A PC's four roster scalars (`ac`,
  `hp_max`, `class_levels`, `level`) in `vault/campaigns/shattered-sea/pcs/<name>.md` frontmatter
  (machine-readable). Every other mechanical attribute lives on that PC's
  satellite page: `vault/campaigns/shattered-sea/pcs/stats/`, `vault/campaigns/shattered-sea/pcs/abilities/`, `vault/campaigns/shattered-sea/pcs/spells/`,
  `vault/campaigns/shattered-sea/pcs/inventory/`. The hub page transcludes these rather than restates.
  Monster/NPC/encounter-creature stats live inline on the creature's own
  page, as the first block under `## Stats & Combat` — no separate
  statblock-only file, no embed. Party-level resources (ship, funds, reputation) live on the
  page that owns the resource, never on a PC page.
  Recaps and run guides reach a stat by `[[wikilink]]` to
  the page that owns it, never as an independent restatement (W62).
- **`vault/episodes/` is append-only history.** Once a session's `vault/refs/runbook-publish.md` (PUBLISH) gate
  passes, its directory is frozen; corrections happen through a new
  CONTRADICTION block and `canon-review`, never by editing an old
  transcript.
- **Generated files are marked.** Anything a script writes carries a
  first-line `%%GENERATED by utils/scripts/X: do not hand-edit%%` comment.
  W11 flags hand edits to one.

## Tag taxonomy

The `tag-taxonomy` skill owns this procedure (auditing, normalizing, and
extending the vocabulary) and is the judgment layer `llm-wiki-lint` hands
W13/W27 findings to.

- Tags come from `docs/tags.md`'s controlled vocabulary, not
  freeform (every page ≥1 Domain tag, max 5 per page,
  lowercase-hyphenated). Reuse an existing canonical tag before adding a
  new one.
- `visibility/*` tags (`public`/`internal`/`pii`) are reserved: at most one
  per page, never counted toward the 5, omit entirely when a page is
  clearly public.
- New tag required → add it under the right section
  (Domain or Project) in `docs/tags.md`, don't invent one silently
  on a page. Normalizing an existing tag → add an `alias -> canonical`
  line under `## Aliases` there instead of hand-fixing pages one at a
  time.
- W13 (soft) flags any page tag that's neither canonical, a listed alias,
  nor `visibility/*`. W27 flags a page carrying no tag at all. Treat both
  the same as any other soft finding: fix it or note why not.
- Migrated legacy tags: entity-identity tags (`tessarine`, `grung`, a
  faction/place/species name) and origin tags (`homebrew`, `raw`) are
  DROPPED BY DESIGN, not mapped. The relationship an identity tag encodes
  belongs in a wikilink or prose mention (one fact, one place). Origin
  lives in the `[HB]`/`[RAW]` mechanic labels. Map a tag to a canonical
  tone ONLY when the page's own content carries that tone. A single worked
  mapping (combat→horror on a page with a horror closing line) is not a
  general rename rule. Log each mapping or drop in the ingest queue file.
  A new tag beyond a mapping/drop routes through `docs/tags.md` instead of
  growing the taxonomy per-file.
- No page is exempt from carrying a tag, and no population is blanketed
  with one role label — the coverage floor and the no-blanket rule live in
  `docs/tags.md` § Rules.
