# OA reading pass, batch oa-9, reader d (18 October 2026)

Branch `agent/oa-read-d`, made from `main` at c640337. Prompt: `docs/tracks/prompts/oa-read.md`. Entries assigned: 3, 7, 8, 9, 14, 19, 20, 23, 25, 26, 34, 51, 53. The oa job ran from `run/oa/read-d` (run 5, `runs/oa/5-oa-9` on `ci`), and 12 of the 13 texts decrypted with matching checksums.

## Counts

- Papers with text: 12 of 13. Read in full: 10. Abstract only: 2 (entries 20 and 34; see below). Not fetched: 1 (entry 14).
- Records logged in `docs/views/evidence/oa-9.jsonl`: 400. Grades: 317 `m` and 83 `g`, with no `i`. Partial: 213. Access: 395 `open` and 5 `abstract`.
- Every record passed `tools/views/quotecheck.py` against its own text (400 verbatim), `tools/senses/check.py`, and `tools/views/oa_lint.py` with `--text` and `--since-main HEAD` (0 faults).
- Papers with no measurement of a BRIEF trait: none. Entry 7 holds only one cited group value.

| Entry | Paper | Read | Records | m | g | partial |
|---|---|---|---|---|---|---|
| 3 | Thomas et al. 2022, amphibian pupil shapes | full text (bioRxiv preprint) | 29 | 9 | 20 | 7 |
| 7 | Thomas et al. 2020, frog eye size (Dryad entry) | full text of the article (PMC) | 1 | 0 | 1 | 1 |
| 8 | Warraich et al. 2020, sea turtle visual fields | full text | 22 | 22 | 0 | 2 |
| 9 | Perrin et al. 2025, photoperiod sensitivity | full text (Europe PMC) | 16 | 14 | 2 | 2 |
| 14 | Ranade et al. 2013, Pinus taeda microarray | not fetched | 0 | | | |
| 19 | Stöckl and Kelber 2019, hawkmoth review | full text (Europe PMC) | 103 | 83 | 20 | 103 |
| 20 | Vermeulen et al. 2008, Potentilla reptans | abstract only | 3 | 3 | 0 | 3 |
| 23 | Hornych et al. 2021, fern antheridiogens | full text (Europe PMC) | 129 | 112 | 17 | 29 |
| 25 | Plotsker et al. 2026, parrot ophthalmology review | full text (BioOne PDF) | 19 | 14 | 5 | 19 |
| 26 | Bischoff et al. 2014, Ipomopsis floral scent | full text (PMC) | 21 | 17 | 4 | 10 |
| 34 | Nishimura et al. 2023, owl retinas | abstract only | 2 | 2 | 0 | 2 |
| 51 | Portugal et al. 2023, African Harrier-Hawk | full text (CentAUR, published version) | 8 | 6 | 2 | 5 |
| 53 | Hart et al. 2016, emu visual pigments | full text (PMC) | 47 | 35 | 12 | 30 |

## Not read, or read only in part

- **Entry 14** (Pinus taeda cDNA microarray): the oa job could not fetch it. scirp.org and doi.org both returned 403 (`lookup.jsonl`, run 5). It has no source line and no records.
- **Entry 20** (Potentilla reptans): the fetched copy is the Wageningen research-portal page, which carries the abstract and no full text. Its three records are partial with access `abstract`. The source line has `"skipped": "full text not in the fetched copy"`, so `gain.py` does not count the paper as read.
- **Entry 34** (owl retinas): the fetched copy is the BioOne landing page, where the article is open to subscribers only. I logged the two topography values from the abstract (partial, access `abstract`) and filled pages 35-44 from that page. The source line carries the same `skipped` field.
- **Entries 3 and 7** are data-set entries. The batch titles name the NHM pupil data set and the Dryad trait file. The oa job fetched the articles instead (the bioRxiv preprint of entry 3 and the PMC article for entry 7), so the per-species data in those data sets are still unread. Both source lines say so. Entry 7's line carries the Dryad DOI from `sources-r1`, so it may mark the data set read on the papers page. The control room should decide whether that line should retire the entry.
- Entry 7's `sources-r1` record had no authors, year or journal. I filled them from the PMC page: Thomas KN, Gower DJ, Bell RC, Fujita MK, Schott RK, Streicher JW; 2020; Proc Biol Sci 287(1935): 20201393. Entry 19's text gives no volume or pages, so its journal field has none, and each note says why.

## Points for the audit

- Paper 25's PDF text prints the degree sign as "8", so 30° appears as "308". Its six degree values are written in words (for example "thirty degrees") so the digit-based checks can match them, and each note says so.
- Paper 53's abstract gives the emu UVS peak as 376 nm. The Results, the Fig. 1 caption and the SWS1 section all give 367 nm. I logged 367 nm and noted the difference.
- Paper 9's Results say eleven of 67 species were significantly photoperiod-sensitive, and its Discussion says 12. Only the named species were logged.
- Paper 51 (Polyboroides typus): the maximum binocular width of 27° is in the text. The 120° vertical extent comes from a Fig. 1 label (partial, "read from Fig. 1"). The three other species in that figure are labelled by common name only and were not logged.
- Table rows were quoted as one line of the table. Paper 8's Table 3 row is broken across two layout lines, so its quote joins the row label to the values line with a cut mark. Paper 23's Table 1 gives 100 records, one for each tested source.
- New-trait keys: `pupil_shape` (29 records, paper 3) and `ocular_media_t50_nm` (1 record, paper 53), each marked "new trait" in its note.
- This machine runs other readers at the same time, so the key and texts were kept in `/tmp/oa-d` instead of `/tmp/oa`. That keeps another reader's key from overwriting this one. No key, PDF, XML or text was committed.

## Next

1. Fetch entry 14 again on a later oa run, or get it through the library.
2. Read the data sets behind entries 3 (NHM pupil data) and 7 (Dryad `Thomas_species_traits.csv`) for per-species pupil shape and activity pattern.
3. Get the full texts of entries 20 and 34 through the library (petiole responses; owl RGC maps and acuity).
