---
type: agent-guidance
status: canon
publish: false
aliases: []
created: "2026-07-31"
updated: "2026-07-31"
tags: [survival]
summary: "The 60-second orientation map for the whole campaign-os system — what it is, the LLM-wiki pattern, the layers, the session loop, and the six laws."
phase: any
uid: 34490cc9-9b33-47c8-a541-1f81c8c2fd01
---

# Campaign OS Overview runbook (any system)

The standing orientation reference for the whole campaign-os system — read
this to answer "what is this repo, and how does it hang together" before
routing to any specific operation. The `campaign-os` skill points here
rather than restating it (`.claude/rules/docs.md` § DRY).

## What it is

A real D&D 5e campaign run with Claude Code as co-writer and co-DM. The
GitHub repo **is** the Obsidian vault **is** the single source of truth —
one file tree, no second database.

## The core idea: compile, don't retrieve

A domain specialization of Karpathy's **LLM-wiki pattern**: knowledge
distilled once into maintained `vault/` pages, never recalled from chat
memory nor re-derived per query. The `llm-wiki` skill owns the pattern and
the retrieval ladder.

## Three routers, plus a fourth standing system

`campaign-os` routes the *system*; `llm-wiki` routes *knowledge* operations;
`draft-story` routes *prose*. GM craft material is searchable via
`npm run search:craft`, spread across `vault/refs/` (flat top level, plus
`ideas/`, `stories/`, and `vault/<type>/references/`).

**Self-improvement is a fourth, standing system.** Friction with this repo's
*own* setup — a misfired skill, a stale doc, a rule the human had to repeat
— routes through `flag-the-gap`'s Observe → Diagnose → Fix → Prove loop,
never hand-patched inline (`vault/refs/runbook-self-improve.md`).

## The layers

Raw source → compiled artifact → player-facing:

```text
vault/episodes/NNN/transcript*  ──▶  vault/ + vault/campaigns/shattered-sea/pcs/ (canon, direct)  ──▶  utils/site/
   (raw, immutable)          (INGEST — a transcript is recorded      (Quartz;
                               play, the highest form of canon)      publish:true only)
```

`status: pending` is PREP-family, not-yet-played material only, authored at
its final path and promoted in place once INGEST confirms it hit the table.
A transcript's own facts skip that step: INGEST writes them `canon` in the
same pass it reads them.

## The session loop

One revolution per session, each phase gated on the last: PREP → RUN →
CAPTURE (`vault/refs/runbook-capture.md`) → INGEST (`vault/refs/runbook-ingest.md`)
→ RECAP → PUBLISH (`vault/refs/runbook-publish.md`).
Triggers, markers, commit verbs, gate-check: `vault/refs/README.md`.

## The six laws

Each makes one face of the LLM-wiki pattern mechanical (full mapping:
`llm-wiki`'s `.claude/skills/llm-wiki/references/pattern.md`):

- **L1. Grep, don't remember.** No fact enters an artifact without being read
  from the repo in the same turn, hit pasted. Chat memory is not canon.
- **L2. Only recorded play writes canon directly.** A transcript is evidence,
  not a draft. Every other source writes `status: pending`; a `canon-review`
  ruling is the only other path to canon.
- **L3. Default-deny publishing.** Player-visible needs `publish: true` AND
  content outside a DM-only section AND a passing leak check on the build.
- **L4. Templates, not freeform.** Every page instantiates a typed template.
  A page that doesn't conform doesn't merge.
- **L5. Numbers, not judgment.** Diffs > 40 lines review
  in chunks of 20. 2 failed lint fixes → escalate. Weak models obey countable
  thresholds and rationalize their way around graded ones.
- **L6. Every NEVER carries a replacement.** A banned action with no named
  alternative gets taken anyway under pressure.

## What it prevents

Canon drift (L1), secret leakage (L3), pipeline rot (L2), freeform sprawl
(L4), ledger rot (git log is the history), diffuse authorship (one owning
guide per content type).

## What "done" means for this system

Healthy = a fresh session with no prior context can know which phase the
campaign is in, answer any canon question by grepping the wiki, resume
any half-finished phase from its
runbook's gate, build the player site past `vault/refs/runbook-publish.md` §
Acceptance, and be audited by grepping a transcript for phase markers.
Missing markers at moments their triggers occurred are the non-compliance
to tune for.
