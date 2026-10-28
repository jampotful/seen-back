# Audit 118: desk-d28 (branch origin/research/desk-d28, head 13108321)

## Lines judged

I drew no sample. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 6 lines of docs/views/searched/desk-d28.jsonl.
- Evidence records: both lines of docs/views/evidence/desk-d28.jsonl.
- Wanted lines: all 3 lines of docs/views/wanted/desk-d28.jsonl. They are listed and not counted.

## Gate

I ran `python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (6 lines) and the wanted file (3 lines). It prints "0 problems". Both evidence lines parse. Their quotes are 65 and 73 characters long, but neither is a whole sentence (see below).

Unit housekeeping faults, not counted:
- The branch adds an empty file, docs/views/evidence/-h.jsonl, which looks like a script run with `-h`. It should be deleted before merge.
- The commit message says "4 wanted", and desk-d28.md is headed "Wanted (4)". The wanted file holds 3 lines.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule and the shared brief's rulings (audits 84, 86 to 90). Audits 90 and 117 served as the format. I ran 31 WebSearches:
- 21 for the null records (flower opening and anthesis hours, pollen-release hours, scent timing, germination light/dark, GA3 and dormancy, shade and light-intensity trials, jasmonate, herbivore and allelopathy responses, named species one at a time);
- 2 that re-ran the records' family-review searches;
- 4 for the evidence source and POWO names;
- 3 for wanted-line DOIs and titles;
- 1 for a screened DOI.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An ezproxyberklee.flo.org mirror and academia.edu hits (nwo.academia.edu/josefstuefer, an academia.edu directory) appeared in result lists, and I left them alone. No paper text is committed. origin/main is at 2819aa44.

### Queries

`harvest_get.py` ran offline.
- Phragmites, Corylus, Convallaria, Argentina and Chimaphila print "in no harvest run yet". Their records list "web: " lines only, which is correct.
- **Filipendula is in harvest run 4.** The harvest prints 12 queries: the three base queries; supplement runs 12, 14 and 20, which include "Filipendula flower opening time", "Filipendula anthesis" and "Filipendula circadian rhythm"; and the family review "Rosaceae photoreceptor review" (333 hits).
  - Record 4 lists none of these lines, and its `where` says "taxon is in no harvest run, so no harvest queries to copy". That is false.
  - The record's own `screened` block holds the five diel candidates that `screen_candidates.py Filipendula` lists from that harvest, and wanted line 3 cites the "Harvest abstract". The desk therefore read the harvest and still left its queries out.
  - Point 7 makes this an error.
- Bellis: the harvest (run 2) shows all three queries and both citation steps "error gave up", with only the family review run. The unit's claim holds, and it rightly wrote no Bellis record (point 6).
- No unlabelled query line appears.

### Chased

- All six records give "none: no measured relative and no family review found".
- For the five genera in no harvest run, the reason rests on labelled "<Family> photoreceptor review" WebSearches.
  - My re-runs of "Poaceae photoreceptor review" and "Ericaceae photoreceptor review" returned general plant-photoreceptor reviews, among them doc.rero.ch 309979 (Lariguet and Dunand 2005), which audits 86, 87 and 90 accepted as a chased DOI. None of these is a review of the family, so "no family review found" is literally true.
  - The records name no DOI, so no unsupported-DOI case arises. Not counted.
- For Filipendula (harvested), the harvest's own family review printed 333 hits, and the record never names it. My reading of its diel and light candidates found strawberry and pear photobiology papers but no Rosaceae flower-timing review, so the none-reason holds in substance. The wording fault is like audit 117's Sorbus, and the error for this record is already the queries.

### Synonyms (POWO, pages opened)

- Convallaria keiskei Miq. (ipni 533481-1): "This species is accepted." The evidence genus is right.
- Argentina anserina (L.) Rydb. (ipni 721546-1): "This species is accepted". Potentilla anserina appears only as an alternative taxonomy (Allred 2012). The genus is right, and P. anserina results count for Argentina.
- Ficaria Guett. (ipni 324406-2): "This name is a synonym of Ranunculus". The unit's skip of Ficaria is right. Its wording, "Ficaria is a synonym of Ranunculus ficaria", conflates the genus with the species (Ficaria verna is the synonym of Ranunculus ficaria, audit 112). Not counted.
- The Saponaria vaccaria note (POWO Gypsophila vaccaria) was not re-checked. It writes nothing, so it does not count.

### Main

- Main already holds old null search records for every unit genus: Phragmites sweep-7, Corylus sweep-9, Convallaria sweep-13, Filipendula sweep-10, Argentina sweep-13 and Chimaphila sweep-9. The unit's nulls repeat them. This is noted and not counted (audit 90, audit 113).
- Main holds evidence for Convallaria majalis sense_chemical only (sweep-13, Dordevic and Radulovic 2018, a flower extract). The C. keiskei lines are another species and a living-seed hormone and light trial, so they neither repeat nor contradict it. Kondo et al. 2015 (10.1017/S0960258515000136) is in no evidence, searched or wanted file on main.
- Wanted line 1 repeats main's wanted line harvest-c17 (Figura et al., filed for Orthilia, with the full author list and PMC6417480). It is listed below and not counted.
- No search record names a trait that main holds evidence for. Main's Saponaria officinalis diel evidence (10.1055/s-2007-978524) is another trait from wanted line 2's.

## Search record verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Phragmites diel | ok. The record is web-only, and the queries and none-reason are as above. My searches (P. australis and common reed anthesis hour, pollen release, florets opening in the morning) returned flora pages (pladias, VicFlora, ualberta), the ESA 2007 abstract, Dirr et al. 2023, the Setaria paper the record screens, and core.ac.uk 4846296 ("Geographic variation in growth responses in Phragmites australis", opened: seasonal flowering only). They also returned Martin, Chamecki and Brush 2010 (PSU page opened: ragweed only) and the Biological Flora of the British Isles account of P. australis (digitalcommons.uri.edu nrs_facpubs/637, unread lead). No hour of opening for a Phragmites species. |
| 2 | Corylus diel | ok, with a citation fault. My searches returned Piotrowska 2008, "Ecological features of flowers and the amount of pollen released in Corylus avellana and Alnus glutinosa", Acta Agrobot 61(1): 33-39 (pbsociety PDF opened: shedding best at 15-18 C, no hours). They also returned Weryszko-Chmielewska and Piotrowska 2012 (opened: Acta Sci Pol Hortorum Cultus 11(3): 69-78, daily counts only), hazelnut phenology pages and patents, and daily-count aerobiology papers (PMC4555345, aaem.pl). Hourly airborne pollen counts would not be flower opening under the owner's diel reading anyway. Fault, not counted: the record files the Lublin paper under 10.5586/aa.2012.002, but the paper it describes is in Hortorum Cultus. My search for that DOI returned only A&A pages, and the Crossref API was refused (proxy 403, then fetch permission unanswered), so the DOI is unverified. |
| 3 | Convallaria diel | ok. My searches returned Antirrhinum and carnation scent-rhythm papers, Kim et al. 2022, "Real-Time Visualization of Scent Accumulation..." (Frontiers 10.3389/fpls.2022.835305, opened: Lilium 'Siberia' only), and Odintsova and Fishchuk 2017, Acta Agrobot 70(1): 1705 (bibliotekanauki PDF opened: C. majalis flower morphology, "proterandrous", no hours). They also returned Araki, Shimatani and Ohara 2007, Plant Ecol 189(2): 175-186 (HUSCAP page opened: C. keiskei clonal pollination, no timing). No opening hour or scent timing for a Convallaria species. |
| 4 | Filipendula diel | **error: queries differ.** Filipendula is in harvest run 4, which prints 12 queries and a family review. The record lists none of them and states "taxon is in no harvest run" (point 7; see Queries). My own searches (F. ulmaria opening time and anthesis; F. vulgaris and F. rubra floral biology) returned PMC9862637 (blooming stages and essential oil, no hours), garden and flora pages, Denisow and Strzałkowska-Abramek 2013 on Syringa (opened: no Filipendula), and Begum et al. 2010 on Nymphaea (opened: no Filipendula). No measurement was missed, so the record can be rewritten with the harvest's queries copied and stand. |
| 5 | Argentina diel; sense_chemical; sense_light_nonvisual | **error: missed measurement (sense_light_nonvisual).** My search '"Potentilla anserina" shading treatment ramets light heterogeneity clonal integration biomass' returned first Wang, Li, During and Li 2011, "Do Clonal Plants Show Greater Division of Labour Morphologically and Physiologically at Higher Patch Contrasts?", PLOS ONE 6(9), 10.1371/journal.pone.0025401 (RePEc page opened; PMC3184135 gave a bot check). Its species is Potentilla anserina (= Argentina anserina, accepted in POWO). Connected and severed ramet pairs grew under set shade and full-light patches, and the abstract reports shoot-root allocation shifting between shaded and fully lit ramets, with higher chlorophyll content and photosynthetic capacity in fully lit ramets under high contrast. A growth trial under set light levels in a living plant counts under sense_light_nonvisual (owner's reading 10(d), audits 78 and 79). The record's searches looked only at germination and missed it. The same search returned Li, Wang and Ma 2008, Chin J Plant Ecol 32(5): 1166-1174, 10.3773/j.issn.1005-264x.2008.05.021 (opened), the same design on P. anserina with a "changing light regime"; its results are unread. The diel and sense_chemical parts found nothing: my searches returned wildlife-trust and flora pages, the UW ESRM 412 ARAN7 protocol (opened: "Seed has physiological dormancy", no trial), Zhao and Li 2010 on 蕨麻 tubers (magtech page opened: soak of unnamed solution, no light or hormone named), and herbivory papers on other species. |
| 6 | Chimaphila diel | ok, with a lead. My searches returned Knudsen and Olesen 1993, "Buzz-pollination and patterns in sexual traits in north European Pyrolaceae", Am J Bot 80(8): 900-913 (AGRIS page opened: C. umbellata polyads, nectar, visitors, no timing in the abstract). They also returned Feng et al. 2023 on Lonicera japonica (opened: not Chimaphila), and the illinoiswildflowers pipsissewa page. Knudsen and Olesen's full text may give flower or scent timing (Knudsen works on floral scent), so it is a lead, not a shown miss. |

Search record errors: **2 of 6 (33.3%)**, lines 4 and 5.

## Evidence record verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Convallaria keiskei sense_chemical (Kondo, Narita, Phartyal, Hidayati, Walck, J. Baskin, C. Baskin 2015, Seed Sci Res 25(2): 210-220, 10.1017/S0960258515000136) | **error (quote not a whole sentence).** The Cambridge Core page (opened) confirms the seven authors in order, the year, volume, issue, pages and DOI. Two independent reads, the Cambridge page and the UKY scholars page, say the abstract's sentence runs about 143 characters: "Alternating temperatures and light had negative effects on root emergence," followed by the GA3 clause. The record's quote "GA3 did not substitute for cold stratification in root emergence." is therefore the second clause, given a capital and a full stop as if it were a sentence. Since the whole sentence exceeds 125 characters, no compliant quote from it exists. The value (GA3 no substitute for cold stratification) is right, applied GA3 on living seed is 10(d), and grade m, `partial` and POWO acceptance (533481-1, opened) are right. Same ruling as audit 109 (Pyrus betulifolia). |
| 2 | Convallaria keiskei sense_light_nonvisual (same paper) | **error (quote not a whole sentence).** The quote "Alternating temperatures and light had negative effects on root emergence" is the first clause of the same sentence, without its comma and continuation. The value is supported, and the note rightly says light is not separated from alternating temperature in the abstract. The abstract's aim sentence ("Effects of temperature, light and GA3 on embryo growth and root and shoot emergence were tested under laboratory conditions.") shows that light was a tested factor. The trait (germination light trial, 10(d)), grade m and `partial` are right. |

Evidence errors: **2 of 2**. Both are form errors, and both values hold. They are repairable only by a quote from elsewhere in the paper, or by the desk's rule for over-long sentences.

## Wanted lines (3, listed, not counted)

1. Figura et al., Annals of Botany, 10.1093/aob/mcy195. The DOI, title opening, year 2018 and journal are confirmed on the Botany One page (opened), which names C. umbellata among the species cultivated (in the dark) and light, gibberellins and saccharides among the factors. Faults:
   - `authors` is empty and `year` null, although Botany One gives "Figura et al. 2018" and main's harvest-c17 line lists the five authors.
   - The title is truncated; main's line has "...and their post-germination ontogenetic development".
   - The work is already on main's wanted list (harvest-c17, for Orthilia), and an open copy exists (PMC6417480, in search results; isyeb.mnhn.fr and HAL hal-02187965 PDFs also appeared). `get` could point to the open copy.
2. 10.1055/s-0035-1565785 (Thieme). My search of the snippet returned that exact thieme-connect.de abstract URL, whose page title is the snippet "Saponaria officinalis L. has been used as a soft cleaning agent and medicinal plant. Understanding germination". The DOI and URL agree. Fault: the `title` is a placeholder ("Saponaria officinalis germination abstract (Thieme)"), and the journal is blank. Not opened (bot wall reported by the desk, not retried).
3. "Comparative biology of some fen plants Filipendula and Iris species" (1970), Spiral, hdl 10044/1/16366. The title, year and handle match the harvest output word for word, and the harvest prints no author, so the empty `authors` is right. No fault.

## Counts

- Search records: 2 of 6, 33.3% (lines 4 and 5).
- Evidence: 2 of 2 (lines 1 and 2).
- Unit: 4 of 8, 50%.

Pooled with the desk's running totals as carried by audit 117 (search records 50 in 1038; with evidence 57 in 1129). That chain runs through audits 83 to 90 and on to 117:
- Search records: 52 in 1044, 4.98%.
- With evidence included: 61 in 1137, 5.36%.

Fork that would change the count. Line 4's fault is the copy of harvest queries only; its searches missed nothing. If the desk treated a wrong "no harvest run" statement as a wording fault, the search-record count would be 1 of 6 (16.7%). The unit fails either way.

**Verdict: fail** (search records 2 of 6, evidence 2 of 2; both above 5%).

**Error lines to drop:**
- docs/views/searched/desk-d28.jsonl: line 4 (Filipendula diel; rewrite with the 12 harvest queries and the family review copied before the "web: " lines) and line 5 (Argentina; re-file without sense_light_nonvisual, and log Wang et al. 2011 or put it on the wanted list).
- docs/views/evidence/desk-d28.jsonl: lines 1 and 2 (quotes are clauses of one 143-character sentence).
- Also delete docs/views/evidence/-h.jsonl.

Lines 1, 2, 3 and 6 of the searched file stand and can merge.

## Leads (not counted)

- Argentina anserina sense_light_nonvisual: Wang, Li, During, Li 2011, PLOS ONE 6(9), 10.1371/journal.pone.0025401 (open access; PMC3184135). Li, Wang, Ma 2008, Chin J Plant Ecol 32(5): 1166-1174, 10.3773/j.issn.1005-264x.2008.05.021.
- Chimaphila umbellata diel: Knudsen and Olesen 1993, Am J Bot 80(8): 900-913, full text.
- Phragmites australis diel: the Biological Flora of the British Isles account (digitalcommons.uri.edu/nrs_facpubs/637), flowering section unread.
- Chimaphila light and chemical: Figura et al. 2018 open at PMC6417480.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC3184135: reCAPTCHA check; read via RePEc instead.
- api.crossref.org: proxy 403 from the shell; WebFetch permission unanswered, not retried.
- Cambridge Core long article URL: refused by the fetch proxy as too long; the short product URL served.
