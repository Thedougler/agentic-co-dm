# Checklist (run before calling the encounter done)

- [ ] Standard queries run and pasted; stub check clean or expansion
      confirmed.
- [ ] PC-Connection Requirement named in `link_of_relevance`.
- [ ] All seven Toy fields present, each passing its field rule.
- [ ] Named/recurring foes hand off to `.claude/skills/draft-content/references/npc.md`; nothing here duplicates
      a villain page's Toy Chest or Three Villain Questions.
- [ ] Composition shape chosen and creature-type cap respected (Hard
      Rule 7).
- [ ] Challenge Calibration (or Skill Track) cites real `vault/campaigns/shattered-sea/pcs/*.md`
      evidence with a confidence label — never CR alone.
- [ ] Terrain features are mechanical, not decorative (2–3 minimum).
- [ ] `## If Ignored` names a concrete, observable consequence.
- [ ] Any faction-clock impact flagged for `world-update`, not applied
      here.
- [ ] Every resolvable check is a full-anatomy `[!check]` or a full-anatomy
      DC-menu table; no attack roll framed as a DC; every resolved loop
      states its number.
- [ ] Combat encounters ship a `## Run Sheet` (foe roster tracker, round
      script, statblocks transcluded at point of use — never restated).
- [ ] `## Raising the Stakes` / `## Lowering the Stakes` present as a
      matched pair, each dial carrying a trigger condition and a concrete
      numeric delta.
- [ ] `## If They're Stuck` present for any objective/puzzle-gated beat
      (three rungs); absent for a straight fight with no gate.
- [ ] `## Endings` covers every branch this page states odds for; no
      plot-defense phrasing without a paired let-it-happen fallback.
- [ ] Opening carries a one-line Dramatic Question; the page closes with a
      `## Transition` block (goto wikilink, elapsed time, every branch
      skip on its own line).
- [ ] A sibling `vault/episodes/NNN/` scene file for the same fight transcludes
      this page's operative blocks and cross-links back; nothing here is
      re-derived or omitted.
- [ ] Page lives at `vault/campaigns/shattered-sea/encounters/<slug>.md`; `status:` at `draft` or
      `pending` only; `publish:` untouched (`false`).
- [ ] `npm run lint -- vault/campaigns/shattered-sea/encounters/<slug>.md` reported zero findings
      BEFORE the `content-quality-checker` dispatch, and again after its
      findings were fixed.
- [ ] `content-quality-checker` run with the `table-run-page` profile over
      the finished page — dispatched alone, never in the same message as a
      writer or linter on that path; `PASS`, or every finding fixed and the
      check re-run clean by resuming that instance (`SendMessage`).
