# Hard rules — what a story may and may not contain

Reached from [SKILL.md](../SKILL.md)'s `DS5`. These bind the chapter itself;
the rails in SKILL.md bind every step.

## Owned path and standing header

Session stories write to **`vault/episodes/NNN/session-NN-<slug>.md`**
(colocated with the episode's run guide and beats). Other scopes write to
**`vault/stories/<scope>-<slug>.md`** — `quest-<slug>.md`,
`season-NN-<slug>.md`, `arc-<slug>.md`, `campaign-<slug>.md`, or
`session-NN-scene-N-<slug>.md` (a cold open scene's own short story, reached
from `writing-cold-opens`, mirroring that scene's `scene-<N>-<slug>.md`
numbering). A cold-open scope has
one difference from every other: second person, present tense, "you" not
"they," since the reader is borrowing a temporary NPC perspective. That
perspective may be one NPC or one NPC group and may be friendly, allied,
neutral, hostile, unknown, or mixed; keep the frame a side story apart from the
main PC plot.

Every story carries frontmatter with three required keys — `type: story`,
`created:`, and `updated:` — copied from `vault/_templates/_stories/_story.md`. Any
further key is optional, including the `owner_skill:` the template carries
through. Below the frontmatter, the header is exactly:

```markdown
# <Title>

*Draft fiction, not canon. Canon lives on the wiki. Derived pages: (none yet).*
```

The deriving guide later replaces `(none yet)` with the wikilinks of every
page derived from the story, in the same pass it writes them.

Stories are kept permanently — the shelf is a growing book, never pruned,
never moved to `raw/`. Session stories write to `vault/episodes/NNN/`;
non-session stories write to `vault/stories/`. Neither scope writes to
`vault/campaigns/shattered-sea/pcs/` or other vault subtrees.

## The rules

1. **A story is prose only.** Scene breaks via `---` and `[[wikilinks]]` are
   allowed, never required. Everything that belongs to a wiki page is banned
   in a story — no callouts (`> [!`), no DCs or checks, no stat references,
   no template headings, no `## DM Only` split -> instead: say it in the
   fiction (the mechanic returns at derivation, on the derived page).
2. **DM-side artifact.** Secrets, villain interiority, and unrevealed truths
   are welcome in the prose — the shelf is unpublishable by construction and
   the site build never scans it.
3. **The story is source material, not a script.** Derived scenes and events
   still obey the sandbox rails — player roles, if-ignored consequences, no
   choice-dependent events (`.claude/skills/composing-beats/references/audits.md`). The
   story supplies the fiction those rails get applied to.
4. **Derivation never starts mid-draft.** The story reaches `DS8` PASS and
   `DS9` sign-off before any template is instantiated from it.

## The chapter, not a summary

This file is the one place in the repo where the wiki's structural contract
is deliberately absent. A timid, summary-shaped "story" that reads like a run
guide with the headings filed off fails these rules exactly as a callout
would — it has smuggled the page shape back in without the syntax.

Write the chapter you would want to read. About to draft the chapter →
`writing-style` apply.
