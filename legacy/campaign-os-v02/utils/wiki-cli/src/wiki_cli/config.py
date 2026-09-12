"""Repo-root discovery and `wiki.toml`.

`wiki.toml` owns only what no other config already owns: where the vault and
templates live, where the cache goes, and how much output one run may return.
Prose style stays in `.vale.ini`, page shape stays in `vault/_templates/`, and
neither is restated here — a second copy of a rule is a second rule.
"""

from __future__ import annotations

import hashlib
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

CONFIG_FILENAME = "wiki.toml"
DISABLE_FLAG = ".claude/.lint-disabled"

DEFAULT_VAULT_ROOT = "vault"
DEFAULT_TEMPLATES_ROOT = "vault/_templates"
DEFAULT_CACHE_PATH = ".wiki-cli/cache.sqlite3"
DEFAULT_SCOPED_ROOTS = ("vault",)
DEFAULT_REPORT_CAP = 50


class ConfigError(RuntimeError):
    """`wiki.toml` exists but cannot be used."""



DEFAULT_GRAVITY_ACTIVE_WINDOW = 3
DEFAULT_GRAVITY_ACTIVE_WEIGHT = 2.0
DEFAULT_GRAVITY_ENCOUNTERED_WEIGHT = 1.0

DEFAULT_AGENT_READS_WINDOW = 90

DEFAULT_ORGANIZER_MIN_CLUSTER_SIZE = 4
DEFAULT_ORGANIZER_MIN_CLUSTER_DENSITY = 0.4
DEFAULT_ORGANIZER_RESOLUTION = 1.0
DEFAULT_ORGANIZER_SRD_INCLUDED = False
DEFAULT_ORGANIZER_FLOAT_TYPES: frozenset[str] = frozenset({
    "scene", "recap", "run-guide", "transcript",
    "session", "beat",
    "reference",
})

DEFAULT_PAGERANK_WEIGHTS: dict[str, float] = {
    "CONTAINS": 3.0,
    "LOCATED_AT": 3.0,
    "MEMBER_OF": 3.0,
    "OWNED_BY": 3.0,
    "ORIGINATES_FROM": 3.0,
    "CANON_IN": 3.0,
    "RELATED_TO": 1.0,
}


@dataclass(frozen=True, slots=True)
class PageRankConfig:
    weights: dict[str, float]


@dataclass(frozen=True, slots=True)
class GravityConfig:
    active_window: int
    active_weight: float
    encountered_weight: float


@dataclass(frozen=True, slots=True)
class AgentAccessConfig:
    agent_reads_window: int


@dataclass(frozen=True, slots=True)
class OrganizerConfig:
    min_cluster_size: int
    min_cluster_density: float
    resolution: float
    srd_included: bool
    float_types: frozenset[str] = field(
        default_factory=lambda: DEFAULT_ORGANIZER_FLOAT_TYPES
    )


def _default_gravity() -> GravityConfig:
    return GravityConfig(
        active_window=DEFAULT_GRAVITY_ACTIVE_WINDOW,
        active_weight=DEFAULT_GRAVITY_ACTIVE_WEIGHT,
        encountered_weight=DEFAULT_GRAVITY_ENCOUNTERED_WEIGHT,
    )


def _default_agent_access() -> AgentAccessConfig:
    return AgentAccessConfig(agent_reads_window=DEFAULT_AGENT_READS_WINDOW)


def _default_organizer() -> OrganizerConfig:
    return OrganizerConfig(
        min_cluster_size=DEFAULT_ORGANIZER_MIN_CLUSTER_SIZE,
        min_cluster_density=DEFAULT_ORGANIZER_MIN_CLUSTER_DENSITY,
        resolution=DEFAULT_ORGANIZER_RESOLUTION,
        srd_included=DEFAULT_ORGANIZER_SRD_INCLUDED,
    )


def _default_pagerank() -> PageRankConfig:
    return PageRankConfig(weights=dict(DEFAULT_PAGERANK_WEIGHTS))


@dataclass(frozen=True, slots=True)
class Config:
    repo_root: Path
    vault_root: Path
    templates_root: Path
    cache_path: Path
    scoped_roots: tuple[str, ...]
    report_cap: int
    fingerprint: str
    """Hash of the settings that can change a rule's verdict. Part of the cache key."""
    _thresholds: dict[str, str]
    gravity: GravityConfig = field(default_factory=_default_gravity)
    agent_access: AgentAccessConfig = field(default_factory=_default_agent_access)
    organizer: OrganizerConfig = field(default_factory=_default_organizer)
    pagerank: PageRankConfig = field(default_factory=_default_pagerank)

    @property
    def disable_flag(self) -> Path:
        return self.repo_root / DISABLE_FLAG

    def is_disabled(self) -> bool:
        return self.disable_flag.is_file()

    def threshold(self, key: str) -> str:
        """Raw threshold string, exactly as in the legacy map."""
        return self._thresholds[key]

    def threshold_list(self, key: str) -> list[str]:
        """Split a `;;`-delimited or ` | `-delimited threshold into a list."""
        parts = self._thresholds[key].split(";;")
        if len(parts) == 1:
            parts = parts[0].split(" | ")
        return parts


def find_repo_root(start: Path | None = None) -> Path:
    """Walk up from `start` for `wiki.toml`, else `.git`.

    Agents run this CLI from wherever they happen to be. Resolving the root
    from the working directory alone silently lints nothing from a subdirectory.
    """
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / CONFIG_FILENAME).is_file():
            return candidate
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    raise ConfigError(
        f"no {CONFIG_FILENAME} or .git found at or above {current} — "
        f"run from inside the repo, or create {CONFIG_FILENAME} at its root"
    )


def _fingerprint(parts: tuple[str, ...]) -> str:
    return hashlib.sha256("\x00".join(parts).encode("utf-8")).hexdigest()[:16]


def _require_str(table: dict[str, object], key: str, default: str) -> str:
    value = table.get(key, default)
    if not isinstance(value, str):
        raise ConfigError(f"{CONFIG_FILENAME}: expected a string for {key!r}, got {value!r}")
    return value


_CONFIG_CACHE: dict[Path, tuple[int, Config]] = {}
"""Resolved repo root -> (`wiki.toml`'s mtime_ns at load time, its `Config`).

`check()` on a `FileRule`/`VaultRule` takes no `config` param, so dozens of
rules call `load_config()` fresh for a single threshold — on a full-vault
run that's tens of thousands of calls, each a disk read plus a TOML parse,
for a file that never changes mid-run. Keyed on mtime_ns (not just root) so
a config file edited between calls — `test_fingerprint_includes_thresholds`
does this within one process — still reloads."""


def load_config(repo_root: Path | None = None) -> Config:
    """Load `wiki.toml` from the repo root, falling back to defaults
    throughout. Cached per resolved root; see `_CONFIG_CACHE`."""
    root = (repo_root or find_repo_root()).resolve()
    config_path = root / CONFIG_FILENAME
    mtime_ns = config_path.stat().st_mtime_ns if config_path.is_file() else -1

    cached = _CONFIG_CACHE.get(root)
    if cached is not None and cached[0] == mtime_ns:
        return cached[1]

    config = _load_config_uncached(root, config_path)
    _CONFIG_CACHE[root] = (mtime_ns, config)
    return config


def _load_config_uncached(root: Path, config_path: Path) -> Config:
    data: dict[str, object] = {}
    if config_path.is_file():
        try:
            data = tomllib.loads(config_path.read_text(encoding="utf-8"))
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as error:
            raise ConfigError(f"{config_path}: {error}") from error

    vault = data.get("vault", {})
    lint = data.get("lint", {})
    cache = data.get("cache", {})
    bench = data.get("bench", {})
    gravity_table = data.get("gravity", {})
    agent_access_table = data.get("agent_access", {})
    pagerank_table = data.get("pagerank", {})
    organizer_table = data.get("organizer", {})
    thresholds_table = data.get("thresholds", {})
    if (
        not isinstance(vault, dict)
        or not isinstance(lint, dict)
        or not isinstance(cache, dict)
        or not isinstance(bench, dict)
        or not isinstance(gravity_table, dict)
        or not isinstance(agent_access_table, dict)
        or not isinstance(pagerank_table, dict)
        or not isinstance(organizer_table, dict)
        or not isinstance(thresholds_table, dict)
    ):
        raise ConfigError(
            f"{config_path}: [vault], [lint], [cache], [bench], [gravity], [agent_access], [pagerank], [organizer] and [thresholds] must be tables"
        )

    vault_root = _require_str(vault, "root", DEFAULT_VAULT_ROOT)
    templates_root = _require_str(vault, "templates", DEFAULT_TEMPLATES_ROOT)
    cache_path = _require_str(cache, "path", DEFAULT_CACHE_PATH)

    raw_roots = lint.get("scoped_roots", list(DEFAULT_SCOPED_ROOTS))
    if not isinstance(raw_roots, list) or not all(isinstance(item, str) for item in raw_roots):
        raise ConfigError(f"{config_path}: lint.scoped_roots must be a list of strings")
    scoped_roots = tuple(str(item).strip("/") for item in raw_roots)

    raw_cap = lint.get("report_cap", DEFAULT_REPORT_CAP)
    if not isinstance(raw_cap, int) or isinstance(raw_cap, bool) or raw_cap < 1:
        raise ConfigError(f"{config_path}: lint.report_cap must be a positive integer")

    gravity_cfg = GravityConfig(
        active_window=int(gravity_table.get("active_window", DEFAULT_GRAVITY_ACTIVE_WINDOW)),
        active_weight=float(gravity_table.get("active_weight", DEFAULT_GRAVITY_ACTIVE_WEIGHT)),
        encountered_weight=float(
            gravity_table.get("encountered_weight", DEFAULT_GRAVITY_ENCOUNTERED_WEIGHT)
        ),
    )

    agent_access_cfg = AgentAccessConfig(
        agent_reads_window=int(
            agent_access_table.get("agent_reads_window", DEFAULT_AGENT_READS_WINDOW)
        ),
    )

    raw_float_types = organizer_table.get("float_types", None)
    if raw_float_types is None:
        float_types = DEFAULT_ORGANIZER_FLOAT_TYPES
    elif not isinstance(raw_float_types, list) or not all(
        isinstance(t, str) for t in raw_float_types
    ):
        raise ConfigError(f"{config_path}: organizer.float_types must be a list of strings")
    else:
        float_types = frozenset(raw_float_types)

    organizer_cfg = OrganizerConfig(
        min_cluster_size=int(
            organizer_table.get("min_cluster_size", DEFAULT_ORGANIZER_MIN_CLUSTER_SIZE)
        ),
        min_cluster_density=float(
            organizer_table.get("min_cluster_density", DEFAULT_ORGANIZER_MIN_CLUSTER_DENSITY)
        ),
        resolution=float(organizer_table.get("resolution", DEFAULT_ORGANIZER_RESOLUTION)),
        srd_included=bool(organizer_table.get("srd_included", DEFAULT_ORGANIZER_SRD_INCLUDED)),
        float_types=float_types,
    )

    raw_weights = pagerank_table.get("weights", {})
    if not isinstance(raw_weights, dict):
        raise ConfigError(f"{config_path}: pagerank.weights must be a table")
    pagerank_weights = dict(DEFAULT_PAGERANK_WEIGHTS)
    pagerank_weights.update({k: float(v) for k, v in raw_weights.items()})
    pagerank_cfg = PageRankConfig(weights=pagerank_weights)

    thresholds: dict[str, str] = {}
    for key, value in thresholds_table.items():
        if not isinstance(value, str):
            raise ConfigError(
                f"{config_path}: expected a string for thresholds.{key!r}, got {value!r}"
            )
        thresholds[key] = value
    threshold_parts = tuple(f"{key}={thresholds[key]}" for key in sorted(thresholds))

    return Config(
        repo_root=root,
        vault_root=root / vault_root,
        templates_root=root / templates_root,
        cache_path=root / cache_path,
        scoped_roots=scoped_roots,
        report_cap=raw_cap,
        fingerprint=_fingerprint((vault_root, templates_root, *scoped_roots, *threshold_parts)),
        gravity=gravity_cfg,
        agent_access=agent_access_cfg,
        organizer=organizer_cfg,
        pagerank=pagerank_cfg,
        _thresholds=thresholds,
    )


def _display(path: Path, repo_root: Path) -> str:
    """`path` relative to `repo_root` when possible, else its raw form —
    keeps error messages readable (`vault/_templates`) instead of a full
    absolute path."""
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def validate_paths(config: Config) -> None:
    """Fail fast when a required path is missing on disk.

    `load_config()` resolves these paths without checking them, so a
    missing `vault/` or `vault/_templates/` would otherwise surface deep
    inside a producer with a confusing error, or silently lint nothing.
    """
    missing: list[str] = []
    if not config.vault_root.is_dir():
        missing.append(f"{_display(config.vault_root, config.repo_root)} (vault_root)")
    if not config.templates_root.is_dir():
        missing.append(f"{_display(config.templates_root, config.repo_root)} (templates_root)")
    for root in config.scoped_roots:
        if not (config.repo_root / root).is_dir():
            missing.append(f"{root} (scoped_roots)")
    if not config.cache_path.parent.is_dir():
        parent_display = _display(config.cache_path.parent, config.repo_root)
        missing.append(f"{parent_display} (cache_path parent)")

    if missing:
        raise ConfigError("required path does not exist: " + "; ".join(missing))


def in_scope(config: Config, rel_path: str) -> bool:
    """True when a repo-relative path lies under a configured lint root."""
    normalised = rel_path.replace("\\", "/")
    return any(
        normalised == root or normalised.startswith(f"{root}/") for root in config.scoped_roots
    )
