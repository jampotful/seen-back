# Audit 83: harvest-c7 (pull request 37, Codex round 2026-10-27; branch cx/round28, head 818d827b)

Gate: `python3 -I tools/views/screen_candidates.py --check` on the 31 search records and 327 wanted lines, saved to /tmp from `origin/cx/round28`, prints "0 problems".

## Sample (seed 83)

`random.seed(83)` and `random.sample(lines, 20)` over the 31 search record lines (1-based) give, in draw order, 16, 28, 30, 15, 3, 5, 13, 2, 24, 21, 7, 22, 6, 10, 27, 23, 20, 17, 19 and 26. The draw was made before any record was read.

The sample holds 4 errors, so the unit fails without an extension. To let the desk drop error records and merge the rest, I also judged the 11 undrawn lines, ordered by `random.seed(8315)` and `random.sample(<undrawn lines ascending>, 11)`: 4, 12, 18, 31, 1, 29, 25, 11, 8, 9 and 14. The two draws cover the whole unit.

## Method

Judged against desk-audit.md and desk-screen.md, point 10 (a) to (e) included. Thirty of the 31 records are plant eye_type records and line 3 is Callicarpa diel. Under point 10(b) plant eye_type is "none" for every plant, and a work on epidermal focusing in the genus belongs under sense_light_nonvisual and must be named in the eye_type record's `screened` with the owner's wording; so a missed measurement for these records means a focusing work on a species of the genus that the record does not name. For the diel record the trait words are "flower opening time anthesis".

Queries. A script compared each record's non-web `queries` with the `query` and `family review` lines `harvest_get.py` prints for the genus. Sixteen of the 20 drawn records match word for word and in order, with their labelled web searches after them; seven of these are genera in no harvest run whose records hold web searches only, as their notes say. No harvest shows a failed ("gave up") step. Lines 2, 3 and 5 (Callicarpa twice, Cnidoscolus) are genera in no harvest run, yet each lists nine unlabelled queries ("Callicarpa flower opening time anthesis", "beautyberry plant ocelli lens-like epidermal cells focusing light", "Lamiaceae photoreceptor review" and six more) that `harvest_get.py` does not print. Their `where` and `note` say these were sent directly to the OpenAlex works API during the round. That disclosure is honest, but point 7 lets `queries` hold the harvest's lines and the "web: " searches only, and nobody can check the nine lines against a harvest, so I count each as an error under step 4 ("queries that differ").

Chased. Every DOI that the harvest genera name in `chased` was looked for in the output. Quercus, Cirsium, Trifolium, Triadica, Youngia, Oxalis, Toxicodendron and Verbesina name each citation-step DOI the output prints; their other DOIs are printed in the output (family reviews and supplement runs). Line 13 (Rhus) names 10.21577/0100-4042.20230101, an Anacardiaceae review found by its web family search, which the Rhus output does not print, and it leaves out the citation step that did run (works citing 10.1016/j.tree.2009.09.010 that name Rhus: 0). Its `chased` is neither a DOI printed in the citation step nor a reason the output supports, so I count it. The no-run genera name a web family review or give a none-reason; with no harvest output there is no citation step to name, so I accept those as audit 82 did.

Screened. I read three screened entries per record (all where fewer) against the harvest's titles and abstract starts or the record's own snippet description. Every focusing work in the drawn records is a general leaf-optics work on other genera (the Medicago, Zea and Impatiens paper 10.1111/j.1399-3054.1996.tb00674.x; the Begonia, Citrus, Ficus, Colocasia and Impatiens paper 10.3732/ajb.94.7.1061, whose species list I confirmed on the Yale bibliography page; the plant-ocelli review PMC9824129) or a genus work screened with the owner's wording (Quercus robur epidermal cell shapes; the Trifolium repens lens-like epidermis; Myers, Vogelmann and Bornman 1994 on Oxalis acetosella, whose AGRIS record I opened). None reports an eye, and none is a focusing work on the genus left out of `screened`.

Searches. I ran 50 WebSearches: three for Callicarpa diel, two focusing searches per drawn genus (scientific name and common name; Triadica, Toxicodendron, Urena and Verbesina took one combined search), one per extension genus, and two for wanted lines. Only pages my own searches returned were opened. The focusing searches return the same general set for nearly every genus (the FIU rain-forest lens-cell paper cas_bio/44, PMC8309337, "Algal Optics" arXiv 2506.15214, the Brodersen 2008 Vermont dissertation, AskNature, Graham 1907 in Nature on Ephedreae stems, and the 1904 Nature review of Haberlandt), so a missed genus-level focusing work would have had to surface by name; none did.

## Verdicts (sample of 20, seed 83)

| Line | Record | Verdict |
|---|---|---|
| 16 | Sambucus eye_type | ok. Web-only (no harvest run). Screened: the Medicago and Impatiens focusing paper, the AJB leaf-optics paper and PMC9824129 hold no Sambucus eye; my two searches found no Sambucus focusing work. |
| 28 | Quercus eye_type | ok. Queries match (4 harvest, 18 web); both citation-step DOIs named. The Q. robur epidermal-shape study and the PMC8309337 review are screened with the owner's wording; my searches returned only the general set. |
| 30 | Cirsium eye_type | ok. Queries match (4, 19); both citation-step DOIs named. The lutein-retina and Tagetes macular works and 10.3390/plants10071455 hold no plant eye; nothing on Cirsium focusing came back. |
| 15 | Phytolacca eye_type | ok. Web-only. The NEON page's "lens-shaped" describes the seed; nothing on Phytolacca focusing came back. |
| 3 | Callicarpa diel | **error (queries).** Nine unlabelled direct-OpenAlex queries for a genus in no harvest run. Content holds: my searches found Xu Lin et al. 2012, "Pollen vitality and stigma receptivity in two species of Callicarpa" (J Beijing Forestry Univ 34(4): 26-30, page opened), which gives a 24-hour blossom period and stigma receptivity in hours from blossoming and no clock time of opening, so it measures no diel timing. |
| 5 | Cnidoscolus eye_type | **error (queries).** As line 3. The two screened focusing works name other genera; nothing on Cnidoscolus focusing came back. |
| 13 | Rhus eye_type | **error (chased).** Queries match (5, 12). `chased` names a web-found Anacardiaceae review that the output does not print and omits the citation step that ran. The screened driving-software, primate-cone and Rhus-extract works hold no plant eye; content holds. |
| 2 | Callicarpa eye_type | **error (queries).** As line 3. The two screened focusing works name other genera; nothing on Callicarpa focusing came back (an AGRIS hit was Martin et al. 1989 on Medicago sativa). |
| 24 | Urena eye_type | ok. Web-only. The three screened focusing works name other genera; nothing on Urena came back. |
| 21 | Trifolium eye_type | ok. Queries match (4, 10); citation-step DOI named. The T. repens lens-like epidermis work is screened with the owner's wording, as point 10(b) asks. |
| 7 | Sabal eye_type | ok. Web-only. Four general optics works screened correctly; nothing on Sabal focusing came back. |
| 22 | Broussonetia eye_type | ok. Web-only. Screened focusing works name other genera; nothing on Broussonetia came back. |
| 6 | Magnolia eye_type | ok. Web-only. Nothing on Magnolia focusing came back. |
| 10 | Ruellia eye_type | ok. Web-only. The JSTOR and Gutenberg Ruellia anatomy items describe structure with no optics; my common-name search added a Ruellieae leaf-epidermis anatomy paper (SWU journal), which is anatomy only. |
| 27 | Triadica eye_type | ok. Queries match (13, 18); both citation-step DOIs named. The green-flower "eye" paper (10.1093/aob/mcae213) and the two optics works hold no Triadica eye. |
| 23 | Passiflora eye_type | ok. Web-only. The "ocellus" of 10.1371/journal.pone.0187905 is an extrafloral nectary, rightly screened; my petal-cell search returned conical-cell and structural-colour work on other genera. |
| 20 | Youngia eye_type | ok. Queries match (13, 15); both citation-step DOIs named. My search returned Fan et al. 2002 on Euonymus japonicus and a Chaenomeles petal study (pages opened); neither names Youngia. |
| 17 | Oxalis eye_type | ok. Queries match (10, 8); citation-step DOI named. Myers et al. 1994 and four other optics works are screened with the owner's wording, as point 10(b) asks. |
| 19 | Toxicodendron eye_type | ok. Queries match (5, 12); citation-step DOI named. Lacquer and extract works hold no plant eye. |
| 26 | Verbesina eye_type | ok. Queries match (13, 21); both citation-step DOIs named. "Ox-eye", the legume genus Lens and the anther-collar anatomy are rightly screened. |

Errors in the sample: 4 of 20 (lines 2, 3, 5 and 13).

## Verdicts (extension of 11)

| Line | Record | Verdict |
|---|---|---|
| 4 | Parthenocissus eye_type | **error (queries).** No harvest run; nine unlabelled direct-OpenAlex queries, as line 3. Nothing on Parthenocissus focusing came back. |
| 12 | Stachys eye_type | ok. Queries match (13, 12). `chased` names a family-review DOI the output prints and leaves out three zero-hit citation steps; the reason it gives is what the output shows, so I note the omission without counting it. |
| 18 | Phyla eye_type | ok. Queries match (5, 16); citation-step DOI named. The Kew "strong lens" is a hand lens. |
| 31 | Ilex eye_type | ok. Queries match (5, 33). No citation step ran; the harvest's Aquifoliaceae review printed 11 hits, and the record's "no family photoreceptor review found" is a fair reading of them. |
| 1 | Bidens eye_type | **error (queries).** No harvest run; nine unlabelled direct-OpenAlex queries. Nothing on Bidens focusing came back. |
| 29 | Saururus eye_type | ok. Web-only. Nothing on Saururus focusing came back. |
| 25 | Campsis eye_type | ok. Web-only. Nothing on Campsis focusing came back. |
| 11 | Salvia eye_type | **error (chased).** Queries match (5, 10). `chased` names only a web-found Lamiaceae aerobiology review (PMC11207455), which the output does not print, and omits the two citation steps that ran (10.1111/een.12947 and 10.1016/j.isci.2022.104455, 0 works each). |
| 8 | Smilax eye_type | ok. Web-only. The screened Smilax syphilitica aerial-organ anatomy (my search returned it too) describes structure with no optics. |
| 9 | Erythrina eye_type | ok. Web-only. My search returned a flower-epidermis morphology paper on E. corallodendron, which is anatomy only. |
| 14 | Pontederia eye_type | ok. Queries match (13, 12). `chased` names a DOI the output prints and omits one zero-hit citation step, as line 12. |

Errors in the extension: 3 of 11 (lines 1, 4 and 11).

## Counts

Sample: 4 of 20, 20.0%. Whole unit: 7 of 31, 22.6%. The unit is above 5% and fails. Pooled with the desk's earlier audits of desk-screen units as audit 82 gives them (23 errors in 829 records, audit 80's two withdrawn by the desk ruling of 27 October): 30 in 860, 3.5%. Counting audit 80's two as written: 32 in 860, 3.7%.

Fork. All seven errors are form faults, and none hides a measurement. If the desk accepts direct OpenAlex queries listed without the "web: " prefix for genera in no harvest run, lines 1, 2, 3, 4 and 5 leave the count; if it also accepts a web-found family review in `chased` that leaves out zero-hit citation steps, lines 11 and 13 leave it. On that lenient reading the unit holds 0 errors in 31 and passes, pooled 23 in 860, 2.7%. I hold to the strict reading, since step 4 names both faults and the unlabelled queries cannot be checked by anyone.

**Error records: lines 1, 2, 3, 4, 5, 11 and 13** of docs/views/searched/harvest-c7.jsonl (Bidens, Callicarpa, Callicarpa diel, Parthenocissus, Cnidoscolus, Salvia and Rhus). The other 24 records stand. The five query errors can be repaired by moving the nine OpenAlex lines out of `queries` into `note`, or by prefixing them; the two `chased` errors by naming the citation steps that ran.

Pattern. The Codex screener ran OpenAlex itself for the first genera of the batch with no harvest run (Bidens, Callicarpa, Parthenocissus, Cnidoscolus) and switched to web-only records once the round's 429 notice reached it (Magnolia's note says so). The eye_type records themselves are sound: every focusing candidate carries the owner's wording, and the germination-first searches of point 10(e) appear in every record.

## Wanted lines (listed, not counted)

All lines I read leave `authors` empty, so none is counted. Checked against pages my searches returned:
- Line 1 (10.1371/journal.pone.0233228): "Seed germination of Bidens subalternans DC. exposed to different environmental factors", PLoS ONE 15(5): e0233228, 2020, by de Paiva Pamplona J, de Freitas Souza M, Sousa DMM and five others (DOAJ page). DOI and year match; the authors can be filled.
- Line 18 (10.11924/j.issn.1000-6850.2013-1772): Chinese Agricultural Science Bulletin 30(7): 238-241, published 5 March 2014 (journal page). The DOI matches; the line has year null, which can be filled with 2014; the page names no authors, so the empty field is right.
- The other lines were not checked against a page.

## Leads

- Callicarpa diel: Xu Lin et al. 2012 (J Beijing Forestry Univ 34(4): 26-30) on C. dichotoma and C. giraldii gives flower lifespan and receptivity windows in hours; the full text might give an opening hour, which would make it a diel candidate.

## Blocked pages

- revistas.ucr.ac.cr rbt article 19718 redirected to archivo.revistas.ucr.ac.cr; I did not follow it.

No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
