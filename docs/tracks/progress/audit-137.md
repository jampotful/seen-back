# Audit 137: desk-d47 (28 October 2026)

Unit: desk-d47, branch origin/research/desk-d47 (commit 38f7e7f), files docs/views/evidence/desk-d47.jsonl (4 lines) and docs/tracks/progress/desk-d47.md. The unit has no searched or wanted file, so the mechanical gate and the search-record sample have nothing to run on; every evidence line was judged. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. Quotes were checked against pages my own WebSearches returned, asking the fetch tool for the exact sentence and its boundaries; lengths were counted with Python on the record's string.

## Evidence records

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Drosera rotundifolia / sense_light_nonvisual | ok | Aalto research page (opened): the quote is one whole sentence, verbatim, ending at its period and followed by "However, after 7-day exposure..."; 112 characters. Living plants raised in low light and exposed to high-intensity sunlight 5 h a day for 7 days: a light-intensity response, which the owner's reading 10(d) files under sense_light_nonvisual. Authors (Tkalec, Doboš, Babić, Jurak), Acta Physiol Plant 37(4), 2015 and the DOI agree with the page. Not on main (main has only a sweep-14 sense_chemical record for the species). |
| 2 | Lactuca serriola / diel | ok | bioRxiv full-text PDF (opened): "In contrast, L. serriola accession Armenian999 does not flower until the afternoon." is a whole Results sentence, verbatim, 83 characters; the same text gives the late parent's inferred peak floral opening as 1:15 pm and names Armenian999 as an L. serriola accession. Flower opening time is plant diel. Author list agrees with the Michelmore lab publications page ("Han R, Wong AJY, Tang Z, Truco MJ, Lavelle DO, Kozik A, Jin Y, Michelmore RW"), which lists the peer-reviewed version (J Exp Bot 2021, 72(8)); citing the preprint is not a fault. Main has L. serriola only under sense_light_nonvisual (sweep-14, a different paper on photoperiod), so nothing repeats. `partial` is conservative for an open full text, not an error. |
| 3 | Tiarella polyphylla / sense_chemical | ok | KoreaScience page (opened): the English abstract holds the sentence word for word (GA with subscript 3), 64 characters, and gives 33.3%, 45.0%, 42.5% and 72.5% at 0, 10, 100 and 1000 mg/L, matching the value's doses, unit and percentages. Applied GA3 on living seed counts under sense_chemical. Six authors, KJPR 31(4): 363-371, 2018 and DOI agree. Tiarella polyphylla is the accepted name (POWO entry returned by search). Not on main. |
| 4 | Borago officinalis / sense_light_nonvisual | ok | VDU CRIS page (opened): the abstract has five sentences; the quote is sentence 3, standing alone between periods, verbatim (the record writes "m-2s-1" as the page does), 124 characters by my count. The page names the species as Borago officinalis L., and the trial is borage microgreens only, so the "microgreens" of the sentence are that species. The independent variable is set PPFD (110 to 545 umol m-2 s-1, unit correct); tissue nitrate falling at moderate irradiance is a measured response of the living plant to set light intensity, which 10(d) files under sense_light_nonvisual. The nutrient-ion exclusion applies to sense_chemical (a plant's uptake as a response to a chemical), and here no nutrient was varied. The value's growth part (rise to 440, inhibition at 545) is also in the abstract. Authors, Rural Development 2013 proceedings 6(2): 272-275 and the DOI agree. Not on main. A desk-d40 wanted line had called the abstract a single 274-character sentence; the page shows that was wrong, so this record supersedes the lead. |

Epithets: Drosera rotundifolia, Lactuca serriola and Borago officinalis are long-accepted Linnaean names (not re-checked on POWO pages); Tiarella polyphylla checked via the POWO hit. None is a hybrid or a synonym.

Evidence: 0 errors in 4.

## Leads the progress note closes (sample of 10, random.seed(137) over the 42 "no qualifying sentence" leads and the 3 "closed on main" claims)

Drawn: Anacamptis longicornu, Anthyllis vulneraria, Encelia farinosa (photosynthesis), Cynoglossum officinale, Yucca (light), Ericameria nauseosa, Torilis japonica, Menyanthes trifoliata, Ulex europaeus, Ipomopsis (second lead).

| lead | check | verdict |
|---|---|---|
| Anacamptis longicornu (10.3390/plants10112543) | DOAJ abstract: six sentences; the only photoperiod result ("temperature and photoperiod widely affect seed germination and development", 96) pools two species and gives no direction; the A. longicornu numbers are about media | holds |
| Anthyllis vulneraria (10.1002/ece3.4831) | DOAJ abstract has no shade-specific result; PMC Results: the 90.8% shade biomass sentence is about 190 characters, none shorter | holds |
| Encelia farinosa sun/shade (10.1071/PP9950833) | CSIRO abstract: six sentences, all 141 to 298 characters | holds |
| Cynoglossum officinale MeJA (treesearch 52777) | Abstract sentence "MeJA-treated plants emitted large amounts of plant volatiles and produced leaves with twice as many trichomes as untreated plants." is 130 characters (counted); next result sentence 140 | holds |
| Yucca elata light (IPICYT PDF) | Sentences naming Yucca with the light/dark result are long; none of 125 or fewer | holds |
| Ericameria nauseosa GA3 (BYU GBN 47(2)) | The one GA3/kinetin result sentence is about 161 characters | holds |
| Torilis japonica (10.1017/S0960258508038877) | Cambridge abstract: the light results (embryos fail to grow without a light stimulus; spring germination) are about 141 and 198 characters; the 120-character light sentence is Methods. The fetch paraphrased, so lengths are approximate, but the margins are wide | holds |
| Menyanthes trifoliata UVB (10.1016/j.envpol.2009.06.022) | AGRIS abstract: UVB result sentences 159 and 174 characters | holds |
| Ulex europaeus shade (10.1371/journal.pone.0137500) | DOAJ abstract: the decrease sentence is 161; the genotype sentence reassembled verbatim is about 127 and states genotype dependence, not a direction; "All traits studied responded to shading..." (81) has no direction | holds |
| Ipomopsis warming scent (10.1093/aob/mcad195) | Richmond abstract: volatile sentences 221 and 194 characters and directionless ("subtle ways", "affected") | holds |

"Closed on main" claims, all three checked on origin/main evidence: Mimosa pudica sense_light_nonvisual (desk-d42, 10.3390/physiologia2040012; also plant-fungus-slime), Ericameria nauseosa sense_light_nonvisual (desk-d38), Mercurialis annua sense_chemical (desk-d43, 10.3389/fpls.2022.812558). All hold.

Leads: 0 misses in 10; closed-on-main: 3 of 3 hold. These are checks of the progress note, not records, and are not added to the pooled counts.

## Counts and verdict

- Evidence: 0 errors in 4, 0%.
- Search records: none in the unit.
- Pooled with audits 83 to 90 (audit 90's pool as carried by audit 136: 52 in 1090 overall, 48 in 1026 search records): overall 52 in 1094, 4.8%; search records unchanged at 48 in 1026, 4.7%.
- Verdict: pass. All four evidence lines stand.

## Error lines

- docs/views/evidence/desk-d47.jsonl: none
- docs/views/searched/desk-d47.jsonl: no file
- docs/views/wanted/desk-d47.jsonl: no file

Note for the desk (not counted): main still carries older null search records for these genera (Drosera, Lactuca, Tiarella and Borago in desk-d29/d33/d40/d42 and sweep runs) whose leads these records now settle; the d40 Borago wanted line's "one abstract sentence" description was wrong.
