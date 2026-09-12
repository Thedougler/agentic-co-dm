"""duplication producer (W83): shells the system-installed jscpd v5 (Rust
binary via Homebrew, `brew install jscpd`) and filters known-boilerplate
clones, mirroring `utils/scripts/lint-duplication.mjs`.

A block every instantiated page copies verbatim from a template on purpose
(e.g. `_npc.md`'s voice-recording button trio) is identical by template
design, not duplicated content to collapse (vault/CLAUDE.md rule 5/6 already
carves out this reasoning for the location family's shared blocks). Content
pages stay untouched — no inline ignore comment, no per-page mutation; the
exemption lives here, once, keyed on a literal signature unique to the known
block.

jscpd's own JSON reporter omits `fragment` text in some configurations, so
exemption matching reads each clone's real line range off disk instead of
trusting reporter fragment text — same approach the legacy script takes.

The `KNOWN_BOILERPLATE` signatures are meant to live in `wiki.toml`
(`thresholds.DUPLICATION_KNOWN_BOILERPLATE`, `;;`-delimited) so they stop
being a hardcoded Python constant — see `_known_boilerplate` below. That key
does not exist in `wiki.toml` yet; until it is added there, this module
falls back to the exact literal signatures
`utils/scripts/lint-duplication.mjs`'s `KNOWN_BOILERPLATE` hardcodes.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier, When

FAMILY_ID = "W83"
VERSION = "1"
PURE = False
"""Uncached: duplication is a cross-file question — no single file's
content hash can key it. SWEEP, so it never runs on a scoped lint."""

RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.CONTENT_SHAPE,
        severity=Severity.WARNING,
        when=When.SWEEP,
        fix=(
            "Keep one owner for the duplicated block and replace the copy with "
            "![[owner#Heading]] for verbatim reuse, or a [[wikilink]] for a restatement. "
            "Rewording the copy until it slips under jscpd's token threshold is not a fix."
        ),
    ),
)

_FORMAT_SUFFIX_RE = re.compile(r":[a-z]+$")
"""jscpd's report suffixes a clone's file name with the sub-format it was
tokenized under (e.g. `...clone-a.md:yaml`) — stripped before resolving the
real path on disk."""

_DEFAULT_KNOWN_BOILERPLATE: tuple[str, ...] = (
    "obsidian-shellcommands:shell-command-voicepr",
    "Read while recording: [[dm-voice-script|voice-profile script]]",
    "zoomDelta: 0.125",
    "Every physical place occupies space relative to other places",
    "Every location worth a page hides at least one findable-but-not-obvious",
    "**Casting Time:** Action\n\n**Range:** 60 feet",
    (
        "**Casting Time:** Action\n\n**Range:** 120 feet\n\n**Components:** V, S\n\n"
        "**Duration:** Instantaneous"
    ),
)
"""`utils/scripts/lint-duplication.mjs`'s `KNOWN_BOILERPLATE` signatures,
verbatim. See the module docstring: this is the fallback used until
`wiki.toml` carries a `DUPLICATION_KNOWN_BOILERPLATE` threshold key."""


def _known_boilerplate(config: Config) -> tuple[str, ...]:
    try:
        return tuple(config.threshold_list("DUPLICATION_KNOWN_BOILERPLATE"))
    except KeyError:
        return _DEFAULT_KNOWN_BOILERPLATE


def _strip_format_suffix(name: str) -> str:
    return _FORMAT_SUFFIX_RE.sub("", name)


def _read_range(file_entry: dict[str, object]) -> str:
    """The real on-disk text of a clone's line range, or `""` when the file
    is unreadable — an exemption can only match text that is actually
    there, and a vanished file is never a false exemption."""
    file_path = Path(_strip_format_suffix(str(file_entry["name"])))
    if not file_path.is_file():
        return ""
    lines = file_path.read_text(encoding="utf-8").split("\n")
    start = int(file_entry["start"]) - 1  # type: ignore[call-overload]
    end = int(file_entry["end"])  # type: ignore[call-overload]
    return "\n".join(lines[start:end])


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Run jscpd over `targets` and map real (non-exempt) clones to findings.

    `targets` are absolute paths under the repo. Mirrors the legacy script:
    same binary family (system-installed jscpd v5, resolved off `PATH`),
    same config (`.jscpd.json`, auto-discovered — no `--config` flag, cwd is
    the repo root), same reporter (`--reporters json`) and flags (`--silent
    --absolute`). An empty `targets` list is a no-op, matching every other
    producer in this package — invoking jscpd with zero path arguments
    would fall back to `.jscpd.json`'s own configured `path` (a full-repo
    sweep), never what an empty target list means to a caller of this
    function.
    """
    if not targets:
        return []

    repo_root = corpus.repo_root
    binary_path = shutil.which("jscpd")
    if binary_path is None:
        raise FileNotFoundError("jscpd not found on PATH — install it: `brew install jscpd`")
    binary = Path(binary_path)

    known_boilerplate = _known_boilerplate(config)
    rel_args = [str(target.resolve().relative_to(repo_root)) for target in targets]

    with tempfile.TemporaryDirectory(prefix="jscpd-report-") as tmp_dir:
        result = subprocess.run(
            [str(binary), "--reporters", "json", "--output", tmp_dir, "--silent", "--absolute", *rel_args],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        report_path = Path(tmp_dir) / "jscpd-report.json"
        if not report_path.is_file():
            return []
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"jscpd output unparseable ({error}); "
                f"first 300 bytes of stdout: {result.stdout[:300]!r}; "
                f"stderr: {result.stderr[:300]!r}"
            ) from error

    findings: list[Finding] = []
    for dup in report.get("duplicates") or []:
        first = dup["firstFile"]
        second = dup["secondFile"]
        text = _read_range(first)
        if any(signature in text for signature in known_boilerplate):
            continue

        first_rel = str(Path(_strip_format_suffix(str(first["name"]))).resolve().relative_to(repo_root))
        second_rel = str(Path(_strip_format_suffix(str(second["name"]))).resolve().relative_to(repo_root))
        findings.append(
            Finding(
                rule_id=FAMILY_ID,
                file=first_rel,
                line=int(first["start"]),
                message=(
                    f"{dup['lines']} duplicated line(s) also at {second_rel}:{second['start']}-{second['end']} "
                    "— keep one owner and replace the copy with ![[owner#Heading]] (verbatim) or a "
                    "[[wikilink]] (restated)"
                ),
                severity=Severity.WARNING,
                tier=Tier.CONTENT_SHAPE,
                producer="duplication",
                column=1,
                fixable=False,
            )
        )
    return findings
