# Audit 112: desk-d23 (2 evidence records; branch origin/research/desk-d23, head 5cdd624c)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: both lines of docs/views/evidence/desk-d23.jsonl.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone: the Primula forbesii skip, and 4 others spot-checked from its progress file (Vitis riparia, Daucus carota, Vaccinium myrtillus, Chelone glabra); Oxalis tuberosa was tried and could not be checked.

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. Both evidence lines parse as JSON. Quote lengths: 89 and 118 characters.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings included), the counting rule of audit 39, the rulings of audits 84 and 86 to 90, the taxon rulings of audits 86, 88, 94 and 111, and audits 110 and 111 as format. For each record I ran a title WebSearch, fetched URLs that search returned, and compared authors, year, journal, DOI, quote, value, trait, grade and partial flag. Names were checked on POWO pages my searches returned. I checked origin/main (08a74ccf, the desk-d21 merge after audit 111) docs/views/evidence, docs/views/searched and docs/views/gaps/queue.jsonl for both taxa.

Searches: 12 WebSearches. I fetched only URLs my searches returned. The PMC page for the published oak paper (PMC12050401) was not answered at the permission step and was not retried, so the published wording stays unchecked, as the record's note says. The Oxalis tuberosa paper was not returned by either of my two searches. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Quercus robur sense_chemical (Sanchez-Lucas, Bosanquet, Henderson, Catoni, Pastor, Luna 2025, Plant Cell Environ 48(6): 4455-4474, 10.1111/pce.15419; quote from bioRxiv 10.1101/2024.09.20.613659) | **ok, value wording to tighten.** The UJI portal record (opened) gives the six authors in the record's order, 2025, Plant, Cell and Environment 48(6): 4455-4474 and DOI 10.1111/PCE.15419; my title search returned the preprint, the PMC article and the UJI record under the same title, so the authors and DOI belong to the paper the preprint became. The bioRxiv full PDF (opened) prints no byline, as the note says, and states 3-month-old Q. robur seedlings, BABA 5 mM soil drench, SA 5 mM foliar spray, JA 500 uM foliar spray, inoculation with Erysiphe alphitoides 7 days after treatment at 1.5x10^6 spores/mL, a glasshouse at 16/8 h with 42% RH, UK provenance 405, and field cages at BIFoR FACE scored at 30 dpi. The quote is one whole Discussion sentence, word for word (89 characters). Elicitor and hormone response of living plants is inside the owner's sense_chemical reading; grade m and no partial flag fit a full text read. Fork: the preprint also says "Under field conditions, a significant reduction in disease severity at 30 dpi was confirmed only for BABA treatment" and "SA only enhanced resistance in laboratory conditions". The value's closing "(glasshouse and field)" follows the JA clause and matches the preprint's "JA had no significant impact on resistance in both conditions", so I read it as scoping JA and count the record ok; read as scoping the whole value it would wrongly claim SA worked in the field. The value should say so outright (SA in the glasshouse only; in the field only BABA). The glasshouse temperatures print garbled in the PDF text ("20_/18_"), so "20/18 C" is not confirmed. Main holds no Quercus robur evidence (it appears only in the conditions of desk-d6:6, a Carpinus betulus record); queue line 1634 lists Q. robur sense_chemical open. No repeat. |
| 2 | Ranunculus ficaria diel (Prokop, Provazník, Tučník 2025, Plants 14(10): 1437, 10.3390/plants14101437) | **ok.** The MDPI page (opened) confirms the three authors in order, volume, issue, article number, year and DOI, the quote word for word as one whole abstract sentence (118 characters), the site near Trnava, 4 to 24 April 2021 and day 4 to 17 C, night -2 to 6 C. POWO ipni 711233-1 (opened): "This name is a synonym of Ranunculus ficaria", so the name follows audit 111's fix. Value, method, grade m and partial false (MDPI full text) are as audit 111 confirmed. Main (08a74ccf) holds no evidence record under Ficaria or Ranunculus ficaria in any evidence file (its Ranunculus evidence is R. sceleratus, desk-d16:1 to 3, and R. asiaticus, sweep-6:31), so no repeat. Main's null search records harvest-9:53, sweep-5:25 and desk-c12:2 (genus Ficaria) remain contradicted, main's fault, not counted. |

## Leads left alone (not counted)

| Lead | Unit's reason | My check |
|---|---|---|
| Primula forbesii photoperiod (Li et al. 2026, 10.1016/j.scienta.2026.114774) | POWO synonym of Primula filipes | **Confirmed.** POWO ipni 701943-1 (opened) is Primula forbesii Franch. and says "This name is a synonym of Primula filipes". Skipping under the synonym rule is right; filing under P. filipes is open for a later unit. |
| Vitis riparia (Garris et al. 2009, J Am Soc Hortic Sci 134(2): 261-272) | summary-length abstract, no quotable sentence | **Confirmed.** openprairie.sdstate.edu record (opened): the only sentence of 125 characters or fewer is a QTL-mapping sentence with no photoperiod value; the photoperiod sentences are longer. |
| Daucus carota smoke (Çatav, Küçükakyüz, Tavşanoğlu, Akbaş 2015, Ann Bot Fenn 52(1-2): 93-100) | the sentence naming D. carota is over 125 characters | **Confirmed.** acikerisim.mu.edu.tr record (opened): the sentence names D. carota, O. caricum and S. spinosum and goes on to Hypericum aviculariifolium, over 125 characters; no DOI on the page. |
| Vaccinium myrtillus (Uleberg et al. 2012, J Agric Food Chem 60(42): 10406-10414) | results are about temperature, not photoperiod | **Confirmed.** NIBIO Brage record (opened): the abstract's results are temperature and clone effects; no sentence reports a day-length effect. |
| Chelone glabra (Richardson, Irwin 2015, J Pollin Ecol 17: 132-144) | nectar timing only | **Confirmed for the abstract** (pollinationecology.org page opened): diurnal variation in reward presentation, tied to "floral phenology", with no opening or scent timing given. The full-text PDF was not read. |
| Oxalis tuberosa (Gancheva, Tkachenko 2026) | abstract cut off, page refused | **Unchecked.** Neither of my two searches returned the paper. |

## Counts

- Search records: 0 of 0.
- Evidence: 0 of 2.
- Unit: 0 of 2, 0%.

Pooled with audits 83 to 90, from audit 111's figures (search records 48 in 1026; with evidence 53 in 1098):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 53 in 1100, 4.8%.

**Verdict: pass.** Both lines can merge.

**Error lines to drop:**
- docs/views/evidence/desk-d23.jsonl: none.

Follow-ups:
- Line 1: reword the value so the field result is explicit (BABA enhanced resistance in glasshouse and field; SA in the glasshouse only; JA had no effect in either), and drop or confirm the "20/18 C" glasshouse temperature, which prints garbled in the preprint. Check the published PMC12050401 wording when that page can be read.
- Main's Ficaria null records (harvest-9:53, sweep-5:25, desk-c12:2) and the queue's Ficaria verna rows should move under Ranunculus and be re-opened now that the measurement lands.
- Primula forbesii photoperiod could be filed under Primula filipes by a later unit.
