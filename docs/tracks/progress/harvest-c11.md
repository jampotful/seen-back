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

### Chasmanthium continuation, 2026-10-27

Adds **1 genus,2 searches,1 wanted,0 evidence**. Worker23 totals **2 genera,3 searches,10 wanted,0 evidence/0 measured cells**. Batch cumulative **11 genera,15 searches,94 wanted,0 evidence**; **29 remain**, next Paulownia. Tropaeolum gate printed0 problems before commit14f29ef2.

10 successful connected web queries here, worker23 cumulative22; no quota refusal. Cached run6 and supplements14/20 contain70 displayed result occurrences,15 family-review titles and68 unique stored abstracts/titles; all screened. Both required harvesting/screening aids run, plus cached metadata inspected. No new API, MDPI/UChicago/SANBI or source-page fetch. Global evidence/wanted/status check found no duplicate for the hormone experiment. No in-hand canon compilation supplies Chasmanthium data; relevant catalog DOI lists retained.

Exact cached queries:
- `Chasmanthium phytochrome photoreceptor`
- `Chasmanthium light perception`
- `Chasmanthium phototropism`
- `Chasmanthium flower opening time`
- `Chasmanthium nyctinasty`
- `Chasmanthium anthesis`
- `Chasmanthium pollination biology`
- `Chasmanthium volatile signalling`
- `Chasmanthium epidermal lens cells`
- `Chasmanthium epidermal focusing leaf optics`
- `Poaceae photoreceptor review`

Exact web queries:
- `web: Chasmanthium seed germination light dark`
- `web: Chasmanthium germination gibberellin OR smoke OR dormancy`
- `web: Chasmanthium floral scent volatiles`
- `web: Chasmanthium flower opening time anthesis`
- `web: northern sea oats flower opening time anthesis`
- `web: Chasmanthium plant ocelli lens epidermal focusing eye`
- `web: northern sea oats plant ocelli lens epidermal focusing eye`
- `web: Chasmanthium chemical sensing volatiles`
- `web: northern sea oats chemical sensing volatiles`
- `web: Poaceae photoreceptor review`

Wanted: Hormonal Effects on the Germination Response of Chasmanthium latifolium; 10.21273/hortsci.30.4.836d; https://journals.ashs.org/downloadpdf/journals/hortsci/30/4/article-p836D.pdf. Living Chasmanthium latifolium caryopses were treated with nitrate, GA3 and kinetin; germination was compared across treatment combinations. This is an applied chemical response under plant10(d). Cached harvest title/abstract screened2026-10-27; source not fetched/read, no evidence logged. Exact query: `query "Chasmanthium light perception"`.

Main holds only the partial measured light/photoperiod report sweep27#13 for this genus. No light query pair or redundant light request added. Hormonal germination qualifies under10(d), so chemical remains pending. Cached UV-B and shade studies are light-related background to an already-evidenced trait and were not requested. Diel cached candidate10.1111/j.1365-294x.2006.03051.x is general phytochrome biology, without genus-specific daily data in available abstract. All returned genus flora/nursery phenology gives flowering months, not hours. Uniola paniculata source specifically gives early-morning floret opening, but that is a distinct genus; old synonym Uniola latifolia must not be confused with Uniola paniculata. Broad oat-crossing anthesis and oat food-volatilome results concern Avena; Chimonanthus/Chrysanthemum scent results are likewise other genera. Eye candidate10.1093/aob/mct027 is inflorescence morphology, using human eyes rhetorically. General ocelli/focusing sources belong under light if a genus response is established; plant eye_type stays none by owner decision. No speculative generic source requested for missing daily timing.

### Paulownia continuation, 2026-10-27

Adds **1 genus,1 search,9 wanted,0 evidence**. Worker23 totals **3 genera,4 searches,19 wanted,0 evidence/0 measured cells**. Batch cumulative **12 genera,16 searches,103 wanted,0 evidence**; **28 remain**, next Chenopodium. Chasmanthium validation printed0 problems before commit94dc0e6a. Stop between genera for fresh-context continuation after final combined validation.

10 successful web queries here, worker23 cumulative32. Raw responses in work/harvest-c11/Paulownia-web1/2/3.json. No quota refusal or prohibited live API/source-page fetch. Cached run7 supplements14/20:120 result occurrences,2 family-review titles,109 unique stored abstracts/titles screened. Original light evidence checked directly against measured source record; no old thin search suppresses open chemical/diel/eye traits. Canon catalog checked; no in-hand compilation adds Paulownia data.

Exact cached queries:
- `Paulownia phytochrome photoreceptor`
- `Paulownia light perception`
- `Paulownia phototropism`
- `Paulownia flower opening time`
- `Paulownia nyctinasty`
- `Paulownia anthesis`
- `Paulownia pollination biology`
- `Paulownia volatile signalling`
- `Paulownia epidermal lens cells`
- `Paulownia epidermal focusing leaf optics`
- `Paulowniaceae photoreceptor review`

Exact web queries:
- `web: Paulownia seed germination light dark`
- `web: Paulownia germination gibberellin OR smoke OR dormancy`
- `web: Paulownia floral scent volatiles`
- `web: Paulownia flower opening time anthesis`
- `web: princess tree flower opening time anthesis`
- `web: Paulownia plant ocelli lens epidermal focusing eye`
- `web: princess tree plant ocelli lens epidermal focusing eye`
- `web: Paulownia chemical sensing volatiles`
- `web: princess tree chemical sensing volatiles`
- `web: Paulowniaceae photoreceptor review`

New wanted provenance:
- Identification of Genes Related to Paulownia Witches’ Broom by AFLP and MSAP; https://www.mdpi.com/1422-0067/15/8/14669/pdf?version=1408608398. Methyl methane sulfonate treatment of living diseased Paulownia seedlings restored normal morphology in the cached abstract. This is an observed chemical-treatment response, beyond genomic prediction alone; confirm the species in the methods. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `query "Paulownia light perception"`.
- Salinity effects on protein content, lipid peroxidation, pigments, and proline in Paulownia imperialis (Siebold & Zuccarini) and Paulownia fortunei (Seemann & Hemsley) grown in vitro; http://www.scielo.cl/scielo.php?script=sci_arttext&amp;pid=S0717-34582010000500013. Title names physiological and biochemical responses of living Paulownia cultured under salinity treatments, a direct chemical exposure comparison. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `query "Paulownia light perception"`.
- A carotenoid cleavage dioxygenase 4 from Paulownia tomentosa determines visual and aroma signals in flowers; https://doi.org/10.1016/j.plantsci.2023.111609. Flower aroma signals and carotenoid-derived volatiles are studied in Paulownia. Reader must establish a living-flower emission or signaling experiment; isolated-enzyme activity or harvested-tissue chemistry alone does not qualify. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `query "Paulownia anthesis"`.
- Biology of Flowering Paulownia tomentosa in the conditions of the Sirdaryo Region; https://ijcmas.com/15-4-2026/Juraev Hasanbek Nuriddinovich and Allaberdiev Rustamjon Khamraevich.pdf. Dedicated flowering-biology observations include floral structure and pollination. Retained for checking within-day anthesis timing; the truncated abstract only states seasonal flowering delay, so no daily hour is yet established. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `query "Paulownia pollination biology"`.
- Stimulation of empress tree seed germination by liquid smoke; https://agris.fao.org/search/en/providers/122535/records/65de55130f3e94b9e5cd94ea. Applied liquid smoke and growth regulators are tested in living empress-tree seed germination. This targets the open chemical trait; light is already measured on main. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `web: Paulownia seed germination light dark`, `web: Paulownia germination gibberellin OR smoke OR dormancy`, `web: Paulownia floral scent volatiles`.
- Effects of Gibberellin on Seed Germination and Physiological Characteristics of Paulownia Seedlings under Salt Stress; https://www.aeeisp.com/seed/en/article/doi/10.16590/j.cnki.1001-4705.2021.06.031. Applied GA3 concentration treatments compare germination, seedling growth and antioxidant physiology under salt stress across three Paulownia species, qualifying under plant10(d). Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `web: Paulownia seed germination light dark`, `web: Paulownia germination gibberellin OR smoke OR dormancy`, `web: Paulownia floral scent volatiles`.
- Germination of Paulownia Seeds in the Presence and Absence of Light; https://rngr.net/publications/tpn/32-4/32_4_27_29.pdf/at_download/file. The returned USDA seed-paper result and associated title snippet describe GA3 pretreatment alongside stratification and light/dark comparisons. Read for the chemical germination treatment; do not request merely as repeat light evidence. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `web: Paulownia seed germination light dark`, `web: Paulownia germination gibberellin OR smoke OR dormancy`, `web: Paulownia floral scent volatiles`.
- Light and nitrate interaction in phytochrome-controlled germination of Paulownia tomentosa seeds.; https://pubmed.ncbi.nlm.nih.gov/24196743/. Nitrate interaction is part of a living-seed germination experiment. Read for the applied chemical response; the already-known light response alone is not the reason for this request. Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `web: Paulownia seed germination light dark`, `web: Paulownia germination gibberellin OR smoke OR dormancy`, `web: Paulownia floral scent volatiles`.
- Characteristics of BVOCs from Fragrant Flowering Trees and Their Emission Along Urban Roadsides in Shanghai, China; https://agris.fao.org/search/en/providers/122436/records/69b95eb9ce5e0ae4f87880d9. Floral samples across flowering stages and roadside air emission measurements include Paulownia tomentosa. Verify living attached flowers and the signaling interpretation; harvested floral chemistry alone does not qualify under10(a). Cached harvest abstract/title or connected web title/snippet screened2026-10-27; source not fetched/read, no evidence logged. Returned query/batch: `web: Paulownia seed germination light dark`, `web: Paulownia germination gibberellin OR smoke OR dormancy`, `web: Paulownia floral scent volatiles`.

Global evidence/wanted/status inspected before append; no duplicates of these9 sources located. Unknown years remain null, rather than inferring years from DOI strings or relative web dates.1981 comes from the returned Tree Planters Notes Fall1981 source listing; cached years retained where provided. Authors absent from metadata remain empty.

Chemical gap is supported by real applied-GA3, nitrate, smoke, salinity and MMS morphology experiments, with floral-emission candidates requiring attached living-material verification. The2023 CCD4 work is retained for aroma/signaling measurements, not for enzyme sequence prediction. The2026 flowering-biology paper is a dedicated Paulownia observation source; daily timing remains unconfirmed, so no diel null. Seasonal month ranges in USDA/arboretum results and New Zealand handbook are not hours. Cached circadian transcriptome2014 studies describe infection/gene expression, not a measured daily oscillation from available text; the related2014 MMS study separately reports morphological recovery and is wanted for chemical response. Other-genus rice, poplar, peony, petunia and Verbena studies cannot provide Paulownia daily/chemical data.

Steam-distilled Shan-Tong floral oil W7220175094, flower phytochemistry10.1007/s11101-014-9376-y, dried medicinal tea tissues10.3390/antiox14030280, extracts and biorefinery/wood processing were not requested as living sensing evidence. The three cached eye candidates are substring matches inside lignocellulosic. General ocelli/epidermal focusing belongs under light; no plant eye inferred.

Worker23 final combined check `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c11.jsonl --wanted docs/views/wanted/harvest-c11.jsonl` printed **0 problems**. No incomplete genus called complete and no wanted trait declared exhausted. Final handoff: **Chenopodium**, then Aquilegia onward; **28 remain**.

## 2026-10-27 — worker30 continuation: Chenopodium

Adds **1 genus,1 search,6 wanted,0 evidence/0 measured cells**. Batch cumulative **13 genera,17 searches,109 wanted,0 evidence**; **27 remain**, next Aquilegia. Read AGENTS and current guide, round4, THOROUGH, BRIEF/Round2, round3, desk-screen1–10 including10(e), audit53/54 findings. No branch/gate or issue29/30 edits.

Both required aids run: Chenopodium absent from harvest runs1–17,20,23,24; no cached query/candidate omitted. Main actual light evidence sweep16#5 (Karssen1970 Pfr-dependent living germination) preserved. Old thin two-query search does not suppress chemical/diel/eye work. Canon catalog checked; no in-hand plant compilation supplies this genus. Global wanted/evidence/papers-status checked before append: no matching new sources. Unknown years remain null; unknown authors empty. Ten successful connected web queries, all returned titles/snippets screened; variable counts, no claim of twenty where fewer supplied. OpenAlex remains skipped after429; no MDPI/UChicago/SANBI or primary source page fetched. No web quota refusal.

Exact queries:
- `web: Chenopodium seed germination light dark`
- `web: Chenopodium germination gibberellin OR smoke OR dormancy`
- `web: Chenopodium jasmonate herbivore`
- `web: Chenopodium flower opening time anthesis`
- `web: lamb's quarters flower opening time anthesis`
- `web: Chenopodium plant ocelli lens epidermal focusing eye`
- `web: lamb's quarters plant ocelli lens epidermal focusing eye`
- `web: Chenopodium chemical sensing volatiles`
- `web: lamb's quarters chemical sensing volatiles`
- `web: Amaranthaceae photoreceptor review`

Wanted provenance:
- Studies on Seed Dormancy and Germination in Chenopodium album L.; https://www.jstage.jst.go.jp/article/weed1962/1970/10/1970_10_19/_article/-char/en. Snippet reports that applied gibberellin at 1,000 ppm stimulated germination in place of light exposure. This is a living seed hormone-response experiment under plant10(d).
- Distinct hormonal and morphological control of dormancy and germination in Chenopodium album dimorphic seeds; https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1156794/full. Snippet reports release of black-seed dormancy by applied gibberellin and contrasting GA/ABA sensitivity across seed morphs and accessions. Read the actual treatment experiments, not sequence predictions.
- Effects of Temperature and Gibberellic Acid (GA3) on seed Germination of Vicia sativa, Chenopodium album and Physalis minima; https://indianjournals.com/article/ijaeb-6-4-018. Snippet describes GA3 concentration treatments of living Chenopodium album seeds at 50, 150, 250 and 350 ppm across temperatures. Chemical response is unresolved; the existing light record is not the reason for requesting this.
- Seed Germination in Chenopodium album L: Relationships between Nitrate and the Effects of Plant Hormones; https://academic.oup.com/plphys/article/77/4/940/6079828. Snippet describes applied ethylene, gibberellins and kinetin in seed germination experiments under different nitrate availability; this targets living chemical response.
- Investigation of the endogenous rhythm of flowering in Chenopodium rubrum L.; https://bp.ueb.cas.cz/artkey/bpl-197405-0005_Investigation-of-the-endogenous-rhythm-of-flowering-in-Chenopodium-rubrum-L.php. The title explicitly investigates an endogenous flowering rhythm; snippet describes inductive photoperiodic-cycle experiments. Read to establish the measured clock rhythm and current taxonomic scope; days to seasonal flowering alone would not qualify.
- Plant volatiles as cues and signals in plant communication; https://onlinelibrary.wiley.com/doi/full/10.1111%2Fpce.13910. Review snippet specifically reports exposure of living barley to Chenopodium album donor volatiles reducing aphid acceptance, citing Glinwood et al.2004 and Ninkovic and Ahman2009. Read the cited experiment and living donor setup; this is a named genus-specific signaling measurement lead, not a generic background request.

No light-only germination studies requested: existing measured trait already covered. Applied GA, nitrate/ethylene/kinetin and GA-ABA germination treatments qualify under10(d); this is why the chemical sources are wanted. The flowering-rhythm study is held pending actual clock measurement, with no diel null. Quinoa pollen protocol PMC9118578 samples pollen at a fixed5h after lights-on and over days after anthesis; this alone does not show a daily rhythm and was not requested. New2026 Chenopodium album BBCH phenology10.1007/s44372-026-00861-0, PROSEA crop stages and flora/extension results give stages/seasons rather than within-day hours. Endogenous clock lead prevents treating daily physiology absent.

Chemical-search returns on cooked quinoa seed volatiles, distilled oils/ascaridole and harvested culinary tissues10.3389/fnut.2022.912680 are chemistry under10(a), not living-plant response. Other-genus Nicotiana/tomato/Lolium jasmonate experiments cannot supply Chenopodium. The C.ambrosioides volatile-stress study10.3390/plants12223810 names living maize/soybean receptors; donor setup and taxonomy (Dysphania) uncertain, so no new request for queue C.album from it. General optical/ocelli reviews name no genus measurement in returned snippets and focusing belongs under light, never eye_type. Amaranthaceae review query returned general photoreceptors10.1146/annurev-arplant-042809-112259 and10.1002/wmts.36 plus family C4 phylogeny10.1086/378649, no genus eye data; none requested as background.

Chenopodium validation: required screen_candidates.py --check printed **0 problems** before commit. No incomplete protocol called complete.

### Aquilegia continuation, 2026-10-27

Adds **1 genus,1 search,8 wanted,0 evidence**. Worker30 cumulative **2 genera,2 searches,14 wanted,0 evidence/0 measured cells**. Batch cumulative **14 genera,18 searches,117 wanted,0 evidence**; **26 remain**, next Helianthus. Chenopodium gate0 problems before commitfb66e110.

12 successful connected web queries; worker30 total22. Both required aids run: Aquilegia absent from harvest runs1–17,20,23,24, no cached queries/candidates omitted. Raw responses saved work/harvest-c11/Aquilegia-web1–4.json. Existing main order-level oa2#3883 PHYE transcript inference is not a measured living-species response, so full light protocol run. No other actual Aquilegia sensing evidence in main/corrected logs. No in-hand plant canon compilation; canon catalog checked, no generic canon requested anew. Global wanted/status inspected; no new source duplicated. Unknown metadata stays null/empty. No OpenAlex/MDPI/UChicago/SANBI or source-page fetch. Search results included a library-proxy OUP host and ResearchGate; neither opened nor used as source. Usable nonproxy primary/index snippets supply retained facts.

Exact queries:
- `web: Aquilegia seed germination light dark`
- `web: Aquilegia germination gibberellin OR smoke OR dormancy`
- `web: Aquilegia floral scent volatiles`
- `web: Aquilegia flower opening time anthesis`
- `web: columbine flower opening time anthesis`
- `web: Aquilegia plant ocelli lens epidermal focusing eye`
- `web: columbine plant ocelli lens epidermal focusing eye`
- `web: Aquilegia chemical sensing volatiles`
- `web: columbine chemical sensing volatiles`
- `web: Aquilegia photoperiod phototropism light response`
- `web: columbine photoperiod phototropism light response`
- `web: Ranunculaceae photoreceptor review`

Wanted provenance:
- Environmental and molecular analysis of the floral transition in the lower eudicot Aquilegia formosa; https://link.springer.com/article/10.1186/2041-9139-2-4. Experimental photoperiod and vernalization comparison reports little or no photoperiod response in living A.formosa. A measured day-neutral response is a useful finding; this request targets the response experiment, not gene expression alone.
- Growth and development of aquilegia in relation to temperature, photoperiod and dry seed vernalization; https://www.sciencedirect.com/science/article/abs/pii/S0304423896009983. Commercial cultivars and genetic lines were grown under controlled temperature and photoperiod and evaluated for growth/flowering. Source listing at Rutgers explicitly identifies Merritt, Gianfagna, Perkins and Trout1997; request actual photoperiod comparisons, not merely cold response.
- Rate and time of GA4/7 treatment affect vegetative growth and flowering in a genetic line of Aquilegia × hybrida Sims; https://www.sciencedirect.com/science/article/abs/pii/S0304423899000825. Applied gibberellin at different developmental stages/rates changes flower number, plant height and leaf area in living Aquilegia. This directly tests chemical response under10(d).
- Conservation implications of seed germination studies of Aquilegia fragrans Benth.: A native and endangered medicinal plant species of Kashmir Himalaya; https://www.sciencedirect.com/science/article/pii/S0254629924000322. The snippet explicitly describes GA3, BAP and zeatin treatment comparisons in living seeds and nondeep simple morphophysiological dormancy. Applied hormones qualify under10(d); read germination methods for any light comparison too.
- Effect of Gibberellin Treatment on Growth and Flowering Characteristics in the Cultivation of Aquilegia japonica Nakai & H. Hara; https://www.kjpr.kr/articles/article/xq05/. GA3 and GA4+7 treatments compare plant height, petiole elongation and flowering in living cultivated plants. The snippets report flowering91.7–100% after GA3. Verify treatment conditions in original before logging.
- Virus-induced gene silencing as a tool for functional analyses in the emerging model plant Aquilegia (columbine, Ranunculaceae); https://link.springer.com/article/10.1186/1746-4811-3-6. Despite the molecular title, the returned snippet reports actual GA concentration treatment of fresh/aged seeds, with no germination improvement. A measured absence of response to applied hormone is a chemical-response result; read that experiment, not VIGS sequence work alone.
- Flowering, nectar secretion, pollen shed and insect foraging on Aquilegia vulgaris L. (Ranunculaceae); https://citeseerx.ist.psu.edu/document?doi=7013a98092dc4e8771d2cb01b906166e24a4f7f1&repid=rep1&type=pdf. The scholarly index snippet explicitly reports a diurnal opening peak between05:00 and07:00 GMT+2 and declining opening from16:00. This targets actual within-day flower timing, not seasonal bloom dates. Original journal metadata and DOI not shown by the usable returned source.
- Population-specific responses of floral volatiles to abiotic factors in changing environments; https://bsapubs.onlinelibrary.wiley.com/doi/10.1002/ajb2.1846. Plants grown from three wild populations received water treatments and dynamic headspace sampling of enclosed flowers. This is a living floral-emission/signaling candidate. Dataset-catalog snippet separately identifies day/evening emission samples; verify attached living flowers and actual within-day comparison before logging.

Specific measurements drive requests: A.formosa photoperiod experiment reports day neutrality, so no assumption of a universally positive light effect. Controlled hybrids supply growth/flowering comparisons. Applied GA3/GA4+7, BAP/zeatin and even the negative GA result embedded in VIGS methods qualify under10(d). Actual within-day vulgaris opening hours are from the CiteSeer index snippet, not a fetched paper; no evidence record. The living A.coerulea headspace experiment is the strongest volatile lead, with day/evening dataset metadata as a possible diel comparison.

Existing anther study10.3732/ajb.91.12.1969 is already requested in plant1; not duplicated and thermal-desorbed excised anthers alone would fail10(a). Essential oils of A.olympica likewise do not qualify. Floral SPME paper10.1186/s13065-021-00754-1 and TPS studies10.1093/hr/uhab020/kiaf372 may include detached-flower chemistry or sequence prediction; direct living-plant hormonal/headspace targets already retained, so no redundant speculative request. Genetic introgression paper73(6):886 supplies no extra open-trait target beyond the retained emission experiment. Deno A.formosa entry is indexed in Supplement2; the same book is already requested in harvest-c10#91, so no duplicate. Propagation handbooks and commercial guides state light requirements but controlled photoperiod sources above are more useful; no flood of nursery copies.

Seasonal flora/nursery blooming months and fixed flower lifespan are not daily rhythms. Staminode epidermis/lignification PMC7380458 and papillate organ-identity work PMC1867376 describe morphology/reflectance rather than eyes. Family search returned10.1093/jxb/erad492 morphological/genomic review and general photoreceptor sources; buttercup optics10.1098/rsif.2016.0933 is other genera and reflectance. General ocelli/focusing belongs under nonvisual light by owner10(b), never eye_type. All returned snippets screened; unread full reviews not claimed read.

Aquilegia validation: required screen_candidates.py --check printed **0 problems** before commit. All twelve web steps retained; no pending trait declared exhausted.

### Helianthus continuation, 2026-10-27

Adds **1 genus,1 search,13 wanted,0 evidence**. Worker30 cumulative **3 genera,3 searches,27 wanted,0 evidence/0 measured cells**. Batch cumulative **15 genera,19 searches,130 wanted,0 evidence**; **25 remain**, next Arundo. Aquilegia gate0 problems before commit754145ad.

11 successful connected web queries; worker30 total33. Required aids run and raw cached metadata inspected: run5 supplements12/20 have120 result occurrences,15 family-review titles and124 unique titles/stored abstracts. Every title and available abstract screened; cached abstracts are intrinsically truncated, not full texts. Raw metadata and web1–3 responses in work/harvest-c11. No API/source-page fetch, including prohibited OpenAlex/MDPI/UChicago/SANBI. No quota refusal. Canon catalog checked; no in-hand plant compilation. Global wanted/papers-status checked by genus and all retained title/DOI fragments; no duplicate source identified. Unknown years null; no guessed authors.

Exact queries in executed cached order then live web order:
- `Helianthus phytochrome photoreceptor`
- `Helianthus light perception`
- `Helianthus phototropism`
- `Helianthus volatile signalling`
- `Helianthus photoperiod`
- `Helianthus circadian rhythm`
- `Helianthus epidermal lens cells`
- `Helianthus epidermal focusing leaf optics`
- `Asteraceae photoreceptor review`
- `web: Helianthus seed germination light dark`
- `web: Helianthus germination gibberellin OR smoke OR dormancy`
- `web: Helianthus jasmonate herbivore`
- `web: Helianthus plant ocelli lens epidermal focusing eye`
- `web: sunflower plant ocelli lens epidermal focusing eye`
- `web: Helianthus chemical sensing volatiles`
- `web: sunflower chemical sensing volatiles`
- `web: Helianthus tuberosus photoperiod phototropism light response`
- `web: Jerusalem artichoke photoperiod phototropism light response`
- `web: Asteraceae photoreceptor review`
- `web: Helianthus tuberosus chemical sensing gibberellin jasmonate`

Wanted provenance:
- Influence of photoperiod on vegetation phases and tuber development in topinambour (Helianthus tuberosus L.); http://www.doiserbia.nb.rs/ft.aspx?id=0354-46641201175T. Cached abstract compares 141 accessions in day-length response, flowering/vegetation and tuber number/mass. This targets the species-specific light gap, rather than duplicating measured H.annuus light responses.
- Effects of photoperiod and storage temperature on inulin and fructo-oligosaccharides accumulation in In vitro microtubers of kaentawan (Helianthus tuberosus L.); cached work W2474158865, Journal of Food Science and Agricultural Technology2015. Cached abstract directly compares microtuber induction in16h light/8h dark, complete darkness and8h light/16h dark; long days and darkness produced higher fresh weight than short days. This is living tissue growth under controlled illumination, not food chemistry alone.
- Plant development and hormonal status in the Jerusalem artichoke (Helianthus tuberosus L.); https://www.sciencedirect.com/science/article/pii/092666909290022N. Snippet explicitly reports cultivar-dependent photoperiod sensitivity, long-day leaf/stem growth and delayed stolon/tuber induction. Target the actual controlled photoperiod response; do not infer applied-hormone treatment from the title.
- Existence d'un stimulus photopériodique non spécifique capable de provoquer la tubérisation chez Helianthus tuberosus L.; https://www.tandfonline.com/doi/abs/10.1080/00378941.1965.10838250. Grafting experiments report that interrupting the long night with one hour of weak red light prevents the tuber-forming stimulus. A direct photoperiod manipulation in the unresolved species.
- Studies on the Photoperiodic Responses in Short-Day Plant Helianthus tubevotus; https://www.jipb.net/EN/abstract/abstract24170.shtml. Returned source title spells tubevotus, while abstract explicitly names H.tuberosus white-tuber variety and controlled4–18h daylength treatments. Six to thirteen hours induced flowering and14h or longer retained vegetative growth; verify source spelling/metadata before logging.
- Physiological responses of sun choke’s seedlings under different wavelength LED lighting; https://www.sciencedirect.com/science/article/abs/pii/S0304423821001369. Snippet reports development, morphology and fluorescence of living Jerusalem-artichoke seedlings under natural, fluorescent, red, blue and red/blue LED treatments, with actual irradiances. This directly targets the open species light trait.
- Response of Sunflower (Helianthus annuus L.) Leaf Surface Defenses to Exogenous Methyl Jasmonate; https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0037191&type=printable. Living sunflower accessions received exogenous MeJA to induce herbivore-defense responses. This is the unresolved chemical trait, not repeat light sensing or isolated extract chemistry.
- Effects of methyl jasmonate on plant growth and leaf properties; https://onlinelibrary.wiley.com/doi/full/10.1002/jpln.201700373. Snippet explicitly names living sunflower treated with0–2.5mM MeJA, comparing trichome/stomatal density, cuticle, height and biomass. The hormonal treatment response qualifies under10(d).
- INVESTIGATIONS ON AUXIN-GIBBERELLIN INTERACTION ON THE PHOTOTROPISM OF HELIANTHUS ANNUUS HYPOCOTYL; https://doi.org/10.1093/oxfordjournals.pcp.a078988. Cached abstract explicitly reports applied IAA-gibberellin and IAA-NAA mixtures increasing/decreasing phototropic response compared with IAA-water controls. Read for the applied chemical response; light alone is already measured.
- Programmed Cell Death and Aerenchyma Formation in Water-Logged Sunflower Stems and Its Promotion by Ethylene and ROS; https://www.frontiersin.org/articles/10.3389/fpls.2018.01928/pdf. Cached abstract reports aerenchyma induction by ethylene/ROS and partial suppression with an applied NADPH-oxidase inhibitor. Living seedling chemical-treatment response, not a genomic prediction.
- Stimulated accumulation of lectin mRNA and stress response in Helianthus tuberosus callus by methyl jasmonate; https://pubmed.ncbi.nlm.nih.gov/12951522/. Title explicitly reports an induced response in living callus after methyl-jasmonate treatment. Read to establish treatment and actual stress/lectin response; sequence annotation alone would not qualify. This specifically targets the unresolved tuberosus chemical trait.
- Volatiles of the trap crop sunflowers: Effects on the behaviour of adult female Conogethes punctiferalis moths; https://onlinelibrary.wiley.com/doi/10.1111/jen.13185. Snippet describes headspace collection of sunflower-disk volatiles and olfactometer attraction experiments. Verify that collected flower disks were attached living donors; this is a specific signaling measurement candidate, while harvested-disk chemistry alone fails10(a).

Actual main response records checked: corrected/plant-fungus-slime#65 and recheck2-fixed#1/sweep19#14 support H.annuus light; oa12#20 adds neighbor R:FR directional response; recheck6-fixed#3 supports H.annuus circadian movement. These are preserved, so no repeated model-sunflower light/diel requests or null. Original queue specifically still lacks H.tuberosus light and both species chemical; full species-directed light searches were necessary because nonvisual-light cannot carry at genus level.

Six light leads for H.tuberosus include actual red night interruption, day-length flowering, LED seedling treatments and viable microtuber development. The 2012 accession phenology trial is held as a light lead pending checking experimental/environmental design; no within-day rhythm inferred from June/August flowering dates.2015 microtuber fresh-weight comparison under LD/D/SD is living growth, not storage chemistry alone. The graft trial year remains null because relative search dates conflict with historical DOI year; no date inferred.

Chemical targets use actual applied MeJA, IAA/GA/NAA and ethylene/ROS/inhibitor responses. H.tuberosus callus treatment is specifically held for living tissue induction rather than untested transcript annotation. Trap-crop flower-disk signaling10.1111/jen.13185 still requires attached-living donor verification under10(a). No claim that collection alone proves signaling. Cached2006 light/hormone-level study10.1111/j.1365-3040.2006.01612.x and2000 protandry10.1093/jexbot/51.349.1403 do not establish applied treatment in the truncated abstract; stronger actual intervention sources retained instead.

Roasted/cooked oils, fresh harvested pollen fingerprint, isolated secretory-disk chemistry10.3390/plants13030345 and methanolic extracts10.36948/ijfmr.2026.v08i05.86783 are not established living response. Generic VOC/crop-blue-light reviews name no additional target measurement in available abstracts and are not requested. Vigna, Raphanus, Cucumis, Hopea, Arabidopsis, Pelargonium, Vernonia, Synedrella and Lomatozona studies are distinct genera. Human retinal Tagetes lutein papers and Lens SNP work are eye keyword false matches. General focusing survey and leaf-optics thesis belong under light; owner plant eye none remains. Unmeasured light/diel crop background is not converted into a new request simply because sunflower is mentioned.

Full stored-abstract tail check also found a direct elicitor intervention in the2009 Manitoba thesis MOLECULAR CHARACTERIZATION OF THE INTERACTION BETWEEN HELIANTHUS ANNUUS AND VERTICILLIUM DAHLIAE (W2791459808; http://hdl.handle.net/1993/3838), returned by `Helianthus light perception`: VdNEP was infiltrated into living sunflower plants. Added as a specific chemical-response lead, not generic pathogen sequence prediction. Helianthus now13 wanted (six light, seven chemical). Initial Helianthus gate with12 wanted printed0 problems; repeated after adding this real candidate.

Chenopodium1974 rhythm-lead year normalized to null: the title/index key indicates historical provenance but no explicit usable publication-year field was shown. Historical C.rubrum identity remains pending current taxonomic-scope verification; it is not claimed as a validated C.album/congener measurement. No evidence or legacy records changed.

Final worker30 validation `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c11.jsonl --wanted docs/views/wanted/harvest-c11.jsonl` printed **0 problems** after the thirteenth Helianthus lead. Worker30 final **3 genera,3 search records,27 wanted leads,0 evidence/0 measured cells,33 successful web queries**. Batch cumulative **15 genera,19 searches,130 wanted,0 evidence**. Stop between genera for fresh-context continuation: **25 remain**, resume **Arundo**, then Sorghum onward in exact assignment order. No tool quota refusal or new service refusal. Skipped round-refused OpenAlex/MDPI/UChicago/SANBI throughout; no primary-paper pages fetched. No pending candidate trait called exhausted.
