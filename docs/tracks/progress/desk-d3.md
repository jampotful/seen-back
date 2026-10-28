# desk-d3 (plant genera, 27 October 2026)

Genera done (8 of 16): Hibiscus, Liriodendron, Eclipta, Hedera, Lantana, Sonchus, Juncus, Conoclinium (8 counting Sonchus, which had no open cell).

Not started (the desk's shared web search budget of 200 per turn ran out after Conoclinium; every later search was refused): Hamamelis, Apios, Nothoscordum, Clematis, Carpinus, Cocculus, Sagittaria, Richardia. They still need all their web searches. Cocculus also shows three failed supplement queries in the harvest ("gave up"), so its record waits for a rerun.

Hibiscus: its two citation steps show "error gave up" in the harvest, so no search record can be written (point 6); the one open cell (sense_chemical) is closed by a measurement instead (Saberi et al. 2021, H. sabdariffa GA priming; the page lists no DOI).

Sonchus: harvest-13 and sweep-6 already hold exhausted records for all four traits, so no search record was written. Four measurements were added anyway from germination and flower-clock searches (see below).

Evidence (docs/views/evidence/desk-d3.jsonl, 11 records, all m; abstract-level ones carry partial):
- Hibiscus sabdariffa sense_chemical: Saberi, Tarnian, Karimian 2021, Ecopersia 9(1).
- Liriodendron tulipifera sense_chemical and sense_light_nonvisual: Barnett and Farmer 1978, Silvae Genetica 27(3-4) (gibberellin sporadically effective; light a significant germination factor, levels not given).
- Eclipta prostrata sense_chemical: Kedia, Kasera, Mohammed 2014, Seed Research 42(2), DOI 10.56093/sr.v42i2.163227 (published as E. alba, a POWO synonym).
- Hedera helix diel: Teppner et al. 2009, Mitt. naturwiss. Ver. Steiermark 139 (successive opening through the day; German text; no DOI).
- Lantana camara sense_light_nonvisual: Taha and Sarmamy 2023, ZANCO J Pure Appl Sci, DOI 10.21271/ZJPAS.35.SpD.21 (growth under three set light intensities).
- Sonchus oleraceus and S. asper sense_light_nonvisual: Lee et al. 2024, Plants 13(23): 3451, DOI 10.3390/plants13233451. Sonchus oleraceus sense_chemical: Guevara-Barrera et al. 2024, DOI 10.15446/rfnam.v77n1.107027 (GA3). Sonchus oleraceus diel: Linnaeus's flower clock as printed on the Uppsala University Linnaeus Garden page (opens 5, closes 12); a historical table, not a modern measurement, no DOI.
- Juncus ranarius sense_chemical: Kołodziejek and Patykowski 2015, DOI 10.15835/nbha4329752 (GA3 promoted germination).

Search records (docs/views/searched/desk-d3.jsonl, 14): Liriodendron diel, eye_type; Eclipta diel, eye_type; Hedera eye_type, sense_chemical; Lantana diel, eye_type; Juncus diel, eye_type; Conoclinium sense_light_nonvisual, sense_chemical, diel, eye_type. Harvest query lines are copied word for word where the genus is in a harvest run (Liriodendron, Juncus); the other genera list "web: " lines only, with the family review taken from a labelled web search (Asteraceae: 10.1007/s44372-025-00446-3; Verbenaceae the same; Araliaceae gave none).

Wanted lines: none.

Leads left open (not logged): Liriodendron PMC8325688 (L. chinense flowering mutant) blocked by an unanswered permission request; Eclipta Weed Technology "Factors affecting eclipta seed germination" (cambridge.org, not opened); Lantana Wijayabandara et al. 2011 (PURSE, Peradeniya; germination 0% under light/dark and constant dark, deep dormancy) not logged because it shows no light response; Sonchus oleraceus Chauhan, Gill, Preston 2006, Weed Science 54(5): 854-860 (light favoured germination; no DOI on the page opened).

Taxonomy checks: Eclipta alba is a synonym of Eclipta prostrata (POWO ipni 202735-1, opened). Conoclinium coelestinum was searched also under Eupatorium coelestinum; the Eupatorium works returned were on E. adenophorum (now Ageratina) and are not Conoclinium.

## Desk disposition after audit 93 (28 October 2026)

Audit 93 judged the whole unit (14 search records, 11 evidence records). Search errors: line 6 (Hedera sense_chemical, a missed GA3 result, Marc and Hackett 1992), line 7 (Lantana diel, a missed result, Barros et al. 2001, flowers open at 06:30) and line 9 (Juncus diel, a missed result, Michalski and Durka 2007, which the audit flagged as a fork and counted). Evidence error: line 10, the Sonchus flower clock, a historical Linnaeus table that fails the owner's reading of plant diel. Those four records are dropped and the rest merged: 11 search records, 10 evidence records. The three missed results are leads and their cells stay open. The unit wrote no wanted lines. Eclipta is filed correctly (the paper's name Eclipta alba is a synonym of Eclipta prostrata, same genus) and the Hibiscus record duplicates nothing on main. Not screened: Hamamelis, Apios, Nothoscordum, Clematis, Carpinus, Cocculus, Sagittaria, Richardia.
