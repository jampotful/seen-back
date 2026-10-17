# Precision audit 29, 17 October 2026

Scope: the units that Codex pull request #20 adds (oa-1, oa-2, oa-3, oa-5, oa-6, oa-9, oa-10 evidence; harvest-c1 to c6 evidence and searched files). Sampling with Python `random.seed(29)`: first 20 records stratified (oa-1 x3, oa-2 x3, oa-6 x3, oa-9 x3, oa-10 x2, harvest-c evidence x3, harvest-c search x3), then, because errors were found, a second draw of 15 (the remaining records of the first pooled draw with the same seed). The oa-none files hold sources only, not evidence, so no none-variant records exist to audit.

Method as in audit 16 and audit 27. Open sources came from URLs returned by WebSearch. Blocked or unanswered: PubMed Central (permission step), Figshare, data.nhm.ac.uk CSV, jstage, Springer PDF, Europe PMC REST. Open and read: Purdue PDF (Fernandez-Juricic 2010), Birmingham PDFs (Cantlay 2023, Potier 2023), Frontiers PDF, Springer full text (Streinzer 2016), cris.unibo.it PDF (Lozano-Castellanos 2025), UCL PDF (Schott 2024), AGRIS, KU pure, NHM dataset page, ICO proceedings page, and the public GitHub data (Perrin et al.). The harvest queries were recomputed with `tools/views/harvest_get.py` from the ci branch. Per audit 27, a compiled or review read without `partial: true` counts as `correct`.

## Table (first 20)

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| oa-1:8981 | Corvus brachyrhynchos / monocular_exclusive_h_deg 129.5 | i | retract | quote is a gloss, not in the paper; the text gives binocular 42 deg and blind area +164% and no lateral value; Fig. 3 has no numeric labels in its caption |
| oa-1:1248 | Bucephala albeola / visual_field_margin_separation_deg 23.5 | m | unverifiable | Figshare CSV blocked; authors complete (8), vol 290 confirmed, issue 2006 missing |
| oa-1:5667 | Chiromantis rufescens / opsin_gene_recovery | m | correct | author list ends "et al."; the MBE print lists 28 authors. S1 cell not seen |
| oa-2:2452 | Acanthophis antarcticus / diel | m | unverifiable | Banks 2015 Table S1 blocked (PMC) |
| oa-2:3461 | Arabidopsis thaliana / sense_light_nonvisual | g | unverifiable | Springer ESM not reachable |
| oa-2:2482 | Cacophis harriettae / diel | m | unverifiable | as oa-2:2452 |
| oa-6:296 | Glossina morsitans / cff_hz 176 | m | correct | systematic-review supplement read, primary not opened, no `partial` |
| oa-6:89 | Eugonatonotus crassus / cff_hz 24 | m | correct | same |
| oa-6:523 | Strix aluco / binocular_vertical_extent_deg 70 | m | correct | review table (an image) without `partial`; the page text gives the vertical binocular field as 80 deg, so 70 needs a second look |
| oa-9:2817 | Papaver rhoeas / sense_light_nonvisual | g | correct | row 266 of appendix1.xlsx matches (ld); compiled from Laurie and Poesch 1932, original not opened, no `partial` |
| oa-9:3219 | Punica granatum / sense_light_nonvisual | g | correct | row 668 matches (sd); same fault |
| oa-9:3404 | Acaena sp. A / germination 22/30 | i | confirm | RawBinaryGermData.csv: 30 rows for K.N.P.A at 6L/18D, 22 germinated; first row matches the quote |
| oa-10:10 | Sinomicrurus japonicus / lambda_max_nm 551 | g | unverifiable | value lives in a figure image; composite quote with ellipsis |
| oa-10:17 | Laticauda frontalis / lambda_max_nm 484 | g | unverifiable | same |
| harvest-c1:7 | Campanula medium / sense_chemical | m | unverifiable | metadata correct (5 authors, BMC Plant Biol 16:117); Fig. 1 and abstract support insensitivity at 0 to 0.1 uL/L; quoted sentence not seen |
| harvest-c2:29 | Portulaca umbraticola / sense_chemical | m | correct | record has no journal; Hort J 85(1):70-75; abstract says "both SR and SCR", so the quote's "both cultivars" is unverified |
| harvest-c5:21 | Calendula officinalis / sense_light_nonvisual | m | requote | quote is a fragment of a Simple Summary sentence, `where` says Results and Discussion; no journal field |
| search harvest-c1:15 | Nymphalis / cff_hz | | correct | four trait queries match; the harvest family-review query "Nymphalidae vision review" is missing (another phrasing used) |
| search harvest-c3:45 | Tilia / eye_type | | confirm | the three harvest queries are word for word; plant family review and common-name step added; three chased DOIs |
| search harvest-c5:22 | Elymnias / interommatidial_deg | | correct | queries match; chased says "no measured relative", but Pararge aegeria and Precis almana are measured Nymphalidae |

First draw: 20 records, 7 unverifiable, 13 verifiable, 11 errors (5 of them only a missing `partial` flag).

## Second draw (15)

| id | taxon / trait | verdict | note |
|---|---|---|---|
| oa-10:367 | Ptilotrigona occidentalis / eye_type | requote | quote cuts "...subunits, called ommatidia (Land 1997)." mid-sentence; Springer full text read |
| oa-1:3400 | Xenopus laevis / photoreceptor_fraction_pct | requote | fragment; review read without `partial` |
| oa-2:3412 | Sorex / receptor_classes | correct | review table, no `partial` |
| oa-3:67 | Salvelinus fontinalis / cff_hz | correct | Lafitte compilation, no `partial` |
| harvest-c4:24 | Berteroa incana / diel | correct | explicitly secondary risk assessment, no `partial`; spacing lost ("than14hours") |
| oa-1:2495, 2843, 612, 1060 | owl, raptor and duck field values | unverifiable | spreadsheets on Figshare blocked; Potier text gives no Milvus value |
| oa-2:1869, 1803; oa-9:1144, 1380 | amphibian pupil shape | unverifiable | NHM CSV blocked; authors match the dataset page |
| oa-6:758 | Euploea mulciber / eye_parameter_um | unverifiable | Table 2 not reachable |
| harvest-c3:17 | Bufo cryptotympanicus / pupil_shape | unverifiable | Appendix S2 not reachable |

Second draw: 15 records, 9 unverifiable, 6 verifiable, 5 errors.

## Error rate

- First 20: 11 errors in 13 verifiable records (85%).
- Both draws: 16 errors in 19 verifiable records (84%); 16 of 35 unverifiable. Without the missing-`partial` faults (8 of the 16): 8 of 19 (42%).
- The threshold of 5% is not met on any counting.

## Systematic faults

1. Compiled, review or table reads without `partial: true`: 8 of the 16 errors (oa-6 Lafitte rows, Martin and Katzir, Jacobs, Mohun, Perrin rows, Berteroa, oa-3 Lafitte). This is the audit 27 fault again; a script could set the flag where `note` says "secondary", "review", "compilation" or "not the primary study".
2. Bibliographic fields: harvest-c2 (34 of 39) and harvest-c5 (28 of 28) have no `journal`; 48 of 105 in harvest-c3 and 20 of 60 in harvest-c1 have a journal without a volume; oa-2 and oa-9 mostly cite a data portal with no volume; "et al." in an author list (oa-1:5667); Proc R Soc B records lack the issue number.
3. Quotes that are fragments or glosses: oa-10:367, oa-1:3400, harvest-c5:21 (also the wrong section), and oa-1:8981, whose quote is a constructed label.
4. Search records: a harvest query rewritten (Nymphalis) and a "no measured relative" claim that the evidence files contradict (Elymnias).

## Recommendation

Do not merge PR #20 yet. The error rate is far above 5%, but the faults are mechanical: a script for `partial` and `journal`, plus the 16 rows in `docs/views/recheck/recheck-29.jsonl`, would clear most of them. The 16 unverifiable records are mostly spreadsheet and CSV cells that this session could not open; they need a session with Figshare and NHM access.
