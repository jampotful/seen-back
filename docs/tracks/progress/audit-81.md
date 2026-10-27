# Audit 81: harvest-c23b (branch research/harvest-c23b, head 8f0cfe10)

Gate: `screen_candidates.py --check` on the 37 search records and 9 wanted lines prints "0 problems".

## Sample (seed 81)

`random.seed(81)` and `random.sample(lines, 20)` over the 37 search record lines (1-based) give, in draw order, 33, 30, 22, 25, 31, 2, 6, 5, 15, 35, 34, 20, 1, 11, 10, 12, 8, 23, 36 and 3. The draw was made before any record was read.

The sample found errors, so the desk's 15-record extension ran: `random.seed(8115)` and `random.sample(<the 17 undrawn line numbers in ascending order>, 15)` draw 13, 26, 24, 21, 16, 4, 27, 28, 17, 19, 9, 37, 7, 14 and 32. Lines 18 and 29 were in neither draw.

## Method

Judged against desk-audit.md and desk-screen.md, point 10 included, with the readings in force as the launch prompt gives them: plant sense_chemical counts living responses, responses to applied hormones or elicitors included, and volatile signalling, while extracts, oils, hairy-root cultures and cut-flower or excised-tissue chemistry do not count; plant diel means flower opening and scent timing (CAM gas exchange does not count); growth or germination trials under set light intensities count under sense_light_nonvisual. Main logs germination responses to smoke under sense_chemical (Epacris tasmanica) and light requirements for germination under sense_light_nonvisual, and I followed it on both.

Armoracia and Mentha are the only genera with a harvest run. For their three drawn records (1, 32, 33) a script compared the non-web `queries` with the harvest's `query` and `family review` lines: all match word for word and in order, and each adds its labelled web searches. `harvest_get.py` prints "in no harvest run yet" for the other nine genera, so those records correctly hold web searches only. No harvest shows a failed step. No record names a DOI in `chased`; the none-reasons ("no citation step printed", or no harvest run with OpenAlex unreachable) are what the output supports. Record 1 names all 20 sense_chemical candidates the tool lists for Armoracia, and I judged its screened entries from the harvest titles and abstract starts (all 20 hold no living Armoracia response). Record 32's five screened works are a poplar isoprene paper, Croton essential oils, honeybee learning, a review of tissue content and a Clarkia linalool review, correctly screened. The web-only records have empty `screened` fields, so step (d) carries the audit.

I ran 49 WebSearches (of 60) and opened only pages my own searches returned. Two proxy-mirror results (0-www-mdpi-com.brum.beds.ac.uk) were left closed. No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened, and no paper text is committed.

## Verdicts, first draw (seed 81)

| Line | Record | Verdict |
|---|---|---|
| 33 | Mentha eye_type | ok. Queries match (6 harvest, 2 web). My focusing search returned the leaf-optics review (PMC8309337) and the FIU lens-cell paper; nothing on Mentha. |
| 30 | Themeda diel | ok. My searches returned "Environmental control of reproduction in Themeda australis" (Aust J Bot 17(3): 375-389, 1969, 10.1071/BT9690375, CSIRO page opened), a day-length and vernalization study with no hour of floret opening, and flora pages. See Leads. |
| 22 | Dermatophyllum eye_type | ok. My pooled focusing search found nothing on the genus. |
| 25 | Himantoglossum eye_type | ok. My orchid petal-epidermis search returned general conical-cell work; nothing on Himantoglossum. |
| 31 | Themeda eye_type | ok. Same pooled search as line 22. |
| 2 | Bellardia diel | ok. My pollination search returned floral-biology papers on other genera; no hour of opening in Bellardia. |
| 6 | Eriophorum diel | ok. My search returned grass pollen-release studies on other taxa; no Eriophorum timing. |
| 5 | Bellardia sense_light_nonvisual | **error**. Tucci GF and Melchionna M, "Ecologia della germinazione dei semi di Bellardia trixago (L.) All.", Delpinoa n.s. 20 (1978 [1979]): 87-97 (Orto Botanico di Napoli PDF, returned by my search on Bellardia germination requirements): fresh seeds germinated in light and almost not at all in darkness at room temperature; from November to April light-exposed seeds reached 90 to 100% in about six days while dark-incubated seeds stayed near zero. A light requirement for germination, the kind main logs. |
| 15 | Sapindus sense_chemical | ok. My searches returned S. mukorossi saponin papers on field-grown trees with no applied hormone (Zhou et al. 2024, BMC Plant Biol 24: 588, PDF opened; Xu et al., Front Plant Sci 13, 10.3389/fpls.2022.1037784, opened) and sulphuric-acid scarification trials (Kheloufi et al., Die Bodenkultur 75(2): 105-113, 10.2478/boku-2024-0010; Diniz et al. 2018, 10.18378/rvads.v13i2.5286), which erode the seed coat and are no cue. |
| 35 | Oncosiphon eye_type | ok. Same pooled search as line 22. |
| 34 | Oncosiphon diel | ok. My pollination search returned Cape flower-visiting studies with no Oncosiphon opening hour. |
| 20 | Helleborus sense_light_nonvisual | **error**. Herranz Ferrer R, Copete Carreño MA, Copete Carreño E, Ferrandis Gotor P, Herranz Sanz JM 2023, "Influence of environmental conditions on embryo growth, dormancy breaking, and germination in seeds of Helleborus foetidus (Ranunculaceae)", Acta Physiologiae Plantarum 45: 137, 10.1007/s11738-023-03617-5 (Springer page opened): "The light–temperature requirements for embryo growth and radicle emergence were studied", with the best germination (75%) in darkness. Stinking hellebore is the record's own common name. The temperature-only study I also found (J Environ Hortic 28(3): 179-186, 10.24266/0738-2898-28.3.179) holds the photoperiod constant and does not count. |
| 1 | Armoracia sense_chemical | ok. Queries match (13 harvest, 3 web). My searches returned a flea-beetle paper that used Arabidopsis only (Sporer et al. 2021, Front Plant Sci 12: 645030, opened), a 1979 feeding-preference study of Phyllotreta armoraciae on glucosinolates (10.1111/j.1570-7458.1979.tb02875.x, AGRIS page), and an extract allelopathy paper (Simpson and Ku 2021, Plants 10(10): 1992), with no living horseradish response. An AGRIS record on NAA and BA in horseradish organ culture in vitro is excised tissue under the reading. |
| 11 | Desmanthus eye_type | ok. Same pooled search as line 22. |
| 10 | Desmanthus diel | ok. My searches returned a Mimosa floral study (Botanical Sciences 103(2), 10.17129/botsci.3633, opened) and flower-visitor pages; no Desmanthus opening hour. |
| 12 | Desmanthus sense_chemical | ok. My searches returned a mechanical-scarification paper (HortScience 45, rngr.net listing) and sulphuric-acid scarification work on D. illinoensis (Schnell 1990, Emporia State thesis; Call 1985, J Range Manage 38(6): 500-503, 10.2307/3899740), which is no cue. |
| 8 | Eriophorum sense_chemical | ok. My searches returned Molau and Shaver 1997 on seed production (LTER page, no chemical treatment shown) and hormone papers on other plants; no Eriophorum response. |
| 23 | Dermatophyllum sense_chemical | ok. My searches returned scarification trials on Sophora secundiflora with sulphuric acid, hot water and hydrogen peroxide (Kheloufi et al. 2024, 10.24193/subbbiol.2024.2.04; Ruter and Ingram 1991, HortScience 26(3): 256-257; Sayed 2019, Bull Fac Agric Cairo Univ 70: 247-255) and no hormone, elicitor or scent work. I read the peroxide soak as a scarification agent; if the desk reads hydrogen peroxide as a chemical cue, this verdict becomes an error. |
| 36 | Oncosiphon sense_chemical | **error**. Perez-Ochoa Z and de la Rosa CA, "Environmental factors and herbicide effect on germination rates of stinknet", Cal-IPC Symposium 2019 poster (cal-ipc.org PDF opened): smoke-treated O. piluliferum seeds germinated "significantly more than control seeds" (their Fig. 4). Main logs smoke-cued germination under sense_chemical. The source is a symposium poster; if the desk does not accept posters, this verdict becomes ok. The herbicide trials on the same page measure kill and are not counted. |
| 3 | Bellardia eye_type | ok. Same pooled search as line 22. |

First draw: 3 errors in 20, 15.0% (lines 5, 20, 36).

## Verdicts, extension (seed 8115)

| Line | Record | Verdict |
|---|---|---|
| 13 | Desmanthus sense_light_nonvisual | **error**. Rangel JH de A 2005, "Agroecological studies of Desmanthus: a tropical forage legume", PhD thesis, James Cook University (repository page opened): seedling emergence in soils from under and between canopies rose "by increasing shade levels and watering frequency", and seedlings under tree canopies had more leaves, greater height and better survival. The shade-level emergence trial is the kind of light response the reading counts; by point 3 the work keeps the trait out of the record. |
| 26 | Himantoglossum sense_light_nonvisual | **error**. Dulić J, Ljubojević M, Ognjanov V, Barać G, Dulic T 2019, "In vitro germination and seedling development of two European orchid species, Himantoglossum jankae ... and Spiranthes spiralis", In Vitro Cell Dev Biol Plant 55(4): 380-391, 10.1007/s11627-019-09997-z (Åbo Akademi page opened): H. jankae germinated better in continual darkness than under a 16-hour photoperiod, which the authors read as negative photoblasty. |
| 24 | Dermatophyllum sense_light_nonvisual | ok. My searches returned a fertilization study (Egypt J Agric Sci 71(4), 10.21608/ejarc.2020.210560) and a Kalmia light-germination paper; no Dermatophyllum light trial. |
| 21 | Dermatophyllum diel | ok. My search returned a Sophora davidii flowering-period study and other genera; no opening hour in Dermatophyllum. |
| 16 | Sapindus sense_light_nonvisual | ok, two leads. Yue et al. 2019 (J Beijing For Univ 41(6): 75-85, 10.13332/j.1000-1522.20180424, opened) compares seedlings at three field sites with no set light levels, and Gao et al. 2016 (Scientia Silvae Sinicae 52(11): 29-38, 10.11707/j.1001-7488.20161104, opened) relates canopy light to yield under pruning; neither is a set-light trial. The scarification trials on S. saponaria (Ciência Florestal 28(3): 987-996, 10.5902/1980509833376; Ciência Rural) test no light. |
| 4 | Bellardia sense_chemical | **error**. Tucci and Melchionna (Delpinoa n.s. 20, as under line 5) tested GA3 at 3.5, 35 and 350 mg/l: GA3 lowered the seeds' dependence on light, more so at higher doses, while kinetin had no effect. A living seed's response to an applied hormone counts under point 10(d). |
| 27 | Sesuvium eye_type | ok. My pooled focusing search found nothing on the genus. |
| 28 | Sesuvium sense_chemical | ok. My searches returned a salinity transcriptome of S. portulacastrum with no applied hormone (Chen et al. 2022, Front Plant Sci 13, 10.3389/fpls.2022.995855, DOAJ page opened), leaf-explant regeneration with zeatin and IAA (Jiang et al. 2024, Agriculture 14(8), excised tissue) and jasmonate work on rice. |
| 17 | Helleborus diel | ok. My search returned Helleborus plant patents and a Petunia scent-clock thesis; no Helleborus opening or scent hour. |
| 19 | Helleborus sense_chemical | **error**. Zhao X, Wang F, Wang L, Wang Q, Liu A, Li Y 2024, "Deep Simple Epicotyl Morphophysiological Dormancy in Seeds of Endemic Chinese Helleborus thibetanus", Agriculture 14(7): 1041 (RePEc page opened): 300 mg/L GA3 shortened warm stratification, raised radicle emergence and broke epicotyl dormancy. Moore 2008, "Enhancement of Seed Germination and Seedling Growth of Lenten rose", Auburn thesis (repository page opened), found GA3 before warm stratification raised germination by 42 to 58% in Helleborus × hybridus. Both are living hormone responses of the kind audit 79 counted. |
| 9 | Eriophorum sense_light_nonvisual | **error**. Bliss LC, "Seed Germination in Arctic and Alpine Species", Arctic, pp. 180-188 (University of Calgary journal PDF; year not printed, data from 1953 to 1955): E. vaginatum ssp. spissum seeds germinated in continuous light (about 22.6%) and not at all in darkness, and dark-held seeds germinated when moved to light. Holloway, Sparrow and Willison 2012 (HortScience 47(9): S376, UAF PDF) also compared light and dark for E. angustifolium (under 15% in all conditions). |
| 37 | Oncosiphon sense_light_nonvisual | **error**. Oliver RC and Laubscher CP 2023, "Abiotic influences on seed germination of three spring flowering Asteraceae annuals from the winter-rainfall region of South Africa", Acta Horticulturae 1365: 17-24 (CPUT repository page opened): O. suffruticosum germinated under continuous light, continuous darkness and 12-hour cycles at 7 to 27 °C. The abstract gives the temperature optimum and not the light result, so by point 3 the work belongs on the wanted list and the trait out of the record. |
| 7 | Eriophorum eye_type | ok. Same pooled search as line 27. |
| 14 | Sapindus eye_type | ok. Same pooled search as line 27. |
| 32 | Mentha diel | ok. Queries match (6, 2); the five screened works are correctly screened. My searches returned Osmanthus scent-rhythm work, a Mentha × gracilis origin paper (Econ Bot 44: 183-213, opened, no anthesis hour) and a Convolvulus reproductive-biology paper. |

Extension: 6 errors in 15 (lines 4, 9, 13, 19, 26, 37).

## Rate

Sample: 3 of 20, 15.0%. Sample and extension: 9 of 35, 25.7%. If the desk rejects the poster of line 36, 8 of 35, 22.9%. The unit is above 5% on any base and fails. Pooled with the desk's earlier audits of desk-screen units (audits 43 to 51, 55 to 73 and 75 to 78, 13 errors in 724; audit 79, 7 in 35; audit 80 at its desk ruling, 0 in 35): 29 in 829, 3.5%.

**Error records: lines 4, 5, 9, 13, 19, 20, 26, 36 and 37** of docs/views/searched/harvest-c23b.jsonl (Bellardia sense_chemical and sense_light_nonvisual, Eriophorum sense_light_nonvisual, Desmanthus sense_light_nonvisual, Helleborus sense_chemical and sense_light_nonvisual, Himantoglossum sense_light_nonvisual, Oncosiphon sense_chemical and sense_light_nonvisual). Lines 18 (Helleborus eye_type) and 29 (Sesuvium sense_light_nonvisual) were not drawn.

Pattern. Eight of the nine misses are seed-germination studies, under light against darkness or with GA3 or smoke, and each turned up within the first page of a search naming the genus with "germination". The record's point 10(e) phrases ("light intensity OR shade OR photoperiod growth", "jasmonate OR elicitor OR hormone response") returned growing guides and jasmonate reviews, and nothing was opened, so studies whose titles say "germination ecology" or "dormancy" were passed over. The unit's own Themeda follow-ups used germination words and found wanted lines; the other genera did not get that search.

## Wanted lines (listed, not counted)

All 9 lines leave `authors` empty, so none is counted.
- Line 3 (10.3390/compounds2010004): Romano VA, Rosati L, Fascetti S, Cittadini AMR, Racioppi R, Lorenz R, D'Auria M, Compounds 2(1): 37-53, 2022 (MDPI page opened). The plants were potted and whole inflorescences were enclosed in a glass bell, so they were living flowers and the sense_chemical reading holds. The paper compares early and late flowering phases and two years and gives no within-day timing, so the line's diel claim does not hold.
- Line 2 (Sapindus, ScienceDirect pii S0926669025012701): a title search did not return the article, so year, DOI and authors stay unconfirmed.
- Line 1 (10.5511/plantbiotechnology.20.13): its material is horseradish hairy roots, which the reading in force excludes, so the line cannot fill the Armoracia sense_light_nonvisual cell.
- The other lines were not checked against a page.

## Leads

- Themeda sense_light_nonvisual (wanted cell, no record): "Environmental control of reproduction in Themeda australis", Aust J Bot 17(3): 375-389, 1969, 10.1071/BT9690375, tests day length and vernalization on 30 races (short-day, long-day and day-neutral races); T. australis is now T. triandra. A stronger source than wanted line 7.
- Helleborus sense_light_nonvisual and sense_chemical: the three works under lines 19 and 20.
- Bellardia: the Tucci and Melchionna paper settles both lines 4 and 5 once logged.
- Sapindus sense_light_nonvisual: Gao et al. 2016 under line 16, if the desk reads canopy light set by pruning as a set light level.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC11191301 (reCAPTCHA); the BMC PDF served the paper.
- muse.jhu.edu article 680013 (verification page).
- reference-global.com boku-2024-0010 PDF (binary data); the article page served the abstract.
