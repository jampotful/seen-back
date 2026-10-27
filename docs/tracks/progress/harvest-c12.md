# harvest-c12

## 2026-10-27 — round 28 checkpoint

This worker: 1/40 genera desk-screened (Equisetum), 0 partially screened, 2 search records, 6 new wanted lines, 0 evidence records. Cumulative: the same; there was no prior harvest-c12 progress/searched/wanted file. No cells closed by measurement; two null traits have completed available-source desk screening. Remaining:39; first incomplete Cardamine in the original batch order.

Read AGENTS.md first, the round28 worker guide, round4-harvest, THOROUGH, BRIEF (including Round2), round3-sweep and desk-screen points1–10 including plant10(e). Harvest_get printed Equisetum “in no harvest run yet”; screen_candidates printed “not in the harvest”. Checked global evidence, searched, wanted and papers-status. Existing oa-9 evidence already covers sense_chemical (antheridiogen responses), so no chemical null or duplicate wanted for that paper. Old sweep-3 search is thin and remains untouched. No canon relevant to Equisetum was marked in_hand; plant canon checked in canon.jsonl and no new canon wanted line added.

Ten web queries ran, in this exact order (first20 titles/snippets where returned; no result page/full text fetched):
- `web: Equisetum seed germination light dark`
- `web: Equisetum germination gibberellin OR smoke OR dormancy`
- `web: Equisetum jasmonate herbivore`
- `web: Equisetum light photoperiod phototropism`
- `web: horsetail light photoperiod phototropism`
- `web: Equisetum flower opening time anthesis`
- `web: horsetail flower opening time anthesis`
- `web: Equisetum eye type epidermal focusing`
- `web: horsetail eye type epidermal focusing`

- `web: Equisetaceae photoreceptor review`

Useful results and dispositions: the six titled works in wanted/harvest-c12.jsonl are unread candidates, not evidence. No duplicate source title/DOI was found in existing wanted or papers-status. Germination lead 10.3389/fpls.2015.00441 was retained under10(e). Guillon2003 light-level sex expression, Nakatani/Noguchi1996 photoperiod growth, the blue-light stomatal paper, low-light field horsetail growth and Thompson’s thesis all concern possible light responses; none licenses an eye_type measurement. Stomatal ultrastructure, fossil epidermal anatomy, silica microprobe papers, botanical identification profiles and medical use of extracts under the eye searches do not measure image-forming eyes. Plant eye_type follows the owner’s “none” reading; no focusing lead was found. Anthesis searches mainly returned botanical descriptions of spore-bearing, nonflowering horsetails and flowering papers on other taxa; seasonal spore dates and daylength growth treatments do not establish a daily activity class. The diel null was written after the family query completed and the parent authorized available-source web screening in place of refused OpenAlex steps.

Source limitation: OpenAlex HTTP429 on the first missing-step query `Equisetum light photoperiod phototropism`, URL https://api.openalex.org/works?search=Equisetum+light+photoperiod+phototropism&per-page=20 (network enabled). Three concurrent requests launched; aborted on first refusal with no usable responses saved. Source skipped rest of round. Parent directed continuation through available web sources, and accurate scientific/common-name paired web searches plus family review satisfy available-source screening. OpenAlex queries are not represented as executed successes. Family query `Equisetaceae photoreceptor review` returned general plant reviews including Li/Mathews2016 (canon); no family-specific review or eye/diel measurement was identified in returned titles/snippets. Chased is consequently “none: no measured relative and no family review found”, with places searched named. Two null records cover eye_type/diel only; light is held for the six wanted works; chemical already has evidence. All title/snippet provenance and exact queries retained. Unknown metadata remains empty/null. The blue-light landing page’s kiaf238 identifier was not assumed a DOI because results also showed a kiaf298 PDF.

Next: Cardamine, then Rumex in original order. Do not repeat Equisetum’s completed available-source desk searches. No evidence logged under desk-screen point5; no paper full text committed.

### Cardamine checkpoint

This worker and cumulative totals now:2/40 genera screened;2 search records (Equisetum only);15 wanted lines (6 Equisetum,9 Cardamine);0 evidence records. Next first incomplete: Rumex;38 genera remain. No plant measurements extracted.

Cardamine harvest run2’s current open trait is sense_chemical. Existing global eye_type/diel screenings remain untouched; main oa-10 and oa-12 already report Cardamine light response, so no light null or duplicate shade paper wanted. All cached harvest titles and stored abstracts were read, including supplemental chemical query and the15 family-review results. The earlier failed `Cardamine volatile signalling` was repaired by the later same-word supplementary query; only that successful query is listed once below. No live OpenAlex retry.

Cached successful queries, exact order: `Cardamine phytochrome photoreceptor`; `Cardamine light perception`; `Cardamine phototropism`; `Cardamine volatile signalling`; family `Brassicaceae photoreceptor review`. No failed query is represented as successful. The family-review list includes phytochrome flower responses10.3732/ajb.89.2.230 and Translating Flowering Time10.3390/plants7040111; broad photoreceptor/microgreen papers add no direct Cardamine chemical measurement in their printed metadata.

Web queries (first20 returned titles/snippets where available):
- `web: Cardamine seed germination light dark`
- `web: Cardamine germination gibberellin OR smoke OR dormancy`
- `web: Cardamine floral scent volatiles`
- `web: Cardamine volatile emission herbivore induced response methyl jasmonate`
- `web: bittercress volatile emission herbivore induced response methyl jasmonate`
- `web: Cardamine flower opening time anthesis`
- `web: bittercress flower opening time anthesis`
- `web: Cardamine eye type epidermal focusing`
- `web: bittercress eye type epidermal focusing`

Nine new wanted leads preserve actual titles and DOI metadata from the cache or search snippets. The two JA experiments and phytohormone induction paper directly concern the owner’s chemical-response reading. DOF/GA germination and C.impatiens dormancy cycling are retained under10(e). Selenite/selenate response experiments remain candidate living chemical responses, pending separation from simple accumulation/speciation. Flagellin functional assay requires confirmation of Cardamine species representation. There is no chemical null while these leads wait.

Other candidate dispositions:10.1111/tpj.16699 is nuclear autofluorescence imaging, not living chemical sensing;10.1002/mnfr.201700990 concerns human taste/flavor;10.30574/wjbphs.2026.27.2.0428 is botanical-name etymology. Extract antidiabetes/anti-inflammatory work (10.1021/acsomega.3c01034;10.3389/fchem.2022.1077581), animal feeding10.3389/fnut.2022.996932, and detached-tissue metabolite/speciation papers (10.1039/d0mt00216j;10.3390/metabo12111024;10.3390/agronomy13112760;10.54598/000340) do not alone meet chemical-response10(a). New genome10.1038/s41421-021-00286-x and rhizosphere-strain10.1155/2014/108562 abstracts do not identify a direct plant cue-response assay beyond the other retained response studies. No paper text fetched.

Additional paired eye/diel web searches returned botanical identification and seasonal phenology, and two observational diel leads: Pennsylvania flora says C.concatenata opens on warm sunny days (https://www.paenflowered.org/apgii/brassicales/brassicaceae/cardamine/cardamine-concatenata); UCANR says C.californica closes petals in late afternoon (https://ucanr.edu/blog/coastal-gardener/article/cardamine-edible-not-so-tasty). These are secondary descriptions, not extracted measurements. Existing globally completed eye/diel records are preserved, and no new null is added for these traits.

### Rumex and handoff checkpoint

This worker/cumulative:3/40 genera screened (Equisetum, Cardamine, Rumex);2 null search records;17 new wanted lines;0 evidence/measurement closures. Remaining37, first incomplete Centaurea. The batch continues in its original order after Centaurea. Stop is between genera for fresh-context handoff; no tool web-limit rejection occurred. OpenAlex remains skipped after HTTP429; no retry was made.

Rumex current harvest traits were diel, sense_chemical and sense_light_nonvisual; main already has the latter two (oa-13b and sweep-6). Existing plant-1 eye_type fully screened record remains unchanged. The family review and all cached title metadata were screened, together with stored abstracts for plausible diel sources. No new null is appropriate: two new diel candidates are in harvest-c12 wanted; existing plant-1 also has10.1139/b74-282 and10.1139/cjb-2014-0123. Existing chemical/light evidence and wanted are preserved without duplication.

Successful cached queries, exact order:
- `Rumex phytochrome photoreceptor`
- `Rumex light perception`
- `Rumex phototropism`
- `Rumex flower opening time`
- `Rumex nyctinasty`
- `Rumex volatile signalling`
- `Rumex photoperiod`
- `Rumex circadian rhythm`
- `Rumex anthesis`
- `Rumex pollination biology`
- `Polygonaceae photoreceptor review`
The failed initial run’s genus queries were superseded by successful later runs; they are not represented as failed executed search successes. Cached citation steps cite10.3390/plants11233212 (zero hits) and10.1007/BF00393317 (eight listed hits), and the Polygonaceae family-review list was screened. No live OpenAlex call was attempted for Rumex.

Web queries, exact order:
- `web: Rumex seed germination light dark`
- `web: Rumex germination gibberellin OR smoke OR dormancy`
- `web: Rumex floral scent volatiles`
- `web: Rumex flower opening time anthesis`
- `web: dock sorrel flower opening time anthesis`
- `web: Rumex eye type epidermal focusing`
- `web: dock sorrel eye type epidermal focusing`

The first two queries exposed many light/GA/ethephon germination studies, including existing main evidence10.1155/2015/170176 and existing wanted10.1111/j.1438-8677.1992.tb01340.x. Main already reports red/far-red germination and nitrate response in this genus, so these were not falsely screened as absent or redundantly requested. The third query’s living-herbivory VOC paper is consistent with existing oa-13b chemical evidence; dietary extracted volatiles/essential oils do not alone count10(a).

Diel candidates screened without a null claim: Sorghum/Arabidopsis circadian ethylene studies, rose opening studies, Pseudoplusia larval diet papers, mosquito rhythms, human circulatory/skin studies, Tillandsia epithelium, wheat nitrogen and azalea hormone studies do not measure Rumex daily activity. Rumex leaf/flower removal and seed-maturity studies measure seed development/seasonal phenology; their anthesis word alone is not a daily-opening measurement. RP-ACS1 rhythmic ethylene and R.acetosa flower longevity/opening-count studies remain plausible and are wanted. Common-name sorrel search results about Hibiscus sabdariffa are a different genus and were excluded. Botanical Rumex anatomy, pollen, plant identification and seasonal flowering profiles under eye/diel queries do not report image-forming eyes or a daily opening time. No optical focusing source was found. The existing global eye_type screening is preserved.

Validation history: the Equisetum checkpoint checker returned0 before its commit. At Cardamine, the checker was started before commit but its0-problems result arrived after commit13b269d3 (sequencing mistake); it found0 problems and the final combined checkpoint is checked again to completion before its commit. No failed validation was bypassed. No app tests/builds/servers run.

Final combined validation returned `0 problems` before the handoff commit; cross-file wanted DOI/title scan found no duplicates. This worker used26 web protocol queries total (10 Equisetum,9 Cardamine,7 Rumex); raw tool results are available in work/harvest-c12 for local takeover, outside committed deliverables.

## 2026-10-27 — worker13 Centaurea continuation

This worker:1 genus screened (Centaurea),1 null search record,16 new wanted lines,0 evidence/measurement closures. Cumulative:4/40 genera screened (Equisetum, Cardamine, Rumex, Centaurea),3 null search records,33 wanted lines,0 evidence. Remaining36, next Ratibida. Preserve completed Cardamine/Rumex screening even though wanted-only outcomes remain in the raw queue.

Read AGENTS.md and all round28/round4/THOROUGH/BRIEF/round3/desk-screen protocols, including10(e). Runtime network policy inspected through the cloud environment skill: unrestricted and enforced; no VPN configured. OpenAlex429,MDPI429,UChicago403 and SANBI403 remain source skips with no direct requests or API retries. No paper/source pages fetched. harvest_get and screen_candidates report Centaurea absent from every available cached harvest run (1–17,20,23,24). The independent Asteraceae cached family review was read:15 titles and all stored abstracts, successful query `Asteraceae photoreceptor review`. No genus API query was run or represented as successful. Global normal/corrected evidence, searched, wanted and papers-status were checked; no existing Centaurea evidence found, and the thin sweep-5 record stays untouched. Canon review found no plant compilation marked in hand for these traits; no extra canon requests written.

Exact web queries, in execution order, with first20 titles/snippets where returned (some queries return fewer):
- `web: Centaurea seed germination light dark`
- `web: Centaurea germination gibberellin OR smoke OR dormancy`
- `web: Centaurea floral scent volatiles`
- `web: Centaurea light photoperiod phototropism`
- `web: knapweed light photoperiod phototropism`
- `web: Asteraceae photoreceptor review`
- `web: Centaurea volatile emission herbivore induced response methyl jasmonate`
- `web: knapweed volatile emission herbivore induced response methyl jasmonate`
- `web: Centaurea flower opening time anthesis`
- `web: knapweed flower opening time anthesis`
- `web: Centaurea eye type epidermal focusing`
- `web: knapweed eye type epidermal focusing`

Results and dispositions:16 actual titled candidates and source URLs are saved in wanted, with unknown authors/years/DOIs left empty or null. The moncktonii, hermannii, iberica, cyanus, endemic Phalolepis, solstitialis and nigra germination leads follow10(e); even neutral/no-effect light treatments remain measurements to inspect. The23-species seed-treatment candidate requires species-table confirmation. NASA20170010193 retains the yellow-starthistle daylength/irradiance lead;20160013415 appears related and was not requested separately. Photoperiodic After-Effects10.1086/335088 and the Auburn table12 specifically name C.cyanus/C.montana. The historically named C.repens Russian-knapweed light study was not used to carry a result to current Centaurea species (the result also identifies Acroptilon repens). The neighbor-identity MeJA study is a direct chemical-response lead; in-situ volatile collection and damaged-leaf emission papers require intact-plant/species/signalling confirmation. The secretory petal study remains a candidate pending distinction of living floral scent from extracted tissue chemistry. Distilled essential-oil composition of capitula (including S0305197818305878,ffj.1585 and essential oils of atropurpurea/orientalis/kilaea/cuneifolia) alone does not establish a living response under10(a). ResearchGate results were not opened or used as source records.

Diel is held, with no null: already wanted10.1002/ajb2.16179 in harvest-c6 is titled “Pollinator visitation closely tracks diurnal patterns in pollen release”; the returned AJB snippet explicitly names Centaurea jacea and a daily pollen/flowering schedule. Do not duplicate that global wanted source. Flowerhead lifespan, seedhead reopening after drying, seasonal bloom months, cut-flower harvest stages and degree-days to anthesis in the other results are not daily opening measurements. The Centaurea lydia phenology result lacked a daily-clock statement and full title; no daily result was inferred. Botanical identification/anatomical and medicinal-organ microscopy sources report no image-forming eyes. Eye searches found no optical focusing work; eye_type null follows owner10(b), with relevant anatomical/retinal-nutrition false positives named in screened.

Cached family review10.3390/plants7040111 supplies the review chase; other15-result-family entries concern Kansas shade responses, Vernonia, Pelargonium, Synedrella, Lomatozona, Gerbera, human retinal-cell nutrition, butterfly/beetle visitors, broad secondary metabolism, genetic assimilation and blue-light reviews. None of their printed metadata reports Centaurea eyes or displaces the retained light/chemical/diel candidates. Available-source family web search returned broad photoreceptor reviews (including canon Li/Mathews2016), not a new Centaurea eye measurement. Raw tool responses are saved locally in work/harvest-c12/Centaurea-web1–4-worker13.json; no full text committed.

Next:Ratibida, then Fraxinus, then Adiantum, in original batch order.

Worker13 Centaurea checkpoint validator completed before commit: `0 problems`.

## 2026-10-27 — worker13 Ratibida and handoff checkpoint

This worker total:2 genera screened (Centaurea, Ratibida),2 null search records,17 new wanted lines,0 evidence/measurement closures,23 web protocol queries. Cumulative:5/40 genera screened (Equisetum, Cardamine, Rumex, Centaurea, Ratibida),4 null search records,34 wanted lines,0 evidence. Remaining35, next Fraxinus, then Adiantum, then Botrypus. Stop is between genera for fresh-context takeover. No web usage-limit refusal occurred.

Ratibida harvest_get and screen_candidates report no genus in any cached harvest run1–17,20,23,24. No failed/unrun API step is claimed. The successful cached `Asteraceae photoreceptor review`15-result titles and stored abstracts already read for Centaurea supply this genus's family step;10.3390/plants7040111 is the review chase. No live OpenAlex or blocked-source retry. Global normal/corrected evidence, wanted, searched and papers-status checked; no Ratibida evidence or wanted sources found, thin sweep-15 stays intact. Canon checked as for Centaurea; no relevant plant compilation in hand and no new canon wanted.

Eleven Ratibida web queries, exact order (first20 returned titles/snippets where available):
- `web: Ratibida seed germination light dark`
- `web: Ratibida germination gibberellin OR smoke OR dormancy`
- `web: Ratibida floral scent volatiles`
- `web: Ratibida light photoperiod phototropism`
- `web: prairie coneflower light photoperiod phototropism`
- `web: Ratibida volatile emission herbivore induced response methyl jasmonate`
- `web: prairie coneflower volatile emission herbivore induced response methyl jasmonate`
- `web: Ratibida flower opening time anthesis`
- `web: prairie coneflower flower opening time anthesis`
- `web: Ratibida eye type epidermal focusing`
- `web: prairie coneflower eye type epidermal focusing`

One new wanted source:the Texas A&M thesis result “EXPLORING THE POTENTIAL COMMERCIAL SIGNIFICANCE OF RATIBIDA”. The original Seed Germination Theory and Practice supplement cited by the indexed Ratibida germination entry is already wanted in harvest-c11 and was not duplicated. Unknown author/year/DOI metadata left empty/null. The thesis snippet explicitly describes R.columnifera seed-treatment trials and sequential flower opening; per10(e) it remains a lead, with no assumed light/GA result. The existing supplement source's indexed dark germination description conflicts with nursery recommendations for light; the original experiment is needed, so no light null. Light/chemical and potential flowering timing remain pending this source reading; the present work does not establish chemical sensing or a daily rhythm from hydration or sequential floret development.

Other returned results:smoke/GA studies on Nicotiana, Anigozanthos, Avena and lettuce, MeJA/VOC work on cotton, Iva, oak, cranberry, Trifolium and bracken, and photoperiod studies on Echinacea/Rudbeckia/Coreopsis/Stellaria concern other genera. They supply no Ratibida measurement. Ratibida xanthanolides in S0031942200815022 concern aerial-part chemistry, not living chemical response10(a). Illinois Wildflowers describes little/no R.pinnata floral scent and crushed-seedhead anise odor; this secondary description is not an emitted signalling measurement. USFS germination/stratification review, SDSU native-plant notes, the Tallgrass seed-production guide and nursery germination instructions are retained as provenance leads in raw results, not substituted for the original candidate trials. Seasonal growth/bloom months, flowering order up the column and seed maturity are not by themselves diel measurements.

Eye searches returned Ratibida taxonomy/morphology, flora and horticultural descriptions; no optical focusing lead. Other coneflower results explicitly name Echinacea or Rudbeckia and bee UV vision, not Ratibida eyes. Eye_type null alone follows owner10(b). All candidate sources stayed at title/snippet level under desk-screen3; no full text or evidence written. Raw tool responses preserved in work/harvest-c12/Ratibida-web1–4-worker13.json. Source skips remain OpenAlex429,MDPI429,UChicago403,SANBI403 with no further requests.

Worker13 final cumulative validator completed before commit: `0 problems`; own-file `git diff --check` passed. Existing supplement wanted in harvest-c11 was detected and not duplicated; Ratibida adds1 wanted, worker13 adds17, cumulative34.

## 2026-10-27 — worker18 Fraxinus continuation

This worker:1 genus screened (Fraxinus),1 null search record,46 wanted lines,0 evidence/measurement closures. Cumulative:6/40 genera screened;5 null search records;80 wanted lines;0 evidence. Remaining34, next Adiantum, then Botrypus, then Parthenium. Earlier completed wanted-only Cardamine/Rumex screenings remain complete and are not repeated.

Read AGENTS.md first and all round28/round4/THOROUGH/BRIEF/round3/desk-screen instructions, including plant10(e). The cloud runtime skill and networking reference were read; current unrestricted policy is enforced, no VPN configured. No branch/gate changes, application startup, tests or build. No source-page/full-paper fetch or evidence write. OpenAlex429, MDPI429, UChicago403 and SANBI403 remain skips; no direct retries. Initial web call used an unsupported argument shape and returned `{content:[],isError:true}`; it executed no documented query. After reading the tool declaration, all12 actual protocol queries below succeeded. No quota-limit refusal occurred.

harvest_get and screen_candidates completed. Fraxinus has cached successful genus queries/supplements and three citation steps:10.1603/022.038.0629 (22 returned works),10.1111/een.12947 (zero) and10.3390/ijms26010361 (zero). All179 unique genus/supplement/citation titles and stored abstract excerpts were screened, plus15 Oleaceae family-review titles and stored abstracts. Missing stored abstracts remain unknown, not invented. The raw cache is work/harvest-c12/Fraxinus-cache-worker18.json. No live OpenAlex query was executed or claimed. Exact successful cached queries, followed by actual web queries in execution order:
- `Fraxinus phytochrome photoreceptor`
- `Fraxinus light perception`
- `Fraxinus phototropism`
- `Fraxinus flower opening time`
- `Fraxinus nyctinasty`
- `Fraxinus volatile signalling`
- `Fraxinus photoperiod`
- `Fraxinus circadian rhythm`
- `Fraxinus anthesis`
- `Fraxinus pollination biology`
- `Fraxinus epidermal lens cells`
- `Fraxinus epidermal focusing leaf optics`
- `Oleaceae photoreceptor review`
- `web: Fraxinus seed germination light dark`
- `web: Fraxinus germination gibberellin OR smoke OR dormancy`
- `web: Fraxinus floral scent volatiles`
- `web: Fraxinus light photoperiod phototropism`
- `web: ash tree light photoperiod phototropism`
- `web: Fraxinus flower opening time anthesis`
- `web: ash tree flower opening time anthesis`
- `web: Fraxinus eye type epidermal focusing`
- `web: ash tree eye type epidermal focusing`
- `web: Oleaceae photoreceptor review`
- `web: Fraxinus volatile emission herbivore induced response methyl jasmonate`
- `web: ash tree volatile emission herbivore induced response methyl jasmonate`

Global normal/corrected main evidence, searches, wanted and papers-status were checked. Main recheck-5-fixed#2 corrects the green-ash leaf-volatiles result, so no chemical null or repeat request for Chen/Poland2009. This congener record does not establish species-level chemical response in every original-batch ash species. The old thin sweep-12 stays unchanged and did not hide actual open light/diel/chemical needs. Canon checked; no relevant plant compilation is marked in hand. Broad animal eye canon is not a plant eye measurement; no new canon request.

Forty-six new wanted records preserve actual cache/search titles and source URLs. Unknown authors, years and DOIs remain empty/null; no DOI was guessed from MDPI issue/article URLs. Cached GA3 germination (F.hupehensis), daylength-dependent periderm/xylem (F.pennsylvanica), phototropic stem bending (F.americana), light-gradient leaf costs, light-pollution/budburst, photoperiod spring phenology and the review's explicit green-ash branching citation are real light/chemical leads. Broad light-intensity meta-analysis, UV-B review and leaf-optical/surface-phenotype studies require species-table confirmation. Epidermal focusing belongs under sense_light_nonvisual, never eye_type; Vogelmann1996 is retained as a possible species-table lead, not a Fraxinus measurement claim.

The germination searches returned species-named dormancy trials, the Thomas2016 review, recent rapid germination methods and explicit GA/ABA/kinetin/exogenous-hormone treatments. These stay wanted under10(d,e), including studies whose excerpt does not yet reveal a tested light or hormone contrast. The indexed Deno second-supplement description of F.anomala dark germination is an additional provenance lead; Seed Germination Theory and Practice supplement is already globally wanted (harvest-c11) and was not duplicated. Nursery/USFS field germination and stratification descriptions do not replace reading these trial sources. The phloem-MeJA work, MJ/SNP hybrid experiment, native hormone-expression assays, foliar-melatonin seedlings, living-ash paclobutrazol trials, induced Manchurian-ash volatiles and living regeneration cultures remain chemical candidates. Culture studies require reader confirmation of living response scope; no response measurement is inferred from extracted tissue chemistry alone. FmNAC11 preprint was not separately requested alongside the related published NAC1 work pending identity resolution. Leaf glycoside/extract/coumarin pharmacology, fresh-cut lemons treated with extracted manna, and constitutive phenolic chemistry alone do not count10(a). Pangenome/genomic tolerance and rhizobiome records do not establish chemical cue response from their printed metadata alone.

No diel null: continuous day/night green-ash sap flow, the six-month sap-flow study and daily/intradiurnal Fraxinus pollen counts are retained for full timing/transport interpretation. Their relevance must be decided from the source; no daily activity class is extracted. Other cached diel matches concern rose cut flowers, Osmanthus fragrance, general ABA clock regulation, hares/lynx, sunflower, wheat, Cupressus, lilies, nocturnal pollinators or seasonal tree budburst, not a directly demonstrated Fraxinus daily opening schedule. Fertilization after days of anthesis, annual flowering variation, floral-sex systems and seasonal bloom dates do not alone establish diel activity.

Eye searches returned taxonomic leaflet/epidermal SEM, organ microscopy, stomatal ridges resembling eyes, pollen morphology, tree identification and horticultural anatomy; these do not measure image-forming eyes. The sole tool-listed eye candidate is Halopteris thallus development, a different genus of brown algae; it is explicitly screened. The single eye_type null follows owner10(b). Returned generic plant-photoreceptor reviews and cached Oleaceae review results add no Fraxinus eyes; no new null is written for light, chemical or diel while candidates remain unread. Source excerpts stay at search/cache level. Raw web responses:work/harvest-c12/Fraxinus-web1–4-worker18.json. Cross-file exact DOI/title duplicate check found0 matches among the46 candidates before appending; no n/a source re-requested.

Next:Adiantum, then Botrypus, original genus order. Required candidate validation completed before commit: `0 problems`. Own-file whitespace check passed.

## 2026-10-27 — worker18 Adiantum and handoff checkpoint

This worker total:2 genera screened (Fraxinus, Adiantum),2 null search records,61 wanted lines,0 evidence/measurement closures,24 actual web protocol queries. Cumulative:7/40 genera screened;6 null search records;95 wanted lines;0 evidence. Remaining33, next Botrypus, then Parthenium, then Andropogon. Stopping between genera for fresh context. Preserve all seven completed genera, including wanted-only Cardamine and Rumex, if the raw queue reoffers them.

Adiantum harvest run4 plus supplements12,14,20 and Pteridaceae family metadata were screened:167 unique pooled titles and all stored abstract excerpts. There is no cached citation step; the family review supplies the chase10.1562/2006-02-27-ir-817. The15 family-review entries include general photomovement, evolutionary/genomic/clonality, facilitation, shade/drought, cultural-law and ABA stomatal work. None licenses a genus eye measurement. Existing main canon-3/oa-2/oa-12/sweep-13/corrected plant-fungus-slime light records and oa-9#171–172 antheridiogen records were checked with global searches, wanted and papers-status. The latter measure A.radicans, not all batch species. Original open species are A.pedatum, A.aleuticum and A.capillus-veneris; existing capillus-veneris photoreceptor measurements are preserved with their actual species limits. Thin sweep-13 stays untouched and did not suppress the newer complete searches. Relevant plant canon is checked; the known receptor compilations are already logged for capillus-veneris. No extra canon wanted entry.

Successful cached queries followed by actual web queries, exact order (first20 returned titles/snippets where available):
- `Adiantum phytochrome photoreceptor`
- `Adiantum light perception`
- `Adiantum phototropism`
- `Adiantum flower opening time`
- `Adiantum nyctinasty`
- `Adiantum volatile signalling`
- `Adiantum photoperiod`
- `Adiantum circadian rhythm`
- `Adiantum anthesis`
- `Adiantum pollination biology`
- `Adiantum epidermal lens cells`
- `Adiantum epidermal focusing leaf optics`
- `Pteridaceae photoreceptor review`
- `web: Adiantum seed germination light dark`
- `web: Adiantum germination gibberellin OR smoke OR dormancy`
- `web: Adiantum jasmonate herbivore`
- `web: Adiantum flower opening time anthesis`
- `web: maidenhair fern flower opening time anthesis`
- `web: Adiantum eye type epidermal focusing`
- `web: maidenhair fern eye type epidermal focusing`
- `web: Adiantum light photoperiod phototropism`
- `web: maidenhair fern light photoperiod phototropism`
- `web: Pteridaceae photoreceptor review`
- `web: Adiantum volatile emission herbivore induced response methyl jasmonate`
- `web: maidenhair fern volatile emission herbivore induced response methyl jasmonate`

Fifteen new wanted candidates preserve real titles/DOIs/URLs from cache and indexed results. One duplicate candidate, ABA stomatal kinetics10.1111/nph.15736, is already wanted in harvest-c8 and was not re-requested. Unknown metadata remains empty/null. The repository microtubule/morphogenesis result exposes only a truncated title, retained exactly with an explicit metadata limitation; its snippet identifies colchicine effects in living capillus-veneris leaflet cells. The16 screened candidates were checked against global wanted and papers-status; the15 appended candidates had no exact DOI/title match.

Germination leads are retained under10(e):axenic dark/red-light spore protocol, A.reniforme light/macronutrient/sucrose trial, Taiwan multi-species irradiance/temperature/density thesis, UV/blue inhibition of red-induced germination and phytochrome nuclear relocation. The Taiwan dark-germination snippet and the red-light protocol should be interpreted in their species and treatment conditions, not flattened into a genus light requirement. Further new light candidates include A.flabellulatum transcriptional response, flabellulatum/capillus-veneris biomass allocation under three light levels, A.cuneatum leaf phototropism and2024 low-light phy3/neo growth. Existing main capillus-veneris source measurements were not called absent or requested repeatedly:2003 Nature,2005 PNAS,2015 TPJ,2016 Wada review and canon photoreceptor sources already have records. Other primary phototropic/chloroplast sources mainly concern the same measured capillus-veneris response; their actual cached metadata remains in scratch for future source-level upgrades.

Chemical is held without a null. The2026 A.trapeziforme culture paper explicitly reports benzyladenine inhibition and other regulator treatments, A.raddianum fertilization reports living growth at N/P/K levels, sucrose/macronutrient germination and colchicine responses need reading under10(a,d), and the Selaginella-titled GLV survey actually samples monilophytes too, requiring its species-table check for Adiantum. It was not screened out just for its title. GA-signalling conservation, Remorin response-element predictions and native gene/transgenic flowering comparisons alone do not identify a direct living chemical response from their printed metadata. Extract/essential-oil pharmacology, antioxidant/antibacterial assays, dried powder taste and extracted allelopathy applied to lettuce/tomato are not Adiantum cue responses. Paired JA/VOC searches mostly return Pteridium, Asplenium, Selaginella, cotton, Iva, Nicotiana, oak and other genera; these are not silently carried to Adiantum.

No diel null:the sporangium exposure/spore-release paper10.1371/journal.pone.0138495 remains a lead to inspect for timing, despite its abstract emphasizing passive desiccation/hydraulic actuation rather than a daily schedule. The GI thesis10.6845/nchu.2013.00602 explicitly has native fern circadian gene expression, retained for nonvisual light rather than assuming daily activity. Cached remaining diel matches concern marine diatoms, Arabidopsis, mammals, Citrus, coral algae, Japanese cedar, carnation, CAM cacti or book-index terms. General light-entrained genes and a response after hours in darkness are not by themselves a diel activity class. Ferns lack flowers; anthesis web queries chiefly yielded botanical/houseplant descriptions, seasonal spore dates, and unrelated flower-opening reviews. These do not establish daily activity.

Eye_type alone is null under owner10(b). All six tool-listed eye candidates receive explicit screened reasons:animal cryptochromes; Adiantum pharmacognostic epidermis; two Vallisneria chloroplast papers; Metasequoia anatomy; Magnolia epidermal morphogenesis. Additional Nepalese epidermal taxonomy and leaflet cytoskeletal morphogenesis report no image-forming eyes in returned descriptions. No Adiantum epidermal optical-focusing lead was found. No source-page/full-text fetches or evidence writes. Raw web and cache outputs are local work/harvest-c12/Adiantum-*-worker18 files. Blocked sources remain OpenAlex429, MDPI429, UChicago403 and SANBI403, no retry. No actual web quota refusal.

Required combined candidate validation completed before commit: `0 problems`. Own-file whitespace check passed. Next first incomplete genus:Botrypus.


## 2026-10-27 — worker25 continuation: Botrypus

This worker:1 genus completed,0 search records,1 new wanted,0 evidence. Cumulative:8/40 genera completed,6 search records,96 wanted,0 evidence;32 remain, next Parthenium. No measured cells closed.

Read AGENTS.md first and all specified protocols. Runtime networking verified with the cloud-environment skill; no external source/full-paper page was fetched. Harvest and candidate tools read the cached ci metadata:run6, supplements15/20 and Ophioglossaceae family review. All stored titles/abstracts screened. The sole live-tool open trait is light, corroborated against original gaps and main:the old sweep-31#3 is an actual family-level review record, retained without rewriting or treating it as a species measurement. Existing replant-1 eye_type/diel/chemical screenings are substantive available-source protocols and were preserved without repeating their paired searches. Canon plant list checked, no relevant in-hand compilation found.

Exact successful cached and executed web queries, in order:
- `Botrypus phytochrome photoreceptor`
- `Botrypus light perception`
- `Botrypus phototropism`
- `Botrypus flower opening time`
- `Botrypus nyctinasty`
- `Botrypus anthesis`
- `Botrypus pollination biology`
- `Botrypus volatile signalling`
- `Botrypus photoperiod`
- `Botrypus circadian rhythm`
- `Botrypus epidermal lens cells`
- `Botrypus epidermal focusing leaf optics`
- `Ophioglossaceae photoreceptor review`
- `web: Botrypus seed germination light dark`
- `web: Botrypus germination gibberellin OR smoke OR dormancy`
- `web: Botrypus jasmonate herbivore`
- `web: Botrypus light photoperiod phototropism`
- `web: rattlesnake fern light photoperiod phototropism`
- `web: Botrychium virginianum spores germination dark light`
- `web: Botrychium virginianum Whittier 1973 germination light`
- `web: Ophioglossaceae photoreceptor review`
- `web: "Spore germination and young gametophytes" "virginianum"`
- `web: "Botrychium virginianum" germination Whittier Peck 1990`

Ten new web queries read returned titles/snippets (up to first20 where returned). Required seed-name queries and JA query mostly returned generic model-plant seed/hormone results, so a species-synonym germination query followed. Scientific/common light searches locate species germination citations under Botrychium virginianum. One new wanted entry retains Whittier1985, explicitly a possible meeting abstract, with real bibliographic reference-list provenance and no invented DOI. Whittier1973 actually treats B.dissectum (now Sceptridium), so its darkness experiment is not silently carried to Botrypus. Peck1990 germination percentage is cited secondhand by conservation assessments, with no verified light-treatment detail; not independently requested. The2022 belowground-methods paper10.1002/aps3.11469 explicitly includes Botrypus but repeats general Botrychium darkness statements already represented by main; its indexed methods/structure-density result does not establish a new species light treatment. The broad2023 circadian fern panel and2024 nonflowering-plant photoperiod review have no Botrypus experiment identified by returned snippets, so no speculative species-table request.

Other cached candidates are phytochrome genomics (already wanted/canon and logged at order level), HGT, KAI2 receptor evolution, oxygen-sensing enzymes, phylogenetic markers, general anatomy and vegetation inventories; none identifies a new direct Botrypus light-response trial in stored abstracts. Leaf epidermal microscopy10.3724/cbb-t99-047 has no focusing measurement; existing eye disposition retained. Family review metadata includes phylogeny/classification and GA experiments in Osmunda/Athyrium; no target-species light measurement. Broad stomatal review is background. The existing2025 Botrypus phenology wanted10.1640/0002-8444-115.4.296 remains, no duplicate. No null is written while species germination and prior phenology leads await reading. Blocked services remain OpenAlex429/MDPI429/UChicago403/SANBI403, no retry; no web quota refusal. Local provenance:work/harvest-c12/Botrypus-*-worker25 files.


## 2026-10-27 — worker25 continuation: Parthenium

This-worker cumulative:2 genera completed (Botrypus, Parthenium),1 search record,7 new wanted,0 evidence. Batch cumulative:9/40 genera completed,7 search records,102 wanted,0 evidence;31 remain, next Andropogon. No measured cells closed.

Harvest_get and screen_candidates both report no genus harvest. Original gap traits are eye_type,diel,chemical; existing sweep-35#4 has an actual measured species light response from an abstract, preserved. Prior sweep-35 screening of the remaining traits has combined broad queries and the old narrow chemical reading; it does not suppress the current full chemical/diel/eye protocol. Global evidence/wanted/status/searched checked before writing; six selected candidates had no exact DOI/title match. Asteraceae cached run17 family query reused without repeating previous real searches; all15 returned titles/stored abstracts screened. Canon relevant to eye_type has no plant-specific in-hand measurement.

Exact cached and web queries, in order:
- `Asteraceae photoreceptor review`
- `web: Parthenium seed germination light dark`
- `web: Parthenium germination gibberellin OR smoke OR dormancy`
- `web: Parthenium floral scent volatiles`
- `web: Parthenium volatile emission herbivore induced response methyl jasmonate`
- `web: ragweed parthenium volatile emission herbivore induced response methyl jasmonate`
- `web: Parthenium flower opening time anthesis`
- `web: ragweed parthenium flower opening time anthesis`
- `web: Parthenium eye type epidermal focusing`
- `web: ragweed parthenium eye type epidermal focusing`
- `web: "Germination of Parthenium hysterophorus" "chemicals" -site:researchgate.net`
- `web: "Reproductive ecology" "Whitetop" -site:researchgate.net`
- `web: "Parthenium hysterophorus" "volatiles" living plant jasmonate`
- `web: "Parthenium" "germination promoting chemicals" -site:researchgate.net -site:eurekamag.com`
- `web: "Reproductive ecology of the globally invasive" Usharani journal`
- `web: "Parthenium hysterophorus" salicylic acid gibberellic seed germination`

Fifteen web queries read returned titles/snippets, first20 where available; targeted follow-ups identify real sources and chemical relevance. Six wanted leads:direct target-species chemical germination study; reproductive ecology and multi-species anthesis/pollen timing; field volatile allelopathy; intact-host volatile attraction; root-exudate mosquito oviposition. Publication metadata remains null/empty where not actually verified. ResearchGate results were discovery snippets only, never opened or used as measurements; the germination study was verified through legal indexed reference-list/synthesis sources and the reproductive paper through indexed bibliography. The six requested works target the open P.hysterophorus chemical/diel cells. No already-measured light-only source was requested merely for extra coverage.

Under10(a), the2011 volatile field experiment is retained since it includes living intercropped plants despite also testing fresh detached tissues; the actual intact versus detached comparison needs reading. Mosquito host-plant and root-exudate leads need method checks for living release versus extraction and microbial production. The2023 synthetic-lure study10.1093/jme/tjad077 describes hexane floral/foliar extracts, so it was not automatically requested as plant signalling. The2024 bacteria-root-exudate work10.3389/fitd.2024.1359774 chiefly tests isolated bacteria; retained as provenance of the primary root study, without an extra speculative wanted line. Methanol-extract phytotoxicity to Eleusine/Digitaria/crops, distilled oils and human dermatitis do not show living Parthenium chemical response. Applied Fusarium filtrate germination and incoming Artemisia/grass extracts are secondary possible chemical routes, with direct hormone/germination lead prioritized; they are not grounds for a chemical null. Guayule(P.argentatum) light/GA/smoke studies name a different species without an allowed chemical carry to the queued P.hysterophorus, so not added solely to inflate genus leads. Pyrethrum/Tanacetum parthenium floral scent sources name a different genus.

Diel remains held:the reproductive study and1992-looking DOI pollen-release source identify actual target anthesis; no year inferred from DOI digits. Seasonal flowering, age-to-bloom and continuous reproduction are distinct from daily flower timing. Eye_type alone has a full null under owner10(b), with explicit trichome-anatomy/human-dermatitis/retinal-cell screened reasons. No epidermal focusing candidate found. Cached family results mostly treat other Asteraceae/crops, model flowering networks, human retinal protection and general reviews; no direct target eye measurement. No source/full-paper pages fetched, no evidence written. Service exclusions remain OpenAlex429/MDPI429/UChicago403/SANBI403; no retries and no web quota refusal. Local raw provenance:work/harvest-c12/Parthenium-*-worker25 files.


## 2026-10-27 — worker25 continuation: Andropogon

This-worker cumulative:3 genera completed(Botrypus,Parthenium,Andropogon),2 search records,12 new wanted,0 evidence. Batch cumulative:10/40 genera completed,8 search records,107 wanted,0 evidence;30 remain, next Cynodon. No measured cells closed.

Harvest_get and screen_candidates report no genus harvest. Original species/gaps independently checked:Andropogon gerardi has light,diel,eye_type,chemical open. Existing measured short-day classifications for gayanus/virginicus are actual main evidence, preserved with species limits; they cannot silently settle gerardi chemical/light. Former scoparius measurements belong to Schizachyrium. Thin sweep-34 two-query record was not treated as a completed protocol. Global evidence/wanted/status checked. Poaceae cached family result reused from real ci metadata held in neighboring worker scratch, copied to own scratch; all15 titles/stored abstracts screened, with a new web family review query too. No new in-hand plant canon measurement.

Exact successful cached and executed web queries, in order:
- `Poaceae photoreceptor review`
- `web: Andropogon seed germination light dark`
- `web: Andropogon germination gibberellin OR smoke OR dormancy`
- `web: Andropogon jasmonate herbivore`
- `web: Andropogon light photoperiod phototropism`
- `web: big bluestem light photoperiod phototropism`
- `web: Andropogon flower opening time anthesis`
- `web: big bluestem flower opening time anthesis`
- `web: Andropogon eye type epidermal focusing`
- `web: big bluestem eye type epidermal focusing`
- `web: Andropogon volatile emission herbivore induced response methyl jasmonate`
- `web: big bluestem volatile emission herbivore induced response methyl jasmonate`
- `web: Poaceae photoreceptor review`
- `web: "Andropogon gerardii" germination gibberellic acid light`
- `web: "Andropogon gerardii" anthesis "morning"`
- `web: "Andropogon gerardii" chemical response volatile ethylene salicylic`
- `web: "Andropogon gerardii" "photoperiod" McMillan flowering ecotypes`
- `web: "Evolutionary Implications" "Cytotypes" "Andropogon" -site:researchgate.net`
- `web: "Andropogon" "Knapp" "solar radiation"`

Eighteen web queries read returned titles/snippets, up to first20 where available. Genus germination searches initially mostly returned gayanus and other congeners, so follow-ups target gerardii spelling used by primary papers. Five new wanted candidates:target-species GA pretreatment/germination trial, target ecology/germination thesis, two A.gerardii irradiance response/acclimation sources, and the1997 reproductive cytotype study for possible anthesis timing. The Knapp1984 source is identified by real title/DOI/reference metadata. For the other irradiance paper the title is kept as indexed in the EPA bibliography(including Poacea spelling), and year/authors remain empty/null; no year inferred from DOI. All five candidates passed exact normalized title/DOI checks against existing wanted/status; no existing paper/evidence was rewritten.

No light null while these candidates wait. The field irradiance studies require separation of light effects from temperature/water/fire covariates; sun/shade anatomy is a candidate living response, not claimed photoreceptor mechanism. McMillan ecotype references found in later drought/photoperiod papers were followed as citations but no unsupported primary title was invented. Rice1950 already appears in main evidence under Schizachyrium with big bluestem named in its group note; it was not duplicated as a new request. The switchgrass photoperiod-extension paper cites prior big-bluestem studies but its own species is Panicum; it is not an A.gerardi measurement.

No chemical null:Cracking the case explicitly describes GA seed pretreatment and includes A.gerardii. General JA searches mostly return Iva,cotton,Nicotiana,Arabidopsis,Quercus and other non-targets. Gayanus GA/cytokinin experiments and general grass germination are real congener sources but do not close the queued species chemical cell and were not requested solely for volume. The nearby-plant phytochemical field experiment10.1093/aobpla/plaf071, nutrient/mycorrhizal trials and tissue-culture protocol are additional possible routes, but the direct hormone-germination source was prioritized; no claim that they prove absence. Ammonia volatilization during drought quantifies N loss without a demonstrated signalling function in snippets, so not treated as chemical communication. Bacterial ACC-deaminase genomic potential alone is not living target response.

No diel null:the reproductive cytotype paper has before-anthesis and next-morning methods, enough to retain for checking native opening observations; scheduled crossing by itself would not establish daily activity. Other hits describe seasonal flowering, cultivar phenology, first anthesis dates or gayanus spikelet opening, not a gerardi daily class. Eye_type alone gets a null under owner10(b), with anatomical flora/taxonomic epidermal studies/stomatal review screened explicitly. No optical-focusing candidate found. Family metadata covers grass stomata, phytochrome signalling/shade pathways, cereal/rice and general carotenoid reviews; none identifies direct Andropogon eye measurement. No source/full-paper pages fetched and no evidence logged. OpenAlex429/MDPI429/UChicago403/SANBI403 skipped throughout; no new refusal or actual web-quota refusal. Local provenance:work/harvest-c12/Andropogon-*-worker25 and Poaceae-cache-worker25 files.

Worker25 final checkpoint:combined candidate validation printed `0 problems` for all8 searched/107 wanted lines; own-file whitespace check passed. All12 this-worker sources were also checked against global main evidence by normalized title/DOI, with no matches. No unknown-year numeric0 values exist in the batch wanted file. Stop between genera for fresh-context continuation at Cynodon; preceding Botrypus commit d32c34a9, Parthenium commit03991b96.


## 2026-10-27 — worker31 continuation: Cynodon

This worker:1 genus completed,1 search record,11 new wanted,0 evidence/measurement closures. Batch cumulative:11/40 genera screened,9 search records,118 wanted,0 evidence;29 remain, next Glechoma. Prior Cardamine/Rumex wanted-only full screenings and all107 prior wanted lines preserved. The existing Parthenium anthesis request was expanded to include C.dactylon without a duplicate wanted line; its year1992 and journal Grana are verified by cached harvest metadata rather than DOI digits.

Read AGENTS.md first and the round28 guide/round4-harvest/THOROUGH/BRIEF/round3-sweep/desk-screen points1–10 including10(e). Current original queue and global evidence/searched/wanted/papers-status/canon checked. Harvest_get and screen_candidates ran; genus run7, supplements15/20, citation step citing10.1016/j.tree.2009.09.010, and all15 Poaceae family-review titles/stored abstracts screened. The full cached abstract metadata for the plausible sources was inspected. Local ci cache was reconstructed from origin/ci without new OpenAlex calls; a truncated gzip shard required decompressobj, matching harvest_get, and was then parsed successfully. No failed harvest step remains. Old sweep-44 single-query combined record is thin and did not suppress current work. Main already measures C.dactylon photoperiod response through Ji2022(10.7717/peerj.14326;partial); no already-covered light-only source added.

Successful cached queries followed by actual web queries, exact order:
- `Cynodon phytochrome photoreceptor`
- `Cynodon light perception`
- `Cynodon phototropism`
- `Cynodon flower opening time`
- `Cynodon nyctinasty`
- `Cynodon anthesis`
- `Cynodon pollination biology`
- `Cynodon volatile signalling`
- `Cynodon epidermal lens cells`
- `Cynodon epidermal focusing leaf optics`
- `Poaceae photoreceptor review`
- `web: Cynodon seed germination light dark`
- `web: Cynodon germination gibberellin OR smoke OR dormancy`
- `web: Cynodon floral scent volatiles`
- `web: Cynodon volatile emission herbivore induced response methyl jasmonate`
- `web: bermudagrass volatile emission herbivore induced response methyl jasmonate`
- `web: Cynodon flower opening time anthesis`
- `web: bermudagrass flower opening time anthesis`
- `web: Cynodon eye type epidermal focusing`
- `web: bermudagrass eye type epidermal focusing`
- `web: "Cynodon dactylon" gibberellic acid salicylic acid germination`
- `web: "Cynodon" anthesis "morning"`
- `web: "Effect of different concentrations of gibberellic acid on seeds germination and growth in different turf grass genera" -site:researchgate.net`
- `web: Poaceae photoreceptor review`
- `web: "Cynodon" "epidermal" focusing lens`
- `web: "Cynodon" "Circadian patterns of pollen release"`
- `web: "Cynodon" "A Note on Anthesis"`
- `web: "Cynodon" "Plant responsiveness to root" stress cues`
- `web: "Cynodon" "Volatile and Contact Chemical Cues"`

Eighteen web queries read returned titles/snippets, up to first20 where returned. The first malformed call used the unsupported search_query argument and returned empty content with isError:true; it ran no documented query and is not counted. Corrected system2_search_query syntax immediately succeeded; this was not an actual quota refusal. All successful raw tool provenance is in work/harvest-c12/worker31-Cynodon-web1..5.json, cache and harvest/candidate scratch. No source/full-paper pages fetched.

Eleven new wanted candidates passed global DOI/normalized-title checks against wanted, status, evidence and corrected evidence. They target living C.dactylon responses to melatonin, root-neighbour stress cues, paclobutrazol, sulfur dioxide, Peganum extracts, wild-mango extracts, cytokinin, GA seed priming, acid pretreatment; and measured circadian pollen release, plus host-material volatile attraction requiring confirmation of living versus detached source. The hormone/germination work meets10(d,e); acid scarification needs separation from actual cue perception. Incoming extracts applied to living Cynodon seedlings/seeds are retained chemical-response candidates, distinct from extracting Cynodon for animal or test-tube assays. Cytokinin thesis must confirm cultivar/species identity, and no pooled GA numeric result was extracted. Unknown author fields stay empty; no year0 values added. No chemistry/null fork identified in main's existing light-only evidence.

Diel has actual target timing leads: the1988 circadian pollen paper explicitly names C.dactylon flowering twice per circadian cycle; the1992 anthology already requested for Parthenium also explicitly names Cynodon. No diel null. Davidson's general grass anthesis note(10.5962/p.386043) has conflicting1935 cached versus1941 bibliography metadata and only a Volume7 abstract; species representation remains unverified. It was not inflated into another target request while two direct species timing studies are retained. Wheat drought-priming and rice anthesis-temperature papers name other taxa. Seasonal bloom descriptions, weeks-to-flower, floral anatomy and bee pollen-resource use do not themselves establish daily opening time.

Chemical candidate dispositions:10.1093/aob/mcs045 is an unusually direct target root-communication experiment, not a review. General root-VOC review10.1007/s11104-016-2823-3 and new2023 interspecific review/cuing lead were considered against that direct source, with no extra background request. Schinus fruit anticancer extracts, Artemisia liqueur chemistry, medicinal Cynodon oils/extracts, antimicrobial compounds, rodent assays and mosquito grass infusions are not live Cynodon responses/signals under10(a). C.nlemfuensis volatile composition concerns a different species. The Carya leachate paper tests a living receiver in another genus and nonvolatile donor leachates, not direct Cynodon perception; no unsupported Cynodon chemical closure. Soil remediation/genomic surveys and endogenous hormone profiling alone do not establish cue response; direct hormone/germination sources are prioritized. Billbug olfactometer source remains wanted only until intact versus detached host-material methods are checked.

Eye_type alone has the completed null under owner10(b). Explicit candidate screening covers the two screen_candidates hits(the Cynodon epidermal/stomatal taxonomy paper and Panicum anatomical thesis), plus the indexed medicinal-grass and SEM anatomy studies. No lens focusing lead was identified. Poaceae cached review metadata covers grass stomata, phytochrome/shade/carotenoid pathways, rice/sugarcane and general reviews; no Cynodon image-forming eyes. Canon has no relevant in-hand plant measurement. OpenAlex429/MDPI429/UChicago403/SANBI403 remain skipped; no new refusal, paid API, library/proxy mirror, source-page fetch, evidence extraction or app checks.

Worker31 Cynodon validation:combined screen_candidates --check completed with `0 problems` before commit; global normalized-title/DOI duplicate gate passed for all11 new lines. No unknown numeric-year0 introduced.


## 2026-10-27 — worker31 continuation: Glechoma

This worker cumulative:2 genera completed(Cynodon,Glechoma),2 search records,19 new wanted,0 evidence/measurement closures. Batch cumulative:12/40 genera screened,10 search records,126 wanted,0 evidence;28 remain, next Senecio. Cynodon commit63941286. No prior wanted-only screening repeated. No existing evidence or legacy nulls altered.

Original queue targets G.hederacea; cached genus run2 plus supplementary volatile query has many G.longituba studies and actual G.hederacea root-recognition and extract studies. Cached titles and stored abstracts were screened for all returned works, with all15 family-review stored abstracts. Two completed citation filters(cites10.1111/een.12947 and10.1016/j.isci.2022.104455 naming Glechoma) returned zero. Global evidence/corrected evidence/searched/wanted/papers-status checked; no main Glechoma measurement was found. Thin harvest-8 and sweep-4 nulls do not satisfy the full protocol and remain untouched. Canon has no relevant in-hand plant measurement.

Exact successful cached queries then executed web searches, in order:
- `Glechoma phytochrome photoreceptor`
- `Glechoma light perception`
- `Glechoma phototropism`
- `Glechoma volatile signalling`
- `Lamiaceae photoreceptor review`
- `web: Glechoma seed germination light dark`
- `web: Glechoma germination gibberellin OR smoke OR dormancy`
- `web: Glechoma floral scent volatiles`
- `web: Glechoma light photoperiod phototropism`
- `web: ground ivy light photoperiod phototropism`
- `web: Glechoma volatile emission herbivore induced response methyl jasmonate`
- `web: ground ivy volatile emission herbivore induced response methyl jasmonate`
- `web: Glechoma flower opening time anthesis`
- `web: ground ivy flower opening time anthesis`
- `web: Glechoma eye type epidermal focusing`
- `web: ground ivy eye type epidermal focusing`
- `web: "Glechoma hederacea" gibberellin ethylene auxin salicylic jasmonate`
- `web: "The Response of Petioles of Glechoma hederacea to a Dynamic Light Climate" -site:researchgate.net`
- `web: "Clonal integration and plasticity in foraging behaviour in Glechoma hederacea" -site:researchgate.net`
- `web: "Glechoma hederacea" seed germination light dark experiment`
- `web: "Glechoma" "gibberellin" "corolla"`
- `web: "Glechoma hederacea" "Dynamic Light Climate" Plant Biology`
- `web: "Glechoma" "Clonal integration and plasticity" 1987 1023 DOI`
- `web: "POLLINATION AND FLORAL ECOLOGY OF GLECHOMA"`
- `web: "Effect of gibberellic acid on corolla size"`
- `web: "Glechoma" "Dynamic Light Climate" doi`
- `web: "Glechoma hederacea" "effects of light intensity" 1987 doi`
- `web: "10.1111/j.1438-8677.1999.tb00281.x"`
- `web: "The effects of light intensity on foraging" Glechoma doi`
- `web: "Effect of Gibberellic Acid on Corolla Size" Plack Nature`

Twenty-five web searches screened returned titles/snippets, up to first20 where returned. Follow-ups resolve named primary studies and target-species identity instead of inventing source titles or DOI metadata. Raw results in work/harvest-c12/worker31-Glechoma-web1..7.json; original ci metadata in worker31-Glechoma-cache.json. No source/full-paper page fetched, no API retry. In the first printed combined tool response some output was display-truncated; the omitted search-result tail and relevant full stored abstracts were read separately from scratch before disposition.

Eight target-specific wanted sources:2020 root-kin-recognition experiment; Plack1958 GA/corolla-size experiment; two1987 Slade/Hutchings light/foraging studies; legal-repository spectral growth experiment explicitly including G.hederacea; publisher floral-ecology study explicitly indexed for morning flower opening; Biological-Flora account holding seed germination stages/light observations and primary citations; NARO target-species germination-characteristics entry retained under10(e). All8 passed global normalized-title/DOI duplicate comparison against wanted,status,evidence and corrected evidence. Every target is G.hederacea. Plack author's full name/year/title verified by Nature issue and DOI by legal review bibliography; attached buds versus cut flowers still needs primary methods checking10(a). Root-recognition source needs exudate/physical-contact/resource controls before calling the mechanism chemical. No measurements logged, and year remains null for the spectral, floral-ecology and NARO entries whose exact publication year was not verified. No year inferred from DOI digits or PDF filenames.

The1987 integration paper's light/nutrient factors are described explicitly by indexed bibliographic abstract; light-intensity primary source has a separately verified title/authors/year/DOI in USDA and legal Springer/Wiley citations. The1999 Biological-Flora request targets actual germination/light data and references, not medicinal background. NARO's species page is an unread germination lead under10(e); its title is retained as indexed, without inventing response values. Grime1981 germination compilation was encountered in discovery, but a G.hederacea row/chemical/light result was not verified and no speculative request was added. Another legal dissertation synopsis mentions species germination(chilling) but the named direct species entries are prioritized. No light/diel/chemical null while direct target measurements await reading.

Other dispositions: G.longituba colored-film, UV-B/methylation, shade-touch, kin-recognition and alkaline-stress experiments are real but not the queued species, and were not requested merely for volume; G.grandis neighbour-channel work and G.hirsuta shade work likewise cannot silently settle hederacea. Potentilla/Trifolium/Portulaca/Arabidopsis/Valeriana/Artemisia/pea experiments and generic ROS/transduction reviews are other taxa or general context. Cached medicinal G.hederacea extraction(10.3390/plants11060819;10.3390/plants11172217), human-cell/plasma assays(10.3390/nu15071671), oral-health review(10.3390/plants15152396), isolated glycosides, distilled oils and botanical-name etymology do not show the living target response under10(a). Family results cover Lamiaceae industrial-compound/light reviews, Teucrium germination, Hyptis light responses and human/animal pharmacology, with no target eye measurement. No duplicate background wanted from those reviews.

The petiole dynamic-light study was discovered, but its candidate DOI10.1111/j.1438-8677.1999.tb00281.x/author/date returned only ResearchGate metadata in follow-ups, with conflicting1999 versus2008 indexing. ResearchGate was never opened or used as measurement/source authority. Legal Wiley citation independently confirms the title/Plant Biology pages; it remains a named unrequested bibliographic lead while three independently sourced direct target light experiments are retained, without a light-null claim. Secondary generic phytochemical/infusion results do not establish signalling by living Glechoma. A direct2,4-D population rate-response source also appeared; the GA/root-cue experiments were prioritized without claiming the herbicide source disproves a response.

Eye_type alone gets a completed null under owner10(b). Web eye searches returned a Korean taxonomic leaf-epidermis/stomata/trichome comparison and ordinary botanical identification, not image-forming eyes. Biological-Flora's cross-hair eye-piece is a microscope instrument; no optical focusing lead found. Diel lead's Russian publisher snippet explicitly says flowers open in the morning; seasonal March-June bloom or continuous12h growth-room lighting is not used as a daily activity measurement. Old13Oct/16Oct nulls remain unchanged and no source-rule conflict in legacy evidence was identified. OpenAlex429/MDPI429/UChicago403/SANBI403 skipped; no new refusal or web quota refusal. No paper text committed and no app tests/builds/servers run.

Worker31 Glechoma checkpoint:combined screen_candidates --check completed with `0 problems` before commit for all10 searched/126 wanted; own additions passed global duplicate and metadata checks. No unknown numeric-year0 added.


## 2026-10-27 — worker31 continuation: Senecio and handoff

This worker cumulative:3 genera completed(Cynodon,Glechoma,Senecio),3 search records,33 new wanted,0 evidence/measurement closures. Batch cumulative:13/40 genera screened,11 search records,140 wanted,0 evidence;27 remain, next Ranunculus in original batch order. Stop between genera for fresh-context takeover after final validation/commit. Cynodon commit63941286; Glechoma commit53626498. No actual web quota refusal.

Authoritative original gaps are light,chemical and eye_type for S.vulgaris(37,976records) and S.inaequidens(10,115records). No Senecio genus harvest exists in cached origin/ci. All15 Asteraceae family-review titles and stored abstracts were screened. Current global evidence/corrected evidence,searched,wanted,papers-status and canon checked; thin sweep-9 does not satisfy the full protocol. No relevant in-hand plant canon measurement. Main's existing sweep-9 chemical/diel source is S.articulatus, now often placed in Curio, and explicitly does not measure either queued species. This species/genus coverage mismatch was reported to parent; legacy records remain untouched and no chemical/diel null is invented. The original queue has no Senecio diel cell, so this entry does not claim a new completed target-diel protocol or duplicate the congener source.

Exact cached family query and actual web searches, in order:
- `Asteraceae photoreceptor review`
- `web: Senecio seed germination light dark`
- `web: Senecio germination gibberellin OR smoke OR dormancy`
- `web: Senecio floral scent volatiles`
- `web: Senecio light photoperiod phototropism`
- `web: groundsel ragwort light photoperiod phototropism`
- `web: Senecio volatile emission herbivore induced response methyl jasmonate`
- `web: groundsel ragwort volatile emission herbivore induced response methyl jasmonate`
- `web: Senecio eye type epidermal focusing`
- `web: groundsel ragwort eye type epidermal focusing`
- `web: "Senecio inaequidens" germination light gibberellic nitrate`
- `web: "Senecio vulgaris" "Senecio inaequidens" jasmonic salicylic chemical response`
- `web: "Senecio inaequidens" gibberellin abscisic salicylic jasmonate`
- `web: "Senecio vulgaris" "seed dormancy" gibberellic acid Hilton`
- `web: "Common Groundsel" "Seed Longevity and Seedling Emergence" -site:researchgate.net`
- `web: "Senecio inaequidens" "Acta" "1998" invasion germination`

Fifteen web searches read returned titles/snippets, up to first20 where returned. Additional target-species searches check S.inaequidens chemical/germination relevance and identify real primary dormancy studies rather than relying on medicinal extract hits. Raw metadata/provenance in work/harvest-c12/worker31-Senecio-cache.json and worker31-Senecio-web1..4.json. Any display-truncated search-result tail was read separately from saved scratch. No source/full-paper page fetched, no evidence extracted and no live OpenAlex request.

Fourteen new wanted lines passed global DOI/normalized-title duplicate checks against wanted,status,evidence and corrected evidence. Target S.vulgaris sources:Hilton1983 phytochrome white/red-light germination; Lutman2008 seed production/germination; WeedScience2026 laboratory/light-versus-dark/salinity/osmotic/pH study; origin/seasons/storage germination; different light/pH/salt practices; Mediterranean GA3/kinetin dormancy; Figueroa2007 seed longevity/emergence;2010 maternal-environment dormancy; direct light/photosynthesis study; and intercropping/light-competition experiment. Target S.inaequidens sources:highland-pasture control/light-quality study; Ernst1998 invasion ecology with monthly germination-cohort data; three-invader emergence study; and field seed-bank burial/viability study. These are actual target germination,light or chemical-response candidates; no unrelated crop/model, extract chemistry or generic background review added.

Owner10(e) retains germination/dormancy leads even where the snippet only reports a set photoperiod or burial treatment. The wanted reasons explicitly flag where fixed12h lighting, burial, temperature, maternal conditions or nutrient factors cannot alone establish a light-response effect. The direct white/red/dark experiment and2026 design provide clear target light contrasts. GA3/kinetin in living S.vulgaris seeds is a chemical-response candidate under10(d). For S.inaequidens, the highland study explicitly names stage-dependent herbicide resistance and light-quality/quantity effects; its primary treatment/control design needs reading before accepting living chemical response. No inference of chemical absence from failed jasmonate keyword matches. Unknown authors/journals/years stay empty/null; no year inferred from DOI/PubMed-ID digits, crawl age or elapsed publication age. Year2026 is explicitly in publisher volume74/e70 metadata,1983/2008 in publisher labels,1992 in the indexed Acta citation,2007/2010 in legal citing bibliographies and1998 in the legal Acta repository metadata. No year0 added.

Other sources/dispositions: Senecio cineraria growth-regulator/light-germination work concerns a different formerly named taxon, not either target; S.madagascariensis germination/floral scent, Jacobaea vulgaris phytochrome/induced volatile papers and old Curio/S.articulatus scent work were not requested for target species. The broad common name ragwort often returns Jacobaea or Packera; these matches cannot silently settle Senecio. Target-species essential-oil/antioxidant/anti-diabetic/cytotoxic/antimicrobial papers(e.g.10.1080/09637480500131236) test extracts or other organisms and do not qualify under10(a). Pyrrolizidine-alkaloid chemistry, honey residues, leaf reflectance spectroscopy and field herbivore/plant-size associations do not by themselves demonstrate living cue response. Native/invasive life-history studies, ecological theses and fixed thermal seed-killing protocols were considered as adjacent context; named direct light/germination studies are prioritized without a light/chemical-null claim. Field abundance/light-index/flowering-season profiles and flower counts do not establish daily activity. No plausible target measurement was falsely called absent.

Eye_type has the completed null under owner10(b), with botanical epidermal authentication, cypsela ultrastructure, human retinal-cell/macular-health results explicitly screened. The six-succulent epidermal-window paper includes former S.rowleyanus(now Curio) and Peperomia focusing. It is named in screened with the required owner's phrase: focusing belongs under sense_light_nonvisual; its actual species do not match the queued targets, so no speculative Senecio wanted. No focusing measurement for S.vulgaris/S.inaequidens found. Asteraceae family results mostly concern crop flowering, other-genus light responses, medicinal compounds and human retinal protection, not plant image-forming eyes.

Service restrictions remain OpenAlex429/MDPI429/UChicago403/SANBI403, with no retries. No paid API, library/proxy mirror, plant source/fullpaper-page fetch, paper-text commit or app builds/tests/servers. Actual research desk audit/application ownership stays with parent; no branch/gate/issue29/30 changes.

Worker31 final checkpoint:actual harvest_get.py Senecio and screen_candidates.py Senecio completed, reporting no genus harvest; reconstructed cached family metadata was screened as described. Combined screen_candidates --check completed with `0 problems` before commit for all11 searched/140 wanted lines. Own-file whitespace check passed; batch has no year0 placeholders. This worker used58 successful web queries(18Cynodon,25Glechoma,15Senecio); one initial malformed uncounted call is documented above. No source/full-paper page fetched. Stop between genera at Ranunculus;27 remain.


## 2026-10-27 — worker41 continuation: Ranunculus

Worker41 cumulative:1 genus completed,1 search record,11 new wanted,0 evidence/measurement closures. Batch cumulative:14/40 genera screened,12 search records,151 wanted,0 evidence;26 remain, next Datura. Prior completed real protocols preserved; no wanted-only completed genus repeated.

Authoritative original gaps target R.repens(37,621 records), R.acris(18,569), R.sceleratus(10,878), R.abortivus(9,960), each light/chemical/diel/eye_type. harvest_get.py and screen_candidates.py actually ran; the current open-trait filter prints only light because thin older nulls suppress other traits. That filter was not treated as completion. Cached genus run4, supplementary run12, all five citation-step works citing10.3389/fpls.2020.597823 and all15 Ranunculaceae family-review titles and complete stored abstracts were screened. Existing sweep-6#31 light evidence measures R.asiaticus only; it cannot carry to these targets. No legacy record altered, and no living-chemical source-rule conflict identified. Canon checked; no relevant in-hand plant measurement.

Exact successful cached queries, in original order:
- `Ranunculus phytochrome photoreceptor`
- `Ranunculus light perception`
- `Ranunculus phototropism`
- `Ranunculus photoperiod`
- `Ranunculus circadian rhythm`
- `Ranunculaceae photoreceptor review`

Exact actual web queries, in order:
- `web: Ranunculus seed germination light dark`
- `web: Ranunculus germination gibberellin OR smoke OR dormancy`
- `web: Ranunculus floral scent volatiles`
- `web: Ranunculus light photoperiod phototropism`
- `web: buttercup light photoperiod phototropism`
- `web: Ranunculus volatile emission herbivore induced response methyl jasmonate`
- `web: buttercup volatile emission herbivore induced response methyl jasmonate`
- `web: Ranunculus flower opening time anthesis`
- `web: buttercup flower opening time anthesis`
- `web: Ranunculus eye type epidermal focusing`
- `web: buttercup eye type epidermal focusing`
- `web: "Ranunculus repens" light shade photoperiod germination gibberellic`
- `web: "Ranunculus acris" germination light dormancy gibberellic`
- `web: "Ranunculus abortivus" germination light dormancy`
- `web: "Anthecology" "Ranunculus acris"`
- `web: "Ranunculus abortivus" "seed" germination study`
- `web: "Ranunculus repens" "Population dynamics" "light" 1987`
- `web: "Spatial fragrance patterns" "Ranunculus acris" DOI`
- `web: "Anthecology of gynodioecious" Ranunculus journal`
- `web: "Germination studies of Ranunculus abortivus and Ranunculus bulbosus"`
- `web: "Anthecology" "Ranunculus acris" "opening"`
- `web: "Ranunculus repens" "light" "ethylene" gibberellin`
- `web: "10.2307/2260434"`

Twenty-three web queries; returned titles/snippets screened, up to first20 where returned. Any display-truncated result tail and cache abstract segment were read separately from saved raw metadata. Provenance:work/harvest-c12/worker41-Ranunculus-cache.json and worker41-Ranunculus-web1..6.json. No source/full-paper page fetched; no live OpenAlex request.

Eleven target-specific wanted sources passed global DOI/normalized-title comparison against wanted/status/evidence/corrected evidence. R.sceleratus: Korean GA/light/dark seed experiment; intact-plant ethylene/1-MCP/salinity study;1981 long/short-day flowering and GA/ethylene stem responses. R.acris:58-plant sun/shade epidermal experiment; salt/germination response;1995 headspace spatial floral fragrance; primary anthecology/opening study;2023 native-flora germination trial; and plant-diversity/herbivory induced-response experiment. R.repens:1987 high/low light and nutrient factorial experiment. R.abortivus:1976 germination study, retained under10(e), with exact citation and no invented treatment results.

The1976 source is a genuine indexed citation in EurekaMag bibliographies, not an obtained primary paper; get explicitly requests the exact Newsletter of the Association of Official Seed Analysts50(3):56–58 citation. Authors Lincoln WJ/McGuigan M and year1976 are indexed. The1987 repens paper's part number varies II versus III in indexes; III follows the detailed bibliographic entry, with the identical DOI/year/pages independently corroborated. No claim depends on the part numeral. The1995 scent source's DOI/year/pages are verified in a legal PMC reference list and authors in PalDat; primary methods still need checking for intact versus detached material. The anthecology title is indexed in DOAJ; opening sequence, seasonal male/female synchrony and daily anthesis must be distinguished by the reader. Unknown publication years/authors remain null/empty, never inferred from DOI digits or search-relative age. No new year0.

Other dispositions: R.asiaticus horticultural photoperiod studies already have species light evidence and do not fill these targets; auricomus/kuepferi/adoneus/hirtellus/aquatilis/trichophyllus/kadzusensis studies concern other species and are not requested for volume. Cached salt-melatonin asiaticus study is a real living response but outside the queued species. Cut-Ranunculus TDZ/1-MCP vase treatment10.3389/fhort.2023.1183754 is excluded10(a). R.multifidus animal trypanosome assays, medicinal extracts, antimicrobial chemistry and metabolite profiles without experimental cue responses do not establish target sensing. General auxin, LED, insect pollination/colour vision, thermal ecology and plant VOC reviews do not warrant duplicate background requests when direct target sources are available. Korean cantoniensis/chinensis and Mediterranean pond Ranunculus germination sources are outside these targets. No light/chemical/diel null while direct or plausible target candidates remain unread.

Eye_type alone has a completed null under owner10(b), explicitly screening all three cached eye-word hits(Arabidopsis epidermal/stomatal study,insect vision review,green-flower perception study). Glossy-petal reflectance and microscopy focusing are not image-forming eyes. Kew's flower-dish concentration of sun/heat is classified with the required focusing-belongs-under-light phrase; no optical-focusing sensory measurement is asserted from that botanical account. Direct-light epidermal-plasticity source is wanted and does not block an eye-only record.

OpenAlex429/MDPI429/UChicago403/SANBI403 round-wide restrictions respected; no retry, paid API, unauthorized copy, source fetch, evidence log, app check, branch/gate or issue29/30 change. No new service or actual web quota refusal. Managed runtime skill read for current network policy; policy enforced/unrestricted, no credentials bound, no configuration changed. Parent retains audit/application and push/PR responsibilities.

Worker41 Ranunculus checkpoint: actual combined screen_candidates --check completed with `0 problems` for12 searched/151 wanted. Own-file whitespace check passed; unknown-year metadata null. Ready to commit.


## 2026-10-27 — worker41 continuation: Datura and handoff

Worker41 cumulative:2 genera completed(Ranunculus,Datura),2 search records,25 new wanted,0 evidence/measurement closures. Batch cumulative:15/40 genera screened,13 search records,165 wanted,0 evidence;25 remain, next Lunaria. Ranunculus commit8950581b. Stop between genera after validation/commit for fresh-context takeover; no actual web quota refusal.

Original queue targets D.wrightii(22,076 records) and D.stramonium(19,909), both light/chemical/eye_type. Existing sweep-10#10 is D.wrightii diel(abstract), not a chemical or light measurement. Its CO2/nectar-emission source may also be relevant to the chemical row, but is already in evidence and not re-requested. Original queue has no Datura diel gap, so no new daily-opening protocol claimed and no duplicate CO2/diel request. No existing evidence or legacy null altered. Global evidence/corrected evidence/searched/wanted/papers-status checked; thin sweep-10 is not full completion. Canon has no relevant in-hand plant response measurement.

harvest_get.py and screen_candidates.py were run for Datura; no genus harvest exists. All15 cached Solanaceae family-review run17 titles and entire stored abstracts were screened. Family results cover tomato/potato/tobacco/pepper light studies and genomic evolution, Nicotiana/Jaborosa/Solanaceae floral-colour signals and general phytochrome reviews. They are other taxa or background, not target plant-eye measurements; no duplicate crop/model/background request.

Exact successful cached query and actual web queries, in order:
- `Solanaceae photoreceptor review`
- `web: Datura seed germination light dark`
- `web: Datura germination gibberellin OR smoke OR dormancy`
- `web: Datura floral scent volatiles`
- `web: Datura light photoperiod phototropism`
- `web: jimsonweed sacred datura light photoperiod phototropism`
- `web: Datura volatile emission herbivore induced response methyl jasmonate`
- `web: jimsonweed sacred datura volatile emission herbivore induced response methyl jasmonate`
- `web: Datura eye type epidermal focusing`
- `web: jimsonweed sacred datura eye type epidermal focusing`
- `web: "Datura wrightii" germination light dormancy`
- `web: "Datura wrightii" light shade photosynthesis experiment`
- `web: "Datura" "Feeding-induced rearrangement of green leaf volatiles reduces moth oviposition"`
- `web: "Datura" "Effects of light conditions on growth and defense compound contents"`
- `web: "Datura stramonium" "Preliminary studies of seed dormancy"`
- `web: "Datura" "Variation in herbivore and methyl jasmonate-induced volatiles"`

Fifteen actual web queries screened all returned titles/snippets, up to first20 where returned. Four targeted follow-ups resolve exact primary titles, DOI correction and species identity. Cache metadata in work/harvest-c12/worker41-Datura-cache.json; raw tool output worker41-Datura-web1..4.json. No source/full-paper page fetched, no live OpenAlex request. No display-truncated search result left unread.

Fourteen new wanted lines passed global normalized-title/DOI duplicate checks against wanted/status/evidence/corrected evidence. Target stramonium: light-environment/phytochrome seed study;1998 burial/light sensitivity study; physical/chemical dormancy treatment; preliminary dormancy/endosperm/GA/benzyladenine study; Dormancy-breaking Seed Treatments with GA; older PubMed gibberellin/germination study; germination response to pH/salinity/temperature;2019 three-light-condition growth study; and native/non-native induced-leaf-damage VOC study. Target wrightii:2007 herbivore/MeJA-induced genetic-line volatiles; field ontogeny/season MeJA responses; constitutive/jasmonate-inducible traits; feeding/oral-secretions/GLV study comparing100%,20–10%,0% light; and floral-scent attraction/oviposition study. These are direct target primary cue/response experiments, not model-crop background.

The wrightii feeding paper gives a direct controlled-light lead missed by broad photoperiod searches. Its DOI10.7554/eLife.00421 is independently indexed in the legal eLife/PMC correction, which readers should consult. Other compound profiles need intact-versus-detached headspace methods verified before living emission is logged10(a). Seed pH/salinity trials and GA responses count as living chemical-treatment candidates10(d,e), while set12h/16h culture lighting alone does not establish a light response. The const/jasmonate source includes genuine negative treatment contrasts; these are measurements rather than proof that there is no chemical sensing. Unknown years/authors/journals stay null/empty. Year2019 verified by Japanese Botanical Society issue listing and legal bibliographic citations,2007 by PMC bibliography,2006 by author university bibliography,1998 by Wiley label. The older PubMed title has indexed typo PF; preserved rather than silently inventing corrected metadata. No year inferred from DOI/PMID digits or elapsed publication-age labels; no new year0.

Other dispositions: ferox seed phytochrome/GA/expansin papers, inoxia/innoxia seed studies and tissue cultures, metel medicinal results and Brugmansia do not fill these queued species. Tobacco/cotton/cranberry model HIPV papers and plant-communication reviews are background; named direct target experiments prioritized. Datura genome/gene-annotation predictions alone do not establish cue response; comparative herbivory transcriptome work is related primary context but direct target volatile response sources already retained. Essential oils, extracted tropane alkaloids, historical human drug effects, anticholinergic pupil dilation and corneal toxicity do not show plant chemical perception or plant eyes. Practical germination guides, commercial seed pages, weed identification and shade recommendations are not substituted for primary experimental evidence. Variable-impact herbivory source has set germination-chamber lighting but no confirmed light contrast; target feeding/light experiment is retained. Pepperdine student flower-water-stress/light-hypothesis project is adjacent context; the direct controlled-light GLV experiment takes priority. No chemical/light null while target leads remain unread.

Eye_type alone gets completed null under10(b). Explicit screened dispositions cover leaf epidermal identification(stomata/trichomes/crystals/palisade ratio), stem/ovary histology, human pupil/corneal cases and Datura-juice toxicity. No lenslike epidermal focusing source found. Ordinary epidermal cells, human implanted lenses and moth olfactory imaging are not plant image-forming eyes. The existing diel source and all old sweep records remain untouched, with species limitations preserved.

OpenAlex429/MDPI429/UChicago403/SANBI403 remain skipped. Indexed UChicago/MDPI/OpenAlex search hits were not opened or fetched; no request to those services, paid API, proxy/library mirror, full paper text, evidence entry, app check, branch/gate or issue29/30 change. Actual web usage total for this worker:38 successful queries(23 Ranunculus,15 Datura). Parent retains research desk audit/application and push/PR.

Worker41 Datura checkpoint: actual harvest_get/screen_candidates confirm no genus harvest. Combined screen_candidates --check completed with `0 problems` for13 searched/165 wanted; own-file whitespace and metadata counts passed.
