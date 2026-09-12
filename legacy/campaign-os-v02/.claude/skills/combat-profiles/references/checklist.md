# Checklist (run before calling a profile done)

- [ ] Standard queries run; idempotent check confirmed this wasn't
      already current (Hard Rule 1).
- [ ] Every number carries `[sheet]`/`[session-NN]`/`[calculated]`/
      `[simulated]`/`[unknown]`/`[theoretical]` — none bare (Hard Rule 2).
- [ ] Three lanes kept separate throughout (Hard Rule 3).
- [ ] Every `[simulated]` figure backed by a real run; seed, version, and
      command recorded; no simulated number hand-adjusted (Hard Rule 9).
- [ ] Every relevant PC capability declared in the block's `abilities:`
      list — a capability the sim can't see is a silent floor
      (Workflow step 4).
- [ ] Unsimulable abilities listed by name, not silently dropped.
- [ ] Session Combat Log entries only appended, never edited/removed
      (Hard Rule 4).
- [ ] Confidence label / sim-assumption label present on every derived
      band or number (Hard Rule 5).
- [ ] Nothing written to `vault/campaigns/shattered-sea/pcs/<name>.md` itself — only
      `vault/campaigns/shattered-sea/pcs/combat-profile/`, `vault/campaigns/shattered-sea/pcs/character-sheets/`, and
      the four governed attribute pages (§ Owned paths).
