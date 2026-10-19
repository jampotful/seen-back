# Audit 70: harvest-54 (branch research/harvest-54, commit 8455c82e)

Gate: `screen_candidates.py --check` on the 70 records and 5 wanted lines prints "0 problems".

## Sample (seed 70, 20 of 70 lines)

Line numbers (1-based): 10, 14, 16, 18, 25, 26, 27, 38, 39, 42, 43, 44, 46, 52, 53, 58, 59, 61, 64, 70.

## Method

For each sampled record I compared `queries` with `harvest_get.py` for the genus (all 20 match word for word, then the family review, then the "web: " searches), checked that each `screened` id appears in the harvest output (all do; the OpenAlex ids come through `screen_candidates.py`), checked `chased` and `canon`, and ran my own searches for the trait. Main's rows were counted from both stores (`docs/views/audit/corrected`, `docs/views/evidence`) with `gbif-names.tsv` for synonyms. About 60 WebSearch calls were used.

## Verdicts, first sample

| Line | Record | Verdict |
|---|---|---|
| 10 | Cameraria corner_hz | ok. Canon names Frolov and Ignatova 2019. The lamp search is recorded. The Nowinszky et al. 2022 chapter (IntechOpen 80625, Table 1, 381 macro-moth species) lists no Cameraria; the queue holds no open spectral_range_nm cell for it. |
| 14 | Pastor fov_h_deg | ok. Canon names Martin 2007, Martin 2017 and Land and Nilsson 2012. My search for Pastor roseus visual field found nothing. |
| 16 | Pastor lambda_max_nm | ok. 11 canon compilations named; none read (leads below). |
| 18 | Ceratina acuity_cpd | ok. The claim of 25 Kelber and Somanathan 2019 rows with none for Ceratina checks out (Apis 12, Apidae 5, Bombus 5, Tetragonula 1, Xylocopa 2). |
| 25 | Pharomachrus cff_hz | ok. Canon includes Haarlem et al. 2026. |
| 26 | Pharomachrus fov_h_deg | ok |
| 27 | Pharomachrus interreceptor_deg | ok. Main holds 13 rows from Odeen and Hastad 2003, none for Pharomachrus (checked). |
| 38 | Fowlea fovea | ok for fovea. Simoes 2016 gives no fovea. |
| 39 | Fowlea lambda_max_nm | **error**. The screened entry says Simoes et al. 2016 (10.1093/molbev/msw148) has no Fowlea. Main holds two lambda_max_nm rows for Xenochrophis piscator from it (RH1 476-489 nm, LWS 560 nm; oa-1, Tables S3 and S5). X. piscator is Fowlea piscator (Reptile Database and Wikipedia list the species under Fowlea). The record itself says the genus was Xenochrophis until recently. The rows are filed under Xenochrophis, which gbif-names.tsv still treats as accepted, so the queue keeps Fowlea open; the record needed to say so instead of "none is a Fowlea". |
| 42 | Herpetotheres acuity_cpd | ok. Five screened entries are off-topic or other genera (snakes, Falco imaging). |
| 43 | Herpetotheres binocular_deg | ok in substance. The Hawk Eyes I claim says main holds 48 rows; I count 22 by DOI (17 by title), for Accipiter, Astur, Buteo and Falco and none for Herpetotheres. The count is wrong and the substance holds; listed, not counted. |
| 44 | Herpetotheres cff_hz | ok. Haarlem et al. 2026 named. |
| 46 | Herpetotheres interreceptor_deg | ok |
| 52 | Lophoceros cff_hz | ok |
| 53 | Lophoceros interreceptor_deg | ok |
| 58 | Lobocleta corner_hz | ok. The lamp search is recorded; Nowinszky Table 1 lists no Lobocleta. |
| 59 | Lobocleta interommatidial_deg | ok |
| 61 | Myzomela binocular_deg | ok. Tyrrell and Fernandez-Juricic S1 table named. |
| 64 | Myzomela interreceptor_deg | ok |
| 70 | Nyctereutes fovea | ok. Hughes 1977 named. Main holds Kopania and Clark 2025 (qrae072) rows for 90-odd mammals and none for Nyctereutes, so that compilation is not a lead for it. |

First sample: 1 error in 20 (5.0%).

## Extension (seed 7001, 15 more, drawn from the 50 unsampled lines)

Lines 8, 9, 11, 15, 19, 28, 30, 31, 41, 60, 62, 63, 65, 68, 69.

All 15 repeat the harvest queries word for word, and their screened ids are in the harvest output. One error:

- 41 Fowlea receptor_classes: same false screened entry for Simoes 2016 ("none is a Fowlea"). Simoes is also canon for receptor_classes and main holds RH1 and LWS rows for X. piscator, so the record's statement is contradicted by main's rows. If the desk treats point 8 as covering this (unread canon compilation, so a lead), the error drops out and the extension has 0 errors.

The other 14 are ok. Telebasis 8 and Ceratina 19 were searched with no hit.

## Rate

- First sample: 1/20 = 5.0%.
- With extension: 2/35 = 5.7%.
- Pooled with audits 43-51 and 55-69 (4 in 537): 6/572 = 1.0%.
- Verdict: the unit fails by a margin of one record (2/35; 1/35 = 2.9% passes if line 41 is read as a canon lead). A single fault source accounts for both: the Fowlea records that screen Simoes 2016 on the strength of the genus name. Fix: Fowlea lambda_max_nm (39) and receptor_classes (41) should name the Xenochrophis piscator rows or leave the cells to the owner's synonym handling. Lines 36, 37, 38, 40 are not affected (acuity, field, fovea, pupil).

## Own searches

Searched in the audit: Cameraria flicker fusion; Pastor roseus visual field; rosy starling spectral sensitivity; Pastor/Sturnus roseus visual acuity; Ceratina visual acuity, compound eye, opsin and eye size; Pharomachrus flicker fusion, visual field, visual acuity, opsin and retina; trogon eye; Nyctereutes retina, visual acuity, visual field, depth, tapetum; Bungarus retina, pupil, visual field; Myzomela opsin, acuity, visual field; honeyeater flicker; Telebasis eye; Herpetotheres; Lophoceros; Lobocleta and Cameraria lamp searches. None returned a measurement for a genus in a record the unit called absent.

## Leads (compilations whose species lists I could not see)

- Veilleux and Kirk 2014 (Brain Behav Evol 83:43-53, online supplementary table 1, acuity of many mammals): Nyctereutes acuity_cpd (66) and fovea (70).
- Odeen and Hastad 2013 (BMC Evol Biol 13:36, canon) and Odeen and Hastad 2010 (wanted): Pharomachrus (28) and Myzomela lambda_max_nm; the latter is on the wanted list.
- Simoes et al. 2016 supplementary tables: Bungarus (33, 35); main holds none for Bungarus. I could not open the supplement.
- Banks et al. 2015 (canon) for Bungarus pupil_shape (34). A Wikipedia mirror (Bionity) says Bungarus "eyes have round pupils"; the Reptile Database pages for Bungarus fasciatus and Fowlea piscator state no pupil shape. Not a reference-database account, so not counted.
- Nowinszky et al. 2022 Table 1: no Cameraria, no Lobocleta (checked from the genus lists the page returned).
- Canon compilations (Haarlem 2026, Tyrrell and Fernandez-Juricic 2017 S1, Caves 2018 and 2023, Martin 2017, Frolov and Ignatova 2019) are named in every record I read.

## Wanted lines (not counted)

Odeen and Hastad 2010 (DOI 10.1007/s00359-009-0474-z, JCP A 196:91-96): title and DOI match the record page. Martin and Coetzee 2004 (Ibis 146:18-26, DOI 10.1111/j.1474-919X.2004.00211.x): matches; species are Bucorvus leadbeateri and Tockus leucomelas, so the wanted line bears on Lophoceros only through the synonym. The other three were not opened.

## Rattus

The unit wrote no Rattus record. Main holds Rattus fovea (methods:1145, Land and Nilsson 2012) and Rattus norvegicus fovea (oa-1:3622, Kopania and Clark) and receptor_classes (canon-3:12, oa-8:105, squirrel-deer-rabbit:65): all for the genus and the trait.
