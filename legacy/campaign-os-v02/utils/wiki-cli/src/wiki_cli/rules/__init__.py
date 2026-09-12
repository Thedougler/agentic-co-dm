"""Auto-discovers every rule module in this package. A new rule file dropped
here registers itself on import — no edits to this file needed."""

from __future__ import annotations

import importlib
import pkgutil

for _mod in pkgutil.iter_modules(__path__):
    if not _mod.name.startswith("_"):
        importlib.import_module(f"{__name__}.{_mod.name}")
