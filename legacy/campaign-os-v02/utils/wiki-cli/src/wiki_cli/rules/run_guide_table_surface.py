"""W140/W141 — session ≥ RUN_GUIDE_SHAPE_MIN_SESSION table-surface contract.

W140: episode `subtype: overview` is named `eNN-overview.md` and carries
`session_shape:`. Episode `subtype: run-guide` is named
`eNN-run-guide-<slug>.md`.

W141: every beat in the episode directory appears on at least one episode
run-guide — a whole-page `![[beat-…]]` embed, a section or spoken-sibling
embed under a numbered play H2, or a `[[slug]]` under `## Side-tracks` /
`## Exit`. `![[` is illegal under those two headings.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_EPISODE_DIR_RE = re.compile(r"^vault/episodes/(\d+)/")
_E_GUIDE_RE = re.compile(r"^e(\d+)-run-guide-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
_H2_RE = re.compile(r"^## (.+)$")
_EMBED_RE = re.compile(r"!\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]")
_LINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]")
_PERFORMATIVE_MARKERS = ("-narration-", "-dialogue-")
_RESERVED_H2 = frozenset({"Last Time", "Prep", "Side-tracks", "Exit"})
_LINK_ONLY_H2 = frozenset({"Side-tracks", "Exit"})
_SESSION_SHAPES = frozenset(
    {
        "crossing",
        "site",
        "town",
        "intrigue",
        "investigation",
        "set-piece",
        "hunt",
        "downtime",
        "climax",
    }
)
_SOURCE = "vault/_templates/_episodes/_session_run_guide.md"
_OVERVIEW_SOURCE = "vault/_templates/_episodes/_session_overview.md"


def _min_session() -> int:
    return int(load_config().threshold("RUN_GUIDE_SHAPE_MIN_SESSION"))


def _episode_session(rel: str) -> int | None:
    match = _EPISODE_DIR_RE.match(rel)
    return int(match.group(1)) if match else None


def _in_scope(rel: str) -> bool:
    session = _episode_session(rel)
    return session is not None and session >= _min_session()


def _sections(body: str) -> list[tuple[str, str]]:
    lines = body.splitlines()
    current = ""
    chunks: list[str] = []
    out: list[tuple[str, str]] = []
    for line in lines:
        match = _H2_RE.match(line)
        if match:
            if current:
                out.append((current, "\n".join(chunks)))
            current = match.group(1).strip()
            chunks = []
            continue
        if current:
            chunks.append(line)
    if current:
        out.append((current, "\n".join(chunks)))
    return out


def _play_text(body: str) -> str:
    return "\n".join(
        text for name, text in _sections(body) if name not in _RESERVED_H2
    )


def _link_only_text(body: str) -> str:
    return "\n".join(
        text for name, text in _sections(body) if name in _LINK_ONLY_H2
    )


def _basenames(pattern: re.Pattern[str], text: str) -> set[str]:
    return {match.group(1).strip().rsplit("/", 1)[-1] for match in pattern.finditer(text)}


def _coverage_slug(slug: str) -> str:
    """A `…-narration-open` embed covers its parent moment/situation slug."""
    for marker in _PERFORMATIVE_MARKERS:
        if marker in slug:
            return slug.split(marker, 1)[0]
    return slug


def _expected_pad(session: int) -> str:
    return f"{session:02d}"


def _episode_run_guides(corpus: Corpus, directory: str) -> list[Page]:
    return [
        page
        for page in corpus.pages()
        if page.rel_path.startswith(f"{directory}/")
        and page.frontmatter.get("subtype") == "run-guide"
        and page.rel_path.count("/") == directory.count("/") + 1
    ]


@register
class RunGuideBasenameAndPlanRule(FileRule):
    """W140 — overview basename + session_shape; episode run-guide slug."""

    id = "W140"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Name the overview eNN-overview.md and set session_shape: to one of "
        "the nine session shapes. Name each episode run-guide "
        "eNN-run-guide-<slug>.md."
    )
    producer = "wiki"
    pure = True
    version = "4"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not _in_scope(rel):
            return
        session = _episode_session(rel)
        if session is None:
            return
        subtype = page.frontmatter.get("subtype")
        basename = rel.rsplit("/", 1)[-1]
        pad = _expected_pad(session)

        if subtype == "run-guide":
            match = _E_GUIDE_RE.match(basename)
            if match is None or int(match.group(1)) != session:
                yield self.finding(
                    file=rel,
                    line=page.body_start_line,
                    message=(
                        f'subtype: run-guide page is named "{basename}" — '
                        f'write it as "e{pad}-run-guide-<slug>.md" so the '
                        f"stretch slug is unique ({_SOURCE})"
                    ),
                )
            return

        if subtype == "overview":
            expected = f"e{pad}-overview.md"
            if basename != expected:
                yield self.finding(
                    file=rel,
                    line=page.body_start_line,
                    message=(
                        f'subtype: overview page is named "{basename}" — '
                        f'write it as "{expected}" ({_OVERVIEW_SOURCE})'
                    ),
                )
            shape = page.frontmatter.get("session_shape")
            shape_text = shape.strip() if isinstance(shape, str) else ""
            if not shape_text:
                yield self.finding(
                    file=rel,
                    line=1,
                    message=(
                        "subtype: overview page has no session_shape: — "
                        "set it to one of crossing, site, town, intrigue, "
                        f"investigation, set-piece, hunt, downtime, climax "
                        f"({_OVERVIEW_SOURCE})"
                    ),
                )
            elif shape_text not in _SESSION_SHAPES:
                yield self.finding(
                    file=rel,
                    line=1,
                    message=(
                        f'session_shape: "{shape_text}" is not a session shape — '
                        "use crossing, site, town, intrigue, investigation, "
                        f"set-piece, hunt, downtime, or climax ({_OVERVIEW_SOURCE})"
                    ),
                )
            return

        if subtype == "index":
            yield self.finding(
                file=rel,
                line=page.body_start_line,
                message=(
                    'subtype: index is retired — write eNN-overview.md '
                    f"(subtype: overview) ({_OVERVIEW_SOURCE})"
                ),
            )


@register
class RunGuideCoverageRule(FileRule):
    """W141 — each episode frame is on a walk or linked from Exit."""

    id = "W141"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.ERROR
    fix = (
        "Write numbered play H2s that transclude each beat page whole "
        "(![[beat-...]]) in play order. Wikilink Side-tracks and Exit "
        f"({_SOURCE})."
    )
    producer = "wiki"
    pure = False
    version = "8"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not _in_scope(rel):
            return
        if page.frontmatter.get("subtype") != "run-guide":
            return
        basename = rel.rsplit("/", 1)[-1]
        if _E_GUIDE_RE.match(basename) is None:
            return

        elsewhere = _link_only_text(page.body)
        if _basenames(_EMBED_RE, elsewhere):
            yield self.finding(
                file=rel,
                line=page.body_start_line,
                message=(
                    "## Side-tracks or ## Exit contains a transclusion — "
                    f"wikilink other paths ({_SOURCE})"
                ),
            )

        directory = rel.rsplit("/", 1)[0]
        guides = _episode_run_guides(corpus, directory)
        if not guides:
            guides = [page]
        first = min(guides, key=lambda item: item.rel_path)
        if rel != first.rel_path:
            return

        covered: set[str] = set()
        for guide in guides:
            play = _play_text(guide.body)
            links = _link_only_text(guide.body)
            covered |= {_coverage_slug(slug) for slug in _basenames(_EMBED_RE, play)}
            covered |= {_coverage_slug(slug) for slug in _basenames(_LINK_RE, play)}
            covered |= _basenames(_LINK_RE, links)

        for sibling in corpus.pages():
            if not sibling.rel_path.startswith(f"{directory}/"):
                continue
            if sibling.frontmatter.get("subtype") == "run-guide":
                continue
            slug = sibling.slug
            if sibling.type != "beat":
                continue
            if slug not in covered:
                yield self.finding(
                    file=rel,
                    line=page.body_start_line,
                    message=(
                        f"beat [[{slug}]] is on no episode run-guide walk "
                        f"or Exit ({_SOURCE})"
                    ),
                )
