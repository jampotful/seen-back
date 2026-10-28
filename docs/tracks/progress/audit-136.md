# Audit 136 of desk-d46, 28 October 2026

Unit: desk-d46 (branch research/desk-d46, head 00ec21cb). Files: docs/views/evidence/desk-d46.jsonl (4 lines), docs/views/searched/desk-d46.jsonl (2 lines), docs/views/wanted/desk-d46.jsonl (3 lines), docs/tracks/progress/desk-d46.md. The launch prompt expected about 6 evidence records; the unit holds 4 evidence and 2 search records, and all 6 were judged, so no sample was drawn. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

Mechanical gate: `screen_candidates.py --check` on the unit's searched and wanted files prints "0 problems".

## Evidence records

| line | taxon / trait | verdict |
|---|---|---|
| 1 | Hieracium terraccianoi sense_chemical (Di Gristina, Varshanidze and Domina 2020, Fl. Medit. 30: 431-437, 10.7320/FlMedit30.431) | ok. herbmedit.org PDF opened: the authors, DOI and pages match. The quoted sentence is word for word the H. terraccianoi Observations sentence, and the dose "10-3 M" is printed that way. It reports the study's own result (germination in GA3 similar to water). At 92 characters it is a single sentence. A GA3 germination trial on living seed counts under plant sense_chemical. Name status: a POWO WebSearch returned a POWO page titled "Hieracium terraccianoi Di Grist., Gottschl. & Raimondo" (ipni 77143944-1), but the page failed to load, so I could not read its status line. The Phytotaxa 188(1): 55-60 page (2014, opened) describes it as a new species. I found no sign that it is a synonym or a hybrid. POWO acceptance is therefore likely but not confirmed, and I do not count it as an error. Main holds no evidence on Hieracium sense_chemical; desk-d44 has this paper only as a wanted lead. |
| 2 | Pilosella hoppeana subsp. sicula sense_chemical (same paper) | ok. The quote matches its Observations sentence word for word (111 characters), and the dose matches. POWO 238132-1 (opened) says "This species is accepted" and lists "Pilosella hoppeana subsp. sicula Di Grist., Gottschl. & Raimondo" among the accepted infraspecifics. The record is filed under Pilosella, which is correct. Main has no Pilosella sense_chemical evidence. The sweep-10:35 null on main is now contradicted by this record, but that fault belongs to sweep-10, not this unit. |
| 3 | Succisa pratensis diel (Štenc et al. 2023, Am J Bot 110(6): e16179, 10.1002/ajb2.16179) | ok, judgement call. Starfos record (opened) confirms the quote word for word, along with the journal, volume and DOI. It is exactly 125 characters, one sentence, and states the study's result with a direction. My ruling: pollen release here measures flower opening (the anthers' daily dehiscence schedule, which is part of anthesis), not scent timing. Audits 90, 99, 101 and 104 counted anther dehiscence and pollen-presentation schedules as flower timing, and audit 104 accepted desk-d14:4 (C. jacea) from this same paper. The species differs from desk-d14:4 and so does the quote, so nothing repeats main. On main the paper is only a wanted lead (harvest-c6 wanted 1). `grade` m and `partial` are right. Cosmetic fault: the `journal` field leaves out 110(6): e16179. |
| 4 | Pleurozium schreberi sense_light_nonvisual (Kellomäki, Hari and Väisänen 1977, Silva Fennica 11(1)) | **error.** The record's own `conditions` and `note` say "natural light gradient, not set light treatments" and "field correlation across stands, not a set-light trial". Under the ruling in force, a field gradient is not a set-light trial for sense_light_nonvisual, so this cannot close the cell. The note also says the 30 to 40 percent threshold is stated for the mosses together, so the value's second half is a group figure under an `m` grade. Pleurozium light keeps its wanted leads (Gundale et al. 2012; the 1979 Journal of Bryology paper). |

Evidence: 1 error in 4 (line 4).

## Search records

`queries` in both records repeat the harvest's 12 queries word for word and in order ("Pleurozium phytochrome photoreceptor" through "Pleurozium epidermal focusing leaf optics"), then the family review step "Hylocomiaceae photoreceptor review", which harvest_get prints at its line 274 ("1 hits"), then five "web: " searches. The `chased` reason (the family review returned one hit, Acta Biologica Plantarum Agriensis (7.), with no Pleurozium measurement, and no citation step was printed) agrees with the harvest output. screen_candidates lists 4 diel candidates and 0 eye_type candidates, and all 4 diel candidates are named in `screened`.

| line | genus / trait | verdict |
|---|---|---|
| 1 | Pleurozium diel | ok. A moss has no flowers, so plant diel (flower opening and scent timing) has nothing to measure beyond possible scent timing. The four screened works are boreal forest-floor or atmospheric VOC fluxes and two animal studies, and none times a Pleurozium's scent. My own search (Pleurozium schreberi volatile emission diurnal) returned a moss-volatile methods review and forest-floor flux papers, with no Pleurozium emission timed through the day. One hit (ddd.uab.cat 294341) was blocked by a bot check and is unchecked. No GA3, KNO3, smoke, light/dark or other trial belongs under diel. Main has no Pleurozium evidence, so nothing is duplicated. |
| 2 | Pleurozium eye_type | ok. Plant eye_type is "none" under the owner's reading. The note uses the required focusing phrase, and the canon entries are named. |

Search records: 0 errors in 2.

## Skip claim (Alloberberis and batches 36 to 45)

I wrote my own script (scratch, not committed). For each genus in desk-queue.md batches 36 to 45, plus Alloberberis, it took every cell in docs/views/gaps/queue.jsonl and looked on origin/main for a search record or an evidence record for that genus and trait. It searched docs/views/evidence, docs/views/searched and docs/views/audit/corrected, splitting multi-trait `trait` fields and leaving out desk-d46. It found uncovered cells only for Succisa (diel, sense_chemical), Pleurozium (all four) and Lagurus (sense_light_nonvisual). Fucus is covered through audit/corrected. Alloberberis is covered in all four cells. This is exactly the desk's list.

I then drew 12 skipped genera (random.seed(136)): Heliopsis, Helleborus, Taxus, Galactites, Pelecyphora, Engelmannia, Nemophila, Rhizophora, Glebionis, Cota, Clethra and Micranthes. For each I listed the covering records, read sample lines (sweep-96:31 Heliopsis and sweep-41:2 Taxus carry all four plant traits), and checked that no covering record id has a retract, drop, error or reject verdict in docs/views/audit/ALL.jsonl. Every open cell of all 12 is covered by at least one live record. No genus has an uncovered open cell, so the skip claim holds. This check covers only whether a record exists. It does not ask whether those older sweep nulls would survive a new audit.

## Wanted lines (listed, not counted)

- 1 (Gundale et al. 2012): the dhi-paris catalogue record (opened) gives the four authors in the record's order, 2012, and New Phytologist 194(2): 453-463. The DOI agrees with the harvest output (harvest item 95). No fault.
- 2 (1979, Journal of Bryology, 10.1179/jbr.1979.10.3.321): the title, year, journal and DOI agree with harvest item 91. No page was opened, the empty authors field is honest, and the year and DOI rest on the harvest output.
- 3 (Lagurus ovatus, HortScience 39(4), 2004, 10.21273/hortsci.39.4.836b): the title, year and DOI agree with the Lagurus harvest item 32, whose abstract names light among the germination conditions. No page was opened, and the empty authors field is honest.

## Counts and verdict

- Evidence: 1 in 4, 25% (line 4).
- Search records: 0 in 2, 0%.
- Unit: 1 in 6, 16.7%. Above 5%, so the unit fails as written. Every line was judged, so dropping evidence line 4 leaves a clean remainder of 5 lines (3 evidence, 2 search).
- Pooled with audits 83 to 90 (audit 90's pool: 48 in 1026 search records, 52 in 1090 overall): search records 48 in 1028, 4.7%; overall 53 in 1096, 4.8%.

## Error lines

- docs/views/evidence/desk-d46.jsonl: 4
- docs/views/searched/desk-d46.jsonl: none
- docs/views/wanted/desk-d46.jsonl: none (faults not counted)
