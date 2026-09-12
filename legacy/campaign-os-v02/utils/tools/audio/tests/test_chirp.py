"""Tests for chirp-based time-of-flight calibration (v1: offset-only)."""

from __future__ import annotations

import pytest

np = pytest.importorskip("numpy")
pytest.importorskip("scipy")

from shattered_audio import chirp as chirp_mod  # noqa: E402
from shattered_audio.chirp import (  # noqa: E402
    CalibrationMic,
    generate_chirp,
    locate_chirp,
    run_calibration,
)

SR = 16000


def test_generate_chirp_shape_and_duration():
    sweep = generate_chirp(duration_s=1.5, f0=200.0, f1=8000.0, sample_rate=SR)
    assert sweep.dtype == np.float32
    assert len(sweep) == int(round(1.5 * SR))


def test_generate_chirp_is_tapered():
    sweep = generate_chirp(duration_s=1.0, sample_rate=SR)
    peak = float(np.abs(sweep).max())
    # Tukey taper drives the very first/last samples toward zero relative to
    # the sweep's peak amplitude — a hard-edged sweep would not.
    assert abs(sweep[0]) < 0.05 * peak
    assert abs(sweep[-1]) < 0.05 * peak


def test_locate_chirp_finds_synthetic_injection():
    sweep = generate_chirp(duration_s=1.0, sample_rate=SR)
    rng = np.random.default_rng(42)
    total_s = 4.0
    buf = (0.02 * rng.standard_normal(int(total_s * SR))).astype(np.float32)
    true_offset_samples = int(1.732 * SR)
    buf[true_offset_samples : true_offset_samples + len(sweep)] += sweep

    arrival_s, strength = locate_chirp(buf, sweep, sample_rate=SR)

    assert abs(arrival_s - true_offset_samples / SR) < 0.005
    assert strength >= 0.5


def test_locate_chirp_prefers_first_strong_peak_over_global_max():
    """Multipath: a later, louder reflection must not beat the earlier direct path."""
    sweep = generate_chirp(duration_s=0.2, sample_rate=SR)
    total_s = 2.0
    buf = np.zeros(int(total_s * SR), dtype=np.float32)
    direct = int(0.5 * SR)
    reflection = int(0.9 * SR)
    buf[direct : direct + len(sweep)] += sweep  # direct path, normal level
    buf[reflection : reflection + len(sweep)] += 1.3 * sweep  # louder "reflection"

    arrival_s, strength = locate_chirp(buf, sweep, sample_rate=SR)

    assert abs(arrival_s - direct / SR) < 0.005
    assert strength >= 0.5


def test_locate_chirp_empty_when_no_match():
    sweep = generate_chirp(duration_s=0.1, sample_rate=SR)
    silence = np.zeros(SR, dtype=np.float32)
    arrival_s, strength = locate_chirp(silence, sweep, sample_rate=SR)
    assert arrival_s == 0.0
    assert strength == 0.0


def _embed(rng, sweep, offset_samples: int, total_s: float = 1.0) -> np.ndarray:
    buf = (0.01 * rng.standard_normal(int(total_s * SR))).astype(np.float32)
    buf[offset_samples : offset_samples + len(sweep)] += sweep
    return buf


def test_run_calibration_ntp_arithmetic(monkeypatch):
    duration_s = 0.05
    sweep = generate_chirp(duration_s=duration_s, sample_rate=SR)
    rng = np.random.default_rng(0)

    arrival_b_samples = 4000
    arrival_a_samples = 3000
    samples_b = _embed(rng, sweep, arrival_b_samples)
    samples_a = _embed(rng, sweep, arrival_a_samples)

    t0, t2 = 100.0, 205.0
    play_timestamps = iter([t0, t2])

    def fake_play_and_timestamp(chirp, device_index, sample_rate=SR):
        return next(play_timestamps)

    monkeypatch.setattr(chirp_mod, "play_and_timestamp", fake_play_and_timestamp)
    monkeypatch.setattr(chirp_mod.time, "sleep", lambda s: None)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=50.0,
        get_samples=lambda: samples_a, output_device=1,
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=60.0,
        get_samples=lambda: samples_b, output_device=2,
    )

    result = run_calibration([mic_a, mic_b], sample_rate=SR, duration_s=duration_s)

    assert result is not None
    t1 = 60.0 + arrival_b_samples / SR
    t3 = 50.0 + arrival_a_samples / SR
    expected_offset = ((t1 - t0) + (t2 - t3)) / 2.0
    assert result["offset_start_s"] == pytest.approx(expected_offset, abs=1.0 / SR)
    assert result["method"] == "chirp"
    assert result["devices"] == {"mic00": 1, "mic01": 2}
    assert set(result["peak_strengths"]) == {"mic00", "mic01"}


def test_run_calibration_needs_exactly_two_mics():
    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32), output_device=1,
    )
    assert run_calibration([mic_a], sample_rate=SR) is None
    assert run_calibration([mic_a, mic_a, mic_a], sample_rate=SR) is None


def test_run_calibration_returns_none_when_device_matching_fails(monkeypatch):
    """sounddevice missing/erroring during device lookup must degrade to None, never raise."""

    def fake_match_output_device(mic_name: str):
        raise RuntimeError("PortAudio not available")

    monkeypatch.setattr(chirp_mod, "match_output_device", fake_match_output_device)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32),
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32),
    )

    assert run_calibration([mic_a, mic_b], sample_rate=SR) is None


def test_run_calibration_returns_none_when_no_output_device_matches(monkeypatch):
    monkeypatch.setattr(chirp_mod, "match_output_device", lambda name: None)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32),
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32),
    )

    assert run_calibration([mic_a, mic_b], sample_rate=SR) is None


def test_generate_and_locate_chirp_at_15k_17500_48k():
    """A high-band leg (e.g. EMEET speaker -> MacBook mic) round-trips at 48 kHz."""
    sr = 48000
    sweep = generate_chirp(duration_s=0.3, f0=15000.0, f1=17500.0, sample_rate=sr)
    rng = np.random.default_rng(7)
    buf = (0.01 * rng.standard_normal(int(1.0 * sr))).astype(np.float32)
    offset_samples = int(0.4 * sr)
    buf[offset_samples : offset_samples + len(sweep)] += sweep

    arrival_s, strength = locate_chirp(buf, sweep, sample_rate=sr, f1=17500.0)

    assert abs(arrival_s - offset_samples / sr) < 0.005
    assert strength >= 0.5


def test_generate_chirp_raises_on_nyquist_violation():
    with pytest.raises(ValueError, match="Nyquist"):
        generate_chirp(duration_s=0.1, f0=200.0, f1=8000.0, sample_rate=15000)


def test_locate_chirp_raises_on_nyquist_violation():
    sweep = generate_chirp(duration_s=0.1, f0=200.0, f1=6000.0, sample_rate=16000)
    silence = np.zeros(SR, dtype=np.float32)
    with pytest.raises(ValueError, match="Nyquist"):
        locate_chirp(silence, sweep, sample_rate=16000, f1=9000.0)


def test_locate_chirp_without_f1_does_not_validate_nyquist():
    """f1 is opt-in — omitting it (existing callers) must not raise."""
    sweep = generate_chirp(duration_s=0.1, f0=200.0, f1=6000.0, sample_rate=16000)
    silence = np.zeros(SR, dtype=np.float32)
    arrival_s, strength = locate_chirp(silence, sweep, sample_rate=16000)
    assert arrival_s == 0.0
    assert strength == 0.0


def test_generate_chirp_default_band_still_valid_at_16k():
    """The 200-8000 Hz @ 16 kHz default sits exactly at Nyquist and must stay legal."""
    sweep = generate_chirp()
    assert len(sweep) == int(round(chirp_mod.CHIRP_DURATION_S * chirp_mod.SAMPLE_RATE))


def test_run_calibration_missing_hardware_with_custom_bands(monkeypatch):
    """A hardware-lookup failure must still degrade to None when custom bands/rates are used."""

    def fake_match_output_device(mic_name: str):
        raise RuntimeError("PortAudio not available")

    monkeypatch.setattr(chirp_mod, "match_output_device", fake_match_output_device)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32),
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(48000, dtype=np.float32),
    )

    result = run_calibration(
        [mic_a, mic_b],
        sample_rate=SR,
        bands={"mic01": (15000.0, 17500.0)},
        capture_rates={"mic01": 48000},
    )
    assert result is None


def test_run_calibration_default_bands_none_matches_previous_contract(monkeypatch):
    """bands=None / capture_rates=None (the default) must not add optional result keys."""
    duration_s = 0.05
    sweep = generate_chirp(duration_s=duration_s, sample_rate=SR)
    rng = np.random.default_rng(1)

    samples_b = _embed(rng, sweep, 4000)
    samples_a = _embed(rng, sweep, 3000)

    play_timestamps = iter([100.0, 205.0])
    monkeypatch.setattr(
        chirp_mod, "play_and_timestamp", lambda chirp, device_index, sample_rate=SR: next(play_timestamps)
    )
    monkeypatch.setattr(chirp_mod.time, "sleep", lambda s: None)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=50.0,
        get_samples=lambda: samples_a, output_device=1,
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=60.0,
        get_samples=lambda: samples_b, output_device=2,
    )

    result = run_calibration([mic_a, mic_b], sample_rate=SR, duration_s=duration_s)

    assert result is not None
    assert "bands" not in result
    assert "capture_rates" not in result


def test_run_calibration_returns_none_when_playback_raises(monkeypatch):
    def fake_play_and_timestamp(chirp, device_index, sample_rate=SR):
        raise RuntimeError("no such output device")

    monkeypatch.setattr(chirp_mod, "play_and_timestamp", fake_play_and_timestamp)

    mic_a = CalibrationMic(
        mic_id="mic00", name="A", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32), output_device=1,
    )
    mic_b = CalibrationMic(
        mic_id="mic01", name="B", record_start_monotonic=0.0,
        get_samples=lambda: np.zeros(SR, dtype=np.float32), output_device=2,
    )

    assert run_calibration([mic_a, mic_b], sample_rate=SR) is None
