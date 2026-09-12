"""Export a session's per-mic tracks as one playback audio file.

The pipeline's durable artifacts are per-mic raw part series (48 kHz FLAC;
m4a in legacy sessions). For humans that's unlistenable — this module concats
each mic's raw parts and joins the mics into a single stereo m4a for playback:
dm-mic on the left channel, player-mic on the right. Track separation
survives (pan your player to hear one mic), and the file drops next to the
manifest so Obsidian/Finder can play the whole session in one click.
Both channels come from the same raw tier (``discover_tracks``).
"""

from __future__ import annotations

import logging
import subprocess
import tempfile
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_EXPORT_BITRATE = "192k"

# join filter channel placement per mic count: mic00 (dm) left, mic01
# (player) right — matching _MIC_ROLE_DIR_NAMES's table roles.
_STEREO_MAP = "0.0-FL|1.0-FR"


def write_concat_list(parts: list[Path], list_path: Path) -> Path:
    """Write an ffmpeg concat-demuxer list file for one mic's parts.

    ``file`` lines use absolute paths so the list works from any cwd
    (concat demuxer resolves relative paths against the list file's dir,
    which is a tempdir here). Quotes are escaped per the demuxer's rules.
    """
    lines = []
    for p in parts:
        escaped = str(p.resolve()).replace("'", "'\\''")
        lines.append(f"file '{escaped}'")
    list_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return list_path


def build_export_command(
    list_files: list[Path],
    out_path: Path,
    bitrate: str = DEFAULT_EXPORT_BITRATE,
    ffmpeg: str = "ffmpeg",
    segment_seconds: int | None = None,
) -> list[str]:
    """Build the ffmpeg argv: N concat inputs → one playback file.

    Two mics join into stereo (dm-mic=left, player-mic=right); one mic
    passes through as mono. More than two mics is not a playback layout
    this rig produces — callers reject it before building.
    ``segment_seconds`` switches the output to the segment muxer —
    ``out_path`` must then be a ``part-%03d.m4a``-style pattern.
    """
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "warning", "-y"]
    for lf in list_files:
        cmd += ["-f", "concat", "-safe", "0", "-i", str(lf)]
    if len(list_files) == 2:
        cmd += [
            "-filter_complex",
            f"[0:a][1:a]join=inputs=2:channel_layout=stereo:map={_STEREO_MAP}[a]",
            "-map",
            "[a]",
        ]
    cmd += ["-c:a", "aac", "-b:a", bitrate]
    if segment_seconds is not None:
        cmd += [
            "-f",
            "segment",
            "-segment_time",
            str(segment_seconds),
            "-reset_timestamps",
            "1",
        ]
    cmd.append(str(out_path))
    return cmd


def export_session(
    session_dir: Path,
    out_path: Path | None = None,
    *,
    bitrate: str = DEFAULT_EXPORT_BITRATE,
    ffmpeg: str = "ffmpeg",
    segment_minutes: int | None = None,
) -> Path:
    """Concat + join a session's mic tracks into one playback m4a.

    ``segment_minutes`` chunks the export into ``part-NNN.m4a`` files under
    an ``audio/playback/`` dir instead of one long file (``out_path`` then
    names the pattern and its parent dir is returned).

    Raises ``FileNotFoundError`` when the session has no audio parts and
    ``ValueError`` for track counts with no playback layout (3+ mics).
    """
    from .session_transcribe import discover_tracks

    tracks = [t for t in discover_tracks(session_dir) if t.parts]
    if not tracks:
        raise FileNotFoundError(f"No audio parts found under {session_dir}/audio")
    if len(tracks) > 2:
        raise ValueError(
            f"export needs 1 or 2 mic tracks for a playback layout, got {len(tracks)}"
        )

    if out_path is None:
        if segment_minutes is not None:
            out_path = session_dir / "audio" / "playback" / "part-%03d.m4a"
        else:
            out_path = session_dir / "audio" / f"{session_dir.name}-playback.m4a"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="shattered-export-") as td:
        list_files = [
            write_concat_list(t.parts, Path(td) / f"concat-{i}.txt")
            for i, t in enumerate(tracks)
        ]
        cmd = build_export_command(
            list_files,
            out_path,
            bitrate=bitrate,
            ffmpeg=ffmpeg,
            segment_seconds=segment_minutes * 60 if segment_minutes else None,
        )
        logger.info(
            "Exporting %s (%s) → %s",
            ", ".join(t.mic_id for t in tracks),
            "stereo dm=L player=R" if len(tracks) == 2 else "mono",
            out_path,
        )
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(
                f"ffmpeg export failed (exit {proc.returncode}): {proc.stderr.strip()[-500:]}"
            )
    return out_path.parent if segment_minutes is not None else out_path
