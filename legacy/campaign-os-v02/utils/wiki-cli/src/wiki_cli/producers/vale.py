"""vale producer (W86): shells the real `vale` binary and this repo's real
`.vale.ini` config — the same config the legacy JS engine's `runVale`
(`utils/scripts/lib/lint-findings.mjs`) merges into its own W86 family.

Only `.vale.ini` is ever used here — `.vale-hard.ini` (the stricter
`MinAlertLevel = error` CI gate) is a separate, standalone check, out of
scope for this producer.

`.vale.ini` itself decides which style packages apply to which file via its
own directory-scoped glob sections (`[vault/**/*.md]`, `[docs/guardrails/**/
*.md]`, ...) — this producer does not reimplement any of that routing. It
only does what the legacy `runVale` did: pick the one config file, hand it
the target paths (relative to `corpus.repo_root`, matching Vale's own
project-relative glob matching — an absolute path never matches a section
glob, confirmed empirically against vale 3.13.0), and translate Vale's own
JSON alerts into `Finding`s. `vale`'s own OOM-driven file-count batching
(`VALE_FILE_BATCH`/`runValeScoped` in `utils/scripts/lib/prose-scope.mjs`)
is not reproduced here: this producer is the SCOPED hot path (a handful of
targets per call, never a full ~2.5k-file corpus sweep in one call), which
stays well under the batch ceiling that machinery exists to protect
against — a future whole-corpus sweep mode can add it if profiling shows a
real need.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "W86"
VERSION = "1"
PURE = True

_CONFIG_FILES: tuple[str, ...] = (
    ".vale.ini",
    ".vale-hard.ini",
    "utils/scripts/lint-rules/config/vale-severity.json",
)
"""Every file outside a target that can change this producer's verdict: the
two Vale configs and the severity-promotion registry. The style packages
under `docs/vale-styles/` join them in
`config_fingerprint` — a styles edit that did not bust the cache is the
exact bug ADR-0024 records against the old engine."""

_STYLES_DIR = "docs/vale-styles"


def config_fingerprint(repo_root: Path) -> str:
    """Size+mtime of every config and style file this producer reads.

    Size+mtime rather than a content hash: the styles tree is hundreds of
    small YAML rules, and hashing all of them on every lint invocation
    costs more than the cache saves. A `touch` with no edit busts the
    cache — a false miss, never a stale hit, which is the safe direction.
    """
    parts: list[str] = []
    paths = [repo_root / name for name in _CONFIG_FILES]
    styles_root = repo_root / _STYLES_DIR
    if styles_root.is_dir():
        paths.extend(sorted(p for p in styles_root.rglob("*") if p.is_file()))
    for path in paths:
        try:
            stat = path.stat()
        except OSError:
            continue  # absent config — its absence is itself part of the key below
        parts.append(f"{path.relative_to(repo_root)}:{stat.st_size}:{stat.st_mtime_ns}")
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:16]


RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.PROSE,
        severity=Severity.WARNING,
        fix=(
            "Rewrite the flagged sentence so the pattern the check names is gone and the "
            "sentence still says the same thing. Swapping a synonym for the matched word, or "
            "rewording to dodge the pattern, is a violation, not a fix."
        ),
    ),
)

# Vale lints YAML frontmatter through a separate code path (`lintMetadata`)
# that runs, and completes, before the Transform step TokenIgnores/
# BlockIgnores apply in — confirmed against Vale v3.13.0 source (see
# `.vale.ini`'s own TokenIgnores comment). Without a guard, a frontmatter
# value that is legitimately non-prose (a wikilink slug, a `SKILL.md` path
# an `owner_skill:` key is required to hold, an `_assets/` file path, a
# lowercase `pc:`/`rarity:` enum value) trips CampaignOS/ai-tells rules that
# only make sense against body prose. This applies the same targeted value
# transform as `transformFrontmatterWikilinks` (utils/scripts/lib/
# prose-scope.mjs) — never a blanket frontmatter skip, most frontmatter text
# still gets linted, e.g. a `summary:` field's prose — but the transformed
# copy is written to a private, per-run temp directory OUTSIDE the repo
# (`tempfile.mkdtemp()`), never beside the original: this repo runs many
# concurrent lint invocations, and a same-directory sibling is visible to
# every other invocation's own target discovery for the whole time it
# exists — a real page under active edit, indistinguishable from one until
# the `finally` block deletes it. Vale's own directory-scoped `.vale.ini`
# sections (`[vault/**/*.md]`, `[vault/episodes/*/transcript*.md]`, ...)
# glob-match a target's path string as passed on the command line, relative
# to the process's cwd — not the file's real on-disk location — and Vale
# resolves `StylesPath`/`Vocab` relative to the `--config` file's own
# directory, never cwd (confirmed empirically against vale 3.13.0: same
# alert, same `Check`, from `--config <repo>/.vale.ini` run with cwd inside
# the repo vs. cwd pointed at an unrelated mirrored tree). So the copy is
# written to `<tmp_root>/<original-repo-relative-path>` and Vale is invoked
# with `cwd=<tmp_root>` and the SAME relative path string the real file
# would use — the section glob sees an identical string and applies
# identically, with zero bytes ever touching a directory the corpus scans.
# `<tmp_root>` is torn down (`shutil.rmtree`) in the same `finally` block
# that already existed; `_sweep_stale_temp_roots` additionally reclaims any
# `wiki-vale-fm-<pid>-*` directory a SIGKILLed prior run left behind (the
# `finally` block never runs on SIGKILL), gated on the embedded pid no
# longer being alive so a genuinely still-running sibling invocation is
# never raced.
_FM_PIPED_WIKILINK_RE = re.compile(r"\[\[[^\]|]+\|([^\]]+)\]\]")
_FM_EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
_FM_UNPIPED_WIKILINK_RE = re.compile(r"\[\[[^\]|]+\]\]")
_FM_UNPIPED_WIKILINK_FILLER = "link"
_FM_VERY_RARE_RE = re.compile(r"\bvery rare\b", re.IGNORECASE)
_FM_OWNER_SKILL_RE = re.compile(r'^(owner_skill:\s*).*$')
_FM_ASSET_PATH_RE = re.compile(r'^([a-z_]+:\s*).*_assets/.*$')
_FM_PC_KEY_RE = re.compile(r'^(pc: "?)([a-z][a-z0-9-]*)("?)$')
_FM_TRANSFORM_HINT_RE = re.compile(
    r"\[\[[^\]]+\]\]|\bvery rare\b|^pc: \"?[a-z]|^owner_skill:\s*\S|_assets/",
    re.IGNORECASE | re.MULTILINE,
)


def _frontmatter_end(lines: list[str]) -> int:
    """Index of the closing `---` fence, or -1 — mirrors `frontmatterEnd`
    in prose-scope.mjs exactly (same boundary rule, same -1 contract)."""
    if not lines or lines[0].strip() != "---":
        return -1
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index
    return -1


def _title_case_slug(slug: str) -> str:
    return "-".join(word[:1].upper() + word[1:] for word in slug.split("-"))


def _transform_frontmatter(content: str) -> str:
    """Applies the same slug-vs-display wikilink split, `very rare` ->
    `rare`, `owner_skill:`/`_assets/` value blanking, and `pc:` title-casing
    as `transformFrontmatterWikilinks` — value by value, never a blanket
    frontmatter skip. Blanks/replaces IN PLACE (never deletes a line), so
    every line number in the file, frontmatter and body alike, stays
    unchanged."""
    lines = content.split("\n")
    end = _frontmatter_end(lines)
    if end == -1:
        return content
    for index in range(1, end):
        line = lines[index]
        line = _FM_EMBED_RE.sub("", line)
        line = _FM_PIPED_WIKILINK_RE.sub(lambda m: m.group(1), line)
        line = _FM_UNPIPED_WIKILINK_RE.sub(_FM_UNPIPED_WIKILINK_FILLER, line)
        line = _FM_VERY_RARE_RE.sub("rare", line)
        line = _FM_OWNER_SKILL_RE.sub(r'\1""', line)
        line = _FM_ASSET_PATH_RE.sub(r'\1""', line)
        line = _FM_PC_KEY_RE.sub(
            lambda m: f"{m.group(1)}{_title_case_slug(m.group(2))}{m.group(3)}", line
        )
        lines[index] = line
    return "\n".join(lines)


def _needs_frontmatter_transform(content: str) -> bool:
    lines = content.split("\n")
    end = _frontmatter_end(lines)
    if end == -1:
        return False
    fm = "\n".join(lines[: end + 1])
    return bool(_FM_TRANSFORM_HINT_RE.search(fm))


_TEMP_ROOT_PREFIX = "wiki-vale-fm-"
"""Mirror-tree directory name prefix: `wiki-vale-fm-<pid>-<mkdtemp suffix>`
under the system temp root — `<pid>` lets `_sweep_stale_temp_roots` tell a
crashed run's leftover apart from a live sibling invocation's."""

_STALE_TEMP_ROOT_AGE_S = 2 * 60
"""Same threshold `prose-scope.mjs`'s `STALE_TEMP_MS` uses for its own
same-dir temp reclaim: long enough that a live run's own still-in-use
directory (however long its `vale` subprocess takes) is never mistaken for
an orphan just because it is old, short enough that a crashed run's litter
does not linger."""


def _pid_is_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # exists, owned by someone else — still alive
    return True


def _sweep_stale_temp_roots(temp_root_parent: Path | None = None) -> None:
    """Best-effort: removes every `wiki-vale-fm-<pid>-*` directory under
    `temp_root_parent` (defaults to the system temp root) whose embedded
    pid is no longer alive AND old enough (`_STALE_TEMP_ROOT_AGE_S`) — self-
    heals a SIGKILLed run's leftover mirror tree instead of letting it
    accumulate forever. Age+liveness together, not either alone: age alone
    would race a live run's own directory (a full-corpus sweep can stage
    mirrors for minutes); pid alone would let a recycled pid shield an
    orphan indefinitely. Called once per `run()` invocation — cheap (a
    single `iterdir` over the temp root), always run so ANY invocation can
    reclaim a prior crash's litter, not only one that itself needs a mirror
    tree this call."""
    root = temp_root_parent or Path(tempfile.gettempdir())
    try:
        entries = list(root.iterdir())
    except OSError:
        return
    now = time.time()
    own_pid = os.getpid()
    for entry in entries:
        if not entry.name.startswith(_TEMP_ROOT_PREFIX):
            continue
        try:
            if not entry.is_dir():
                continue
        except OSError:
            continue
        pid_str = entry.name[len(_TEMP_ROOT_PREFIX) :].split("-", 1)[0]
        try:
            pid = int(pid_str)
        except ValueError:
            continue
        if pid == own_pid:
            continue  # this run's own live mirror tree
        try:
            age_s = now - entry.stat().st_mtime
        except OSError:
            continue
        if age_s < _STALE_TEMP_ROOT_AGE_S:
            continue
        if _pid_is_alive(pid):
            continue  # a live sibling invocation's mirror tree
        shutil.rmtree(entry, ignore_errors=True)


def _run_vale_json(vale_config: Path, rel_args: list[str], cwd: Path) -> dict[str, Any]:
    """Shells `vale --output=JSON` for one batch of already-relative-to-cwd
    targets and returns the parsed alert payload. Split out of `run()` so
    it can be called once for real (repo-relative) targets with
    `cwd=repo_root` and, separately, once for frontmatter-guarded mirror
    copies with `cwd=<tmp_root>` — two batches because they need two
    different cwds for the SAME relative path strings to resolve to two
    different sets of real files on disk."""
    result = subprocess.run(
        ["vale", "--config", str(vale_config), "--output=JSON", *rel_args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode > 1:
        raise RuntimeError(
            f"vale exited {result.returncode} over {len(rel_args)} file(s) — findings would be "
            f"under-reported. stderr: {result.stderr[:300]!r}"
        )
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"vale output unparseable ({error}); "
            f"first 300 bytes of stdout: {result.stdout[:300]!r}; "
            f"stderr: {result.stderr[:300]!r}"
        ) from error
    return payload if isinstance(payload, dict) else {}


_SEVERITY_CONFIG_REL = Path("utils/scripts/lint-rules/config/vale-severity.json")
"""Vale rule -> promoted severity ('error'), hand-maintained
(docs/adr/0018). A promotion always wins over Vale's own declared severity —
mirrors `effectiveValeSeverity`'s first check in `lint-findings.mjs`."""

_RAW_SEVERITY_MAP: dict[str, Severity] = {
    "error": Severity.ERROR,
    "warning": Severity.WARNING,
    "suggestion": Severity.WARNING,
}
"""A promotion entry's own value ('error'/'warning'/'suggestion') maps
through this same table — `vale-severity.json` only ever promotes to
'error' in practice, but the table stays total rather than assuming that."""


def _load_json_object(path: Path) -> dict[str, Any]:
    """Best-effort load of a small config JSON file. Missing, unreadable, or
    malformed all fall back to an empty object — same as the legacy loaders
    (`loadValeSeverityConfig`/`loadAdvisoryConfig`), which treat "no config
    here" as "nothing promoted/advisory" rather than an error. A `repo_root`
    that is a fixture vault (as wiki-cli's own tests use) legitimately has
    neither file; that is not a failure, just an empty override set."""
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _load_severity_overrides(repo_root: Path) -> dict[str, str]:
    promoted = _load_json_object(repo_root / _SEVERITY_CONFIG_REL).get("promoted")
    return promoted if isinstance(promoted, dict) else {}


def _effective_severity(
    check: str,
    raw_severity: str,
    overrides: dict[str, str],
) -> Severity:
    """A promotion override always wins; otherwise Vale's own alert
    `Severity` carries through, with `suggestion` bucketing into `WARNING`
    (the schema is binary — ADR-0005/0006/0064). A warning is baselineable
    debt, so a low-confidence check needs no severity of its own."""
    if check in overrides:
        return _RAW_SEVERITY_MAP.get(overrides[check], Severity.WARNING)
    return Severity.ERROR if raw_severity == "error" else Severity.WARNING


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Run `vale --output=JSON` over `targets` using `corpus.repo_root`'s
    real `.vale.ini`, translating each alert into a `Finding`.

    `targets` are absolute paths under the repo. An empty `targets` list is
    a no-op — invoking `vale` with zero file arguments switches it into its
    own config-driven full-vault glob sweep instead (the ~142s cold-sweep
    cost this producer's scoped design exists to avoid), never what an
    empty target list means to a caller of this function (same contract as
    the markdownlint producer).

    HANDLED FAILURES: `vale` binary missing from PATH (raised, clear
    message); no `.vale.ini` at `corpus.repo_root` (Vale is simply not
    configured there — a fixture repo without a prose arm — returns `[]`,
    same as the legacy `runVale`'s own `existsSync` guard); `vale` exiting
    >1 (an execution error, not "0 alerts" — raised, since the legacy engine
    treats this as "findings would be under-reported," never a clean file);
    unparseable JSON output (raised with a stdout/stderr excerpt); a target
    unreadable at frontmatter-guard time (treated as "not this producer's
    problem," same posture as a target that vanished before the `vale` call
    below — `vale` itself reports the real error for it).
    NOT HANDLED (by choice): the JS engine's OOM-driven file-count batching
    and per-file line-chunking (`prose-scope.mjs`'s `runValeScoped`) — see
    the module docstring for why the scoped hot path this producer serves
    does not need it.
    """
    del config  # this producer's invocation is fully determined by corpus.repo_root's own .vale.ini
    if not targets:
        return []

    repo_root = corpus.repo_root
    vale_config = repo_root / ".vale.ini"
    if not vale_config.is_file():
        return []  # Vale is not configured at this root — not a failure, just inapplicable

    if shutil.which("vale") is None:
        raise FileNotFoundError(
            "vale binary not found on PATH — install Vale (https://vale.sh) before running the vale producer"
        )

    _sweep_stale_temp_roots()  # reclaim any SIGKILLed prior run's mirror tree before this one runs

    # A target can vanish between the corpus glob that built `targets` and
    # this subprocess call — a concurrent edit/delete elsewhere in the repo,
    # not a lint failure of the page itself. Vale exits 2 on a missing CLI
    # argument (E100 "does not exist"), which the check above already
    # treats as "findings would be under-reported" and raises; skip a
    # vanished target instead, the same as if it had never been a target
    # (this function's own contract for an empty `targets` list).
    #
    # A target whose frontmatter needs the transform (see module-level
    # comment above `_FM_PIPED_WIKILINK_RE`) gets its transformed copy
    # mirrored into a private out-of-repo temp directory (`temp_root`,
    # created lazily on the first target that actually needs one) at
    # `temp_root/<original-repo-relative-path>` — same relative path string
    # as the original, so `.vale.ini`'s directory-scoped sections still
    # match it (see module docstring), but no bytes ever land inside a
    # directory the corpus/target-discovery walk scans. Every other target
    # (the common case) passes through untouched, batched into `rel_args`
    # and run with `cwd=repo_root` exactly as before — zero added cost for
    # the common path.
    temp_root: Path | None = None
    rel_args: list[str] = []
    fm_rel_args: list[str] = []
    for target in targets:
        if not target.is_file():
            continue
        resolved = target.resolve()
        original_rel = str(resolved.relative_to(repo_root))
        try:
            content = resolved.read_text(encoding="utf-8")
        except OSError:
            rel_args.append(original_rel)  # unreadable — let `vale` itself report why
            continue
        if not _needs_frontmatter_transform(content):
            rel_args.append(original_rel)
            continue
        if temp_root is None:
            temp_root = Path(tempfile.mkdtemp(prefix=f"{_TEMP_ROOT_PREFIX}{os.getpid()}-"))
        mirror_path = temp_root / original_rel
        mirror_path.parent.mkdir(parents=True, exist_ok=True)
        mirror_path.write_text(_transform_frontmatter(content), encoding="utf-8")
        fm_rel_args.append(original_rel)
    if not rel_args and not fm_rel_args:
        return []
    try:
        payload: dict[str, Any] = {}
        if rel_args:
            payload.update(_run_vale_json(vale_config, rel_args, repo_root))
        if fm_rel_args:
            assert temp_root is not None
            payload.update(_run_vale_json(vale_config, fm_rel_args, temp_root))
    finally:
        if temp_root is not None:
            shutil.rmtree(temp_root, ignore_errors=True)

    overrides = _load_severity_overrides(repo_root)

    findings: list[Finding] = []
    for file_key, alerts in payload.items():
        file_path = Path(file_key)
        rel_path = (
            str(file_path.resolve().relative_to(repo_root)) if file_path.is_absolute() else file_key
        )
        for alert in alerts or []:
            check = alert.get("Check") or ""
            span = alert.get("Span") or [1]
            findings.append(
                Finding(
                    rule_id=FAMILY_ID,
                    file=rel_path,
                    line=int(alert.get("Line") or 1),
                    message=f"{check}: {alert.get('Message', '')}",
                    severity=_effective_severity(check, alert.get("Severity", ""), overrides),
                    tier=Tier.PROSE,
                    producer="vale",
                    column=int(span[0]) if span else 1,
                    fixable=False,
                )
            )
    return findings
