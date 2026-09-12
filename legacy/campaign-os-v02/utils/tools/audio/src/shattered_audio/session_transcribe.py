"""Transcribe a multi-mic session recording into one continuous speaker CSV.

Consumes what :mod:`shattered_audio.record` produces — one isolated FLAC track
per microphone (m4a for legacy sessions), chunked into time-aligned parts for
crash-safety — and emits a
single whole-session transcript the ``session-ingest`` skill consumes::

    .raw/sessions/session-07/transcripts/raw/session-07.csv  (ID,Start,End,Speaker,Text)

Each mic's parts are losslessly concatenated (ffmpeg stream copy) back into one
continuous track before transcription, so no utterance is ever cut at a
recording-segment boundary. We transcribe each mic's full track, label every
utterance by which mic it came from (the mic is a strong speaker prior — the
DM's mic is the DM), refine the label with voice profiles when available, then
merge all mics into one time-ordered CSV.

Speaker attribution degrades gracefully:

1. **Voice profiles** (default, when enrolled) — :func:`identify_speaker_v2`
   turns a mic's audio into an actor or character-voice name.
2. **Mic prior** — the ``speaker`` recorded in the manifest for that mic.
3. **Stable label** — ``"Speaker mic01"`` so ``session-ingest`` can resolve it.

pyannote diarization is layered in only when ``HF_TOKEN`` is set; it splits
turns *within* a single mic (useful when two people share one mic). Without it,
each mic chunk is treated as one speaker stream — which is exactly right for the
common one-person-per-mic setup.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path

from .record import mic_dir_name

logger = logging.getLogger(__name__)

PART_CSV_FIELDS = ["ID", "Start", "End", "Speaker", "Text"]


@dataclass
class MicTrack:
    mic_id: str
    speaker: str | None
    parts: list[Path] = field(default_factory=list)


@dataclass
class Utterance:
    start: float
    end: float
    speaker: str
    text: str
    mic_id: str = ""
    engine_speaker_id: str = ""


def fmt_timestamp(seconds: float) -> str:
    """Format seconds as SRT-style ``HH:MM:SS,mmm`` (transcribeX CSV format)."""
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _mic_parts(audio: Path, mic_dir: str) -> list[Path]:
    """Raw parts for one mic dir — FLAC (current capture) or m4a (legacy).

    Raw is the only transcription source: it is the full-fidelity capture
    (48 kHz FLAC), and every engine resamples to its own rate anyway.
    """
    raw_dir = audio / "raw" / mic_dir
    for pattern in ("*.flac", "*.m4a"):
        parts = sorted(raw_dir.glob(pattern), key=lambda p: p.name)
        if parts:
            return parts
    return []


def discover_tracks(session_dir: Path) -> list[MicTrack]:
    """Find a session's raw mic tracks, honoring manifest.json if present.

    ``session_dir`` is the session packet root (``.raw/sessions/session-NN/``).
    Capture artifacts live under its ``audio/`` subdir: ``audio/manifest.json``
    and per-mic raw tracks under ``audio/raw/dm-mic/`` and
    ``audio/raw/player-mic/`` (see ``record.mic_dir_name``); any pre-split
    transcribe-ready parts under ``audio/parts/`` are the no-manifest fallback.
    """
    audio = session_dir / "audio"
    manifest_path = audio / "manifest.json"
    raw = audio / "raw"

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        tracks: list[MicTrack] = []
        for m in manifest.get("mics", []):
            mic_id = m["mic_id"]
            # The manifest keeps the positional id (mic00); on disk the raw
            # dir is role-named (dm-mic, player-mic), matching record.raw_mic_dir.
            parts = _mic_parts(audio, mic_dir_name(mic_id))
            tracks.append(MicTrack(mic_id=mic_id, speaker=m.get("speaker"), parts=parts))
        return tracks

    # No manifest: treat per-mic subdirs if present, else loose parts as one mic.
    if raw.is_dir():
        tracks = []
        for mic_dir in sorted(p for p in raw.iterdir() if p.is_dir()):
            parts = _mic_parts(audio, mic_dir.name)
            if parts:
                tracks.append(MicTrack(mic_id=mic_dir.name, speaker=None, parts=parts))
        if tracks:
            return tracks

    loose = sorted(
        [*(audio / "parts").glob("*.flac"), *(audio / "parts").glob("*.m4a")],
        key=lambda p: p.name,
    )
    if loose:
        return [MicTrack(mic_id="mic00", speaker=None, parts=loose)]
    return []


def concat_track_parts(parts: list[Path], out_path: Path, *, ffmpeg: str = "ffmpeg") -> Path:
    """Losslessly rejoin one mic's recording segments into one continuous file.

    Recording segments come from one encode split at packet boundaries
    (``record.py``'s segment muxer with ``reset_timestamps``), so the concat
    demuxer with stream copy restores the exact original stream — no re-encode,
    no boundary loss. A single part is returned as-is.
    """
    import subprocess

    from .export import write_concat_list

    if len(parts) == 1:
        return parts[0]
    list_path = out_path.with_suffix(".concat.txt")
    write_concat_list(parts, list_path)
    cmd = [
        ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", str(list_path),
        "-c", "copy", str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"ffmpeg concat failed (exit {proc.returncode}): {proc.stderr.strip()[-500:]}"
        )
    return out_path


def resolve_speaker(match: str | None, prior: str | None, mic_id: str) -> str:
    """Pick the best available speaker label for an utterance."""
    if match:
        return match
    if prior:
        return prior
    return f"Speaker {mic_id}"


def resolve_engine_speaker_ids(utterances: list[Utterance], resolved: set[int]) -> None:
    """Backfill speaker labels via majority vote over an engine's own diarization, in place.

    Some engines (e.g. ElevenLabs Scribe) tag each utterance with their own
    ``engine_speaker_id`` from server-side diarization, independent of our
    per-utterance voice-profile embedding match. When most utterances sharing
    a ``(mic_id, engine_speaker_id)`` pairing were confidently identified by
    the embedding pass, apply that majority actor to the other utterances on
    the same pairing the embedding pass could not resolve (too short a
    segment, no profile enrolled, below threshold).

    ``resolved`` holds the indices into ``utterances`` the embedding pass
    confidently resolved (i.e. had a real profile ``match``, not a mic-prior
    or ``"Speaker <mic_id>"`` fallback) — passed in from the call site rather
    than inferred from ``speaker`` text, since a fallback label can coincide
    with a real actor name and can't be told apart from a true match by
    string alone.

    Ties (no single majority actor) are left untouched. No-op when no
    utterance carries an ``engine_speaker_id`` — whisper/parakeet sessions
    never populate it, so this never runs for them.
    """
    if not any(u.engine_speaker_id for u in utterances):
        return

    from collections import Counter

    votes: dict[tuple[str, str], Counter] = {}
    for i, u in enumerate(utterances):
        if i in resolved and u.engine_speaker_id:
            key = (u.mic_id, u.engine_speaker_id)
            votes.setdefault(key, Counter())[u.speaker] += 1

    for i, u in enumerate(utterances):
        if i in resolved or not u.engine_speaker_id:
            continue
        counter = votes.get((u.mic_id, u.engine_speaker_id))
        if not counter:
            continue
        ranked = counter.most_common(2)
        top_actor, top_count = ranked[0]
        if len(ranked) > 1 and ranked[1][1] == top_count:
            continue  # tie — leave as-is
        u.speaker = top_actor


# Cross-mic ghost dedup. Each room mic acoustically picks up the other side's
# loud speech (bleed), so whisper emits a copy of it on the mic that didn't
# own it — usually fragmented and garbled ("reflux"
# under "refits"). Audio-level signals cannot arbitrate a pair (channel gains
# differ and the room mic's reference level is itself dominated by bleed;
# whisper's avg_logprob is per-30s-window, not per-segment), so the rule is
# textual: a cross-mic pair overlapping in time whose normalized texts nearly
# contain one another is one physical utterance transcribed twice — keep the
# side with more words (ghosts fragment), breaking word-count ties toward the
# close DM mic (in every observed near-dup pair the close mic had the accurate
# rendering: "refits" over "reflux", "Officer Fink" over "officer something").
# A real simultaneous speaker says *different* words, so similarity stays low
# and nothing is dropped. Containment counts whole matched words in sequence
# (char-level matching inflates on short lines — "Yep, been there." scored
# 0.79 against an unrelated long line); a short echoed reaction ("Well,
# shit-faced" under a longer line containing the word) measures 0.5.
GHOST_SIMILARITY = 0.7  # matched fraction of the shorter text's words
GHOST_MIN_OVERLAP = 0.5  # fraction of the shorter utterance's duration


def _norm_words(text: str) -> str:
    return " ".join("".join(c for c in w if c.isalnum()) for w in text.lower().split())


def _dm_priority(mic_id: str) -> int:
    """0 for the close DM mic (mic00 / dm-mic), 1 for any other mic."""
    return 0 if mic_id in ("mic00", "dm-mic") else 1


def _containment(a: str, b: str) -> float:
    """Fraction of the shorter text's words the longer one contains, in order."""
    from difflib import SequenceMatcher

    wa, wb = a.split(), b.split()
    if not wa or not wb:
        return 0.0
    matched = sum(m.size for m in SequenceMatcher(None, wa, wb).get_matching_blocks())
    return matched / min(len(wa), len(wb))


def drop_cross_mic_ghosts(
    utterances: list[Utterance],
    *,
    similarity: float = GHOST_SIMILARITY,
    log=None,
) -> list[Utterance]:
    """Remove cross-mic duplicates of one physical utterance; order preserved."""
    ghosts: set[int] = set()
    order = sorted(range(len(utterances)), key=lambda i: utterances[i].start)
    for oi, i in enumerate(order):
        if i in ghosts:
            continue
        a = utterances[i]
        for j in order[oi + 1 :]:
            b = utterances[j]
            if b.start >= a.end:
                break
            if a.mic_id == b.mic_id or j in ghosts:
                continue
            overlap = min(a.end, b.end) - b.start
            shorter = max(min(a.end - a.start, b.end - b.start), 1e-6)
            if overlap / shorter < GHOST_MIN_OVERLAP:
                continue
            na, nb = _norm_words(a.text), _norm_words(b.text)
            if _containment(na, nb) < similarity:
                continue
            # One utterance, two renderings: fewer words = the ghost fragment;
            # word-count tie goes to the close mic's rendering.
            wa, wb = len(na.split()), len(nb.split())
            if wa != wb:
                loser = i if wa < wb else j
            else:
                loser = j if _dm_priority(a.mic_id) <= _dm_priority(b.mic_id) else i
            ghost = utterances[loser]
            keeper = b if loser == i else a
            ghosts.add(loser)
            if log:
                log(
                    f"ghost dropped [{ghost.mic_id} {ghost.start:.1f}s] "
                    f"{ghost.text.strip()!r} (dup of {keeper.mic_id} "
                    f"{keeper.text.strip()!r})"
                )
            if loser == i:
                break

    return [u for k, u in enumerate(utterances) if k not in ghosts]


def load_scene_markers(session_dir: Path) -> list[dict]:
    """Scene markers for a session, sorted by ``t_offset_s``.

    Reads the finalized ``audio/markers.json`` (written by the recorder on
    stop), falling back to the append log ``audio/markers.jsonl`` when the
    recorder died before finalizing. ``event`` sentinel lines
    (recording-started/-ended) are dropped — only scene markers remain.
    Missing/empty files return ``[]`` so marker-less (legacy, single-take)
    sessions transcribe exactly as before.
    """
    audio = session_dir / "audio"
    markers: list[dict] = []
    final = audio / "markers.json"
    jsonl = audio / "markers.jsonl"
    if final.exists():
        try:
            markers = json.loads(final.read_text(encoding="utf-8")).get("markers", [])
        except (json.JSONDecodeError, AttributeError):
            logger.warning("Unreadable %s — falling back to markers.jsonl", final)
            markers = []
    if not markers and jsonl.exists():
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                markers.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    scenes = [m for m in markers if "event" not in m]
    scenes.sort(key=lambda m: m.get("t_offset_s", 0.0))
    return scenes


def scene_display(marker: dict) -> str:
    """Human/interface label for one scene marker: ``Scene NN — <label>``."""
    number = marker.get("scene_number")
    label = marker.get("label") or marker.get("scene_slug") or ""
    prefix = f"Scene {int(number):02d}" if number is not None else "Scene"
    return f"{prefix} — {label}" if label else prefix


def assign_scene(start_s: float, scenes: list[dict]) -> str:
    """Scene display label for an utterance starting at ``start_s`` seconds.

    The active scene is the last marker at or before the utterance's start;
    anything before the first marker is the pre-session segment.
    """
    current = "Pre-session"
    for marker in scenes:
        if marker.get("t_offset_s", 0.0) <= start_s:
            current = scene_display(marker)
        else:
            break
    return current


def merge_part_utterances(
    utterances: list[Utterance], markers: list[dict] | None = None
) -> list[dict]:
    """Sort utterances across mics into one numbered, timestamped CSV row list.

    With ``markers`` (scene markers from :func:`load_scene_markers`), each row
    additionally carries a ``Scene`` label; without them the row shape is the
    unchanged 5-field contract.
    """
    kept = [u for u in utterances if u.text.strip()]
    kept.sort(key=lambda u: (u.start, u.speaker))
    rows = []
    for i, u in enumerate(kept, start=1):
        row = {
            "ID": i,
            "Start": fmt_timestamp(u.start),
            "End": fmt_timestamp(u.end),
            "Speaker": u.speaker,
            "Text": u.text.strip(),
        }
        if markers:
            row["Scene"] = assign_scene(u.start, markers)
        rows.append(row)
    return rows


def _quote_csv_field(value: str) -> str:
    return '"' + str(value).replace('"', '""') + '"'


def apply_speaker_map(rows: list[dict], mapping: dict[str, str]) -> list[dict]:
    """Replace player names with character names, in place — labels and text.

    ``Speaker`` labels map on exact match; ``Text`` mentions map on
    case-sensitive whole words (transcription capitalizes names, and a
    lowercase collision like the verb "nick" must not match). Keeps player
    names out of wiki content — they live only on their pcs/players/ pages.
    """
    if not mapping:
        return rows
    import re

    pattern = re.compile(
        r"\b(" + "|".join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)) + r")\b"
    )
    for row in rows:
        row["Speaker"] = mapping.get(row["Speaker"], row["Speaker"])
        row["Text"] = pattern.sub(lambda m: mapping[m.group(0)], row["Text"])
    return rows


def write_part_csv(rows: list[dict], out_path: Path) -> None:
    """Write rows in the transcribeX CSV shape: bare ID/Speaker, quoted timestamps + text.

    transcribeX leaves its ``HH:MM:SS,mmm`` timestamps unquoted, which no CSV
    parser can round-trip (the millisecond comma splits the field) — so
    timestamps and text are always quoted here; assemble.py and laughs.py read
    the result with a plain ``csv.DictReader``.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Scene column is additive: present only when rows carry scene markers, so
    # marker-less sessions keep the exact 5-column transcribeX shape.
    with_scene = any("Scene" in row for row in rows)
    fields = [*PART_CSV_FIELDS, "Scene"] if with_scene else PART_CSV_FIELDS
    lines = [",".join(fields)]
    for row in rows:
        speaker = str(row["Speaker"])
        if any(c in speaker for c in ',"\n'):
            speaker = _quote_csv_field(speaker)
        line = (
            f"{row['ID']},{_quote_csv_field(row['Start'])},{_quote_csv_field(row['End'])},"
            f"{speaker},{_quote_csv_field(row['Text'])}"
        )
        if with_scene:
            line += f",{_quote_csv_field(row.get('Scene', ''))}"
        lines.append(line)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Audio + model glue (kept behind small functions so tests can stay light)
# ---------------------------------------------------------------------------


def _load_samples(path: Path, sample_rate: int = 16000):
    """Load an audio file as mono float32 at ``sample_rate`` (resemblyzer-ready)."""
    import numpy as np
    from pydub import AudioSegment

    seg = AudioSegment.from_file(str(path)).set_channels(1).set_frame_rate(sample_rate)
    seg = seg.set_sample_width(2)
    return np.array(seg.get_array_of_samples(), dtype=np.float32) / 32768.0


def _chunk_progress_logger(log):
    """Build a parakeet ``chunk_callback`` that echoes progress every ~25%.

    Kept low-noise: one line per quartile (plus completion), not per chunk.
    """
    last_reported = [-1.0]

    def _cb(current: float, total: float) -> None:
        if not total:
            return
        pct = current / total
        if pct - last_reported[0] >= 0.25 or current >= total:
            last_reported[0] = pct
            log(f"  … {current:.0f}/{total:.0f} s")

    return _cb


def _transcribe_part(
    path: Path,
    model: str | None,
    *,
    engine: str = "whisper",
    engine_kwargs: dict | None = None,
) -> list[Utterance]:
    from . import engines

    segments = engines.run(engine, path, model=model, **(engine_kwargs or {}))
    return [
        Utterance(
            start=s.start,
            end=s.end,
            speaker="",
            text=s.text,
            engine_speaker_id=s.engine_speaker_id or "",
        )
        for s in segments
    ]


def transcribe_session(
    session: int,
    audio_dir: Path,
    *,
    use_profiles: bool = True,
    profiles_dir: Path | None = None,
    model: str | None = "mlx-community/whisper-large-v3-mlx",
    engine: str = "whisper",
    engine_kwargs: dict | None = None,
    channel_boost: float = 0.15,
    actor_threshold: float = 0.7,
    persona_threshold: float = 0.6,
    persona_margin: float = 0.05,
    prosody_weight: float = 0.3,
    dedup: bool = True,
    speaker_map: dict[str, str] | None = None,
    formats: tuple[str, ...] = ("csv",),
    apply_autocorrect: bool = True,
    autocorrect_path: Path | None = None,
    log=None,
) -> list[Path]:
    """Transcribe a recorded session into one continuous speaker CSV.

    Each mic's recording segments are losslessly rejoined and transcribed as a
    single continuous track (see :func:`concat_track_parts`). Returns the CSV
    path written, as a one-element list (regardless of ``formats`` — extra
    formats are written as sibling files and logged, not returned). Voice
    profiles are loaded and applied by default; pass ``use_profiles=False`` to
    label purely by mic prior. Raw tracks are the transcription source. ``engine``
    selects the transcription engine (see :mod:`shattered_audio.engines`);
    ``engine_kwargs`` are forwarded to it verbatim. When ``apply_autocorrect``
    and ``autocorrect_path`` point at a dictionary CSV, corrections are applied
    to the rows before they're written; at least one applied correction gets a
    ``.autocorrect.jsonl`` sidecar next to the CSV.
    """
    log = log or logger.info
    from .autocorrect import apply_corrections, load_dictionary, write_autocorrect_log
    from .output_formats import write_all
    from .record import session_dir as _session_dir

    sdir = _session_dir(audio_dir, session)
    tracks = discover_tracks(sdir)
    if not tracks:
        raise FileNotFoundError(f"No mic tracks found under {sdir}")

    actors = {}
    if use_profiles:
        try:
            from .profiles import load_actor_profiles

            pdir = profiles_dir or (Path.home() / ".config" / "shattered-audio" / "profiles")
            actors = load_actor_profiles(pdir)
            if actors:
                log(f"Loaded {len(actors)} voice profile(s): {', '.join(a.name for a in actors.values())}")
            else:
                log("No voice profiles enrolled — labeling by mic prior")
        except Exception as e:  # resemblyzer / torch missing, etc.
            log(f"Voice profiles unavailable ({e}) — labeling by mic prior")
            actors = {}

    corrections = []
    if apply_autocorrect and autocorrect_path is not None:
        corrections = load_dictionary(autocorrect_path, log=log)
        if corrections:
            log(f"Autocorrect: loaded {len(corrections)} rule(s) from {autocorrect_path.name}")

    channel_priors = {t.mic_id: t.speaker for t in tracks if t.speaker}

    def identify(samples, mic_id: str) -> str | None:
        if not actors:
            return None
        try:
            from .profiles import identify_speaker_v2

            match = identify_speaker_v2(
                samples,
                actors,
                source_mic=mic_id,
                channel_priors=channel_priors,
                channel_boost=channel_boost,
                actor_threshold=actor_threshold,
                persona_threshold=persona_threshold,
                persona_margin=persona_margin,
                prosody_weight=prosody_weight,
            )
            return match.name if match else None
        except Exception:
            logger.debug("identify_speaker_v2 failed", exc_info=True)
            return None

    import tempfile

    utterances: list[Utterance] = []
    resolved_indices: set[int] = set()
    with tempfile.TemporaryDirectory(prefix="shattered-transcribe-") as td:
        for pos, track in enumerate(tracks, start=1):
            track_start = time.monotonic()
            # One continuous file per mic — no per-segment transcription, so
            # no utterance is cut at a recording-chunk boundary.
            track_path = concat_track_parts(
                track.parts,
                Path(td) / f"{track.mic_id}{track.parts[0].suffix}",
            )
            log(
                f"Transcribing mic {pos:02d}/{len(tracks):02d} · {track.mic_id} "
                f"({len(track.parts)} segment(s), continuous)"
            )
            samples = None
            track_engine_kwargs = dict(engine_kwargs or {})
            if engine == "parakeet-v3":
                track_engine_kwargs["progress"] = _chunk_progress_logger(log)
            for utt in _transcribe_part(track_path, model, engine=engine, engine_kwargs=track_engine_kwargs):
                match = None
                if actors:
                    if samples is None:
                        samples = _load_samples(track_path)
                    seg_audio = _slice(samples, utt.start, utt.end)
                    if seg_audio is not None and len(seg_audio) > 0:
                        match = identify(seg_audio, track.mic_id)
                utt.mic_id = track.mic_id
                utt.speaker = resolve_speaker(match, track.speaker, track.mic_id)
                if match:
                    resolved_indices.add(len(utterances))
                utterances.append(utt)
            log(f"  {time.monotonic() - track_start:.0f}s elapsed")

    resolve_engine_speaker_ids(utterances, resolved_indices)

    if dedup and len(tracks) > 1:
        before = len(utterances)
        utterances = drop_cross_mic_ghosts(utterances, log=log)
        if len(utterances) < before:
            log(f"Dedup: dropped {before - len(utterances)} cross-mic ghost line(s)")

    scenes = load_scene_markers(sdir)
    if scenes:
        log(f"Scene markers: {len(scenes)} scene(s) — tagging utterances")
    rows = merge_part_utterances(utterances, markers=scenes)
    if speaker_map:
        rows = apply_speaker_map(rows, speaker_map)
        log(f"Speaker map: {len(speaker_map)} player name(s) replaced with character names")
    stem = f"session-{session:02d}"
    out_dir = sdir / "transcripts" / "raw"

    if corrections:
        rows, applied = apply_corrections(rows, corrections)
        if applied:
            sidecar = out_dir / f"{stem}.autocorrect.jsonl"
            write_autocorrect_log(applied, sidecar)
            log(f"Autocorrect: applied {len(applied)} correction(s) → {sidecar.name}")

    # CSV is always written (regression-critical: tests depend on the
    # CSV-paths-only return contract), regardless of whether the caller
    # included "csv" in `formats`.
    fmt_list = tuple(formats) if "csv" in formats else ("csv", *formats)
    out_paths = write_all(rows, out_dir, stem, fmt_list)
    out = out_paths["csv"]
    log(f"Wrote {len(rows)} line(s) → {out.name}")
    for fmt in fmt_list:
        if fmt != "csv":
            log(f"Wrote {fmt} → {out_paths[fmt].name}")

    return [out]


def _slice(samples, start: float, end: float, sample_rate: int = 16000):
    """Slice [start, end] seconds out of a mono sample array."""
    a = max(0, int(start * sample_rate))
    b = min(len(samples), int(end * sample_rate))
    if b <= a:
        return None
    return samples[a:b]
