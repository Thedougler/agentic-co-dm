# Fragments — capturing raw material before any shape exists

Reached from [SKILL.md](../SKILL.md)'s Entry points, and from
`colab-on-idea`'s `CO7` for the GM-approved capture format. Pure **explore**:
widen the space of what the material could be without committing to structure.
Fragments are noticings; the novelist's diary is the model — unstructured raw
material mined later.

## Register

Collaborative co-writer, not interviewer. Curious, generative, yes-and: "what
if she already knows?", "there's something in that image — what does the harbor
smell like that night?", offers and riffs alongside the GM's, never challenges
or cross-examination. Contribute your own fragments too — both sides of the
conversation are mineable. Capture from the very first thing the GM says,
including the initial prompt.

## What is a fragment

Any piece of text that might survive into the final prose — readable by the GM,
not necessarily by a cold reader. The bar is "is this a piece of good
material?", not "is this self-contained?" Deliberately heterogeneous:

- A sharp sentence to deploy somewhere, destination unknown.
- A vignette: a scene image, a moment at the table, a scenario, an analogy.
- A half-thought: "something about how the cult mirrors the guild — later."
- An NPC line, a player quote, an overheard voice worth keeping.
- A cluster of related observations that hang together by feel.
- A **leading word** — a compact coinage the piece hangs on (a session's
  throughline, a villain's motif, the one term that names the arc). The most
  valuable fragment to land: it shapes structure, transitions, and title later.
  When the conversation circles a recurring idea, offer coinages until one
  sticks.

## File format

One file per topic under `vault/ideas/`,
kebab-case (`vault/ideas/<topic>.md`). No matching
topic file -> start one by copying `vault/_templates/_ideas/_idea.md`, never
retyped (`type: idea`, `created:`, and `updated:` are required; any
further key, `owner_skill:` included, is optional);
ambiguous which topic -> ask once, then remember for the session. On first
write: the template's three required frontmatter keys and a single H1 working
title (it can change later), nothing else — no TOC, no date line in the body.
Then:

```markdown
# Working title

A first fragment. Multiple paragraphs, lists, quotes — whatever shape it
naturally takes.

---

A second fragment.
```

Fragments separated by `---`. No headings inside the body, no tags, no order
beyond arrival order.

One special file: a fragment that is a **placeable line** — a sentence or NPC
quote to deploy verbatim someday, destination unknown — banks in
`vault/ideas/lines.md` (the reserved-lines file,
grouped by speaker or theme with a context note) instead of a topic file.

## Writing rhythm

Append silently — no permission per fragment, a passing "banking that" at most;
never interrupt the flow with save dialogs. Before **every** write: re-read the
file from disk. The GM may have edited, reordered, or deleted fragments between
turns; their edits are sacrosanct — preserve them, never overwrite, only append
(or edit a specific fragment in place when asked). "Cut the last one",
"sharper", "merge those two" are first-class instructions.

## Rules

1. **No structure.** No outlines, phases, orderings, or headings — this stage
   refuses to organize, even when asked mid-flow -> instead: name the next step
   ([beats.md](beats.md) to order it, `DS1` to write it) and keep capturing;
   never switch modes silently.
2. **Append-only, re-read first.** Every write re-reads the file from disk; GM
   edits are never clobbered.
3. **Campaign facts come from the wiki, not memory.** Needing a fact
   mid-capture (an NPC's status, what a session established) -> the
   `llm-wiki-query` skill's tiered method; cite the hit, don't restate it.
4. **Fragments never become wiki pages directly.** No writes to `vault/` — a
   firmed entity routes through `draft-content` to its owning guide.

## Owned paths

Writes only `vault/ideas/*.md` — one file per
topic, kebab-case, the flat format above; never a governed `vault/` page.
`vault/ideas/writers-room/<date>-<slug>/` is staging
owned by `campaign-writers-room` — never write there.

## Degrade by asking

- Can't tell which topic file a fragment belongs to -> ask once ("this feels
  like varkell-endgame — bank it there?"), remember the answer.
- A fragment asserts a campaign fact you can't confirm via `llm-wiki-query` ->
  bank it anyway, verbatim, in the GM's phrasing — fragments are ideas, not
  canon — but say the wiki doesn't corroborate it.
