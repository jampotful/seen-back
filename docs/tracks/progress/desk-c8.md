# desk-c8: plant genera screen (27 October 2026, branch research/desk-c8)

Worktree /tmp/dc8, unit name desk-c8 (addlog.py and the gates accepted it).

## Genera
Done (21): Cercis, Centrosema, Erechtites, Chamaecrista, Celtis, Rivina, Sphagneticola, Pteridium, Asplenium, Ipomoea, Nandina, Ligustrum, Zanthoxylum, Geranium, Lepidium, Melothria, Commelina, Lygodium, Pilea, Ludwigia, Monotropa.
Skipped: Lonicera. `harvest_get.py Lonicera` shows its first query ("Lonicera phytochrome photoreceptor") as "None hits (error gave up)", so desk-screen point 6 bars a search record until a rerun repairs it.

## Cells closed by a measurement (15 evidence records in docs/views/evidence/desk-c8.jsonl, all abstract-level and `partial`)
- Cercis canadensis: sense_chemical (GA3 substitutes for stratification) and sense_light_nonvisual (germinates in light or dark), Hosokawa 1977 thesis.
- Centrosema pubescens: diel (anthesis diurnal), Borges 2006.
- Ipomoea: diel (I. purpurea 4:00-5:00 AM, Hensel 1905; I. quamoclit and I. batata open 6h, Terada et al. 2005); sense_chemical (I. batatas DMNT volatile, Meents et al. 2019; I. purpurea twining induced by volatiles, Atala et al. 2014).
- Nandina domestica: sense_chemical (GA3 substitutes for warm stratification), Rhie et al. 2016.
- Lepidium apetalum: sense_light_nonvisual and sense_chemical, Zhang et al. 2020.
- Commelina benghalensis: sense_light_nonvisual, Matsuo et al. 2004.
- Ludwigia: sense_light_nonvisual (L. hyssopifolia, L. perennis: Jayasuriya and Phartyal 2024; L. ravenii shade levels: Krings and Miller 2026).

## Search records (docs/views/searched/desk-c8.jsonl): 47 lines
Written only for the traits left open after the above and after the wanted leads: see the file. Chamaecrista and Geranium sense_light_nonvisual get no record because main already holds a value.

## Wanted lines (docs/views/wanted/desk-c8.jsonl): 21
Centrosema pubescens GA3/KNO3 (Kumar et al. 2014); Celtis australis GA3 (Zarafshar et al. 2012); Celtis caucasica shade trial; Erechtites hieraciifolius dormancy (Weed Science 65(2)); Ipomoea lacunosa and I. asarifolia germination; Zanthoxylum x5; Asplenium nidus GA3 thesis (1982) and fern spore germination review; Sphagneticola trilobata monoterpene release; Pteridium bracken jasmonate volatiles and P. caudatum fire; Nandina shading trials x2; Lepidium virginicum hormones (no authors on the page); Pilea melatonin/AVG in darkness and Pilea photoperiod/light quality; Ludwigia elegans anthesis.

## Faults and limits to know
- OpenAlex: api.openalex.org returns 403 to CONNECT from this machine (proxy policy denial), and WebFetch of it was left unanswered. No live OpenAlex query was run; no unlabelled direct query appears in any record. All new searches are WebSearch, labelled "web: ". For the six harvest genera (Chamaecrista, Sphagneticola, Pteridium, Nandina, Geranium, Pilea) the cached harvest queries are copied word for word.
- Citation step: the plant protocol's family review was run as a WebSearch ("<Family> photoreceptor review"), and `chased` names a DOI or URL that search printed, or the harvest's citation-step DOIs.
- WebFetch was refused ("permission request not answered") for: bioone Weed Science Erechtites paper, pmc.ncbi.nlm.nih.gov PMC3502421 (bracken jasmonate), J-STAGE hortj 89_UTD-208 (Pilea melatonin), doi.org/10.21273/jashs.105.6.812 (Pilea photoperiod). Not retried.
- Evidence quotes come from WebFetch summaries asked to quote verbatim; quotecheck against the PDFs has not been run.
- Search coverage per genus was lean (germination-light, germination-GA, anthesis, focusing, family review; scent/jasmonate only where flowers or herbivores were obviously involved), so a reader should treat the null records as title-and-snippet screens.

## Desk disposition after audit 87 (27 October 2026)

Audit 87: 0 errors in 20 sampled search records and 0 in all 15 evidence records. All 47 search records and 15 evidence records are merged. Rulings on the audit's two forks: ammonia-fume injury on Rivina humilis (Teresa and Anitha 2000) is tissue damage from a pollutant and is not read as a sense_chemical response, so search line 13 stands; the web-found family review 10.1007/s10265-016-0785-4 is accepted for genera in no harvest run, as for audit 86. Lonicera was not screened (the harvest shows "error gave up" on its first query) and stays in the queue. The null records are title-and-snippet screens because OpenAlex returned a proxy 403 to the unit.

Wanted lines: 10 of 21 merged (7 filled with registry authors from Crossref run desk-wanted-63, 3 already carried authors). The other 11 name a landing page with no DOI and no authors and wait for a source with authors.
