# Round 3: a genus sweep (Sonnet, medium effort, run as a local agent because it needs the web)

Read `docs/views/research/THOROUGH.md` (the protocol) and the Round 2 section of `docs/views/research/BRIEF.md` (records, grades and carry rules). Your launch prompt gives a batch file made by `tools/views/sweep_batches.py`: about 40 genera, each with its open traits, species and nearest measured record. Your branch is `research/sweep-<n>`. Push at least every 15 minutes.

For each genus, in the batch's order, run the protocol once for all its open traits:
1. Canon: check `docs/views/research/canon.jsonl` and the evidence logs for the genus in the compilations already in hand.
2. Search the scientific name and the common name with the traits' words (combined queries are fine), and read the first 20 titles of each.
3. Chase the nearest measured record's source for later work naming the genus, or find a review of the family.
4. Log what you find:
   - a measurement you can open goes to the evidence log through `tools/senses/addlog.py`;
   - a measurement you cannot open goes on `docs/views/wanted/sweep-<n>.jsonl` with `for`, `rows`, `records` and `get`;
   - for each trait with nothing found, write a search record with the full protocol (`level`, `queries`, `where`, `canon`, `chased`, `found`, `date`) to `docs/views/searched/sweep-<n>.jsonl`.
   - `chased` is never empty. Put the DOI of the work whose citations or reference list you checked; when the genus has no measured relative anywhere (the batch's `closest` is empty), name the family review you checked instead, or write `"none: no measured relative and no family review found"` with the places you looked in `where`. A record with an empty `chased` counts as half-searched and the genus is swept again later.
5. Never request a paper marked `n/a` in `docs/views/papers-status.jsonl`.

Final message, at most 150 words: genera done, cells closed by a measurement, cells exhausted, wanted lines added, and the last commit.
