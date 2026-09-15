---
name: writing-for-humans
description: >
  Write text a human will read: documentation, explanations, READMEs,
  tutorials, proposals, reports. Reader `human` → writing-for-humans.
  Stacks with copy-writer (DM) and theatre-of-the-mind (players) when
  those specialized authorities also match. Does not own agent-consumed
  documents.
---

Reference for writing any document a human reads. The counterpart to `writing-for-agents`: that skill tunes for agent execution; this one tunes for human comprehension. When a specialized human-reader authority also matches (`copy-writer` for DM prose, `theatre-of-the-mind` for player-facing narration), both apply — this skill carries the universal craft; the specialist carries the domain.

## Scanning

Humans scan before they read. Most never read at all — they extract what they need and leave. Structure for the scanner first, the reader second.

- **Front-load the point.** First sentence of a section carries the conclusion or the action. Detail follows. A reader who stops after one sentence still got the message.
- **Headings are sentences the scanner reads.** A heading that names a topic ("Configuration") is weaker than one that states the point ("Configure the database before first run"). The scanner reads headings, skips bodies, and still understands.
- **Lists over paragraphs** when items are peers. A paragraph buries peer items in connective tissue the reader must parse to find each one. A list exposes them directly.
- **One idea per paragraph.** A paragraph that covers two ideas forces the reader to hold both while finding the boundary. Split at the boundary.

## Lead with the answer

The reader arrived with a question. Answer it before explaining it. Inverted pyramid: conclusion, then evidence, then background. A reader who leaves early still got the most important thing.

This applies at every scale: the document leads with its point, each section leads with its point, each paragraph leads with its point. Burying the answer after the reasoning asks the reader to hold a stack of context they don't yet know the shape of.

## Concrete language

Abstract language asks the reader to do the grounding work. Concrete language does it for them.

- **Specifics over generalities.** "The retry fires after 500ms" over "the system retries after a short delay." The specific teaches; the general gestures.
- **Examples over definitions.** A definition states the boundary; an example lands inside it. When both are present, the example does more work. Lead with the example when the concept is unfamiliar; the definition clicks after the reader has a mental picture.
- **Name the thing.** Pronouns and vague references ("this", "it", "the above") force the reader to resolve the antecedent. In technical prose, re-state the noun. Repetition is cheaper than ambiguity.

## Sentence economy

Every word earns its place — but earning it means serving the reader, not minimising the character count. Agent prose can be telegraphic because the agent processes all tokens uniformly. Human prose needs rhythm: a sentence that is technically minimal but hard to parse on first read has failed.

- **Active voice** unless passive is genuinely clearer. "The server rejects the request" over "the request is rejected by the server." Active voice names the actor first, which is usually what the reader needs.
- **Short sentences for complex ideas.** Long sentences for simple ones. Match sentence length to cognitive load: when the idea is hard, the syntax should be easy.
- **Cut weasel words.** "Somewhat", "relatively", "fairly", "quite" — each one softens a claim without adding information. Either the claim is true or it needs qualification; a weasel word does neither.
- **Cut meta-commentary.** "It's worth noting that", "it should be mentioned that", "as we discussed above" — preamble that announces the content instead of delivering it. Delete and start with the content.

## Context before detail

Orient the reader before diving in. A detail without context is noise; the same detail after context is signal.

- **State the problem before the solution.** The reader who doesn't know the problem can't evaluate the solution. One sentence of problem is usually enough.
- **State the goal before the steps.** A procedure without a stated goal leaves the reader following instructions they can't debug, because they don't know what success looks like.
- **Name the audience.** When a document serves multiple readers (ops, devs, end users), say who each section is for. A reader who knows a section isn't for them can skip it; a reader who can't tell reads everything and retains less.

## Progressive disclosure

Human progressive disclosure is not the agent kind (pushing reference behind pointers). Here it means: let the reader choose their depth.

- **Summary first, detail on demand.** A one-paragraph overview before a ten-section deep-dive lets the reader who needs the gist stop early, and the reader who needs depth orient before diving.
- **Layer by expertise.** Put the common case first. Advanced options, edge cases, and caveats come after the main path works. A beginner who hits a caveat before the happy path is lost; an expert who hits the happy path first skips to the caveat they need.
- **Link, don't inline.** When supporting material exists elsewhere, a link to it costs one line. Inlining it costs every reader who doesn't need it. Inline only when the material is essential to the current argument and a link would break the reader's flow.

## Honesty over polish

Precise language the reader can act on. No inflated claims, no false simplicity.

- **Say what you don't know.** "This has not been tested under load" is more useful than silence. The reader who discovers the gap themselves trusts nothing else you wrote.
- **Say what's hard.** "This migration requires downtime" is kinder than "follow these simple steps" when step 4 takes the database offline. Surprises erode trust; warnings build it.
- **Prefer the plain word.** "Use" over "utilize", "start" over "initialize", "show" over "surface." The plain word is faster to read and harder to misunderstand. Technical terms earn their jargon — non-technical terms do not.
