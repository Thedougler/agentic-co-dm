---
type: runbook
status: draft
publish: false
aliases: []
created: "2026-07-22"
updated: "2026-08-08"
tags: [craft]
summary: "Bring non-transcript Inbox sources into the wiki: similarity-check, decompose to pending pages via llm-wiki-ingest, archive, record."
phase: any
uid: d7b50b76-16a7-4d85-a562-469896c50f1a
---

# INGEST-INBOX runbook (any: Inbox to wiki)

Run when `inbox/` holds new non-transcript source material (homebrew, legacy docs, setting notes) to bring into the wiki. Orchestrates the inbox toolchain and the `llm-wiki-ingest` skill; per-file mechanics live in `inbox/CLAUDE.md`. Session-transcript ingestion is a different pipeline — [`runbook-ingest.md`](vault/refs/runbook-ingest.md) (Phase 4), not this one.

GATE: `npm run inbox:check`. Paste the pending-source list. Empty means nothing to ingest, so stop.

1. Per source, stub/similarity-check first (llm-wiki-ingest Hard Rule 3: `npm run inbox:similar -- -f <path>`). Paste `INGEST-INBOX: <source>: <new | expands [[page]]>`.
2. Decompose and write back with the `llm-wiki-ingest` skill in new-source mode — it owns fidelity, provenance, and status.
3. A source that isn't decomposable prose (a session record, a character sheet, an art/map asset) hands off instead of ingesting here — llm-wiki-ingest's Hard Rule 5 and Claim buckets own the routing.
4. Archive each finished source: `npm run inbox:archive`.
5. Lint the wave (`llm-wiki-lint`). Obey each FIX line before finishing.

Done = INGEST-INBOX: <N sources, M pages at pending>, archived + recorded, commit `ingest(<source-slug>): ...`
