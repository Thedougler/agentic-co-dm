---
paths:
  - "**/.claude/skills/**"
---

# Skills Contract

Contract for every campaign skill in this repo, directory-scoped to the
narrowest subtree's `.claude/skills/` root it governs. It binds by being this
file; a SKILL.md never restates it, and never declares its own conformance to
it. A skill's body is skill content only — governance metadata about the skill
belongs here, not in the file every invocation pays for.

- Write only to the paths your type owns (`vault/refs/runbook-wiki.md` § Who
  writes what). Prep-family skills write their content type's final
  `vault/`-tree path (including `vault/campaigns/shattered-sea/pcs/` and
  `vault/episodes/`) at `status: pending`, instantiated from
  `_templates/<type>.md` — never `status: canon`, never `publish: true`.
- Inputs missing -> ask the human the specific question, never invent the
  answer and never "need more info" (a vague ask gets a vague answer).
- SKILL.md stays ≤200 lines: frontmatter, the contract line, a short
  orientation, the workflow skeleton every invocation needs, and a pointer
  table to `references/*.md` in the same skill dir. Heavy format specs, long
  checklists, worked examples, and rationale live in `references/*.md`, one
  topic per file (every inline line bills every invocation).
- Descriptions anchor on repo context and phase verbs ("Use when prepping a
  session in a Campaign OS repo…") so they never fire in an unrelated
  project or on generic D&D chat, where their greps would fail confusingly.

## Skills authored elsewhere

No skill is exempt from this contract — a skill that documents an outside
tool (an Obsidian plugin, a language's patterns) is held to it exactly like a
pipeline-native one, because every loaded skill bills the same context and
steers the same model.

A skill copied in from outside this repo is adopted in the same turn it
lands: track it in git, rewrite its `description:` to house form (repo
context plus phase verbs), delete every frontmatter key outside the
allowlist, and bring it under the line cap by moving heavy specs,
checklists, examples, and rationale into `references/*.md`. `npm run lint -- --rule W72`
(skill budget) and `npm run lint -- --rule W84` (skill frontmatter contract)
fail it until all of that holds.

Never leave a copied-in skill untracked -> instead: adopt it in the same turn
you copy it in (an untracked skill loads and steers the model while `git log`
shows nobody ever decided it should).

## Placement: the narrowest owning subtree

A skill lives in the `.claude/skills/` root of the narrowest directory
whose files it governs: repo root for cross-cutting pipeline skills,
`vault/` for vault-wide authoring, `vault/episodes/`, `vault/stories/`,
`vault/ideas/`, `utils/wiki-cli/` for their own subtrees. A subtree
skill's description bills a session only once an agent touches that
subtree — placement is a context-cost decision: put a skill at the
deepest root that still covers every file it acts on. The live roster is
the union of every skills root: `find . -path '*/.claude/skills/*/SKILL.md'`.

## Drafting guides are not skills

Guidance for authoring a `vault/` page lives at
`.claude/skills/draft-content/references/<type>.md`, not in a skill of its own (ADR-0031).
`draft-content` is the single model-invoked router from a page path to its
guide; `vault/CLAUDE.md` and `docs/guardrails/CONTENT.md` reach it. A type
still carrying a `<type>-prep` skill has not migrated yet -> `draft-content`'s
table routes to whichever of the two currently owns it, so the table is the
one place that answers "what owns this type".

Everything a guide shares with its siblings — the stub check, the status
lifecycle, the common hard rules, the interview discipline, the
degrade/out-of-scope/checklist/handoff lists — lives once under
`vault/refs/vault/_common/` and is pointed at, never restated.
