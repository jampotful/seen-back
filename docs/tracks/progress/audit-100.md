# Audit 100: desk-d10 (re-screen of cells sent back by audits 98 and 99; branch origin/research/desk-d10, head cb222092)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 5 lines of docs/views/searched/desk-d10.jsonl (1 to 5).
- Evidence records: all 6 lines of docs/views/evidence/desk-d10.jsonl (1 to 6).
- Wanted line: 1, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (5 lines) and the wanted file (1 line) prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, and the rulings of audits 84 and 86 to 90, with audits 98 and 99 as the format. About 22 WebSearches and the WebFetches below, only on URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a researchgate.net PDF and an independent.academia.edu page in two result lists were left alone), and no paper text is committed. `harvest_get.py` and `screen_candidates.py` ran without the network (origin/ci). Main's evidence, searched and wanted files were checked for each evidence taxon and trait.

## Faults named by audits 98 and 99: were they fixed?

| Fault | Fixed? |
|---|---|
| Nyssa (d9 4 to 7) left out the harvest family review | Yes. Lines 1 to 4 list the four harvest queries and "Nyssaceae photoreceptor review" word for word and in order, then the "web: " lines. `chased` 10.1093/jpe/rtv012 is the first work that family review prints (harvest run 10). |
| Lolium (d9 10) gave the family review only as a "web: " line | Yes. Line 5 lists all eleven harvest lines in harvest order, the family review included. `chased` 10.1093/jxb/erm205 is printed under that family review ("The molecular analysis of the shade avoidance syndrome in the grasses has begun", 2007). |
| Argan filed as Sideroxylon | Yes. POWO 785772-1 opened: "This name is a synonym of Sideroxylon spinosum". Evidence line 4 is filed as Sideroxylon spinosum. |
| Melinis minutiflora Khan et al. 1997, 10.1038/41681 | Yes. The Rothamsted repository record (opened) gives Khan, Ampong-Nyarko, Chiliswa, Hassanali, Kimani, Lwande, Overholt, Pickett, Smart, Wadhams and Woodcock, Nature 388(6643): 631-632, 1997, DOI 10.1038/41681. nature.com/articles/41681 (opened) holds the quoted sentence verbatim. |
| Pueraria lobata and Eleusine MeJA records must be living-plant responses | Yes. Wang et al. 2019: living two-week-old seedlings in ½ MS liquid medium given 100 µM MeJA for 7 days against a 0.001% ethanol mock. Ye et al. 2025: sprouts germinated in the dark at 31 °C for 6 days with 150 µM foliar MeJA; growth was measured on the living sprouts, which were frozen only for assays. Both are 10(d). |
| Carica papaya light (Suwarno 1990) to the wanted list | Yes, wanted line 1. |
| Calystegia sepium is Convolvulus sepium | Not re-filed (the progress note skips it), which is right while the queue still carries Calystegia. |

## Search record verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Nyssa diel | ok. Queries and chased match; screened names both tool candidates. My anthesis search returned the 'Nsuhh' plant patent, a WV wetland flora sheet, a nursery sheet and the Wikipedia anthesis page, none with an hour for a Nyssa species. |
| 2 | Nyssa eye_type | ok. Plant eye_type is none (10(b)); the tool lists no candidate. |
| 3 | Nyssa sense_chemical | **error: missed germination-treatment title (10(e), point 3).** The record's own note calls journal.kib.ac.cn Y2007/V29/I03/351 an unchecked lead, yet closes the trait. The oriprobe table of contents for Acta Botanica Yunnanica 2007 issue 3 (opened) names the article on p. 351: Sun Bao-Ling, Zhang Chang-Qin, Zhou Feng-Lin, Shi Fu-Qiang and Wu Zhi-Kun, "Seed Morphology and Effects of Different Treatments on Germination of the Critically Endangered Nyssa yunnanensis (Nyssaceae)". A title naming germination treatments for a species of the genus goes on the wanted list and keeps the trait out of the search record. Other checks are clean: queries and chased match, all nine tool candidates are screened, DeBell and Naylor 1972 (AGRIS record opened: temperature, water regime, aeration, seed-coat removal) and Balestri 2015 (Iowa State thesis, opened: stratification and pulp only) hold no hormone or elicitor trial, and my floral-scent search found nothing on Nyssa. |
| 4 | Nyssa sense_light_nonvisual | **error: missed germination-treatment title**, the same Sun et al. 2007 article. My "Nyssa seed germination light dark" search returned it first, as the desk's did. The journal page still redirects to integrativebiology.ac.cn, so whether its treatments include light is unread. All eight tool candidates are screened. The sjfsci.com nursery study (Qiu, Yang, Zhong and Chen 2013, J Sichuan For Sci Technol 34(2): 66-68, opened) has no light test. |
| 5 | Lolium eye_type | ok. Queries and chased match, all seven tool candidates are screened with the 10(b) reason where apt. My focusing search returned Dunn et al. 2015 (10.1086/683278, which the record names), Forde 1959 on ryegrass epidermal cell dimensions (ir.wgtn.ac.nz, opened, growth anatomy only) and the general leaf-optics set. |

Search record errors: **2 of 5 (40%)**, lines 3 and 4.

## Evidence record verdicts (6)

No line repeats or contradicts evidence on main: main holds no evidence for Melinis, Sideroxylon (diel or sense_chemical), Argania, Pueraria, Eleusine or Agave potatorum in these traits. Main's sweep-40:13 (Polianthes tuberosa, floral scent) is a different species and measurement, as line 2 notes. Main's harvest-c10 wanted lines 118 and 163 list Ye et al. 2025 and Wang et al. 2019; lines 5 and 6 now log them. All six carry "partial": true. Melinis minutiflora, Agave potatorum, Sideroxylon obtusifolium, Pueraria montana var. lobata (POWO 967441-1 per audit 99) and Eleusine coracana are accepted names in accepted genera; I opened only the argan page.

| Line | Record | Verdict |
|---|---|---|
| 1 | Melinis minutiflora sense_chemical (Khan et al. 1997) | ok. DOI, year, journal and pages confirmed; the quote is one whole abstract sentence, verbatim; the herbivore-damage clause of the value is in the abstract. Grade m, partial. |
| 2 | Agave potatorum sense_chemical (Villavicencio-Gutiérrez et al. 2024) | ok. INIFAP PDF opened: authors, 15(86), DOI 10.29298/rmcf.v15i86.1403, 28 ± 1 °C with 8 h light and 16 h dark. The quote is a whole sentence of the English abstract. Control 53.06%, 1,000 ppm 60.56%. The paper's own words are "1 000 ppm AG3 had an inhibitory effect", though 60.56% sits above the control in the same Tukey group; the value repeats the paper and is not wrong. |
| 3 | Sideroxylon obtusifolium diel (Kiill, Martins and Silva 2014) | ok. Embrapa PDF opened: Rev Árvore 38(6): 1015-1025, no DOI printed. The quote is one whole English sentence ("... have diurnal anthesis and protogynous dichogamy."). The Portuguese text gives "nas primeiras horas da manhã" and the stigma change "por volta das 7 h"; the bud stigma is exposed "a partir das 4h30". Flower-opening timing in a named species. |
| 4 | Sideroxylon spinosum sense_chemical (Alouani and Bani-Aameur 2004) | ok, **requote (not counted)**. afs-journal.org abstract opened: Ann For Sci 61(2): 191-194, DOI 10.1051/forest:2004011, combined treatment 79.5%. The sentence begins "In contrast, either GA application ..."; the quote drops "In contrast," and capitalises "Either", so it is not the whole sentence. The value stands. |
| 5 | Pueraria lobata sense_chemical (Wang et al. 2019) | ok. Frontiers page opened: authors, Front Plant Sci 10, DOI 10.3389/fpls.2019.00028; the quote is a complete Results sentence; living seedlings, MeJA up-regulated all three UGTs. |
| 6 | Eleusine coracana sense_chemical (Ye et al. 2025) | ok. MDPI page opened: authors, Plants 14(14): 2201, DOI 10.3390/plants14142201; the quote is a whole abstract sentence; 150 µM foliar MeJA on sprouts grown in the dark at 31 °C. |

Evidence errors: **0 of 6 (0%)**. Requote, not counted: line 4.

## Wanted line

Line 1 (Suwarno 1990): IPB repository full record opened. Authors "Suwarno, Faiza C.", 1990, the title as given, Buletin Agronomi XV(3), no DOI, the PDF bitstream as `get` names it. No fault.

## Rates

- Search records: 2 of 5, 40%.
- Evidence: 0 of 6, 0%.
- Unit: 2 of 11, 18.2%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 50 in 1031, 4.8%.
- With evidence included: 54 in 1101, 4.9%.

Fork that would change the count: if the desk counts only titles whose treatments are shown (Sun et al. 2007 says "different treatments" without naming light or hormones), lines 3 and 4 stand and the unit has no error. I count them, as audit 99 counted the Suwarno title, because the record itself flagged the lead and closed the cells anyway, which point 3 forbids.

**Verdict: fail** on search records (2 of 5); evidence passes. Both files were judged whole, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d10.jsonl: lines 3 and 4 (Nyssa sense_chemical and sense_light_nonvisual). Sun, Zhang, Zhou, Shi and Wu 2007, Acta Botanica Yunnanica 29(3): 351, should go on the wanted list for Nyssa yunnanensis (both traits); the journal's own page redirects and was not read.
- docs/views/evidence/desk-d10.jsonl: none. Line 4 should be requoted to the whole sentence ("In contrast, either GA application ...").

## Blocked pages

- journal.kib.ac.cn EN pages redirect to integrativebiology.ac.cn/pd; the CN page waited on a permission request and was not retried.
