---
name: tag-taxonomy
description: >
  Audit, normalize, and extend the controlled tag vocabulary in docs/tags.md — resolves W13
  (unknown tag) and W27 (untagged page) findings. Use for "fix/normalize my tags", "tag audit",
  "tag hygiene", "my tags are a mess", after llm-wiki-lint surfaces a W13/W27, or when picking
  tags for a page being authored. Resolve W13/W27 autonomously per docs/tags.md.
---

# tag-taxonomy

Owns `docs/tags.md`. Resolves W13's judgment half — an
alias→canonical remap is mechanical and is `llm-wiki-lint`'s own job per its
Mechanical-vs-judgment table; a tag in neither the canonical list nor the
alias list is a taxonomy decision, handled here — and all of W27 (a page
with no tags at all). Never restate W13/W27's rule or FIX wording here —
run `npm run lint -- --rules`. Never restate the migration doctrine — read
`vault/refs/runbook-wiki.md` § Tag taxonomy. campaign-os has only **Domain** and
**Project** tag groups (no "type" tag slot — that's the `type:` frontmatter
field); entity-identity and origin tags are dropped by design, never
re-added as tags.

## Standard queries

```
# Every page's tag line
grep -rn "^tags:" vault/ --include="*.md"

# Pages carrying a given tag
grep -rlE "^tags:.*\b<tag>\b" vault/

# W13 findings (unknown tag, not canonical/alias/visibility)
npm run lint -- <path> --rule W13

# W27 findings (a page carrying no tag — both authored shapes)
npm run lint -- --rule W27

# Propose tags for every untagged page from its own evidence, no writes
node utils/scripts/derive-tags.mjs
```

## Owned write scope

Narrow and explicit — this skill never does anything else to a page:

- A page `tags:` value matching a listed alias in `docs/tags.md`
  → its canonical form.
- Trim an over-cap page (>5 non-`visibility/*` tags) to ≤5, proposing which
  to drop (keep the most specific/on-tone), confirmed with the human.
- A `tags: []` or missing-tags page (W27) → apply the closest-fit Domain
  tag read off the page's own subject, at any `status`. Never a role-label
  fallback (`reference`, `srd`, `rules`) → instead: read further; every
  page is about something.
- On confirmation only: append a canonical tag under `### Domain` or
  `### Project`, or a `- alias -> canonical` line under `## Aliases`, in
  `docs/tags.md` — see header gate below.
- Never: a prose edit, a `status`/`publish` flip, an entity-identity or
  origin tag re-added, a silent `docs/tags.md` append, a `visibility/*` tag
  touched (exempt from alias mapping, not counted toward the cap).

## Workflow

1. **Read the vocabulary** — `docs/tags.md`'s canonical tags, aliases,
   visibility group, rules. `TT1: <vocab read>`.
2. **Get findings** — the CLI query above, plus per-page `tags:`
   extraction for pages the CLI scope excludes. `TT2: <counts:
   alias-remap / unknown-≥2-pages / unknown-1-page / over-cap / W27
   empty>`.
3. **Classify** each against the migration doctrine (apply it, don't
   restate it): identity/origin token → never re-add as a tag; matches a
   listed alias → canonical (mechanical, fix directly); unknown on ≥2
   pages → propose adding to `docs/tags.md` (ask); unknown on exactly 1 page →
   propose the specific remap target or a drop, and **ask** — see red
   flags below; over-cap → propose a trim; W27 empty → derive the
   closest-fit Domain tag from the page's own subject and apply it. Never
   fall back to a role label (`reference`, `srd`, `rules`) → instead: read
   what the page is about and name that tone. `TT3: <classification>`.
4. **Check each affected page's `status`.** `draft`/`pending` → apply.
   `canon`/`retired` → report only, except a W27 empty-tag page, where the
   coverage floor applies at every status — Canon-page gate below.
   `TT4: <applied vs reported, by status>`.
5. **Apply** within Owned write scope; `docs/tags.md` changes only after the
   human has seen and confirmed the exact diff (header gate below).
   `TT5: <pages retagged, tags.md lines added or N/A>`.
6. **Lint before done** — re-run the Standard-queries CLI check on every
   page touched; confirm zero new `tag-not-in-taxonomy`/`empty-tags`
   findings. `TT6: <clean, or NOTED>`.
7. **Report** — retags applied (page → tag), `docs/tags.md` additions
   confirmed, unknowns still awaiting the user's call, canon-gated pages
   reported, drops/trims proposed. `TT7: <report given>`.

## Picking tags for a new page

Consulted by the `<type>-prep` skills authoring the page. Read `docs/tags.md`;
pick ≤5 canonical tags, weighted 1–2 Domain + 0–1 Project; no "type" slot;
add one `visibility/*` only if genuinely restricted. Every page carries at
least one Domain tag — no page type is exempt. A page that
reads tone-neutral is under-read, not exempt: derive the tone from what the
page is actually about (a random-encounter table is `combat`, a
derelict-ship table is `maritime` + `salvage`). Never leave `tags: []`
→ instead: name the closest-fit Domain tag from the page's own subject.

## The tags.md header gate

`%%GENERATED-BY-HUMANS — automated pipelines read, never write%%` blocks
*unattended machine* writes, not human-directed ones. This skill, run by a
model with a human confirming in-turn, is not a blind pipeline — but it
still drafts the exact proposed diff and writes only on explicit
confirmation, never silently, never mid-batch. About to append to
`docs/tags.md` without having shown and gotten a yes on the diff → stop, draft,
ask.

## Canon-page gate

**Never edit a `status: canon` or `status: retired` page in this skill to
change which tags it carries — a remap, a drop, a trim. Report the
suggestion instead.** A tag edit is still an edit.

**One exception, and only this one: the coverage floor.** A canon or
retired page carrying no tag at all (W27) is a defect, not a taxonomy
decision — add the closest-fit Domain tag from the page's own subject and
move on. Adding a page's first tag takes nothing away and
overwrites no judgment; changing tags it already carries does both.

| Rationalization | Reality |
|---|---|
| "PJ11 licenses fixing structural rot unprompted" | PJ11 (`docs/guardrails/PROJECT.md`) widens file scope only, never the canon-status STOP gate, and a tag isn't "rot" under its own definition. |
| "It's just a tag, not real prose" | Frontmatter is still page content. Narrowness is not an exemption criterion anywhere in this repo's canon-editing convention. |
| "W13's FIX line already tells me what to do, so I don't need to ask" | The FIX line names the *options* (remap, drop, propose) — it is not authorization to choose one unilaterally. An unknown tag is explicitly "a taxonomy decision" (W13's own text), and a taxonomy decision on a canon page still routes through this gate. W27's coverage floor is the exception above, and is not a taxonomy decision. |
| "Flip `status: canon` to `pending`, edit, flip back" | A status flip is `transcript-ingest`'s/world-update's/canon-review's/PUBLISH's exclusive verb, not a workaround this skill invents for itself. |

**Red flags — stop and report instead:** about to edit a page and haven't
checked its `status:` yet; any thought starting "this is just a tag, so…";
about to remap or drop a 1-page unknown tag because the FIX line already
named the options; about to append to `docs/tags.md` without having shown the
diff and gotten a yes.

## Degrade by asking

- An unknown tag's canonical target isn't obvious → propose the specific
  remap or a drop, then ask — don't pick because the FIX line named valid
  options.
- A W27 page's closest-fit tag is ambiguous between two plausible
  canonical tags → propose both, ask; a single clear fit → apply directly
  (draft/pending) or report (canon).
- An over-cap trim set isn't obvious → propose it, ask.

## Relationship to other skills

- **`npm run lint -- --rules`** — W13/W27's rule and FIX wording; never
  restated here.
- **`vault/refs/runbook-wiki.md` § Tag taxonomy** — the migration doctrine
  (identity/origin tags dropped by design, one worked mapping isn't a
  general rename rule); never restated here.
- **`llm-wiki-lint`** — detects W13/W27 at scale, fixes the mechanical
  alias-remap itself, hands the unknown-tag/empty-tag judgment here, the
  same way it hands W25 to `cross-linker`.
- **`cross-linker` / `canon-review`** — own W26 knowledge-island
  cross-linking; a tag cluster surfaced during an audit is their input,
  never this skill's to link.
- **`<type>-prep` skills** — consult "Picking tags for a new page" when
  authoring.
