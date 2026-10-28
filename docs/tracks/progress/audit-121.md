# Audit 121: desk-d30 (19 plant genera; branch origin/research/desk-d30, head ae8a10cf)

## Lines judged

No sample was drawn. The brief asks for the whole unit so that error lines can be dropped.
- Search records: all 32 lines of docs/views/searched/desk-d30.jsonl.
  - The 15 diel and sense_chemical nulls each got my own WebSearches: lines 1, 3, 4, 6, 9, 11, 13, 16, 18, 19, 21, 23, 27, 29 and 31.
  - The 17 eye_type nulls were judged against owner's reading 10(b), with one pooled focusing search and the mechanical checks.
- Evidence records: all 3 lines of docs/views/evidence/desk-d30.jsonl.
- Wanted lines: all 4, listed and not counted.

## Gate

I ran `python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (32 lines) and the wanted file (4 lines). It prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86, 87, 88 and 90. Audit 90 served as the format.

### Queries

`harvest_get.py` ran offline from origin/ci. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus.
- Harvest-run claims. Every record that claims a harvest run matches its harvest word for word and in order, with the "web: " lines after them. These are lines 1 to 3 (Cymbalaria, run 4), 13 and 14 (Dactylorhiza, run 4), 15 (Epilobium), 16 and 17 (Athyrium), 18 (Dipterostemon, run 2), 23 and 24 (Lindera, run 5), 27 and 28 (Encelia) and 31 and 32 (Malva).
- No harvest shows "gave up", and no record has an unlabelled line.
- The genera the records call absent are in no harvest run, as `harvest_get.py` prints: Conium, Tripleurospermum, Berberis, Abies, Fouquieria, Betula, Thuja, Lupinus, Picea and Symphoricarpos. Their records list "web: " lines only.

### Chased

- Lines 6 and 7 (Tripleurospermum) name 10.1007/s10265-016-0785-4. My own "Asteraceae photoreceptor review" search returned "evolutionary aspects of plant photoreceptors" (nutrition-evidence.com, opened). That page gives Li and Mathews 2016, J Plant Res 129(2): 115-22, with this DOI. The chased DOI is supported, as in audits 86 and 87.
- Lines 13 and 14 name 10.3390/horticulturae9091007, and lines 31 and 32 name 10.1016/j.tree.2009.09.010. Both DOIs are citation steps that the harvest prints, so they are supported. Each harvest also prints other citation steps that the records leave out:
  - Dactylorhiza: 10.1007/s00442-004-1750-9.
  - Malva: 10.3390/plants12132484 and 10.1017/S0043174500050177.

  This is noted and not counted.
- All other lines read "none: no measured relative and no family review found". No harvest prints a family review or citation step for those genera.

### Main

I checked origin/main (58dfef7f) docs/views/evidence/*.jsonl for every genus in the unit.
- Abies holds sense_chemical evidence only.
- Picea holds diel, sense_chemical and sense_light_nonvisual. The unit writes only Picea eye_type.
- Lupinus holds light and chemical. The unit writes only eye_type.
- Betula holds light only. Lindera, Epilobium, Athyrium and Malva hold light only.
- Dactylorhiza holds sense_chemical only (D. majalis). The unit writes diel and eye_type records and a sense_light_nonvisual evidence record. Neither the evidence nor any search record repeats main.
- Mahonia japonica (main) carries diel and light evidence. It is Berberis japonica under the audit-88 ruling, which bears on the Berberis diel cell. The unit writes only Berberis eye_type, so it does not conflict.
- No unit search record names a trait that main holds evidence for. No evidence line duplicates or contradicts main evidence.
- Every genus also has an older multi-trait search record on main (for example "diel; eye_type; sense_chemical; sense_light_nonvisual"), and the unit's records re-search those cells. Following audit 90, I note this and do not count it.

### Searches and fetches

I ran about 50 WebSearches and fetched only URLs that my own searches returned. I opened no ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page; an academia.edu result for the Fouquieria search was left alone. Two fetches failed or were blocked:
- The bioone.org Southwestern Naturalist page failed at its site.
- An archive.org biostor PDF (dn760104.eu.archive.org) was blocked by the permission layer and not retried.

No paper text is committed.

## Search record verdicts (32)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cymbalaria diel | ok. Queries match run 4. My searches returned flora and extension pages and Prieto-Benitez et al. 2016 (PMC5055817, opened: Silene colorata, no Cymbalaria). No Cymbalaria opening hour. |
| 2 | Cymbalaria eye_type | ok. Queries match, and 10(b) applies. |
| 3 | Cymbalaria sense_chemical | ok. Queries match. My germination (light, gibberellin) and volatile, herbivore and jasmonate searches returned Arabidopsis and general pages only. |
| 4 | Conium diel | ok. Web-only. Two searches (Latin and common name) returned weed fact sheets and Heracleum phenology. No Conium hour. |
| 5 | Conium eye_type | ok (10(b); pooled focusing search found nothing). |
| 6 | Tripleurospermum diel | ok. Web-only, and chased is supported (above). My capitulum-rhythm search returned only sunflower circadian work. My germination search returned a Centaurea paper (PJB 38(4): 983, opened, no Tripleurospermum). |
| 7 | Tripleurospermum eye_type | ok. |
| 8 | Berberis eye_type | ok. |
| 9 | Abies diel | ok. Web-only. My pollen-shedding search returned seed-orchard phenology reports. Conifer pollen release is not flower opening under the owner's diel reading. |
| 10 | Abies eye_type | ok. |
| 11 | Fouquieria diel | ok, with a lead. Web-only. The pages I opened give no hour of opening or nectar timing: Scott 1989 (LSU dissertation, opened, seasonal only), Bowers 2006 (Plant Ecol 186: 87-95, Springer opened, branch length) and the FEIS review. Bowers 2005 is titled "Influence of plant size and climatic variability on the floral biology of Fouquieria splendens" (Madrono 52: 158-165; BHL part 169116, opened, metadata only). It may hold daily timing and stays an unread lead, not a shown miss. |
| 12 | Fouquieria eye_type | ok. |
| 13 | Dactylorhiza diel | ok. Queries match, and chased is printed (incomplete, noted). My scent-rhythm search returned the general circadian-scent review (PMC4829607) and Gymnadenia and Arum work, none for Dactylorhiza. |
| 14 | Dactylorhiza eye_type | ok. |
| 15 | Epilobium eye_type | ok. |
| 16 | Athyrium diel | ok. Queries match. My spore-discharge search returned propagation protocols and flora pages, with no time-of-day spore release. |
| 17 | Athyrium eye_type | ok. |
| 18 | Dipterostemon sense_chemical | ok. Queries match run 2. Three searches (smoke, GA3 and karrikin; Keeley smoke study; stratification) returned Keeley and Fotheringham 1998 (Ecology 79: 2320-2336, USGS page opened, no Dichelostemma or Dipterostemon named) and the UW ESRM protocols, which the record already cites. POWO lists Dichelostemma capitatum as a separate page (result titles only), and the accepted genus Dipterostemon is as the record says. |
| 19 | Betula diel | ok. Web-only. My anther-dehiscence search returned airborne pollen-flight papers (Diurnal pattern of Poaceae and Betula pollen flight). The record rightly treats air counts as not flower opening. |
| 20 | Betula eye_type | ok. |
| 21 | Thuja diel | ok. Web-only. My pollination-biology search returned flora, wiki and phenology pages. |
| 22 | Thuja eye_type | ok. |
| 23 | Lindera diel | ok, with a lead. Queries match run 5. My second search returned "Phenology and flower-visiting entomofauna of six species of Lindera (Lauraceae) in Japan" (Nordic J Bot 19(6): 707-718, 1999, 10.1111/j.1756-1051.1999.tb00680.x; researchmap page opened). The opened text gives seasonal flowering only, with no time of day, so this is a lead and not a miss. |
| 24 | Lindera eye_type | ok. |
| 25 | Lupinus eye_type | ok. |
| 26 | Picea eye_type | ok. |
| 27 | Encelia diel | ok. Queries match. My capitulum-timing search returned only sunflower circadian work. |
| 28 | Encelia eye_type | ok. |
| 29 | Symphoricarpos diel | ok. Web-only. My nectar and anthesis search returned Denisow and Anton 2012 (Acta Agrobot 65(1): 37-44, opened: Aquilegia vulgaris only), a Cornus alba nectary paper (Springer s00606-010-0364-4, opened) and bee-forage pages. No Symphoricarpos hour. |
| 30 | Symphoricarpos eye_type | ok. |
| 31 | Malva diel | ok. Queries match, and chased is printed (incomplete, noted). I opened the screened M. sylvestris floral-biology paper (journal.iahs.org.in ijh 1341). It says anthers dehisce before the flowers open and gives pollen viability peaking at 11 am, with no time of flower opening, so the screening reason holds. |
| 32 | Malva eye_type | ok. |

**Search record errors: 0 of 32 (0%).**

## Evidence record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Berberis koreana sense_chemical | ok. MDPI page opened: Kim, Kim, Lee, Na and Lee 2023, Horticulturae 9(5): 547, 10.3390/horticulturae9050547. "However, the GA3 treatment had little effect on the seed germination." is verbatim, whole, and under 125 characters. The doses are copied exactly: abstract 0, 10, 100 and 1000 mg·L−1; Methods 10, 100, 500 and 1000 mg·L−1 for 24 h at room temperature, with a distilled-water control. The 71% after 12 weeks at 4 C matches. Berberis is an accepted genus, and the species is not a synonym of another genus. Grade m, partial (summariser), is right. |
| 2 | Dactylorhiza majalis sense_light_nonvisual | ok. The ucviden.dk page (opened) gives Rasmussen, Andersen and Johansen 1990, Physiol Plant 79(2): 226-230, 10.1111/j.1399-3054.1990.tb06734.x. The quote matches except that the source has an en dash in "10–14", which the record's note discloses (a typographic difference, as in audit 39). The value (light stimulation, then about 14 days of darkness, and interruption before day 8) matches. Abstract-only, so partial is right. |
| 3 | Symphoricarpos microphyllus sense_light_nonvisual | ok. The Redalyc PDF (opened) gives Martinez Orea et al. 2019, Acta Bot Mex 126: e1458, 10.21829/abm126.2019.1458. "In cameras, germination percentages were the highest in FRL (32%)." is verbatim. Kew's species page (opened) lists S. microphyllus (Humb. & Bonpl. ex Schult.) Kunth as accepted. |

**Evidence errors: 0 of 3 (0%).**

## Fouquieria: an unwritten lead

My searches found the Southwestern Naturalist 48(1) 2003 paper, DOI 10.1894/0038-4909(2003)048<0001:EOSAGS>2.0.CO;2. The bioone slug reads "Effects of seed age, germination substrate, gibberellic acid, light and ...", and the result came back for a Fouquieria GA search. The bioone page failed at its site, and the issue TOC returned no content, so neither I nor the unit could see which species it covers. I did not open the academia.edu copy.

The unit wrote no null for Fouquieria sense_chemical or sense_light_nonvisual, and these cells stay open, so no record is wrong. It also wrote no wanted line, because the title it saw names no species. Once the species is confirmed as a Fouquieria, the paper belongs on the wanted list under 10(e). The desk should resolve this from a build machine.

## Counts

- Search records: 0 of 32, 0%.
- Evidence: 0 of 3, 0%.
- Unit: 0 of 35, 0%.

Pooled with audits 83 to 90, using audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence):
- Search records: 48 in 1058, 4.5%.
- With evidence included: 52 in 1125, 4.6%.

Forks that would change the count:
- Lines 13, 14, 31 and 32 name only one of the citation-step DOIs that the harvest prints. If the desk reads `chased` as having to list every printed citation step (audit 90 says its lines "name exactly the citation-step DOIs their harvest output prints"), these four become errors, and search records go to 4 of 32 (12.5%, a fail). I count them as supported, because the DOI named is printed and the brief's error is an unsupported DOI.
- Lines 11 and 23 have unread leads (Bowers 2005 on Fouquieria floral biology; the Lindera phenology paper of 1999). If the full texts give flower-opening hours, those lines become missed measurements.

**Verdict: pass.** Both whole files were judged, and no line needs dropping. The four chased lines should be completed with the omitted citation-step DOIs.

**Error lines to drop:**
- docs/views/searched/desk-d30.jsonl: none.
- docs/views/evidence/desk-d30.jsonl: none.

## Wanted lines (listed, not counted)

- Line 1 (Zhang, Sharifi and Nobel 1995). The CSIRO page (opened) confirms the authors, year, Aust J Plant Physiol 22(5): 833-841, DOI 10.1071/PP9950833, and the 40% shade contrast.
- Line 2 (Padgett, Vazquez and Allen 1999). The BHL part 171458 (opened) confirms the title and authors, and shows no year or DOI. The USFS Woody Plant Seed Manual Encelia PDF (opened) gives 1999, Madrono 46(3): 126-133, and 100 ppm GA for 30 minutes raising germination 2 to 3-fold. The DOI field is empty, and none was shown.
- Line 3 (Jurado et al. 2011). The IPICYT repository page (opened) confirms Phyton (Buenos Aires) 80(1): 101-105, 2011, and 30% best germination. It gives the authors as Enrique Jurado Ybarra, Marco Antonio Marquez Linares and Joel David Flores Rivas, so the line's surnames are shortened (cosmetic). It shows no DOI.
- Line 4 (Laskowski et al. 2013). **Fault:** the DOI field is empty, but the NPJ page (opened) prints DOI 10.3368/npj.14.1.49. The authors, year, 14(1): 49-54, the 1:50 (v:v) result and the A. montana subsp. montana stand-in all match.
