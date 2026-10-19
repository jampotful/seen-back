# Audit 71: harvest-54b (branch research/harvest-54b, commit 4f37ea61)

Gate: `screen_candidates.py --check` on the 68 records and 5 wanted lines prints "0 problems".

## Sample (seed 71, 20 of 68 lines)

Line numbers (1-based): 2, 4, 6, 13, 17, 20, 24, 33, 34, 39, 42, 45, 49, 53, 57, 58, 61, 65, 66, 67.

## Method

For every sampled record I compared `queries` with `harvest_get.py` for the genus (the harvest queries match word for word; the family review is the unit's one extra entry and the harvest prints it as a "family review" line), checked each `screened` id against the harvest output and `screen_candidates.py` (the three W ids come from the latter), checked `chased`, and compared `canon` with the canon file for the trait (every record names the compilations that cover its taxon; the ones left out cover other taxa, such as Anseriformes for Pharomachrus). Main's rows were counted in both stores (docs/views/audit/corrected, docs/views/evidence) under the genus name and its older or newer names (Xenochrophis, Tockus, Sturnus roseus), with the species names. About 40 WebSearch calls and 20 fetches of returned URLs were used.

## Verdicts, first sample

| Line | Record | Verdict |
|---|---|---|
| 2 | Physocephala cff_hz | ok. Laughlin and Weckstrom 1993 (Diptera) and Haarlem 2026 named. Own search found no conopid flicker value. |
| 4 | Physocephala interommatidial_deg | ok. Own search found no Physocephala eye measurement. |
| 6 | Telebasis cff_hz | ok. Haarlem 2026 named; Ischnura referee report is off topic. |
| 13 | Pastor cff_hz | ok. Haarlem 2026 named; 18 screened entries are off topic. Own search for rosy starling flicker found nothing. |
| 17 | Pastor spectral_range_nm | ok. Eight canon compilations named. Main holds no Pastor or Sturnus roseus row. Odeen and Hastad 2013 and Odeen, Hastad and Alstrom 2011 (oa-4 holds 137 rows of the latter, none Sturnus roseus) are leads below. |
| 20 | Ceratina corner_hz | ok. Frolov and Ignatova 2019 named. |
| 24 | Pharomachrus binocular_deg | ok. Tyrrell and Fernandez-Juricic S1 and Martin 2007 and 2017 named. Own search for quetzal visual field found nothing. |
| 33 | Bungarus lambda_max_nm | ok. Main's 83 Simoes taxa include no Bungarus. Opsin searches found no krait. |
| 34 | Bungarus pupil_shape | ok. I opened the Madhya Pradesh Snake Research Organization accounts of Bungarus caeruleus (page 91, "eye entirely black", no pupil) and B. fasciatus (page 92, no eye sentence). No pupil statement for the genus found. Banks et al. 2015 species list is a lead. |
| 39 | Fowlea pupil_shape | **error**. The record searched "Xenochrophis pupil shape" and found none. The Portal for Reptiles of Madhya Pradesh page for Xenochrophis piscator (mpforest.gov.in/mpsbb/snakes/90.html, Snake Research Organization, Ujjain) states in its diagnostic characters "Eyes has round pupil." Main's precedent counts such a species account for pupil_shape (reptilesofaz.org for Rhinocheilus, sweep-56#5; audit 64#8). Main holds no Xenochrophis or Fowlea pupil row. The record's note says species pages in the results were not opened. |
| 42 | Herpetotheres cff_hz | ok. Haarlem 2026 named. |
| 45 | Megacopta acuity_cpd | ok. Feller et al. 2021 citation step run. |
| 49 | Lophoceros acuity_cpd | ok. Tockus searched too. Main holds only Tockus leucomelas binocular_deg (Martin 2007), which bears on no record in the sample; the unit left binocular_deg and fov_h_deg to the Martin and Coetzee 2004 wanted line. |
| 53 | Lophoceros spectral_range_nm | ok. Own searches for hornbill opsin or spectral sensitivity found only fields papers. |
| 57 | Lobocleta interommatidial_deg | ok. Lamp search recorded. |
| 58 | Myzomela acuity_cpd | ok |
| 61 | Myzomela fov_h_deg | ok |
| 65 | Nyctereutes binocular_deg | ok. Heesy et al. 2011 named. |
| 66 | Nyctereutes depth_cue | ok. Nityananda and Read 2017 named. |
| 67 | Nyctereutes fov_h_deg | ok. Hughes 1977 named. |

First sample: 1 error in 20 (5.0%).

## Extension (seed 7101, 15 of the 48 unsampled lines)

Lines 3, 7, 26, 28, 29, 32, 36, 40, 43, 46, 50, 54, 56, 62, 63.

All 15 repeat the harvest queries word for word and their screened ids are in the harvest output. No error.

- 36 Fowlea acuity_cpd (extra care): the screened entry for Simoes 2016 still says "none is a Fowlea", which is false (main holds two lambda_max_nm rows and one diel row for Xenochrophis piscator from it, oa-1:5253, 5362, 5507). The conclusion stands, because Simoes reports no acuity and main holds no Xenochrophis acuity row. A wording defect, listed and not counted. Line 38 (fovea) carries the same sentence and the same verdict.
- 37 Fowlea fov_h_deg was not drawn; my searches (checkered keelback visual field, Fowlea retina, fovea, Xenochrophis acuity, ocular media) found no field, acuity or fovea value.
- 28 and 29 Pharomachrus: the screened note for Odeen and Hastad 2003 explains it by "no acuity or receptor spacing", which is the wrong trait for these records. Main logs no Pharomachrus row from it, and the paper's species list is a lead (below).
- 43 Herpetotheres fov_h_deg: the claim of 48 Hawk Eyes I rows on main repeats the count audit 70 found wrong (22 by DOI). The substance holds (no Herpetotheres row). Listed, not counted.

## Rate

- First sample: 1/20 = 5.0%.
- With extension: 1/35 = 2.9%.
- Pooled with audits 43 to 51 and 55 to 70 (6 in 572): 7/607 = 1.2%.
- Verdict: the unit passes (under 5%). Fowlea pupil_shape (line 39) must be rewritten as a held cell or taken to the owner's page: the Xenochrophis piscator account gives a round pupil.

## Leads (compilations whose species lists I could not see)

- Banks et al. 2015 (Sci Adv, pupil shapes, canon): Bungarus (34) and Fowlea (39). Main holds its Nyctereutes row only.
- Simoes et al. 2016 supplement: main's 83 taxa include no Bungarus; the supplement itself was not opened.
- Odeen and Hastad 2003 and 2013, Odeen, Hastad and Alstrom 2011 (PMC3225180 returned a browser check page): Pharomachrus (28, 29), Pastor (17), Lophoceros (53), Myzomela. Main logs no row for these genera from the first and third.
- Veilleux and Kirk 2014 (Nyctereutes acuity, not sampled) and the Simoes supplement stay open as in audit 70.
- Nowinszky et al. 2022 Table 1: my lamp search for Lobocleta returned no table naming it; the table itself was not read. Point 9 does not reach the sampled Lobocleta cells.

## Wanted lines (not counted)

Not opened; faults there are not counted. Martin and Coetzee 2004 and Odeen and Hastad 2010 were checked by audit 70.

## Rattus

Not contested and no sampled record bears on it.
