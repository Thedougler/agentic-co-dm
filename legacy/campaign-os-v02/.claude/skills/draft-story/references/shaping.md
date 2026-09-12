# Shaping — growing a fixed pile into prose, block by block

Reached from [SKILL.md](../SKILL.md)'s Entry points, for material headed to a
single destination page that never needed a chapter — a handout, a lore page
body, a staged recap draft. The pile is fixed (session notes, a fragments
file, a reviewed ledger, a bullet outline) and read-only; the finished prose
lands somewhere else.

## The loop

1. **Read the pile in full.** Whatever the format, form a sense of what is in
   it before proposing anything.
2. **Settle the reader with the GM.** Who reads this (players on the site? the
   DM at the table? a handout in someone's hand?) and what they know walking
   in — the concepts grounded from the start. Everything else must be
   introduced by a block before a later block can lean on it.
3. **Draft 2-3 candidate openings.** Each implies a different thesis or angle.
   Show all of them; the GM picks one or composes a hybrid. The chosen opening
   defines what the rest of the piece must do.
4. **Check `vault/ideas/lines.md`** for a
   reserved line a block could land naturally — never force one; mark a placed
   line per that file's convention.
5. **Grow block by block.** After the opening lands, ask "given this opening,
   what does the reader need next?" and pull material from the pile to answer.
   Weigh the format of each block out loud (§ Format choices). Write each
   agreed block immediately — don't batch — so the GM watches the piece take
   shape.
6. **Loop step 5 until the GM calls it done.** The GM decides, not you.

## Grounding

Every concept must be grounded before a block leans on it: the reader either
walked in knowing it (settled in step 2) or met it in an earlier block. The
unit is the concept, not the word — a block can lean on an idea the reader
lacks with no jargon in sight. Keep a running list of what's grounded; when
the next move needs an ungrounded concept, grounding it *is* the next move.
The lever to settle with the GM: demand too much up front and you shut readers
out; introduce too much inside and the opening drowns in definitions.

## Format choices — argue them out loud

Pairs with `obsidian-markdown` conventions; callout container rules belong to
`callouts` — load it before writing any `> [!` block.

- **Prose vs. list.** Prose carries argument; lists carry parallel items.
  Items not truly parallel -> prose.
- **Inline vs. callout.** Only if the aside would genuinely derail the main
  thread inline — and the callout type must come from the `callouts` taxonomy.
- **Table vs. repeated structure.** Same shape 3+ times with the same fields
  -> table. Otherwise prose with bold leads.
- **Quote vs. paraphrase.** Quote when the wording is the point (and cite the
  source per its rules); paraphrase when only the idea matters.

## Collaborative moves

Offer these as choices at natural pauses — the GM steers:

- "What does this paragraph add that the previous one didn't? Keep or fold?"
- "If we cut this, what breaks? If nothing, want to cut it?"
- "This could be prose or a list — I'd lean list because the items are
  parallel. Your call."
- "The opening promised X and we've drifted to Y — re-thread the body, or
  change the opening?"
- The pile lacks something the piece needs -> name the gap: "We need an example
  here and the pile doesn't have one — give me one, or we cut the section."

Treat the pile as a quarry, not a script: split a fragment across blocks,
merge two, paraphrase freely — the piece reads as one voice.

## Rules

1. **The raw material file is read-only.** Never edit it, never "tidy" it.
2. **Blocks lean only on grounded concepts** — reader-known or introduced
   earlier. No exceptions for "they'll get it later."
3. **Campaign facts come from the wiki, cited by wikilink** — never restated
   from memory, never invented to fill a gap in the pile. Pending content
   never appears in anything player-facing.
4. **Re-read the working file from disk before every write** — the GM may have
   edited between turns; never overwrite blindly. Rewrite requests edit that
   block in place, leaving the rest alone.

## Where the prose lands

Typed wiki pages land via the owning guide — `vault/refs/vault/<type>/GUIDE.md`
or the matching `<type>-prep` skill, routed by `draft-content` — at
`status: pending`; when shaping a section of such a page, write only within the
section that guide designates. Free-standing work (a handout draft, a recap
draft staged for `recap-writer`, prose with no home yet) stages in
`vault/ideas/`. No destination named -> ask once,
remember the answer.

Ordering a pile is [beats.md](beats.md)'s job, not this file's — shaping only
renders an already-fixed order into prose.
