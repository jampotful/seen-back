# Audit 92: desk-d2 (7 plant genera; branch origin/research/desk-d2, head f8aad2a4)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 12 lines of docs/views/searched/desk-d2.jsonl (1 to 12).
- Evidence records: all 11 lines of docs/views/evidence/desk-d2.jsonl (1 to 11).
- Wanted lines: all 5, listed and not counted.

Ostrya has evidence only (lines 5 to 7) and no search record, which fits: its harvest lists sense_chemical and sense_light_nonvisual as open, and both are closed by those lines.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (12 lines) and the wanted file (5 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), and the rulings of audits 84 and 86 to 90.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus. All ten records for harvested genera match word for word and in order, with the "web: " lines after them: Osmunda (lines 1, 2), Antigonon (7, 8), Diodia (9 to 11) and Portulaca (12). Sisyrinchium (3, 4) and Catharanthus (5, 6) are in no harvest run and list "web: " lines only. No harvest shows a failed step, and no unlabelled line appears.

Chased. Every DOI named in Antigonon, Diodia and Portulaca is a citation step that the harvest prints (each returned 0 works). Osmunda, Sisyrinchium and Catharanthus give reasons. The Sisyrinchium and Catharanthus reasons rest on labelled web family searches, which audits 86 and 87 accept for genera in no harvest run.

Screened. Every screened DOI is printed by the harvest output for its genus, except W7210156986 in line 1 (Osmunda diel). Neither the harvest output nor `screen_candidates.py Osmunda` lists it, since diel is not an open Osmunda trait.

Searches. I ran 37 WebSearches:
- 13 to check evidence sources and taxonomy;
- 5 for wanted lines;
- the rest on the null records, weighted toward the germination and flower-timing phrasings that audits 88 to 90 found misses with.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.

## Search record verdicts (12)

| Line | Record | Verdict |
|---|---|---|
| 1 | Osmunda diel | **error: repeats a closed cell.** The harvest header gives Osmunda's open traits as sense_chemical and sense_light_nonvisual only. Diel and eye_type are already covered on origin/main by harvest-20.jsonl line 9 (the "diel; eye_type" record of 16 October). The unit's own progress note says that for this reason no new search record was written, yet the file holds one. The record also screens W7210156986, which no harvest or candidate listing prints. Its chased reason, "returned no review of the family", is arguable: the harvest family review printed 8 works, fern-wide reviews among them (10.1093/aob/mcp194). My own searches found nothing on Osmunda timing, so no measurement was missed. |
| 2 | Osmunda eye_type | **error: repeats a closed cell**, as line 1 (harvest-20 line 9 on main; the harvest shows the trait is not open). |
| 3 | Sisyrinchium eye_type | ok. Web-only. My pooled focusing searches returned the general set and nothing on Sisyrinchium. |
| 4 | Sisyrinchium sense_chemical | ok. Web-only. My searches turned up the following, and none of them measures a chemical response in a Sisyrinchium: <br>- germination hits on Sisymbrium (Carrillo-Barral et al. 2014, another genus); <br>- the Annales Bot Fennici smoke paper; <br>- the UW SISA4 protocol; <br>- MeJA papers on Nicotiana and Jacobaea (pherobase pages opened); <br>- the oil-trichome work (Chauveau et al., 10.1093/aob/mcr080; botany.one page opened: trichomes only, no scent emission). |
| 5 | Catharanthus diel | ok. Web-only. I opened four pages: <br>- Ravikumar and Dhatt 2023 in IJAgS 93(5) and in IJH 80(3): emasculation timing only; <br>- Ravikumar and Dhatt 2024 (Cambridge core reader): its opening-time sentence is background cited to their 2023b paper, as the record says; <br>- He et al. 2026 (Ornamental Plant Research review): no anthesis hour. <br>The rest of what came back was plant patents. |
| 6 | Catharanthus eye_type | ok. The conical-cell searches returned Antirrhinum (Glover and Martin 1998, opened) and general petal-optics reviews, none on Catharanthus. |
| 7 | Antigonon eye_type | ok. Queries match, and the chased steps are printed. Nothing on Antigonon focusing came back. |
| 8 | Antigonon sense_light_nonvisual | **error: missed measurement.** Planas i Puig 2018, "Effect of shade on Antigonon leptopus (Corallita) growth and germination rate", Utrecht University student thesis (studenttheses.uu.nl handle 20.500.12932/30639, page opened). Seeds and seedlings were grown under four shade treatments for about a month, with height, weight, leaf number, leaf area and seed survivorship measured. The thesis reports no significant difference between treatments. That is a growth and germination trial under set light intensities, which 10(d) counts, and a null result is still a measurement. My search "Antigonon leptopus shade tolerance experiment light treatment seedlings growth" returned it first. The unit itself logs an M.Sc. thesis as evidence (line 11), so a thesis source is in scope. Burke and DiTommaso 2011 (IPSM 4: 265-273, PDF opened) gives only "prefer full sun", with no measurement. |
| 9 | Diodia diel | ok. Diodia virginiana is accepted (POWO, opened). My searches returned profile pages, a uchicago vegetative-reproduction paper (10.1086/297035, blocked) and no opening hour. |
| 10 | Diodia eye_type | ok. Nothing on Diodia focusing came back. |
| 11 | Diodia sense_chemical | ok, with an open fork. My searches returned herbicide-control papers (Weed Technology; not a hormone or elicitor response under the reading audit 89 used) and the Weed Science germination paper. That paper's page refused my fetch too, as it refused the unit's. If it tests nitrate, GA or smoke, point 3 required sense_chemical to be held out as well. Unchecked: page blocked. |
| 12 | Portulaca eye_type | ok. Queries match, the chased steps are printed, and the three screened works are rightly reasoned. My focusing search returned general leaf-optics work (FIU cas_bio/44, PMC8309337), none on Portulaca. |

Search record errors: **3 of 12 (25.0%)**, lines 1, 2 and 8.

## Evidence record verdicts (11)

`partial` check: every record with access "abstract" (lines 1 to 7 and 9) carries `"partial": true`. Line 11 (a thesis read through a page summary) also carries it. Lines 8 and 10 are full-text PDFs without the flag, which is correct. So the flags are right, but the progress note's count is off. It says 7 records are from abstracts; the file has 8 abstract-access records, and 9 carry `partial`. It also says "Genera done (8)" and lists 7.

| Line | Record | Verdict |
|---|---|---|
| 1 | Osmunda cinnamomea sense_light_nonvisual (Bao et al. 1986) | **error: filed under a synonym's genus.** The abstract (bbr.nefu.edu.cn, opened) has the words, the 2000 lux and 20 C detail, and var. asiatica. But Osmunda cinnamomea L. is Osmundastrum cinnamomeum (L.) C.Presl, which PPG I (2016) segregates as its own genus. The Wikipedia page I opened says so, and my POWO search returned "Osmundastrum cinnamomeum" and subsp. asiaticum entries. Main already files this species as Osmundastrum cinnamomeum (oa-9). Audit 88's ruling applies, so the record should move to Osmundastrum. |
| 2 | Sisyrinchium bermudiana sense_light_nonvisual (Roberts 1990) | ok. ISHS page opened: the quote is verbatim, with 10 h against 14 h and 350 umol PAR. S. bermudiana L. is accepted (POWO, opened). |
| 3 | Catharanthus roseus sense_chemical (Dugé de Bernonville et al. 2017) | ok. The JIC page (opened) confirms the authors, Sci Rep 7, 10.1038/srep40453 and the verbatim quote. The JA, JA-Ile and OPDA detail is not on the abstract page (PMC gave a bot check), so `partial` is right. |
| 4 | Catharanthus roseus sense_chemical (Ababaf et al. 2021) | ok. Journal page opened: the quote is verbatim, and SA (0.5 and 1 mM, 24 to 48 h) and JA (10 uM, 12 to 24 h) match. |
| 5 | Ostrya carpinifolia sense_chemical (Pipinis et al. 2014) | ok. The DOAJ and journal pages (opened) give the quote verbatim, 94.17% for GA3 2000 ppm against 98.34%, and the DOI. |
| 6 | Ostrya virginiana sense_chemical (Franco Coronado and West 2013) | ok. ASHS page opened: the quote is verbatim, with GA3 at 0 to 5 uM in a 6 x 2 factorial. |
| 7 | Ostrya virginiana sense_light_nonvisual (same) | ok, requote (not counted). The value holds for the light-against-dark factorial. The quote, however, stops before the sentence's end ("... for germination of American Hophornbeam seed"), so it is not one complete sentence. |
| 8 | Antigonon leptopus diel (Raju et al. 2024) | ok. JoTT full text opened: the quote is verbatim, with closing by 1500 h and the authors, 16(1): 24597-24600 and DOI as recorded. |
| 9 | Portulaca oleracea sense_light_nonvisual (Gutterman 1974) | ok, wording fault (not counted). The BGU page (opened) gives the verbatim quote, Oecologia 17(1): 27-38 and 10.1007/BF00345093. The value's "seeds never germinated in darkness" goes beyond the abstract, which reports no dark germination after maturation under continuous red light. The short-day finding and "the shorter the daylength the faster the germination" hold. |
| 10 | Portulaca oleracea sense_light_nonvisual (Chauhan and Johnson 2008) | ok. CAWS PDF opened: the quote is verbatim, with 1.1 to 2.2% in darkness and 58.9 to 69.4% in light/dark. |
| 11 | Portulaca oleracea sense_chemical (Kaur 2019) | ok. Krishikosh PDF opened: the quote is verbatim, with 26.7% against 81.7%. |

Evidence errors: **1 of 11 (9.1%)**, line 1.

## Counts

- Search records: 3 of 12, 25.0%.
- Evidence: 1 of 11, 9.1%.
- Unit: 4 of 23, 17.4%.

Pooled with the desk's other audits of desk-screen units, starting from audit 90's corrected pool (search records 48 in 1026, and 52 in 1090 with evidence). Audit 91 is not on origin and is not included. With audit 92:
- Search records: 51 in 1038, 4.9%.
- With evidence included: 56 in 1113, 5.0%.

Forks that would change the count:
- Lines 1 and 2 (Osmunda). If the desk reads the brief's "repeats ... evidence on origin/main" as covering evidence only, and treats a duplicate search record for a closed cell as harmless, both lines stand (with W7210156986 removed). Search records would then be 1 of 12 (8.3%), and the verdict is unchanged.
- Line 8 (Antigonon). If the desk will not count a student thesis, the line stands. Search records would then be 2 of 12, and the verdict is still a fail.
- Line 11 (Diodia sense_chemical). If the blocked Weed Science paper tests a chemical cue, this line also fails under point 3.

**Verdict: fail.** The search records fail at 25.0% and the evidence at 9.1%. Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d2.jsonl: lines 1, 2 and 8.
  - Dropping 1 and 2 leaves Osmunda diel and eye_type as main already has them (harvest-20 line 9).
  - Dropping 8 reopens Antigonon sense_light_nonvisual. Planas i Puig 2018 (studenttheses.uu.nl 20.500.12932/30639) can close it.
- docs/views/evidence/desk-d2.jsonl: line 1. Refile it under Osmundastrum cinnamomeum (var. or subsp. asiaticum) rather than dropping it outright, if the desk prefers.

## Wanted lines (listed, not counted)

- Line 1 (Freitas and Sazima 2003, S. vaginatum): my search returned the title on repositorioslatinoamericanos.uchile.cl, but the page served only a DSpace shell. Authors, year and journal are not checked.
- Line 2 (Jamian et al. 2020): the JOPR page (opened) confirms all eleven authors, 32(3): 471-479 and 10.21894/jopr.2020.0053. The abstract says GC-MS was run on extracts and gives no A. leptopus result, so the wanted line's question stands.
- Line 3 (Diodia virginiana, Weed Science): the Cambridge page refused my fetch, so it is not checked.
- Line 4 (Portulaca umbraticola, 10.2503/hortj.okd-078, 2017): the DOI, title and year match the harvest output. The page itself was not opened.
- Line 5 (Portulaca smallii, 10.1016/s0033-7560(63)80023-x, 1963): this matches the harvest output (a closed work). It was not opened.

## Leads

- Antigonon sense_light_nonvisual: Planas i Puig 2018 (above).
- Catharanthus diel: Ravikumar and Dhatt "2023b", cited in their 2024 introduction for evening opening, is not yet identified. Their two 2023 papers that I opened (IJAgS 93(5), IJH 80(3)) give no opening hour.

## Blocked pages and unchecked items

- cambridge.org Weed Science Diodia virginiana germination abstract: permission unanswered (line 11 fork, wanted line 3).
- pmc.ncbi.nlm.nih.gov PMC5240345: bot check, so I used the JIC page.
- powo.science.kew.org taxon 177076-2: client error.
- journals.uchicago.edu 10.1086/297035: client error.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
