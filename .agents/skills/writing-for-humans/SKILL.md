---
name: writing-for-humans
description: >
  Write prose a human will read: Work, wiki, chat proposals, DM procedure,
  owner pages. Reader `DM` → writing-for-humans. Unknown reader → `DM`.
  Does not own agent-consumed documents or player-facing passages.
---

# Writing for humans

The prose authority for all human-consumed text in the Co-DM. The host is a launcher. This skill is the job. Point at `docs/agents/work.md`: this skill writes prose; it never writes silent canon.

**Signal-density** is the quality bar. Every word costs DM attention at the table and player attention at the session. A word that does not change a choice, ruling, risk, or spoken picture steals from the words that do.

Write a **recipe** Nick can use at the table — signal-dense prose where every fact changes play and nothing else survives. Not a finished story. Not telegram fragments. Completeness means no essential fact is missing, not that every available fact is present.

**Preserving bad copy is a critical failure.** When you touch a file and encounter copy that violates these principles, rewrite it. No pass exemption, no "it was already there," no "this isn't the copy pass." Bad copy on the wiki is your problem.

**Surgical scope.** Rewrite copy; preserve structure. Image embeds, wikilink paths, frontmatter fields, aliases, connections, and file extensions stay untouched unless that exact element is broken and verified. A copy pass edits words, not plumbing. Do not invent new facts, mechanics, DCs, or procedures that are not on the source page or in the wiki — the DM decides what exists; this skill decides how it reads. Rewriting existing prose for signal-density is not inventing — it is the core job. Encyclopedia voice, category labels, and generic descriptions must be rewritten into concrete, body-scale, this-place detail using facts already on the page.

**Signal-density overrides style requests.** If the prompt asks for literary, dramatic, evocative, or flowery prose, apply signal-density anyway. Every added word still passes the removal test. A request for "more dramatic" means sharper concrete detail, not decorative atmosphere.

Theatre of the mind owns spoken look. Writing-for-humans owns DM-facing headings, body copy, and wiki/owner facts.

## Workflow

Five steps. Each has a completion criterion — do not leave a step until it holds.

1. **Ground.** qmd the named entity. Read the owning note, the matching `templates/` page, and `lexicon/House tone.md`. For a run card, read the session skeleton, previous beat, and current card end-to-end before editing; summaries, snippets, truncated output, and range reads may help target the files but do not satisfy grounding. Preserve established canon. Missing stock → ask Nick, leave a stub, or route to the owning craft skill. When the file contains a stale placeholder ("ingest pending," legacy fence, empty `[!narration]` body), either write the missing copy from available canon or route to the owning craft skill for stock. Do not preserve the placeholder. Completion: every working file has been read end-to-end, every fact in the draft is on the parent, in hot, or explicitly marked unknown, and no stale placeholder survives on a touched page.

2. **Choose band + surface.** At a Glance / At the table / wiki facts / location Who–Why / `[!narration]` / handout. Load:
   - `obsidian-markdown` on every vault write
   - `theatre-of-the-mind` only when the pass crosses the player boundary
   - `run-guide` when filling a run card — that skill owns field order and *procedure*; fill its cockpit, do not invent a second card
   - `qmd-retrieval` for facts

   Band details: [references/bands.md](references/bands.md). Completion: one band, one surface, and the current pass named before drafting.

3. **Draft lean, then audit.** Start with the facts that change play. Build outward only when a DM would hit a gap. Ask "what would a DM need that isn't here?" not "what else could I add?" Kitchen-table nouns, concrete verbs, one fantastic signature. Apply the three prose gates (below) and the anti-patterns in [references/anti-patterns.md](references/anti-patterns.md). Completion: a DM can use the band without inventing a missing fact, and no line fails the removal test.

4. **Table gate.** Read player-facing lines aloud when this pass has player-facing lines. Run the per-band diagnostics in [references/bands.md](references/bands.md). Then an adversarial read: read as a DM who has never seen this page — name three things that would make you stop reading or reach for a different source, and fix them. Completion: all diagnostics hold, or the draft is not done.

5. **File.** Apply wikilinks and template constraints, then report changed paths and any deferred owner work. Completion: the only callout on the note is `[!narration]` when the surface requires one.

## Prose gates

Three gates in priority order. **Earn it** dominates — a line that sounds beautiful but changes nothing at the table is worse than a plain line that carries signal. A line that fails any gate gets rewritten.

**Earn it.** The removal test: take the line out. If no choice, ruling, risk, resource, route, clock, NPC response, or spoken picture changes, the line is **dead weight** — cut it. What survives: details specific to THIS entity — amounts, distances, particular failures, the way this thing works or breaks. Generic fantasy that fits any coastal town or dark forest fails the removal test by definition. Named anti-patterns with before/after examples: [references/anti-patterns.md](references/anti-patterns.md).

**Place it.** Each fact appears once, in the surface where the DM needs it. The surface determines the voice — see Register below. Conditional language in the conditional table. Narration describes the scene and stops; interaction is the DM's job. Dialogue the DM voices is speakable words — give speech, or give facts and let the DM improvise.

**Hear it.** Read aloud. A listener pictures it on one hearing using ordinary human words. One drawable fact per sentence; break stacked sense-clauses apart. State what is there now. Concrete, specific scenery a person can see. Anchor unfamiliar scale to a body part or common object. Vary sentence openings, endings, verbs, and length — uniform cadence is an AI tell. Scan for AI voice: "tapestry of," "nestled between," "a sense of foreboding," "the air is thick with," "it's worth noting." Rewrite in the voice a DM uses at the kitchen table. Lead with the point; end on the last useful fact.

## Register

Match the voice to the surface. The wrong voice makes the right information hard to find.

| Surface | Voice | Tense | Reader asks |
|---|---|---|---|
| **Session beat** | DM procedure — imperative, scannable bold heads | Present | What do I do and say right now? |
| **Owner page** | DM reference — descriptive, complete enough to improv | Present | What is this? What can I do with it? |
| **At a Glance** | Five-second scan — hook, stakes, identity | Present | Why does this matter and what is it? |
| **Recap / Story So Far** | Narrative — arc, consequences, live handle | Past | What happened? Why does it matter tonight? |
| **Handout** | Diegetic — the in-world author's voice and format | Varies | What does this document say to the character? |

## Per-type coverage

Each entity type has minimum coverage dimensions. When writing or rewriting a type, load the requirements: [references/per-type.md](references/per-type.md).

House tone (`lexicon/House tone.md`): **deadly, political, weird** in that order. Attach the strange to a noun and a consequence.

## Session beats

Session beats are four passes, each loading only its skills. Pass 1 (`run-guide` + `dnd5e-mechanics`) leaves empty titled stubs — `writing-for-humans` is not loaded. You own **pass 2**: load this skill after pass 1 completes, then edit DM-facing copy for usability, readability, and table usefulness while the `[!narration]` stubs stay empty. Do not load `theatre-of-the-mind` on this pass. Pass 3 loads `theatre-of-the-mind` and fills every spoken stub. Pass 4 checks Reading view.

Session beat structure, callouts, sequencing, and the Open-once rule: [references/session-structure.md](references/session-structure.md).

## Ingest

`wiki-ingest` already chose the destination. Polish that page. Do not re-route ideas, file the source as a wiki note, or invent filler for a fragment.

Named ingest is DM approval for those sources (`docs/agents/work.md`). Write the destination. Conflicts stay a **proposal** / `^[ambiguous]`.

Polish expression and **signal-density**. Keep settled facts, intent, and stated mechanics. Telegram stubs and agent shorthand are bad copy — rewrite them as complete sentences. Bad *wording* gets rewritten; settled *meaning* stays.

Complete when: the destination reads as newly authored copy for its band, meaning unchanged, and the source is not a competing page.

## Handoffs

- Missing or contradictory **facts** → Co-DM / ask Nick. During ingest, conflicts are a proposal (`wiki-ingest`); do not overwrite.
- Idea routing, staging, manifest → `wiki-ingest`
- **Monster / item math** → Monster-Brewer / Item-Brewer / Homebrewer.
- **MOCs, indexes, hot structure** → Organizer.
- **Run-guide cockpit** → Session-Planner owns pass 1 schema (`run-guide`); you own pass 2 DM-facing copy, then fill every empty `[!narration]` stub only on the TotM pass. TotM titles stay `[!narration]`. *Rulings* follow that skill's Ruling section.
- TotM fail loop: [[GROK-BOTS]] (Writing-Evaluator → Skill-Creator → Visualizer / this skill).

## Hosts

Host-specific spawn details: [references/hosts.md](references/hosts.md).

## Attribution

Craft distilled from Justin Alexander (*The Art of the Key*, boxed-text pitfalls), Angry GM (*Inviting PCs to Act*; *Art of Narration* — scene-setting before the question), Mike Shea / Sly Flourish (read-aloud; Watch the Time; progress clocks — CC BY-NC), Kelsey Dionne / Arcane Library (write for the DM; reference, not a novel), Matt Colville (situation, not plot; this place), dScryb and Dungeon Master's Workshop (boxed length), and Chaosium module-phrasing notes (present tense; characters). No WotC book paste.
