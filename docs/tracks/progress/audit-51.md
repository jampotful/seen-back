# Audit 51, 18 October 2026: harvest-38 (desk-screen unit)

Unit: branch research/harvest-38 at commit d2a453d6, 32 search records (docs/views/searched/harvest-38.jsonl) for 12 genera (Alauda, Allograpta, Rissa, Spizelloides, Hypolimnas, Myadestes, Agrius, Corizus, Catopsilia, Decticus, Alaus, Spiza) and 18 wanted lines (docs/views/wanted/harvest-38.jsonl). The commit message also names Platalea, Tenodera and Dissosteira, which have no search records. I read both files with `git show d2a453d6:<path>` and saved copies to /tmp/au51/ (byte-identical to the committed files, checked with cmp). The audit worktree /tmp/wsau51 was cut from origin/main (c074d019) and edits only this report.

(This file is being written in stages. The gate and the sample come first, drawn before any record was read; the verdicts and the look-hard pass follow.)

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au51/harvest-38.jsonl --wanted /tmp/au51/harvest-38-wanted.jsonl` printed "0 problems". The worktree holds main's current test (placeholder titles and authors in wanted lines, and failed harvest steps), so the unit passes the stricter gate. The unit goes on to the sample.

## Sample (step 2)

All 32 search record lines (1-based line numbers), `random.seed(51)`, `random.sample(lines, 20)`. The draw used the line count only, and it is written here before any record was read.

Draw order: 16, 27, 17, 18, 6, 8, 31, 29, 9, 13, 25, 15, 22, 30, 11, 12, 23, 5, 7, 19

Sorted: 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 22, 23, 25, 27, 29, 30, 31

The 12 lines left out are 1, 2, 3, 4, 10, 14, 20, 21, 24, 26, 28 and 32. They are the whole pool of the 12-record extension (`random.seed(5101)`), which runs only if the first 20 turn up an error.
