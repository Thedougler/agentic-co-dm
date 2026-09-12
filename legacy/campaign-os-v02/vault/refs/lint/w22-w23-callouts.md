---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
summary: "W22/W23 callout findings: lowercase type tokens and play-vs-doc callout taxonomy, with the fix for each shape."
uid: 1f631d93-aba8-4c10-aaad-42b7bc46010d
---

# W22/W23 — Callout lowercase & type-by-path

Protects: one consistent callout vocabulary — case-normalized types, and
the right family of type for the page the callout sits on — so a scan for
`[!check]` or `[!mechanic]` never misses a variant spelling. Full prose
contract for each callout type: `.claude/skills/callouts`.

## W22 — lowercase type

`> [!MECHANIC]` must be `> [!mechanic]`. Autofixable — `npm run lint -- <path>`
rewrites the token in place; nothing to do by hand beyond re-running lint
if you fixed it manually and want confirmation.

## W23 — type must match page family

Play pages (`vault/**`, `pcs/**`, `sessions/**`, excluding the doc roots
below) take play callouts (`check`, `mechanic`, `read-aloud`, `quote`,
etc.); doc/meta pages (`sys/**`, `vault/srd/spells/`, `vault/srd/monsters/`,
`vault/srd/items/`, and five migrated `vault/srd/rules/*.md` equipment
pages) take the generic set (`note`, `warning`, `tip`, …).

`[!dm]` is retired without replacement (`CampaignOS.RetiredCallout`) — a
page carrying one reclassifies its content into the row below that
actually matches, or folds it into plain prose.

### Fix — a generic callout on a play page

Convert to the play type the content actually is:

| Generic type | Convert to |
|---|---|
| `caution` / `warning` | `[!mechanic]` (hazard/trap) or plain prose (secret/handling) |
| `danger` | `[!mechanic]` |
| `important` | plain prose (handling note) or `[!mechanic]` (stat line) |
| `note` / `tip` | plain prose |
| `success` / `failure` | one `[!check]` with tiered **Success:**/**Failure:** lines |

### Fix — a play callout on a doc page

Use the generic set instead (`.claude/skills/callouts/references/generic-types.md`).

### Fix — DC in bare prose on a play page

A roll-gated branch belongs in a `[!check]`; a standing rule belongs in a
`[!mechanic]`. Bare `DC` text outside a callout on a play page always
fires except inside a run guide's `## At a Glance` section (a deliberate
compressed index of DCs whose adjudicating callout lives in the scene
file).

### Fix — `[!check]` with no title split

`[!check]` needs a `"<Skill> — <Label>"` title
(`.claude/skills/callouts/references/check.md`).

## Edge cases

- Excluded entirely: `vault/stories/`, `vault/ideas/`,
  `vault/campaigns/shattered-sea/pcs/combat-profile/`, `vault/campaigns/shattered-sea/pcs/character-sheets/`, the
  `vault/campaigns/shattered-sea/pcs/va-scripts/dm-voice-script.md` file, and the canon-review workflow blocks
  (`[!warning] CONTRADICTION`, `[!success] RESOLVED`).
- `vault/srd/items/` and the five migrated `vault/srd/rules/*.md` equipment
  pages accept either doc or play callouts — some entries formalize a
  rollable mechanic as a real `[!check]`/`[!mechanic]`, which is a strict
  upgrade over bare prose, not a family violation.
