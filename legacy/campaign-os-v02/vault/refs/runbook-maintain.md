---
type: runbook
status: draft
publish: false
aliases: []
created: "2026-07-22"
updated: "2026-08-08"
tags: [healing, travel]
summary: "Whole-wiki health sweep. Run the lint table at scale, route each finding to the skill that owns its fix, and drive the report to zero."
phase: any
uid: 24f753df-ab56-4549-bb34-bfa50f6a7ba9
---

# MAINTAIN runbook (any: wiki health)

Run when the wiki needs a health or cleanup pass (on demand, or after a bulk import/pull that bypassed the per-edit hooks). It never restates `llm-wiki-lint`'s own sweep, fix, or routing procedure.

GATE: know the scope (whole-repo, or `--since <ref>`). Unrelated edits already in the tree → commit or stash them first (this runbook commits only its own fixes).

1. Run the `llm-wiki-lint` skill over the scope. It owns the sweep, fixes what's mechanical, and routes every remaining finding to its owner. Paste its own markers as they land.
2. Friction the sweep surfaces in your OWN setup (a rule misfiring, a stale doc, a repeat correction) is not a content fix → hand it to `fix-on-discovery`, never hand-patch it here.

Done = MAINTAIN: report driven to {0 | only human-ruling items remain}, commit `chore(wiki): <scope>`.
