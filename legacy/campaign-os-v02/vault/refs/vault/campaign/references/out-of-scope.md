## Out of scope

Full routing table, one row per boundary: `.claude/skills/draft-content/references/campaign.md`
§ Boundary & hand-off.

Detail beyond that table:

- An NPC's or faction's own page also covers any Front mechanics it
  carries — write those on the NPC/faction page
  (`.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/faction.md`),
  never here.
- Transcribing content from an existing source document is
  `llm-wiki-ingest`'s fidelity-only job — Hard Rule 1: a claim with no
  source text backing a field gets a stub, never an invented detail
  (`.claude/skills/llm-wiki-ingest/SKILL.md`).
- The prose polish hand-off is `draft-story`'s, once facts and Safety &
  Tone are set — its `DS9` GM sign-off checkpoint
  (`.claude/skills/draft-story/SKILL.md`).
- Writing `vault/campaigns/` outside the draft/pending flow, or flipping
  `status:`/`publish:` past `pending`, belongs exclusively to
  `transcript-ingest` (`.claude/skills/transcript/SKILL.md`)
  and PUBLISH (`vault/refs/runbook-publish.md`).
