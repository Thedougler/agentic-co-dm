"""Chirp-based time-of-flight calibration between the two mic tracks (v1).

v1 scope: offset-only, measure-and-log, opt-in. A logarithmic sweep is played
out each mic's own matched output device (a USB speakerphone typically
exposes both an input and an output under related names) and picked up by
*both* mics' recordings. A two-way exchange — sweep A→B, then sweep B→A — lets
NTP-style arithmetic cancel the (roughly symmetric) room propagation delay,
leaving an estimate of the start-of-recording offset between the two tracks'
own timelines. Never blocks recording: every public entry point that touches
hardware or the two-way exchange is wrapped so a failure degrades to ``None``,
not an exception.

Drift is deliberately out of scope here — the measurement is observational
(recorded into ``manifest.json`` as ``chirp_calibration``): a start-of-session
offset estimate for per-mic (non-aggregate) captures, whose tracks run on
independent clocks. Aggregate captures share one clock and skip it entirely.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Callable

from .record import SAMPLE_RATE

logger = logging.getLogger(__name__)

CHIRP_DURATION_S = 1.5
CHIRP_F0_HZ = 200.0
CHIRP_F1_HZ = 8000.0
TUKEY_ALPHA = 0.2

# A matched-filter peak counts as "the chirp" once it reaches this fraction of
# the global max. The *first* (earliest) peak clearing the bar wins, not the
# global max itself — multipath reflections in a room are frequently louder
# than the direct-path arrival.
PEAK_STRENGTH_FLOOR = 0.5

# Pause between the two directions of the exchange so the first sweep's tail
# (and any room reverb) has fully decayed before the second one plays.
SETTLE_S = 1.0

_INSTALL_HINT = "chirp calibration needs numpy/scipy/sounddevice — pip install -e '.[live]'"


def _np():
    try:
        import numpy as np

        return np
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(_INSTALL_HINT) from e


def generate_chirp(
    duration_s: float = CHIRP_DURATION_S,
    f0: float = CHIRP_F0_HZ,
    f1: float = CHIRP_F1_HZ,
    sample_rate: int = SAMPLE_RATE,
):
    """Logarithmic sweep ``f0`` → ``f1`` over ``duration_s``, Tukey-tapered.

    The taper avoids the audible/measurable click a hard-edged sweep would
    add at start and end, which would otherwise register as a spurious sharp
    matched-filter peak of its own.
    """
    if f1 > sample_rate / 2:
        raise ValueError(
            f"chirp f1={f1} Hz must be below the Nyquist limit "
            f"({sample_rate / 2} Hz for sample_rate={sample_rate})"
        )

    np = _np()
    from scipy.signal import chirp as _scipy_chirp
    from scipy.signal.windows import tukey

    n = int(round(duration_s * sample_rate))
    t = np.linspace(0.0, duration_s, n, endpoint=False)
    sweep = _scipy_chirp(t, f0, duration_s, f1, method="logarithmic")
    window = tukey(n, TUKEY_ALPHA)
    return (sweep * window).astype(np.float32)


def _match_device(mic_name: str, *, output: bool) -> int | None:
    """Find a sounddevice device whose name matches ``mic_name``, dropping
    trailing words as a fallback so a mic name still finds its sibling device
    ("MacBook Air Microphone" -> "MacBook Air" -> "MacBook Air Speakers").
    """
    import sounddevice as sd

    kind = "output" if output else "input"
    key = "max_output_channels" if output else "max_input_channels"
    devices = sd.query_devices()

    words = mic_name.lower().split()
    for end in range(len(words), 0, -1):
        candidate = " ".join(words[:end])
        for idx, dev in enumerate(devices):
            if dev.get(key, 0) > 0 and candidate in dev["name"].lower():
                logger.info(
                    "Matched mic %r -> %s device [%d] %s", mic_name, kind, idx, dev["name"]
                )
                return idx
    logger.warning("No %s device matches mic %r", kind, mic_name)
    return None


def match_output_device(mic_name: str) -> int | None:
    """Find a sounddevice *output* device whose name matches ``mic_name``
    (progressively dropping trailing words — see :func:`_match_device`).

    Case-insensitive. sounddevice's device index space is PortAudio's own and
    does not line up with ffmpeg/avfoundation's ``-list_devices`` indices —
    always resolve through this function, never reuse an avfoundation index.
    """
    return _match_device(mic_name, output=True)


def match_input_device(mic_name: str) -> int | None:
    """Find a sounddevice *input* device whose name matches ``mic_name``
    (progressively dropping trailing words — see :func:`_match_device`).

    Used when a calibration leg needs to listen at a rate other than the
    session's own ffmpeg capture rate (e.g. a 48 kHz leg) via an explicit
    :class:`sounddevice.InputStream`, rather than decoding that mic's
    ffmpeg-recorded track.
    """
    return _match_device(mic_name, output=False)


def play_and_timestamp(chirp, device_index: int, sample_rate: int = SAMPLE_RATE) -> float:
    """Play ``chirp`` (blocking) on ``device_index``; return the monotonic time
    right before playback starts.

    ``time.monotonic()`` is sampled *before* handing off to sounddevice so the
    timestamp reflects "when we asked for playback to start", matching how
    the NTP-style exchange in :func:`run_calibration` treats it.
    """
    import sounddevice as sd

    t0 = time.monotonic()
    sd.play(chirp, samplerate=sample_rate, device=device_index, blocking=True)
    return t0


def locate_chirp(
    samples, chirp, sample_rate: int = SAMPLE_RATE, f1: float | None = None
) -> tuple[float, float]:
    """Matched-filter search for ``chirp`` inside ``samples``.

    Returns ``(arrival_s, peak_strength)`` — the seconds-from-start position
    of the chirp's onset in ``samples``, and the winning peak's magnitude as
    a fraction of the global max (1.0 when the earliest strong peak *is* the
    global max). Picks the first peak reaching ``PEAK_STRENGTH_FLOOR`` of the
    global max rather than the global max itself, since a room's multipath
    reflections can outscore the direct-path arrival.

    ``f1``, if given, is the upper edge of the band the caller expects
    ``chirp`` to occupy — validated against ``sample_rate``'s Nyquist limit
    so a capture-rate/band mismatch fails loudly instead of silently
    aliasing. Omitted by default (existing callers pass only ``samples``,
    ``chirp``, ``sample_rate``), so default behavior is unchanged.
    """
    if f1 is not None and f1 > sample_rate / 2:
        raise ValueError(
            f"chirp f1={f1} Hz must be below the Nyquist limit "
            f"({sample_rate / 2} Hz for sample_rate={sample_rate})"
        )

    np = _np()
    from scipy.signal import correlate

    samples = np.asarray(samples, dtype=np.float32)
    chirp = np.asarray(chirp, dtype=np.float32)
    if len(samples) < len(chirp):
        return 0.0, 0.0

    corr = correlate(samples, chirp, mode="valid")
    mag = np.abs(corr)
    global_max = float(mag.max()) if mag.size else 0.0
    if global_max <= 0.0:
        return 0.0, 0.0

    strong = np.nonzero(mag >= PEAK_STRENGTH_FLOOR * global_max)[0]
    first = int(strong[0]) if strong.size else int(np.argmax(mag))
    return first / sample_rate, float(mag[first] / global_max)


@dataclass
class CalibrationMic:
    """One mic's role in a two-way chirp calibration exchange.

    ``get_samples`` is called *after* this mic's chirp has had time to
    arrive, and must return that mic's own recorded audio (mono float32) —
    :func:`run_calibration` locates the *other* mic's chirp inside it.
    ``record_start_monotonic`` is the ``time.monotonic()`` value at which
    this mic's own recording began, used to convert a match's in-buffer
    offset into an absolute timestamp comparable across mics.
    """

    mic_id: str
    name: str
    record_start_monotonic: float
    get_samples: Callable[[], object]
    output_device: int | None = None


def run_calibration(
    mics: list[CalibrationMic],
    *,
    sample_rate: int = SAMPLE_RATE,
    duration_s: float = CHIRP_DURATION_S,
    f0: float = CHIRP_F0_HZ,
    f1: float = CHIRP_F1_HZ,
    settle_s: float = SETTLE_S,
    bands: dict[str, tuple[float, float]] | None = None,
    capture_rates: dict[str, int] | None = None,
) -> dict | None:
    """Two-way chirp exchange between exactly 2 mics; NTP-style offset estimate.

    Plays a chirp from mic A's matched output device, then locates its
    arrival in mic B's own recording; then the reverse. Combining both
    one-way transit measurements with NTP arithmetic
    (``offset = ((t1-t0)+(t2-t3))/2``) cancels the (assumed roughly
    symmetric) room propagation delay, leaving an estimate of how far B's
    recording timeline is offset from A's.

    ``bands`` and ``capture_rates`` are both keyed by the *listening* mic's
    ``mic_id`` — i.e. ``bands[b.mic_id]`` is the ``(f0, f1)`` used for the
    sweep played toward B and searched for in B's own recording,
    ``bands[a.mic_id]`` the reverse leg. This lets the two directions of an
    asymmetric rig (different speaker/mic hardware per leg) use different
    frequency bands and, via ``capture_rates``, different sample rates —
    e.g. a leg captured through a separate 48 kHz ``InputStream`` instead of
    the mic's normal recording. Both default to ``None``, which reproduces
    the exact single-band, single-rate exchange this function always did.

    Never raises: any failure — missing sounddevice, no matched output
    device, a chirp that can't be located, anything else — is caught and
    logged, returning ``None`` so a calibration failure never blocks
    recording.
    """
    try:
        if len(mics) != 2:
            logger.warning(
                "Chirp calibration needs exactly 2 mics, got %d -- skipping", len(mics)
            )
            return None

        a, b = mics

        dev_a = a.output_device if a.output_device is not None else match_output_device(a.name)
        dev_b = b.output_device if b.output_device is not None else match_output_device(b.name)
        if dev_a is None or dev_b is None:
            logger.warning(
                "Chirp calibration: no matched output device for one or both mics -- skipping"
            )
            return None

        # Leg 1 (A -> B): band/rate keyed by the listening mic, B.
        f0_ab, f1_ab = (bands.get(b.mic_id) if bands else None) or (f0, f1)
        rate_ab = (capture_rates or {}).get(b.mic_id, sample_rate)
        sweep_ab = generate_chirp(duration_s, f0_ab, f1_ab, rate_ab)

        # Leg 2 (B -> A): band/rate keyed by the listening mic, A.
        f0_ba, f1_ba = (bands.get(a.mic_id) if bands else None) or (f0, f1)
        rate_ba = (capture_rates or {}).get(a.mic_id, sample_rate)
        sweep_ba = generate_chirp(duration_s, f0_ba, f1_ba, rate_ba)

        # Direction 1: A plays, listen for it in B's own recording.
        t0 = play_and_timestamp(sweep_ab, dev_a, rate_ab)
        time.sleep(settle_s)
        arrival_b, strength_b = locate_chirp(b.get_samples(), sweep_ab, rate_ab, f1=f1_ab)
        t1 = b.record_start_monotonic + arrival_b

        # Direction 2: B plays, listen for it in A's own recording.
        t2 = play_and_timestamp(sweep_ba, dev_b, rate_ba)
        time.sleep(settle_s)
        arrival_a, strength_a = locate_chirp(a.get_samples(), sweep_ba, rate_ba, f1=f1_ba)
        t3 = a.record_start_monotonic + arrival_a

        offset = ((t1 - t0) + (t2 - t3)) / 2.0

        result = {
            "offset_start_s": float(offset),
            "method": "chirp",
            "measured_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "devices": {a.mic_id: dev_a, b.mic_id: dev_b},
            "peak_strengths": {a.mic_id: strength_a, b.mic_id: strength_b},
        }
        if bands is not None:
            result["bands"] = {a.mic_id: [f0_ba, f1_ba], b.mic_id: [f0_ab, f1_ab]}
        if capture_rates is not None:
            result["capture_rates"] = {a.mic_id: rate_ba, b.mic_id: rate_ab}
        logger.info(
            "Chirp calibration: offset %+.1f ms (peak strengths %.2f/%.2f)",
            offset * 1000.0,
            strength_a,
            strength_b,
        )
        return result
    except Exception:
        logger.exception("Chirp calibration failed -- continuing without it")
        return None
