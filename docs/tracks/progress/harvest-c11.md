# harvest-c11 progress

## 2026-10-27 — round 28

This worker and cumulative batch: **6 genera protocol-screened** (Ulmus, Malvaviscus, Carya, Pyrus, Zizia, Ptelea), **9 search records**, **38 wanted leads**, **0 evidence records**, **0 cells measured closed**. Remaining **34 genera**, next **Iris**; then Ricinus, Conopholis, Tropaeolum, Chasmanthium, Paulownia, Chenopodium, Aquilegia, Helianthus, Arundo, Sorghum, Dioscorea, Vinca, Lobelia, Foeniculum, Hypochaeris, Sorghastrum, Packera, Cortaderia, Nasturtium, Tecoma, Cosmos, Achillea, Mahonia, Apocynum, Bromus, Marchantia, Vachellia, Poa, Parkinsonia, Panicum, Artemisia, Polystichum, Ailanthus. Screening is complete for these six even where plausible measurements remain wanted; no wanted trait is called exhausted. Search dispositions are Ulmus diel/eye_type, Malvaviscus eye_type, Carya eye_type; Pyrus eye_type; Zizia diel/eye_type/sense_chemical; Ptelea eye_type.

Read AGENTS.md, the round28 guide, round4-harvest, THOROUGH, BRIEF including Round 2, round3-sweep, desk-screen points 1–10 including plant10(e), and audit 53/54 findings. No app startup, build, server, test or global-state modification. Main's existing sweep-13 Ulmus light/chemical records and old sweep-13/sweep-16 search records remain untouched. Global wanted/status lookup found no duplicates for the new leads. Canon catalog checked: no in-hand plant compilation covering these genera; relevant trait canon DOIs are retained in search records, without pretending source text was read. Owner eye_type decision followed; epidermal focusing is a nonvisual-light topic.

### Sources, queries and boundaries

harvest_get.py and screen_candidates.py explicitly report Ulmus, Malvaviscus and Carya absent from runs 1–17,20,23,24. Thus no harvest queries or candidates were silently omitted. Ulmus direct OpenAlex requests returned all nine queries at per-page=20 (or all results when fewer); titles and the available abstracts were screened. On the first Malvaviscus query, OpenAlex returned **HTTP429**. No later OpenAlex API request was made. Per the source-refusal rule, the complete scientific/common-name pairs and family searches for Malvaviscus and Carya were executed with connected web search; they are recorded as `web:` queries only. The failed API query is not called executed in a search record. Parent was informed of the refusal and continuation through usable web search.

**71 successful connected web queries**: Ulmus11, Malvaviscus12, Carya12, Pyrus12, Zizia12, Ptelea12. One initial call with an unsupported argument returned an empty tool error and is not counted as successful. No quota refusal from connected web. Search tool returns variable numbers of results; all returned titles/snippets were screened, never claiming twenty where fewer returned. Raw tool responses and direct OpenAlex metadata are scratch files under work/harvest-c11, not committed. No primary-source page fetched or paper text/evidence committed, per desk-screen point3.

Ulmus: scientific/common searches found seasonal flowering dates, not a daily opening hour. Biological Flora Ulmus glabra (10.1111/1365-2745.12994) and USDA American/Cedar Elm snippets were screened out for diel because their dates are seasonal. Existing sweep-13 already holds Ulmus pumila light and Ulmus minor chemical evidence, so neither gets a null. New wanted leads include three living-tissue hormone responses, five seed-germination studies, the GA3 red-elm report and photoperiodic American-elm growth. They are leads pending source reading, not new evidence. Ulmaceae review query returned five titles, including 10.1111/jbi.70113 and 10.3390/urbansci9010014: seasonal tree phenology, not a direct Ulmus within-day anthesis measurement. Other returned titles concerned introgression, Cannabis and natural-products chemistry.

Malvaviscus: hummingbird-pollination and petal-colour papers are retained for anthesis/diel reading rather than treating their flowering as a null. Deno's germination entry is a light lead, with the original conditions still to verify. The headspace paper is held conservatively: source reader must verify living attached material or signaling, since picked-tissue chemistry alone fails 10(a). General ocelli/focusing papers do not name Malvaviscus in returned text and cannot change plant eye_type. Malvaceae review query returned general structural reviews including 10.1146/annurev-arplant-042809-112259 and 10.1111/tpj.70817, no Malvaviscus measurement in returned text.

Carya: direct seed light/dark comparison, GA3 germination, intact-shoot/nutlet emission and living damaged-plant headspace studies remain wanted. Two flowering-development studies remain candidate diel leads rather than false nulls; reader must separate daily hours from season and dichogamy. Nut roasting, storage oxidation and electronic-nose food-quality studies are tissue chemistry, not living plant chemical response; no wanted request from those. Juglandaceae review query returned general plant/fungal photoreceptor and animal reviews plus a genomic portal, not Carya eye measurements. Carya cathayensis flowering transcriptome (PMID24106755) predicts pathways from gene expression rather than testing photoperiod treatments; the genuine light/dark germination lead already holds the light trait out of searched.

### Exact queries

Ulmus:

- Ulmus flower opening time anthesis
- elm flower opening time anthesis
- Ulmus epidermal lens cells eye
- elm epidermal lens cells eye
- Ulmus chemical sensing volatiles
- elm chemical sensing volatiles
- Ulmus photoperiod phototropism light response
- elm photoperiod phototropism light response
- Ulmaceae photoreceptor review
- web: Ulmus seed germination light dark
- web: Ulmus germination gibberellin OR smoke OR dormancy
- web: Ulmus jasmonate herbivore
- web: Ulmus flower opening time anthesis
- web: elm flower opening time anthesis
- web: Ulmus plant ocelli lens epidermal focusing eye
- web: elm plant ocelli lens epidermal focusing eye
- web: Ulmus chemical sensing volatiles
- web: elm chemical sensing volatiles
- web: Ulmus photoperiod phototropism light response
- web: elm photoperiod phototropism light response

Malvaviscus:

- web: Malvaviscus seed germination light dark
- web: Malvaviscus germination gibberellin OR smoke OR dormancy
- web: Malvaviscus floral scent volatiles
- web: Malvaviscus flower opening time anthesis
- web: Turk's cap flower opening time anthesis
- web: Malvaviscus plant ocelli lens epidermal focusing eye
- web: Turk's cap plant ocelli lens epidermal focusing eye
- web: Malvaviscus chemical sensing volatiles
- web: Turk's cap chemical sensing volatiles
- web: Malvaviscus photoperiod phototropism light response
- web: Turk's cap photoperiod phototropism light response
- web: Malvaceae photoreceptor review

Carya:

- web: Carya seed germination light dark
- web: Carya germination gibberellin OR smoke OR dormancy
- web: Carya jasmonate herbivore
- web: Carya flower opening time anthesis
- web: hickory flower opening time anthesis
- web: Carya plant ocelli lens epidermal focusing eye
- web: hickory plant ocelli lens epidermal focusing eye
- web: Carya chemical sensing volatiles
- web: hickory chemical sensing volatiles
- web: Carya photoperiod phototropism light response
- web: hickory photoperiod phototropism light response
- web: Juglandaceae photoreceptor review

### Wanted source provenance

1. Plant Regeneration from Cell Suspension Culture of Ulmus americana L. — https://journals.ashs.org/downloadpdf/journals/hortsci/32/3/article-p461E.pdf; query `OA: Ulmus chemical sensing volatiles`. Abstract reports TDZ/NAA/benzylaminopurine/IBA responses in living regenerating tissue; hormone responses qualify under 10(d). Lead screened from OpenAlex title/abstract on 2026-10-27; source not fetched/read; no evidence logged.

2. β-Aminobutyric acid promotes stress tolerance, physiological adjustments, as well as broad epigenetic changes at DNA and RNA nucleobases in field elms (Ulmus minor) — https://link.springer.com/content/pdf/10.1186/s12870-024-05425-6.pdf; query `OA: Ulmus chemical sensing volatiles`. Applied BABA changes development and stress tolerance in living elms, an elicitor response under 10(d). Lead screened from OpenAlex title/abstract on 2026-10-27; source not fetched/read; no evidence logged.

3. Plant Regeneration from Hypocotyl of `King's Choice' Elm — https://journals.ashs.org/downloadpdf/journals/hortsci/32/3/article-p461F.pdf; query `OA: elm chemical sensing volatiles`. Abstract reports dose-dependent TDZ/NAA shoot regeneration, GA elongation and IBA rooting in Chinese elm; verify accepted species identity of cultivar. Lead screened from OpenAlex title/abstract on 2026-10-27; source not fetched/read; no evidence logged.

4. Seed germination of three Ulmus species from Turkey as influenced by temperature and light — https://www.jeb.co.in/journal_issues/200704_apr07_supp/paper_12.pdf; query `web: Ulmus seed germination light dark`. Snippet compares total darkness with an 8-hour photoperiod and reports light-dependent germination. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

5. Effect of different treatments and light quality on Ulmus pumila L. germination and seedling growth — https://www.tandfonline.com/doi/full/10.1080/21580103.2021.1968960; query `web: Ulmus seed germination light dark`. Snippet describes BA/IBA/GA3 and dark/fluorescent/red-blue LED treatments of living seeds. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

6. Ecological factors related to seed germination and early seedling establishment in Ulmus minor Mill., an endangered riparian tree species — https://academic.oup.com/forestry/article/96/5/775/7131118; query `web: Ulmus seed germination light dark`. Snippet explicitly describes factorial full-sun/shade germination and seedling treatments. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

7. Effects of Temperature, Light and Storage on Seed Germination of Ulmus glabra Huds. and U. laevis Pall — https://scialert.net/fulltext/?doi=pjbs.2006.697.699; query `web: Ulmus seed germination light dark`. Title and snippet compare light and darkness during seed germination; Publisher URL identifies the work; full DOI not independently shown. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

8. Differentiation of seed germination traits in relation to the natural habitats of three Ulmus species in Japan — https://www.tandfonline.com/doi/abs/10.1007/s10310-009-0165-1; query `web: Ulmus seed germination light dark`. Snippet describes 16h dark/8h light versus 24h darkness germination tests; verify species list. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

9. Improving Germination of Red Elm (Ulmus rubra) Seeds With Gibberellic Acid — https://www.pubhort.org/ipps/60/107.htm; query `web: Ulmus germination gibberellin OR smoke OR dormancy`. Snippet reports a germination response to GA3 after 90-day stratification. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

10. Effects of Photoperiod on Growth of Trees — https://www.journals.uchicago.edu/doi/abs/10.1086/335918; query `web: elm photoperiod phototropism light response`. Snippet reports American elm growth cessation after 20 weeks of eight-hour days. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

11. Hummingbird pollination of Malvaviscus arboreus in Costa Rica — https://www.tandfonline.com/doi/pdf/10.1080/0028825X.1984.10425293; query `web: Malvaviscus flower opening time anthesis`. Result shows a flower form and anthesis section; a plausible within-day flowering candidate needing reading. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

12. Colour change of petals in Malvaviscus arboreus flowers — https://natuurtijdschriften.nl/pub/539777/ABN1971020004001.pdf; query `web: Malvaviscus flower opening time anthesis`. Result describes successive anthesis stages and nectar production; read for timing rather than infer a daily hour from colour. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

13. Headspace Volatiles of the Leaves and Flowers of Malvaviscus arboreus Cav. (Malvaceae) — https://www.scielo.org.mx/scielo.php?pid=S1870-249X2021000100141&script=sci_arttext; query `web: Malvaviscus floral scent volatiles`. Headspace floral/leaf emission candidate. Reader must establish living attached material or a signaling assay; extracted/harvested tissue chemistry alone does not qualify under 10(a). Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

14. Seed Germination Theory and Practice, 1st Supplement — https://denosgarden.com/s/malvaviscus-arboreus/; query `web: Malvaviscus seed germination light dark`. Genus germination search returns an indexed Deno entry labeled light; verify original experimental Malvaviscus entry and actual light/dark conditions before logging. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

15. Luminosity and temperature on pecan seed germination — https://revistapag.agricultura.rs.gov.br/ojs/index.php/revistapag/article/view/697; query `web: Carya seed germination light dark`. Snippet compares light with darkness; absence of light at 25C produced more normal seedlings. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

16. Regulation of Germination of Pecan, Carya illinoensis — https://www.sciencedirect.com/science/article/pii/S0044328X76801419; query `web: Carya seed germination light dark`. Germination title qualifies as a lead under 10(e); snippet describes shell restriction, so reader must verify actual light or chemical treatments. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

17. Gibberellic acid increases premature germination in pecan (Carya illinoinensis Koch.) — https://revistascientificas.uach.mx/index.php/tecnociencia/en/article/view/693; query `web: Carya germination gibberellin OR smoke OR dormancy`. Title reports GA-induced germination; living hormone response qualifies under 10(d). Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

18. Volatiles emitted by Carya illinoinensis (Wang.) K. Koch as a prelude for semiochemical investigations to focus on Acrobasis nuxvorella Nuenzig (Lepidoptera: Pyralidae) — https://scijournals.onlinelibrary.wiley.com/doi/abs/10.1002/ps.2205; query `web: Carya chemical sensing volatiles`. Snippet describes headspace sampling of intact new shoots and nutlets, a plausible living signal-emission measurement. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

19. 云斑天牛对不同受害状态下山核桃挥发物成分的触角电位和行为反应 — https://zlxb.zafu.edu.cn/cn/article/doi/10.11833/j.issn.2095-0756.2019.03.002; query `web: hickory chemical sensing volatiles`. Chinese snippet explicitly describes dynamic headspace bag sampling on living plants in healthy, feeding-damaged, oviposition and boring treatments; qualify under 10(a). Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

20. Flowering characteristics and pollen viability of Carya illinoensis 'Mahan' — https://zlxb.zafu.edu.cn/en/article/doi/10.11833/j.issn.2095-0756.2014.04.006; query `web: Carya flower opening time anthesis`. Flower-development stage candidate from anthesis search; read for daily pollen or anthesis timing rather than infer it from seasonal development. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

21. 薄壳山核桃在南京的开花物候期观察和比较 — https://zwzy.jib.ac.cn/Contribution/PeriodicalDirectoryDetails_6579b959-a72f-4886-84fe-9b212ec27ff3.html; query `web: Carya flower opening time anthesis`. Snippet describes single-flower blossom progression and pollen shedding in eighteen cultivars; candidate for daily timing needing full text. Lead screened from connected web title/snippet on 2026-10-27; source not fetched/read; no evidence logged.

### Validation and next step

First two-genera gate: `screen_candidates.py --check` printed **0 problems**. Three-genera gate: **0 problems** before commit. Resume at Iris in exact batch order. OpenAlex remains skipped after 429; use cached harvest where present and connected web for scientific/common/family protocol. No uncompleted protocol is counted done.

### Pyrus and Zizia continuation, 2026-10-27

This continuation adds 2 screened genera,4 search records and13 wanted lines (12 Pyrus; one new Deno second-edition book for Zizia, while the existing first-supplement line is extended to Zizia aptera instead of duplicated). Pyrus eye_type is the only new null for that genus; main already has pear photoperiod evidence and new light/chemical/diel candidates remain wanted. Particularly useful leads are the2014 Japanese-pear red/far-red photoperiod trial (PMID24876291; OUP tpu033 PDF) and2023 photoperiod/diurnal-transcriptome study (10.1111/ppl.13893). They refine the existing dormancy-specific finding; no blanket claim of pear light insensitivity is made. Nut/fruit storage and aroma-profile chemistry was screened out under10(a). Pyrus lens-shaped stomata (PMC3845256) are anatomy, not a visual organ. Rosaceae review queries returned general photoreceptor reviews plus10.1002/fsn3.72269 on Rosaceae pigment regulation, with no Pyrus eye measurement in returned text.

Zizia light held for original Deno germination entries indexed on denosgarden.com; original conditions remain to verify. Diel, eye_type and chemical null dispositions follow full name pairs, germination/GA/scent searches and Apiaceae review. Results naming Ziziphus, Zizyphus, Ziziphora, Zizania or Vetiveria zizanioides concern other genera. Zizia horticultural pages report flowering seasons, not daily hours, and cold/moist stratification with endogenous chemistry, not an applied hormone or airborne signal. Review10.1093/hr/uhac076 returned no Zizia measurement in its available abstract/excerpts; unread tables are not claimed searched in full. Neither genus was in cached harvest; no harvest query was omitted. Pyrus and Zizia checks each printed0 problems.

Exact Pyrus queries:

- web: Pyrus seed germination light dark
- web: Pyrus germination gibberellin OR smoke OR dormancy
- web: Pyrus floral scent volatiles
- web: Pyrus flower opening time anthesis
- web: pear flower opening time anthesis
- web: Pyrus plant ocelli lens epidermal focusing eye
- web: pear plant ocelli lens epidermal focusing eye
- web: Pyrus chemical sensing volatiles
- web: pear chemical sensing volatiles
- web: Pyrus photoperiod phototropism light response
- web: pear photoperiod phototropism light response
- web: Rosaceae photoreceptor review

Exact Zizia queries:

- web: Zizia seed germination light dark
- web: Zizia germination gibberellin OR smoke OR dormancy
- web: Zizia floral scent volatiles
- web: Zizia flower opening time anthesis
- web: golden alexanders flower opening time anthesis
- web: Zizia plant ocelli lens epidermal focusing eye
- web: golden alexanders plant ocelli lens epidermal focusing eye
- web: Zizia chemical sensing volatiles
- web: golden alexanders chemical sensing volatiles
- web: Zizia photoperiod phototropism light response
- web: golden alexanders photoperiod phototropism light response
- web: Apiaceae photoreceptor review

Continuation wanted provenance:

22. Ascorbic acid releases dormancy and promotes germination by an integrated regulation of abscisic acid and gibberellin in Pyrus betulifolia seeds — https://onlinelibrary.wiley.com/doi/10.1111/ppl.14271; query `web: Pyrus germination gibberellin OR smoke OR dormancy`. Snippet states germination tests after exogenous AsA and lycorine, qualifying living chemical responses. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

23. Seed coat-derived ABA regulates seed dormancy of Pyrus betulaefolia by modulating ABA and GA balance — https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1667946/full; query `web: Pyrus germination gibberellin OR smoke OR dormancy`. Snippet reports exogenous ABA and fluridone germination assays. A fixed 16/8h culture photoperiod alone is not a light-treatment measurement. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

24. Endemik Pyrus serikensis (Rosaceae) türünün tohum çimlenmesi üzerine araştırmalar — https://dergipark.org.tr/en/pub/akdenizfderg/article/267393; query `web: Pyrus seed germination light dark`. Snippet reports an 18h light/6h darkness germination treatment as the best combination; verify comparison against darkness and species name. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

25. Seed germination response of Indian wild pear (Pyrus pashia) to gibberellic acid treatment and cold storage — https://notulaebiologicae.ro/index.php/nsb/article/view/11044; query `web: Pyrus germination gibberellin OR smoke OR dormancy`. Title explicitly reports seed germination under applied GA, a living hormone-response lead. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

26. Flowers of European pear release common and uncommon volatiles that can be detected by honey bee pollinators — https://link.springer.com/article/10.1007/s00049-019-00289-x; query `web: Pyrus floral scent volatiles`. Snippet reports floral emission rates and pollinator antennal activity. Verify living-flower collection rather than harvested-tissue chemistry. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

27. Volatile Emission of Pear Tree (Pyrus communis) and Olfactory Perception of Pear Psyllids (Cacopsylla pyri and C. pyrisuga) are Affected by Elevated Tropospheric Ozone Concentration — https://link.springer.com/article/10.1007/s10886-025-01642-x; query `web: Pyrus chemical sensing volatiles`. Tree volatile emissions under ozone exposure plausibly measure a living chemical response and emitted signals. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

28. Dual biotic stressors shape volatile organic compound emission patterns in pome fruit trees — https://pubmed.ncbi.nlm.nih.gov/42424400/; query `web: Pyrus chemical sensing volatiles`. Snippet names pear trees, herbivore-induced emissions and pear-decline pathogen effects. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

29. Diurnal transcriptome dynamics reveal the photoperiod response of Pyrus — https://onlinelibrary.wiley.com/doi/10.1111/ppl.13893; query `web: Pyrus photoperiod phototropism light response`. Snippet reports plants grown under long and short days and samples every4h for2days. Verify measured species and distinguish rhythmic gene expression from flower-opening behaviour. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

30. Effect of extending the photoperiod with low-intensity red or far-red light on the timing of shoot elongation and flower-bud formation of 1-year-old Japanese pear (Pyrus pyrifolia) — https://academic.oup.com/treephys/article-pdf/34/5/534/17432724/tpu033.pdf; query `web: Pyrus photoperiod phototropism light response`. Snippet explicitly reports flowering regulation by red:far-red ratio. This concerns flower induction rather than daily anthesis and does not contradict the older dormant-growth experiment. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

31. Genome-wide analysis of the CCT gene family in Chinese white pear (Pyrus bretschneideri Rehd.) and characterization of PbPRR2 in response to varying light signals — https://link.springer.com/article/10.1186/s12870-022-03476-1; query `web: Pyrus photoperiod phototropism light response`. Snippet reports gene-expression responses under enhanced red illumination; verify plants and light-treatment comparison in methods. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

32. Monochromic Radiations Provided by Light Emitted Diode (LED) Modulate Infection and Defense Response to Fire Blight in Pear Trees — https://pmc.ncbi.nlm.nih.gov/articles/PMC8465259/; query `web: Pyrus photoperiod phototropism light response`. Title and snippet describe monochromatic light treatments and plantlet defense-expression rhythms; reader must establish the named pear species. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

33. Pollen Compatibility Studies of Some Commercially Important Pear Varieties (Pyrus communis L.) — https://krishikosh.egranth.ac.in/server/api/core/bitstreams/94731ab3-d396-4c3a-b715-b5f55ae69e20/content; query `web: Pyrus flower opening time anthesis`. Returned thesis section is Flower anthesis and anther dehiscence, a candidate source for daily timing. No time is inferred from generic flowering stages. Connected web title/snippet lead, 2026-10-27; source not fetched/read, no evidence logged.

34. Seed Germination Theory and Practice, 2nd ed. — https://denosgarden.com/s/zizia-aurea/; query `web: Zizia seed germination light dark`. Indexed Zizia aurea germination entry gives a darkness regime; verify original experiment and whether it compares light/dark. Genus germination lead under10(e); original source not fetched/read, no evidence logged.


### Ptelea continuation, 2026-10-27

Adds 1 screened genus, 1 null search disposition and4 wanted studies; existing Deno second-edition wanted line extended to Ptelea species instead of duplicated. Total this worker/cumulative 6 genera, 9 search records, 38 wanted lines,0 evidence,0 measured cells. Stops between genera for fresh-context takeover;34 remain from Iris in batch order. No uncompleted genus counted. OpenAlex remains skipped after 429; connected web had no refusal.

Ptelea cached harvest run6 and supplements14/20 were reviewed once its asynchronous tool completed. Scientific/common-name trait pairs, plant10(e) and Rutaceae review were screened. Anthesis results provide seasons, not within-day timing. General ocelli/focusing results do not name Ptelea; any focusing belongs to sense_light_nonvisual. Floral Aromatics of Ptelea (10.21273/JASHS05119-21,2022) is a chemical lead, with attached/living collection still to verify; essential-oil leaf/flower distillation alone was screened out. Deno's original germination entry explicitly names P. isophylla and P. trifoliata; reader must verify actual light or chemical treatment rather than infer a response from a fixed temperature. Other GA/smoke studies returned in the genus search concern Pimelea, not Ptelea. Rutaceae review search returned general photoreceptor reviews10.1002/wmts.36 and10.1387/ijdb.051989kf plus Kew and Watson/Dallwitz family morphology; no Ptelea daily-hour or eye measurement in returned text. First six-genus gate failed1 on an unaddressed human eye review (10.3390/life13010077); screened as human disease, then rerun required. The late Ptelea harvest also corrected the preliminary absence statement before commit; every successful cached query is now present. Diel null was removed because the reproductive-biology work is a plausible lead and is now wanted.

Exact Ptelea queries:

- web: Ptelea seed germination light dark
- web: Ptelea germination gibberellin OR smoke OR dormancy
- web: Ptelea floral scent volatiles
- web: Ptelea flower opening time anthesis
- web: hoptree flower opening time anthesis
- web: Ptelea plant ocelli lens epidermal focusing eye
- web: hoptree plant ocelli lens epidermal focusing eye
- web: Ptelea chemical sensing volatiles
- web: hoptree chemical sensing volatiles
- web: Ptelea photoperiod phototropism light response
- web: hoptree photoperiod phototropism light response
- web: Rutaceae photoreceptor review

Wanted35. Floral Aromatics of Ptelea: Chemical Identification and Human Response — https://journals.ashs.org/downloadpdf/view/journals/jashs/147/1/article-p25.pdf; query `web: Ptelea floral scent volatiles`. Returned abstract describes volatiles emitted by flowers of P. trifoliata and P. crenulata and human fragrance response. Verify living attached flower collection under10(a); essential-oil distillation alone would not qualify. Connected web lead on2026-10-27; source not fetched/read, no evidence logged.

Deno wanted lines34 and14 were extended, respectively, with Ptelea and Zizia aptera provenance; source URLs and exact queries remain in their JSON why/queries. Raw search responses: work/harvest-c11/{Ulmus,Malvaviscus,Carya,Pyrus,Zizia,Ptelea}-web*.json and family JSON; Ulmus OA metadata in Ulmus-oa.json. Scratch metadata is not committed. No source full text was saved in tracked files.

### Ptelea late harvest reconciliation

The first five genera were absent from harvest; Ptelea is present in run6/supp14/20. Its asynchronous tools had not finished when the provisional note was prepared, and no commit of that claim was made. Final Ptelea record copies every successful cached query, including zero-hit queries, before web queries. Citation step on10.1016/j.plantsci.2024.112264 returned zero. All102 displayed result occurrences and family-review titles plus stored abstract starts screened; among them, three additional plausible sources were retained, bringing batch wanted count38. No direct light/chemical/diel null was written for Ptelea.

Cached query list:

- Ptelea phytochrome photoreceptor
- Ptelea light perception
- Ptelea phototropism
- Ptelea flower opening time
- Ptelea nyctinasty
- Ptelea anthesis
- Ptelea pollination biology
- Ptelea volatile signalling
- Ptelea photoperiod
- Ptelea circadian rhythm
- Ptelea epidermal lens cells
- Ptelea epidermal focusing leaf optics
- Rutaceae photoreceptor review

Additional wanted provenance:

36. Cold Stratification and Pericarp Removal Improve Seed Germination of Ptelea trifoliata and Ptelea crenulata — https://journals.ashs.org/downloadpdf/journals/hortsci/55/4/article-p503.pdf; cached query `Ptelea pollination biology`. Genus germination title is a mandatory10(e) lead; abstract specifically tests cold stratification/pericarp, so original methods must establish any light comparison. Cached harvest title/abstract lead screened2026-10-27; source not fetched/read, no evidence logged.

37. CONSERVATION OF THE DIVERSITY OF BOTANICAL GARDEN COLLECTION WITH THE USE OF IN VITRO TECHNIQUES WITH EXAMPLE OF PTELEA TRIFOLIATA L. (RUTACEAE JUSS.) — https://journal.kdpu.edu.ua/ecolog/article/download/8343/7909; cached query `Ptelea photoperiod`. Stored abstract compares propagation media in living cultured tissue; reader should establish which hormones/nutrient formulations and measured response qualify under10(d). Cached harvest title/abstract lead screened2026-10-27; source not fetched/read, no evidence logged.

38. Hop tree (Ptelea trifoliata) in Canada: population and reproductive biology of a rare species — https://doi.org/10.1139/b85-272; cached query `Ptelea pollination biology`. Population/reproductive biology includes direct floral observations and insect visitation; plausible source for daily floral timing, which truncated abstract does not settle. Cached harvest title/abstract lead screened2026-10-27; source not fetched/read, no evidence logged.

Other cached Ptelea dispositions: spectral flower characteristics10.26565/2075-5457-2026-46-8 are physical flower optics, not an eye. The nursery catalogs contain shade recommendations, not a measured living light response. Phototoxicity10.3390/life14081019 and medical review10.3390/life13010077 concern effects on humans. The Papilio volatile paper10.1007/s10886-023-01433-2 measures butterfly antennae, not a Ptelea plant response; the other chemical candidate palynology10.1603/ice.2016.113858 reports beetle pollen-feeding, not plant chemoreception. Reviews on elicitors/oil yield are retained as background, without mistaking generic plants for genus-specific evidence. The positive culture/germination/floral candidates keep those traits out of null records.

Final six-genus gate after Ptelea harvest reconciliation: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c11.jsonl --wanted docs/views/wanted/harvest-c11.jsonl` printed **0 problems**. All 38 wanted lines were checked against other wanted units and papers-status with no DOI/title duplicate or owner status match. Previous committed chunk: a2a9c42f. Final chunk stops cleanly before Iris for fresh-context takeover.
