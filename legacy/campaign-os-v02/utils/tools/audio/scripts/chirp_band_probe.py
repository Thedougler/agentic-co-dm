#!/usr/bin/env python3
"""Manual probe: which chirp bands actually round-trip on this rig's hardware?

Not a pytest test and not an installed CLI command — a standalone hand-run
script for the table's actual mics/speakers, since chirp.py's own tests are
synthetic (no hardware). Run it in a quiet room; ambient noise or a running
AC will distort the peak strengths below.

For each (leg, band, amplitude) combination, this generates a chirp, plays it
out the leg's speaker device, records on the leg's mic device via an explicit
``sounddevice.InputStream`` (mirroring the "sd.play() kills an in-progress
sd.rec()" gotcha ``chirp.py`` already works around — see its module
docstring), locates it with :func:`shattered_audio.chirp.locate_chirp`, and
prints a table of leg / band / amplitude / peak strength / verdict against
``chirp.PEAK_STRENGTH_FLOOR``.

Legs probed (asymmetric — matches the two mic/speaker pairs' real limits):
  - emeet_to_mac: EMEET speaker -> MacBook mic, captured at 48000 Hz, bands
    (12000, 14000), (14000, 16000), (15000, 17500) — how high the EMEET
    speaker (specced to 20 kHz) can usefully drive a chirp that MacBook's
    48 kHz-capable mic can resolve.
  - mac_to_emeet: MacBook speaker -> EMEET mic, captured at 16000 Hz, bands
    (200, 8000), (5000, 7500) — EMEET's mic is natively 16 kHz (hard 8 kHz
    Nyquist cap), so this leg never probes above 8 kHz.

Usage:
    python scripts/chirp_band_probe.py
    python scripts/chirp_band_probe.py --emeet-name EMEET --mac-mic-name "MacBook"
    python scripts/chirp_band_probe.py --amplitudes 0.3,0.6 --legs mac_to_emeet
"""

from __future__ import annotations

import argparse
import sys
import time

# Repo layout: scripts/ sits beside src/ under tools/audio/.
sys.path.insert(0, str((__import__("pathlib").Path(__file__).resolve().parent.parent / "src")))

DEFAULT_DURATION_S = 1.5

# (band f0, band f1)
EMEET_TO_MAC_BANDS = [(12000.0, 14000.0), (14000.0, 16000.0), (15000.0, 17500.0)]
MAC_TO_EMEET_BANDS = [(200.0, 8000.0), (5000.0, 7500.0)]

EMEET_TO_MAC_CAPTURE_RATE = 48000
MAC_TO_EMEET_CAPTURE_RATE = 16000

DEFAULT_AMPLITUDES = [0.3, 0.6, 0.9]


def _np():
    try:
        import numpy as np
    except ImportError:
        print(
            "chirp_band_probe needs numpy/scipy/sounddevice — pip install -e '.[live]'",
            file=sys.stderr,
        )
        raise SystemExit(1)
    return np


def find_device(name_substring: str, *, output: bool) -> int:
    """Return the PortAudio device index (input or output) name-matching ``name_substring``."""
    import sounddevice as sd

    name_lower = name_substring.lower()
    devices = sd.query_devices()
    key = "max_output_channels" if output else "max_input_channels"
    for i, dev in enumerate(devices):
        if dev[key] > 0 and name_lower in dev["name"].lower():
            return i
    kind = "output" if output else "input"
    raise SystemExit(
        f"No {kind} device matching {name_substring!r} found. "
        f"Available: {[d['name'] for d in devices if d[key] > 0]}"
    )


def record_leg(speaker_device: int, mic_device: int, chirp, sample_rate: int, settle_s: float = 0.5):
    """Play ``chirp`` on ``speaker_device`` while capturing on ``mic_device``.

    Both sides are explicit stream instances — the listening side because
    ``sd.play()`` kills an in-progress ``sd.rec()`` on the shared default
    stream (the gotcha ``record._LiveCapture`` works around), and the playing
    side because ``sd.play()``'s own global-stream teardown deadlocks
    PortAudio on macOS while another stream is running (main thread wedges in
    ``FinishStoppingStream`` waiting on a mutex).
    """
    import sounddevice as sd

    np = _np()
    chunks: list = []

    def _callback(indata, frames, time_info, status):
        chunks.append(indata[:, 0].copy())

    stream = sd.InputStream(
        device=mic_device, channels=1, samplerate=sample_rate, dtype="float32", callback=_callback
    )
    stream.start()
    try:
        out = sd.OutputStream(
            device=speaker_device, channels=1, samplerate=sample_rate, dtype="float32"
        )
        out.start()
        try:
            out.write(np.ascontiguousarray(chirp.reshape(-1, 1), dtype=np.float32))
        finally:
            out.stop()
            out.close()
        time.sleep(settle_s)
    finally:
        stream.stop()
        stream.close()

    if not chunks:
        return np.zeros(0, dtype=np.float32)
    return np.concatenate(chunks)


def probe_leg(leg_name, speaker_idx, mic_idx, bands, capture_rate, amplitudes, duration_s):
    from shattered_audio.chirp import PEAK_STRENGTH_FLOOR, generate_chirp, locate_chirp

    rows = []
    for f0, f1 in bands:
        for amp in amplitudes:
            sweep = generate_chirp(duration_s, f0, f1, capture_rate) * amp
            captured = record_leg(speaker_idx, mic_idx, sweep, capture_rate)
            _, peak = locate_chirp(captured, sweep, capture_rate, f1=f1)
            verdict = "OK" if peak >= PEAK_STRENGTH_FLOOR else "WEAK"
            rows.append((leg_name, f"{f0:.0f}-{f1:.0f}", amp, peak, verdict))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--emeet-name", default="EMEET", help="EMEET device name substring")
    parser.add_argument(
        "--mac-mic-name", default="MacBook", help="MacBook mic device name substring"
    )
    parser.add_argument(
        "--legs",
        default="emeet_to_mac,mac_to_emeet",
        help="Comma-separated legs to probe (default: both)",
    )
    parser.add_argument(
        "--amplitudes",
        default=",".join(str(a) for a in DEFAULT_AMPLITUDES),
        help="Comma-separated chirp amplitudes (0-1) to try",
    )
    parser.add_argument("--duration", type=float, default=DEFAULT_DURATION_S, help="Chirp duration (s)")
    args = parser.parse_args()

    legs = [leg.strip() for leg in args.legs.split(",") if leg.strip()]
    amplitudes = [float(a) for a in args.amplitudes.split(",")]

    emeet_out = find_device(args.emeet_name, output=True)
    emeet_in = find_device(args.emeet_name, output=False)
    mac_out = find_device(args.mac_mic_name, output=True)
    mac_in = find_device(args.mac_mic_name, output=False)

    all_rows = []
    if "emeet_to_mac" in legs:
        print(f"\n--- emeet_to_mac (EMEET speaker[{emeet_out}] -> MacBook mic[{mac_in}] @ "
              f"{EMEET_TO_MAC_CAPTURE_RATE} Hz) ---")
        all_rows += probe_leg(
            "emeet_to_mac", emeet_out, mac_in, EMEET_TO_MAC_BANDS,
            EMEET_TO_MAC_CAPTURE_RATE, amplitudes, args.duration,
        )
    if "mac_to_emeet" in legs:
        print(f"\n--- mac_to_emeet (MacBook speaker[{mac_out}] -> EMEET mic[{emeet_in}] @ "
              f"{MAC_TO_EMEET_CAPTURE_RATE} Hz) ---")
        all_rows += probe_leg(
            "mac_to_emeet", mac_out, emeet_in, MAC_TO_EMEET_BANDS,
            MAC_TO_EMEET_CAPTURE_RATE, amplitudes, args.duration,
        )

    print("\nleg           | band            | amp | peak   | verdict")
    print("-" * 60)
    for leg, band, amp, peak, verdict in all_rows:
        print(f"{leg:13s} | {band:15s} | {amp:.1f} | {peak:.3f}  | {verdict}")


if __name__ == "__main__":
    main()
