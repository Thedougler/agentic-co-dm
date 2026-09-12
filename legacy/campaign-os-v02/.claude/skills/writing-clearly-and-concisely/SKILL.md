---
name: writing-clearly-and-concisely
description: >-
  writing-clearly-and-concisely — Strunk's grammar rules and Orwell's clarity doctrine for any
  prose in this repo meant to be read: CLAUDE.md lines, skill/rule bodies, runbooks, commit
  messages, PR descriptions, error messages, lint findings, and all DM-facing or player-facing
  campaign prose. Use when drafting or editing any of those.
---

# Writing Clearly and Concisely

## Overview

Two authorities cover all prose in this repo:

- **Orwell's clarity rules** (`.claude/skills/writing-player-prose/references/prose-quality.md`) — six priority
  rules, four writing faults to eliminate (dying metaphors, verbal false limbs, pretentious
  diction, meaningless words), and prose inflation filters. Applies to every sentence in every
  context. Read this file first.
- **Strunk's grammar and composition rules** (`elements-of-style.md`) — grammar, punctuation,
  active voice, parallel construction, concision. Read when you need specific mechanical guidance.

**WARNING:** `elements-of-style.md` consumes ~12,000 tokens. Read it only when writing or editing prose.

## When to Use This Skill

Use this skill whenever you write prose for humans:

- Documentation, README files, technical explanations
- Commit messages, pull request descriptions
- Error messages, UI copy, help text, comments
- Reports, summaries, or any explanation
- Editing to improve clarity

**If you're writing sentences for a human to read, use this skill.**

## Limited Context Strategy

When context is tight:

1. Write your draft using judgment
2. Dispatch a subagent with your draft and `elements-of-style.md`
3. Have the subagent copyedit and return the revision

## All Rules

### Elementary Rules of Usage (Grammar/Punctuation)

1. Form possessive singular by adding 's
2. Use comma after each term in series except last
3. Enclose parenthetic expressions between commas
4. Comma before conjunction introducing co-ordinate clause
5. Don't join independent clauses by comma
6. Don't break sentences in two
7. Participial phrase at beginning refers to grammatical subject

### Elementary Principles of Composition

8. One paragraph per topic
9. Begin paragraph with topic sentence
10. **Use active voice**
11. **Put statements in positive form**
12. **Use definite, specific, concrete language**
13. **Omit needless words**
14. Avoid succession of loose sentences
15. Express co-ordinate ideas in similar form
16. **Keep related words together**
17. Keep to one tense in summaries
18. **Place emphatic words at end of sentence**

### Section V: Words and Expressions Commonly Misused

Alphabetical reference for usage questions

## Bottom Line

Writing for humans? Read `elements-of-style.md` and apply the rules. Low on tokens? Dispatch a subagent to copyedit with the guide.
