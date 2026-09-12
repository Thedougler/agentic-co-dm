"""Tests for shattered_audio.autocorrect."""

from __future__ import annotations

import json

from shattered_audio.autocorrect import (
    Correction,
    apply_corrections,
    load_dictionary,
    write_autocorrect_log,
)

ROWS = [
    {"ID": 1, "Start": "00:00", "End": "00:03", "Speaker": "DM", "Text": "reflux hurts the party"},
    {"ID": 2, "Start": "00:03", "End": "00:05", "Speaker": "Nick", "Text": "Reflux is bad"},
    {"ID": 3, "Start": "00:05", "End": "00:07", "Speaker": "DM", "Text": "REFLUX overwhelms them"},
    {"ID": 4, "Start": "00:07", "End": "00:09", "Speaker": "Nick", "Text": "the bunker held firm"},
    {"ID": 5, "Start": "00:09", "End": "00:11", "Speaker": "DM", "Text": "nothing to correct here"},
]


def test_case_preservation_lower_title_upper():
    corrections = [Correction(wrong="reflux", right="refits")]
    rows, applied = apply_corrections(ROWS[:3], corrections)
    assert rows[0]["Text"] == "refits hurts the party"
    assert rows[1]["Text"] == "Refits is bad"
    assert rows[2]["Text"] == "REFITS overwhelms them"
    assert len(applied) == 3


def test_word_boundary_does_not_match_inside_longer_word():
    corrections = [Correction(wrong="Bunk", right="Thunk")]
    rows, applied = apply_corrections([ROWS[3]], corrections)
    assert rows[0]["Text"] == "the bunker held firm"
    assert applied == []


def test_multi_word_phrase_match():
    corrections = [Correction(wrong="show them the rain", right="Show Them the Rain", mode="phrase")]
    rows, applied = apply_corrections(
        [{"ID": 1, "Text": "let's Show Them The Rain tonight"}], corrections
    )
    # Matched text is Title-cased -> replacement is title-cased word-by-word.
    assert rows[0]["Text"] == "let's Show Them The Rain tonight"
    assert len(applied) == 1


def test_longest_entry_applied_first_via_load_dictionary_sort(tmp_path):
    csv_path = tmp_path / "dict.csv"
    csv_path.write_text("wrong,right,mode\nrain,storm,word\nshow them the rain,greeting,phrase\n")
    corrections = load_dictionary(csv_path)
    # Longest (word-count) entry sorts first so it pre-empts the shorter one.
    assert corrections[0].wrong == "show them the rain"
    rows, applied = apply_corrections(
        [{"ID": 1, "Text": "show them the rain now"}], corrections
    )
    assert rows[0]["Text"] == "greeting now"
    assert len(applied) == 1


def test_missing_csv_is_a_noop(tmp_path):
    missing = tmp_path / "does-not-exist.csv"
    corrections = load_dictionary(missing)
    assert corrections == []


def test_malformed_row_is_skipped(tmp_path):
    csv_path = tmp_path / "dict.csv"
    csv_path.write_text("wrong,right,mode\n,missing-wrong,word\nreflux,,word\nfoo,bar,word\n")
    corrections = load_dictionary(csv_path)
    assert len(corrections) == 1
    assert corrections[0].wrong == "foo"


def test_applied_entries_match_before_after():
    corrections = [Correction(wrong="reflux", right="refits")]
    rows, applied = apply_corrections([ROWS[0]], corrections)
    assert applied[0]["before"] == "reflux hurts the party"
    assert applied[0]["after"] == "refits hurts the party"
    assert applied[0]["wrong"] == "reflux"
    assert applied[0]["right"] == "refits"
    assert applied[0]["row_id"] == 1


def test_empty_applied_means_no_sidecar_written(tmp_path):
    corrections = [Correction(wrong="nonexistent", right="whatever")]
    rows, applied = apply_corrections(ROWS, corrections)
    assert applied == []
    sidecar = tmp_path / "part.autocorrect.jsonl"
    if applied:
        write_autocorrect_log(applied, sidecar)
    assert not sidecar.exists()


def test_write_autocorrect_log_round_trips(tmp_path):
    corrections = [Correction(wrong="reflux", right="refits")]
    rows, applied = apply_corrections(ROWS[:1], corrections)
    sidecar = tmp_path / "nested" / "part.autocorrect.jsonl"
    write_autocorrect_log(applied, sidecar)
    lines = sidecar.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    entry = json.loads(lines[0])
    assert entry == applied[0]


def test_rows_not_mutated_order_and_ids_preserved():
    original = [dict(r) for r in ROWS]
    corrections = [Correction(wrong="reflux", right="refits")]
    rows, _ = apply_corrections(ROWS, corrections)
    assert ROWS == original  # input list/rows untouched
    assert [r["ID"] for r in rows] == [r["ID"] for r in ROWS]
    assert len(rows) == len(ROWS)


def test_no_corrections_is_a_noop():
    rows, applied = apply_corrections(ROWS, [])
    assert applied == []
    assert rows == ROWS
    assert rows is not ROWS
