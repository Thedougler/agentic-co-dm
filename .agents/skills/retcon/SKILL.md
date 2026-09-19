---
name: retcon
description: >
  Use only when the user explicitly asks to retcon a campaign wiki error; repair that DM-specified error everywhere in the live vault.
---

# Retcon

Correct a campaign wiki error only when the user's current message explicitly asks for a retcon; that request is the authorization to repair the live wiki directly, overriding FR-019 and lifecycle gates for this correction only.

## Start

1. Resolve the vault with the Config Resolution Protocol in `llm-wiki/SKILL.md`.
2. Read `$OBSIDIAN_VAULT_PATH/AGENTS.md` when it exists, and follow its wiki conventions unless this skill explicitly overrides them.
3. Parse the correction into:
   - the **original error**: every exact phrase, name, filename stem, alias, wikilink, or slug that must disappear.
   - the **truth**: replacement text, removal, or deletion target.
4. If the original error or truth is ambiguous, ask one focused question before editing.

Done: the vault path is known, owner conventions are loaded, and the exact original-error search set is explicit.

## Search

Search the resolved vault, not the repo unless they are the same path.

1. Search contents for each original-error form with exact, case-aware text search first.
2. Search likely variants:
   - Obsidian wikilinks: `[[Original]]`, `[[path/original]]`, aliases after `|`
   - Markdown links whose label or target contains the error
   - YAML `title`, `aliases`, `summary`, `sources`, relationships, and tags
   - slug and kebab forms used in filenames or links
3. Search filenames and directory names under the vault for the same forms.
4. Include live pages, owner pages, `journal/`, recaps, `index.md`, `hot.md`, `log.md`, `_raw/`, and archive-like wiki folders unless the DM explicitly excludes them.

Done: every hit is inventoried by path and kind: content hit, link hit, frontmatter hit, filename hit, or page whose existence is the error.

## Repair

Choose the smallest repair that makes the wiki unable to repeat the falsehood.

- **Replacement:** when the page remains valid and the truth is a direct substitute.
- **Removal:** when the sentence, bullet, alias, source, relationship, or link only exists to carry the error.
- **Whole-file deletion:** when the file itself is a false owner, duplicate owner, or false recap and cannot be made true without preserving the error.

Rules:

- Edit live wiki files in place.
- Do not leave "formerly X", "previously X", parenthetical explanations, aliases, backlinks, or redirects containing the original error.
- If deleting or renaming a page, repair inbound links, `index.md`, `hot.md`, `log.md`, and any manifest or dashboard entry that names it.
- Preserve unrelated page facts and local formatting.
- Follow existing helpers and conventions instead of copying their procedures here. Use local manifest, index, lint, and qmd maintenance commands when the loaded wiki conventions require them.

Done: every inventoried hit has been replaced, removed, or deleted.

## Verify

Verification is exhaustive and blocks completion.

1. Re-run every original-error search from **Search** against the resolved vault.
2. Re-run filename and directory-name checks.
3. Search common transformed forms introduced by the repair, including slug, title, alias, and wikilink variants.
4. If any original-error hit remains, return to **Repair**. The run is unfinished.
5. Run the narrow available wiki checks for touched files. Prefer the repo's existing focused lint and qmd maintenance helpers when present; report any unavailable helper without substituting a weaker success claim.

Done: every search for the original error returns 0 hits in the resolved vault.

## Report

Report only:

- the correction applied
- files changed, renamed, or deleted
- the zero-hit verification terms
- checks run and any check that could not run

Do not include the original error as a lingering explanatory note except inside the zero-hit term list needed to prove verification.
