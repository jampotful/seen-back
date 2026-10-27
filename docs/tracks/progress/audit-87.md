# Audit 87: desk-c8 (21 plant genera; branch origin/research/desk-c8, head 576d729a)

## Samples (seed 87), drawn before any record was read

Search records (47 lines): `random.seed(87)`, `random.sample(range(1, 48), 20)`, sorted: 1, 5, 6, 7, 8, 9, 10, 13, 18, 21, 22, 24, 25, 32, 35, 41, 42, 43, 44, 45.

Evidence records: all 15 lines of docs/views/evidence/desk-c8.jsonl are judged, so that any error line can simply be dropped.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of docs/views/searched/desk-c8.jsonl (47 lines) and docs/views/wanted/desk-c8.jsonl (21 lines) prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (the owner's readings 10(a) to 10(e) included) and the rulings of audits 83 to 86, with the launch prompt's two: an unlabelled direct OpenAlex query line is waived (audit 84), and a `chased` DOI that no harvest output prints is an error unless otherwise supported (audit 86 accepted a web-found family review for genera in no harvest run).

Queries. `harvest_get.py` ran without the network (it reads origin/ci). Five sampled records belong to harvest genera: Chamaecrista (lines 9, 10), Sphagneticola (24, 25) and Geranium (32). A script compared their unprefixed `queries` with every `query` and `family review` line the output prints. All five match word for word and in order (Chamaecrista 9 lines, Sphagneticola 11, Geranium 3), with the "web: " lines after them. No harvest shows a failed step for these genera. The other 15 sampled records are for genera in no harvest run and list "web: " lines only. No unlabelled line appears anywhere in the sample.

Chased.
- Chamaecrista names both citation-step DOIs the output prints (10.3389/fpls.2015.00207 and 10.1016/j.tree.2009.09.010, 0 works each) and the Fabaceae family-review DOI 10.1093/jxb/erag313, which the output also prints.
- Sphagneticola names its one citation step (10.1016/j.tree.2009.09.010) and adds the web family DOI.
- Geranium's harvest ran neither a citation step nor a family review, and its record names a web family DOI.
- Cercis (line 1) names 10.1093/jxb/erag313, from its labelled web Fabaceae search. That DOI is in the Chamaecrista harvest output, so it is supported.
- Ten sampled no-run records (5, 6, 13, 18, 21, 35, 42, 43, 44, 45) name 10.1007/s10265-016-0785-4. No file on origin/ci holds it (git grep), but it is otherwise supported. My own "Onagraceae photoreceptor review" and "Cannabaceae photoreceptor review" searches both returned "Evolutionary aspects of plant photoreceptors". The page I opened (nutrition-evidence.com 249643) gives Li and Mathews 2016, J Plant Res 129(2): 115-122, DOI 10.1007/s10265-016-0785-4.
- Celtis (7, 8) names PMC6455078, which my Cannabaceae search returned first.
- Asplenium (22) and Lygodium (41) give a reason: fern neochrome results with no Asplenium or Lygodium measurement.

As in audit 86, I accept these web family reviews and count none of them.

Screened. I read up to three entries per record against the record's reasons and my own result lists. Most screened entries are extension, flora and encyclopedia pages, or the general focusing set (PMC9824129, nature.com 075535b0). None reports a measurement of the record's trait in a species of the genus.

Searches. I ran 46 WebSearches:
- 12 for evidence and taxonomy checks;
- two or more of my own for each sampled non-eye_type record: Ligustrum, Chamaecrista, Rivina, Geranium, Melothria and Ludwigia for sense_chemical, and Cercis, Erechtites, Celtis, Sphagneticola, Asplenium and Monotropa for diel;
- three pooled focusing searches for the eight eye_type records;
- two family-review checks and two for wanted lines.

I fetched only URLs my searches returned. I left one result on a library proxy (0-www-mdpi-com.brum.beds.ac.uk) and one academia.edu result alone.

Deviation noted, not counted. desk-screen point 2 asks for two searches per trait, "<Genus> <trait words>" and "<common name> <trait words>". This unit runs one merged search instead ("Cercis OR redbud flower opening time anthesis"), where desk-c7 ran the pair. Ludwigia (lines 42, 43) and Melothria (35) also skipped the scent or jasmonate search that 10(e) asks for, and the Ludwigia note says so ("budget"). Audit rule 4 counts a protocol shortfall only through a miss it causes, so I ran the missing searches myself (below) and found no miss.

## Search record verdicts (sample of 20)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cercis diel | ok. Web-only, chased supported. My two searches returned redbud bloom-season guides, the Arnold Arboretum story, NPN phenology and a cultivar patent. None gives an hour of opening. |
| 5 | Erechtites diel | ok. Web-only. My searches returned flora pages, Eberle et al. 2014 on Echium (PMC4245144, opened: no Erechtites) and Ossa and Medel 2011 on Echinopsis (Gayana Bot 68(2), opened). No Erechtites opening hour. |
| 6 | Erechtites eye_type | ok. Web-only. The general focusing works carry the owner's wording. My pooled search returned only the general set (PMC8309337, FIU cas_bio/44, AskNature). |
| 7 | Celtis diel | ok. Web-only. My searches returned the Celtis floral morphogenesis paper (title only, breeding system), NPN and allergy pages. No hour. |
| 8 | Celtis eye_type | ok. Web-only. Nothing on Celtis focusing came back. |
| 9 | Chamaecrista eye_type | ok. Queries match (9 harvest, 4 web), and both citation steps are named. The Lotus nodule paper carries the owner's wording. |
| 10 | Chamaecrista sense_chemical | ok. Queries match. The ten screened works hold no Chamaecrista chemical response. My searches returned the C. fasciculata extrafloral-nectar study (par.nsf.gov 10654012, opened: leaf age and nectar removal, no hormone or volatile applied) and a C. rotundifolia dormancy study (SciELO Ciência Animal Brasileira, opened: hot water and HCl scarification only). |
| 13 | Rivina sense_chemical | ok, with a fork. Web-only. My searches returned Teresa and Anitha 2000 (J Environ Biol 21(3): 207-209, wildflower.org record opened), in which ammonia fumes on living Rivina humilis caused foliar injury and loss of chlorophyll and carotenoid. I read this as pollutant injury rather than a response to a cue, and main logs no such work under sense_chemical. If the desk reads 10(a)'s "chemical or airborne cue" to cover fume injury, this line becomes an error. |
| 18 | Ligustrum sense_chemical | ok. Web-only. My searches returned Althaus-Ottmann et al. 2012 on L. lucidum (Acta Sci Biol Sci 34(3), DOAJ opened: storage only, no chemical) and the Woody Plant Seed Manual entry for Ligustrum (fs.usda.gov, opened). That entry's only growth-regulator result is for rooting cuttings, which the cut-branch rule excludes. |
| 21 | Zanthoxylum eye_type | ok. Web-only. Nothing on Zanthoxylum focusing came back. |
| 22 | Asplenium diel | ok. Web-only. My searches returned work on Onoclea (Harvard OEB news, opened: seasonal only) and Rodríguez de la Cruz et al. 2010 on fern-spore aerobiology (gredos.usal.es, opened: bracken only, no Asplenium). |
| 24 | Sphagneticola diel | ok. Queries match (11, 5), and the citation step is named. My searches returned Mamut et al. 2018 on Heteracia (Biodiversity Science 26(5), opened) and a S. trilobata leaf anatomy paper (IIUM 100094, opened). No hour of opening. |
| 25 | Sphagneticola eye_type | ok. Queries match. The cosmetic, bee-nesting and macular pages are rightly screened. |
| 32 | Geranium sense_chemical | ok. Queries match (3, 6); the harvest ran no citation step. My searches returned Baskin and Baskin 1974 on G. carolinianum (Oecologia 16(3), scholars.uky.edu opened), which gives a light and dark result only, for a different trait. Geranium's harvest header lists no open traits, so this record may duplicate an older one (noted, not counted). |
| 35 | Melothria sense_chemical | ok. Web-only. My searches returned seed-shop and flora pages and fruit volatiles of Solena amplexicaulis, another genus. No Melothria chemical trial. |
| 41 | Lygodium eye_type | ok. Web-only. Nothing on Lygodium focusing came back. |
| 42 | Ludwigia eye_type | ok. Web-only. My pooled search returned a systematics paper on the foliar epidermis of West African Ludwigia (title only: taxonomy, no optics). |
| 43 | Ludwigia sense_chemical | ok. Web-only. My searches returned allelopathy work in which Ludwigia exudates act on other species (Ludwigia is the source, not the responder) and general herbivore-volatile papers. No Ludwigia response. |
| 44 | Monotropa diel | ok. Web-only. My searches returned flora, extension and pollinator pages. No hour of opening. |
| 45 | Monotropa eye_type | ok. Web-only. Nothing on Monotropa focusing came back. |

Search record errors: 0 of 20.

## Evidence record verdicts (all 15)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cercis canadensis sense_chemical | ok. thekeep.eiu.edu/theses/3266 opened: Hosokawa 1977, "Gibberellic acid was found to substitute for stratification." A hormone response of living seed (10(d)); grade m. |
| 2 | Cercis canadensis sense_light_nonvisual | ok. Same page: "Germination occurred in either light or dark conditions." |
| 3 | Centrosema pubescens diel | ok. Museu Goeldi page opened: Borges 2006, 1(1): 31-38, 10.46357/bcnaturais.v1i1.755, and the quote is verbatim. The Tropical Forages factsheet (lucidcentral, opened) gives C. pubescens Benth. as the accepted name. |
| 4 | Ipomoea purpurea diel | ok. UNL page opened: Esther Pearl Hensel 1905, and the quote is verbatim (4:00 to 5:00 A.M., greenhouse). |
| 5 | Ipomoea quamoclit diel | ok. UEM page opened: Terada et al., Acta Sci Anim Sci 27(1): 137-143. The sentence holds. |
| 6 | Ipomoea batata diel | ok. Same sentence. The taxon copies the abstract's "I. batata", but the accepted name is Ipomoea batatas (noted, not counted, since the genus is right). |
| 7 | Ipomoea batatas sense_chemical | ok. PMC6874613 opened: Meents et al. 2019, Sci Rep 9: 17431. DMNT induces sporamin activity in neighbouring living plants (10(a)). |
| 8 | Ipomoea purpurea sense_chemical | ok. udec.cl page opened: Atala, Quilodrán and Molina-Montenegro 2014, Gayana Bot 71(2): 181-187. The Spanish abstract holds the result, and the record's English quote matches the ANID record. Living plants responding to volatiles (10(a)). |
| 9 | Nandina domestica sense_chemical | ok. Korea University record opened: Rhie et al. 2016, Sci Hortic 210: 180-187, and the quote is verbatim. |
| 10 | Lepidium apetalum sense_light_nonvisual | ok. AGRIS record opened: Zhang et al. 2020, Plants 9(3), 10.3390/plants9030333: "Light promoted germination." |
| 11 | Lepidium apetalum sense_chemical | ok. Same record, and the GA3 sentence is verbatim. |
| 12 | Commelina benghalensis sense_light_nonvisual | ok. Miyazaki repository opened: Matsuo et al. 2004, Weed Biol Manag 4(3): 148-153, and the quote is verbatim. |
| 13 | Ludwigia hyssopifolia sense_light_nonvisual | ok. Taiwania page opened: Jayasuriya and Phartyal 2024, 69(1): 50-56. The page gives DOI 10.6165/tai.2024.69.50, which the record could carry. |
| 14 | Ludwigia perennis sense_light_nonvisual | ok. Same abstract, which covers both species. |
| 15 | Ludwigia ravenii sense_light_nonvisual | ok. Castanea page opened: Krings and Miller 2026, 91(1). Shade at 0, 40 and 90% is a set-light-intensity trial (10(d)), and the quote is verbatim. |

Evidence errors: 0 of 15. All values come from abstracts and are marked `partial`, as the progress note says. Quotecheck against full texts has not been run.

## Counts

Search records: 0 of 20, 0%. Evidence: 0 of 15, 0%. The unit as judged: 0 of 35.

Pooled with the desk's other audits of desk-screen units, using audit 86's figures as written (39 search-record errors in 945, plus audit 86's evidence sample of 2 in 10):
- Search records: 39 in 965, 4.0%.
- With the evidence samples included: 41 in 990, 4.1%.
- Under audit 84's waiver of unlabelled OpenAlex lines (audit 86's alternatives): 32 in 965 (3.3%) or 26 in 965 (2.7%).

Two forks would change the count:
1. If the desk reads ammonia-fume injury as a sense_chemical response, search line 13 fails. That gives 1 of 20, exactly 5%, and 15 more records would need drawing.
2. If the desk reads the web-found 10.1007/s10265-016-0785-4 as unsupported (the fork audit 86 set out), the ten sampled records that name it fail (lines 5, 6, 13, 18, 21, 35, 42, 43, 44 and 45).

I hold to audits 83, 85 and 86 on both.

**Verdict: pass.**

**Error lines to drop:**
- docs/views/searched/desk-c8.jsonl: none.
- docs/views/evidence/desk-c8.jsonl: none.

## Wanted lines (listed, not counted)

- Line 1 (Kumar, Sridhar and Malaviya 2014, Range Manag Agrofor 35(1): 151-156): authors, year and journal match the AGRIS record I opened. That record gives no DOI either.
- Line 21 (Gimenes, Ludwigia elegans): the year field reads "None", but the SciELO page I opened dates the issue to November 2003. Its abstract says the flowers "open simultaneously in the morning", so the Ludwigia diel cell probably has a measurement, and the unit was right to hold it out of the search records. My search also returned "Chronobiologic appraisal of the relation between ludwigia elegans flowers and its more frequent visiting bees" (1991, repositorio.usp.br 000832105, not opened), a second lead for the same cell.
- Lines 6 to 10, 12, 14, 15 and 21 carry the string "None" in `year`, and 17 of the 21 lines leave `authors` empty. Empty authors follow point 6, but the "None" string is placeholder text that would reach the owner's page.
- No other wanted line was checked against a page.

## Leads

- Rivina sense_chemical: Teresa and Anitha 2000 (above), if the desk counts fume injury.
- Geranium sense_chemical: a Weed Science 64(3) paper (10.1614/WS-D-15-00136.1, "Effects of Environmental Factors on Seed Germination and Seedling Emergence ...") came back for a Geranium germination search. Its page served metadata only, so I could not see the species or treatments.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC7154808 served a bot check, so I used AGRIS instead. PMC12246837 hit an unanswered permission request, so I used par.nsf.gov instead.
- link.springer.com 10.1007/BF00345883 hit an unanswered permission request. wicri-demo.istex.fr was blocked by robots, the DOAJ page daa2b361 failed at the site, and two uchile pages and one conicet DSpace page served headers only.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
