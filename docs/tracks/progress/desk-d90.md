# desk-d90 progress (East and Southeast Asian wild plants, regional English-abstract journals)

Started 29 October 2026. Branch research/desk-d90. About 25 WebSearches and 35 WebFetch pages. Curl is refused by the proxy, so every page came through WebFetch (which caps verbatim quotes; sentences were taken only where the fetch printed them whole, and each filed quote was confirmed a second time with a yes/no request). Almost all hits were koreascience.kr open PDFs; Taiwanese, Thai, Indonesian, Philippine and Malaysian searches returned no quotable single-species trial.

## Filed (6 records, docs/views/evidence/desk-d90.jsonl)
- Astilboides tabularis, sense_light_nonvisual (86.3% at 30 C in light; partial true, dark values only in a figure) and sense_chemical (GA3 to 97.0% at 200 and 500 mg/L; kinetin, KNO3, KCl no effect). Cho, Jeong, Lee 2016, Korean J. Hortic. Sci. Technol. 34(3): 363-371, 10.12972/kjhst.20160037. POWO, WFO, GBIF 3754647 accepted.
- Catolobus pendulus (paper: Arabis pendula), sense_chemical: GA3 24 h soak 27.4% to 97.3% at 500 mg/L. Shin et al., Korean J. Plant Res. 30(1): 50-57, 10.7732/kjpr.2016.30.1.050. WFO page confirms Arabis pendula as synonym; POWO and GBIF 3688630 accept Catolobus pendulus.
- Hydrangea petiolaris, sense_light_nonvisual (25 C: 78.0% light, 52.0% dark) and sense_chemical (GA3 78.0% to 98.5% at 500 mg/L; kinetin lowered germination). Cho et al., Korean J. Plant Res. 27(5): 534-539, 10.7732/kjpr.2014.27.5.534. POWO and GBIF 3645181 accepted.
- Kadsura coccinea, sense_chemical: GA3 73.3% to 96.7% at 250 mg/L, down to 80.6% at 1,000. Je et al., J. Environ. Sci. Int. 32(1): 77-88, 10.5322/JESI.2023.32.1.77. POWO and GBIF 7335142 accepted.

## Wanted lines
None.

## Held out (leads)
- Astilbe koreana (Jang, Cho, Lee, Korean J. Plant Res. 29(2): 235-240, 2016, 10.7732/kjpr.2016.29.2.235; koreascience JAKO201614859324514): light-only germination (none in dark at 15-30 C, 40.8% at 15 C) and KNO3 raised germination to 77.8-78.0% (20-40 mM; KCl lowered it; GA3 to 68.3% at 500 mg/L). Held out on name: GBIF 3754990 treats it as a synonym of Astilbe grandis, POWO's page for Astilbe chinensis var. koreana points to "Astilbe koreana" as accepted, and no POWO page for the species itself would open. Quotable whole sentences: "In addition, the seed was not germinated at dark condition regardless of temperature." and "As a results, KNO3 treatment, regardless of concentrations, promoted germination compared to control."
- Aster scaber (Park SK, Korean J. Plant Res. 7(1): 73-76, 1994, no DOI): "The germination rate was higher with light condition than dark and Gibberellin treatment waseffective." Held out on name: GBIF lists Aster scaber Moench, and the species is moved between Aster and Doellingeria; POWO would not open.
- Tiarella polyphylla (Choi et al. 2018, 10.7732/kjpr.2018.31.4.363): already on main (desk-d47).
- Trollius macropetalus (Kim et al., Korean J. Plant Res. 37(1): 79-86, 2024, 10.7732/kjpr.2024.37.1.079): GA3 sentences longer than 125 characters.
- Pseudolysimachion kiusianum var. diamantiacum (10.7732/kjpr.2023.36.4.381): a variety, every result sentence over 125 characters.
- Heloniopsis koreana and H. tubiflora (10.7235/hort.2014.14025): two species pooled. Three Campanulaceae (Kang et al. 1997) pooled. Taraxacum ohwianum (10.7783/KJMCS.2016.24.3.177) and Spiraea fritschiana (10.12972/kjhst.20160057): result sentences over 125 characters. Allium koreanum (hydrogen peroxide, not a listed trigger). Centella asiatica flower phenology (Thai-language abstract, stigma receptivity 05:37-06:28, no DOI).
- Capsicum and Nicotiana (Kang 1998, 1999) are crops, left out.

## Advice
Korean Journal of Plant Resources, Korean Journal of Horticultural Science & Technology and Journal of Environmental Science International print whole short abstract sentences and open PDFs on koreascience.kr; the first-page PDF fetch gives journal, volume and pages. Roughly one in four Korean native-plant germination papers has a sentence set that fits the 125-character rule.

## Desk disposition after audit 180
Audit 180: 4 of 6 errors, all dropped (whole unit covered): line 1 Astilboides tabularis light (full text open but filed partial; omitted that days to germination were shorter in light at every temperature, 11 days in light against 19 in darkness at 30 C), line 2 Astilboides tabularis GA3/kinetin/KNO3/KCl (copied the abstract's "no effect" while the body shows KNO3 raised germination energy by at least 30% and shortened time to 50% germination; GA3 speed figures missing), line 3 Catolobus pendulus GA3 (uniformity direction reversed: it is a variance, 500 mg/L was most uniform and 1,000 mg/L no better than control), line 5 Hydrangea petiolaris GA3/kinetin (omitted kinetin's lower germination energy and longer time to 50%, KNO3's significant reductions, and KCl at 200 mM lowering germination to 59.5%). Refile only with those results carried. Hydrangea petiolaris light and Kadsura coccinea GA3 merged; the Kadsura root-growth clause was reworded to the audit's reading.
