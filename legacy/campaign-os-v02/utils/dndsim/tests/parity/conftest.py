"""Puts ``scripts/`` on ``sys.path`` for every test in this directory —
``utils/dndsim/scripts`` is not an installed package (it is issue #52's own
scratch space, matching ``scripts/differential_harness.py``'s precedent of
never being packaged either), so importing ``parity_matchups``/
``parity_harness`` from a test needs the path set explicitly."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
