# Audit oa-1018-c: the OA reading pass on agent/oa-read-c

Branch audited: `agent/oa-read-c` (577 evidence lines added to `docs/views/evidence/oa-1.jsonl`, lines 5158 to 5734). Prompt: `docs/tracks/prompts/oa-audit.md` on main, run with 30 lines and `random.seed(1018)`; fetch branch `run/oa/audit-1018-c`; corrections in `docs/views/recheck/recheck-oa-1018-c.jsonl`.

## Sample (drawn before any record was read)

Population: the 577 lines added to `docs/views/evidence/oa-1.jsonl` (`git diff -U0 origin/main...origin/agent/oa-read-c`), in file order; `random.seed(1018)`; `random.sample(lines, 30)`.

| # | id |
|---|---|
| 1 | docs/views/evidence/oa-1.jsonl:5561 |
| 2 | docs/views/evidence/oa-1.jsonl:5562 |
| 3 | docs/views/evidence/oa-1.jsonl:5260 |
| 4 | docs/views/evidence/oa-1.jsonl:5383 |
| 5 | docs/views/evidence/oa-1.jsonl:5482 |
| 6 | docs/views/evidence/oa-1.jsonl:5349 |
| 7 | docs/views/evidence/oa-1.jsonl:5697 |
| 8 | docs/views/evidence/oa-1.jsonl:5578 |
| 9 | docs/views/evidence/oa-1.jsonl:5379 |
| 10 | docs/views/evidence/oa-1.jsonl:5273 |
| 11 | docs/views/evidence/oa-1.jsonl:5555 |
| 12 | docs/views/evidence/oa-1.jsonl:5709 |
| 13 | docs/views/evidence/oa-1.jsonl:5338 |
| 14 | docs/views/evidence/oa-1.jsonl:5306 |
| 15 | docs/views/evidence/oa-1.jsonl:5552 |
| 16 | docs/views/evidence/oa-1.jsonl:5211 |
| 17 | docs/views/evidence/oa-1.jsonl:5597 |
| 18 | docs/views/evidence/oa-1.jsonl:5317 |
| 19 | docs/views/evidence/oa-1.jsonl:5554 |
| 20 | docs/views/evidence/oa-1.jsonl:5530 |
| 21 | docs/views/evidence/oa-1.jsonl:5267 |
| 22 | docs/views/evidence/oa-1.jsonl:5363 |
| 23 | docs/views/evidence/oa-1.jsonl:5483 |
| 24 | docs/views/evidence/oa-1.jsonl:5492 |
| 25 | docs/views/evidence/oa-1.jsonl:5654 |
| 26 | docs/views/evidence/oa-1.jsonl:5657 |
| 27 | docs/views/evidence/oa-1.jsonl:5421 |
| 28 | docs/views/evidence/oa-1.jsonl:5173 |
| 29 | docs/views/evidence/oa-1.jsonl:5528 |
| 30 | docs/views/evidence/oa-1.jsonl:5310 |

## Setup

- The machine had 1.6 GB free, so the repository was cloned blobless (`--filter=blob:none`); nothing else differs.
- The key was made as the prompt says, in `/tmp/oa/a1018c/` instead of `/tmp/oa/`, because `/tmp/oa` on this machine already holds other agents' keys (`a1018b`, `c`). The key and the texts stayed there and were never committed.
- Fetch branch `run/oa/audit-1018-c` (commit f49273c0) changes only `ci/oa/pub.pem` and `ci/oa/list.jsonl`, cut to the five papers behind the sample: oa-1 entries 59, 60, 66 and 68 (matched by DOI) and 19 (matched by title; its list line has no DOI). The oa run 12 returned `runs/oa/12-oa-1`; all five texts decrypted with matching checksums.
- Copies read: 59, Simões et al. 2016, City Research Online accepted manuscript with the supplementary tables (PDF); 60, Para 2026, Carleton MSc thesis (PDF); 66, Ödeen et al. 2011, Europe PMC XML (no layout part); 68, Pecsics and Csörgő 2023, publisher PDF; 19, Futahashi et al. 2015, Europe PMC PDF (the Europe PMC XML returned HTTP 500; the reading run had the PMC HTML page).
- Grades follow BRIEF line 22 and line 62 and `docs/views/audit/SAMPLE.md` ("The rule decided"), as the control room directed on 18 October: a cited, review or compiled value on the record's own taxon is graded by what it reports, and `g` stays only for a taxon mismatch. Typographic differences count as `confirm` and table rows from the layout part are allowed (audit 31; launch prompt).

## Verdicts

Every quote was run through `python3 -I tools/views/quotecheck.py` against its text and then read in its sentence or table row. Table rows were read in the layout part with their column heads.

| # | id | taxon / trait = value | grade, partial | quotecheck | verdict | reason |
|---|---|---|---|---|---|---|
| 1 | oa-1:5561 | Morpho peleides / cff_hz = 115 | m, – | verbatim | confirm | Fig. 1.7 caption states it in words ("Beyond 115 Hz, the photoreceptor response failed to reliably follow the stimulus"); the thesis's own ERG of one individual, as `conditions` says; a stated number, so no figure read |
| 2 | oa-1:5562 | Lepidoptera (A/A colour class) / cff_hz = [65, 107.5] | g, – | verbatim | confirm | whole sentence in 2.4.1; three species of one colour class (Table 2.2), so `g`; the range is stated in the text |
| 3 | oa-1:5260 | Boiga forsteni / lambda_max_nm RH1 = [500, 505] | g, – | verbatim | confirm | Table S3 row; the caption says every λmax is predicted from sequence except those in parentheses; a prediction is `g` |
| 4 | oa-1:5383 | Dipsas catesbyi / lambda_max_nm LWS = 536 | g, – | verbatim | confirm | Table S5 row, predicted |
| 5 | oa-1:5482 | Typhlophis squamosus / diel = not primarily diurnal | m, true | verbatim | confirm | Table S2 row, Primarily Diurnal N; a compiled classification of the record's own species (Starace and Lambert 2013), so `m` with `partial` |
| 6 | oa-1:5349 | Malpolon monspessulanus / lambda_max_nm LWS = [550, 560] | m, true | verbatim | confirm | Table S5 "560 (550-560 )"; the parenthesised value is measured (caption), footnote 4 is Govardovskii and Chkheidze 1989, an MSP study of this species (main text); a cited measurement on the record's species |
| 7 | oa-1:5697 | Hesperornis regalis / monocular_sector_width_deg = 143 | m, – | verbatim | confirm | Table 1, sixth column. Column order checked from the head positions in the layout text and from the text ("the scores of Great Crested Grebe and the extinct Hesperornis were the same on each level"); the model is of H. regalis (Fig. 2); a skull-model estimate, which audit 2 accepted as `m` for this paper's grebe |
| 8 | oa-1:5578 | Photinus pyralis / diel = most active at low light levels | m, true | verbatim (layout row) | confirm | Table A1 row "… 40 ± 10 L"; the caption defines the column as the light levels they are most active (H = high, L = low); compiled, so `partial` |
| 9 | oa-1:5379 | Leptodeira annulata / lambda_max_nm LWS = 536 | g, – | verbatim | confirm | Table S5 row, predicted |
| 10 | oa-1:5273 | Helicops angulatus / lambda_max_nm RH1 = [491, 496] | g, – | verbatim | confirm | Table S3 row, predicted |
| 11 | oa-1:5555 | sea snakes (two species) / lambda_max_nm = 429 | g, true | verbatim | confirm | whole Discussion sentence citing Hart et al. 2012; two unnamed species, so `g` |
| 12 | oa-1:5709 | Hesperornis regalis / blind_area_deg = 50 | m, – | verbatim | confirm | Table 1, sixth column, as row 7 |
| 13 | oa-1:5338 | Python bivittatus / lambda_max_nm LWS = 560 | g, – | verbatim | confirm | Table S5 row with no parenthesised value, predicted |
| 14 | oa-1:5306 | Xylophis captaini / lambda_max_nm SWS1 = UVS | g, – | verbatim | confirm | Table S4 row; the caption defines UVS (λmax c. 360nm); predicted |
| 15 | oa-1:5552 | Serpentes / oil_droplets = absent | g, true | verbatim | **correct** (grade `g` to `m`) | "The eyes of snakes … lacking photoreceptor oil droplets, … (Walls 1942)" puts the fact in snakes as a group, the record's own taxon. A statement about a group's typical members is `m` (BRIEF line 22; SAMPLE.md). Quote, value and `partial` stand |
| 16 | oa-1:5211 | Bachia flavescens / lambda_max_nm RH1 = [491, 496] | g, – | verbatim | confirm | Table S3 row, predicted; the table prints the name this way |
| 17 | oa-1:5597 | Papilio demoleus / cff_hz = [90, 110] | m, true | verbatim (layout row) | confirm | Table A1 row "Lime butterfly Papilio demoleus 90 - 110 H"; a compiled measurement on the record's species |
| 18 | oa-1:5317 | Sibon nebulatus / lambda_max_nm SWS1 = UVS | g, – | verbatim | confirm | Table S4 row, predicted |
| 19 | oa-1:5554 | sea snakes (two species) / filter_pigments = lenses transmit significant amounts of UV | g, true | verbatim | confirm | starts at the sentence's start, cut marked, cites Hart et al. 2012; two unnamed species, so `g` |
| 20 | oa-1:5530 | Boiga forsteni / diel = not primarily diurnal | m, true | verbatim | confirm | Table S2 row, Primarily Diurnal N; compiled (Whitaker et al. 2004) |
| 21 | oa-1:5267 | Leptodeira annulata / lambda_max_nm RH1 = [500, 505] | g, – | verbatim | confirm | Table S3 row, predicted |
| 22 | oa-1:5363 | Chrysopelea ornata / lambda_max_nm LWS = 560 | g, – | verbatim | confirm | Table S5 row printed "Chrysopelea ornate"; the taxon follows the paper's Table S2 and sample list; predicted |
| 23 | oa-1:5483 | Liotyphlops beui / diel = not primarily diurnal | m, true | verbatim | confirm | Table S2 row; compiled (Kley 2003a) |
| 24 | oa-1:5492 | Uropeltis cf. macrolepis / diel = not primarily diurnal | g, true | verbatim | confirm | Table S2 row. The identification is provisional ("cf.") and the cited field guide describes the named species, so `g` is defensible (see judgment calls) |
| 25 | oa-1:5654 | Passerida/Petroicidae / lambda_max_nm SWS1 = UVS | g, – | verbatim | confirm | Discussion sentence from its start, cut marked; the clade's class is the paper's own result ("two major clades, the Passerida/Petroicidae and the suboscines, are homogeneous with respect to colour vision"); `g` for a clade and for a class read from a gene |
| 26 | oa-1:5657 | Malurus / lambda_max_nm SWS1 = VS and UVS species | g, true | verbatim | confirm | Figure 2 caption, two sentences with the cut marked; [40] is Ödeen et al. on fairywrens (Background); genus-level and cited |
| 27 | oa-1:5421 | Thamnophis sirtalis / ocular_media_lambda_t50_nm = 413 | m, – | verbatim | confirm | Table S22: λ50% lens 413, spectacle 340; "All data newly generated for this study" except Pantherophis guttatus |
| 28 | oa-1:5173 | Sympetrum frequens / whole_eye_spectral_peak_nm = 360 | m, – | fail | confirm | the sentence is in the text. The quote reads "S. frequens ," where this copy has "S. frequens,": the reading run had the PMC HTML page, which renders a space after the italic name, so the difference is typographic. The ERG is this paper's own (Methods, Electrophysiology) |
| 29 | oa-1:5528 | Chrysopelea ornata / diel = primarily diurnal | m, true | verbatim | confirm | Table S2 row "N Y N Y ? ?", Primarily Diurnal Y; the row's last cell ("-") is cut with a mark. The note says the cell is N (uncounted, see below) |
| 30 | oa-1:5310 | Thamnophis sirtalis / lambda_max_nm SWS1 = 360 | m, true | verbatim | confirm | Table S4 "UVS (360 )", footnote 4 is Sillman et al. 1997, the garter-snake MSP study; a cited measurement on the record's species |

## Counts

- Verdicts: 29 `confirm`, 1 `correct`, 0 `requote`, 0 `retract`.
- **Errors: 1 of 30, 3.3%** (exact 95% interval 0.1% to 17.2%).
- Of these, `g` given where the rule gives `m` (the reading prompt's narrower grade wording, counted under the rule and given apart as the control room asked): **1** (oa-1:5552). Errors outside that pattern: **0 of 30** (95% interval 0% to 11.6%).
- For transparency: eight `m` records report a cited or compiled measurement on the record's own species (rows 5, 6, 8, 17, 20, 23, 29, 30). The rule confirms them; under the oa-audit prompt's literal wording ("`m` only for one named species measured in this paper") they would be eight more grade errors (9 of 30, 30%).
- Metadata faults (not counted): none. Every `source` object matches `ci/oa/sources-r1.jsonl`, and the two gaps the reader filled are right: the thesis's degree line from its title page, and PNAS pages E1247-E1256 from the page footer.
- Note faults (not counted): oa-1:5528, whose note says the Primarily Diurnal cell is N where the table prints Y; a row in the recheck file fixes the note.

## λmax predicted from an opsin sequence for one named species

Rule applied: grade `g`, never `m`; `method` names the prediction; `partial` is false when the paper made the prediction from its own sequences.

- BRIEF line 170: "an intact gene predicts a pigment and does not measure one; grade and `method` say so". BRIEF line 22 defines `m` as measured in this creature and `g` as measured in a relative or a wider group.
- Audit 2, pattern 3 and row 31 (sweep-6:10, an SWS1 tuning-site class for one named tern): "predicted pigment class is g, never m", the rule from recheck 1.
- SAMPLE.md, "The rule decided", keeps `g` for "a presumption or hypothesis" and "a value borrowed from another animal".
- The paper states what its numbers rest on (Simões et al. 2016, Methods, "Estimating visual pigment λmax"): correlations with pigments whose λmax "has been measured directly in photoreceptors or where opsin genes have been cloned and pigments regenerated in vitro", at tuning sites important "in other vertebrates". The number is a measurement in other animals carried to this species by its sequence, which is what `g` means.

What follows from it: `m` on such a record is a grade error, corrected to `g`. `i` is too low under the same rule and is corrected to `g` too; `i` is for a value the logger derives (a conversion or a mean) or for a guess. A class without a number (UVS, VS) is graded the same way, and the caption's nominal λmax for the class belongs in `note`. A value that the same table puts in parentheses is a measurement (MSP or in vitro), so it is `m` for the named species, with `partial` true when the table cites it (rows 6 and 30). `partial` turns true for a prediction only when the paper reports someone else's prediction or the number is read from a figure. In this sample all 10 predictions (rows 3, 4, 9, 10, 13, 14, 16, 18, 21, 22) carry `g`, `partial` false and a `method` that names the prediction, so none is an error.

**Caution on the mechanical regrade.** `keep_g` in `tools/views/audit_rule.py`, run on these records' `note` and `method` text, keeps `g` for 1 of the 17 sampled `g` records (row 26, through "genus-level") and would send the other 16 to `m`. Those 16 include all 10 predictions, the two unnamed sea-snake records, the A/A colour class and the Passerida/Petroicidae clade. Its pattern has no term for a prediction or for an unnamed or composite taxon, so applied this way it would add about 14 grade errors to these 30. The one record it should change here (row 15) is a group record, so a regrade limited to species-rank records would miss it.

## Judgment calls (not counted)

- Row 24: `g` for "Uropeltis cf. macrolepis". The table puts the classification on the row's own taxon, which argues for `m`; the provisional identification argues for `g`. Under the stricter reading it would add one to the rule-wording tally.
- Row 1: a number stated in words in a figure caption was treated as stated text, so `partial` false.
- Row 11: "c. 429nm" is logged as 429; the quote carries the "c.", and the note could say so.
- Rows 7 and 12: `m` for a skull-model estimate of an extinct species, following audit 2's acceptance of the same paper's estimates.
- Row 25: `partial` false. The paper presents the clade's class as its own result, although its Background cites earlier work finding every investigated Passerida UVS.

## Fault patterns

1. Group statements graded by the reading prompt's "a value given for a genus, family or wider group … is `g` at most": row 15, a general statement about snakes, where BRIEF line 22 and SAMPLE.md give `m`. One instance in 30.
2. Notes copied across rows of one table without checking the cell: row 29 says N where the table prints Y. The value is right, so it is not counted.
3. Quote checks depend on the copy fetched: row 28's quote matches the PMC HTML page the reader had and fails against the Europe PMC PDF this run fetched, by one space. Rechecks should note which copy they used.
4. The pass is table-heavy and accurate on tables. 21 of the 30 come from Simões et al. 2016 (10 sequence predictions, 5 Table S2 classifications, 2 parenthesised measurements, 1 lens λ50%, 3 cited sentences), and every table value matched its row and column. The five Table S2 `diel` records are faithful, but they are coarse evidence: "not primarily diurnal" from field guides does not say nocturnal.

## Recommendation

Merge after applying the counted correction in `docs/views/recheck/recheck-oa-1018-c.jsonl` (oa-1:5552, grade to `m`) and the note fix (oa-1:5528). Do not run `keep_g` over these records' notes as it stands: it would undo the `g` on sequence predictions that BRIEF line 170 and audit 2 require.
