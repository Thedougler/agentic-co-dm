# dndsim

The combat statistics engine (`utils/dndsim/`): Monte-Carlo simulation of D&D 5e combat
outcomes. Produces DPR distributions, win-rate curves, and effective-CR measurements
consumed by the campaign's encounter-design workflow.

## Language

**Rules pack**:
An installable package defining one ruleset's concepts — conditions, AC/hit
points, attack rolls, saves, damage types — discovered through the
`dndsim.rules` entry-point group. The engine core holds none of this
(`docs/adr/0007-dndsim-engine-is-rules-agnostic.md`).
_Avoid_: "the rules" for engine behavior — engine behavior is the core; a
rules pack is the D&D layer sitting on top of it.

**Primitive**:
One member of the closed vocabulary of effects the engine can execute and
the planner can value. Content composes primitives; it never introduces one.
_Avoid_: "ability" or "feature" as a synonym — those name authored content,
which compiles _down to_ primitives.

**Mechanic**:
One class implementing a single primitive's resolution and its expected
value together, bound by a property test
(`docs/adr/0008-a-mechanic-carries-both-resolve-and-expected-value.md`).
_Avoid_: naming the two halves separately ("the executor path", "the policy
math") — treating them as separable is the drift this contract exists to
prevent.

**Universe**:
One Monte-Carlo sample inside a lockstep batch. Combatant state is held as
arrays indexed by universe, so a single event dispatch advances thousands at
once.
_Avoid_: "iteration" and "run" for this sense — an iteration is one
universe's full encounter; a run is one CLI invocation.

**Importer**:
A plugin that reads authored content — the vault ` ```statblock ` fence, SRD
attack prose — and compiles it to primitives. The fence stays authoritative
(`docs/adr/0009-content-authority-stays-in-the-vault-statblock-fence.md`).
_Avoid_: "parser" when the compile-to-primitives step is meant; parsing is
only the first half of what an importer does.

**Policy**:
A pluggable decision-maker choosing a combatant's action each turn —
greedy expected-value, fixed routine, random, or rollout. Registered in the
`dndsim.policies` group.
_Avoid_: "AI" and "tactics" — both read as a quality judgment about play
rather than a named, swappable component.

**Divergence**:
An intentional behavior difference between `dndsim` and its predecessor,
recorded in `utils/dndsim/DIVERGENCES.md` with its mechanism and
its measured effect on win rate.
_Avoid_: "bug fix" or "regression" — a divergence is neither; it is a known,
measured difference that parity is defined around.
