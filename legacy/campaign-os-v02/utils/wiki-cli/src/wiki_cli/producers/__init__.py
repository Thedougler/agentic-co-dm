"""Auto-discovers every producer module in this package and builds the
`PRODUCERS` registry, keyed by the legacy family id each module reports
under (e.g. `"W87"`). A new producer module dropped here — declaring
`FAMILY_ID: str` and `run(config, targets, corpus) -> list[Finding]` at
module level — registers itself; no edits to this file needed. A module also
declaring `RULE_DOCS: tuple[ProducerRuleDoc, ...]` files its `fix` text under
each rule id it emits (`RULE_DOCS` here, keyed by rule id rather than family
id, since a module can emit more than one rule id), which is what
`report.fix_text` and `wiki lint --rules` read for an id no rule class
owns. Mirrors
`wiki_cli.rules`'s auto-discovery (`pkgutil.iter_modules` on this package),
except a producer is a plain function, not a `BaseRule` subclass, so
registration reads two module-level names instead of relying on a class
decorator's side effect.

`ProducerMeta` carries the four runtime facts the orchestrator needs beyond
`run` itself, each an optional module-level name:

- `WHEN` — `When.EDIT` (the default) or `When.SWEEP`. A SWEEP producer runs
  only on a full-vault sweep. Absent, it is derived from `RULE_DOCS`: SWEEP
  when every doc the module files says SWEEP.
- `PURE` — True when the producer's verdict for one target depends on that
  target's own bytes plus its declared config alone. Only a pure producer
  joins the content-hash findings cache (`db.py`). Default False.
- `VERSION` — a digit string in the cache key; bump it when the producer's
  own logic changes. Default `"1"`.
- `config_fingerprint(repo_root) -> str` — the part of the cache key that
  covers config living outside the target file (a Vale styles package, a
  disabled-rule set). A pure producer whose output any on-disk config can
  change MUST declare it, or a config edit serves stale cached findings.
"""

from __future__ import annotations

import importlib
import pkgutil
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from wiki_cli.contracts import ProducerRuleDoc, When

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from wiki_cli.config import Config
    from wiki_cli.contracts import Corpus, Finding


class ProducerRun(Protocol):
    """Shape every producer module's `run` function must match."""

    def __call__(self, config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]: ...


@dataclass(frozen=True)
class ProducerMeta:
    """One producer's runtime metadata — see the module docstring."""

    family_id: str
    run: ProducerRun
    when: When
    pure: bool
    version: str
    config_fingerprint: Callable[[Path], str] | None

    def cache_fingerprint(self, repo_root: Path) -> str:
        """The config half of this producer's cache key."""
        return "" if self.config_fingerprint is None else self.config_fingerprint(repo_root)


PRODUCERS: dict[str, ProducerRun] = {}
PRODUCER_META: dict[str, ProducerMeta] = {}
RULE_DOCS: dict[str, ProducerRuleDoc] = {}


def _derive_when(module: object, docs: tuple[ProducerRuleDoc, ...]) -> When:
    declared = getattr(module, "WHEN", None)
    if isinstance(declared, When):
        return declared
    if docs and all(doc.when is When.SWEEP for doc in docs):
        return When.SWEEP
    return When.EDIT


for _mod_info in pkgutil.iter_modules(__path__):
    if _mod_info.name.startswith("_"):
        continue
    _module = importlib.import_module(f"{__name__}.{_mod_info.name}")
    _family_id = getattr(_module, "FAMILY_ID", None)
    _run = getattr(_module, "run", None)
    if _family_id is None or _run is None:
        continue
    if _family_id in PRODUCERS:
        raise ValueError(f"duplicate producer family id {_family_id!r}")
    PRODUCERS[_family_id] = _run
    _docs: tuple[ProducerRuleDoc, ...] = getattr(_module, "RULE_DOCS", ())
    PRODUCER_META[_family_id] = ProducerMeta(
        family_id=_family_id,
        run=_run,
        when=_derive_when(_module, _docs),
        pure=bool(getattr(_module, "PURE", False)),
        version=str(getattr(_module, "VERSION", "1")),
        config_fingerprint=getattr(_module, "config_fingerprint", None),
    )
    for _doc in _docs:
        if _doc.id in RULE_DOCS:
            raise ValueError(f"duplicate producer rule doc id {_doc.id!r}")
        RULE_DOCS[_doc.id] = _doc


def all_producers() -> dict[str, ProducerRun]:
    return dict(PRODUCERS)


def all_producer_meta() -> dict[str, ProducerMeta]:
    """Every registered producer's `ProducerMeta`, keyed by family id."""
    return dict(PRODUCER_META)


def all_rule_docs() -> dict[str, ProducerRuleDoc]:
    """Every producer-emitted rule id -> its tier/severity/`fix` metadata."""
    return dict(RULE_DOCS)
