# Fix A, 26 October 2026: record fixes from `2026-10-26-fixes-needed-a.md`

Branch `research/fix-a`, cut from origin/main 9469df54. Every group was checked against the records before any change. No existing evidence file was rewritten; retractions are 28 new lines at the end of `docs/views/audit/ALL.jsonl` (`by: fix-a`), the regraded copies are a new file, and `python3 -I tools/senses/check.py` reports only the nine problems main already had (intake-4-failed and intake-5-failed), plus 22 clean records in the new file. `tools/views/test_rows.py` and `test_apply_audit.py` pass. `papers_refresh.py` was not run.

## A2, duplicates: 3 of 4 retracted

Retracted `oa-1:2566` (repeats 2534: same DOI, taxon, trait, value 48 and quote; its note says it is an "alternate value" from the owl worksheet while holding the same 48, so it is either a repeat or a mistyped 47, and both readings call for retraction), `oa-1:3353` (repeats 3352) and `oa-1:3358` (repeats 3357).

Skipped `oa-1:3349`: it and 3348 hold the same figure from one table cell, but the note of 3348 gives the aquatic phase (433 +/- 4) and the note of 3349 the land phase (433 +/- 2). Those are two observations that happen to share a value, so it is not a repeat. The desk may still choose to retract it.

## A6, opsin records at m under receptor_classes: 22 regraded

All 22 hold: grade m, trait receptor_classes, method says the observation predicts a spectral class and does not measure one (Steck et al. 2024, Vision Research 217: 108367). Mechanism as for the 89 earlier oa regrades: the original is retracted in `ALL.jsonl` (flag `regrade`) and a corrected copy is filed in a new file, `docs/views/evidence/oa-2-regraded.jsonl` (22 lines, grade g, `rechecked` names the original). Copies carry `unit: oa-2-regraded` so their line numbers cannot collide with retractions of `oa-2:<line>` (gaps.py keys a retraction by the record's own `unit` field and its line in its file).

- 17 immunohistochemistry records (`oa-2:3974-3976, 3979-3985, 3987-3993`) went to `receptor_presence`, the key `oa-4:505` uses for retinal immunohistochemistry. Their note says "new trait", as check.py requires.
- 5 transcriptome records (`oa-2:3995-3999`, the "Vis Ops" column of Table 2) went to `opsin_gene_count`, the key `canon-7:1` uses; the value became the integer (4, 3, 3, 3, 4) with units "putative visual opsins".

The trait choices follow those two precedents. The owner or desk may prefer another key; the retractions stand either way.

## A7, plant extract and oil records: 3 retracted

`sweep-13:11` (Convallaria majalis, diethyl ether extract of flowers), `sweep-40:5` (Crithmum maritimum, essential oil by hydrodistillation) and `sweep-40:14` (Oplopanax horridus, root-bark oil by supercritical fluid extraction). Each reports tissue chemistry and no living response; desk-screen.md point 10(a) excludes them.

## A8, held intake *-failed lines: nothing done (note for the control room)

The audit mechanism does not take these lines cleanly. `gaps.py` retracts by `"<unit>:<line>"`, where unit is the record's own `unit` field, and every record in every `intake-*.jsonl` and `intake-*-failed.jsonl` has `unit: "intake"`. A retraction of "intake:3" would hit line 3 of every intake file at once, including the good ones, and no id can name a line of a `-failed` file. (ALL.jsonl's existing "intake-7:16" style ids are matched by `apply_audit.py` through the file name, but gaps.py looks for "intake:16" and so does not drop them.) Two routes remain: have gaps.py and rows.py skip `*-failed.jsonl`, or give the records distinct `unit` values. The file counts are 12, 7, 3, 2 and 5 (intake-2, -4, -5, -6, -8). The check.py problems in intake-4-failed and intake-5-failed (no doi or url) are the same held records.

## A5, undated searched records: 50 dated 13 October 2026

`web-birds.jsonl` (16), `web-herps.jsonl` (13), `web-mammals.jsonl` (21) each gained `"date": "2026-10-13"` on every line, appended to the line text with nothing else changed (checked by parsing both versions). QUEUE.md row 16a states that the web searches for mammals, birds and herps ran on 13 October, 16:25 to 16:50. These three searched files had no other write mechanism, so they were edited in place.

## B1, wanted-line row titles: stopped

Ten sampled lines and a count over all wanted files (273 row labels across 14 views that rows.json does not list) show no clear rule. The labels were written freely (`bird:Photoreceptors`, `bird:Acuity`, `bird:Fovea`, `bird:Head movement`, `insect:Colour`, `deer:Dim light`) and a live title cannot be chosen without a judgment for each (does `bird:Fovea` belong under Sharpness or Field of view? `insect:Colour` has no insect row at all). The one mechanism, `wanted/fixes.jsonl`, matches on first author and year and sets fields on the merged download list in `wanted_csv.py`; that script does not output `rows`, `gain.py` skips the file, and a match by paper would rewrite the rows of every wanted line for the paper at once. Nothing was written.

## Also noticed, not changed

`evidence/oa-regraded.jsonl` carries the units of the originals (`oa-1`, `oa-7`), so its line N shares a key with `<unit>:N`. Six of its 89 lines have a key that the earlier regrade retracted, so gaps.py drops those six corrected copies along with their originals. The control room should check which cells that touches.

## Skipped by instruction

A3 (needs new sourced records), A4 (needs paper text), anything in `docs/views/gaps/`, `src/`, `views/*.json`, taxonomy-extra.tsv.

## Desk follow-up, 27 October 2026 (checked at 19:00 UTC)

The collision noted under "Also noticed" is closed. gaps.py now takes the unit for a retraction key from the evidence file name (`take(f[:-6], ...)`), so a line of `oa-regraded.jsonl` is keyed `oa-regraded:N` and no longer matches a retraction of `oa-1:N`. A rerun of the key match over all 89 regraded lines found 58 equal to an `oa-1:N` retraction under the old rule and none under the current one. A8 (the `*-failed` intake files) is closed by the same change, since gaps.py skips them. B1 went to Codex data-1 and its 210 fixes lines are merged. A3 and A4 stay open: A3 needs new sourced records and A4 needs paper text.
