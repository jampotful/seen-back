# harvest-c11 progress

## 2026-10-27 — round 28

Prior worker chunk: **6 genera protocol-screened** (Ulmus, Malvaviscus, Carya, Pyrus, Zizia, Ptelea), **9 search records**, **38 wanted leads**, **0 evidence records**, **0 cells measured closed**. Remaining **34 genera**, next **Iris**; then Ricinus, Conopholis, Tropaeolum, Chasmanthium, Paulownia, Chenopodium, Aquilegia, Helianthus, Arundo, Sorghum, Dioscorea, Vinca, Lobelia, Foeniculum, Hypochaeris, Sorghastrum, Packera, Cortaderia, Nasturtium, Tecoma, Cosmos, Achillea, Mahonia, Apocynum, Bromus, Marchantia, Vachellia, Poa, Parkinsonia, Panicum, Artemisia, Polystichum, Ailanthus. Screening is complete for these six even where plausible measurements remain wanted; no wanted trait is called exhausted. Search dispositions are Ulmus diel/eye_type, Malvaviscus eye_type, Carya eye_type; Pyrus eye_type; Zizia diel/eye_type/sense_chemical; Ptelea eye_type.

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

## 2026-10-27 — worker17 continuation

Worker17: **1 genus protocol-screened (Iris plant only), 1 search record, 14 wanted lines,0 evidence,0 measured cells closed**. Cumulative batch: **7 genera,10 search records,52 wanted lines,0 evidence**; **33 remain**, next Ricinus then the original batch order. Prior six genera remain complete; no incomplete genus counted.

Iris harvest_get.py and screen_candidates.py finished and both explicitly report no harvest. Original queue plant gaps are eye_type, sense_chemical and sense_light_nonvisual for Iris pseudacorus and I. versicolor; diel already has sweep-8 measured evidence corrected in recheck-5-fixed. Global mixed sweep-8 record is thin and does not suppress those three plant protocols; rescreen-2 mantis Iris oratoria records remain untouched. Canon catalog checked, no in-hand plant compilation supplies Iris light/chemical measurements; animal eye canon named in null per point8. Global wanted/evidence/searched and owner papers-status checked, no matching candidate title/status found; rapid-opening Iris2015 wanted already in sweep-8 and not duplicated.

OpenAlex remains skipped following round-wide429; no API query represented as executed. No MDPI/UChicago/SANBI direct fetch, no other primary-source or paper fetch, no evidence.10 successful connected web queries, plus1 unsupported-argument empty error (not successful and not a quota refusal). All returned titles/snippets screened, variable counts without claiming20 where fewer; raw tool results work/harvest-c11/Iris-web{1,2,3}.json.

Exact successful queries:
- `web: Iris seed germination light dark`
- `web: Iris germination gibberellin OR smoke OR dormancy`
- `web: Iris floral scent volatiles`
- `web: Iris plant ocelli lens epidermal focusing eye`
- `web: yellow flag iris plant ocelli lens epidermal focusing eye`
- `web: Iris chemical sensing volatiles`
- `web: yellow flag iris chemical sensing volatiles`
- `web: Iris photoperiod phototropism light response`
- `web: yellow flag iris photoperiod phototropism light response`
- `web: Iridaceae photoreceptor review`

Family query returned general photopigment/photoreceptor reviews10.1002/wmts.36 and10.1007/s10265-016-0785-4, insect colour review10.1146/annurev-ento-061720-071644 and Iris cultivation review PMC12473546. The latter is a retained review lead with germination references; general plant/animal reviews do not name an Iris plant eye. Eye pair mainly yielded human eye anatomy and bumblebee ocelli (iris as an anatomical term), plus plant-ocelli review10.3390/plants12010061; focusing belongs to light under10(b), not plant eye_type.

Added14 genuine leads below, no source read or measurements asserted. Light/dark Iris pseudacorus experiment and multiple-photoperiod Iris domestica/dichotoma experiment prevent light exhaustion. Germination/dormancy titles retained per10(e), including Iris tenax, I. scariosa, six-species in-vitro work,1966 seed review and winter-dormancy study. Auxin/GA culture response qualifies as a plausible10(d) lead; endogenous-hormone correlations alone need actual treatment verification. Four headspace/floral-scent studies retained conservatively for living attached collection/signaling; two ScienceDirect versions of the20-species study folded into one lead. Dried rhizome chemistry PMC11397506 is harvested tissue under10(a); perfume marketing, anatomical human iris, gas-sensor IRIS repositories and Dietes bicolor are not Iris-plant measurements. PMID23218543 flower-opening hormone work has cut-flower risk with attached/living status unestablished in snippet, so retained as a boundary wanted lead; no positive measurement claimed.

Wanted provenance (exact retrieval URLs and query stored in JSON lines):
- Germination niche breadth of invasive Iris pseudacorus (L.) suggests continued recruitment from seeds with global warming: https://pmc.ncbi.nlm.nih.gov/articles/PMC9544747/. Three light treatments compare light, total darkness and darkness with green-light inspection.
- Factors Influencing Germination of a Functionally Important Grassland Plant, Iris tenax: https://pmc.ncbi.nlm.nih.gov/articles/PMC3938591/. Genus germination title is a mandatory plant10(e) lead; verify which light or chemical comparisons accompany the stratification studies.
- The Study on Seed Dormancy and Germination Characteristics of Iris scariosa: https://manu40.magtech.com.cn/Jweb_cdxb/EN/abstract/abstract2470.shtml. Snippet names gibberellin application, inhibitor determination and stratification; verify species and any light comparison.
- METHODS FOR OVERCOMING SEED DORMANCY AND FEATURES OF IRIS CULTIVATION IN IN VITRO CONDITIONS: https://agris.fao.org/search/en/records/6759aecd0ce2cede71ca7df8. Snippet describes auxin and GA3 culture supplements in living explants; germination title also needs light-treatment review. Species list comes from the matching CyberLeninka search snippet, not a fetched page.
- A Review of Factors in Iris Seed Germination: https://wiki.irises.org/pub/Hist/Info1966AISBulletinNo181April/AIS%20Bulletin%201966%20Apr.pdf. Review titled Iris seed germination is a mandatory10(e) lead; original species, experimental light and chemical treatments remain to verify.
- MADS-box transcription factors determine the duration of temporary winter dormancy in closely related evergreen and deciduous Iris spp.: https://academic.oup.com/jxb/article/73/5/1429/6424403. Dormancy title retained under10(e); endogenous-hormone correlations alone do not establish an applied chemical response. Reader must verify any light or hormone treatment.
- Identification of Floral Scent Profiles in Bearded Irises: https://pmc.ncbi.nlm.nih.gov/articles/PMC6540295/. Headspace floral scent study of27 accessions; reader must establish attached living flowers or signaling rather than harvested-flower chemistry.
- Floral scent in Iris planifolia (Iridaceae) suggests food reward: https://iris.unipa.it/bitstream/10447/335902/7/PHYTOCHEM_2018_187_Revision_2_V0.pdf. Snippet describes natural-environment dynamic headspace collection and pollinator cues; verify living attached flowers and signaling interpretation.
- Integrated metabolomics and sensoryomics reveal scent diversification of 20 iris species for fragrance-targeted breeding: https://www.sciencedirect.com/science/article/pii/S0926669026001469. HS-SPME comparison across species, stages and organs; verify living attached flower sampling. Search also returned version S0926669025020849; one work requested once, with species list beyond the two named examples still to verify.
- Effects of different photoperiods on flower opening, flower closing and circadian expression of clock-related genes in Iris domestica and I. dichotoma.: https://pubmed.ncbi.nlm.nih.gov/35157159/. Snippet explicitly compares continuous darkness, five light/dark photoperiods and continuous white light for opening and closing. Diel evidence is already on main, so this request targets the light response.
- Physiological Analysis of Flower Formation in Wedgwood Iris: https://academic.oup.com/jxb/article-abstract/16/3/405/542063. Living bulb buds/scales in nutrient media were treated with gibberellic acid; verify the measured species behind Wedgwood cultivar.
- The Genus Iris Tourn. ex L.: Updates on Botany, Cultivation, Novel Niches and Impactful Applications: https://pmc.ncbi.nlm.nih.gov/articles/PMC12473546/. Genus review includes seed germination/dormancy and cultivation light requirements; reader should follow its experimental sources rather than treat advice or tissue phytochemistry as measured sensing.
- Analysis of Floral Volatile Components Among Different Bearded Iris Cultivars Using GC-IMS: https://www.ahs.ac.cn/EN/10.16420/j.issn.0513-353x.2024-0379. GC-IMS floral headspace study of16 cultivars is plausible; verify attached living material rather than harvested-tissue chemistry.

- Opening of Iris flowers is regulated by endogenous auxins: https://pubmed.ncbi.nlm.nih.gov/23218543/. Query `web: Iris germination gibberellin OR smoke OR dormancy`; GA3 opening response requires living attached tissue verification; cut flowers would fail10(a).

### Ricinus continuation, 2026-10-27

Adds1 protocol-screened genus,1 eye_type null search and24 wanted lines;0 evidence/0 measured cells. Worker17 totals2 genera,2 searches,38 wanted. Cumulative8 genera,11 searches,76 wanted;32 remain, next Conopholis. No uncompleted genus counted.

Both harvest_get.py and screen_candidates.py completed and report Ricinus absent from all cached runs1-17,20,23,24. Original gap traits all four checked; existing touch evidence oa7/recheck-codex-b-fixed retained. Sweep14 thin query record reviewed, not treated as full coverage. No matching existing wanted Ricinus lead and no owner status title/URL match. Canon catalog checked; no in-hand plant compilation closes these gaps.

12 successful connected web queries (worker17 cumulative22). All returned titles/snippets screened, including short result sets and broad/redundant results; raw responses work/harvest-c11/Ricinus-web{1,2,3,4}.json. OpenAlex remains skipped after429, no API query claimed executed; MDPI, UChicago, SANBI and all paper/source pages left unfetched per point3.

Exact successful queries:
- `web: Ricinus seed germination light dark`
- `web: Ricinus germination gibberellin OR smoke OR dormancy`
- `web: Ricinus jasmonate herbivore`
- `web: Ricinus flower opening time anthesis`
- `web: castor bean flower opening time anthesis`
- `web: Ricinus plant ocelli lens epidermal focusing eye`
- `web: castor bean plant ocelli lens epidermal focusing eye`
- `web: Ricinus chemical sensing volatiles`
- `web: castor bean chemical sensing volatiles`
- `web: Ricinus photoperiod phototropism light response`
- `web: castor bean photoperiod phototropism light response`
- `web: Euphorbiaceae photoreceptor review`

Family query returned general plant/fungal/algal photoreceptor reviews10.1002/wmts.36,10.1146/annurev-arplant-042809-112259,10.1007/s10265-016-0785-4,10.1007/s44372-025-00446-3, UV-B/shade reviews and insect-colour review; no Ricinus plant eye measurement in available snippets. Plant focusing reviews10.3390/plants12010061 and10.1111/j.1399-3054.1996.tb00674.x belong under light, with no Ricinus named in returned text; eye_type screened accordingly.

Diel pair returns morning pollen shedding in reproductive-biology review, plausible anthesis observations in developmental paper, and a castor crop chapter; those are wanted, not a false diel null. Generic crop manuals have snippets for other plants (cashew, garden bean, rice) and seasonal-flowering pages cannot establish Ricinus daily hours. RG, Scribd, PDFCoffee copies not used or opened. Chemical results include direct JA-induced nectar, methyl jasmonate response, artificial induction, intact-leaf headspace and castor-insect signal assays. Extracted leaf chemistry10.1071/BT16184, ricin analytical sensors and castor extract acting on Cyperus do not qualify as Ricinus sensing. Ixodes ricinus is a tick; Phaseolus leaf movement is another genus.

All genus germination/dormancy titles retained per10(e), even where snippets mention hydration/temperature or fixed culture photoperiod instead of an actual light comparison; reader must verify. Direct seedling-light, blue/red hypocotyl, photomorphogenesis and stomatal light/dark experiments prevent light exhaustion. High-light seed-coat/lipid study formerly dismissed in sweep14 retained for reading under the broader owner10(d) treatment rule. Endogenous expression alone is not measured photoreception; new castor genomics title retained cautiously for experimental-method verification. No measurements asserted.

New wanted provenance (exact query in each JSON):
- Phloem sugar flux and jasmonic acid-responsive cell wall invertase control extrafloral nectar secretion in Ricinus communis: https://pubmed.ncbi.nlm.nih.gov/25023077/. JA application increased extrafloral nectar secretion in living plants, an applied-hormone response under10(d).
- Studies on the Germination and Emergence of Castor Seedlings: https://www.mdpi.com/2674-1024/3/2/19. Gibberellin applied to seeds promoted faster/higher germination; mandatory germination lead. MDPI not fetched; AGRIS corroborating snippet https://agris.fao.org/search/fr/records/675ac59a0ce2cede71d0fe6c.
- GA(3) acts as a germination promoter in wild castor bean (Ricinus communis L.): https://avesis.ogu.edu.tr/yayin/af6aa22c-686a-4256-8959-f5f3dbc5f18f/ga3-acts-as-a-germination-promoter-in-wild-castor-bean-ricinus-communis-l. Title directly reports GA3 germination response, with nitrate also in returned keywords; verify any light treatment.
- Developing Seeds of Ricinus communis L., When Detached and Maintained in an Atmosphere of High Relative Humidity, Switch to a Germinative Mode without the Requirement for Complete Desiccation: https://academic.oup.com/plphys/article/90/2/702/6084283. Germination title retained per10(e); snippet concerns hydration/detachment so light/chemical experiments still require verification.
- Metabolite profiling of Ricinus communis germination at different temperatures provides new insights into thermo-mediated requirements for successful seedling establishment: https://www.sciencedirect.com/science/article/pii/S0168945215300352. Germination title retained per10(e); snippet tests temperature, so original methods must establish any light or chemical treatment.
- BREAKING DORMANCY IN CASTOR BEAN (Ricinus communis L.): https://produccion.siia.unam.mx/Publicaciones/ProdCientif/PublicacionFrw.aspx?id=504228&scopus=0. Snippet explicitly compares GA plus nitrate with cold/infrared light and methanol treatments; living seed chemical response lead.
- Single-seed selection of fast-germinating genotypes of castor (Ricinus communis): https://www.sciencedirect.com/science/article/pii/S0926669023000717. Snippet reports germination tests under GA exposure and punctured seed coats; verify light/dark conditions.
- Viability Prediction of Ricinus cummunis L. Seeds Using Multispectral Imaging: https://pmc.ncbi.nlm.nih.gov/articles/PMC4367427/. Mandatory germination-context lead under10(e); snippet gives only a fixed14/10h light/dark regime, which alone is not a light-treatment result. Verify experimental comparisons.
- Responses of the invasive Ricinus communis seedlings to competition and light: https://www.tandfonline.com/doi/full/10.1080/0028825X.2010.548069. Title directly tests seedling response to light and competition, qualifying under10(d).
- Effect of Induced Plant Expression on Ants and Extrafloral Nectaries Number in Cotton and Castor: English: https://jpt.faperta.unand.ac.id/index.php/jpt/article/view/81. Snippet describes herbivore and artificial induction of living cotton/castor plants; verify elicitor identity and castor response.
- Effect of Methyl Jasmonate on antioxidative enzyme activities and on the contents of ROS and H2O2 in Ricinus communis leaves: https://www.scielo.br/j/bjpp/a/cqF4s46CnGDTQ7ZKpHF37sg/?lang=en. Methyl-jasmonate treatment of Ricinus leaves is a plausible10(d) response; verify living plant rather than excised-leaf treatment.
- Review on Reproductive Biology of Caster bean (Ricinus communis L.): https://medwinpublishers.com/article/JENR/10.23880/jenr-16000268/full. Snippet reports morning pollen shedding; reader should follow original floral observations and separate shedding from flower-opening hour.
- Probing the floral developmental stages, bisexuality and sex reversions in castor (Ricinus communis L.): https://www.nature.com/articles/s41598-021-81781-9. Snippet names anthesis patterns varying by genotype plus temperature/hormone sex expression; plausible daily floral timing or living hormone-response source, with actual treatments still to verify.
- Castor (Ricinus communis): An Underutilized Oil Crop in the South East Asia: https://www.intechopen.com/chapters/72423. Genus chapter describes anthesis before female flower opening; original daily observations need verification rather than inferring hours from seasonal development.
- Dynamics of aquaporins and water relations during hypocotyl elongation in Ricinus communis L. seedlings: https://academic.oup.com/jxb/article/56/417/1831/484291. Snippet explicitly describes illumination rapidly inhibiting elongation and inducing photomorphogenesis; green/far-red control illumination did not inhibit growth.
- Cooperative effects of blue and red light in the inhibition of hypocotyl elongation of de-etiolated castor bean: https://plu.mx/plum/a/?doi=10.1016%2F0304-4211%2881%2990072-9&hideUsage=true&theme=plum-sciencedirect-theme. Snippet compares cotyledon/hypocotyl continuous irradiation and photoreceptor effects on elongation; true light-response lead.
- Analysis of Volatiles and Wound-Induced Volatiles Component of Ricinus communis: https://www.linyekexue.net/EN/10.11707/j.1001-7488.20060927. Snippet explicitly says intact-leaf volatiles and title contrasts wounding; verify attached living collection and signal function under10(a).
- Intercropping Okra and Castor Bean Reduces Recruitment of Oriental Fruit Moth, Grapholita molesta (Lepidoptera: Tortricidae) in a Pear Orchard: https://pmc.ncbi.nlm.nih.gov/articles/PMC10672554/. Snippet identifies castor headspace constituents and insect behavioural responses; verify living attached emission collection and distinguish castor signals from purchased compounds alone.
- Plant-derived volatile hydrocarbons from resistant castor genotypes deter Trialeurodes ricini and show potential for eco-friendly whitefly management: https://www.sciencedirect.com/science/article/pii/S2773078626000397. Volatile profiles of living castor genotypes with whitefly behavioural assays may qualify as emitted signals; verify sampling rather than extracted tissues.
- The stomatal response to evaporative demand persists at night in Ricinus communis plants with high nocturnal conductance: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-3040.2007.01658.x. Snippet explicitly compares castor gas exchange and stomatal responses in light and darkness.
- Monitoring Chemical-Induced Ripening of Castor (Ricinus communis L.) by UAS-Based Remote Sensing: https://ideas.repec.org/a/gam/jagris/v12y2022i2p159-d731910.html. Chemical-induced ripening title is a plausible applied-regulator response in living plants; original treatment and living status require reading.
- High light exposure on seed coat increases lipid accumulation in seeds of castor bean (Ricinus communis L.), a nongreen oilseed crop: https://pubmed.ncbi.nlm.nih.gov/26589321/. Measured living response to altered sunlight exposure; older sweep14 dismissed photosynthetic treatment, but10(d) includes growth trials under set light and reader must assess the actual response.
- Simultaneous measurement of water flow velocity and solute transport in xylem and phloem of adult plants of Ricinus communis over a daily time course by nuclear magnetic resonance spectrometry: https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-3040.2001.00704.x. Adult Ricinus solute concentrations differ between light and dark periods; verify controlled light response versus correlated daily sampling.
- Genomic analyses in castor identify signatures of selection and loci associated with hypocotyl elongation differentiation over millennia: https://www.sciencedirect.com/science/article/pii/S098194282600135X. Genus hypocotyl study discusses light-inducible regulators; verify a castor light-treatment experiment rather than infer a measured response from Arabidopsis gene functions.

Iris/Ricinus final validation: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c11.jsonl --wanted docs/views/wanted/harvest-c11.jsonl` printed **0 problems**. Both14 Iris and24 Ricinus wanted additions are genuine snippet/title leads, with unknown metadata left empty. No source text/evidence was committed.

### Conopholis continuation, 2026-10-27

Adds1 completed genus,1 eye_type search,8 wanted,0 evidence/0 measured cells. Worker17 totals **3 genera,3 searches,46 wanted,0 evidence**. Cumulative batch **9 genera,12 searches,84 wanted,0 evidence**; **31 remain**, next Tropaeolum. Stop between genera for fresh-context continuation.

Read both cached tools after completion: run5 supplements12/14,70 displayed result occurrences and15 family-review titles, with stored abstracts reviewed from work/harvest-c11/Conopholis-metadata.json. Eye_type is hidden by old thin sweep25 but original gaps require it; all four plant traits remain without actual main measured evidence. The old statement that the other three are already measured rests on other genera, not Conopholis, and cannot complete its protocol. No global wanted/status duplicate found for the8 additions.

12 successful web queries, worker17 cumulative34. Raw responses work/harvest-c11/Conopholis-web{1,2,3,4}.json. No quota refusal. No live OpenAlex request after round-wide429; no MDPI/UChicago/SANBI or any source-page fetch. Canon catalog checked; no in-hand plant compilation supplies Conopholis data. Animal eye canon named per point8. Every cached successful query, including zero-hit ones, copied in record:
- `Conopholis phytochrome photoreceptor`
- `Conopholis light perception`
- `Conopholis phototropism`
- `Conopholis flower opening time`
- `Conopholis nyctinasty`
- `Conopholis volatile signalling`
- `Conopholis photoperiod`
- `Conopholis circadian rhythm`
- `Conopholis anthesis`
- `Conopholis pollination biology`
- `Orobanchaceae photoreceptor review`

Exact web queries:
- `web: Conopholis seed germination light dark`
- `web: Conopholis germination gibberellin OR smoke OR dormancy`
- `web: Conopholis floral scent volatiles`
- `web: Conopholis flower opening time anthesis`
- `web: squawroot flower opening time anthesis`
- `web: Conopholis plant ocelli lens epidermal focusing eye`
- `web: squawroot plant ocelli lens epidermal focusing eye`
- `web: Conopholis chemical sensing volatiles`
- `web: squawroot chemical sensing volatiles`
- `web: Conopholis photoperiod phototropism light response`
- `web: squawroot photoperiod phototropism light response`
- `web: Orobanchaceae photoreceptor review`

All three cached citation steps on10.3390/agronomy13092250,10.1603/022.038.0629 and10.1111/een.12947 returned0. Family review results include PHYA phylogeny10.3732/ajb.93.7.1039, host-interaction review10.1111/nph.17083, general photoreceptor review10.1016/j.conb.2015.01.013 and broad plant/animal gene/optics reviews. Phytochrome sequence phylogeny does not itself demonstrate a functional response in Conopholis; no null inferred from it. Plant ocelli/focusing review10.3390/plants12010061 belongs under light; no genus measurement named. Petal microsculpture10.1071/sb16028 includes Conopholis but gives no eye; optical focusing, if later read, goes to light.

Web expansion often ignored the rare genus: Conophytum, Conopodium, Gymnadenia conopsea, Conogethes and conophthorin are distinct taxa/compound names and cannot supply Conopholis evidence. General smoking/germination and phototropism reviews name no Conopholis in returned text. Seasonal squawroot flora snippets give spring or May-June flowering, not daily hours; rice, guava, Setaria and Gloriosa anthesis are other genera. No timing value claimed. A book title from a suspicious-copy host was retained only as a legally obtainable ISBN lead, without fetching the copy or accepting a measurement.

Cached chemical candidates: holoparasite olfactory-signal review10.3897/phytokeys.275.192014 retained wanted. The two1908 Key and Flora records10.5962/bhl.title.17342 and10.5962/bhl.title.54197 are broad identification guides; available abstract text names generic flower collection and taxonomy, not Conopholis chemical response. Non-strigolactone review retained for genus-specific experiments. Lettuce KAI2, Striga/Orobanche germination, Arnica achenes and Tibouchina floral-colour studies concern other genera; taxonomic/habitat/genome/black-bear diet titles are not sensing experiments. Conserving seeds in Mexico retained for germination species-list review; seedling/tubercle anatomy retained because snippet names germinated and attached Conopholis seedlings.

New wanted provenance (all titles/metadata from cached harvest or returned web, unknown fields empty):
- A multiverse of trophic networks and coevolutionary trajectories among holoparasitic Orobanchaceae and their animal associates: a global perspective: https://phytokeys.pensoft.net/article/192014/download/pdf/. Holoparasitic Orobanchaceae review explicitly covers olfactory signals and appears in genus queries; reader must verify actual Conopholis emission/signaling observations rather than carry from other genera. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis volatile signalling`.
- Architectural effects regulate resource allocation within the inflorescences with nonlinear blooming patterns: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ajb2.16001. Blooming-pattern and flowering-sequence study is a plausible source of daily floral observations; truncated cached abstract does not establish measured genus/species or hours. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis anthesis`.
- Flower position within plants influences reproductive success both directly and via phenology: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ajb2.16405. Floral-position/phenology observations may include Conopholis daily flowering; reader must establish measured genus/species and distinguish seasonal sequence from daily hours. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis flower opening time`.
- Variación intrainflorescencia en caracteres florales y reproductivos de Conopholis alpina (Orobanchaceae): ¿efecto de la competencia por recursos o de la arquitectura?: http://bindani.izt.uam.mx/downloads/1831ck195. Thesis specifically studies floral/reproductive variation in Conopholis alpina; a plausible source for anthesis timing, not an established daily-hour result from the cached abstract. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis pollination biology`.
- Conserving seeds of useful wild plants in Mexico: main issues and recommendations: https://link.springer.com/content/pdf/10.1007%2Fs10722-016-0427-7.pdf. Seed conservation/germination study of204 useful Mexican species retained for species-list and experimental-treatment verification; actual inclusion of Conopholis and light/chemical comparisons not stated in truncated abstract. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis photoperiod`.
- Non-strigolactone natural products interfering with parasitic weed development: https://pubs.rsc.org/en/content/articlepdf/2026/np/d5np00077g. Review discusses chemically induced germination, haustorium formation and host tropism; returned by genus query, with Conopholis-specific experiments still to verify. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `Conopholis volatile signalling`.
- The developmental anatomy of Conopholis americana (Orobancaceae) seedlings and tubercles: journal via library. Search title/snippet identifies germinated and attached Conopholis americana seedlings. Germination/host-attachment experiments may contain light or chemical conditions; reader must verify actual contrasts. Broker search result was not opened or used as a paper source; obtain by legal journal/library route. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `web: Conopholis seed germination light dark`.
- Spring Wildflowers of the Northeast: A Natural History: ISBN9781400841745; publisher/library edition. Book title returned in squawroot anthesis search; possible source for genus flower-opening observations. No book copy fetched and no timing measurement inferred from an unauthorized-copy host search result. Obtain the publisher/library edition using ISBN9781400841745. Cached harvest abstract/title or connected web snippet screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `web: squawroot flower opening time anthesis`.

Final metadata cleanup: unknown year0 placeholders in59 c11 wanted lines changed to JSON null at parent request; observed source-verified years preserved. Iris eye disposition explicitly scoped with view plant and the two plant species, preserving mantis records. Final combined gate is rerun after metadata cleanup.

Final worker17 combined validation after all annotations/year cleanup: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c11.jsonl --wanted docs/views/wanted/harvest-c11.jsonl` printed **0 problems**. No incomplete genus or plausible wanted trait called exhausted. Clean handoff: Tropaeolum, then Chasmanthium onward,31 remain. Prior continuation commit36ff9434.

## 2026-10-27 — worker23 continuation

Tropaeolum complete: **1 genus,1 search,9 wanted,0 evidence,0 measured cells** this worker. Cumulative **10 genera,13 searches,93 wanted,0 evidence**; **30 remain**, next Chasmanthium. No branch/gate/app changes. Read AGENTS, round28 guide, THOROUGH, BRIEF including Round2, round3/round4 and desk-screen1-10 including plant10(e). Required harvest and screening tools completed. Managed network status ready/unrestricted; no credentials used.

12 successful connected web queries; no quota refusal. No OpenAlex/MDPI/UChicago/SANBI or plant source-page requests. Cached run5 with supplements12/14/20 has160 displayed result occurrences,8 family-review titles,137 unique works; titles and available abstract starts screened. Canon catalog checked: no in-hand plant compilation supplies Tropaeolum data. Owner eye_type rule applied; other original gaps are not suppressed by old sweep26.

Exact cached queries:
- `Tropaeolum phytochrome photoreceptor`
- `Tropaeolum light perception`
- `Tropaeolum phototropism`
- `Tropaeolum flower opening time`
- `Tropaeolum nyctinasty`
- `Tropaeolum volatile signalling`
- `Tropaeolum photoperiod`
- `Tropaeolum circadian rhythm`
- `Tropaeolum anthesis`
- `Tropaeolum pollination biology`
- `Tropaeolum epidermal lens cells`
- `Tropaeolum epidermal focusing leaf optics`
- `Tropaeolaceae photoreceptor review`

Exact web queries:
- `web: Tropaeolum seed germination light dark`
- `web: Tropaeolum germination gibberellin OR smoke OR dormancy`
- `web: Tropaeolum floral scent volatiles`
- `web: Tropaeolum flower opening time anthesis`
- `web: nasturtium flower opening time anthesis`
- `web: Tropaeolum plant ocelli lens epidermal focusing eye`
- `web: nasturtium plant ocelli lens epidermal focusing eye`
- `web: Tropaeolum chemical sensing volatiles`
- `web: nasturtium chemical sensing volatiles`
- `web: Tropaeolum photoperiod phototropism light response`
- `web: nasturtium photoperiod phototropism light response`
- `web: Tropaeolaceae photoreceptor review`

New wanted provenance:
- Application of phytohormones as attenuators of salt stress in Tropaeolum majus L. (Tropaeolaceae); https://hrcak.srce.hr/file/400168. Living nasturtium hormone treatments under salt stress compare jasmonic acid, salicylic acid, cytokinin and polyamine with controls. This tests applied chemical responses under plant10(d). Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum light perception"`.
- Effect of Naphthaleneacetic Acid (NAA) and 6-Benzylamino Purine (BAP) on In-Vitro Propagation of "Mashua" (Tropaeolum tuberosum Ruíz & Pavón) Morphotypes from Peru; https://phcogj.com/sites/default/files/PharmacognJ-15-4-563.pdf. NAA and BAP treatments are compared for micropropagation of living mashua seedlings, a growth regulator response under plant10(d). Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum photoperiod"`.
- Growth, Gas Exchange, and Phytochemical Quality of Nasturtium (Tropaeolum majus L.) Subjected to Proline Concentrations and Salinity; https://www.mdpi.com/2223-7747/14/3/301/pdf?version=1737442579. Applied proline concentrations and salinity are compared for living nasturtium growth, gas exchange and physiology; read the responses and conditions. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum photoperiod"`.
- Seed Germination of the Herbaceous Vine Tropaeolum pentaphyllum Lam. (Tropaeolaceae): A Neglected Geophyte with High Agricultural Potential; https://journaljeai.com/index.php/JEAI/article/download/1900/3806. Controlled seed germination compares natural light with darkness. Web result also describes a light-dependent germination result; source reading is still needed. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum light perception"`.
- Flowering time response of Nasturtium (Tropaeolum majus L.) cultivar ‘Empress of India’ to photoperiod, light integral and temperature using photo-thermal model; https://doaj.org/article/d8576fcf894546ea8e307f3807b9765d. Controlled flowering experiments compare photoperiods, shade levels and temperatures in Empress of India nasturtium; a direct light-response experiment, not daily anthesis. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum photoperiod"`.
- Continuous Lighting and High Daily Light Integral Enhance Yield and Quality of Mass-Produced Nasturtium (Tropaeolum majus L.) in Plant Factories; https://www.mdpi.com/2223-7747/10/6/1203/pdf. Continuous lighting and daily light integral treatments test nasturtium growth, secondary metabolites and light-use efficiency. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum photoperiod"`.
- Morphological, biochemical and physiological responses of Indian cress (Tropaeolum majus) to elevated UV-B radiation; https://doi.org/10.18054/pb.2015.117.3.2858. Outdoor enhanced UV-B treatments test nasturtium physiology and secondary metabolites. Harvest also indexes the same title under DOI10.18054/pb.v117i3.2858 with a conflicting year; obtain one copy and verify bibliographic metadata. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum volatile signalling"`.
- Floral biology of Tropaeolum majus L. (Tropaeolaceae) and its relation with Astylus variegatus activity (Germar 1824) (Coleoptera: Melyridae); https://www.scielo.br/j/aabc/a/KsRx7LyHKHNZhnNYnkhG8Zw/?lang=en&format=pdf. Floral biology study observes flowers and insects during daylight; returned SciELO web snippet explicitly describes daytime anthesis. Read the flower observations for within-day timing. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum anthesis"`.
- 10. Friedrich Oehlkers: Zur reizphysiologischen Analyse der postfloralen Krümmungen des Blütenstiels von Tropaeolum majus; https://doi.org/10.1111/j.1438-8677.1920.tb07352.x. Experimental stimulus physiology of postfloral pedicel curvature in nasturtium, returned by the phototropism query. Verify which stimuli were manipulated and whether light-direction response was measured. Cached harvest title/abstract and returned web snippets screened 2026-10-27; source not fetched/read, no evidence logged. Query: `query "Tropaeolum phototropism"`.

Global wanted/evidence/status checked before append. Existing1938 leaf light/gravity response10.1093/oxfordjournals.aob.a084037 is already requested in harvest26;1990 photoperiod/tuber study W1579049020/W2588713156 already requested in plant1. Preserve these requests without duplication. UV-B record has two cached DOI/year variants; one wanted copy, year null until verified. Authors absent in cache remain empty.

Tropaeolum extracts/essential oils/hydrosols and floral tissues/processed juice (including10.3390/life15071053,10.1021/jf902946v,10.3389/fnut.2022.912680,10.17113/ftb.60.04.22.7667) do not establish a living sender/receiver response. Chromoplast/nectar-spur gene expression alone does not measure sensing. Rose, Brassica, Hymenaea and Chelidonium studies concern other genera. Reproductive stage/season and floral longevity alone were not converted into daily hours. Stacked-scattering paper measures collected-petal reflection; no light perception inferred. Generic plant-ocelli and focusing survey goes under light when a genus measurement is established, never eye_type. Darwin1878 manuscript search snippet contains actual leaf-orientation observation, retained as a historical corroborating lead in this note; existing1938 experimental request already targets the same open light trait. Other broad physiology books/reviews have no Tropaeolum measurement identified in available abstracts and were not requested as background.
