# audit-385: desk-d294, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d294 files present untracked in the worktree (docs/tracks/progress/desk-d294.md and docs/views/evidence/desk-d294.jsonl, 7 lines; neither committed here, neither edited). Line numbers are the file's (1-based). `python3 -I tools/senses/check.py | grep 'd294\.'`: "docs/views/evidence/desk-d294.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 19, 9, 13, 14, 10, 13, 6, all within 40; the only non-ASCII characters in any quote are the two en dashes of line 1 ("10–20", "4E–G"), matching the page.

Sources opened (WebFetch): api.crossref.org/v1/works/ for the six DOIs; zookeys.pensoft.net/article_preview.php?id=109521 and zookeys.pensoft.net/article/109521/download/xml/ (the XML stopped in Table 1); zookeys.pensoft.net/article_preview.php?id=95004; zookeys.pensoft.net/article/35229/download/xml/ (twice); www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2024.1356316/pdf; zookeys.pensoft.net/article_preview.php?id=49349; subtbiol.pensoft.net/article_preview.php?id=192708. All URLs were returned by a WebSearch first. Plazi, Zenodo, GBIF, PMC, PubMed, optimap, bionames, BHL, DOAJ, CONICET and catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Cherneva et al. 2023). Crossref: Irina Cherneva, Christina I. Ellison, Eduardo E. Zattara, Jon L. Norenburg, Megan L. Schwartz, Juan Junoy, Svetlana A. Maslakova; title identical; ZooKeys 1181, 167-200, no issue; issued 2023-10-05; CC BY 4.0 vor. Page licence "...Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Lines 2-3 (Hookabe, Kohtsuka, Fujiwara, Tsuchida, Ueshima 2023). Crossref same order; title identical (two pieces); ZooKeys 1146, 135-146, no issue; issued 2023-02-07; CC BY 4.0 vor. Page licence CC BY 4.0 sentence verbatim. Accepted.
- Line 4 (Trivalairat, Chiangkul, Purivirojkul 2019). Crossref same order; title identical; ZooKeys 882, 1-24, no issue; issued 2019-10-23; CC BY 4.0 vor. Page licence CC BY 4.0 sentence verbatim. Accepted.
- Line 5 (Abato, Chernyshev, Hookabe, Tsuyuki, Kaushik, Kajihara 2024). Crossref same order; title identical; Frontiers in Ecology and Evolution 12, article 1356316, no issue; issued 2024-02-16; CC BY 4.0 vor. Page "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." No conflicting tag. Accepted.
- Line 6 (Neal, Paterson, Blockley, Scott, Sherlock, Huque, Glover 2020). Crossref same order; title identical; ZooKeys 938, 1-86, no issue; issued 2020-06-03; CC BY 4.0 vor. Page licence CC BY 4.0 (tool summary) plus Crossref vor. Accepted.
- Line 7 (Grego, Falniowski, Hofman, Lecoquierre, Fatemi, Flot, Malek-Hosseini, Jaszczyńska 2026). Crossref same order; title identical; Subterranean Biology 58, 1-25, no issue; issued 2026-08-24; CC BY 4.0 vor. Page licence CC BY 4.0 sentence verbatim. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All seven species are described as new in the cited papers; names rest on the original descriptions (no checklist opened). Higher taxa: Tetranemertes in Oerstediidae, Monostilifera (title "(Monostilifera, Hoplonemertea, Nemertea)"); Tetrastemma, Monostilifera, no family heading printed ("Genus Tetrastemma Ehrenberg, 1828" only; "Tetrastemmatidae" in keywords), so the empty family is defensible; Placobdelloides in Glossiphoniidae, Rhynchobdellida (title); Leitoscoloplos under the printed heading "Orbiniidae Hartman, 1942", no order heading, empty order defensible; Iranobelgrandia printed under Truncatelloidea, Hydrobiidae, Belgrandiinae (a gastropod; no crustacean order applies), no order printed, empty order defensible (main has 480 records with empty order). No class is filed as an order. Line 5 fault: the Frontiers page prints "Family Oerstediidae Chernyshev, 1993" (and "Class Hoplonemertea Coe, 1905") in the systematics, but the record leaves family empty and its note says the family was not printed. Fixable.

## Trait key

eyes_count and eye_type are on main. No new key.

## Duplicates

`git grep -i` on origin/main (b5aeb180) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for the six genera and the six DOI suffixes: one hit only, docs/tracks/progress/desk-d284.md, a "Not filed" mention of Tetranemertes ocelata (a different species, not on main as a record). Remote desk-* and audit-* branches (1465 remote branches listed, d294 excluded), docs/views/evidence and docs/tracks, for the seven binomials and DOI suffixes: no hit. Duplicate faults 0.

## Per line

### Line 1, Tetranemertes bifrost, eyes_count 10-20 per side

Under "External appearance of live specimens": "Numerous small reddish brown ocelli (10–20 on each side of head) are arranged in four longitudinal rows (Fig. 4E–G)." **Quote MATCH.** Range and per-side kept in value and units. Next sentences: the lateral rows "have fewer eyes"; "Ocelli are somewhat obscured by the dark pigment of the head, and best seen in worms compressed between a slide and a" / "cover-glass (Fig. 4G)." The paper states no n for the specimens behind the range (only "n = 4" for stylets), as the conditions say. Type material verbatim: "Type material in the form of histological sections, anterior end preserved for histology, and tissue in 95% ethanol" ... "holotype CB057_18_07 (USNM 1618678)," "paratype 852_080203_8 (USNM 1156475), paratype CB057_18_01 (USNM 1618745)." No locality in that block; Table 2 places CB057_18 at Mangrove Point, Isla Colón, Panamá (tool summary); the locality of paratype 852_080203_8 was not seen.

Error (method/sample composition): `method` "taxonomic description of live and compressed type specimens" claims the count was made on the type specimens. The page does not say so; the counted heading is "live specimens", and the type material is held as histological sections, an anterior end and ethanol tissue. The conditions' "type series ... from Bocas del Toro, Panama" extends a locality the page gives only for the CB057_18 specimens. Fixable.

**Line 1 FIXABLE.**

### Line 2, Tetrastemma album, eyes_count 4

Description: "Four reddish brown eyes regular in size (Fig. 2B)." **Quote MATCH.** Holotype NMST-NE-H-06, fixed in Bouin's fluid, "collected on March 12, 2021 ... at depths of 144–200 m" off Miura, Kanagawa; "Before anesthetization, body of a live specimen 17 mm long and 1.0–1.2 mm wide."; no paratypes; sex not stated; Fig. 2 "photographs were taken in life by NH". Conditions match (holotype only, live, 17 mm). Uncounted: "deep-sea" overstates a 144-200 m dredge; optional replacement below.

**Line 2 MATCH.**

### Line 3, Tetrastemma shohoense, eyes_count 4

Description: "Four brown eyes present; anterior pair slightly larger than posterior ones (Fig. 2H)." **Quote MATCH.** Holotype NMST-Nem-H-05, Bouin's-fixed, ROV at 455 m, Shoho Seamount; "Before anesthetization, body of a live specimen 5.5 mm long and 0.3 mm wide."; no paratypes; sex not stated. Conditions match.

**Line 3 MATCH.**

### Line 4, Placobdelloides sirikanchanae, eyes_count 1 pair

Description of holotype, External morphology: "One pair of dark spherical eyes touch each other on somite III (Figure 4)." **Quote MATCH.** Figure 4 caption: "Anterior part of the live holotype of Placobdelloides sirikanchanae sp. nov." Variation (N = 20) and Diagnosis carry no eye sentence (tool summary). Material: "Holotype (ZMKU-ANN-0006), puddle on rubber plantation, Sadao District, Songkhla Province, Thailand"; "Paratypes (nine individuals, ZMKU-ANN-0007 to 0015), same locality data as the holotype." The holotype description cites paratype ZMKU-ANN-0009 (Figs 3, 6, 7) and ZMKU-ANN-0010 (Fig. 5) (tool summary), so "also cites paratype figures" is right.

Errors (sample composition, one record): the description opens "A mature Placobdelloides sirikanchanae sp. nov. (ZMKU-ANN-0006) has an elongated, dorso-ventrally flattened," so the stage is given, against the conditions' "(sex and stage not given)". `method` "preserved type specimens" is not on the page: the eye sentence cites Figure 4, a photograph of the live holotype, and the text does not say whether the description was made live or preserved (specimens were later "kept in 70% alcohol"). Fixable.

**Line 4 FIXABLE.**

### Line 5, Oerstedia pseudoculata, eyes_count 4

Section 3.1.1, External morphology: "Ocelli four in number, bright-orange in color, arranged in square." **Quote MATCH.** The false-eye clause ("white spots at anterolateral sides, showing an impression of big, whitish, false eyes", non-banded form) is in conditions. Holotype "ICHUM 8587, non-banded form"; eight paratypes (8586, 8582, 8583, 8584, 8585, 3287, 3288, Kr-Ann077; tool summary), matching "eight paratypes"; n = 5 statement prints "ICHUM 8282, 8283, 8584–8586", which does not match the list, as the conditions say. External description from living and anaesthetized specimens (tool summary).

Errors: (a) sample composition: the page sexes one specimen, "One paratype female specimen (ICHUM 8584)", and the conditions give no sex at all; (b) filing: family Oerstediidae is printed (see Names) but left empty, and the note says it was not printed. Fixable.

**Line 5 FIXABLE.**

### Line 6, Leitoscoloplos olei, eye_type none

Description: "Prostomium short, conical, anteriorly pointed (Fig. 16b)." then "Peristomium broad, achaetous, anteriorly bearing a pair of small nuchal organs; eyes absent." **Quote MATCH**; the `where` names the shared sentence. Holotype NHM.2018.21756, 450 m, incomplete, 9 mm, 39 chaetigers; paratypes 5 (NHM.2018.21716; NHM.2018.14528–14531), incomplete, 6-9 mm, 36-45 chaetigers, 450-456 m; sex not stated; colour "in alcohol", preserved material. Conditions match (paratype number not stated, uncounted). Family heading "Orbiniidae Hartman, 1942" printed.

**Line 6 MATCH.**

### Line 7, Iranobelgrandia persica, eye_type none

Soft parts morphology and anatomy: "No eyes, body with no pigment." **Quote MATCH.** Diagnosis concurs: "shell thin-walled and translucent, neither eyes nor pigment". Holotype "ethanol-fixed specimen ... NHMW-MO-113910"; paratypes "5 dry and 9 ethanol-fixed specimens", of which 2 destroyed for sequencing, 3 destroyed for anatomy, 3 at ZMUJ, 1 ethanol and 3 dry with J. Grego, 2 dry with Y. Fatemi. Conditions match (the two sequenced paratypes are not named, uncounted). Type locality Tuveh seasonal spring, Andimeshk, Khuzestan.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Tetranemertes bifrost, 10-20 per side | FIXABLE | method, conditions | quote MATCH (19); method says type specimens, page says live specimens only; locality stretched to whole series |
| 2 | Tetrastemma album, 4 | MATCH | none | quote MATCH (9); live holotype only; "deep-sea" optional fix |
| 3 | Tetrastemma shohoense, 4 | MATCH | none | quote MATCH (13); live holotype only |
| 4 | Placobdelloides sirikanchanae, 1 pair | FIXABLE | method, conditions | quote MATCH (14); holotype printed "mature"; live-or-preserved not stated (Fig. 4 live) |
| 5 | Oerstedia pseudoculata, 4 | FIXABLE | family, conditions, note | quote MATCH (10); one female paratype not stated; Oerstediidae printed but left empty |
| 6 | Leitoscoloplos olei, none | MATCH | none | quote MATCH (13); preserved type block matches |
| 7 | Iranobelgrandia persica, none | MATCH | none | quote MATCH (6); Diagnosis concurs; type block matches |

Errors 3 of 7 audited records (42.9%). By kind: quotes 0; value meaning 0; sample composition / method 3 (lines 1, 4, 5); filing convention 1 (line 5, same record); bibliographic 0; licence 0; names 0; duplicates 0. All fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-7 with the Replacement applied (lines 1, 4, 5 required; line 2 optional).

Unchecked: figures not viewed; the bifrost locality of paratype 852_080203_8, the Oerstedia paratype list and live/anaesthetized basis, the Placobdelloides paratype figure citations and the ZooKeys 938 licence sentence rest on tool summaries; the end of the bifrost page (last 3691 characters) was not read; no checklist gave current status of the seven names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1:
- `method`: "taxonomic description of live and compressed type specimens" -> "taxonomic description of live specimens, some compressed under a cover-glass"
- `conditions`: "from Bocas del Toro, Panama" -> "(USNM 1618678, 1156475, 1618745), held as histological sections, an anterior end and ethanol tissue; Table 2 places the CB057_18 specimens at Mangrove Point, Isla Colón, Panamá; the page does not say the live description is of the type specimens"

Line 4:
- `method`: "taxonomic description of preserved type specimens" -> "taxonomic description of the holotype (the eye sentence cites a photograph of the live holotype; the text does not say whether the description was made live or preserved)"
- `conditions`: "(sex and stage not given)" -> "(printed as mature; sex not given)"

Line 5:
- `family`: "" -> "Oerstediidae"
- `conditions`: "holotype ICHUM 8587 (non-banded) with eight paratypes" -> "holotype ICHUM 8587 (non-banded, sex not given) with eight paratypes, of which only ICHUM 8584 is sexed (female)"
- `note`: "Family and order not printed on the page read, left empty." -> "The page prints Family Oerstediidae and Class Hoplonemertea; no order heading is printed, order left empty."

Line 2 (uncounted):
- `conditions`: "deep-sea sublittoral to upper bathyal collection in the northwestern Pacific" -> "dredged at 144-200 m off Miura, Kanagawa, Japan, northwestern Pacific"
