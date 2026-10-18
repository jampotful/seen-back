# Audit 47, 18 October 2026: harvest-33 (desk-screen unit)

The unit is branch research/harvest-33 at commit 71eb012b: 35 search records (docs/views/searched/harvest-33.jsonl) and 26 wanted lines (docs/views/wanted/harvest-33.jsonl). I read the files with `git show 71eb012b:<path>` and compared them byte for byte with the copies saved at /tmp/au47/ (identical). The audit worktree /tmp/wsau47 was cut from origin/main and edits only this report. No ResearchGate, academia.edu, Sci-Hub or LibGen page, library login or library proxy mirror was opened, and no paper text is committed.

## Gate

`python3 -I tools/views/screen_candidates.py --check /tmp/au47/harvest-33.jsonl --wanted /tmp/au47/harvest-33-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample

All 35 search record lines (1-based line numbers), `random.seed(47)`, `random.sample(lines, 20)`. The draw used the line count only and was written here before any record was read. The same call reproduces the published draws of audits 43 (seed 43, 37 lines) and 46 (seed 46, 40 lines).

Draw order: 23, 5, 28, 30, 19, 11, 9, 17, 13, 27, 20, 2, 14, 22, 1, 4, 21, 29, 16, 31

Sorted: 1, 2, 4, 5, 9, 11, 13, 14, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31

The 15 lines left out are 3, 6, 7, 8, 10, 12, 15, 18, 24, 25, 26, 32, 33, 34 and 35. They are the pool for the seed-4701 extension if an error turns up in the first 20.

(Verdicts, counts and the pooled rate follow once the records are read.)
