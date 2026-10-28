# Audit 134: desk-d44 (rework set and queue batch 35, plant; branch origin/research/desk-d44)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit.
- Search records: all 16 lines of docs/views/searched/desk-d44.jsonl.
- Evidence records: all 6 lines of docs/views/evidence/desk-d44.jsonl.
- Wanted lines: all 7 read; lines 4, 6 and 7 checked against an opened page. Faults listed, not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on the unit's searched file with its wanted file prints "0 problems".

## Method

desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, audits 86 to 90 for format and rulings, plus the launch prompt's rulings.

- Queries. `harvest_get.py` (offline, origin/ci) prints "in no harvest run yet" for all nine genera of the unit (Carpobrotus, Helenium, Nuphar, Pistacia, Alisma, Bunias, Ipomopsis, Tribulus, Mimosa). Every record lists "web: " lines only, which is the right shape. No unlabelled line.
- Chased. Helenium (lines 3 to 5) names 10.1007/s44372-025-00446-3 from its labelled "web: Asteraceae photoreceptor review" search; accepted for a genus in no harvest run (audits 86, 87, 133). The others give a none-reason after a labelled family-review search. No harvest genus is involved, so no chased error.
- Main (origin/main 00b8f471). No search record names a trait with evidence on main: Carpobrotus diel (sweep-33:14), Bunias sense_chemical (sweep-33:15, recheck-quotes-3-fixed:159), Alisma sense_light_nonvisual (sweep-34:1), Pistacia diel (sweep-36:1) and Ipomopsis diel (oa-9:319 to 329) are all left out. No evidence record repeats a main record: main holds no Tribulus, Carpobrotus light, Helenium, Pistacia chemical or Alisma diel evidence, and Mimosa on main is M. pudica touch and light only. Several unit nulls repeat older null search records on main (sweep-21:30 Helenium, sweep-33:21 and 22 Carpobrotus and Bunias, sweep-36:14 Nuphar, sweep-36:1 Ipomopsis); noted, not counted.
- Taxonomy (POWO pages opened): Carpobrotus edulis (1200427-2), Tribulus terrestris (873489-1), Alisma plantago-aquatica (30019518-2), Pistacia khinjuk (70252-1), Mimosa setosa (508684-1) and Nuphar variegata (1117161-2) each "This species is accepted". No hybrid or synonym is filed. The Mimosa thesis writes Mimosa paludosa Benth., and IPNI and NYBG results list Mimosa setosa var. paludosa (Benth.) Barneby, so the species M. setosa matches the thesis; the variety page in POWO was not opened.

Searches: about 45 WebSearches and fetches of URLs they returned (two or more per null record under 10(e), plus evidence, taxonomy and wanted checks). No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. No paper text is committed. Blocked: pub.uni-bielefeld.de record 1877137 (bot check), muse.jhu.edu 270191 (verification page).

## Evidence verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Tribulus terrestris diel | ok. JoTT PDF opened: Suvarna Raju and Solomon Raju 2023, 15(5): 23279-23282, DOI as given. Quote verbatim, one sentence, 62 characters; closing in late afternoon is in the next sentence. |
| 2 | Mimosa setosa diel | **error: quote not a whole sentence.** The UFMS PDF (opened) gives "Todas as flores do glomérulo abrem sincronicamente antes das 05h30" as only the opening of a longer sentence (it runs on about anthers, stigma and bee visits until 08:00-09:00), and the record's quote has no terminal stop. The repository abstract's phrase "diurnas, que abrem ao alvorecer (antes 05h30) e duram 10-12 horas" is also part of a longer sentence, so a re-quote needs another whole sentence from the full text. Taxon and value otherwise hold. |
| 3 | Carpobrotus edulis sense_light_nonvisual | ok. iris.unica.it record opened: Podda, Santo, Mattana, Mayoral, Bacchetta 2018, Plant Biol 20(6): 1059-1067, 10.1111/plb.12867; the sentence "All the tested seed lots achieved higher germination percentages in the light, with respect to total darkness." is the study's own result (110 characters), and the lots include C. edulis. |
| 4 | Helenium (genus) sense_light_nonvisual | ok, with a note. The panamseed grower guide (opened) names only "Helenium Dakota Gold", no epithet, and gives the quoted sentence verbatim; year 2017 stated. So the genus-level filing follows the source. Note: the same company's product page (opened) gives "Scientific Name : Helenium amarum", and Baskin and Baskin 1975, "Do seeds of Helenium amarum have a light requirement for germination?" (Bull Torrey Bot Club 102(2): 73-75; wildflower.org literature 2527 opened) is a species-level light-germination measurement the desk could log in preference. |
| 5 | Pistacia khinjuk sense_chemical | ok. openagrar page opened: Acar, Yasar, Ercisli 2017, J Appl Bot Food Qual 90: 191-196, 10.5073/JABFQ.2017.090.024; the quoted sentence is in the abstract verbatim (96 characters); the abstract also says GA3 harmed genotype A. No dose is given, so no dose unit to mis-copy. |
| 6 | Alisma plantago-aquatica diel | ok. Springer page opened: Vislobokov and Kuzmicheva 2022, Dokl Biol Sci 506: 172-178; quote verbatim (100 characters). |

Evidence: 1 error in 6 (16.7%), line 2.

## Search record verdicts (16)

| Line | Record | Verdict |
|---|---|---|
| 1 | Carpobrotus sense_chemical | **error: missed measurement.** My search "Carpobrotus herbivore induced volatiles OR jasmonate OR elicitor response" led to Rodriguez, Calbi, Roiloa and Gonzalez 2018, "Herbivory induced non-local responses of the clonal invader Carpobrotus edulis are not mediated by clonal integration", Sci Total Environ 633: 1041-1050 (portalinvestigacion.udc.gal record and pherobase abstract opened). The abstract reports a defence-compound level in unattacked apical ramets like that of attacked basal ramets after snail (Theba pisana) attack, and a biomass increase, with root-exudate alarm signalling proposed. A herbivore-induced response of a living plant counts (owner's reading; audit 90 counted Urtica the same way). A related figshare dataset (10.6084/M9.FIGSHARE.13389206) reports herbivory-induced shoot biomass in attacked plants and neighbours. |
| 2 | Carpobrotus eye_type | ok. Plant eye_type "none"; no focusing work on Carpobrotus surfaced. |
| 3 | Helenium diel | ok. My two searches returned garden, extension and plant-patent pages; no clock hour of opening. |
| 4 | Helenium eye_type | ok. |
| 5 | Helenium sense_chemical | ok. My searches returned the Baskin 1975 light paper (light, not chemical), a Weed Science allelopathy paper on H. amarum (extracts, which do not count) and unrelated GA3 work (Kepczynski and Sznigir on Amaranthus, Springer page opened). No Helenium hormone, nitrate, smoke or volatile response. |
| 6 | Nuphar sense_chemical | **error: missed GA3 trial.** My search "Nuphar lutea seed germination dormancy light dark OR gibberellic acid OR ethylene experiment" returned Verhoeven, Bacon and Larkin 2024, "Effects of seed traits and dormancy break treatments on germination of four aquatic plant species", Aquat Bot 192: 103746, 10.1016/j.aquabot.2023.103746 (experts.umn.edu opened). It applied scarification and gibberellic acid to Nuphar variegata (POWO accepted), which stayed "overwhelmingly" ungerminated. A GA3 trial on a species of the genus that the record does not name or screen. The same search returned a 2023 South Bohemia diploma thesis (Pospisilova; dspace.jcu.cz opened) testing gibberellic acid on N. pumila, N. lutea and N. x spenneriana seeds, results not shown: a wanted-list title under 10(e). |
| 7 | Nuphar sense_light_nonvisual | ok. My searches returned the screened photosynthesis papers, Schoelynck et al. 2014 on river and oxbow morphology (uu.nl and uantwerpen opened: light as background only), the NECR244 report and Verhoeven 2024 (no light treatment). |
| 8 | Nuphar eye_type | ok. |
| 9 | Pistacia eye_type | ok. |
| 10 | Alisma sense_chemical | ok. Scarabel et al. 2003 abstract (iris.cnr.it opened) tests chloroform, ether and sulphuric-acid scarification only, rightly screened. My searches returned herbicide-resistance papers (not a hormone or elicitor) and no GA3, nitrate, ethylene or smoke trial on Alisma. |
| 11 | Alisma eye_type | ok. |
| 12 | Bunias diel | ok. My searches returned Denisow et al. 2015 (screened), Denisow and Anton 2012 on Aquilegia (opened, no Bunias) and pladias; no opening hour. |
| 13 | Bunias eye_type | ok. |
| 14 | Bunias sense_light_nonvisual | ok. My searches returned Reise et al. 2024, Tuexenia 44: 159-175 (opened: mechanical control, no light trial), a Conyza thesis and unrelated R:FR work. |
| 15 | Ipomopsis sense_light_nonvisual | ok. My searches returned the screened IPAG protocol, the NPN Ipomopsis aggregata protocol (opened: stratification only), and a Phlox longifolia GA3/smoke/KNO3 paper (npj citation opened, another genus). |
| 16 | Ipomopsis eye_type | ok. |

Search records: 2 errors in 16 (12.5%), lines 1 and 6.

## Wanted lines (listed, not counted)

- 4 (Schneider and Moore 1977): authors, year, Brittonia 29(1): 88-99 and DOI match experts.umn.edu. No fault.
- 6 (Bischoff et al.): pure.uhi.ac.uk gives 2013, Ann Bot 113(3): 533-544, 10.1093/aob/mct279; matches. This paper is already on main as diel evidence (oa-9:319 to 329); the wanted line is for sense_chemical, which is a different cell.
- 7 (Wu et al. 2023): scholarship.richmond.edu gives the authors, 2023 and 10.1093/aob/mcad195; matches.
- 1, 2, 3, 5 were read only. Line 2 has an empty doi, which is honest. Line 3 (biostor-137766) has no authors or year, as rule 6 allows.

## Counts and verdict

- Search records: 2 of 16, 12.5% (lines 1, 6).
- Evidence: 1 of 6, 16.7% (line 2).
- Unit: 3 of 22, 13.6%. Above 5%: the unit fails as written; dropping search lines 1 and 6 and evidence line 2 leaves a clean remainder.
- Pooled with audits 83 to 90 (audit 90's pool: 48 in 1026 search records, 52 in 1090 overall): search records 50 in 1042, 4.8%; overall 55 in 1112, 4.9%.

Forks:
- Line 1 (Carpobrotus chemical): if the desk reads snail damage as no chemical cue, the Rodriguez 2018 title still states an induced defence-compound response, which 10(e) sends to the wanted list; I count it once either way.
- Line 6 (Nuphar chemical): the GA3 result in N. variegata is near null, but the ruling counts a missed GA3 trial regardless of direction.
- Evidence line 4 (Helenium): stands on the source's own wording; if the desk reads the company's product-page "Helenium amarum" as naming the species, it would be filed at genus level wrongly and count as an error (unit 4 of 22).

## Error lines

- docs/views/searched/desk-d44.jsonl: 1, 6
- docs/views/evidence/desk-d44.jsonl: 2
