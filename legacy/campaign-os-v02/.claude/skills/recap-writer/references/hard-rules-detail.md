# Hard rules — full detail

Rule numbers match the core `## Hard rules` list in `.claude/skills/recap-writer/SKILL.md`.

1. **`vault/episodes/NNN/sNN-recap.md` is canon-derived, not memory-derived.** Every sentence
   traces to a page the `ingest(sNN)` commit touched (its diff shows the
   fact landing at `status: canon`) or is transcript color directly
   supporting one. Content still `status: pending`/`draft` — prep material
   that hasn't survived contact with the table — never appears, no
   exceptions, no "it'll probably be canon by next session."
2. **`vault/episodes/NNN/sNN-highlights.md` quotes are transcript-derived and verbatim.** Every
   quote and moment cites a real `vault/episodes/NNN/transcript.md` L-number. Lightly clean
   filler/false-starts only; never reword for flavor, never invent a line
   that reads better than what was said.
3. **`vault/episodes/NNN/sNN-recap.md` is 900–1350 words.** Hook by sentence
   two. Every sentence earns its place. `vault/refs/qc-recap.md` SPEAKING-TIME
   / ATTENTION / BREVITY.
4. **3–8 quotes, 1–3 moments on `vault/episodes/NNN/sNN-highlights.md`.** Fewer than 3 quotes →
   the session was thin on table-worthy lines; say so rather than padding
   with a weak one. More than 8 → cut to the best 8, don't ship a long tail.
5. **The Status Gate (`vault/refs/vault/_common/hard-rules.md`), with this
   skill's own proposal mechanic.** Both files ship
   `publish: false`, whatever `status` you land on (`pending` — see Owned
   paths). Propose the flip as a response line, never a file edit:
   `PUBLISH-PROPOSED: <path>, <path> — <one-line reason>`. `publish: true`
   is a Phase-7 verb (`publish-site`, `vault/refs/runbook-publish.md`) —
   writing it here, even flipped back to `false` same-turn, is still a
   rule-5 violation, since a hook run against `publish: true` mid-edit is
   exactly the drift the gates exist to prevent.
6. **`vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md`: both or neither.** Don't leave the
   session half-done because one file was easier. `retrospective.md` is
   separate and optional — it never blocks or is blocked by the other two.
7. **In-world filter applies to highlights, not recap.** A quote candidate
   about the game (in-character speech, a declared in-fiction action, DM
   narration) is fair game; pure table banter (real life, logistics,
   meta-commentary about the rules) is not a highlight no matter how
   memorable, even if it sits right next to a cited L-number.
8. **Wikilink every named entity on first mention**, in both files. No
   resolving page → leave as plain text and flag it in your response; never
   invent a `[[link]]` target.
9. **Correct `created`/`updated` frontmatter.** `vault/_templates/_episodes/_session_recap.md`
   and `vault/_templates/_episodes/_session_highlights.md` both default `created`/`updated`
   to the placeholder `"{date}"` — replace it with today's real date; never
   leave the placeholder.
10. **Degrade by asking**, not guessing (see `.claude/skills/recap-writer/references/degrade-by-asking.md`).
