---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /language-edit command's three-pass system (errors, refinement, final sweep), including Pass 3's minimal-by-design rule."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 9e7d7cab-d797-4ebd-9565-feac2cfb1a36
---

# Stories Playbook: /language-edit ch-XX 1|2|3

Pass number is required. If not given, asks: "Which pass? 1 (errors), 2 (refinement), or 3 (final sweep)." **If pass 2, and currently on Sonnet, tells the author the pass benefits from Opus and suggests switching with `/model opus`, then waits.**

Locates the file (in Chapters/ by name match, or the story root for short stories). Reads the story's own instructions and the vault-level instructions to distinguish intentional stylistic choices from real errors. Deliberate form is never flagged. Reads the prose aesthetic guidance at `vault/refs/stories/prose-aesthetic.md`, the single source of truth for the author's aesthetic. Any pattern described there is intentional and must not be flagged.

Standard across all three passes (American English, Chicago Manual of Style/CMOS conventions, Oxford comma).

**Output format, all passes:** inline edits use ~~strikethrough~~ for deletions and **bold** for additions per paragraph; a paragraph needing no changes returns unchanged with Polish Note "No substantive corrections needed"; Polish Notes are labeled sequentially (PN1, PN2, PN3…) across the full chapter. The entire chapter is processed. No summarizing or commentary appears outside the Polish Notes.

**Pass 1. Errors.** Fix what is broken. Don't chase subtlety (Pass 2's job).

- Corrects: grammar and syntax. It covers CMOS punctuation (American quotation, Oxford comma, capitalisation, numbers), non-native constructions causing misreading, and dummy pronouns or unclear references where fixing yields a clear improvement. It maintains past-tense narration except inside dialogue.
- Does not: fix phrasing that's grammatically correct but sounds slightly non-native (flags for Pass 2 instead). It does not rephrase for style, rhythm, or flow. It does not add, remove, or invent content.
- Polish Note: one line showing what was corrected and why. Pass 2 flags quote the phrase and note "Pass 2: [brief reason]."

**Pass 2. Refinement.** Assumes errors are fixed. It targets what is technically correct but still sounds non-native to a fluent ear. Prompts the Opus switch above.

- Targets: non-native constructions specific to the author's first language (per the vault's recorded language background). This includes article use, literal prepositions, calqued idioms, source-language word order, and grammatically acceptable but non-native constructions. It also addresses idiomatically weak phrasing even when not wrong and distracting word repetitions (lists up to three alternatives, without forcing replacement).
- More assertive than Pass 1 on idiomatic fixes, but preserves voice. Intentional or register-fitting constructions are left alone.
- Polish Note: two parts on one line separated by `|`. Part A shows what was done. Part B provides rationale, quoting flagged phrases with alternatives separated by semicolons. Example: `PN4: Changed "he was feeling" to **he felt** | Non-native: source language uses progressive where English prefers simple past in narration; preserves tense and voice.`

**Pass 3. Final Sweep.** Read as if seeing the text fresh. Flag only what actually sticks out. **Minimal by design. Do not manufacture changes.**

- Corrects only: actual grammatical or consistency errors that slipped through or CMOS issues not caught earlier. Also corrects anything making a native reader pause involuntarily.
- Does not: re-examine idiomaticity already addressed; rephrase for preference; add commentary on structure, pacing, or style.
- Polish Note: one line, or "No substantive corrections needed." **If many changes appear, stop and reconsider whether a Pass 2 would be more appropriate instead of continuing the sweep.**

All passes return inline markup with sequential Polish Notes. The author selects changes, and nothing is applied automatically.

See also: [[dev-edit]], [[writing-style-profile]], [[global-rules]].
