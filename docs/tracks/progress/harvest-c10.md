# harvest-c10 progress

## 2026-10-27

This worker: 1 complete live-trait screening (Hamamelis), 4 additional genera web-screened with OpenAlex steps blocked (Apios, Nothoscordum, Clematis, Carpinus), 0 evidence, 0 null search records, 43 wanted leads. Cumulative own batch: same. Remaining: Apios/Nothoscordum/Clematis/Carpinus missing API steps blocked and35 untouched genera; next untouched Cocculus. Existing globally covered work preserved. Parent relayed OpenAlex/MDPI HTTP429 source refusals; no subsequent calls to either source.

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

### Clematis (cached harvest + web screened; missing common-name OpenAlex blocked)

Live traits diel, eye_type, sense_chemical, sense_light_nonvisual; target species C. vitalba, C. virginiana and C. terniflora. Global evidence/corrected, searched, wanted and papers-status checked; no existing genus evidence or duplicates of the added leads found. Shared OpenAlex HTTP429 remains in force, no retry. Canon file checked for the4 traits; plant relevant compilations are not in hand. No null or evidence records written.

Successful harvest queries copied in order (run4, supplements12/14/20):
- `Clematis phytochrome photoreceptor`
- `Clematis light perception`
- `Clematis phototropism`
- `Clematis flower opening time`
- `Clematis nyctinasty`
- `Clematis volatile signalling`
- `Clematis photoperiod`
- `Clematis circadian rhythm`
- `Clematis anthesis`
- `Clematis pollination biology`
- `Clematis epidermal lens cells`
- `Clematis epidermal focusing leaf optics`

All145 unique returned titles screened. Genus-named plausible sources' available abstract starts read explicitly. Other sources include Arabidopsis, tomato, pepper, kratom, lettuce, insects, human pharmacology, furniture/light projection and mathematical models, which provide no named Clematis measurement in their available title/abstract. Generic760-species light meta-analysis and plant-light reviews may contain genus tables beyond their abstracts; no negative claim made for them. Harvest citation step citing10.1093/oxfordjournals.aob.a087596 returned10.1111/j.1095-8339.2009.01017.x (Floral development in Anemoneae): organ development, not eye or chemical/light response; other chases10.1016/s0031-9422(02)00119-x and10.1111/j.1469-8137.2010.03317.x returned0. Cached family review `Ranunculaceae photoreceptor review` titles/available abstract starts read, dominated by pollinator colour, Anemone/Papaver and broad light reviews. No named Clematis eye measurement in returned abstracts.

Exact web queries:
- `web: Clematis seed germination light dark`
- `web: Clematis germination gibberellin OR smoke OR dormancy`
- `web: Clematis floral scent volatiles`
- `web: Clematis flower opening time anthesis`
- `web: clematis flower opening time anthesis`
- `web: Clematis epidermal lens cells eye type`
- `web: clematis epidermal lens cells eye type`
- `web: Clematis photoperiod light perception phototropism`
- `web: virgin's bower photoperiod light perception phototropism`
- `web: Clematis chemical perception volatile signalling`
- `web: virgin's bower chemical perception volatile signalling`
- `web: virgin's bower flower opening time anthesis`
- `web: virgin's bower epidermal lens cells eye type`

Scientific/common pairs use Clematis/virgin's bower; redundant case-only clematis pairs were sent before resolving the common name and are retained above as actually executed. All returned result titles and snippets screened; no claim that20 results were delivered for each combined query. Primary sources and legal repositories listed in wanted provide bibliographic/snippet provenance. No DOI inferred from article-number patterns. Unknown metadata stays empty/0.

Added 23 wanted leads: sixteen harvest experiments and seven web leads, less any cross-unit duplicate removed immediately before append. Harvest covers hormone effects on flowering, BAP/TDZ explant regeneration, PEG seed germination, floral volatiles, shade/irradiance, UV-B, photoperiod and rooting hormones. Web germination leads explicitly include light/dark and GA3 for C. dilatata, GA response across six Korean species, GA3 for C. hirsutissima, darkness/KNO3 in C. vitalba, GA/chilling in C. vitalba, and C. integrifolia seed pretreatments. New2023 dynamic-headspace scent comparison also wanted. Positive leads block chemical/light exhaustion.

Diel candidates screened cautiously: hormone/flower-opening-duration experiment retained; W2278388607 is a photograph labelled flower at anthesis, not hour-of-day data; W2618719354 is C. udayanii taxonomic morphology and post-anthesis anther position; Arabidopsis diurnal regulation, human green-wall perceptions and honeybee olfactory circadian study concern other organisms. Web flowering pages give seasonal pruning/bloom periods without daily hours. No diel null while missing steps blocked. Eye candidates are insect colour review and pollinator perception of green flowers; epidermal micromorphology study (PMC11397135/PubMed39282113) describes stomata, trichomes and cell walls, no optical focusing in snippet. No eye_type null while protocol incomplete. Owner's none reading preserved.

Excluded chemistry includes cut-stem blockage, preservatives/sugar in cut Clematis flowers, C. flammula essential-oil pharmacology, extracted C. wightiana antioxidants, mouthwash/animal carcinoma studies and stem/root volatile-composition studies: these do not demonstrate a living-plant chemical response under10(a). Nectar-yeast and e-nose sampling boundaries are explicitly flagged on wanted entries for the reader; no measurements assumed.

No paper fetched or evidence logged, per desk-screen5. OpenAlex missing common-name steps remain incomplete. Clean next untouched genus: Carpinus, then Cocculus, Sagittaria. All later batch genera remain untouched in this worker.

### Carpinus (cached scientific harvest + all required web; common-name OpenAlex blocked)

Live open trait sense_chemical only. Existing other-trait global coverage preserved; no duplicate nulls. Corrected/evidence, wanted, searched and owner status checked before screening; existing10.1016/j.scitotenv.2024.177358 on replant-1 wanted retained without duplication. Its abstract explicitly reports living ozone exposure and stomatal light responses in Carpinus/Ostrya; follow existing lead rather than request again. Canon chemical compilations10.1016/j.tree.2009.09.010 and10.1111/ele.12205 checked; neither is in hand.

Exact successful harvest queries (run2, supplement14):
- `Carpinus phytochrome photoreceptor`
- `Carpinus light perception`
- `Carpinus phototropism`
- `Carpinus volatile signalling`

Citation steps citing10.1016/j.tree.2009.09.010,10.1093/treephys/26.8.1013 and10.2478/foecol-2023-0013 each return0 Carpinus works. Cached family `Betulaceae photoreceptor review` titles screened: mainly tree phenology, Alnus/Betula light studies, insects, pollinator colour, and a Carpinus light-intensity/endogenous-hormone experiment (light response already outside live trait). No chemical null is written; broad reviews remain unresolved beyond available abstracts.

Exact web queries:
- `web: Carpinus seed germination light dark`
- `web: Carpinus germination gibberellin OR smoke OR dormancy`
- `web: Carpinus jasmonate herbivore`
- `web: Carpinus chemical perception volatile signalling`
- `web: hornbeam chemical perception volatile signalling`

Screened all returned web titles/snippets and all cached harvest titles, with genus response abstracts read explicitly. Added 9 wanted leads:2 cached living-chemical experiments (methyl jasmonate induction and NO2 response/recovery) and7 germination/dormancy studies, including GA-treated Carpinus laxiflora, a two-Carpinus GA pretreatment study, and species C. cordata, C. caucasica, C. orientalis and C. viminea. Unknown publication years/DOIs/authors left0/empty. Repository date2022 for branch-localized induction is kept as the observed harvest metadata, with source-year uncertainty explicitly on the wanted line; PubMed33180276 independently gives same title and methyl-jasmonate experimental method.

Dispositions:10.3389/fmicb.2019.01110 describes the phyllomicrobiome, not a measured plant receptor response in its available abstract. Truffle aroma concerns fungi; Schinus fruit-extract anticancer study is other genus/tissue chemistry; grapevine disease-volatiles work not Carpinus. Root-volatiles/cockchafer thesis and broad forest-VOC reviews do not name a Carpinus measurement in title/available abstract; no negative conclusion beyond that.10.1111/nph.14671 web meta-analysis mentions isolating hexenal from600kg of removed hornbeam leaves, excluded as tissue chemistry under10(a), not plant-signal evidence. USDA Silvics Carpinus caroliniana page mentions improved germination after GA; source is a review of prior studies, retained here as a citation trail (https://www.srs.fs.usda.gov/pubs/misc/ag_654/volume_2/carpinus/caroliniana.htm), not a duplicate needed to block the chemical null already held by direct experiments. USDA Woody Plant Seed Manual has germination table5 for Carpinus; not reopened or extracted.

No OpenAlex retry after shared429. Missing common-name API steps remain blocked; no complete-protocol claim. No paper fetched, no evidence or null records written. Clean handover at next untouched genus Cocculus;35 untouched genera remain through Sideroxylon. Scratch raw searches and cache in work/; committed note contains exact provenance, no full text.

### This-worker handover counts and checks

Five genera received screening: Hamamelis complete for its live chemical trait before the refusal; Apios, Nothoscordum, Clematis and Carpinus retain explicitly blocked OpenAlex steps and are not claimed full protocols. Own cumulative/this-worker outputs43 wanted lines,0 null records,0 evidence. Missing API steps must be repaired when service is usable; do not repeat completed web searches or duplicate these wanted leads. Next unstarted genus Cocculus, then Sagittaria and Richardia;35 unstarted genera remain. Source refusals relayed by parent: OpenAlex HTTP429 and direct MDPI HTTP429; no subsequent calls to either. Web search remained usable (56 actual queries across these5 genera); no search refused. Gate printed0 problems for each committed chunk and is rerun before final commit.
