"""Tests for the post-transcription corrector helpers (correct.py)."""

from __future__ import annotations

import json

import pytest

from shattered_audio.correct import (
    merge_corrected_parts,
    read_transcript_csv,
    split_transcript_csv,
    suggest_autocorrect_promotions,
    write_correction_log,
)
from shattered_audio.session_transcribe import write_part_csv


def _row(rid, speaker, text, start="00:00:01,000", end="00:00:02,000"):
    return {"ID": str(rid), "Start": start, "End": end, "Speaker": speaker, "Text": text}


class TestReadTranscriptCsv:
    def test_legacy_unquoted_timestamps(self, tmp_path):
        # transcribeX's original shape: timestamps unquoted, millisecond comma
        # splits the field — the merged session-06 artifact is this shape.
        p = tmp_path / "legacy.csv"
        p.write_text(
            "ID,Start,End,Speaker,Text\n"
            '1,00:00:01,519,00:00:31,280,Nick,"Yeah, and totally."\n'
            '2,00:00:31,620,00:00:54,279,Speaker 1,"I attack."\n',
            encoding="utf-8",
        )
        rows = read_transcript_csv(p)
        assert rows[0] == {
            "ID": "1",
            "Start": "00:00:01,519",
            "End": "00:00:31,280",
            "Speaker": "Nick",
            "Text": "Yeah, and totally.",
        }
        assert rows[1]["Speaker"] == "Speaker 1"

    def test_roundtrip_with_write_part_csv(self, tmp_path):
        rows = [_row(1, "Nick", 'He said "go", then left.')]
        out = tmp_path / "t.csv"
        write_part_csv(rows, out)
        assert read_transcript_csv(out) == rows


class TestSplitMerge:
    def _write_transcript(self, tmp_path, n=10):
        rows = [_row(i, "Nick", f"line {i}") for i in range(1, n + 1)]
        p = tmp_path / "session.csv"
        write_part_csv(rows, p)
        return p, rows

    def test_split_into_four_contiguous_parts(self, tmp_path):
        p, rows = self._write_transcript(tmp_path, 10)
        parts = split_transcript_csv(p, parts=4)
        assert len(parts) == 4
        assert all(pp.parent.name == "correction-work" for pp in parts)
        recombined = [r for pp in parts for r in read_transcript_csv(pp)]
        assert recombined == rows

    def test_merge_unchanged_parts_no_diffs(self, tmp_path):
        p, rows = self._write_transcript(tmp_path)
        parts = split_transcript_csv(p, parts=4)
        merged, applied = merge_corrected_parts(p, parts)
        assert merged == rows and applied == []

    def test_merge_audits_changed_fields(self, tmp_path):
        p, _ = self._write_transcript(tmp_path)
        parts = split_transcript_csv(p, parts=2)
        part_rows = read_transcript_csv(parts[0])
        part_rows[0]["Text"] = "line 1 fixed"
        part_rows[1]["Speaker"] = "Chad"
        write_part_csv(part_rows, parts[0])
        merged, applied = merge_corrected_parts(p, parts)
        assert merged[0]["Text"] == "line 1 fixed"
        assert {(a["row_id"], a["field"]) for a in applied} == {("1", "Text"), ("2", "Speaker")}
        assert applied[0]["before"] == "line 1"

    def test_merge_refuses_dropped_rows(self, tmp_path):
        p, _ = self._write_transcript(tmp_path)
        parts = split_transcript_csv(p, parts=2)
        part_rows = read_transcript_csv(parts[0])
        write_part_csv(part_rows[:-1], parts[0])  # agent "lost" a row
        with pytest.raises(ValueError, match="refusing to merge"):
            merge_corrected_parts(p, parts)

    def test_merge_refuses_reordered_rows(self, tmp_path):
        p, _ = self._write_transcript(tmp_path)
        parts = split_transcript_csv(p, parts=2)
        part_rows = read_transcript_csv(parts[0])
        write_part_csv(list(reversed(part_rows)), parts[0])
        with pytest.raises(ValueError, match="refusing to merge"):
            merge_corrected_parts(p, parts)


class TestPromotions:
    def _log(self, tmp_path, name, entries):
        p = tmp_path / name
        write_correction_log(entries, p)
        return p

    def test_recurring_single_token_fix_promoted(self, tmp_path):
        e = {"row_id": "1", "field": "Text",
             "before": "Then Thunc waves.", "after": "Then Thunk waves."}
        logs = [self._log(tmp_path, "a.jsonl", [e]), self._log(tmp_path, "b.jsonl", [e])]
        promos = suggest_autocorrect_promotions(logs, min_occurrences=2)
        assert len(promos) == 1
        assert promos[0].wrong == "Thunc" and promos[0].right == "Thunk"

    def test_single_occurrence_not_promoted(self, tmp_path):
        e = {"row_id": "1", "field": "Text",
             "before": "Then Thunc waves.", "after": "Then Thunk waves."}
        logs = [self._log(tmp_path, "a.jsonl", [e])]
        assert suggest_autocorrect_promotions(logs, min_occurrences=2) == []

    def test_speaker_fixes_never_promoted(self, tmp_path):
        e = {"row_id": "1", "field": "Speaker", "before": "Speaker 1", "after": "Chad"}
        logs = [self._log(tmp_path, "a.jsonl", [e]), self._log(tmp_path, "b.jsonl", [e])]
        assert suggest_autocorrect_promotions(logs, min_occurrences=2) == []

    def test_multi_word_rewrites_not_promoted(self, tmp_path):
        # a diff spanning more than one token isn't a dictionary entry
        e = {"row_id": "1", "field": "Text",
             "before": "he said something", "after": "she never said it"}
        logs = [self._log(tmp_path, "a.jsonl", [e]), self._log(tmp_path, "b.jsonl", [e])]
        assert suggest_autocorrect_promotions(logs, min_occurrences=2) == []

    def test_sidecar_is_jsonl(self, tmp_path):
        e = {"row_id": "1", "field": "Text", "before": "a", "after": "b"}
        p = self._log(tmp_path, "a.jsonl", [e])
        assert json.loads(p.read_text(encoding="utf-8").splitlines()[0]) == e
