#!/usr/bin/env python3
"""Manual probe: is the EMEET's stereo output actually two distinct channels?

Records a short 2-channel capture straight from PortAudio (via ``sounddevice``,
*not* the ffmpeg/avfoundation path ``record.py`` uses for real sessions) and
reports whether the left and right channels carry meaningfully different
audio, or whether the device's stereo output is really a DSP-mono signal
duplicated onto both channels.

Run it, clap once near the left side of the table, wait a beat, then clap
once near the right side. The script prints per-channel RMS, the channel
correlation, the RMS-of-difference (in dB relative to mean channel RMS), and
the L/R amplitude ratio around each detected clap transient, then a verdict.

Caveat — this is a PortAudio probe, not the actual capture path. record.py
captures via ffmpeg's avfoundation input, a different driver stack talking to
the same physical device. The result here is *assumed* to generalize to that
path because it's the same hardware — that assumption is not proven. Treat
this as a quick go/no-go signal before investing in a downstream L/R split,
not as a substitute for verifying against an actual ffmpeg recording.

Usage:
    python scripts/clap_probe.py [--seconds 20] [--device EMEET] [--samplerate 16000]
"""

from __future__ import annotations

import argparse
import sys


def _np():
    try:
        import numpy as np
    except ImportError:
        print("clap_probe needs numpy + sounddevice — pip install -e '.[live]'", file=sys.stderr)
        raise SystemExit(1)
    return np


def find_input_device(name_substring: str) -> int:
    """Return the PortAudio input device index whose name contains ``name_substring``."""
    import sounddevice as sd

    name_lower = name_substring.lower()
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev["max_input_channels"] > 0 and name_lower in dev["name"].lower():
            return i
    raise SystemExit(
        f"No input device matching {name_substring!r} found. "
        f"Available: {[d['name'] for d in devices if d['max_input_channels'] > 0]}"
    )


def record_stereo(device: int, seconds: float, samplerate: int):
    """Record ``seconds`` of 2-channel float32 audio from ``device`` via InputStream."""
    import sounddevice as sd

    np = _np()
    frames = int(seconds * samplerate)
    buf = np.zeros((frames, 2), dtype="float32")
    write_pos = 0

    def callback(indata, count, time_info, status):
        nonlocal write_pos
        if status:
            print(f"  [stream status: {status}]", file=sys.stderr)
        end = min(write_pos + count, frames)
        n = end - write_pos
        if n > 0:
            buf[write_pos:end] = indata[:n]
            write_pos = end

    with sd.InputStream(
        device=device,
        samplerate=samplerate,
        channels=2,
        dtype="float32",
        callback=callback,
    ):
        print(f"Recording {seconds:.0f}s of 2-channel audio at {samplerate} Hz...")
        print("  clap once on the LEFT side, wait, clap once on the RIGHT side")
        sd.sleep(int(seconds * 1000))

    return buf


def rms(x) -> float:
    np = _np()
    return float(np.sqrt(np.mean(np.square(x))))


def find_claps(mono, samplerate: int, threshold_factor: float = 6.0, min_gap_s: float = 0.5):
    """Simple peak-pick: return sample indices of transient spikes above a noise-floor threshold."""
    np = _np()
    window = max(1, int(0.01 * samplerate))  # 10ms envelope
    n = len(mono) // window
    if n == 0:
        return []
    env = np.array(
        [rms(mono[i * window : (i + 1) * window]) for i in range(n)]
    )
    floor = float(np.median(env)) + 1e-9
    peaks = []
    min_gap_blocks = max(1, int(min_gap_s / (window / samplerate)))
    last = -min_gap_blocks
    for i, v in enumerate(env):
        if v > floor * threshold_factor and (i - last) >= min_gap_blocks:
            peaks.append(i * window)
            last = i
    return peaks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--seconds", type=float, default=20.0, help="Recording length (default: 20)")
    parser.add_argument("--device", default="EMEET", help="Input device name substring (default: EMEET)")
    parser.add_argument("--samplerate", type=int, default=16000, help="Sample rate (default: 16000)")
    args = parser.parse_args()

    np = _np()
    device = find_input_device(args.device)
    audio = record_stereo(device, args.seconds, args.samplerate)

    left = audio[:, 0]
    right = audio[:, 1]

    rms_l = rms(left)
    rms_r = rms(right)
    mean_rms = (rms_l + rms_r) / 2 or 1e-12

    diff = left - right
    rms_diff = rms(diff)
    rms_diff_db = 20 * np.log10(max(rms_diff, 1e-12) / mean_rms)

    if np.std(left) > 0 and np.std(right) > 0:
        correlation = float(np.corrcoef(left, right)[0, 1])
    else:
        correlation = float("nan")

    print()
    print(f"Left RMS:  {rms_l:.6f}")
    print(f"Right RMS: {rms_r:.6f}")
    print(f"Correlation (L, R): {correlation:.4f}")
    print(f"RMS(L-R) relative to mean channel RMS: {rms_diff_db:.1f} dB")

    claps = find_claps(np.maximum(np.abs(left), np.abs(right)), args.samplerate)
    if claps:
        print(f"\nDetected {len(claps)} transient(s):")
        window = int(0.05 * args.samplerate)  # 50ms around the peak
        for idx in claps:
            lo, hi = max(0, idx - window), idx + window
            l_amp = rms(left[lo:hi])
            r_amp = rms(right[lo:hi])
            ratio_db = 20 * np.log10(max(l_amp, 1e-12) / max(r_amp, 1e-12))
            t = idx / args.samplerate
            print(f"  t={t:5.2f}s  L/R amplitude ratio: {ratio_db:+.1f} dB")
    else:
        print("\nNo transients detected — did the claps register? Try again louder/closer.")

    print()
    if correlation > 0.98 and rms_diff_db < -30:
        print("VERDICT: CHANNELS EFFECTIVELY IDENTICAL (DSP mono) — stop, do not build L/R split")
    else:
        print("VERDICT: CHANNELS DISTINCT — L/R split viable")


if __name__ == "__main__":
    main()
