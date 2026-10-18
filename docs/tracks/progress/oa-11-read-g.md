# oa-11 reading pass, reader G (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md` as it stands on `main` at 3a573fa8 (grade line: `m` for a value on the record's own taxon, a species or the group it names; `g` for a taxon mismatch or a predicted or presumed value; `i` only for a value derived by the reader), with the control room's instruction to run `tools/views/oa_lint.py --text` before each commit. Entries 2, 13, 33, 35, 18, 45 and 19 of `oa-11`, in that order, read from the texts the `oa` job fetched again for this reader (branch `run/oa/read-g`, run 14, `runs/oa/14-oa-11` on `ci`). All seven texts decrypted with matching checksums, and each checksum equals that of run 11 (`runs/oa/11-oa-11`, branch `run/oa/oa11-r2`), so the audit can use either. Reading branch: `agent/oa-read-g`. The key pair lives in `/tmp/oa-g` and was never committed or printed.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 2 | Hall, Kamilar and Kirk 2012, eye shape and the nocturnal bottleneck of mammals (Proc R Soc B 279: 4962-4968) | Europe PMC PDF, published version | 4 | 2 | 2 | 0 | 4 |

## Notes by paper

- Entry 2. The 266-species table (activity pattern and eye measurements) is in the electronic supplementary material, which the fetched PDF does not include, so no species-level value could be logged. The main text gives group statistics of the corneal diameter to axial length ratio (Table 3) and the discriminant analysis (Tables 1 and 2); eye shape has no key in BRIEF's list and these were not logged. Logged: the two orders the sample shows as entirely nocturnal (Chiroptera, Didelphimorphia; `g`, the sampled species standing for the order, `partial` because the activity data are compiled), and two cited background statements (anthropoid fovea; nocturnal Caprimulgiformes), `m` and `partial`.

## Next

Entries 13, 33, 35, 18, 45, 19.
