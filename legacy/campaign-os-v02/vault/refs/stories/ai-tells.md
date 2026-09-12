---
type: craft
status: canon
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [survival]
summary: "The deduped AI-tell catalog for campaign prose — every pattern grouped by type, with its fix and a fantasy-prose example."
uid: 1f30e577-ceff-49ce-a6bc-c3158c33385e
---

# AI-tell catalog

One deduped catalog of AI writing patterns, grouped by tell type, with
fixes and fantasy-prose examples. Quoted examples in this file are
illustrations of bad writing — never flag or rewrite them.

Credits: pattern research adapted from the humanize-writing skill (based
on Wikipedia's "Signs of AI writing" guide, WikiProject AI Cleanup) and
Conor Bronsdon's avoid-ai-writing skill (MIT).

## Vocabulary

Vale catches every word below on sight (`docs/vale-styles/ai-tells/OverusedVocabulary.yml`,
`OverusedVocabularyVerbs.yml`, `AIAdjectiveNounPairs.yml`, `AICompoundPhrases.yml`)
— its message is generic ("replace with a more specific word"); this table's
job is the per-word fix.

### Tier 1 — replace on sight

| AI word | Instead |
|---|---|
| delve / delve into | look at, dig into |
| tapestry / rich tapestry | (delete — describe the actual complexity) |
| landscape (metaphorical) | field, world — or drop it |
| realm (as filler — "the realm of magic") | area, field. A literal in-fiction realm (a kingdom, a plane) is fine |
| leverage (verb) / utilize | use |
| harness | use, take advantage of |
| navigate (metaphorical) | deal with, handle |
| embark on a journey | set out, start |
| myriad / plethora | many — or give a number |
| testament to | shows, proves — or delete and state the evidence |
| nestled | sits, stands, is built into |
| vibrant / bustling | (name what makes it busy: "dockworkers shout over fish carts") |
| seamless / seamlessly | smooth, easy |
| meticulous(ly) | careful, precise |
| deep dive / unpack | look at, explain |
| ever-evolving / enduring | changing / lasting — or cite how long |
| daunting | hard, dangerous |
| at its core | (delete — just state the thing) |
| in order to | to |
| due to the fact that | because |
| beacon (metaphor) | (rewrite entirely) |
| symphony (metaphor) | (describe the actual coordination) |

Match inflected forms: `delve` covers `delving`, `leverage` covers
`leveraged`, and so on.

### Tier 2 — flag when 2+ cluster in a paragraph

robust, comprehensive, cutting-edge, innovative, pivotal, nuanced,
compelling, transformative, bolster, underscore, fostering, imperative,
intricate, overarching, unprecedented, profound, renowned, stunning,
showcasing, crucial, cornerstone, paramount, poised to, burgeoning,
nascent, quintessential, multifaceted, cultivate, illuminate, elucidate.

Individually fine — a "renowned duelist" in one paragraph is normal
fantasy prose. Three of these in one paragraph is a rewrite signal.

## Synonym cycling — and the proper-noun rule

AI rotates synonyms to dodge repetition: "the ranger... the tracker...
the woodsman... the huntress" for one character in one paragraph. Humans
repeat the clearest word. If the same noun appears three times and it's
the right word, keep all three.

**Proper nouns NEVER rotate — the campaign-specific killer.** A place,
faction, NPC, ship, or item name is the name:

> Bad: "Thassik crept forward. The kobold sniffed the air. The little
> dragon-priest hissed a warning."
>
> Good: "[[Thassik]] crept forward, sniffed the air, hissed a warning."

Wikilink the name on first mention; after that use the name again or a
plain pronoun. An epithet ("the dragon-priest") is only legitimate when
the point of view genuinely doesn't know the name yet — and then the real
name doesn't appear at all. Epithet rotation also breaks the wiki: greps
for the entity miss every epithet mention.

## Significance inflation

Puffing routine content into history: "marking a pivotal moment",
"stands as a testament to", "underscores its importance", "reflects
broader", "setting the stage for", "key turning point", "indelible
mark", "deeply rooted", "watershed moment".

Fix: delete the inflation and state the specific fact.

> Before: "The fall of the lighthouse marked a pivotal moment in the
> port's history, forever altering its destiny."
>
> After: "After the lighthouse fell, three ships wrecked on the shoals
> in one winter, and the harbor guild moved its trade to Saltmere."

Register note: this pass bites DM-facing prose hardest — a prep note has
no business calling anything pivotal. In player-facing prose, drama that
the fiction has *earned* (a god dies on-screen) may keep its weight;
unearned cosmic framing on a tavern description may not. Full register
contract — which bar applies where, both failure directions — is
[register.md](register.md); this section covers only the inflation tell.

## Promotional-brochure prose

Vale flags these on sight (`docs/vale-styles/ai-tells/PromotionalPuffery.yml`).
Tourism-copy defaults: "nestled within the breathtaking foothills", "a
vibrant hub of trade", "boasts a rich history", "natural beauty",
"must-visit", "a thriving community". Replace with plain, specific
description — or, for player-facing flavor, with *concrete* sensory
detail, which is what lush actually means:

> Brochure: "Brindlemark is a vibrant riverside town boasting a rich
> tradition of craftsmanship."
>
> Lush (fine): "Brindlemark smells of pine tar and wet rope; every third
> doorway on the river road is a cooper's or a wainwright's."

## Grammar-level tics

- **Copula avoidance.** "serves as / stands as / represents" → "is";
  "boasts / features / offers" → "has" — when clustering. One "serves
  as" in a formal paragraph is normal; a piece that never uses "is" is
  the tell.
- **Superficial -ing tails.** "...showcasing the town's resilience",
  "...underscoring the threat", "...reflecting the duke's ambition".
  Delete the tail or promote it to its own sentence with real content.
- **Negative parallelism.** "It's not just a sword — it's a legacy."
  Once per piece, at most; includes the split form ("The threat isn't
  the dragon. The real danger is the cult.") and the stacked countdown
  ("It's not the gold. It's not the throne. It's the crown itself.").
  Vale catches most phrasings of this formula mechanically
  (`docs/vale-styles/ai-tells/ContrastiveFormulas.yml`,
  `ContrastiveNegation.yml`).
- **Rule-of-three padding.** "danger, mystery, and intrigue" where the
  third item is a near-synonym. Tricolons are ancient rhetoric — flag
  only when the third leg carries nothing.
- **False ranges.** "From the sewers of the docks to the spires of the
  archmage's tower" when the two aren't a meaningful scale. List the
  actual places.
- **Hyphenated-pair stacking.** "an ancient, long-forgotten,
  ever-watchful guardian" — keep the one modifier that matters.

## Hedging, filler, and fake authority

Vale catches most of this section's phrasings mechanically
(`docs/vale-styles/ai-tells/HedgingPhrases.yml`, `FillerPhrases.yml`,
`SycophancyMarkers.yml`, `VagueAttributions.yml`, `DefensiveHedges.yml`);
this section is what still needs a judgment call.

- **Hedge stacks.** "could potentially", "may eventually", "might
  ultimately" — pick one word.
- **Filler starters.** "It's worth noting that", "It's important to
  note", "Interestingly," "Notably," — delete; state the thing.
- **Hollow intensifiers.** genuinely, truly, "real" as an intensifier
  ("a real threat") — cut, or name the specifics. `very` and `really` are
  the generic line-craft floor, owned by
  `vault/refs/stories/developmental-craft.md` § Words to eliminate.
- **Vague attributions.** "Sages believe", "locals say", "many claim" —
  in campaign prose this is often deliberate in-fiction ambiguity, which
  is fine when it *is* the fact ("locals disagree about what sank the
  Meredine"). The tell is using it to dodge stating what the wiki
  actually knows. Check the page; if the fact exists, state it.
- **Generic closers.** "Only time will tell what fate awaits the
  party." "The future of the realm hangs in the balance." Delete; end
  on a specific draw or just stop.
- **Speculative gap-filling.** Hedged guesses formatted as facts
  ("likely trained in the capital", "is believed to have"). In a wiki
  page every claim traces to canon or is flagged — don't paper gaps
  with plausible filler.
- **Chatbot artifacts.** "I hope this helps!", "Great question!",
  "Let's dive in", reasoning-chain leaks ("Breaking this down...").
  Delete entirely.

## Emotional flatline — show, don't announce

Claiming the emotion instead of conveying it: "What strikes visitors
most", "an awe-inspiring sight", "a terrifying encounter", "the most
interesting feature of the ruin". If the thing is awe-inspiring, the
description has to earn it; the label is filler wearing an emotion
costume.

> Announced: "The cathedral interior is a breathtaking, awe-inspiring
> space."
>
> Shown: "The vault swallows torchlight. Sound comes back wrong —
> a whisper returns as a chord."

This is the central craft rule for read-aloud text: the DM's voice
supplies the emotion; the prose supplies the concrete details that make
it land.

## Structure and rhythm

- **Metronomic sentences.** Every sentence 15–25 words is robotic. Mix
  3–8-word punches with longer builds. Fragments work. "The door held."
  This is the generic floor — [prose-aesthetic.md](prose-aesthetic.md) §
  Prose style sets this GM's specific default (long, comma-linked,
  cumulative sentences as the default carrier of intensity); that stronger
  claim governs, this rule only catches uniform robotic rhythm. Vale
  backstops the worst case (`docs/vale-styles/ai-tells/StaccatoBurst.yml`,
  `ParallelStaccato.yml`).
- **Uniform paragraphs.** Vary deliberately — a one-sentence paragraph
  lands a beat.
- **Em-dash discipline.** More than one per 3–4 paragraphs is above
  human baseline; even one is a tell when it injects a dramatic
  explanatory aside mid-sentence. Count before flagging. Fix with
  commas, periods, or restructuring. Applies to both registers — lush
  prose earns long sentences, not dash-splices. Vale flags every em-dash
  unconditionally (`docs/vale-styles/ai-tells/EmDashUsage.yml`); this
  frequency-and-register judgment is what a human pass still has to make.
- **Boldface and inline-header lists.** Strip mechanical bold; a bullet
  list where every item is "**Label:** sentence" usually wants to be
  prose — except in DM-facing run-guide material, where scannable
  labeled lists are the correct form.
- **Bare-noun-phrase bullet stacks.** 5+ same-shape verb-less bullets
  read as a marketing one-pager; vary the items or write claims.
- **Formulaic sections.** Every section ending in a takeaway bow;
  "Despite challenges... continues to thrive" loops. Vary endings; name
  the actual challenge and response or cut. Vale catches the
  despite-formula phrasing (`docs/vale-styles/ai-tells/DespiteChallenges.yml`).
- **Transition crutches.** Moreover / Furthermore / Additionally / In
  conclusion / When it comes to → use the real connector ("because",
  "but", "so") or none; paragraph breaks transition fine on their own.
  Vale catches the word list (`docs/vale-styles/ai-tells/FormalTransitions.yml`).

## Pattern stacking and when to rewrite

Multiple weak signals converging on one phrase (bold + scare quotes +
em-dash aside) = one strong finding, not three. And when a draft has 5+
vocabulary hits across categories plus uniform rhythm, patching phrases
won't save it — the structure itself is generated. Say so and rebuild
from the draft's core point instead of sanding each sentence.
