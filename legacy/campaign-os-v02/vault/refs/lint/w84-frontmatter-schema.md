---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
summary: "W84 frontmatter-schema findings: what generates the schema, the fix for each failure shape, and the enum-comment mechanism."
uid: 378025a8-0b86-4293-bf0c-5ab0be158d2e
---

# W84 — Frontmatter schema

Protects: every `vault/**` page's frontmatter validates against a JSON
Schema generated from its own `_templates/<type>.md` (layered on
`vault/_templates/_refs/_ref.md`'s shared spine); every `.claude/skills/*/SKILL.md` validates
against the skill-authoring contract instead (path-selected, since a
skill carries `name:`/`description:`, not `type:`/`subtype:`). Severity is
always `error` — a schema violation is a correctness gate, not ratchet
debt.

## Fix

The failing message names the specific key and what's wrong with it — fix
that value. Never delete the key to silence the finding.

### "No template resolves for type / subtype"

The page's `type:` (and `subtype:` if set) has no matching
`_templates/<type>.md` or `_templates/<type>-<subtype>.md`. Either:

- the `type:`/`subtype:` value is a typo — fix it to an existing type, or
- this is a genuinely new content type — chain-load the
  `content-type-scaffold` skill to build the template first.

### "Missing frontmatter key \"type\""

Nothing else validates until `type:` exists — add it before fixing
anything else the schema would otherwise catch.

### "Missing frontmatter key \"summary\"" / summary too long

Checked directly, not through the schema (so the message can name the
actual cap). Add a one-line summary, ≤200 characters
(`MAX_SUMMARY_CHARS`).

### An enum value rejected (e.g. bad `tier:` or `status:`)

A frontmatter key's allowed values come from its own template's trailing
`#` comment on that key, when the comment opens with a pipe-delimited
list (`core | supporting | peripheral`) — not from this script. To add or
change an allowed value, edit the comment in the relevant
`_templates/<type>.md` (or `vault/_templates/_refs/_ref.md` for a shared spine
key); nothing in the linting code needs to change. Full comment-parsing
contract: `vault/_templates/CLAUDE.md` § Enum comments. `status`/`publish` are
the one exception — validated against the fixed `STATUS_ENUM` constant in
`wiki.toml` `[thresholds]`, never a template
comment.

## Edge cases

- Colocated sub-index catalogs (`vault/**/_<name>_index.md`),
  `CLAUDE.md`, skill `references/*.md` files, `vault/ideas/`,
  `vault/stories/`, and `vault/campaigns/shattered-sea/pcs/va-scripts/` are exempt
  outright — none of them are template-typed content pages.
