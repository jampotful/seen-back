# Audit 88: desk-c11 (12 plant genera; branch origin/research/desk-c11, head dccf0f78)

## Samples (seed 88), drawn before any record was read

Search records (29 lines): `random.seed(88)`, `random.sample(range(1, 30), 20)`, sorted: 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 21, 24, 26, 27, 28.

Evidence records: all 8 lines of docs/views/evidence/desk-c11.jsonl are judged.

## Gate

`python3 -I tools/views/screen_candidates.py --check docs/views/searched/desk-c11.jsonl --wanted docs/views/wanted/desk-c11.jsonl` prints "0 problems".

(in progress)
