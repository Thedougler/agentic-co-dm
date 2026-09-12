---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-08"
tags: [craft]
summary: "W25 unlinked entity mentions and W75 dead doc pointers: what each detects and how to resolve it."
uid: 07b50ce2-658b-4e1f-9844-9c15f2dadd17
---

# W25/W75 — Unlinked mentions & dead doc pointers

Both are detection-only, soft findings — neither auto-inserts a fix.

## W25 — unlinked entity mention

Fires when prose names a page (by title or a frontmatter alias) but never
`[[wikilinks]]` it anywhere on the page.

Fix: wikilink the first (or clearest) mention of the named entity — the
`cross-linker` skill resolves the judgment call — never every repeated
mention. If the only place left to put the link is a trailing
"See Also"-shaped list, stop: see `vault/refs/lint/w123-link-footer-section.md`
instead.

A genuine false positive (an ordinary English word, not a reference) →
add it to `UNLINKED_MENTION_STOPLIST` in
`wiki.toml` `[thresholds]`. A real mechanic term
inside the excluded SRD glossary (`vault/srd/rules/**`) worth linking →
add it to `UNLINKED_MENTION_ALLOWLIST` there instead. Never hand-fix the
page to dodge either list.

## W75 — dead doc pointer

Fires when an agent-facing doc (`.claude/skills/`, `.claude/agents/`,
`.claude/rules/`, `vault/_templates/`, `docs/guardrails/`, `vault/refs/`,
`CLAUDE.md` at any depth) points another file by a path that resolves
from neither the repo root nor the pointing file's own directory.

Fix: repoint the path to the target's real repo-root-relative location —
find it with `git ls-files | grep <basename>` — or delete the pointer if
the file is genuinely gone.
