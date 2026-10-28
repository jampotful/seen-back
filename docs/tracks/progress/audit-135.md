# Audit 135: desk-d45 (branch origin/research/desk-d45, head e62a3514)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit.
- Search records: all 18 lines of docs/views/searched/desk-d45.jsonl. The launch prompt and the unit's progress note say 21, but the file holds 18 and the note's own per-genus counts (2+2+4+3+1+2+4) also sum to 18.
- Evidence records: both lines of docs/views/evidence/desk-d45.jsonl.
- Wanted lines: all 3 read; lines 1 and 3 checked against an opened page. Faults listed, not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on the unit's searched file with its wanted file prints "0 problems".

## Method

desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, audits 86 to 90 and 134 for format and rulings, and the launch prompt's rulings.

- Queries. `harvest_get.py` (offline, origin/ci): Calypso harvest run 5, Gymnadenia run 3, Adelinia run 6; Chlorogalum, Malus, Marah, Epifagus, Hieracium and Nuphar "in no harvest run yet". A script compared each record's non-"web: " queries with the harvest's query and family-review lines: lines 1 to 8 match word for word and in order; lines 9 to 18 hold "web: " lines only. No unlabelled line.
- Chased. Calypso and Gymnadenia (lines 1 to 4) name 10.1111/plb.13069, the first work of the harvest's own "Orchidaceae photoreceptor review" list; Adelinia (lines 5 to 8) names 10.21577/0100-4042.20250140, the first work of the harvest's "Boraginaceae photoreceptor review" list. Both are the harvest's family review, as the ruling asks. Gymnadenia's note of the zero-hit citation step (10.1098/rspb.2009.1966) matches the output. Malus (line 12, no harvest run) names 10.1007/s44372-025-00446-3 from its labelled "web: Rosaceae photoreceptor review" search: accepted. No harvest genus names that web DOI.
- Main (origin/main d31cef85). Main holds Gymnadenia diel and sense_chemical (sweep-34:3, 4), Chlorogalum diel (sweep-34:13), Malus sense_light_nonvisual (oa-7:510, oa-12:320, sweep-34:9), diel and sense_chemical (sweep-34:14, 15); the unit writes no record for any of those cells. Main holds no Nuphar or Hieracium sense_chemical evidence (Hieracium umbellatum diel at sweep-32:3; Pilosella aurantiaca light at desk-d29:2), so neither evidence line repeats main.
- Taxonomy. POWO pages returned by search: Adelinia grandis (60469986-2) accepted, with Cynoglossum grande listed as the synonym the protocols use; Chlorogalum grandiflorum (56972-2) shows the genus in use; Nuphar variegata accepted (audit 134, 1117161-2). Pilosella hoppeana subsp. sicula is a Pilosella (Candollea 71(1), bioone result), a genus POWO keeps apart from Hieracium. No hybrid or synonym is filed as a taxon.

Searches: 27 WebSearches and 13 fetches of URLs they returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a saludcastillayleon.es publisher mirror result was left alone). No paper text is committed. Blocked: pmc.ncbi.nlm.nih.gov PMC4377512 (permission not answered); the bioone Southeastern Naturalist page returned meta tags only.

## Evidence verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Nuphar variegata sense_chemical, m, partial | ok. experts.umn.edu opened: Verhoeven, Bacon, Larkin 2024, Aquat Bot 192: 103746, 10.1016/j.aquabot.2023.103746. The quote is in the abstract verbatim, one sentence, 109 characters, the study's own result with a magnitude ("overwhelmingly ungerminated"), and the abstract ties it to the scarification and gibberellic-acid treatments after cold stratification. No dose given, so no unit to mis-copy. One named species: m holds. |
| 2 | Hieracium (genus) sense_chemical, g, partial | **error: genus-level filing of species-level measurements, pooled with a Pilosella.** The abstract (herbmedit PDF opened) names the four taxa (Hieracium hypochoeroides subsp. cilentanum, H. schmidtii subsp. nebrodense, H. terraccianoi, Pilosella hoppeana subsp. sicula), so the ruling "genus-level when the abstract names a species is an error" applies. The record's reason, that the abstract does not tie GA3 to one species, fails on the open PDF itself (access "open", yet "partial": true): its Methods and Results sow all four taxa on GA3 at 10^-3 M and report per taxon, with H. schmidtii subsp. nebrodense at 95% on GA3. The quoted sentence also covers Pilosella hoppeana, so filed under Hieracium it carries data from another genus. Re-file as species records from the full text (for example H. schmidtii subsp. nebrodense, with a whole sentence from the Results); the quote itself is verbatim (98 characters). |

Evidence: 1 error in 2 (line 2).

## Search record verdicts (18)

| Line | Record | Verdict |
|---|---|---|
| 1 | Calypso diel | ok. My two searches returned Proctor and Harder 1995 on floral longevity after pollination (days, no opening hour; ualberta ERA), Boyden 1982 (screened) and a 2015 Sci World J pollinator-behaviour paper on C. bulbosa (PMC4377512, fetch blocked; title is pollinator behaviour, no opening hour shown). No flower-opening or scent-timing measurement found. |
| 2 | Calypso eye_type | ok. Plant eye_type none. |
| 3 | Gymnadenia eye_type | ok. |
| 4 | Gymnadenia sense_light_nonvisual | ok. My searches returned the screened Nabieva 2020 paper, Rasmussen, Andersen and Johansen 1990 (ucviden opened: Dactylorhiza majalis only) and Ponert et al. 2011 (ejes.cz opened: G. conopsea in a sowing table, dark protocol, no light comparison). |
| 5 | Adelinia diel | ok. Fung and Thomson 2017 (JPE opened) is a subalpine flora without Adelinia; no opening hour found. |
| 6 | Adelinia eye_type | ok. |
| 7 | Adelinia sense_chemical | ok. Germination searches returned only the screened protocols and a Pacific Bulb Society page; no GA3, smoke or volatile trial. |
| 8 | Adelinia sense_light_nonvisual | ok. Same searches; no light/dark trial. |
| 9 | Chlorogalum eye_type | ok. |
| 10 | Chlorogalum sense_chemical | ok. Keeley and Fotheringham 1998 smoke paper (pubs.usgs.gov opened) does not name Chlorogalum in its abstract; the Guretzky et al. 2005 DTIC report on C. purpureum (opened) is field monitoring, no germination trial. |
| 11 | Chlorogalum sense_light_nonvisual | ok. Same searches; no light/dark trial on a Chlorogalum species. |
| 12 | Malus eye_type | ok. Web family-review DOI accepted (no harvest run). |
| 13 | Marah diel | ok. Cusser 2006 thesis abstract on Marah macrocarpus pollinators (bfs.pomona.edu opened) gives no time of day. Note below on the chased reason. |
| 14 | Marah eye_type | ok. Same note. |
| 15 | Epifagus diel | ok. Abbate and Campbell 2013, Southeastern Naturalist 12(3) (eaglehill index opened) report insect-visit timing (morning and afternoon), which is visitor behaviour, not flower opening or scent timing. Same note. |
| 16 | Epifagus eye_type | ok. |
| 17 | Epifagus sense_chemical | ok. My searches returned Brooks' morphological study (IAS opened: no germination trial) and a microbial-community paper (pwvas opened: no plant response). No host-stimulant germination trial on Epifagus. |
| 18 | Epifagus sense_light_nonvisual | ok. Same searches. |

Search records: 0 errors in 18.

Note, not counted: lines 13 to 18 give a none-reason in `chased` that cites a "Cucurbitaceae photoreceptor review" or "Orobanchaceae photoreceptor review" search, but neither search appears among the record's "web: " queries. The claim cannot be checked from the record. No ruling makes this an error (the reason is a none-reason for genera in no harvest run); if the desk reads an unlisted claimed search as an unsupported `chased`, six lines (13 to 18) would count and the unit would fail.

## Wanted lines (listed, not counted)

- 1 (Rodriguez et al. 2018): uvigo portal opened; authors, 2018, Sci Total Environ 633: 1041-1050 and 10.1016/j.scitotenv.2018.03.264 match. No fault.
- 2 (Pulmonaria, HortScience 31(4): 630): my title search returned no page for it; DOI and year unchecked. Empty authors field is honest.
- 3 (Hill 1916): BHL part 320110 opened; Hill, April 1916, Annals of Botany 30: 215-222, 10.1093/oxfordjournals.aob.a089592 match. No fault.

## Counts and verdict

- Search records: 0 of 18, 0%.
- Evidence: 1 of 2, 50% (line 2).
- Unit: 1 of 20, 5.0%. Not under 5%, so the unit fails as written; the whole unit was judged, so there are no further lines to draw. Dropping evidence line 2 leaves a clean remainder (19 lines).
- Pooled with audits 83 to 90 (audit 90's pool: 48 in 1026 search records, 52 in 1090 overall): search records 48 in 1044, 4.6%; overall 53 in 1110, 4.8%. Adding audit 134 as well: search 50 in 1060, 4.7%; overall 56 in 1132, 4.9%.

## Error lines

- docs/views/searched/desk-d45.jsonl: none
- docs/views/evidence/desk-d45.jsonl: 2
- docs/views/wanted/desk-d45.jsonl: none (faults not counted)
