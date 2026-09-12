"""Multi-microphone session recorder built on ffmpeg + avfoundation.

One ffmpeg process per microphone, each writing a segmented (chunked) FLAC
track. Recording each mic to its own track keeps the DM and players physically
isolated, which the transcribe step exploits for far better speaker separation
than a single mixed feed.

Why ffmpeg instead of a long-running Python audio loop: a 4+ hour D&D session
needs a recorder that does not drift, leak, or die. ffmpeg's segment muxer is
battle-tested for exactly this — it flushes each chunk to disk as it goes, so a
crash at hour 3 still leaves you hours 0-3 of finalized audio.

Output layout (under ``.raw/sessions/``)::

    session-07/
      audio/
        manifest.json
        markers.jsonl   (scene markers, appended live; markers.json on stop)
        raw/
          dm-mic/ part-000.flac part-001.flac ...
          player-mic/ part-000.flac part-001.flac ...

The pure helpers here (device parsing, command building, mic selection, path
layout, manifest) are unit-tested; :func:`record_session` does the process
orchestration and is exercised by a short real-capture integration test.
"""

from __future__ import annotations

import json
import logging
import re
import signal
import subprocess
import threading
import time
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

SAMPLE_RATE = 16000  # transcription/clean rate — NOT the capture rate
# Capture is lossless FLAC at the hardware-native 48 kHz: lossy AAC measurably
# hurts ASR/diarization accuracy, and every downstream stage resamples to its
# own rate anyway. highpass strips sub-speech rumble/handling noise only —
# denoise is deliberately absent at every stage (it degrades Whisper
# WER and speaker embeddings); raw is what gets transcribed.
CAPTURE_SAMPLE_RATE = 48000
CAPTURE_EXT = "flac"
HIGHPASS_HZ = 80
DEFAULT_SEGMENT_MINUTES = 15
# Device-presence watchdog: poll cadence and consecutive misses required
# before we conclude a mic is really gone (one miss can be an enumeration
# hiccup, not an unplug). The startup grace matters: opening the aggregate
# device wakes a sleeping USB mic, which can briefly drop off the
# avfoundation list while it re-enumerates (observed on the EMEET) — the
# strict pre-flight already proved presence, so early polls prove nothing.
WATCHDOG_POLL_SECONDS = 5.0
WATCHDOG_MISSES_TO_STOP = 3
WATCHDOG_GRACE_SECONDS = 30.0

# Matches `[AVFoundation indev @ 0x...] [1] EMEET OfficeCore M0 Plus`
_DEVICE_LINE = re.compile(r"\[AVFoundation indev[^\]]*\]\s*\[(\d+)\]\s*(.+?)\s*$")
_AUDIO_HEADER = re.compile(r"AVFoundation audio devices:")
_VIDEO_HEADER = re.compile(r"AVFoundation video devices:")


@dataclass
class RecordMic:
    """A microphone selected for recording.

    ``index`` is the avfoundation audio-device index (what ffmpeg's ``-i``
    needs). ``mic_id`` is positional within the selection (mic00, mic01, ...)
    and is what shows up in the output path and manifest.
    """

    index: int
    name: str
    mic_id: str
    speaker: str | None = None
    channels: int = 1
    # Aggregate capture only: 0-based channel of the aggregate device this
    # mic's audio lives on (ffmpeg pan ``c<n>`` numbering). None = the mic is
    # its own avfoundation device (per-mic capture).
    channel: int | None = None


def parse_avfoundation_devices(stderr: str) -> list[dict]:
    """Parse audio input devices from ffmpeg's ``-list_devices`` stderr.

    ffmpeg prints video devices and audio devices under separate headers, each
    using ``[N]`` indices that restart at 0. We only want the audio block.
    """
    devices: list[dict] = []
    in_audio = False
    for line in stderr.splitlines():
        if _AUDIO_HEADER.search(line):
            in_audio = True
            continue
        if _VIDEO_HEADER.search(line):
            in_audio = False
            continue
        if not in_audio:
            continue
        m = _DEVICE_LINE.search(line)
        if m:
            devices.append({"index": int(m.group(1)), "name": m.group(2)})
    return devices


def list_avfoundation_devices(ffmpeg: str = "ffmpeg") -> list[dict]:
    """Query the OS for avfoundation audio input devices."""
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-f", "avfoundation", "-list_devices", "true", "-i", ""],
        capture_output=True,
        text=True,
    )
    # ffmpeg exits non-zero after listing (it has no real input) — that's normal.
    return parse_avfoundation_devices(proc.stderr)


def select_mics(
    devices: list[dict],
    indices: list[int] | None = None,
    names: list[str] | None = None,
) -> list[RecordMic]:
    """Choose which devices to record.

    Priority: explicit ``indices`` → ``names`` substring match → all devices.
    Unknown indices and unmatched names are skipped (a warning, not a crash).
    """
    by_index = {d["index"]: d for d in devices}

    chosen: list[dict] = []
    if indices is not None:
        for idx in indices:
            if idx in by_index:
                chosen.append(by_index[idx])
            else:
                logger.warning("Requested mic index %s not found — skipping", idx)
    elif names:
        for name in names:
            name_lower = name.lower()
            match = next(
                (d for d in devices if name_lower in d["name"].lower() and d not in chosen),
                None,
            )
            if match:
                chosen.append(match)
            else:
                logger.warning("No mic matching %r — skipping", name)
    else:
        chosen = list(devices)

    return [
        RecordMic(index=d["index"], name=d["name"], mic_id=f"mic{i:02d}")
        for i, d in enumerate(chosen)
    ]


def select_aggregate_mics(
    devices: list[dict], aggregate: dict | None
) -> tuple[int, list[RecordMic]] | None:
    """Resolve aggregate-device capture from the ``aggregate:`` config block.

    ``aggregate`` shape (see config.yaml)::

        name: Aggregate Device        # avfoundation name substring
        mics:
          - {channel: 2, name: MacBook Air Microphone}   # mic00 → dm-mic
          - {channel: 0, name: EMEET OfficeCore M0 Plus} # mic01 → player-mic

    Entry order is positional (mic00 = DM first — same contract as
    :func:`select_mics`); ``channel`` is the 0-based aggregate channel the
    mic's audio lives on, ``name`` is a label for the manifest/logs. Returns
    ``(aggregate_device_index, mics)`` or ``None`` when the config block is
    absent/incomplete or no matching device is currently present — callers
    fall back to per-mic capture.
    """
    if not aggregate:
        return None
    mic_entries = aggregate.get("mics") or []
    if len(mic_entries) < 2:
        return None
    name = str(aggregate.get("name", "Aggregate Device")).lower()
    dev = next((d for d in devices if name in d["name"].lower()), None)
    if dev is None:
        logger.warning(
            "Aggregate device %r not present — falling back to per-mic capture",
            aggregate.get("name", "Aggregate Device"),
        )
        return None
    mics = [
        RecordMic(
            index=dev["index"],
            name=str(entry.get("name", f"aggregate channel {entry['channel']}")),
            mic_id=f"mic{i:02d}",
            channel=int(entry["channel"]),
        )
        for i, entry in enumerate(mic_entries)
    ]
    return dev["index"], mics


def session_dir(audio_dir: Path, session: int) -> Path:
    """Resolve the on-disk dir for a session number.

    Campaign OS session dirs are slugged (``sessions/06-show-them-the-rain/``),
    not bare numbers, so prefer an existing ``NN-slug`` (or legacy
    ``session-NN``) dir under audio_dir over inventing a new numeric one.
    """
    padded = f"{session:02d}"
    if audio_dir.is_dir():
        for entry in sorted(audio_dir.iterdir()):
            if entry.is_dir() and (
                entry.name == f"session-{padded}" or entry.name.startswith(f"{padded}-")
            ):
                return entry
    return audio_dir / f"session-{padded}"


# The standard 2-mic table rig: mic00 is always the DM's mic, mic01 the
# shared player mic (see select_mics — mic_id is positional). Any additional
# mic (3+ mic setups) falls back to index form.
_MIC_ROLE_DIR_NAMES = {0: "dm-mic", 1: "player-mic"}


def mic_dir_name(mic_id: str) -> str:
    """On-disk raw/ subdir name for a positional mic_id (mic00, mic01, ...)."""
    digits = "".join(ch for ch in mic_id if ch.isdigit())
    mic_index = int(digits) if digits else 0
    return _MIC_ROLE_DIR_NAMES.get(mic_index, f"mic-{mic_index:02d}")


def raw_mic_dir(audio_dir: Path, session: int, mic: RecordMic) -> Path:
    return session_dir(audio_dir, session) / "audio" / "raw" / mic_dir_name(mic.mic_id)


def build_ffmpeg_command(
    device_index: int,
    out_pattern: Path,
    segment_seconds: int,
    sample_rate: int = CAPTURE_SAMPLE_RATE,
    highpass_hz: int = HIGHPASS_HZ,
    ffmpeg: str = "ffmpeg",
    channels: int = 1,
) -> list[str]:
    """Build the ffmpeg argv for one mic: avfoundation in → segmented FLAC out.

    - ``-i :N`` selects avfoundation *audio* device N (the leading colon means
      "no video, audio index N").
    - downmix to mono, lossless FLAC at the capture rate — unless
      ``channels=2`` opts a mic into preserving both input channels (avfoundation
      has no input-side ``-ar``/``-ac``; this is purely an output-stage choice).
    - segment muxer with ``reset_timestamps`` so each chunk starts at t=0 and
      plays standalone; transcription rejoins the chunks losslessly with the
      concat demuxer before decoding (session_transcribe.concat_track_parts).
      Each FLAC segment is independently valid as written (no m4a moov-atom
      fragility), so a crash never truncates the in-progress chunk.
    """
    return [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "warning",
        "-f",
        "avfoundation",
        "-i",
        f":{device_index}",
        # A glitchy input device (USB drops) delivers fewer samples than wall
        # time; without gap-filling the stream ends up time-compressed and
        # misaligned against the other mic. async inserts silence at PTS gaps
        # so the recorded timeline always matches wall clock. The highpass
        # strips sub-speech rumble only — no capture-time denoise.
        "-af",
        f"aresample=async=1:first_pts=0,highpass=f={highpass_hz}",
        "-ac",
        str(channels),
        "-ar",
        str(sample_rate),
        "-c:a",
        "flac",
        "-f",
        "segment",
        "-segment_time",
        str(segment_seconds),
        "-reset_timestamps",
        "1",
        str(out_pattern),
    ]


def build_aggregate_ffmpeg_command(
    device_index: int,
    mics: list[RecordMic],
    out_patterns: list[Path],
    segment_seconds: int,
    sample_rate: int = CAPTURE_SAMPLE_RATE,
    highpass_hz: int = HIGHPASS_HZ,
    ffmpeg: str = "ffmpeg",
) -> list[str]:
    """Build the ffmpeg argv for aggregate capture: one multichannel
    avfoundation input → one segmented mono FLAC series per mic.

    A CoreAudio Aggregate Device gives every sub-device mic one shared clock,
    so the per-mic tracks are inherently sample-aligned — no inter-device
    drift, no chirp calibration needed. Each mic's channel (``RecordMic
    .channel``, 0-based) is panned to its own mono stream at capture time, so
    the on-disk layout and every downstream stage (clean/enhance/transcribe)
    are identical to per-mic capture. ``aresample=async=1`` still gap-fills
    USB glitches so the timeline matches wall clock.
    """
    cmd = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "warning",
        "-f",
        "avfoundation",
        "-i",
        f":{device_index}",
        "-filter_complex",
        ";".join(
            f"[0:a]pan=mono|c0=c{m.channel},"
            f"aresample=async=1:first_pts=0,highpass=f={highpass_hz}[m{i}]"
            for i, m in enumerate(mics)
        ),
    ]
    for i, pattern in enumerate(out_patterns):
        cmd += [
            "-map",
            f"[m{i}]",
            "-ar",
            str(sample_rate),
            "-c:a",
            "flac",
            "-f",
            "segment",
            "-segment_time",
            str(segment_seconds),
            "-reset_timestamps",
            "1",
            str(pattern),
        ]
    return cmd


def build_manifest(
    session: int,
    mics: list[RecordMic],
    segment_seconds: int,
    started_at: str | None = None,
    chirp_calibration: dict | None = None,
    capture: str = "per-mic",
    started_at_epoch: float | None = None,
    capture_sample_rate: int = CAPTURE_SAMPLE_RATE,
    strict: bool = False,
) -> dict:
    """Serializable description of the recording for the transcribe step.

    ``started_at_epoch`` is the audio-timeline zero: scene-marker offsets
    (``t_offset_s`` in markers.jsonl) are seconds since this instant.
    """
    manifest = {
        "session": session,
        "segment_seconds": segment_seconds,
        "sample_rate": SAMPLE_RATE,
        "capture_sample_rate": capture_sample_rate,
        "started_at": started_at,
        "started_at_epoch": started_at_epoch,
        "capture": capture,
        "strict": strict,
        "mics": [
            {
                "mic_id": m.mic_id,
                "index": m.index,
                "name": m.name,
                "speaker": m.speaker,
                "channels": m.channels,
                "channel": m.channel,
            }
            for m in mics
        ],
    }
    if chirp_calibration is not None:
        manifest["chirp_calibration"] = chirp_calibration
    return manifest


def verify_devices_present(
    devices: list[dict],
    expected_names: list[str],
) -> list[str]:
    """Return the expected device names with no case-insensitive substring
    match in ``devices`` — empty list means every expected mic is present.

    Used for the strict pre-flight check (session recording must not silently
    fall back to a degraded rig) and by the disconnect watchdog.
    """
    present = [d["name"].lower() for d in devices]
    return [
        name
        for name in expected_names
        if not any(name.lower() in p for p in present)
    ]


def _notify(title: str, message: str) -> None:
    """macOS notification so the DM hears about it mid-session; degrades to a
    log line anywhere osascript is unavailable."""
    script = (
        f'display notification "{message}" with title "{title}" sound name "Basso"'
    )
    try:
        subprocess.run(["osascript", "-e", script], capture_output=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        logger.warning("Notification fallback: %s — %s", title, message)


def markers_jsonl_path(audio_subdir: Path) -> Path:
    return audio_subdir / "markers.jsonl"


def append_marker(audio_subdir: Path, marker: dict) -> None:
    """Append one marker as a single NDJSON line (O_APPEND-atomic)."""
    with open(markers_jsonl_path(audio_subdir), "a", encoding="utf-8") as f:
        f.write(json.dumps(marker) + "\n")


def finalize_markers(audio_subdir: Path, session: int, started_at_epoch: float) -> None:
    """Fold markers.jsonl into the sorted ``markers.json`` artifact the
    transcribe step reads. Idempotent; keeps the .jsonl as the append log."""
    jsonl = markers_jsonl_path(audio_subdir)
    markers: list[dict] = []
    if jsonl.exists():
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                markers.append(json.loads(line))
            except json.JSONDecodeError:
                logger.warning("Skipping malformed marker line: %s", line[:200])
    markers.sort(key=lambda m: m.get("t_offset_s", 0.0))
    (audio_subdir / "markers.json").write_text(
        json.dumps(
            {
                "session": session,
                "started_at_epoch": started_at_epoch,
                "markers": markers,
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def _popen_ffmpeg(cmd: list[str]) -> subprocess.Popen:
    # stdin=PIPE lets us send 'q' for a clean ffmpeg shutdown that flushes and
    # closes the current segment (FLAC segments stay decodable even on a hard
    # kill, but a clean quit trims the tail properly).
    return subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )


def _spawn(
    mic: RecordMic,
    out_pattern: Path,
    segment_seconds: int,
    ffmpeg: str,
    sample_rate: int = CAPTURE_SAMPLE_RATE,
    highpass_hz: int = HIGHPASS_HZ,
) -> subprocess.Popen:
    out_pattern.parent.mkdir(parents=True, exist_ok=True)
    cmd = build_ffmpeg_command(
        mic.index, out_pattern, segment_seconds, sample_rate=sample_rate,
        highpass_hz=highpass_hz, ffmpeg=ffmpeg, channels=mic.channels,
    )
    logger.info("Recording %s (avfoundation :%s) → %s", mic.mic_id, mic.index, out_pattern.parent)
    return _popen_ffmpeg(cmd)


def _spawn_aggregate(
    device_index: int,
    mics: list[RecordMic],
    out_patterns: list[Path],
    segment_seconds: int,
    ffmpeg: str,
    sample_rate: int = CAPTURE_SAMPLE_RATE,
    highpass_hz: int = HIGHPASS_HZ,
) -> subprocess.Popen:
    for pattern in out_patterns:
        pattern.parent.mkdir(parents=True, exist_ok=True)
    cmd = build_aggregate_ffmpeg_command(
        device_index, mics, out_patterns, segment_seconds,
        sample_rate=sample_rate, highpass_hz=highpass_hz, ffmpeg=ffmpeg,
    )
    logger.info(
        "Recording aggregate (avfoundation :%s): %s",
        device_index,
        ", ".join(f"{m.mic_id}=ch{m.channel} → {p.parent.name}" for m, p in zip(mics, out_patterns)),
    )
    return _popen_ffmpeg(cmd)


def _stop(proc: subprocess.Popen) -> None:
    """Ask ffmpeg to stop gracefully, then escalate if it ignores us."""
    if proc.poll() is not None:
        return
    try:
        if proc.stdin:
            proc.stdin.write(b"q")
            proc.stdin.flush()
    except (BrokenPipeError, OSError):
        pass
    try:
        proc.wait(timeout=5)
        return
    except subprocess.TimeoutExpired:
        pass
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


# Capture rate used for a calibration leg whose configured band exceeds the
# session's own SAMPLE_RATE Nyquist limit (e.g. a >8 kHz leg against 16 kHz
# recordings) — high enough for the 200-8000..~17500 Hz range this rig's
# hardware (EMEET speaker specced to 20 kHz) can realistically use.
CALIBRATION_HIGH_RATE = 48000


class _LiveCapture:
    """Background capture for a calibration leg that needs a sample rate the
    mic's own ffmpeg-recorded track doesn't have.

    Uses an explicit ``sounddevice.InputStream`` rather than the simpler
    blocking ``sd.rec()`` — ``sd.play()`` (used to emit the other leg's
    chirp) fights over the shared default stream with ``sd.rec()``, so the
    listening side needs its own independent stream instance. Starts
    capturing immediately; :meth:`get_samples` stops the stream and returns
    everything captured so far, matching the ``get_samples`` contract on
    :class:`chirp.CalibrationMic`.
    """

    def __init__(self, device_index: int, sample_rate: int):
        import numpy as np
        import sounddevice as sd

        self._np = np
        self._chunks: list = []

        def _callback(indata, frames, time_info, status):
            self._chunks.append(indata[:, 0].copy())

        self._stream = sd.InputStream(
            device=device_index,
            channels=1,
            samplerate=sample_rate,
            dtype="float32",
            callback=_callback,
        )
        self._closed = False
        self._stream.start()

    def close(self):
        if self._closed:
            return
        self._closed = True
        self._stream.stop()
        self._stream.close()

    def get_samples(self):
        self.close()
        if not self._chunks:
            return self._np.zeros(0, dtype=self._np.float32)
        return self._np.concatenate(self._chunks)


def _try_chirp_calibration(
    mics: list[RecordMic],
    chirp_bands: dict[str, list[float]] | None = None,
) -> dict | None:
    """Best-effort chirp calibration between the 2-mic rig's live devices.

    ``chirp_bands``, if given, maps a mic_id to the ``[f0, f1]`` band to use
    for the calibration leg *listening on that mic* — see
    :func:`chirp.run_calibration`'s ``bands`` param. ``None`` (the default)
    keeps the single default band. Every leg listens on its own
    :class:`_LiveCapture` ``InputStream`` (never the ffmpeg-recorded track —
    an in-progress ``.m4a`` chunk is undecodable until it closes); a leg whose
    band exceeds the session ``SAMPLE_RATE`` Nyquist limit captures at 48 kHz.

    Never raises: any failure returns ``None`` so a calibration problem never
    blocks recording.
    """
    if len(mics) != 2:
        logger.info(
            "Chirp calibration needs exactly 2 mics — skipping (got %d)", len(mics)
        )
        return None
    live_captures: list[_LiveCapture] = []
    try:
        from . import chirp as ch

        def _band_for(mic: RecordMic) -> tuple[float, float] | None:
            """chirp_bands keys match a mic by mic_id or by case-insensitive
            name substring — avfoundation indices (and thus positional
            mic_ids) reshuffle whenever a device appears, so name keys are
            the stable way to pin a band to physical hardware."""
            if not chirp_bands:
                return None
            for key, band in chirp_bands.items():
                if key == mic.mic_id or key.lower() in mic.name.lower():
                    return (band[0], band[1])
            return None

        record_start = time.monotonic()
        cal_mics = []
        bands: dict[str, tuple[float, float]] = {}
        capture_rates: dict[str, int] = {}
        for mic in mics:
            band = _band_for(mic)
            if band is not None:
                bands[mic.mic_id] = band
            needs_high_rate = band is not None and band[1] > SAMPLE_RATE / 2

            # Every leg listens on its own live InputStream: the in-progress
            # ffmpeg .m4a chunk has no moov atom until it closes (15 min), so
            # decoding it at session start can never work.
            rate = CALIBRATION_HIGH_RATE if needs_high_rate else SAMPLE_RATE
            if needs_high_rate:
                capture_rates[mic.mic_id] = rate
            in_idx = ch.match_input_device(mic.name)
            if in_idx is None:
                raise RuntimeError(
                    f"chirp calibration needs a live capture for {mic.mic_id} "
                    f"({mic.name!r}) but no matching input device was found"
                )
            capture = _LiveCapture(in_idx, rate)
            live_captures.append(capture)
            get_samples = capture.get_samples

            cal_mics.append(
                ch.CalibrationMic(
                    mic_id=mic.mic_id,
                    name=mic.name,
                    record_start_monotonic=record_start,
                    get_samples=get_samples,
                )
            )
        return ch.run_calibration(
            cal_mics,
            sample_rate=SAMPLE_RATE,
            bands=bands or None,
            capture_rates=capture_rates or None,
        )
    except Exception:
        logger.exception("Chirp calibration setup failed — continuing without it")
        return None
    finally:
        for capture in live_captures:
            capture.close()


def record_session(
    session: int,
    mics: list[RecordMic],
    audio_dir: Path,
    segment_seconds: int,
    *,
    max_seconds: float | None = None,
    ffmpeg: str = "ffmpeg",
    on_ready=None,
    calibrate: bool = False,
    chirp_bands: dict[str, list[float]] | None = None,
    aggregate_index: int | None = None,
    strict: bool = False,
    watch_device_names: list[str] | None = None,
    capture_sample_rate: int = CAPTURE_SAMPLE_RATE,
    capture_highpass_hz: int = HIGHPASS_HZ,
) -> Path:
    """Record all ``mics`` until interrupted (or ``max_seconds`` elapses).

    Returns the session directory. Writes ``manifest.json`` up front so the
    transcribe step can run even if recording is cut short. Stops cleanly on
    SIGINT/SIGTERM so the controlling agent can end the session on command.

    ``aggregate_index`` (from :func:`select_aggregate_mics`) switches to the
    preferred aggregate capture mode: one ffmpeg on that avfoundation device,
    panning each mic's ``channel`` to its own mono part series. One shared
    CoreAudio clock means the tracks are inherently sample-aligned, so chirp
    calibration is skipped even if requested.

    ``calibrate=True`` (per-mic capture only — a manual fallback for rigs
    without an aggregate device) runs a chirp time-of-flight calibration (v1:
    offset-only, opt-in) once both mic recordings are rolling, and rewrites
    the manifest with its result (``chirp_calibration``) before the main
    recording loop starts. A calibration failure never blocks recording —
    the manifest simply omits ``chirp_calibration``. ``chirp_bands``
    (from ``Config.chirp_bands``, keyed by listening mic_id) overrides the
    default 200-8000 Hz band per calibration leg — see
    :func:`_try_chirp_calibration`; ``None`` keeps the default band.

    A device-presence watchdog polls avfoundation for ``watch_device_names``
    (default: each mic's name) and ends the session cleanly — notification,
    ``device-disconnect`` marker, finalized parts — when a mic vanishes.
    Scene markers land in ``audio/markers.jsonl`` (appended by the Run-Scene
    button) and are folded into ``audio/markers.json`` on stop.
    """
    sdir = session_dir(audio_dir, session)
    audio_subdir = sdir / "audio"
    audio_subdir.mkdir(parents=True, exist_ok=True)

    capture = "aggregate" if aggregate_index is not None else "per-mic"
    started_at = time.strftime("%Y-%m-%dT%H:%M:%S")
    started_at_epoch = time.time()
    manifest = build_manifest(
        session, mics, segment_seconds, started_at=started_at, capture=capture,
        started_at_epoch=started_at_epoch, strict=strict,
        capture_sample_rate=capture_sample_rate,
    )
    (audio_subdir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    append_marker(
        audio_subdir,
        {
            "event": "recording-started",
            "t_offset_s": 0.0,
            "epoch": started_at_epoch,
            "wall": started_at,
        },
    )

    procs: list[tuple[str, subprocess.Popen]] = []
    if aggregate_index is not None:
        out_patterns = [
            raw_mic_dir(audio_dir, session, mic) / f"part-%03d.{CAPTURE_EXT}"
            for mic in mics
        ]
        procs.append(
            (
                "aggregate",
                _spawn_aggregate(
                    aggregate_index, mics, out_patterns, segment_seconds, ffmpeg,
                    sample_rate=capture_sample_rate, highpass_hz=capture_highpass_hz,
                ),
            )
        )
        if calibrate:
            logger.info(
                "Aggregate capture shares one CoreAudio clock — skipping chirp calibration"
            )
            calibrate = False
    else:
        for mic in mics:
            out_pattern = raw_mic_dir(audio_dir, session, mic) / f"part-%03d.{CAPTURE_EXT}"
            procs.append(
                (
                    mic.mic_id,
                    _spawn(
                        mic, out_pattern, segment_seconds, ffmpeg,
                        sample_rate=capture_sample_rate,
                        highpass_hz=capture_highpass_hz,
                    ),
                )
            )

    stop_event = threading.Event()
    stop_reason: list[str] = []  # first writer wins; read after the loop

    def _handle(signum, _frame):
        logger.info("Received signal %s — stopping recording", signum)
        stop_reason.append("manual")
        stop_event.set()

    prev_int = signal.getsignal(signal.SIGINT)
    prev_term = signal.getsignal(signal.SIGTERM)
    signal.signal(signal.SIGINT, _handle)
    signal.signal(signal.SIGTERM, _handle)

    if calibrate:
        time.sleep(1.0)  # let ffmpeg's captures settle before we chirp
        chirp_calibration = _try_chirp_calibration(mics, chirp_bands=chirp_bands)
        manifest = build_manifest(
            session, mics, segment_seconds, started_at=started_at,
            chirp_calibration=chirp_calibration, capture=capture,
        )
        (audio_subdir / "manifest.json").write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )

    if on_ready:
        on_ready(procs)

    # Disconnect watchdog: `aresample=async=1` gap-fills a vanished USB mic
    # with silence, so ffmpeg never exits on unplug — the only reliable signal
    # is the device disappearing from the avfoundation list. Poll it; require
    # consecutive misses so an enumeration hiccup doesn't false-trip.
    def _watchdog(expected: list[str]) -> None:
        misses = 0
        if stop_event.wait(WATCHDOG_GRACE_SECONDS):
            return
        while not stop_event.wait(WATCHDOG_POLL_SECONDS):
            try:
                devs = list_avfoundation_devices(ffmpeg)
            except OSError:
                continue
            if not devs:  # enumeration itself failed — not evidence of unplug
                continue
            missing = verify_devices_present(devs, expected)
            if missing:
                misses += 1
                logger.warning(
                    "Mic(s) missing from device list (%d/%d): %s",
                    misses, WATCHDOG_MISSES_TO_STOP, ", ".join(missing),
                )
                if misses >= WATCHDOG_MISSES_TO_STOP:
                    msg = f"Mic disconnected: {', '.join(missing)} — recording stopped"
                    logger.error(msg)
                    stop_reason.append("device-disconnect")
                    _notify("Session recording stopped", msg)
                    stop_event.set()
                    return
            else:
                misses = 0

    watch_names = watch_device_names or [m.name for m in mics]
    watchdog = threading.Thread(
        target=_watchdog, args=(watch_names,), daemon=True, name="mic-watchdog"
    )
    watchdog.start()

    start = time.monotonic()
    try:
        while not stop_event.is_set():
            # Bail out if every recorder died (bad device, disk full, ...).
            if all(p.poll() is not None for _, p in procs):
                logger.error("All ffmpeg recorders exited unexpectedly")
                stop_reason.append("all-recorders-exited")
                break
            if max_seconds is not None and time.monotonic() - start >= max_seconds:
                break
            time.sleep(0.25)
    finally:
        signal.signal(signal.SIGINT, prev_int)
        signal.signal(signal.SIGTERM, prev_term)
        for label, proc in procs:
            _stop(proc)
            if proc.returncode not in (0, None):
                err = proc.stderr.read().decode("utf-8", "replace") if proc.stderr else ""
                if err.strip():
                    logger.warning("%s ffmpeg stderr: %s", label, err.strip()[-500:])
        ended_epoch = time.time()
        append_marker(
            audio_subdir,
            {
                "event": "recording-ended",
                "reason": stop_reason[0] if stop_reason else "manual",
                "t_offset_s": round(ended_epoch - started_at_epoch, 3),
                "epoch": ended_epoch,
                "wall": time.strftime("%Y-%m-%dT%H:%M:%S"),
            },
        )
        finalize_markers(audio_subdir, session, started_at_epoch)

    return sdir
