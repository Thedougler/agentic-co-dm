## Project — vault/episodes/ (session pipeline)

1. Canon is simple: **played at the table = `status: canon` in frontmatter, edits additive-only**; **not yet played = `status: pending`, edit freely**. Canon state lives in frontmatter ONLY — prose states facts plainly, no provenance narration (git log is the history).
2. Recap length is judged, not counted (ADR 0028) — the recap QC profile's BREVITY row owns it.
3. Every phase pastes its markers (PREP:, CAPTURE:, INGEST:, RECAP:, PUBLISH-CHECK:) from real tool output in the same turn. No marker, phase isn't done.
4. Pending content NEVER appears in recaps or the site; INGEST promotes what actually hit the table.
5. Unsure whether something was revealed at the table? It wasn't — grep the transcript, paste the line, then decide.
6. Creative work (governed .md prose in vault/**): rules above bind facts, canon, structure, visibility — never style. Kit CODE/PLAN/VERIFY routing + iron rules don't bind it either — read docs/guardrails/PROJECT.md. Invent boldly inside these rails; a timid minimum-risk draft violates this rule.

Routing: session pipeline → vault/refs/runbook-session.md, runbook-ingest.md, runbook-recap.md, runbook-publish.md. Wiki edits → vault/refs/runbook-wiki.md.

- Audio file appears in vault/episodes/NNN/audio/ → read vault/refs/runbook-ingest.md
- About to write "recap" or "session summary" → read vault/refs/runbook-recap.md
- User says "prep", "next session", "encounter", or you're about to prep a session/quest/season/arc (narrative-scale, multi-scene) → read vault/refs/runbook-session.md for the phase steps; the story-first gate itself is CLAUDE.md's Project zone, not restated here
- Read tool returns a vault/** file (incl. the vendored SRD/craft reference material under it) → fix any lint finding now, same turn, never NOTED (not done) (docs/guardrails/PROJECT.md PJ15)
