# harvest-c11 progress

## 2026-10-27 — round 28

This worker and cumulative batch: **3 genera protocol-screened** (Ulmus, Malvaviscus, Carya), **4 search records**, **21 wanted leads**, **0 evidence records**, **0 cells measured closed**. Remaining **37 genera**, next **Pyrus**; then Zizia, Ptelea, Iris, Ricinus, Conopholis, Tropaeolum, Chasmanthium, Paulownia, Chenopodium, Aquilegia, Helianthus, Arundo, Sorghum, Dioscorea, Vinca, Lobelia, Foeniculum, Hypochaeris, Sorghastrum, Packera, Cortaderia, Nasturtium, Tecoma, Cosmos, Achillea, Mahonia, Apocynum, Bromus, Marchantia, Vachellia, Poa, Parkinsonia, Panicum, Artemisia, Polystichum, Ailanthus. Screening is complete for these three even where plausible measurements remain wanted; no wanted trait is called exhausted. Search dispositions are Ulmus diel/eye_type, Malvaviscus eye_type, Carya eye_type.

Read AGENTS.md, the round28 guide, round4-harvest, THOROUGH, BRIEF including Round 2, round3-sweep, desk-screen points 1–10 including plant10(e), and audit 53/54 findings. No app startup, build, server, test or global-state modification. Main's existing sweep-13 Ulmus light/chemical records and old sweep-13/sweep-16 search records remain untouched. Global wanted/status lookup found no duplicates for the new leads. Canon catalog checked: no in-hand plant compilation covering these genera; relevant trait canon DOIs are retained in search records, without pretending source text was read. Owner eye_type decision followed; epidermal focusing is a nonvisual-light topic.

### Sources, queries and boundaries

harvest_get.py and screen_candidates.py explicitly report Ulmus, Malvaviscus and Carya absent from runs 1–17,20,23,24. Thus no harvest queries or candidates were silently omitted. Ulmus direct OpenAlex requests returned all nine queries at per-page=20 (or all results when fewer); titles and the available abstracts were screened. On the first Malvaviscus query, OpenAlex returned **HTTP429**. No later OpenAlex API request was made. Per the source-refusal rule, the complete scientific/common-name pairs and family searches for Malvaviscus and Carya were executed with connected web search; they are recorded as `web:` queries only. The failed API query is not called executed in a search record. Parent was informed of the refusal and continuation through usable web search.

**35 successful connected web queries**: Ulmus11, Malvaviscus12, Carya12. One initial call with an unsupported argument returned an empty tool error and is not counted as successful. No quota refusal from connected web. Search tool returns variable numbers of results; all returned titles/snippets were screened, never claiming twenty where fewer returned. Raw tool responses and direct OpenAlex metadata are scratch files under work/harvest-c11, not committed. No primary-source page fetched or paper text/evidence committed, per desk-screen point3.

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

First two-genera gate: `screen_candidates.py --check` printed **0 problems**. Three-genera gate: **0 problems** before commit. Resume at Pyrus in exact batch order. OpenAlex remains skipped after429; use cached harvest where present and connected web for scientific/common/family protocol. No uncompleted protocol is counted done.
