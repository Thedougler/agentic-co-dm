---
name: campaign-writers-room
description: >-
  A room of rival writers for a Campaign OS repo (vault/ present). Use when the GM wants
  multiple takes on narrative prose, or a writers room to improve an existing piece. Runs
  compete mode (parallel stance-distinct drafts, judged, GM picks) or collab mode
  (draft → critique → revise). Invoked as /writers-room.
disable-model-invocation: true
---

# Campaign Writers Room

A room where stances compete, people don't. The GM brings a piece (or a
brief for one); the room returns rival drafts with distinct strengths, or a
critique-and-revise cycle — always as options for the GM's choice, never a
tournament with losers. The creativity contract governs throughout: facts,
canon, and constraints from the brief bind every drafter; style is free
(vault/CLAUDE.md rule 10 — "invent boldly").

## Phase 1 — Capture the brief (collaborative)

Open by building the brief WITH the GM, not interrogating them. Capture:

1. **Target** — the text or page to work on: pasted prose, a file path, or
   a brief for a piece that doesn't exist yet.
2. **Goals / direction** — what better looks like. "Improve generally" is a
   valid answer; specific direction ("more dread", "tighter", "give the
   villain a voice") shapes stance selection.
3. **Constraints** — facts that must not change, as wikilinks to the owning
   canon pages. Grep the wiki for the entities involved and paste hits
   (contract item 1); escalate empty/noisy lookups to `llm-wiki-query`.
4. **Mode** — `compete` (parallel rival drafts) or `collab` (one draft,
   critique waves). GM doesn't care → suggest: compete for fresh takes or
   "show me options", collab for improving an existing piece iteratively.
5. **N drafts** (compete only) — 2–8, default 3. "Best possible version",
   "full room", or "throw everything at it" → **8: one instance per stance**
   in `references/stances.md`, plus the synthesis wave (Phase 3a step 5).

Missing inputs → ask the specific question (degrade by asking); never
invent a target or constraints.

## Phase 2 — Stage

Staging dir: `vault/ideas/writers-room/<YYYY-MM-DD>-<slug>/`.
Write there, in order:

- `<staging-dir>/brief.md` — the captured brief, verbatim constraints included.
- `<staging-dir>/context-pack.md` — the canon slice drafters need, assembled via the
  `llm-wiki-context-pack` skill (written to staging for the subagents; the
  pack skill's no-repo-write rule doesn't apply to this staging copy).
- drafts land as `<staging-dir>/draft-a.md`, `<staging-dir>/draft-b.md`, ... ; `<staging-dir>/verdict.md` last.

All staging files are plain markdown — no wiki frontmatter, never
`publish:` or `status:` keys. Drafts never leave staging.

## Phase 3a — COMPETE mode

1. Spawn N `draft-writer` agents **in parallel — one message, one instance
   per draft**. Each prompt hands: the brief path, the context-pack path,
   **one stance** from `references/stances.md` (pick stances that pull
   toward the GM's stated goals; maximally distinct when the goal is
   general), and its own output path (`<staging-dir>/draft-a.md`, `<staging-dir>/draft-b.md`, ...).
2. When all drafts land — every `draft-writer` returned, none still
   running — run `npm run lint -- <staging-dir>` and fix until it reports
   zero findings. The rewrites it forces land on the same sentences the
   judge would score, so a ranking taken now is thrown away.
3. Only with step 2 at zero, and in its own message: dispatch
   `content-quality-checker` with the `comparative` profile over the
   staged drafts → write its `RANKED` output to `<staging-dir>/verdict.md`.
4. Present to the GM: the ranking, plus a one-paragraph digest of each
   draft — its stance, its distinct strength, where it shines. **The GM
   picks or directs a merge — never auto-select**, and the ranking is
   advisory input to that choice, not the choice.
5. **Synthesis wave (optional — default for a full 8-stance room, offered
   otherwise).** With the GM's go: spawn one more `draft-writer` handed the
   brief, the top drafts the GM names (2–3), and `<staging-dir>/verdict.md`, instructed
   to merge their named strengths into `<staging-dir>/draft-synthesis.md` — a best-of
   version, not an average (take draft C's opening, draft A's villain
   voice, draft F's closing image, per the verdict's quoted evidence). Lint
   that synthesis to zero (`npm run lint -- <staging-dir>/draft-synthesis.md`)
   before the judge sees it, then
   resume that same `comparative` judge instance (`SendMessage`, never a
   fresh dispatch — agent spec § Rounds), handed only the synthesis path —
   it already holds the parent drafts — so the GM sees whether the merge
   actually beat them. The synthesis is one more option on the table — the
   GM still picks.

## Phase 3b — COLLAB mode

Waves, 1–2 cycles:

1. **Draft** — one `draft-writer` instance (drafter stance GM-chosen, or
   pick the stance matching the goals) → `<staging-dir>/draft-a.md`.
2. **Critique** — a developmental findings report against
   `vault/refs/stories/developmental-craft.md` (structure, character, scene,
   line) and `writing-style` apply, plus what's working —
   continuity is step 3's job. Frame findings to the GM as improvement
   opportunities, not failures.
3. **Continuity** — `continuity-checker` over the draft; canon conflicts
   surface as `CONFLICT:` blocks for the GM to adjudicate.
4. **Revise** — `draft-writer` again, handed the draft, the findings, and
   the GM's steering → next draft file.

Then present the result to the GM with what changed and what remains open.

## Phase 4 — Land

The chosen/merged text is handed to the **owning skill for the page type**
— `<type>-prep`, `recap-writer`, `draft-run-guide` — to file at
`status: pending`; a brief targeting a story-shelf chapter lands via
`draft-story` at `vault/stories/` instead. This skill never writes
`vault/`, `vault/campaigns/shattered-sea/pcs/`, or `vault/campaigns/` pages itself. Staging dir is kept by default (it's fragments
material) or pruned at the GM's word.

## Hard rules

- The GM decides the winner — a ranking, a critique, or a checker verdict
  never selects for them.
- Drafts never leave staging; landing goes through the owning skill only.
- Brief facts/canon constraints bind every drafter; style never binds.
- One finding never blocks presenting drafts — QC informs the GM's choice,
  it doesn't gate it. This is creative work, not a lint gate.
- Never flip `publish:` or `status: canon` (contract item 5) -> leave both keys untouched and let the owning skill file the landed text at `status: pending`.

## Read chain

Campaign facts → `llm-wiki-query` (grep first, paste hits). Context
assembly → `llm-wiki-context-pack`. Missing anything → ask the GM.

## References

| File | When to read |
|---|---|
| `references/stances.md` | Picking stances for draft-writer dispatch — one stance per instance. |
