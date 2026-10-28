# The gap table

For each of the fourteen offered views, the species people meet most that borrow it, and how close the best evidence comes to each row. Made by `tools/views/gaps.py`.

## Rerun
```
git fetch --depth 1 origin +refs/heads/pub/naturalist-world:refs/remotes/origin/pub/naturalist-world \
  +refs/heads/pub/data-alachua:refs/remotes/origin/pub/data-alachua \
  +refs/heads/pub/lit-table:refs/remotes/origin/pub/lit-table
python3 -I tools/views/gaps.py            # add --no-lit to skip the literature table
```
It reads the working-tree evidence logs (excluding held `*-failed.jsonl`); `--with-branches` explicitly includes pending `origin/research/*` evidence for comparison only. It drops records the audit retracted (`docs/views/audit/ALL.jsonl`), and rewrites `docs/views/gaps/<view>.md`, `queue.jsonl`, `cells.jsonl` (every cell with its state, for the papers-wanted verdicts) and `summary.json`. Add a genus to `taxonomy-extra.tsv` when a new species has no family or order; the table marks those it filled by hand as `own`, from general knowledge, unchecked against GBIF.

## What each file holds
- `<view>.md`: the 60 borrowing species most recorded worldwide and the 20 most recorded in Alachua County; for each row a grade (`m`, `g`, `i`) and below it, trait by trait, the record behind it and the rule.
- `queue.jsonl`: one line per gap (a species and a trait nobody measured or may carry), with `rows` (how many of the view's rows rest on the trait), `records` (the species' worldwide records), `county_records`, the closest evidence and a `lit_hint` where the automated literature table has the genus. Ranked by `score`, records times rows.
- `rows.json`: each row of each view mapped to trait keys and the carry class of each trait.
- `taxonomy-extra.tsv`: genus, family, order for genera the county list and the evidence lack.

## How the grades are decided
A species is `m` for a trait when a record of grade `m` names the species. It is `g` when a measured congener exists and the trait travels within a genus (rule 3 traits, and rule 2 traits too), or when two or more measured families of its order exist and the trait is a photopigment or receptor count (rule 2). A disagreement (rule 5) is tested crudely: receptor-class counts that differ, or categorical values (pupil, fovea, tapetum, eye type, eye movement, diel) whose first word differs. Numbers are not compared. Family-level evidence never carries; a proposed exception in `docs/views/carry.jsonl` is shown beside the cell and not counted. The literature table (`pub/lit-table`) is automated and unverified: it only adds `lit_hint`.

## Run summary

Records read: 20396 (after dropping 4293 the audit retracted); queue lines: 4474.

| View | species in the world rows | records | share covered by the listed species | county records | share covered by the county's 20 | records of listed species with a gap | gap row-records (records x rows in state i) |
|---|---:|---:|---:|---:|---:|---:|---:|
| bird | 9,190 | 18,548,533 | 32.6% | 20,542 | 50.5% | 6,053,643 | 19,358,298 |
| plant | 141,468 | 44,079,457 | 9.8% | 56,850 | 23.1% | 4,330,534 | 12,349,081 |
| insect | 158,004 | 24,749,927 | 14.6% | 55,748 | 19.2% | 3,625,051 | 7,660,536 |
| wader | 852 | 3,172,323 | 83.0% | 12,583 | 96.0% | 2,632,752 | 12,867,048 |
| reptile | 8,623 | 3,091,009 | 51.7% | 9,642 | 85.7% | 1,597,706 | 1,597,706 |
| bee | 12,161 | 2,515,754 | 58.1% | 4,245 | 67.3% | 1,461,176 | 4,451,937 |
| hawk | 302 | 1,568,972 | 89.3% | 3,337 | 100.0% | 1,401,801 | 3,885,418 |
| frog | 4,513 | 1,318,661 | 70.4% | 4,857 | 100.0% | 928,800 | 2,705,548 |
| squirrel | 1,282 | 926,361 | 89.2% | 1,187 | 100.0% | 826,403 | 1,878,400 |
| deer | 204 | 684,030 | 95.4% | 1,187 | 100.0% | 652,330 | 2,555,004 |
| rabbit | 91 | 218,949 | 99.9% | 590 | 100.0% | 218,739 | 218,739 |
| dog | 37 | 197,300 | 100.0% | 102 | 100.0% | 197,300 | 481,696 |
| cat | 45 | 108,884 | 100.0% | 222 | 100.0% | 108,884 | 695,288 |
| alligator | 27 | 86,487 | 100.0% | 2,781 | 100.0% | 86,487 | 296,025 |
