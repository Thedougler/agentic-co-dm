---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-07-23"
tags: [craft]
summary: "Recreate an external methodology source as a lint-clean guide page, then use it to challenge and improve this repo's own skills/templates/process."
phase: any
uid: 61136cb0-bbb2-4b39-87c1-13196e408fa0
---

# Craft-improvement runbook (any external methodology adoption)

Run when a real gap surfaces against an external craft source. A technique this repo's skill or template actually lacks (not a taste preference) triggers this runbook. Orchestrates `find-guidelines`, the `guideline-recreator` agent, and the improve skill into one pipeline that recreates the source faithfully. The goal is to make it searchable and propose improvements against it. For detailed procedures, see `.claude/rules/docs.md` § DRY.

## When to use it

- A source (official guide, third-party framework, craft technique) has been found or handed over, and it bears on how this repo does something. This includes prep, encounter design, wiki craft, or the process-engineering layer itself (skills, templates, linters).
- The trigger is a **found gap**, not aesthetics: the source states a method, sequence, or step this repo's current skill/template doesn't cover or does worse. "I like this style better" is not a gate pass.
- Not for a campaign fact (NPC, location, faction, item, lore) hiding in the same source. That belongs to `llm-wiki-ingest`'s claim buckets, not this pipeline. See `find-guidelines` § Subtype boundary.

## Section: sequence

1. **Source arrives.** Via `Inbox/` (per `Inbox/CLAUDE.md`'s convention) or handed directly by the user. Either way, the source must resolve to one `source:` path and optionally one `source_url:`. A valid source is required to create a page.
2. **Triage with `find-guidelines`.** That skill confirms the source is guide material (process or methodology for this system, not campaign-specific claims). It runs the stub check against `vault/refs/` (or the source's topically-appropriate `vault/` directory) for an existing near-duplicate and prepares every input the recreation needs (slug, target path, `vault/_templates/_refs/_guide.md` contents, tags from `docs/tags.md`, the exact lint and archive commands).
3. **Dispatch `guideline-recreator` once.** Full spec, isolation contract, and tool scoping: `.claude/agents/guideline-recreator.md`. Never recreate the source yourself as a substitute — the main loop already knows this repo's conventions well enough to unconsciously filter the recreation through them.
4. **Guide lands** when the agent self-lints and self-archives before returning. A lint-clean page appears at its topically-appropriate path under `vault/refs/` — cross-cutting doctrine at the flat top level, prose/voice material under `vault/refs/stories/`, idea-generation material under `vault/refs/ideas/`, per-type methodology under `vault/refs/vault/<type>/references/` — or the source's topically-appropriate `vault/` directory outside `vault/refs/` (e.g. SRD material), with the source moved to its `raw/<YYYY-MM>/` path. `find-guidelines` runs the same lint command once more as independent confirmation. Never re-trust the agent's own report without corroboration.
5. **Guide joins the searchable craft corpus.** `npm run search:craft` indexes all of `vault/refs/**` (house canon and vendored guides together), and, for vendored SRD material outside `vault/refs/`, `npm run search:external`. No separate registration step is needed. Landing the file at the right path is what makes it findable.
6. **The improve skill searches it.** When improving a `vault/_templates/` file, a `.claude/skills/` skill, or any other campaign-os element, search craft docs first (using `npm run search:craft -- query "<topic>"` or `npm run search:external` for vendored SRD material) before proposing changes. The newly-landed guide is now part of what those searches surface.

## The GATE — nothing is sacred

Root `CLAUDE.md`, verbatim: "no element of campaign-os is sacred; that material holds real GM-expert D&D methodology (5e SRD, Sly Flourish's LGMRD/Monster Builder) to improve against, not just campaign facts."

This pipeline exists precisely to feed that challenge. A recreated guide is not shelf reference but ammunition for the next skill or template revision. Skip straight to search and propose only when a guide already covering the relevant territory exists under `vault/refs/` (or the relevant SRD directory). Otherwise, this runbook's steps 1-5 are the prerequisite, not optional scaffolding.

## Done

A lint-clean guide page exists at its topically-appropriate path under `vault/refs/` (or the source's topically-appropriate `vault/` directory) and is findable via `npm run search:craft -- query "<topic>"` (or `search:external` if it's vendored SRD material outside `vault/refs/`'s scope). Commit `content(craft): recreate <slug>` or fold into whichever improvement commit consumed it.
