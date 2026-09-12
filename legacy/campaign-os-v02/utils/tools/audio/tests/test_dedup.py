"""Tests for cross-mic ghost dedup in session transcription."""

from __future__ import annotations

import pytest

pytest.importorskip("numpy")

from shattered_audio.session_transcribe import (  # noqa: E402
    Utterance,
    drop_cross_mic_ghosts,
)


def test_fragmented_ghost_copies_dropped():
    # DM's line, plus the room mic's fragmented ducked copy of the same words.
    utts = [
        Utterance(34.8, 39.1, "DM", "It appears Thunk has gone on a spending spree", mic_id="mic00"),
        Utterance(34.8, 36.8, "Nick", "It appears Thunk has gone on a bit of", mic_id="mic01"),
        Utterance(36.8, 38.6, "Nick", "spending spree on known as Predator", mic_id="mic01"),
    ]
    kept = drop_cross_mic_ghosts(utts)
    # The first fragment matches and drops; the second garbled fragment shares
    # too few words with the full line to match — a documented limitation.
    assert [(u.mic_id, u.text) for u in kept] == [
        ("mic00", "It appears Thunk has gone on a spending spree"),
        ("mic01", "spending spree on known as Predator"),
    ]


def test_equal_length_near_duplicate_keeps_earlier_mic():
    utts = [
        Utterance(106.9, 110.2, "DM", "you were joking about the refits?", mic_id="mic00"),
        Utterance(106.5, 110.2, "Nick", "you were joking about the reflux?", mic_id="mic01"),
    ]
    kept = drop_cross_mic_ghosts(utts)
    assert len(kept) == 1
    assert kept[0].text == "you were joking about the refits?"


def test_different_simultaneous_speech_kept():
    utts = [
        Utterance(0.0, 3.0, "DM", "the order sheet comes out rolled", mic_id="mic00"),
        Utterance(0.5, 2.5, "Nick", "wait what did he buy", mic_id="mic01"),
    ]
    assert len(drop_cross_mic_ghosts(utts)) == 2


def test_short_echoed_reaction_kept():
    # A player echoing one word of the DM's line is real speech, not a ghost.
    utts = [
        Utterance(39.8, 44.3, "DM", "Yeah. He got shit-faced. He decided the ship needed more guns.", mic_id="mic00"),
        Utterance(40.1, 40.9, "Nick", "Well, shit-faced.", mic_id="mic01"),
    ]
    assert len(drop_cross_mic_ghosts(utts)) == 2


def test_non_overlapping_repeat_kept():
    utts = [
        Utterance(0.0, 1.0, "DM", "no refunds", mic_id="mic00"),
        Utterance(5.0, 6.0, "Nick", "no refunds", mic_id="mic01"),
    ]
    assert len(drop_cross_mic_ghosts(utts)) == 2


def test_same_mic_never_deduped():
    utts = [
        Utterance(0.0, 3.0, "DM", "hello there", mic_id="mic00"),
        Utterance(0.1, 2.9, "DM", "hello there", mic_id="mic00"),
    ]
    assert len(drop_cross_mic_ghosts(utts)) == 2


def test_order_preserved_across_multiple_ghosts():
    utts = [
        Utterance(0.0, 2.0, "DM", "two long nines, two short 32-pounders", mic_id="mic00"),
        Utterance(0.1, 1.9, "Nick", "two long nines,", mic_id="mic01"),
        Utterance(3.0, 4.0, "Nick", "been there", mic_id="mic01"),
        Utterance(5.0, 7.0, "DM", "signed twice, Officer Fink", mic_id="mic00"),
        Utterance(5.1, 6.9, "Nick", "signed twice, officer something", mic_id="mic01"),
    ]
    kept = drop_cross_mic_ghosts(utts)
    assert [(u.mic_id, u.text) for u in kept] == [
        ("mic00", "two long nines, two short 32-pounders"),
        ("mic01", "been there"),
        ("mic00", "signed twice, Officer Fink"),
    ]
