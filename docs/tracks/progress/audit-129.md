# Audit 129: desk-d39 (plant genera, batches 31 and 32, partial; branch origin/research/desk-d39, head b78fc399)

## Lines judged

- Evidence: all 5 lines of docs/views/evidence/desk-d39.jsonl.
- Search records: docs/views/searched/desk-d39.jsonl is empty (0 lines). The progress note says no null was filed because the protocol was not completed for any genus, so there is no search record to judge and no sample to draw.
- Wanted lines: both lines of docs/views/wanted/desk-d39.jsonl, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched (0 lines) and wanted (2 lines) files prints "0 problems".

## Method

I followed desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, the rulings in the launch prompt, and audits 90 and 128 as the format.

- Main. A script checked every evidence record's genus and trait against docs/views/evidence/*.jsonl and docs/views/searched/*.jsonl on the merge base (753c0cd8), and `git grep` repeated the evidence check on origin/main (5e7676b1). Main holds no evidence for Petasites, Lilium, Schinus or Lobularia. It holds only null search records for those genera (harvest-18:7 and 8, sweep-19:32, sweep-29:31, sweep-30:22, sweep-31:2), which these records answer. No record repeats a main (paper, quote, species, trait).
- Names. POWO or WFO pages were opened for each name in doubt (below).
- Searches. I ran 11 WebSearches and fetched only URLs they returned. I opened no ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page. Two ezproxyberklee.flo.org results and a brum.beds.ac.uk mirror of the MDPI page were left alone. No paper text is committed.

## Evidence verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Petasites pyrenaicus sense_chemical (Pattrick et al. 2017) | ok, with a cosmetic fault. Springer page opened: Arthropod-Plant Interactions 11: 623-627, 10.1007/s11829-017-9519-3. The quote is verbatim, in the Results, a whole sentence under 125 characters. The olfactometer figures (20.5% of time, p = 0.004, n = 16) match. Volatiles were taken in the field from living male inflorescences. The paper names P. fragrans, and WFO (wfo-0000005828, opened) lists P. fragrans as a synonym of the accepted P. pyrenaicus, so the record is rightly filed under the accepted name. Floral volatile signalling counts under 10(a). Cosmetic: the first author is spelled "Patrick JG"; the page gives "Pattrick". |
| 2 | Lilium longiflorum sense_light_nonvisual (Heins, Wilkins and Healy 1982) | ok, with a cosmetic fault. ASHS PDF opened: J Amer Soc Hort Sci 107(2): 335-338, no DOI shown. The quote is verbatim and reports the study's own result. It stands in the abstract, and the Results give the same result as "SD" with "8hr light" in the Table 3 caption, so `where: Results` is loose. The `method` field lists treatments from the paper's other experiments (light stress, total darkness, the 2200-0200 lighting, bud-opening cycles of 4, 6 or 12 h); all are in the Methods, but the value is the 8 h photoperiod experiment alone. Photoperiod counts as sense_light_nonvisual. One named species (cultivars 'Ace' and 'Nellie White'), so grade m holds. |
| 3 | Schinus molle sense_light_nonvisual (Pereira et al. 2016) | ok. Locus UFV record opened: Seed Sci Res 26(4): 351-361, 10.1017/S0960258516000167. The quote is verbatim in the abstract, and the abstract also says the seeds "are positively photoblastic". The record is marked partial, abstract only. A germination light response, so sense_light_nonvisual. |
| 4 | Schinus terebinthifolia sense_light_nonvisual (Gama and de Jesus 2019) | ok. revista.ueg.br PDF opened: Revista Agrotecnologia 10(2): 25-35, no DOI. The quote is verbatim in RESULTADOS. The treatments are 30, 50 and 80% shade and full sun. POWO 71069-1 (opened) accepts Schinus terebinthifolia Raddi, and the paper's -us spelling is a variant, so the filing is right. Set shade levels count as sense_light_nonvisual. |
| 5 | Lobularia maritima sense_chemical (Zammali et al. 2022) | ok, with a cosmetic fault. MDPI page opened: Seeds 1(2): 99-109, 10.3390/seeds1020009. The quote is verbatim in Results section 3.3. Methods give KNO3 10 mM, thiourea 50 mM, proline 1 mM and salicylic acid 10 µM, as the record says, and the text gives 60% against 30% after 20 days. POWO 1085072-2 (opened) accepts the name. A KNO3 germination response counts under sense_chemical. Cosmetic: the note says the Discussion gives other doses; the page shows the odd dose (20 mM KNO3) in the Results, and the Discussion gives none. |

Evidence errors: **0 of 5 (0%)**.

## Counts and pool

- Search records: none filed, so none judged.
- Evidence: 0 of 5, 0%.
- Unit: 0 of 5, 0%.

Pooled with audits 83 to 90 (audit 90's figures: 48 in 1026 search records; 52 in 1090 with evidence):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 52 in 1095, 4.7%.

If audit 128 (51 in 1061; 56 in 1133) is taken as the base instead, the overall pool is 56 in 1138, 4.9%.

**Verdict: pass.** All five evidence records hold, and the unit files no search record.

**Error lines:**
- docs/views/searched/desk-d39.jsonl: none (file empty).
- docs/views/evidence/desk-d39.jsonl: none.

Cosmetic fixes worth making: line 1 author "Pattrick JG"; line 2 `where` (abstract and Results); line 5 note (the 20 mM figure is in the Results). The progress note's header says "Evidence (6)", but the file holds 5 records.

## Wanted lines (listed, not counted)

- Line 1 (Asaadi 2022, 10.22126/ATIC.2022.7969.1058): the author, year, Agrotechniques in Industrial Crops 2(2): 94-103 and DOI match the DOAJ record (opened). But the abstract on atic.razi.ac.ir (opened) gives the lowest A. eupatoria vigour index (4.99) under 100 ppm gibberellic acid, and dry cold stratification the highest. Only a highlight says that using GA with other treatments improved germination. The line's "GA3 enhanced germination" may overstate the result, so whoever closes it should read the full Results.
- Line 2 (Vandelook, Bolle and Van Assche 2008, 10.1017/S0960258508038877): the authors, year, Seed Sci Res 18(3): 161-171 and DOI match the Cambridge page (opened). The abstract has the light sentence as a whole sentence: "embryo growth in these seeds could not be initiated because of the lack of a light stimulus" (the fetch gives it as a fragment, so the sentence start is still unconfirmed).

## Open cells

The progress note lists more than 20 genera searched without a filed record (Calypso, Eutrochium, Oemleria, Cocos, Daphne, Sequoia and others). No null was filed, so nothing is counted, and those cells stay open for a later unit.

## Blocked pages

None. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
