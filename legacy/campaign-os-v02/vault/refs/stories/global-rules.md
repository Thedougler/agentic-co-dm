---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "Vault-level CLAUDE.md global rules: language editing, developmental editing, editing permissions, consistency checks, story-context loading, session-start behavior, and Obsidian-skill lookup."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: db8e4c9a-90b4-49e6-ad98-af3cd726a08b
---

# Stories Playbook: Global Writing Rules (vault rules file)

Story-specific rules in each story's own rules file override these where they conflict.

**Language rules** (applied during all `/language-edit` passes):

- Flag non-native constructions: unnatural article use, verb tense confusion, over-formal register, idioms reading as direct translations.
- Prefer simple, direct sentence structure. Flag run-ons or complex subordinate clauses that impede clarity.
- Watch for excessive passive voice, adjective order errors, misplaced adverbs, plural/singular agreement errors.
- Aim for natural, idiomatic English prose, not formal or translated-sounding.
- Never auto-apply corrections. Present the original text, the issue, and a suggested fix. The author decides.
- If writing in English as a second language, describe the native language in the Author section and update these rules to reflect that language's common patterns. `/language-edit` Pass 2 uses them to calibrate.

**Developmental editing defaults** (applied during all `/dev-edit` passes unless a story's own rules file overrides them):

- Flag telling instead of showing in emotional beats.
- Flag pacing issues: scenes that stall without narrative purpose, transitions that rush significant moments.
- Flag on-the-nose dialogue, or dialogue existing only to deliver exposition.
- Flag repetition of words, phrases, or ideas within a chapter.

**Editing rules:** never change chapter/story file content unless explicitly instructed. When reviewing a chapter, present suggestions only. The author applies changes manually. Exception: batch operations (e.g. renaming a character across all files) when explicitly requested. `/update-chapter` may only change frontmatter and tracking files (Timeline.md, Character files, Location files). It must never alter chapter prose.

**Consistency rules:**

- Use character names exactly as they appear in their Character file. Flag any variation.
- Use location names exactly as they appear in their Location file. Flag any variation.
- Flag any contradiction with Timeline.md.
- When uncertain about a world detail, check _Index.md before suggesting.
- If a Character file says a character is dead, never write them as alive.

**Story context:** whenever the author references a specific story by name, check whether a folder for it exists before responding. If it does, read that story's rules file, _Index.md, and `/_Lore.md` in full before engaging with any question about it. Don't rely on memory or prior context alone.

**Session start:** if the author's first message in a new session is a greeting, vague, or unspecific, respond with a brief welcome and present the available commands as options. Skip this if the first message is already specific.

**Obsidian skills:** when generating Obsidian-specific syntax (wikilinks, callouts, frontmatter, embeds, `.base` files), fetch the relevant skill from the `kepano/obsidian-skills` repository first rather than generating it from memory. Use the `obsidian-markdown` skill doc for `.md` content and the `obsidian-bases` skill doc for Bases views/filters/formulas.

See also: [[setup-and-plugins]], [[dev-edit]], [[language-edit]].
