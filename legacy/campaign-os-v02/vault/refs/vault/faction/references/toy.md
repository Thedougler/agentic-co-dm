---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The five Faction fields, what belongs in each, and the good/bad pair that shows the difference."
created: "2026-08-03"
updated: "2026-08-10"
tags: [politics]
uid: dc290fea-d72d-4a4e-9e17-789ea9e70503
---

# Faction fields (good/bad pairs)

Write these once, as a markdown table in the DM-only material. No
frontmatter duplication.

Same discipline `.claude/skills/composing-beats/references/runtime-surface.md` §3 states
generically, applied to each field:

| Field | Content | Rule |
|---|---|---|
| `primary_goal` | What they always want | A vector, not a state: "accumulate enough leverage to force the Harbormaster's resignation," not "is ambitious." |
| `consistent_method` | How they pursue it | A table-doable behavior: "offers a favor before naming the ask; never states a threat directly," not "manipulative." |
| `active_problem` | What's currently going wrong for them | A situation, not a feeling: "owes a creditor three favors with no clean repayment route," not "insecure about status." |
| `off_screen_action` | What they do when nobody's watching — the sandbox engine | Observable evidence the party can find, never internal state. ✓ "Seizes the Harbormaster's ledgers and installs their own inspector." ✗ "Continues to grow in power and influence." A *defined* vector, not a resolved outcome — `world-update` is what actually moves it between sessions. |
| `performance_hooks` | How members are recognized — visual identity, vibe | Table-doable, not lore-dump: something a DM can voice or show in one line. `vault/refs/vault/faction/references/content.md` § Member/Patron Flavor has a behavior × ancestry table for quick fuel. |

The legacy `link_of_relevance` field is dropped — it duplicated the
PC-Connection Requirement, which is already mandatory and already cited in
the interview; naming it a second time as a frontmatter-adjacent field
added no new discipline.
