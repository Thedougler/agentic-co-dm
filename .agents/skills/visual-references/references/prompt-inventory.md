# Prompt inventory template

Assemble this as the agent's fact inventory before rendering into the host prompt field.
On Grok Build, turn it into natural prose via `imagine`. On other hosts, adapt to the
prompt style that produces the best results.

The inventory has two halves that serve different purposes:

- **Identity anchors** — short, factual. Lock what things look like. Drawn from vault pages.
- **Scene direction** — expressive, cinematic. Drive composition, camera, mood, movement,
  lighting, depth. This is where art quality lives. Write it the way a cinematographer
  or concept art director would brief a shot.

```text
Scene direction:
[Describe the moment as a shot — camera angle, depth of field, movement, atmosphere,
lighting drama, emotional tone. This is the creative half. Write cinematically.]

Identity anchors (same order as image-input array):
- [owner]: [what to preserve — face, gear, colours, silhouette from vault reference]

Composition notes:
[Framing, foreground/background relationship, where subjects sit in frame, scale cues]

Aspect ratio / size: ...
Constraints: player-safe only; preserve named identities; each depicted thing uses its own look.
```

The image model sees the reference pixels for identity. The prompt text tells it what
matters about those pixels *and* how to shoot the scene. Both halves carry weight — anchor
facts without cinematic direction produce accurate but flat art.
