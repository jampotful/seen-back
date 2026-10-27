# Audit 85: harvest-c11 and harvest-c12 (pull request 37, Codex round 2026-10-27; branch cx/round28, head 818d827b)

## Sample (seed 85), drawn before any record was read

Pairs (file, line), in draw order: (c11, 13), (c12, 15), (c11, 7), (c11, 21), (c12, 16), (c11, 15), (c12, 5), (c11, 23), (c12, 11), (c11, 25), (c11, 18), (c12, 3), (c12, 10), (c12, 6), (c11, 8), (c12, 7), (c11, 22), (c11, 19), (c11, 20), (c11, 24).

The draw was `random.seed(85)` and `random.sample(all, 20)` over the 41 search record lines taken as (file, 1-based line), harvest-c11 (25 lines) first and harvest-c12 (16 lines) after it. The sample holds 3 errors, so the unit fails without an extension. So that the desk can drop error records and merge the rest, as audit 83 did, I judged the 21 undrawn lines too, in the order `random.seed(8515)` gives them: (c11, 10), (c12, 8), (c11, 11), (c12, 2), (c11, 3), (c11, 4), (c12, 9), (c11, 14), (c11, 9), (c11, 2), (c11, 16), (c11, 5), (c11, 17), (c11, 1), (c12, 1), (c12, 4), (c11, 6), (c12, 12), (c12, 13), (c11, 12) and (c12, 14). The two draws cover the whole unit.

## Gate

`python3 -I tools/views/screen_candidates.py --check` prints "0 problems" for harvest-c11 (25 search records, 152 wanted lines) and for harvest-c12 (16 search records, 188 wanted lines), both saved to /tmp from `origin/cx/round28` (head 818d827b).

## Method

Judged against desk-audit.md and desk-screen.md, point 10 (a) to (e) included, with audit 83's strict reading. Of the 41 records, 34 are plant eye_type records, six are diel (Ulmus, Zizia, Chasmanthium, Lobelia, Equisetum, Castilleja) and one is sense_chemical (Zizia). Under point 10(b) plant eye_type is "none" for every plant, so a missed measurement for an eye_type record means a focusing work on a species of the genus that the record leaves out of `screened`.

Queries. A script compared each record's unprefixed `queries` with the `query` and `family review` lines `harvest_get.py` prints for the genus. Fifteen records belong to harvest genera; all 15 match word for word and in order, with their "web: " lines after them, and no harvest shows a failed step. Of the 26 records for genera in no harvest run, 18 list "web: " lines only. Eight do not:
- Ulmus diel and eye_type (c11 lines 1 and 2) list nine unlabelled queries ("Ulmus flower opening time anthesis", "elm epidermal lens cells eye", "Ulmaceae photoreceptor review" and six more). Their `where` says these went to the OpenAlex works API directly. This is the fault audit 83 counted on lines 1 to 5 of harvest-c7.
- Centaurea, Ratibida, Parthenium, Senecio (c12 lines 3, 4, 7 and 11; "Asteraceae photoreceptor review"), Andropogon (c12 line 8; "Poaceae photoreceptor review") and Datura (c12 line 13; "Solanaceae photoreceptor review") each open with one unlabelled family-review line. `harvest_get.py <Genus>` prints nothing for these genera ("in no harvest run yet"). Their `where` says the line is the cached family review of harvest run 17, and that review does exist in the harvest: `harvest_get.py Helianthus` prints `family review "Asteraceae photoreceptor review": 581 hits`. The line is therefore checkable, though only through a sibling genus. Step 3(a) asks that `queries` repeat `harvest_get.py <Genus>` word for word, and the launch prompt counts any unprefixed line that the genus's output does not print, so I count these six. The fork is set out under Counts.

Chased. Every DOI named in `chased` by the 15 harvest-genus records was looked for in the genus's output. Each record names every citation-step DOI the output prints, except Fraxinus (c12 line 5), which names the step that returned 22 works and leaves out two zero-hit steps; audit 83 noted that omission without counting it, and so do I. Ten records add the general reviews 10.1146/annurev-arplant-042809-112259 and 10.1002/wmts.36 (and Conopholis two Orobanchaceae works) from the web family search, which the output does not print. Since these records also name every citation step that ran, I treat the extra DOIs as a fair report of the web family step and count none of them; audit 83 counted Rhus and Salvia only because they named a web DOI in place of the citation steps. Records for no-run genera name a web family review or give a none-reason, which audit 83 accepted.

Screened. I read three entries per record (all where fewer) against the record's description, the harvest's titles and abstract starts, or pages my own searches returned. The focusing works screened are the general ones audit 83 met (10.3390/plants12010061, 10.1111/j.1399-3054.1996.tb00674.x, PMC9824129) or genus anatomy with no optics, each with the owner's wording where focusing is at issue. Senecio (c12 line 11) names the one focusing work on a former Senecio species: Egbert, Martin and Vogelmann 2008, J Exp Bot 59(7): 1863, six succulents with epidermal windows including Senecio rowleyanus (KU ScholarWorks page opened). It gives the owner's wording and notes the species now sits in Curio.

Searches. I ran 40 WebSearches: three each for Zizia sense_chemical, Lobelia diel and Castilleja diel; one focusing search per sampled eye_type genus (scientific and common name in one query); one search per extension diel record; ten combined focusing searches for the extension genera; and two for wanted lines. As audit 83 found, focusing searches return the same general set for nearly every genus (the FIU lens-cell paper cas_bio/44, PMC8309337, AskNature, the Yale bibliography entry, Nature 075535b0, the Brodersen Vermont dissertation), so a missed genus-level focusing work would have had to surface by name. None did.

## Verdicts (sample of 20, seed 85)

| File, line | Record | Verdict |
|---|---|---|
| c11, 13 | Tropaeolum eye_type | ok. Queries match (13 harvest, 12 web); both zero-hit citation steps named. The petal-optics review, the collected-flower reflectance study and the general focusing works hold no Tropaeolum eye; my search returned the general set. |
| c12, 15 | Castilleja eye_type | ok. Queries match (13, 35); three citation steps named. The C. tenuiflora haustorium study is a chemical response with no optics; the other two hold "eye" or "lens" as words only. |
| c11, 7 | Zizia eye_type | ok. Web-only. The Apiaceae review and the two general focusing works name no Zizia; nothing on Zizia focusing came back. |
| c11, 21 | Sorghum eye_type | ok. Queries match (11, 12); citation step and its two works named. Blade-joint epidermis, microCT airspace and silica bodies are anatomy only. Main already holds a Sorghum eye_type record (harvest-29), so the harvest lists eye_type as closed and this record duplicates it; noted, not counted. |
| c12, 16 | Castilleja diel | ok. Queries match (13, 35). The C. sessiliflora day and night exclusion (10.1002/ece3.11443) measures pollinator contribution; the other screened works are other genera or seasonal. My three searches found Olsen 1965 (UNM thesis, page opened), which gives flowering months only. |
| c11, 15 | Chasmanthium eye_type | ok. Queries match (11, 10); citation step named. "Human eyes" in the panicoid paper is a phrase; my grass search returned Dunn, Le and Strömberg 2015 (IJPS 176(9), page opened), a growth trial under four irradiances that names no Chasmanthium on the page and holds no optics. |
| c12, 5 | Fraxinus eye_type | ok. Queries match (13, 12). `chased` omits two zero-hit citation steps (noted). Halopteris, the ash SEM study and the Korean ash microscopy hold no plant eye. |
| c11, 23 | Vinca eye_type | ok. Web-only. Vinca epidermal anatomy and the Boquila essay are rightly screened; nothing on Vinca focusing came back. |
| c12, 11 | Senecio eye_type | **error (queries).** One unlabelled cached family-review line for a genus in no harvest run. Content holds: the S. rowleyanus window paper carries the owner's wording. |
| c11, 25 | Lobelia diel | ok. Web-only. Ten screened works give seasons, protandry stages or fixed photoperiods. My searches found Ren 2009 on L. chinensis (Chinese Journal of Plant Ecology page opened), which stages flowers by days after opening and gives no hour, and Eisen et al. 2017 on L. siphilitica pollen dispensing (LMU page, no abstract), left as a lead. |
| c11, 18 | Aquilegia eye_type | ok. Web-only. Staminode and B-gene works describe epidermal cells with no optics; my petal search returned conical-cell work on other genera. |
| c12, 3 | Centaurea eye_type | **error (queries).** As c12 line 11. Content holds: the C. cyanus histochemistry paper my search returned is screened. |
| c12, 10 | Glechoma eye_type | ok. Queries match (5, 25); both zero-hit citation steps exist and `chased` names one (noted, as Fraxinus). Leaf microstructure and an eyepiece are rightly screened. |
| c12, 6 | Adiantum eye_type | ok. Queries match (13, 12). No citation step ran; `chased` names a DOI the output prints. My search returned "Development of the epidermal cells of the pinnules of Adiantum" (Am Fern J 101(3), page blocked), which by its title is anatomy; left as a lead. |
| c11, 8 | Zizia sense_chemical | ok. Web-only. Screened works are other genera (Ziziphus, Vetiveria) or general. My three searches returned only a Ziziphus GA3 trial (Casini and Salvadori 1980, AGRIS page opened) and goldenrod volatile work, so no Zizia chemical measurement was missed. |
| c12, 7 | Parthenium eye_type | **error (queries).** As c12 line 11. Content holds. |
| c11, 22 | Dioscorea eye_type | ok. Web-only. Rhizome and microtuber anatomy are rightly screened; nothing on Dioscorea focusing came back. |
| c11, 19 | Helianthus eye_type | ok. Queries match (9, 11); citation step named. The filament-expansion study, the petal-cell review and a lentil (Lens) paper are rightly screened. |
| c11, 20 | Arundo eye_type | ok. Queries match (13, 12); citation step named. Six lignocellulose works matched "ocell" inside a word and are rightly screened. |
| c11, 24 | Lobelia eye_type | ok. Web-only. The 22-species epidermis SEM study is anatomy; nothing on Lobelia focusing came back. |

Errors in the sample: 3 of 20 (c12 lines 3, 7 and 11).

## Verdicts (extension of 21)

| File, line | Record | Verdict |
|---|---|---|
| c11, 10 | Iris eye_type | ok. Web-only. Human-iris and bee-ocellus pages are rightly screened. |
| c12, 8 | Andropogon eye_type | **error (queries).** One unlabelled "Poaceae photoreceptor review" line for a genus in no harvest run. Content holds. |
| c11, 11 | Ricinus eye_type | ok. Web-only. The leaf structural study (10.1071/BT16184) holds no optics; my search returned it too. |
| c12, 2 | Equisetum diel | ok. Web-only. My search returned Zajączkowska et al. 2017 (Planta 245(4): 835, page opened) on stem vibration and spore release, which gives no time of day. |
| c11, 3 | Malvaviscus eye_type | ok. Web-only. |
| c11, 4 | Carya eye_type | ok. Web-only. |
| c12, 9 | Cynodon eye_type | ok. Queries match (11, 18); citation step named. Epidermal taxonomy works are rightly screened. |
| c11, 14 | Chasmanthium diel | ok. Queries match (11, 10). The Uniola and Avena morning-opening works are other genera; my search returned flora pages only. |
| c11, 9 | Ptelea eye_type | ok. Queries match (13, 12); citation step named. |
| c11, 2 | Ulmus eye_type | **error (queries).** Nine unlabelled direct-OpenAlex queries, as audit 83's line 3. |
| c11, 16 | Paulownia eye_type | ok. Queries match (11, 10); both citation steps named. |
| c11, 5 | Pyrus eye_type | ok. Web-only. Pear lens-shaped stomata are anatomy; the scale-insect eyes belong to the insect. |
| c11, 17 | Chenopodium eye_type | ok. Web-only. |
| c11, 1 | Ulmus diel | **error (queries).** As c11 line 2. Content holds: my search returned Ślusarczyk et al. 2022 (Alergoprofil 18(3), page opened), daily pollen totals and season dates with no hour. |
| c12, 1 | Equisetum eye_type | ok. Web-only. Its `screened` reasons are shared with the diel record, which is untidy and does not misstate either work. |
| c12, 4 | Ratibida eye_type | **error (queries).** As c12 line 11. |
| c11, 6 | Zizia diel | ok. Web-only. The Ziziphus diel work is rightly screened as another genus; my search returned seasonal pages only. |
| c12, 12 | Ranunculus eye_type | ok. Queries match (6, 23); citation step named. The buttercup petal-reflection works are rightly screened; my search returned the same set. |
| c12, 13 | Datura eye_type | **error (queries).** One unlabelled "Solanaceae photoreceptor review" line. Content holds. |
| c11, 12 | Conopholis eye_type | ok. Queries match (11, 12); three citation steps named. The holoparasite petal-microsculpture study carries the owner's wording. |
| c12, 14 | Juglans eye_type | ok. Web-only. |

Errors in the extension: 5 of 21 (c11 lines 1 and 2; c12 lines 4, 8 and 13).

## Counts

Sample: 3 of 20, 15.0%. Whole unit: 8 of 41, 19.5%. The unit is above 5% and fails. Pooled with the desk's earlier audits of desk-screen units as audit 83 gives them (30 in 860), and adding this unit whole: 38 in 901, 4.2%. I have not seen audit 84, so it is not in that figure.

Fork. Every error is a form fault in `queries`, and none hides a measurement. Six of the eight are a single cached family-review line that the genus's own `harvest_get.py` output does not print but a sibling genus's output does. If the desk accepts such a line for a genus in no harvest run, the sample holds 0 errors in 20 and the whole unit 2 in 41 (Ulmus only), 4.9%, which passes; pooled 25 in 901, 2.8% on audit 83's lenient figure (23 in 860). I hold to the strict reading the launch prompt names, since step 3(a) asks for the genus's own output and a reader cannot check the line from it.

**Error records:** harvest-c11.jsonl lines 1 and 2 (Ulmus diel and eye_type); harvest-c12.jsonl lines 3, 4, 7, 8, 11 and 13 (Centaurea, Ratibida, Parthenium, Andropogon, Senecio and Datura, all eye_type). The other 33 records stand. All eight can be repaired by moving the unlabelled lines into `note` (or `where`, which already describes them).

## Wanted lines (listed, not counted)

- harvest-c12.jsonl line 97 (Pandey and Palni 2005, Seed Science and Technology 33(2): 485-491): its `get` field reads "journal via library", which points a reader at a library route, and its `url` is a 2026 Frontiers article citing the paper, not the paper. My search did not return a page for the paper itself, so the authors and year stay unchecked.
- harvest-c11.jsonl line 1 (Ling and Sauvé 1997, 10.21273/hortsci.32.3.461e): my title search did not return the HortScience page, so it stays unchecked.
- No other wanted line was checked against a page.

## Leads

- Lobelia diel: Eisen, Case, Caruso and Dudash 2017, "Variation in pollen-dispensing schedules of Lobelia siphilitica", IJPS 178(1): 79-84, 10.1086/688961 (LMU page). Whether the schedules are hourly is not stated on the page.
- Adiantum: the Am Fern J 101(3) paper on pinnule epidermal cell development (10.1640/0002-8444-101.3.172 as the BioOne link shows it) was blocked; by its title it is anatomy.
- Grasses: Dunn, Le and Strömberg 2015 grew five grass species under four irradiances; if one belongs to a desk genus, it is a sense_light_nonvisual lead under point 10(d).

## Blocked pages

- pmc.ncbi.nlm.nih.gov/articles/PMC11112297 (Castilleja sessiliflora pollination): the permission request was not answered; not retried.
- bioone.org (Adiantum pinnule epidermis): bot protection.

No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a beds.ac.uk proxy mirror of MDPI appeared in one result list and was left alone), and no paper text was committed.
