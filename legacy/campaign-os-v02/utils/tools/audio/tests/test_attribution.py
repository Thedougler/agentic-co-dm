"""Tests for cross-engine speaker attribution backfill in session transcription."""

from __future__ import annotations

from shattered_audio.session_transcribe import Utterance, resolve_engine_speaker_ids


def test_whisper_session_is_noop():
    # No engine_speaker_id anywhere (whisper/parakeet) -> untouched, even
    # with an empty resolved set.
    utts = [
        Utterance(0.0, 1.0, "DM", "hello", mic_id="mic00"),
        Utterance(1.0, 2.0, "Speaker mic01", "hi there", mic_id="mic01"),
    ]
    before = [u.speaker for u in utts]
    resolve_engine_speaker_ids(utts, set())
    assert [u.speaker for u in utts] == before


def test_majority_vote_backfills_unresolved_rows():
    utts = [
        # mic01/eng-A: two embedding-resolved rows both say "Nick" -> majority Nick.
        Utterance(0.0, 1.0, "Nick", "one", mic_id="mic01", engine_speaker_id="eng-A"),
        Utterance(1.0, 2.0, "Nick", "two", mic_id="mic01", engine_speaker_id="eng-A"),
        # Unresolved row on the same (mic, engine id) pairing -> should backfill to Nick.
        Utterance(2.0, 3.0, "Speaker mic01", "three", mic_id="mic01", engine_speaker_id="eng-A"),
    ]
    resolved = {0, 1}
    resolve_engine_speaker_ids(utts, resolved)
    assert utts[2].speaker == "Nick"
    # Resolved rows and their labels are untouched.
    assert utts[0].speaker == "Nick"
    assert utts[1].speaker == "Nick"


def test_tie_leaves_unresolved_row_as_is():
    utts = [
        Utterance(0.0, 1.0, "Nick", "one", mic_id="mic01", engine_speaker_id="eng-A"),
        Utterance(1.0, 2.0, "Dave", "two", mic_id="mic01", engine_speaker_id="eng-A"),
        Utterance(2.0, 3.0, "Speaker mic01", "three", mic_id="mic01", engine_speaker_id="eng-A"),
    ]
    resolved = {0, 1}
    resolve_engine_speaker_ids(utts, resolved)
    # 1-1 tie between Nick and Dave -> unresolved row left untouched.
    assert utts[2].speaker == "Speaker mic01"


def test_embedding_resolved_rows_never_overwritten():
    utts = [
        # Majority on this pairing is "Dave", but row 0 was itself embedding-
        # resolved to "Nick" -> must never be overwritten by the majority.
        Utterance(0.0, 1.0, "Nick", "one", mic_id="mic01", engine_speaker_id="eng-A"),
        Utterance(1.0, 2.0, "Dave", "two", mic_id="mic01", engine_speaker_id="eng-A"),
        Utterance(2.0, 3.0, "Dave", "three", mic_id="mic01", engine_speaker_id="eng-A"),
    ]
    resolved = {0, 1, 2}
    resolve_engine_speaker_ids(utts, resolved)
    assert utts[0].speaker == "Nick"
    assert utts[1].speaker == "Dave"
    assert utts[2].speaker == "Dave"


def test_key_with_no_votes_left_untouched():
    # engine_speaker_id present but no embedding-resolved rows anywhere for
    # that (mic, id) pairing -> nothing to vote from, row is left as-is.
    utts = [
        Utterance(0.0, 1.0, "Speaker mic01", "one", mic_id="mic01", engine_speaker_id="eng-Z"),
    ]
    resolve_engine_speaker_ids(utts, set())
    assert utts[0].speaker == "Speaker mic01"


def test_different_mic_same_engine_id_kept_separate():
    # Same engine_speaker_id string on two different mics must not cross-vote.
    utts = [
        Utterance(0.0, 1.0, "Nick", "one", mic_id="mic00", engine_speaker_id="0"),
        Utterance(1.0, 2.0, "Nick", "two", mic_id="mic00", engine_speaker_id="0"),
        Utterance(2.0, 3.0, "Speaker mic01", "three", mic_id="mic01", engine_speaker_id="0"),
    ]
    resolved = {0, 1}
    resolve_engine_speaker_ids(utts, resolved)
    # No votes recorded for (mic01, "0") -> unresolved row on mic01 untouched.
    assert utts[2].speaker == "Speaker mic01"
