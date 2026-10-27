# harvest-c10 progress

## 2026-10-27

This worker: 1 complete live-trait screening (Hamamelis), 2 additional genera web-screened with OpenAlex steps blocked (Apios, Nothoscordum), 0 evidence, 0 null search records, 11 wanted leads. Cumulative own batch: same. Remaining: Apios/Nothoscordum missing API steps blocked and37 untouched genera; next untouched Clematis. Existing globally covered work preserved; no source refusals.

Read AGENTS.md, round28 worker guide, round4-harvest.md, THOROUGH.md, BRIEF Round2 and record rules, round3-sweep.md, desk-screen1–10 including10(e); audit53/54 fault summaries. No evidence written per desk-screen5. Canon file checked; chemical compilations 10.1016/j.tree.2009.09.010 and10.1111/ele.12205 are not in hand. Corrected/evidence, searched, wanted and owner status searched for Hamamelis; no duplicate of the three leads found. The harvest live target has only sense_chemical open; the original gap queue lists four traits and older global searches cover the other three. Those records are untouched. Extra web pairs for those three were run before resolving this live-target difference and are listed honestly below.

### Hamamelis

Harvest_get and screen_candidates output screened; own scratch cache holds all titles and abstract starts. Harvest run2 plus supplement15. Exact harvest query order: `Hamamelis phytochrome photoreceptor`; `Hamamelis light perception`; `Hamamelis phototropism`; `Hamamelis volatile signalling`. Citation steps citing10.1086/336744 and10.1093/oxfordjournals.aob.a086894 each returned0 Hamamelis works. Family review `Hamamelidaceae photoreceptor review` returned8; screened all titles. Pinguicula, Distylium, Pteridaceae, tree ferns and buckwheat are other genera. Major Flower Pigments concerns pollinator colour signals. Acetylcholine review has no abstract or named Hamamelis response, retained as background rather than a confirmed species lead; eye-disease review concerns medicinal extracts.

Missing OpenAlex common-name step: `witch hazel volatile signalling`, HTTP200, first20 titles and available abstracts screened. Hamamelis results concern cultivar identification (10.21273/hortsci.31.4.615d) or medicinal bark extracts acting on human cells (10.3390/ijms23169279,10.3390/antiox11061119); these do not measure living plant chemical responses. Other results concern apple, melon, broccoli, pepper, carnation, tea, blueberry, analytical chemistry or human flavour perception. No additional Hamamelis living-response lead.

All11 chemical keyword candidates in screen_candidates were excluded by measured organism:10.21273/hortsci.31.4.644d mango taste panel; .605a apple cuticle; .643e muskmelon; .643f analytical sampling; .640d strawberry postharvest fumigation;10.1111/j.1438-8677.2009.00284.x poplar review;10.21273/hortsci.31.4.639a apple aroma; .638f Fuji apple; .635e broccoli; W2944007483 Xerophyta; .678c pepper/fungal response. All other harvest titles screened as well, which revealed the two Hamamelis IBA/growth-regulator experiments absent from the keyword candidates. Both are wanted and block a chemical null.

Exact web queries (titles and snippets returned by the search tool screened; combined calls do not guarantee20 results for every query):
- `web: Hamamelis seed germination light dark`
- `web: Hamamelis germination gibberellin OR smoke OR dormancy`
- `web: Hamamelis floral scent volatiles`
- `web: Hamamelis flower opening time anthesis`
- `web: witch hazel flower opening time anthesis`
- `web: Hamamelis epidermal lens cells eye type`
- `web: witch hazel epidermal lens cells eye type`
- `web: Hamamelis photoperiod light perception phototropism`
- `web: witch hazel photoperiod light perception phototropism`
- `web: Hamamelis chemical perception volatile signal`
- `web: witch hazel chemical perception volatile signal`

Web provenance: germination query returns INIST record8535850, title `Hamamelis seed germination`, keywords dormancy/cooling/heat; wanted under10(e), unknown bibliographic fields empty/0. USDA Woody Plant Seed Manual and horticultural sites describe stratification, not confirmed light or chemical trials. Floral/chemical queries return PubMed17253239 (`Study on the composition of the volatile fraction of Hamamelis virginiana`): water-distilled leaf/bark material, excluded under10(a). EMA report likewise discusses distilled fractions. Miller Library and horticultural scent pages give fragrance descriptions rather than measured living-plant response. Anthesis pair returns10.3732/ajb.89.1.67 and seasonal flowering pages; snippet reports developmental phenological stages and autumn/spring dates without a daily hour, not treated as a new daily-timing measurement. Eye pair returns animal/human histology and no Hamamelis eye; plant eye_type follows owner's none reading. No paper fetched or logged as evidence.

Gate: screen_candidates --check with own searched and wanted printed0 problems on27 October2026 before commit. Next: Apios, Nothoscordum, Clematis. Scratch raw API and web responses kept only in work/, no paper text committed.

### Apios (web complete, OpenAlex blocked; no exhaustion claim)

Harvest_get reports in no harvest run; screen_candidates likewise has no harvest genus. Original queue lists diel, eye_type, sense_chemical and sense_light_nonvisual. Prior sweep-40 search preserved. Global main evidence, corrected evidence, wanted, searched and status checked; no existing Apios measurement or duplicate of these4 wanted leads found. Canon candidates for the four traits checked; plant light/chemical compilations remain not in hand;10.3389/fpls.2015.00207 is the nearest-light source in the old queue.

Parent reported an actual shared-round OpenAlex HTTP429; per source-refusal rule no further OpenAlex requests. Missing scientific/common OpenAlex searches cannot be claimed executed. Therefore no new null search records, even for eye/diel, and no full-protocol completion claim. All returned web result titles/snippets screened, with no claim that the tool returned20 per query. First unquoted pairs often returned Arachis peanut or Vigna Bambara groundnut, which are not Apios; refined quoted scientific/common names rather than importing those measurements.

Exact queries:
- `web: Apios seed germination light dark`
- `web: Apios germination gibberellin OR smoke OR dormancy`
- `web: Apios floral scent volatiles`
- `web: Apios flower opening time anthesis`
- `web: American groundnut flower opening time anthesis`
- `web: Apios epidermal lens cells eye type`
- `web: American groundnut epidermal lens cells eye type`
- `web: Apios photoperiod light perception phototropism`
- `web: American groundnut photoperiod light perception phototropism`
- `web: Apios chemical perception volatile signalling`
- `web: American groundnut chemical perception volatile signalling`
- `web: "Apios" photoperiod`
- `web: "Apios" flower opening time anthesis`
- `web: "Apios" seed germination light dark`
- `web: Fabaceae photoreceptor review`
- `web: "Apios" germination gibberellin dormancy`
- `web: "Apios" "In Vitro Propagation"`
- `web: "American groundnut" photoperiod`

Family/review step: `Fabaceae photoreceptor review` returned10.1093/jxb/erag313, Beyond the CO–FT regulatory module: E1 and PHYA emerge as players in photoperiodic regulation of flowering in legumes; snippet discusses alfalfa, clover, pea, common bean, soybean, cowpea and pigeon pea, no named Apios experiment. No family carry is inferred.

Provenance/dispositions: PubMed26521814 and J-STAGE64_ess15132, Evaluation of the Key Odorants in Volatile Oils from Tubers of Apios americana, concern oils from removed tuber tissue, excluded under10(a); no floral emission signal. DOI10.1360/aps050016, Systematic significance of leaf epidermal features in Apios and Cochlianthus, describes cell shapes, anticlinal walls and wax ornamentation, no focusing or eye measurement. Anthesis results mostly Arachis/Vigna or flowering seasons at Michigan CLIMBERS/RHS; no Apios hour of opening found in returned snippets. Propagation refinements found3 real regulator/explant-response studies, wanted; Darwin book snippet reports heliotropism in Apios, wanted. FWS930210 recovery-plan snippet mentions small germination tests in A. priceana without light/hormone treatment, noted as background and not evidence. No forbidden site was opened; a ResearchGate search listing was encountered only. No paper fetched or measured value logged.

Apios wanted-only leads do not certify completion while API steps are blocked. Next: Nothoscordum, Clematis, Carpinus.

### Nothoscordum (cached scientific harvest and web screened; common-name OpenAlex blocked)

Harvest run6, supplements14 and20, plus cached Amaryllidaceae family review screened. All unique harvest result titles and all genus-relevant abstract starts reviewed, not only keyword candidates. Original/live open traits diel, eye_type and sense_chemical. Main holds sense_light_nonvisual (sweep-27 for N. bivalve), preserved with no duplicate search. Global evidence/corrected, wanted and status checked; no duplicate of the4 leads found. Canon eye/diel/chemical list checked; only plant chemical compilations are relevant background and are not in hand.

Exact successful harvest query order:
- `Nothoscordum phytochrome photoreceptor`
- `Nothoscordum light perception`
- `Nothoscordum phototropism`
- `Nothoscordum flower opening time`
- `Nothoscordum nyctinasty`
- `Nothoscordum anthesis`
- `Nothoscordum pollination biology`
- `Nothoscordum volatile signalling`
- `Nothoscordum epidermal lens cells`
- `Nothoscordum epidermal focusing leaf optics`

Citation step citing10.1656/045.023.0309 returned0 works naming the genus. Cached family query `Amaryllidaceae photoreceptor review` screened15 returned titles/abstract starts (n82). Crinum pollination, Zephyranthes germination, tomato, microgreens and Narcissus are other genera; broader metabolite/light reviews hold no named Nothoscordum measurement in available abstracts. Lepidopteran-eye review concerns insects.

Exact web queries (all returned titles/snippets screened, no20-per-query guarantee):
- `web: Nothoscordum seed germination light dark`
- `web: Nothoscordum germination gibberellin OR smoke OR dormancy`
- `web: Nothoscordum floral scent volatiles`
- `web: Nothoscordum flower opening time anthesis`
- `web: false garlic flower opening time anthesis`
- `web: Nothoscordum epidermal lens cells eye type`
- `web: false garlic epidermal lens cells eye type`
- `web: Nothoscordum chemical perception volatile signalling`
- `web: false garlic chemical perception volatile signalling`

Sources/dispositions:10.26786/1920-7603(2020)585 scented living N. bivalve flowers, wanted.10.54985/peeref.2501p8798703 samples living Nothoscordum volatiles, wanted; web poster listing also mentions nocturnal Inodorum flowers, so daily timing remains unresolved. Primary Castanea life-cycle study (Baskin and Baskin1979) and UnB germination thesis notice are wanted under10(e). INIST-style unknown metadata not invented;0/empty denotes unknown. The doctoral notice's title was returned verbatim, author and year were not established.

Keyword candidate W7217718689 (Introducción al estudio fitofenológico de los pastizales de la depresión del Salado) describes seasonal phases over1974–1976, not daily anthesis.10.1093/botlinnean/boae066 is Crinum, not Nothoscordum.10.1007/s00359-025-01751-8 is lepidopteran eye structure, not plant eye.10.13128/caryologia-670 is Zephyranthes megagametophytes, not Nothoscordum chemical sensing.10.4236/aim.2018.85028 tests extracted N. bivalve material against bacteria, excluded under10(a). Taxonomic/cytology papers describe morphology, ITS and plastomes rather than chemical/light response.1952 endopolyploidy paper10.1080/00087114.1952.10797537 uses sodium2,4-D on monocot roots but its available abstract names no Nothoscordum; unresolved species relevance, no chemical null written. Web eye results were mostly animal/human histology; false-garlic common-name searches returned Allium chemistry and breeding, not Nothoscordum. Botanical descriptions of no garlic odour are not signal-emission experiments.

Missing common-name OpenAlex queries not executed because parent reported actual HTTP429 earlier this round. No new nulls, including eye_type, until missing protocol steps can be repaired. No evidence or paper text committed. Next untouched genus: Clematis.
