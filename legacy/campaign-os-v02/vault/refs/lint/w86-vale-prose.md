---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-08"
tags: [craft]
summary: "W86 Vale prose findings: why the finding's own message is the fix, and where a genuine false positive gets corrected."
uid: 51991721-f396-4d74-8b6d-b0d837627d45
---

# W86 — Vale prose findings

`W86` is every finding from a Vale style check (`CampaignOS`,
`CampaignDiegesis`, `CampaignLiterary`, `AgentGuidance`, `Readability`,
`proselint`, `write-good`, `ai-tells`) — recognizable by a dotted rule id
(`CampaignOS.BannedCliches`), never a bare `W`-number. Full style
inventory and each package's purpose: `docs/vale-styles/README.md`.

## Why W86 carries no legend fix

Every other rule family gets a one-line remediation
(`FIX_BY_FAMILY`/inline em-dash split) because the fix is genuinely
instance-independent. Vale checks are freeform prose findings — the
message itself, on the finding's own line, IS the remediation. There is
no general "the fix for a Vale hit" sentence to hoist into a legend.

## Fix — the rule's intent binds, not its regex

Rewording the flagged text so the pattern stops matching while the
underlying problem stays true is evasion, not a fix (`CLAUDE.md` iron
rules). Two forms specific to Vale prose checks:

- **A game-mechanical term is never synonym-swapped.**
  `docs/vale-styles/CampaignOS/MechanicalTermSynonym.yml`'s own message
  names the fix (wikilink the defined term to its `vault/srd/rules/`
  page) every time it fires — the mechanic's wording IS the term, never
  swap it for a synonym.
- **A verbatim SRD/transcript quote stays verbatim.** If a rule fires
  inside quoted rules text or a cited transcript line, the fix is a Vale
  vocabulary/token-ignore exception, never editing the quote to dodge the
  pattern.

## Fix — a genuine false positive

`CLAUDE.md`'s rule governs (fix the rule's term list, not the instance;
two failed fixes on the same lint → stop and ask). The two places a Vale
rule's term list lives:

- Spelling/terms allowlist:
  `docs/vale-styles/config/vocabularies/CampaignOS/accept.txt` (one regex
  per line, grouped by category with a comment explaining the exception).
- A rule's own token/pattern list: its own
  `docs/vale-styles/<Style>/<RuleName>.yml`.

Full "adding a rule/term" procedure, plus the two pattern shapes that
make a Vale rule silently dead: `docs/vale-styles/README.md` § Adding a
rule / § Adding a vocab term.

## Which pass blocked you

`.vale.ini` and `.vale-hard.ini` read the same styles at different
severities — `.vale.ini` is informational and never blocks;
`.vale-hard.ini` scopes to `CampaignOS` only and gates on
`level: error` alerts there alone. Full mechanism,
including why Vale findings sit outside the markdownlint W-rule ratchet:
`docs/vale-styles/README.md` § The advisory-vs-hard split.
