# Quickstart: Audience Writing and Visual Skills

Prove the feature by classifying jobs and checking pointers. Do not rewrite `legacy/` to “fix” them.

## Prerequisites

- Branch `010-audience-writing-skills`
- Spec [spec.md](./spec.md), contract [contracts/writing-authorities.md](./contracts/writing-authorities.md)
- `AGENTS.md` contains the six-row stack table and says they stack
- The six skill descriptions match their contract branches (or were already matching)

## 1. Classify the contract jobs (P1, SC-001)

Cover the 16 jobs in the contract. A second reviewer names authorities without seeing the first list.

Expected: 100% agreement. Fail if a job is missing an authority or given one that does not match.

## 2. Agent vs DM vs players (P2–P4)

- Agent-only job (skill or standing instruction): writing-for-agents only. Fail if scored as wiki copy or theatre of the mind.
- DM-only chat Work, not filed: copy-writer only. Fail if vault format is required. Fail if telegraphic agent-speak is treated as done.
- Player-facing spoken sample: theatre of the mind. Fail if a secret, difficulty class, unearned name, or process note is inside that passage.

## 3. Vault format stacks (P5, SC-005, SC-006)

On a mixed wiki page (DM bands plus spoken look): copy-writer on DM bands, theatre of the mind on spoken, obsidian-markdown on the note. Fail if one voice is used for the whole file. Fail if a non-vault chat proposal is required to use vault format.

## 4. Visual split (P6–P7, SC-008, SC-009)

- Gather look for a known owner: visual-references. Fail if this job is treated as placing art.
- Place or mint the picture: visual-aids. Fail if gather is skipped when the owner is known.
- Spoken look on the same page still theatre of the mind. Fail if the picture is treated as the words the DM says.
- Missing look: stop. Fail if a face is invented.
- Different owner's picture used as identity: fail.

## 5. Pointers, not copies (Constitution IX)

- `AGENTS.md` is the stack table.
- `docs/agents/work.md` and `wiki/AGENTS.md` do not hardcode only copy-writer plus obsidian-markdown.
- Craft skills that already follow `docs/agents/work.md` do not restate the old vault-write load trio.

## 6. Legacy untouched (SC-007)

This change set does not rewrite `legacy/` or restyle historical wiki pages solely to match routing.

Pass: steps 1–6 hold. Fail any step → routing is not the default yet.
