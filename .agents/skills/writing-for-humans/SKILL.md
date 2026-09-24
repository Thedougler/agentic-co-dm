---
name: writing-for-humans
description: >-
  Write and edit every DM-facing text: session-beat pages, session plans,
  run-guide cockpit copy (pass 2), wiki owner pages (At a Glance, At the Table,
  facts, secrets), recaps' DM sections, and reports or proposals to the DM in
  chat. Produces plain, complete, scannable sentences a DM can use mid-session
  in seconds. Reader `DM` or unknown → writing-for-humans. Spoken player text
  belongs to theatre-of-the-mind; agent instructions belong to
  writing-for-agents.
---

# Writing for humans

You write for a DM who is running a game. They glance at the page between
players' turns, with four people waiting. Every line must give them what they
need in seconds: who, what, where, how much, and what happens if. The best DM
copy reads like a clear note from a sharp co-DM, never like an encyclopedia,
a novel, or a shorthand list.

This skill decides **how** DM-facing text reads. What a session beat must
contain is set by `docs/agents/table-ready.md` and the beat's type skill; the
numbers come from `dnd5e-mechanics`; formatting comes from `obsidian-markdown`.
File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named page or section to write or edit, its template, the owner
  pages its facts come from, and the reader (the DM, unless stated).
- **Work:** Write or rewrite only the DM-facing prose in scope, following the
  steps below. Keep the page's structure, links, and facts.
- **Done:** Every in-scope line passes the final check at the bottom of this
  file.
- **Capability Handoff:** Return the edited page or text to its parent (the
  beat skill, run-guide pass 2, the owner skill, or chat). Missing facts go
  back to the owner skill or the DM as a named gap.

## Steps

### 1. Name the surface and the DM's question

Find the surface you are writing in the table below. Its question is what the
DM wants answered when their eyes land there. Every line you write answers it.

| Surface | The DM's question |
|---|---|
| Beat page header lines (Card, Trigger, Stakes, Ends when…) | What is this beat and what do I need to know before it starts? |
| Situation, Cast, Space, Opposition | Who and what is here, what do they want, where are they? |
| Rulings, checks, pressure, outcome tables | A player just did X. What happens? |
| Carry forward / Handoff | What is true now, and where does play go next? |
| Session plan | What happens tonight, in what order, and what is the opposition doing? |
| Run-guide cockpit (pass 2) | What do I do and say right now? |
| Owner page: At a Glance | What is this and why does it matter right now? |
| Owner page: At the Table | How do I run it when the party meets it? |
| Owner page: facts, Drive, Secrets | What is true, including what the players do not know? |
| Chat report or proposal | What happened, what changed where, and what do you need from me? |

Recipes for each surface: [references/surfaces.md](references/surfaces.md).
Read the one for your surface.

### 2. Gather the facts

Read the target page end to end, its template, and the owner pages its facts
come from. On a run-guide cockpit, also read the previous beat and the
session plan. Write down the facts the page needs: names, numbers, wants,
positions, triggers, consequences. Every fact comes from a source. A missing
fact goes to the owner skill for that page or back to the DM as a named gap;
a missing number goes to `dnd5e-mechanics`.

Done when every fact you will write has a source.

### 3. Draft

Write each line to answer the surface's question, using the rules below.
Lead with the point, name everything, and put conditionals in tables. Read
[references/examples.md](references/examples.md) for the weak → strong pair
closest to your job, and match its quality, never its words.

### 4. Cut

Take each line out in your head. If no choice, ruling, risk, resource, route,
clock, NPC response, or spoken picture changes, cut the line. Then remove
everything in the cut table below.

### 5. Cold read

Read the page as a DM who has never seen it, mid-session, with players
waiting. Find the answer to the surface's question. Name the three places you
slowed down, hunted, or had to guess, and fix each one.

Done when the answer to each surface's question is findable in about five
seconds for a glance section and about thirty seconds anywhere else.

### 6. File

Format with `obsidian-markdown` (check and DC notation, wikilinks, tables,
callouts). Report what changed and where, plus any gaps.

## Rules

1. **Lead with the point.** The first words of a line or section answer the
   reader's question. "The smuggler wants the ledger and will not trade blows
   with four people" beats a paragraph that arrives there at the end.
2. **Name it.** Proper names with wikilinks, exact numbers, exact places.
   "[[mara-quill|Mara]] is 5 feet from the ledger," never "the thief is
   nearby." Every pronoun has an obvious owner.
3. **Short, complete sentences.** A subject and a verb, one idea each, about
   8–20 words. A sentence that needs "and" three times is two sentences.
   Fragments, slash-stacks, and chains of arrows with no subject are notes to
   yourself, not copy.
4. **Scannable shape.** A bold label at the start of a line names what the DM
   scans for (**Trigger.**, **If they flee.**). Parallel items go in a list.
   If-then goes in a table. Nothing a DM needs mid-play hides inside a
   paragraph.
5. **Say what the world does.** "If the party surrounds her, Mara cuts the
   lantern rope and swings onto the barge." State outcomes and
   responses; the DM runs the table (see `docs/agents/table-ready.md`
   § World voice).
6. **Plain truth for the DM.** State secrets, motives, and answers outright:
   "Oren lies about the second grave; he buried his brother there." The DM
   layer hides nothing (AGENTS.md **HARD: dm-facing-explicit**).
7. **This one, not the category.** Write the fact that makes this person,
   place, or thing different: "Barnacles grow up the dock posts past the
   high-water mark," not "a coastal trading town."
8. **Kitchen-table words.** Common words a tired DM reads instantly. A
   campaign label gets its plain meaning the first time it appears on a page.
9. **Each fact once.** One fact lives in the one section where the DM needs
   it. Other sections link or refer to it.
10. **Numbers where they are used.** DCs, damage, distances in feet, counts,
    and times sit in the line where the DM rolls or rules, formatted per
    `obsidian-markdown`.

## Cut table

| Cut | Why |
|---|---|
| Default conditions (fair weather, drinkable water, safe road) | Nothing changes. State them only when unsafe, scarce, costly, magical, or a clue. |
| Category descriptions ("a coastal trading settlement") | Fits any place. Replace with this place's specific fact. |
| Mood with no consequence ("a sense of unease") | Changes no ruling. Replace with the fact that causes it, or cut. |
| Lines about the DM's conduct instead of the world | Replace with what the world does in that case. |
| Hedges ("perhaps", "might want to", "consider") | State the fact or the ruling. |
| Design diary, balance commentary, rules comparisons, agent-process notes | Not playable. Keep it off the page. |
| The same fact in Glance, Situation, and narration | Keep it in the one place the DM uses it. |
| AI tells ("tapestry of", "nestled", "it's worth noting", "delve", "the air is thick with") | Say the thing plainly. |
| Placeholders ("TBD", "ingest pending", empty sections) | Fill from the sources, or with a marked canon proposal (`docs/agents/table-ready.md` § Fill the silence). |

## Hard lines

1. **Facts from sources.** Rewriting for clarity never adds facts,
   mechanics, DCs, or procedures. The owner pages, the template, the user, and
   `dnd5e-mechanics` are where facts and numbers come from.
2. **Keep the plumbing.** Frontmatter, wikilink targets, embeds, headings the
   template requires, and file names stay as they are unless one is verifiably
   broken.
3. **Spoken text is not yours.** `[!narration]` blocks and `_italic_`
   narration cells belong to `theatre-of-the-mind`. On run-guide pass 2 they
   stay empty.
4. **Complete sentences on every wiki page.** Bold labels, tables, and the
   check notation are fine when each cell still reads as a clear statement.
5. **Clarity beats style requests.** "Make it more dramatic" means sharper,
   more specific facts, never ornament.
6. **Leave touched sections better.** Bad copy inside the sections you are
   editing gets rewritten, even if it was already there. Sections outside the
   request stay as they are.

## Final check

Fail and fix if any answer is no.

- [ ] Does every section answer its surface's question, with the answer first?
- [ ] Is every person, place, and item named and linked, and every number
      exact?
- [ ] Is every line a complete sentence (or a clear table cell or labeled
      item), mostly under 20 words?
- [ ] Is every if-then in a table or labeled line, and every secret stated
      plainly?
- [ ] Does every line pass the removal test, with each fact said once?
- [ ] Is nothing from the cut table left?
- [ ] Are hard lines 1–6 intact?
- [ ] On the cold read, is each answer findable in seconds?
