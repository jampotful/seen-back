# Progress: audit3 (burst 9)

This note lives in `docs/views/audit/` because the burst 9 prompt keeps every other folder under `docs/views/` unchanged today.

- Started 14 October 2026, 11:55 US Eastern, on `agent/audit3`.
- Done: the literature collection is checked out; the sample is next.
- Next: draw the sample of the 820 `m`-to-`g` rows, read each passage, judge, count.
- 12:00: sample of 124 `m`-to-`g` rows drawn (`tools/views/audit_sample.py`, seed 9) and read; 109 too strict, 14 right, 1 wrong for another reason. Next: the narrower rule, the 37 `g`-to-`m` rows, the corrected copies.
- 12:30: done. Narrower rule (`tools/views/audit_rule.py`), `decisions.jsonl` (767 rows), `apply_audit.py --decisions` with its test, `corrected/` for all 20 logs, `SAMPLE.md`. Nothing further on this track.
