# Audit 79: harvest-c22 (branch research/harvest-c22, head bbd25b54)

Gate: `screen_candidates.py --check` on the 35 search records and 15 wanted lines prints "0 problems".

## Sample

`random.seed(79)` and `random.sample` over lines 1 to 35 give 10, 29, 23, 11, 8, 31, 24, 33, 16, 5, 3, 12, 1, 7, 4, 27, 35, 6, 14, 20. The first draw held errors, so per the desk's rule 15 more were drawn with `random.seed(7915)` from the other 15 lines: 34, 13, 26, 19, 9, 18, 28, 21, 25, 15, 32, 2, 30, 17, 22. The two draws cover the whole unit.

## Method

Judged against desk-screen.md, point 10 included, with the owner's readings of 25 October 2026 as the launch prompt states them: plant sense_chemical counts living responses, responses to hormones or elicitors included, and volatile signalling; extracts, oils and cut-flower treatments do not count; plant eye_type is "none" for every plant, with epidermal focusing logged under sense_light_nonvisual. For the scope of sense_light_nonvisual I followed main's evidence, which logs light-intensity, shade and light-for-germination responses under that trait (Cochemiea grahamii seeds needing light, Pinus pinaster seedlings in sun against lateral light and shade, Geranium robertianum under far-red enrichment, Silene gallica germination under a wheat canopy). For hormones I followed main's MeJA and ethylene rows (oa-13b:473 and 474) and its gibberellin rows (oa-9: Vittaria, Cyathea australis, Cibotium barometz and others).

`harvest_get.py` prints "in no harvest run yet" for all 13 genera, and `screen_candidates.py` lists no works, so every record's `queries` correctly hold only its two "web: " searches, and every `chased` field ("no citation step ran ... closest = none") is a none-reason the harvest output supports. Only records 9, 10 and 17 have `screened` entries (PMC5439701 for Agropyron diel; 10.1086/683278 for the Agropyron and Alopecurus eye_type records, with the owner's wording); both judgements hold by title. Step (c) therefore reduces to these three entries, and step (d) carries the audit.

I ran 57 WebSearches (of 60) and opened the pages named below, every one returned by my own searches. Three fetches met bot checks and one went unanswered; none was retried. Two proxy-mirror results were left closed (springerlink.bibliotecabuap.elogim.com in the Centaurium search, 0-bmcplantbiol-biomedcentral-com.brum.beds.ac.uk in the Caragana search). No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened, and no paper text is committed.

## Verdicts, first draw (seed 79)

| Line | Record | Verdict |
|---|---|---|
| 10 | Agropyron eye_type | ok. Web queries only, as the harvest allows. The grass-epidermis paper is screened with the owner's wording. My shared focusing searches returned the leaf-optics review, the Selaginella silica-body paper and Bone et al. 1985; nothing on Agropyron. |
| 29 | Simmondsia eye_type | ok. The same shared focusing searches found nothing on Simmondsia. |
| 23 | Staphylea eye_type | ok. The same searches found nothing on Staphylea. |
| 11 | Caladenia diel | ok. My searches returned pollination studies of Caladenia arenaria, C. concolor and C. nobilis (wasp visitation) and the waterlily auxin paper; no hour of flower opening in a Caladenia. |
| 8 | Centaurium sense_chemical | **error**. Matekalo et al. 2018, "Organ-specific and genotype-dependent constitutive biosynthesis of secoiridoid glucosides in Centaurium erythraea Rafn, and its elicitation with methyl jasmonate", Phytochemistry 155: 69-82, 10.1016/j.phytochem.2018.07.015 (IBISS repository record and Zenodo page opened): MeJA raised secoiridoid glucoside production and reprogrammed the pathway genes. Also Lukić et al. 2018 (Belgrade conference abstract, IBISS repository): 250 µM MeJA in the medium of C. erythraea shoot cultures raised swertiamarin several-fold, with five pathway genes up after five days. Whether Matekalo et al. treated whole plants or cultures is not shown; by point 3 a work that may hold the measurement keeps the trait out of the record either way. Božunović et al. 2019 (Plants 8(12): 589, 10.3390/plants8120589) treats wounding, a mechanical cue. |
| 31 | Liatris eye_type | ok. My shared focusing searches found nothing on Liatris. |
| 24 | Staphylea sense_chemical | ok. My searches returned induced-defence pages on other taxa and a Ptelea floral-scent paper (JASHS 2021); no Staphylea response or scent work. |
| 33 | Caragana eye_type | ok. My shared focusing searches found nothing on Caragana. |
| 16 | Scaevola sense_chemical | ok. My searches returned jasmonate papers on other plants and an Asarum scent abstract (ESJ 73); no Scaevola work. |
| 5 | Erysimum sense_light_nonvisual | ok, one lead unread. My searches returned photoperiod teaching pages, a Sinapis alba vernalization thesis (Liège) and a sunflower photoperiod paper. The Michigan State "vernalization part 5" PDF, which may list wallflowers, met a bot check; vernalization is a temperature response in any case. |
| 3 | Phlomoides sense_chemical | ok. My searches returned an elicitor study on common bean (Farouk and Osman 2009) and Polianthes tuberosa scent papers; nothing on Phlomoides or Phlomis tuberosa. |
| 12 | Caladenia eye_type | ok. My shared focusing searches found nothing on Caladenia. |
| 1 | Phlomoides diel | ok. My searches returned a Syringa flowering paper (Acta Agrobotanica 2013) and a Heteracia paper (Biodiversity Science 2018), both with morning opening hours for other genera; no Phlomoides. |
| 7 | Centaurium eye_type | ok. My shared focusing searches found nothing on Centaurium. |
| 4 | Erysimum eye_type | ok. The same searches found nothing on Erysimum. |
| 27 | Hylotelephium eye_type | ok. The same searches found nothing on Hylotelephium. |
| 35 | Caragana sense_light_nonvisual | **error**. Yan et al. 2015, "Characteristics of seed germination and seedling growth of Caragana korshinskii under different light intensities", Chinese Journal of Ecology 34(4): 912 (journal page opened; DOI field empty): seeds and seedlings under 55.4, 18.9, 5.5, 2.2 and 0.5% of sunlight; germination peaked at 18.9%, and height, specific leaf area and root:shoot ratio shifted with light. Zhang et al. 2018 (same journal, 37(11): 3262) adds light-by-burial effects on germination. The record's trait words ("photoperiod phototropism light response flowering") steered both searches to teaching pages. |
| 6 | Centaurium diel | ok. My searches returned Štenc et al. 2023 on pollen-release timing, whose three species are Succisa, Centaurea and Trifolium (Charles University record), and centaury wildlife pages; no hour of opening in a Centaurium. |
| 14 | Scaevola diel | ok, one lead unread. Swensen et al. 2024 (Front Plant Sci 15, 10.3389/fpls.2024.1281797) gives floral stages and visitation hours (0900 to 1500) and no opening hour. The Hawaii thesis "Pollination biology of Hawaiian Scaevola (Goodeniaceae)" (scholarspace.manoa.hawaii.edu) met a bot check and may hold anthesis timing. |
| 20 | Viscaria sense_chemical | **error**. Jürgens 2004, "Flower scent composition in diurnal Silene species (Caryophyllaceae): phylogenetic constraints or adaption to flower visitors?", Biochemical Systematics and Ecology 32(10): 841-859 (AGRIS record opened; DOI not shown): floral scent of ten day-flowering Silene species collected by dynamic headspace and analysed by GC-MS, 40 compounds in S. viscaria, which is Viscaria vulgaris. Main logs headspace floral scent of living flowers under sense_chemical (Primula beesiana). The abstract does not say whether the flowers were attached, so by point 3 the work belongs on the wanted list and the trait out of the record. |

First draw: 3 errors in 20, 15.0%.

## Verdicts, second draw (seed 7915)

| Line | Record | Verdict |
|---|---|---|
| 34 | Caragana sense_chemical | **error**. Ji et al. 2017, "Identification of two CiGADs from Caragana intermedia and their transcriptional responses to abiotic stresses and exogenous abscisic acid", PeerJ 5: e3439, 10.7717/peerj.3439 (PeerJ page opened): 2- to 3-week seedlings in water culture given 200 mM NaCl with ABA at 0 to 200 µM; CiGAD1 and CiGAD2 transcripts in roots and leaves shift with ABA dose and time against the salt-only control. A living hormone response. Main holds no ABA row yet, so this is the first of its kind. |
| 13 | Caladenia sense_light_nonvisual | ok, one weak lead. Janissen et al. 2022 (Aust J Bot 70(4): 275-291, 10.1071/BT21085) germinated C. robinsonii in darkness only. A 1997 Australian Orchid Foundation progress report (Cross, Royal Botanic Gardens Melbourne) says photoautotrophic conditions lowered Caladenia germination, attributed to light inhibiting the fungus; no species, values or peer review, so it is a lead. |
| 26 | Hylotelephium diel | ok. My search returned cultivar pages and 't Hart and van Arkel 1985 on photoperiod in Sedum telephium (see Leads); no opening hour. |
| 19 | Viscaria eye_type | ok. My shared focusing searches found nothing on Viscaria. |
| 9 | Agropyron diel | ok. My searches returned GRIN accession pages and wheat anther-extrusion papers (Zajączkowska et al. 2021; De Vries 1973); no Agropyron opening hour. PMC5439701 is correctly screened by title. |
| 18 | Alopecurus sense_chemical | ok. Li et al. 2014 (PLoS ONE 9(6): e101331, 10.1371/journal.pone.0101331) measured aphid-induced volatiles in Festuca pratensis and Schedonorus phoenix only; no Alopecurus work found. |
| 28 | Hylotelephium sense_chemical | ok. My searches returned tulip, tomato and generic volatile papers; no Hylotelephium response. |
| 21 | Viscaria sense_light_nonvisual | ok. My search returned germination studies of other Silene species (Brullo and Salmeri 2022; Kırmızı et al. 2013); none includes S. viscaria. |
| 25 | Staphylea sense_light_nonvisual | **error**. Zhang et al. 2017, "Effect of Different Light Intensities on Growth of 1-year Staphylea bumalda Seedlings", Zhejiang Forestry Science and Technology 37(6): 79-82, 10.3969/j.issn.1001-3776.2017.06.014 (journal page opened): seedlings under 100, 39.87 and 11.21% of full light; moderate shade gave the greatest height, diameter, leaf size and biomass. The same kind of light response as line 35. |
| 15 | Scaevola eye_type | ok. My shared focusing searches found nothing on Scaevola. |
| 32 | Liatris sense_chemical | **error**. Park, Suh, Chun and Choi 1986, "Studies on the Dormancy of Liatris spicata Corm I. Study on the Induction and Awakening of Dormancy and Effect of Gibberellin Treatment on the Breaking of Dormancy", Current Research on Agriculture and Life Sciences 4: 18-21 (KoreaScience page opened): a 1-hour soak in 200 ppm GA broke corm dormancy, more strongly the deeper the dormancy. A living hormone response of the kind main logs from oa-9. Janowska et al. 2018 (Hort Sci Prague 45(4): 205-210) cites a benzyladenine spray on L. spicata 'Alba' (Pogroszewska and Sadkowska 2008b) as a further lead. |
| 2 | Phlomoides eye_type | ok. My shared focusing searches found nothing on Phlomoides. |
| 30 | Simmondsia sense_chemical | **error**. Prat, Botti and Fichet 2008, "Effect of plant growth regulators on floral differentiation and seed production in Jojoba (Simmondsia chinensis (Link) Schneider)", Industrial Crops and Products 27: 44-49, 10.1016/j.indcrop.2007.07.001 (Universidad de Chile repository opened): foliar benzyladenine raised flower numbers on 5-year-old plants of two clones and enlarged the flower meristem in one; GA4+7 lowered flower numbers. Jojoba seed germination under salinity with GA and kinetin (jijas.ut.ac.ir article 16258) and Singh et al. 2008 on micropropagation (Biologia Plantarum 52(3): 538-542, in vitro) are further leads. |
| 17 | Alopecurus eye_type | ok. The grass-epidermis paper is screened with the owner's wording, and my shared searches found nothing on Alopecurus. |
| 22 | Staphylea diel | ok. Garwood and Horvitz 1985 (Am J Bot 72(3): 453-466, 10.1002/j.1537-2197.1985.tb05369.x) treats fruit set of S. trifolia; its abstract gives no opening hour. |

Second draw: 4 errors in 15.

## Counts

Errors: 7 of 35, 20.0% (first draw 3 of 20, 15.0%). Pooled with audits 43 to 51, 55 to 73 and 75 to 78 (13 errors in 724 records): 20 in 759, 2.6%. The unit is above 5% and fails.

Three of the seven errors (30, 32, 34) rest on the launch prompt's reading that hormone responses count. If the owner reads growth-regulator sprays, soaks and ABA dosing as outside sense_chemical, those three become ok and the unit has 4 errors in 35, 11.4%, still above 5%. Lines 8 and 20 stand under any reading, since point 3 keeps a trait out of the record while a work may hold its measurement.

Pattern. All 35 records are web-only, and the four trait phrasings decided what the searches could find. The sense_chemical phrase ("volatile emission herbivore induced response methyl jasmonate") returned the same generic induced-volatile pages for every genus, and the sense_light_nonvisual phrase ("photoperiod phototropism light response flowering") returned photoperiod teaching pages; my shorter genus-plus-hormone and genus-plus-light-intensity searches found five of the seven misses on the first page.

Because the two draws cover the whole unit, the desk can drop the error records and merge the rest: **drop lines 8, 20, 25, 30, 32, 34 and 35** of docs/views/searched/harvest-c22.jsonl (Centaurium sense_chemical, Viscaria sense_chemical, Staphylea sense_light_nonvisual, Simmondsia sense_chemical, Liatris sense_chemical, Caragana sense_chemical, Caragana sense_light_nonvisual). The 28 other records stand. The seven cells then wait for the works above on a wanted list.

## Wanted lines (listed, not counted)

All 15 lines leave `authors` empty, so none is counted. None of their DOIs or URLs is on main's wanted, evidence or sources files. Checked against pages my searches returned:
- Line 11: Tel-Zur, Rothschild, Vaknin et al., "Characterization of Flowering Time and Pollen Production in Jojoba (Simmondsia chinensis) towards a Strategy for the Selection of Elite Male Genotypes", Agronomy 10(4): 592, 2020, 10.3390/agronomy10040592 (MDPI reprints page). The line carries year 0 and no DOI; both can be filled.
- Line 13: Stawiarz and Wróblewska, 10.5586/aa.2014.033; year 2014 agrees. The abstract gives the flowering period and flower lifespan and no hour of opening, so the diel reading depends on the full text.
- Line 15: Chen, Zuo and Zhao 2020, "Comparative Floral Characters, Pollinator Limitation, and Pollination Success in Different Habitats of Caragana microphylla Lam", Frontiers in Ecology and Evolution 8: 170, 10.3389/fevo.2020.00170 (Frontiers PDF). It reports complete opening and pollen release between 09:00 and 15:00, a likely Caragana diel measurement.
- Lines 2 and 9: searches for the DOIs returned other Thieme items and repository listings without titles, so both stay unconfirmed.
- The other lines were not checked against a page.

## Leads

- Hylotelephium sense_light_nonvisual (a wanted cell in this unit, no record): 't Hart and van Arkel 1985, "Quantitative aspects of the influence of day-length and temperature on Sedum telephium (Crassulaceae)", Acta Botanica Neerlandica 34(1): 115-118 (natuurtijdschriften.nl page opened), on the long-day flowering of S. telephium, which is Hylotelephium telephium. A stronger lead than wanted line 10.
- Scaevola diel: the Hawaii thesis named under line 14.
- Liatris sense_chemical: Pogroszewska and Sadkowska 2008b, cited under line 32.
- Caladenia sense_light_nonvisual: the 1997 Australian Orchid Foundation progress report named under line 13.

## Blocked pages

- radar.ibiss.bg.ac.rs/handle/123456789/3146 (human verification; its ?show=full page served the record).
- pmc.ncbi.nlm.nih.gov PMC9977281 (reCAPTCHA); the Charles University record served the paper.
- scholarspace.manoa.hawaii.edu "Pollination biology of Hawaiian Scaevola" (Turnstile).
- canr.msu.edu vernalizationpart5.pdf (Incapsula).
- aminer.org redirect for "Interlinked regulator loops of ABA and JA respond to salt and drought" (permission not answered; not retried).
