---
name: content-type-scaffold
description: Scaffold a brand-new wiki content type — its `_templates/<type>.md` and companion `.claude/skills/draft-content/references/<type>.md` guide — for a Campaign OS repo (vault/ present). Use when about to author content of a type with no matching template yet, or when W19 flags a `vault/<folder>/` with no template or drafting guide. Not for a type that already has both, and not for one-off page content itself.
---

# Content Type Scaffold

Root, cross-cutting — lives at
`.claude/skills/content-type-scaffold/`.

Builds the `_templates/<type>.md` + `vault/refs/vault/<type>/GUIDE.md` pair a
genuinely novel content type needs, by researching how the type is already represented
elsewhere rather than inventing a design from a blank page. Reuse or
repurpose an existing design first — every other content type in this repo
already has this pair; a new one gets built the same weight-bearing way.

## Workflow

Run all five steps in order; step 5 doesn't start until steps 1-4 produce a
validated template.

1. **Research remote exemplars — web only, never local code.** `WebSearch`/
   `WebFetch` for an existing Obsidian-vault template for this content type
   first — many are free online. If no Obsidian-specific template exists,
   research how the content type is represented in text form by official
   sources (the game system's own text) or high-quality community/
   third-party sources. Goal: reuse or repurpose an existing design.
2. **Match exemplar count to local references.** Find every existing local
   instance of this content type already sitting in the repo (an
   ingest-queue entry, a draft page, a source document under
   `raw/`). Find at least one remote exemplar per local reference for a
   balanced comparison — more than one where available.
3. **Design the template** — `_templates/<type>.md`, concise, focused,
   flexible, reusable — built from the remote exemplar(s). Copy the
   governed frontmatter spine from `vault/_templates/_refs/_ref.md` (the
   authority; W55 checks conformance), add per-type keys and fixed H2
   section headings. A key with a fixed set of legal values declares it
   as a closed-enum trailing comment (`# a | b | c` — convention:
   `vault/_templates/CLAUDE.md` § Enum comments); W54 then validates pages
   against it with zero rule code. `vault/_templates/CLAUDE.md`'s
   ownership rule: the template owns shape, its companion skill owns
   quality — don't put procedural or quality guidance in the template body.
4. **Validate the template against local content.** Check the template
   against every local reference found in step 2 — every field the local
   content actually needs has a place; nothing forces content that doesn't
   fit. Revise before treating it as final.
5. **Create the companion drafting guide** at
   `.claude/skills/draft-content/references/<type>.md`, with a `vault/refs/vault/<type>/references/`
   directory beside it for type-specific checklists, examples, and toy-chest specs —
   never a `.claude/skills/<type>-prep/`
   skill (`.claude/rules/skills.md` § Drafting guides are not
   skills). Copy the shape every sibling guide uses — read
   `.claude/skills/draft-content/references/faction.md` as the model: a `## Template` pointer
   naming `_templates/<type>.md` and its fixed headings, `## Read first`,
   `## Hard rules — this type only`, `## Interview — this type only`,
   `## Before you ship`, and a `## Reference files` table. Everything shared
   with sibling types — the stub check, the status lifecycle, the common
   hard rules, the degrade/out-of-scope/checklist/handoff lists — is pointed
   at in `vault/refs/vault/_common/`, never restated. Type-only
   checklist additions go in `vault/refs/vault/<type>/references/checklist.md`.
   Validate by actually using the new template + guide to author the real
   content that triggered this procedure — a successfully authored,
   lint-clean page is the proof.

## After scaffolding

- Add a row for the new type to `.claude/skills/draft-content/SKILL.md`'s
  routing table (page path -> guide), and add
  the type to `vault/CLAUDE.md`'s drafted-type trigger list — the router
  table is the one place that answers "what owns this type".
- Map the type to its home folder in `DEFAULT_TYPE_HOME`
  (`utils/wiki-cli/src/wiki_cli/rules/w95-type-folder-placement.mjs`) so W95 enforces
  placement. Edit that constant, never `thresholds.json`'s `TYPE_HOME`,
  which replaces the whole list rather than extending it.
- Add the new folder's entry to W19's exception table
  (`.claude/skills/llm-wiki-lint/SKILL.md`'s W19 grep) only if the new
  folder sits under `vault/srd/` or `vault/campaigns/*/` — W19 scans only
  those two globs — and its name doesn't reduce to its type by stripping a
  trailing `s`. Most won't need an entry.
- Hand off to the new guide for the actual content — this skill's job ends
  once the pair exists and the triggering content is authored.

## Owned paths

Writes `_templates/<type>.md` and `.claude/skills/draft-content/references/<type>.md` (plus
its `vault/refs/vault/<type>/references/checklist.md`), and the router rows above. Never writes
`vault/` page content directly (including
`vault/campaigns/shattered-sea/pcs/`) — the new guide owns that, same as
every other type.
