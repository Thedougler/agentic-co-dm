> Superseded by [REFACTOR-PLAN.md](../../REFACTOR-PLAN.md) — the convergence refactor that reworked, executed, or retired this spec.

You are a senior technical writer and tooling engineer specializing in docs-as-code, Obsidian vaults, and the Vale prose linter. Your job is to audit this local workspace, interview me about key decisions, then implement a production-ready Vale setup that enforces Obsidian LLM-wiki best practices.

## Goal

1. Audit the local system and vault structure.
2. Interview me in depth about decisions before writing files.
3. Create and configure Vale for an Obsidian LLM-wiki (raw/ immutable sources + wiki/ LLM-maintained pages + schema).
4. Stop after setup + a short verification report. Do not invent wiki content.

## Phase 1 — Audit (read-only first)

Inspect the workspace thoroughly. Report findings before asking questions.

Check and summarize:

- Whether this is (or should become) an Obsidian vault (`.obsidian/`, markdown layout).
- Presence of `raw/`, `wiki/`, schema files (`CLAUDE.md`, `AGENTS.md`, `SCHEMA.md`), `index.md`, `log.md`.
- Existing `.vale.ini`, `styles/`, or other lint configs.
- Whether Vale is installed (`vale -v` or equivalent); note OS and install method if missing.
- Editor/CI hints (VS Code settings, GitHub Actions, package managers).
- Markdown volume and folder conventions (kebab-case vs TitleCase, frontmatter patterns).
- Anything that would conflict with a root-level Vale config.

Output a concise audit: structure, tooling state, risks, and recommended placement for Vale files.

## Phase 2 — Interview (required before writing)

Use focused questions. Do not assume. Cover at least:

1. **Scope**
   - Lint only `wiki/**/*.md`, all `*.md`, or custom globs?
   - Should `raw/` be mostly exempt (spelling only / off)?

2. **Style packages**
   - Base packages: Google, write-good, alex, Microsoft, proselint, Readability? Confirm a minimal set (default proposal: Google + write-good + alex).

3. **Custom style name**
   - Default: `LLMWiki`. Confirm or rename.

4. **Severity**
   - `MinAlertLevel`: suggestion | warning | error?

5. **Vocabulary**
   - Project/domain terms, product names, Obsidian/plugin terms to accept?
   - Any terms to reject?

6. **Filename & link conventions**
   - kebab-case vs TitleCase for wiki pages?
   - Prefer `[[wikilinks]]` over markdown links inside `wiki/`?

7. **Frontmatter**
   - Required keys (e.g. title, type, tags, sources, created, updated, confidence)?
   - Note: Vale cannot fully validate YAML schemas; we may add light rules + a note to complement with Obsidian Linter / a script.

8. **Prose rules to enable first**
   - Confirm priority among: hedging/weak language, preferred terminology substitutions, heading punctuation, sentence length, inclusive language, American vs British spelling.

9. **Editor / CI**
   - VS Code Vale extension? Obsidian Vale plugin? GitHub Action later?

10. **Install**
    - May I install Vale if missing (brew/choco/winget/binary)? Prefer which method?

Ask only what you still need. Batch questions. Wait for my answers before Phase 3.

## Phase 3 — Implement (only after interview)

Create a clean, minimal, documented setup:

### Layout (adjust paths only if audit requires)

```text
.vale.ini
styles/
  LLMWiki/          # custom rules (.yml only)
  config/
    vocabularies/
      LLMWiki/
        accept.txt
        reject.txt
```

### `.vale.ini` requirements

- `StylesPath = styles` (or agreed path)
- `MinAlertLevel` as decided
- `Packages = ...` as decided
- `Vocab = LLMWiki` (or agreed name)
- Sensible `IgnoredScopes` / `TokenIgnores` for code, Obsidian templates, math if relevant
- `[*.md]` BasedOnStyles including Vale + LLMWiki + chosen packages
- Softer or empty rules for `raw/**/*.md` if we agreed to exempt raw
- Optional tighter section for `wiki/**/*.md`

### Custom `LLMWiki` rules (start small, high-signal)

Implement a focused initial set as individual `.yml` files, for example:

- Hedging / weak language (existence): simply, obviously, just, clearly, everyone knows (tune to our decisions)
- Terminology substitutions (substitution) for any agreed swaps
- Heading end-punctuation (existence, scope: heading) if desired
- Sentence length (occurrence) only if we agreed on a max
- Any project-specific existence/substitution rules from the interview

Each rule: clear `message`, appropriate `level`, `extends` correct check type. No `.yaml` extensions.

### Vocabulary

Populate `accept.txt` / `reject.txt` from interview + obvious local terms found in the audit (wiki page titles, product names). One term per line.

### Install & sync

- Install Vale if missing and permitted.
- Run `vale sync` for packages.
- Run `vale` on a small sample path (e.g. `wiki/` or a single file) and fix config errors.

### Documentation

Add a short `styles/LLMWiki/README.md` (or a section in existing schema) explaining:

- What Vale enforces
- How to run it (`vale wiki/`, `vale path/to/file.md`)
- How to add vocab and new rules
- That graph/orphan/broken-wikilink checks remain agent/schema concerns, not Vale

## Constraints

- Prefer editing/creating only Vale-related files unless install requires otherwise.
- Do not modify `raw/` content.
- Do not bulk-rewrite wiki notes.
- Do not over-engineer: small rule set first; progressive disclosure over a huge rulebook.
- Match existing repo conventions when they exist.
- After setup, give a brief verification report: files created, sample `vale` output, remaining manual steps (editor extension, CI).

## Start

Begin with Phase 1 audit now. Then interview. Implement only after I answer.
