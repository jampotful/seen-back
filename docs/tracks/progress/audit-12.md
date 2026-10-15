# Precision audit 12, 15 October 2026

Scope: every evidence record in sweep-80 to sweep-83. sweep-83 has no evidence file, so the audit covers 16 records (sweep-80: 2, sweep-81: 4, sweep-82: 10). No sampling; all were opened.

Method as in audits 6 to 11: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-12.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-80:1 | Heremites auratus / fovea | m | confirm | verbatim on the Mosul journal page; the sentence continues ", the deep convexiclivate centrodorsal one" and names the shallow concave dorsotemporal fovea. The page prints no author, volume or page numbers, so "p. 38" and the author field could not be checked against it |
| sweep-80:2 | Heremites auratus / oil_droplets | m | confirm | verbatim, one sentence; page numbers unchecked as for 80:1. The abstract's rod figure reads "The cone ratio was 77% while the rod 13%.", as the note says |
| sweep-81:1 | Aipysurus laevis / acuity_cpd | m | confirm | verbatim (Macquarie portal), split after "A. laevis,"; the sentence continues "the superior value for A. laevis may reflect its specialized crevice-foraging hunting technique." Already `partial: true` |
| sweep-81:2 | Aipysurus laevis / fovea | m | confirm | verbatim; the stereology sentence names "the olive sea snake (Aipysurus laevis)"; the ventral area is given for L. curtus and D. major only, as the note says |
| sweep-81:3 | Atractus / fovea | g | confirm | verbatim (USP thesis page, English abstract); no species named; "86 retinas of 20 different species" |
| sweep-81:4 | Cyclorana novaehollandiae / behaviour_vision | m | confirm | verbatim (NAU portal); prey types, "velocity of movement" and "fast and slow prey" all in the abstract. Issue 180(3) |
| sweep-82:1 | Acanthophis / pupil_shape | g | retract | Wikipedia source; no paper or thesis found for an Acanthophis species |
| sweep-82:2 | Leioheterodon / pupil_shape | g | retract | Reptile Database source; the diagnosis is Boulenger 1893 (Catalogue I), whose BHL copy the fetch tool refused |
| sweep-82:3 | Hydrodynastes gigas / pupil_shape | m | retract | Wikipedia source, uncited; three H. gigas or Hydrodynastes papers opened carry no pupil statement |
| sweep-82:4 | Spalacopus cyanus / fov_h_deg | m | confirm | verbatim (nature.com), split after "170°"; Methods: ophthalmoscope reflex, ketamine-xylazine anaesthesia, campimeter, eyes paralysed with lidocaine; two animals per species |
| sweep-82:5 | Spalacopus cyanus / binocular_deg | m | confirm | verbatim, split after "dorso-rostrally"; S. cyanus paragraph |
| sweep-82:6 | Spalacopus cyanus / fovea | m | correct | quote verbatim, but it is the abstract's third sentence (the record says first), and the full text is open with the authors' own ganglion cell layer maps: "Remarkably, we found a circumscribed higher cell density region or area centralis (AC), only in S. cyanus (Fig. 2a)." Flag set to `partial: false`, requoted to that sentence |
| sweep-82:7 | Spalacopus cyanus / lambda_max_nm 505 | m | confirm | verbatim (UC repository); ERG, "three spectral mechanisms". Metadata row: Peichl et al. 2005, J Comp Neurol 486(3): 197-208, DOI 10.1002/cne.20491 |
| sweep-82:8 | Spalacopus cyanus / lambda_max_nm 365 | m | confirm | as 82:7 |
| sweep-82:9 | Spalacopus cyanus / receptor_classes | m | confirm | verbatim; it follows the ERG sentence, and the next reads "Immunocytochemistry with opsin-specific antibodies confirms the presence of rods, L-cones, and S-cones." Metadata row as 82:7 |
| sweep-82:10 | Trapelus mutabilis / fovea | m | confirm | verbatim (EJZ page), already `partial: true`; the abstract also says "Photoreceptor layer of retina contains both single and double cones." and mentions no rods |

**Rate: 4 errors in 16 verifiable records, 25%** (0 unverifiable). Every quote that was checked is verbatim. The errors are the three encyclopedia and database pupil records and one over-flagged record.

## Checks the desk asked for

- **Pupil records from Wikipedia and the Reptile Database (82:1 to 82:3).** All three retracted; no paper or thesis stating the pupil for the same taxon was reached. For Leioheterodon the obvious replacement is Boulenger (1893), Catalogue of the snakes in the British Museum (Nat. Hist.) I, cited on the Reptile Database page as the source of the genus diagnosis ("eye large, with round pupil"). The BHL item (47181) was refused by the fetch tool. If a later pass opens that page, the record can be refiled from it at grade `g`, since the diagnosis is for the genus. For H. gigas, Carvalho et al. 2020 (PeerJ 8: e10073), the species' main morphological study, does not contain the word "pupil".
- **Abstract-only records carry `partial: true`.** Yes for all seven abstract-only records (81:1 to 81:4, 82:7 to 82:10). One record carries the flag without cause: 82:6 cites the open Nature paper whose full text has the data (corrected). The two Heremites records are filed as `access: open` with no flag; the sweep agent read a PDF of the article, and the values rest on abstract sentences that were confirmed.
- **Pooled or unnamed-species records are `g`.** Atractus (81:3, genus, no species named) is `g`. The two genus-level pupil records were `g` and are retracted. No other record pools species: the Aipysurus values are given per species.
- **Spalacopus values.** The Vega-Zuniga et al. 2017 full text matches 82:4 and 82:5 (170°, −25° to 145°; 50° between 30° and 60° elevation) and supports the area centralis (peak 6,400 cells/mm²). The 2005 abstract matches 82:7 to 82:9: rod about 500 nm, L cone about 505 nm, S cone near 365 nm, "This suggests dichromatic color vision.", with immunocytochemistry confirming rods, L and S cones. Vega-Zuniga et al. cite the 2005 paper only for a 10% cone proportion and give no lambda-max of their own, so the two papers do not conflict.

## Rows written

`recheck-12.jsonl`: 7 rows.

- Counted: 82:1, 82:2, 82:3 (`retract`), 82:6 (`correct`, partial flag, quote, method, where).
- Not counted: 82:7, 82:8, 82:9 (`correct`, metadata only). The 2005 records named no authors, volume or DOI; filled from the ANID researcher record (Peichl L, Chávez AE, Ocampo A, Mena W, Bozinovic F; 486(3): 197-208; 10.1002/cne.20491), with volume and pages matched on a second UC repository record.

## Blocked pages

- doi.org/10.1002/cne.20491 (Wiley) and a PubMed search page returned fetch errors.
- The Mosul DOI redirect (ojs.uomosul.edu.iq, article 42119), the Reptile Database page for Heremites auratus and the BHL item for Boulenger 1893 were refused at the permission step. The Mabuya aurata synonymy in the Heremites notes was therefore not rechecked.

## Patterns (this run)

1. Sweep agents reach for encyclopedia and database pages when a trait is new to the log (here pupil shape, three times in one sweep). The addlog check could refuse a record whose source journal field says "web page".
2. A record built from a repository abstract can miss that the same paper is open in full elsewhere; 82:6 was filed as abstract-only from CONICET while 82:4 and 82:5 cite the full Nature text of the same paper.
3. Records filed from repository pages with blank metadata (82:7 to 82:9) leave authors and DOI empty; a researcher-database record (ANID here) usually fills them in one fetch.
