# oa-11 reading pass, reader G (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md` as it stands on `main` at 3a573fa8 (grade line: `m` for a value on the record's own taxon, a species or the group it names; `g` for a taxon mismatch or a predicted or presumed value; `i` only for a value derived by the reader), with the control room's instruction to run `tools/views/oa_lint.py --text` before each commit. Entries 2, 13, 33, 35, 18, 45 and 19 of `oa-11`, in that order, read from the texts the `oa` job fetched again for this reader (branch `run/oa/read-g`, run 14, `runs/oa/14-oa-11` on `ci`). All seven texts decrypted with matching checksums, and each checksum equals that of run 11 (`runs/oa/11-oa-11`, branch `run/oa/oa11-r2`), so the audit can use either. Reading branch: `agent/oa-read-g`. The key pair lives in `/tmp/oa-g` and was never committed or printed.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 2 | Hall, Kamilar and Kirk 2012, eye shape and the nocturnal bottleneck of mammals (Proc R Soc B 279: 4962-4968) | Europe PMC PDF, published version | 4 | 2 | 2 | 0 | 4 |
| 13 | Wald, Brown and Kennedy 1957, the visual system of the alligator (J Gen Physiol 40: 703-713) | Europe PMC PDF (scanned, OCR text layer), published version | 7 | 5 | 2 | 0 | 3 |

## Notes by paper

- Entry 2. The 266-species table (activity pattern and eye measurements) is in the electronic supplementary material, which the fetched PDF does not include, so no species-level value could be logged. The main text gives group statistics of the corneal diameter to axial length ratio (Table 3) and the discriminant analysis (Tables 1 and 2); eye shape has no key in BRIEF's list and these were not logged. Logged: the two orders the sample shows as entirely nocturnal (Chiroptera, Didelphimorphia; `g`, the sampled species standing for the order, `partial` because the activity data are compiled), and two cited background statements (anthropoid fovea; nocturnal Caprimulgiformes), `m` and `partial`.

- Entry 13. The text layer is OCR of a 1957 scan and garbles units and Greek letters (`),r~= 500 mtt` for λmax = 500 mμ); quotes keep the characters exactly as the file holds them and the notes say what they mean. Logged for Alligator mississippiensis: rod rhodopsin λmax 500 nm from the retinal extract (no cone pigment found), vitamin A1 alone, dark adaptation complete in 5 to 7 minutes by ERG (all `m`, own measurements), and the dorsal tapetum and the rod-dorsal, cone-ventral layout cited from Laurens and Detwiler (1921) (`m`, `partial`). Also the unnamed frog's dark adaptation (30 minutes or longer, `g` under Anura) and vitamin A2 in Pseudemys retinas from the authors' earlier work (`g`, genus only, `partial`). Rhodopsin synthesis rates in solution (alligator, frog, cattle, chicken, scup, butterfish) are biochemistry, not a trait of seeing, and were not logged. New trait keys: `dark_adaptation_min`, `photoreceptor_distribution`; `chromophore` reuses a key other logs already use.

## Next

Entries 33, 35, 18, 45, 19.
