# audit-443: desk-d329, evidence lines 7 to 11

Audited 1 November 2026 from the desk-d329 files present untracked in the worktree (docs/views/evidence/desk-d329.jsonl, 11 lines, and docs/tracks/progress/desk-d329.md; neither committed here, neither edited). This audit covers 1-based file lines 7 to 11 only; another auditor has lines 1 to 6. Base 14a624e77. `tools/senses/check.py --require-evidence-kind` on the file: 11 records, 0 problems. Quote lengths (`len(q.split())`), lines 7 to 11: 29, 24, 20, 33, 33, all within 40. Rules applied: /tmp/desk/rules.md, docs/views/research/BRIEF.md, EVIDENCE-INTAKE.md, ECOLOGICAL-OUTCOMES.md (1 November 2026) and LIGHT-RESPONSE.md, with docs/tracks/progress/ecological-outcomes-350.md.

Sources opened (WebFetch, URLs from my WebSearch results or the record's own url): peerj.com/articles/10591 (five passes); mdpi.com/2076-2615/10/5/768; www.nature.com/articles/s41598-025-04270-3 (two passes); www.nature.com/articles/s41598-019-39711-3 (two passes, a third failed with a client error) and its .pdf (Methods); www.mdpi.com/2075-4450/15/1/1; api.crossref.org/works/ single-DOI lookups for 10.7717/peerj.10591, 10.1038/s41598-025-04270-3, 10.1038/s41598-019-39711-3 and 10.3390/insects15010001; for 10.3390/ani10050768 the single-DOI lookup failed again (client error) and a Crossref list query (filter prefix:10.3390, April to May 2020, title words) returned the record; mammaldiversity.org/taxon/1004787. cockroach.speciesfile.org (redirect from isoptera.speciesfile.org) returned PROVENANCE_REQUIRED: not retried, not worked around. A plazi treatment page returned only a redirect placeholder. No PMC, Europe PMC, ResearchGate, academia.edu, proxy or Sci-Hub page was opened. 13 WebSearch calls.

## Trait keys (the caller's question)

Main's practice: animal light-driven behaviour from a controlled light contrast has gone under `behaviour_vision` (Puffinus puffinus light-on counts; Lymnaea stagnalis photo-locomotory response, desk-d152), and locomotor rhythm under light regimes under `sense_light_nonvisual` (Spalax ehrenbergi entrainment, oa-2; Astyanax mexicanus activity in light, desk-d187). BRIEF defines `behaviour_vision` as "a behaviour that shows what is seen". ECOLOGICAL-OUTCOMES.md (1 November) and EVIDENCE-INTAKE.md add: "Catch, survey encounter rate or another ecological endpoint under an intervention" and "Catch, camera-event rate, occupancy, survival or abundance under an intervention, without a resolved sensory response" go to `ecological_intervention_outcome` / `ecological_outcome`, and ecological-outcomes-350.md applied this the same day to camera-station event counts (desk-d253:5 to 8): "Counts combine activity, local availability and detectability."

Rulings per line:
- Line 7 (bat acoustic passes against calculated natural moonlight): passes at four fixed recorders are a survey encounter rate, not a directly measured approach or choice, so `behaviour_vision` substitutes behaviour for an encounter count. `ecological_intervention_outcome` does not fit either: nothing was imposed. No existing key fits an observational encounter-count association with natural light. Key fault; hold for an owner ruling (line 6, same paper, shares this ruling; it is outside this audit).
- Line 8 (hedgehog camera-trap presence and feeding per ten-minute block, one week lit against one week dark at each station): a camera-event endpoint under an imposed light intervention, the case ECOLOGICAL-OUTCOMES.md names. Key fault; fixable by refiling under `ecological_intervention_outcome` with the required fields.
- Line 9 (skylark mist-net catch against calculated natural moonlight): catch is named in the policy as an ecological endpoint, which the unit saw, but the policy requires an intervention and the record itself says "none imposed". The unit's key is the least bad, and it is still outside the definition. Key fault; hold for an owner ruling.
- Line 10 (rat movement in a lit against a dark chamber, one rat per night, directly observed): a directly measured movement and crossing endpoint in a specified light comparison, as in the policy's first row. `behaviour_vision` / `behavioural_response` follows main's practice; the value claims nothing about vision. Key right.
- Line 11 (termite locomotor rhythm in DD, LD and LL): a regime comparison of the set-light and photoperiod kind that rules.md files under `sense_light_nonvisual` for plants, and main files animal locomotor rhythm under light regimes the same way (Spalax, Astyanax). `diel` is plant-only. Key right; the value ("rhythm ... abolished", the authors' word, with p values) does not claim a receptor or a visual pathway.

## Bibliographic and licence

| line | printed citation | authors (page / Crossref) | DOI | licence | fault |
|---|---|---|---|---|---|
| 7 | "PeerJ 8:e10591", 2020 | page header gives no names; Crossref Dylan G.E. Gomes, Giulliana Appel, Jesse R. Barber | 10.7717/peerj.10591 | page "open access article distributed under the terms of the Creative Commons Attribution License"; Crossref CC BY 4.0 unspecified | none |
| 8 | "Animals 2020, 10(5), 768" | page and Crossref list query agree, eight authors in filed order | 10.3390/ani10050768 | page metadata CC BY 3.0 (footer links 4.0); Crossref list query CC BY 4.0, vor | none; note's "failed twice" is out of date (optional fix) |
| 9 | "Scientific Reports volume 15, Article number: 19944 (2025)" | page byline truncated with "…" but ends Wieland Heim; Crossref seven authors in filed order | 10.1038/s41598-025-04270-3 | page: none; Crossref CC BY 4.0 vor and tdm | none |
| 10 | Sci Rep 9, 3739 (2019) | Crossref Bridgette Farnworth, Richard Meitern, John Innes, Joseph R. Waas | 10.1038/s41598-019-39711-3 | page: none ("open access article"); Crossref CC BY 4.0 vor and tdm | none |
| 11 | "Insects 2024, 15(1), 1" (Crossref issued 2023-12-19; printed year used, correct) | page and Crossref six authors in filed order | 10.3390/insects15010001 | page CC BY, metadata 3.0; Crossref CC BY 4.0 vor | none |

Titles verbatim on all five (line 7 title includes ": an acoustic monitoring study", as filed). Author form: all five lines give full given names; desk-d327 and desk-d328 on main use Surname Initials. Replacement strings are given below; uncounted format fixes.

## Names

Peropteryx kappleri: MDD taxon 1004787 opened, valid species, W. C. H. Peters 1867, Emballonuridae, Chiroptera. Erinaceus europaeus, Alauda arvensis, Rattus rattus: EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv. Odontotermes formosanus: not in gbif-names.tsv, but on main already (desk-d225, sense_chemical; audit 314 accepted the name); search results show "Odontotermes formosanus (Shiraki, 1909)" (plazi) and GBIF "Termes formosanus Shiraki, 1909" as the original combination. Accepted. No class, order or family fields are filled on these five lines, so nothing was filled from general taxonomy.

## Duplicates

git grep on origin/main across docs/ and views/ for "Peropteryx", "peerj.10591", "Erinaceus europaeus", "ani10050768", "hedgehog", "Alauda arvensis", "skylark", "04270-3", "Prinz", "Rattus rattus", "39711", "Farnworth", "ship rat", "Odontotermes", "insects15010001". Hits: Peropteryx only in gaps/try-species.json (P. macrotis); Erinaceus europaeus rows are ocular media, hearing and orbit convergence from other DOIs; Alauda arvensis rows are acuity, eye length, diel and foraging category from 10.1242/jeb.246063; Rattus rattus rows are ocular media and filter pigments (methods, squirrel-deer-rabbit); "Farnworth" hits are Max S. Farnworth on a moth review; Odontotermes is the desk-d225 trail-pheromone row. No repeat of main on any line.

## Per line

### Line 7. Peropteryx kappleri, behaviour_vision: ERROR, unfixable as filed (hold)
Quote MATCH, one Results sentence in two pieces: "C. maximiliani, P. kappleri and P. macrotis, on the other hand, have high probabilities of negative effects" / " of moonlight on bat activity (80.4%, 93.8% and 89.5% respectively; Fig. 4)." Methods "from the evening of 10 April 2018, to the morning of 19 April 2018"; "There were 12,151 bat passes above the canopy and 3,972 below the canopy." Moonlight "calculated using custom windows command line code"; overall activity "80.9% probability" positive. The paper defines no meaning for the percentages (unit says so).
Faults: (1) trait key, above. (2) Dropped qualifier: Table 2 row "b[Moon Illuminance |perkap]" gives estimate −0.23, SE 0.16, 80% CI [−0.46 to −0.04], 90% CI [−0.52 – 0.01]. The 90% interval includes zero. The conditions list which species "overlapped zero" and then say "while other species were negative", which tells the reader P. kappleri did not overlap zero. Also two recording towers "180 m apart", four recorders, site as random intercept; 1,544 P. kappleri passes (280 understory, 1,264 canopy). The moonlight effect is pooled over strata (no moon by stratum term), which the value does not contradict. Fault (2) is fixable; fault (1) holds the record.
Uncounted: the Methods print "Saut Pararé Nourages research station" and the Figure 3 caption "Nouragues Research Station"; the inconsistency is the spelling of Nouragues, and Saut Pararé is the camp name, so "the page is inconsistent" overstates it.

### Line 8. Erinaceus europaeus, behaviour_vision: ERROR, fixable (trait key; light source)
Quote MATCH, Abstract, two pieces: "Similarly, there was no overall impact of ALAN on the presence or feeding activities of hedgehogs in gardens" / "where supplementary feeding stations were present." Preceding sentence: "Although temporal changes in activity patterns in response to the treatments were noted in some individuals," / "the direction of the effects was not consistent." Confirmed: 33 gardens in England and Wales, 31 in the activity-pattern analysis; 15 July to 21 August 2017; order followed each station's existing lighting (dark first at dark stations, light first at lit ones); presence OR 1.00 (95% CI 0.92 to 1.09, p = 0.945), feeding OR 0.99 (0.91 to 1.10, p = 0.992); patterns differed at 13 of 31 sites; individuals not recognised, age and sex not recorded.
Faults: (1) trait key: camera-event presence and feeding under an imposed light treatment belongs under `ecological_intervention_outcome` (above). (2) The conditions say "about 1,000-lumen LED floodlights"; the page says the floodlight (about 1000 lumens, 10 W) was supplied only where no suitable exterior light existed, so lit stations used their own lights and intensity was not matched across stations. One record error, two fields. Not checked: the 3,470 of 22,615 blocks figure.

### Line 9. Alauda arvensis, ecological_intervention_outcome: ERROR, unfixable as filed (hold)
Quote MATCH, Abstract, two pieces: "The occurrence of birds increased with moon fraction, moonlight intensity and duration, while abundance" / " correlated positively with increasing moonlight intensity." Confirmed: 56 autumn nights 2018 to 2020, 1,533 skylarks, 50 x 80 m maize stubble at the Julius-Kühn-Institute near Münster; sex and age not reported; moon variables calculated (suncalc, moonlit, astronomical tables); moon fraction occurrence 2.78 (0.27, 5.56), abundance 0.70 (−0.19, 1.65); intensity 9.59 (3.69, 15.53) and 3.10 (1.72, 4.46); duration occurrence printed "0.27, 95% CrI: 0.07, − 0.49".
Faults: (1) trait key, above (no intervention; "intervention": "none imposed"). (2) Omitted design confound: "We placed a tape lure with the calls and song of skylark in the middle of the mist-nets." and "It can be assumed that birds were attracted solely by the tape lure, as no skylarks were observed when no playback was used." The Discussion adds "lower-flying birds could have a higher chance to hear the playback". Catch is attraction to playback, and the record never mentions it. (3) Omitted null: moonlight duration on abundance 0.05 (−0.04, 0.13). Faults (2) and (3) are fixable; (1) holds the record.

### Line 10. Rattus rattus, behaviour_vision: ERROR, fixable (omitted nulls)
Quote MATCH: the page carries "While light did not prevent rats from crossing into the opposing chamber (nine out of the ten rats crossed)," immediately followed by "rats significantly reduced their rate of movement when the chamber was illuminated (by 40%)." with nothing after "(by 40%)" before the stop; subheading "Movement". The tool would not return the sentence whole, so it was confirmed in two exact-string checks. Confirmed: 20 wild rats "caught in live capture traps from native forests in Canterbury", housed at Lincoln University; pen "situated outdoors within the research compound", dusk to the following morning, 10 to 30 August 2016, 12 h food deprivation, "Animals were only tested once"; c. 1000 lux against <1 lux; one excluded, 19 analysed (5 M and 5 F lit, 5 M and 4 F dark); males −45 min (t = 2.44, p = 0.05), females t = 1.11, p = 0.34; "None of the foraging behaviours differed significantly across treatments." Licence via Crossref vor.
Fault: the Abstract says "three of seven movement behaviours were significantly impaired". The record names the three and the visit-duration trend but never says that four of seven movement measures did not change. Fixable.

### Line 11. Odontotermes formosanus, sense_light_nonvisual: OK (optional fixes)
Quote MATCH with marked cuts. The sentence in three pieces: "However, under LD and LL conditions, the circadian rhythms of locomotor activity were abolished" / " in the two termites R. chinensis (LD, p = 0.130; LL, p = 0.558) (Figure 2B,C) and O. formosanus" / " (LD, p = 0.60; LL, p = 0.242) (Figure 3B,C)." The first " … " drops R. chinensis's p values and figure reference, the trailing one "(Figure 3B,C)". No O. formosanus qualifier dropped. Confirmed: Shizi Hill, Wuhan; seven O. formosanus colonies; six workers per 9 cm dish; 100 lux (0.62 W/m²) for LD and LL; DD rhythm p < 0.001 with period close to 24 h; DD day > night Z = −3.78, LD Z = −1.28, p = 0.20, LL day < night Z = −3.58, p < 0.001. Figure 3 legend n = 10, 9, 9.
Optional: the page does not say whether n counts dishes or workers, nor whether colonies were pooled per dish. "so the unit is the dish" is the unit's inference (a reasonable one, since 9 and 10 are not multiples of six) and should say so.

## Summary

| line | record | verdict | fields | reason |
|---|---|---|---|---|
| 7 | Peropteryx kappleri, 93.8% negative moonlight effect | ERROR, unfixable as filed (hold) | trait; value, conditions | acoustic encounter counts against natural moonlight fit no key; 90% CI −0.52 to 0.01 includes zero, which conditions imply it does not |
| 8 | Erinaceus europaeus, no ALAN effect | ERROR, fixable | trait, evidence_kind, required fields, conditions | camera-event outcome under an imposed light treatment; light source not uniform 1,000 lm floodlights |
| 9 | Alauda arvensis, catch rises with moonlight | ERROR, unfixable as filed (hold) | trait; conditions | no intervention for the ecological key; tape-lure attraction and the duration-abundance null omitted |
| 10 | Rattus rattus, 40% slower in light | ERROR, fixable | conditions | four of seven movement measures unchanged, not stated |
| 11 | Odontotermes formosanus, rhythm abolished in LD and LL | OK | (optional) conditions | quote and values confirmed; n unit is an inference |

Errors: 4 of 5 records (80%): trait key 3 (lines 7, 8, 9), scientific context 4 (dropped interval qualifier, line 7; light-source/intensity matching, line 8; playback confound and null, line 9; movement nulls, line 10). Licence 0; bibliographic 0; quote-form 0; name 0; duplicate 0. Uncounted: author form on all five lines (full names, desk uses Surname Initials). Line 11 can merge; lines 8 and 10 after the replacements; lines 7 and 9 only if the owner rules that observational encounter or catch counts against natural moonlight have a key, and then with the replacements below.

Owner question (recorded, not decided here): which key, if any, takes an observational association between an encounter or catch count and natural, calculated moonlight (no imposed light)? `behaviour_vision` substitutes behaviour for a count, and `ecological_intervention_outcome` requires an intervention. The answer also governs line 6 (Molossus molossus, same paper) and may touch main's Puffinus puffinus light-on counts.

## Replacement

All old strings occur exactly once in the named line. Strings in backticks marked "raw JSON" are matched against the raw line text; the others are plain string field contents.

Line 7 (apply only if the owner admits a key; otherwise drop):
- `value`: "89.5%)" -> "89.5%); estimate −0.23 (SE 0.16), 80% credible interval −0.46 to −0.04, 90% credible interval −0.52 to 0.01, which includes zero"
- `conditions`: "while other species were negative" -> "while C. maximiliani, P. kappleri and P. macrotis had high probabilities of negative effects; the P. kappleri 90% interval (−0.52 to 0.01, Table 2) includes zero; 1,544 P. kappleri passes (280 understory, 1,264 canopy); two towers 180 m apart, four recorders, site as random intercept; moonlight effect pooled over strata (no moon by stratum term)"
- `conditions`: "the page is inconsistent" -> "the Methods spell it 'Saut Pararé Nourages research station' and the caption 'Nouragues Research Station'"
- `source.authors` (raw JSON): `"authors": "Dylan G.E. Gomes, Giulliana Appel, Jesse R. Barber"` -> `"authors": "Gomes DGE, Appel G, Barber JR"`

Line 8:
- raw JSON: `"trait": "behaviour_vision"` -> `"trait": "ecological_intervention_outcome", "measured_endpoint": "presence and feeding of hedgehogs recorded by camera trap at the feeding station, per ten-minute block", "experimental_unit": "ten-minute block at a garden feeding station (33 gardens; individuals not identified)", "intervention": "one week of constant artificial light on the feeding station at night (the station's existing exterior light or, where none was suitable, a supplied LED floodlight of about 1,000 lumens, 10 W)", "comparator": "one week of darkness at the same station", "mechanism_limit": "camera-event counts combine activity, local availability and detectability; no sensory pathway is tested, and a null does not show that light is not perceived"`
- raw JSON: `"evidence_kind": "behavioural_response"` -> `"evidence_kind": "ecological_outcome"`
- raw JSON: `"eye": "whole animal"` -> `"eye": ""`
- `conditions`: "about 1,000-lumen LED floodlights" -> "the station's existing exterior light or, where none was suitable, a supplied LED floodlight of about 1,000 lumens (10 W), so intensity was not matched across stations"
- `conditions`: "individuals not distinguished as far as read" -> "individuals not recognised, and age and sex not recorded"
- `note`: "The Crossref licence lookup for this DOI failed twice (client error), so the licence rests on the page metadata, which lists CC BY 3.0." -> "The single-DOI Crossref lookup fails (client error); a Crossref list query (prefix 10.3390) returns CC BY 4.0 for the vor, and the page metadata lists CC BY 3.0."
- `source.authors` (raw JSON): `"authors": "Domhnall Finch, Bethany R. Smith, Charlotte Marshall, Frazer G. Coomber, Laura M. Kubasiewicz, Max Anderson, Patrick G. R. Wright, Fiona Mathews"` -> `"authors": "Finch D, Smith BR, Marshall C, Coomber FG, Kubasiewicz LM, Anderson M, Wright PGR, Mathews F"`

Line 9 (apply only if the owner admits a key; otherwise drop):
- `conditions`: "ringed only, no tags;" -> "a tape lure of skylark calls and song played in the middle of the nets, and the authors state no skylarks were observed when no playback was used, so catch depends on attraction to the lure (the Discussion adds that lower-flying birds may hear it better); ringed only, no tags;"
- `conditions`: "time since moonrise and time to moonset had no significant effect on occurrence" -> "time since moonrise and time to moonset had no significant effect on occurrence, and moonlight duration had no significant effect on abundance (0.05; −0.04 to 0.13)"
- `conditions`: "a credible interval for moonlight duration is printed with reversed bounds" -> "the occurrence estimate for moonlight duration is printed as mean 0.27, 95% CrI '0.07, − 0.49', with reversed bounds"
- `source.authors` (raw JSON): `"authors": "Dajana Prinz, Ramona Julia Heim, Moritz Meinken, Nick Niemann, Laurin Temme, Alexandra Esther, Wieland Heim"` -> `"authors": "Prinz D, Heim RJ, Meinken M, Niemann N, Temme L, Esther A, Heim W"`

Line 10:
- `conditions`: "visit duration trend about twice as long was not significant (p = 0.07)" -> "only three of seven movement behaviours changed significantly (Abstract) and the other four did not, including a visit duration trend about twice as long (p = 0.07)"
- `source.authors` (raw JSON): `"authors": "Bridgette Farnworth, Richard Meitern, John Innes, Joseph R. Waas"` -> `"authors": "Farnworth B, Meitern R, Innes J, Waas JR"`

Line 11 (optional and format only):
- `conditions`: "so the unit is the dish" -> "so the unit is probably the dish (the Figure 3 legend does not say whether n counts dishes or workers, or whether colonies were pooled)"
- `source.authors` (raw JSON): `"authors": "Yongyong Gao, Huan Xu, Bao Jia, Yutong Liu, Ali Hassan, Qiuying Huang"` -> `"authors": "Gao Y, Xu H, Jia B, Liu Y, Hassan A, Huang Q"`

Optional (uncounted): line 7 `note` could add the Table 2 row; line 10 `note` could add the Methods design (outdoor pen, tested once, 10 to 30 August 2016) already reflected in conditions.
