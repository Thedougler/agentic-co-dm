# Shell-safety notes for this skill's queries

**Cross-day idempotency `find`** (zsh-safe): `find`'s own recursion off a literal
`vault/campaigns/shattered-sea/episodes` root, not a bare `vault/episodes/*/` shell glob — the same class of bug the
standard queries' `--include` below catches: an unquoted glob with zero matches
aborts the whole command before `find` ever runs.

**Standard queries' `grep --include`** (recursive, quoted — `--include="*.md"` — so
zsh doesn't glob-expand it before grep runs): an unquoted `--include=*.md` aborts with
`zsh: no matches found` in any repo where `*.md` doesn't literally match a file in the
cwd. Not a bare `vault/campaigns/shattered-sea/factions/*.md` glob either — empty output is informative: no
Fronts exist yet, nothing to advance, say so and stop. `-A20` because `.claude/skills/draft-content/references/faction.md`'s
Front template runs to ~15-20 lines per front — a shorter window risks truncating
`**Consequence at fill:**` or `**Quest link:**` out of the paste.
