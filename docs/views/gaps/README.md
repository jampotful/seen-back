# The gap table

For each of the fourteen offered views, the species people meet most that borrow it, and how close the best evidence comes to each row. Made by `tools/views/gaps.py`.

## Rerun
```
git fetch --depth 1 origin +refs/heads/pub/naturalist-world:refs/remotes/origin/pub/naturalist-world \
  +refs/heads/pub/data-alachua:refs/remotes/origin/pub/data-alachua \
  +refs/heads/pub/lit-table:refs/remotes/origin/pub/lit-table
git fetch --depth 1 origin '+refs/heads/research/*:refs/remotes/origin/research/*'
python3 -I tools/views/gaps.py            # add --no-lit to skip the literature table
```
It reads the evidence logs on the working tree and on every `origin/research/*` branch, drops records the audit retracted (`docs/views/audit/ALL.jsonl`), and rewrites `docs/views/gaps/<view>.md`, `queue.jsonl`, `cells.jsonl` (every cell with its state, for the papers-wanted verdicts) and `summary.json`. Add a genus to `taxonomy-extra.tsv` when a new species has no family or order; the table marks those it filled by hand as `own`, from general knowledge, unchecked against GBIF.

## What each file holds
- `<view>.md`: the 60 borrowing species most recorded worldwide and the 20 most recorded in Alachua County; for each row a grade (`m`, `g`, `i`) and below it, trait by trait, the record behind it and the rule.
- `queue.jsonl`: one line per gap (a species and a trait nobody measured or may carry), with `rows` (how many of the view's rows rest on the trait), `records` (the species' worldwide records), `county_records`, the closest evidence and a `lit_hint` where the automated literature table has the genus. Ranked by `score`, records times rows.
- `rows.json`: each row of each view mapped to trait keys and the carry class of each trait.
- `taxonomy-extra.tsv`: genus, family, order for genera the county list and the evidence lack.

## How the grades are decided
A species is `m` for a trait when a record of grade `m` names the species. It is `g` when a measured congener exists and the trait travels within a genus (rule 3 traits, and rule 2 traits too), or when two or more measured families of its order exist and the trait is a photopigment or receptor count (rule 2). A disagreement (rule 5) is tested crudely: receptor-class counts that differ, or categorical values (pupil, fovea, tapetum, eye type, eye movement, diel) whose first word differs. Numbers are not compared. Family-level evidence never carries; a proposed exception in `docs/views/carry.jsonl` is shown beside the cell and not counted. The literature table (`pub/lit-table`) is automated and unverified: it only adds `lit_hint`.

## Run summary

Records read: 20427 (after dropping 503 the audit retracted); queue lines: 51138.

| View | species in the world rows | records | share covered by the listed species | county records | share covered by the county's 20 | records of listed species with a gap | gap row-records (records x rows in state i) |
|---|---:|---:|---:|---:|---:|---:|---:|
| plant | 141,468 | 44,079,457 | 50.5% | 56,850 | 23.1% | 22,273,484 | 66,505,244 |
| bird | 9,190 | 18,548,533 | 90.3% | 20,542 | 50.5% | 16,743,425 | 55,815,696 |
| insect | 158,004 | 24,749,927 | 54.3% | 55,748 | 19.2% | 13,449,285 | 28,765,854 |
| wader | 852 | 3,172,323 | 100.0% | 12,583 | 96.0% | 3,172,323 | 14,119,101 |
| reptile | 8,623 | 3,091,009 | 93.5% | 9,642 | 85.7% | 2,888,573 | 2,888,573 |
| bee | 12,161 | 2,515,754 | 93.7% | 4,245 | 67.3% | 1,748,562 | 4,891,883 |
| hawk | 302 | 1,568,972 | 100.0% | 3,337 | 100.0% | 1,568,972 | 3,679,307 |
| frog | 4,513 | 1,318,661 | 98.0% | 4,857 | 100.0% | 1,292,499 | 3,470,229 |
| squirrel | 1,282 | 926,361 | 100.0% | 1,187 | 100.0% | 907,108 | 2,011,468 |
| deer | 204 | 684,030 | 100.0% | 1,187 | 100.0% | 676,123 | 1,633,301 |
| dog | 37 | 197,300 | 100.0% | 102 | 100.0% | 197,300 | 395,140 |
| rabbit | 91 | 218,949 | 100.0% | 590 | 100.0% | 195,582 | 195,582 |
| alligator | 27 | 86,487 | 100.0% | 2,781 | 100.0% | 86,487 | 211,839 |
| cat | 45 | 108,884 | 100.0% | 222 | 100.0% | 70,641 | 406,451 |
