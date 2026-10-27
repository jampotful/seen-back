# oa-14: whole-unit recheck of the oa-14 reading (26 October 2026)

Scope: all 123 records of `docs/views/evidence/oa-14.jsonl` on `origin/research/oa-14` at ebe77bad (24 papers with records, batch entries 3 to 75). Each record was matched to its entry in `docs/tracks/batches/oa-14.json` on that branch by DOI (title as a fallback; every match was checked against the title words in the text), run through `python3 -I tools/views/quotecheck.py` against `/tmp/oa14key/txt/oa-14-<entry>.txt` (123 of 123 passed before any fix: 78 verbatim, 45 as table rows of the layout text), and read against the sentence or table row around its quote, with the Methods read wherever eligibility or the value's source turned on them. Rules: `oa-audit.md`, `oa-read.md`, audits 31 and 39, the oa-13b part 1 and part 2 and oa-13c rechecks, desk-screen points 9 and 10, BRIEF, and the readings in force for this unit (plant `sense_chemical` counts living responses, applied hormones and elicitors included, and volatile signalling, never extracts, oils, cut flowers, cell cultures or excised tissue; plant `eye_type` is "none"; lamp activity comparisons are behaviour, light-trap catch tables stay under `spectral_range_nm`). The decrypted texts were read in place on the build machine; no key was made, no build job ran, and no paper text, PDF or key enters this branch. The branch's own evidence file is untouched.

## Output

`docs/views/evidence/oa-14-checked.jsonl`: 288 records. Lines 1 to 123 are the 123 rechecked records in their original order (none retracted), `"unit": "oa-14"`, the `source` object untouched, with the fixes below applied. Lines 124 to 288 are the 165 rows of entry 56's Table 2, which the reader left unlogged (section below). `python3 -I tools/senses/check.py` reports 0 problems on the file; every quote passes `quotecheck.py` (78 verbatim, 210 as table rows of the layout text), and no quote opens with a cut.

## Counts

| verdict | records |
|---|---|
| confirm | 116 |
| requote | 6 |
| correct | 1 |
| retract | 0 |
| **all** | **123** |

Errors (requote, correct, retract): 7 of 123, 5.7%. Wrong value, taxon, grade or partial flag (correct and retract only): 1 of 123, 0.8%.

## Verdicts other than confirm

Line numbers are those of `oa-14.jsonl` at ebe77bad.

| line | entry | taxon / trait | verdict | reason and fix |
|---|---|---|---|---|
| 23 | 17 | Artiodactyla / behaviour_vision | requote | The value opened "susceptible to the Müller-Lyer illusion", a conclusion the abstract draws two sentences later; the quote gives only the group's preference in experimental trials. Value trimmed to the preference. |
| 24 | 17 | Artiodactyla / behaviour_vision | requote | The same for the Delboeuf illusion. Value trimmed to the preference. |
| 49 | 55 | Mentha arvensis / sense_chemical | requote | "Foliar" came from the sentence before the quote. Value trimmed; the route stays in `method`. |
| 50 | 55 | Mentha arvensis / sense_chemical | requote | The same for KAR1. |
| 89 | 71 | Caragana intermedia / sense_chemical | requote | The value says "in roots"; the quote ("However, CiGAD1 showed a 3.8-fold increase …") does not name the organ, which is in the sentence before. The quote now carries that sentence's opening and its "at 3 h", with a marked cut, 35 words. |
| 91 | 71 | Caragana intermedia / sense_chemical | requote | The value says "in leaves"; the organ is in the sentence before. The quote now opens "In the leaves, however, after 3 h of ABA treatment, …" and keeps the 24 h sentence, 39 words. |
| 100 | 75 | Heliconius sara / lambda_max_nm 550 | correct | `partial` false → true. Table 1 prints 550 with no source footnote, but the abstract says this study measured 12 nymphalids and 1 riodinid, the Methods list the 22 nymphalids of the survey without H. sara, and the Results name H. erato, H. charithonia and H. hecale as the Heliconius sampled. The paper names H. sara only for a published opsin sequence (Hsu et al. 2001; Zaccardi et al. 2006). The value is not shown to be this paper's measurement and its source is unnamed; the note says so. |

Fixed without a verdict (not counted): line 52's note called the species table 'Table 1' (it is Table 2) and now also says that the table lists 11 dipterocarps, with 8 of 11 bearing EFN in the Discussion, where the abstract the record quotes says 12 and 3; the value follows the abstract's sentence and stands. Lines 1 to 3 (entry 3, Campanula floral scent) had `method` "on living plants enclosed in oven bags"; the Methods say only that inflorescences from two to three plants were enclosed together in a polyester oven bag. The method now says what the Methods say, and the note names the gap.

## Checks that held

- Entry 64, Table 3 (lines 71 to 82): every cell read against the layout text, column heads RH1, SWS1 and LWS; the Lampropeltis getula SWS1 cell (c.370, n = 1, footnote a: an estimate from noisy data) is logged as 370 with the footnote in the note, and stands. The Thamnophis sirtalis values (85 to 87) and the Telescopus fallax Table 2 row (83, 84) are partial and name Sillman et al. 1997 and Munk and Rasmussen 1993, both checked against the reference list.
- Entry 75, Table 1 (lines 92 to 123): every λmax cell and footnote read against the layout table. The partial flags follow the footnotes (b, d, f, g, h, i, k), and the unflagged nymphalid records cover 13 species, 12 of which are exactly the 12 nymphalids the abstract and Methods name as measured here. Apodemia mormo (121, 122, footnote j) stays unflagged: the abstract counts it as the one riodinid measured in this study. Heliconius sara is the one unflagged row outside that set (line 100, above).
- The cited references checked against the papers' reference lists: Melin et al. 2016 for the lion's 13.42 cpd (line 60), Awata et al. 2010 for the Parnassius opsins (line 63).
- Eligibility: the scent records of entries 7, 44 and 50 sample inflorescences on the plant (intact flowers attached to the plant; potted plants; plants in their natural habitat); the hormone and elicitor records of entries 21, 55 and 71 treat seeds, whole plants and seedlings. The hairy-root records of entry 40 (38, 39) are light responses of transformed root cultures, which the readings in force exclude only from `sense_chemical`; they stand, and the desk may want to decide whether the culture exclusion should extend to `sense_light_nonvisual`.

## Entry 56, Table 2: 165 records added

Linatoc, Owen and Dalimin 2023 (source object copied from line 52) screen 165 species of the Danum Valley forest for leaf emission of isoprene and monoterpenes and for extrafloral nectaries. Table 2 gives one row per species with columns family, species, habit, VOC emitter (y or n) and EFN bearing (y or n). EFN is not a BRIEF trait, so each row gives one `sense_chemical` record: value "VOC emitter: yes" (131 rows) or "VOC emitter: no" (34 rows), the row quoted as one line of the table (`"5. | Annonaceae | Annona senegalensis Pers. | Tree | n | y"`) with the column heads in `where`, `method` from Methods 2.2 (air drawn for 20 minutes from a Li-COR 6400 leaf chamber on a healthy, fully expanded attached leaf; GC-FID and mass-selective detection), and the habit in `conditions`. The counts agree with the paper's own totals (131 emitters, 41 EFN-bearing, 134 trees, 15 shrubs, 9 herbs, 3 vines, 2 palms, 2 bamboos). Four rows span three lines of the layout text (7, 9, 49, 94) and say so in the note.

- Grades: 114 records are named species, graded `m`, `partial` false. 51 rows name an unidentified species ("Polyalthia sp. 1", "Rosaceae sp."); these are logged at the genus (23) or family (28) the row names, graded `g`, with the row's own label in the note.
- Every note says that only isoprene and monoterpenes were analysed, that the records are constitutive emission from an attached leaf of a living plant logged at the desk's request, and that the paper presents emission as a defence without testing a signalling role (point 10a). The 34 "no" records also carry the paper's caveat that a non-emitter is not necessarily a non-producer.
- **Caution for the desk.** By the checker's own botanical reading (not stated in the paper, which says every species was screened in Danum Valley), 38 named species and 2 genera in the table are native to Africa or the Neotropics and not to Borneo: for example Annona senegalensis, Acacia tortilis, Carapa guianensis, Simarouba amara, Virola sebifera and Warszewiczia coccinea. Each of these 40 records says so in its note. The pattern suggests that the table mixes in species from another study or misidentifies Bornean trees; the desk should confirm the identifications, or hold these 40 records, before they settle any cell.

## Fault patterns

1. **The value carries a word from the neighbouring sentence (6 records: 23, 24, 49, 50, 89, 91).** The oa-13 pattern recurs at a lower rate: an author's conclusion ("susceptible"), an application route ("foliar") and the organ named in the sentence before a "However" or a time-step sentence. In each case the word is true of the paper and absent from the quote.
2. **An unfootnoted cell in a compiled table read as the paper's own (100).** Entry 75's Table 1 mixes this study's measurements with earlier ones and marks the earlier ones by footnote, with one exception. The fix is to check each unflagged row against the paper's own list of species measured.
3. **A method stating a condition the paper does not state (1 to 3, not counted).** "On living plants" was the reader's inference; the same wording in entry 4 led the reader to log nothing. Whether entry 3's scent counts under point 10a depends on whether the inflorescences stayed attached, which the text does not say. The desk should decide entries 3 and 4 together.

Not counted, as in the earlier rechecks: trait keys used loosely (seasonal non-photochemical quenching under `sense_light_nonvisual` at 16 to 19, flower opening times under `diel` at 20 and 21, a warm-then-cool stratification result under `sense_light_nonvisual` at 40), review notes that name a cited study by reference number only (68, where the Europe PMC XML holds no reference list), and line 83, whose compiled ecology cell names no source.

Desk note (27 Oct): the 165 Table 2 records of entry 56 (Danum Valley VOC emitter yes/no) are held off main. Constitutive isoprene and monoterpene emission, with no induction or receiver, is plant physiology; the desk reads plant sense_chemical as living responses and volatile signalling (point 10a), so the table waits for the owner's reading.
