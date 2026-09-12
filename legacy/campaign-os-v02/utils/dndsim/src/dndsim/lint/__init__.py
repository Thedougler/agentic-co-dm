"""The `dndsim lint` arm (ADR-0010).

The statblock and combatant-block rules moved out of markdownlint-obsidian
because their logic is the combat engine's parser, and that parser now lives
here. Enforcement does not fork with them: :mod:`dndsim.lint.findings` emits
the same JSON payload shape ``markdownlint-obsidian --output-formatter json``
emits, so ``utils/scripts/lib/lint-findings.mjs`` can merge both producers
before the one lint ratchet (docs/adr/0005, docs/adr/0006) sees a finding.
"""

from __future__ import annotations
