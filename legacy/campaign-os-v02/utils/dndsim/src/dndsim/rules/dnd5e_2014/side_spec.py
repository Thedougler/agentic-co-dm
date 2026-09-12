"""Side-spec grammar for ``dndsim sim-combat <X> <Y>`` (issue #67): resolves
one side-spec string — a bare slug, a literal path, ``<slug>:<count>``, a
comma list of either, or the reserved keyword ``party`` — into the loaded
:class:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec` list ``run_combat``
takes for that side.

``run_combat`` (``rules/dnd5e_2014/combat.py``) takes ``party``/``enemies``
as two separate lists rather than one combatant array keyed by an embedded
``side`` field: which list a combatant ends up in *is* its side, regardless
of what the page's own ``sim: side`` says.

Page loading goes entirely through ``rules/dnd5e_2014/sweep.py``'s
``load_combatant_spec`` (built on
:func:`~dndsim.profile.load_compiled_statblock`, the one page-to-
``CompiledStatblock`` assembly path) — the resolution problem sweep.py
already solved is reused here rather than re-derived a second time; this
module adds only the token grammar and the slug/alias search sweep.py's
callers don't need (a sweep's subject/opponent are always literal paths).
"""

from __future__ import annotations

import glob
import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import yaml

from dndsim.profile import ProfileError
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec
from dndsim.rules.dnd5e_2014.statblock import StatblockParseError
from dndsim.rules.dnd5e_2014.sweep import (
    DEFAULT_CORPUS_DIRS,
    DEFAULT_PARTY_GLOB,
    SweepLoadError,
    load_combatant_spec,
)

# Mirrors runner.mjs's DEFAULT_PC_DIRS/DEFAULT_CANDIDATE_DIRS: a bare
# side-spec token is resolved against both the creature corpus and the
# PC-sheet directory, since sim-combat doesn't know in advance whether a
# token names a PC or a monster — either can appear on either side.
DEFAULT_PC_DIRS: Final[tuple[Path, ...]] = (Path(DEFAULT_PARTY_GLOB).parent,)
DEFAULT_CANDIDATE_DIRS: Final[tuple[Path, ...]] = DEFAULT_CORPUS_DIRS + DEFAULT_PC_DIRS

# Mirrors load.mjs's STRIPPABLE_SUFFIXES.
_STRIPPABLE_SUFFIXES: Final[tuple[str, ...]] = ("-sheet", "-statblock")

_COUNT_RE: Final[re.Pattern[str]] = re.compile(r"^\d+$")
_FRONTMATTER_RE: Final[re.Pattern[str]] = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


class SideSpecError(ValueError):
    """A side-spec string failed to resolve — empty, ambiguous, unresolvable,
    or a token whose page failed to load — naming the offending spec/token
    and (for ambiguity) every candidate, never fuzzy-matching."""


def _read_alias(path: Path) -> str | None:
    """The page's frontmatter ``alias:`` value, or ``None`` — the one field
    :func:`resolve_combatant_arg` reads, mirroring ``load.mjs``'s
    ``readFrontmatter``."""
    try:
        text = path.read_text()
    except OSError:
        return None
    match = _FRONTMATTER_RE.match(text)
    if match is None:
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    if isinstance(data, dict):
        alias = data.get("alias")
        return alias if isinstance(alias, str) else None
    return None


def resolve_combatant_arg(arg: str, candidate_dirs: Sequence[Path]) -> Path:
    """Resolve one bare combatant reference (a slug or alias) against
    ``candidate_dirs`` — port of ``load.mjs``'s ``resolveCombatantArg``.

    A real, resolvable path (relative or absolute) is used literally.
    Otherwise ``arg`` is matched against each candidate dir's ``*.md``
    files: the basename with any trailing ``-sheet``/``-statblock`` suffix
    stripped, the bare basename itself, or the file's own frontmatter
    ``alias:`` value must equal ``arg`` exactly (case-sensitive, no
    fuzzy/partial matching — a convenience shortcut, not a search feature).
    Zero or multiple matches raises :class:`SideSpecError` naming every
    directory searched or every candidate found, respectively.
    """
    literal = Path(arg)
    if literal.exists():
        return literal

    matches: set[Path] = set()
    for directory in candidate_dirs:
        if not directory.is_dir():
            continue
        for file in directory.glob("*.md"):
            base = file.stem
            slug = base
            for suffix in _STRIPPABLE_SUFFIXES:
                if base.endswith(suffix):
                    slug = base[: -len(suffix)]
                    break
            alias = _read_alias(file)
            if slug == arg or base == arg or alias == arg:
                matches.add(file)

    if not matches:
        dirs = ", ".join(str(d) for d in candidate_dirs)
        raise SideSpecError(
            f'no file matching "{arg}" — searched {dirs} for <slug>.md, '
            f"<slug>-sheet.md, <slug>-statblock.md, or a frontmatter alias: "
            f'matching "{arg}" (pass a literal path to use a file elsewhere)'
        )
    if len(matches) > 1:
        found = ", ".join(str(p) for p in sorted(matches))
        raise SideSpecError(
            f'"{arg}" matches multiple files: {found} — pass a literal path to disambiguate'
        )
    return next(iter(matches))


@dataclass(frozen=True, slots=True)
class SideResolution:
    """One resolved side: the loaded combatants plus the source path each
    came from, same order — lets a caller label a side (party/enemy names
    joined) without re-deriving it from the ``CombatantSpec`` list."""

    combatants: tuple[CombatantSpec, ...]
    paths: tuple[Path, ...]


def _load(path: Path, *, suffix: str) -> CombatantSpec:
    try:
        return load_combatant_spec(path, suffix=suffix)
    except (StatblockParseError, ProfileError, SweepLoadError) as err:
        raise SideSpecError(f"{path}: {err}") from err


def resolve_side(
    spec: str,
    *,
    role: str,
    candidate_dirs: Sequence[Path] = DEFAULT_CANDIDATE_DIRS,
    party_glob: str = DEFAULT_PARTY_GLOB,
) -> SideResolution:
    """Resolve one side-spec string into loaded combatants — port of
    ``runner.mjs``'s ``resolveSide``.

    Grammar: the literal keyword ``"party"`` expands ``party_glob``
    (sorted, matching ``resolve_side``'s JS counterpart); otherwise a
    comma-separated list of tokens, each a bare slug/path or
    ``<slug-or-path>:<count>`` (``count`` must be a base-10 positive
    integer — a non-digit suffix after the last colon is treated as part of
    the ref, not a count, matching the reference's ``/^\\d+$/`` test).
    ``role`` ("party"/"enemy") only labels entity-id suffixes and error
    context here — which Python list a combatant ends up in is what
    determines its side for ``run_combat``, not any field on the spec.

    Raises :class:`SideSpecError` on an empty spec, an empty token list, a
    zero/negative count, an unresolvable or ambiguous token, or a page that
    fails to load.
    """
    if spec.strip() == "party":
        pc_paths = sorted(Path(p) for p in glob.glob(party_glob))
        if not pc_paths:
            raise SideSpecError(f'--party-glob "{party_glob}" matched no files')
        pc_combatants = tuple(
            _load(path, suffix=f"/{role}{index}") for index, path in enumerate(pc_paths)
        )
        return SideResolution(combatants=pc_combatants, paths=tuple(pc_paths))

    tokens = [t.strip() for t in spec.split(",") if t.strip() != ""]
    if not tokens:
        raise SideSpecError(
            "empty combatant spec — expected a comma list of <slug-or-path>[:count] "
            'tokens, or the keyword "party"'
        )

    combatants: list[CombatantSpec] = []
    paths: list[Path] = []
    occurrence = 0
    for token in tokens:
        colon_idx = token.rfind(":")
        maybe_count = token[colon_idx + 1 :] if colon_idx != -1 else None
        has_count = maybe_count is not None and _COUNT_RE.match(maybe_count) is not None
        ref = token[:colon_idx] if has_count else token
        count = int(maybe_count) if has_count and maybe_count is not None else 1
        if count < 1:
            raise SideSpecError(f'"{token}": count must be >= 1')
        path = resolve_combatant_arg(ref, candidate_dirs)
        for _ in range(count):
            combatants.append(_load(path, suffix=f"/{role}{occurrence}"))
            paths.append(path)
            occurrence += 1

    return SideResolution(combatants=tuple(combatants), paths=tuple(paths))
