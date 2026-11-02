# audit-374: desk-d284, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d284 files present untracked in the worktree (docs/tracks/progress/desk-d284.md and docs/views/evidence/desk-d284.jsonl, 7 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d284). Worktree HEAD 14b92427; origin/main has since moved to 6873b0bc (Merge d283 after audit 373), against which duplicates were checked. `python3 -I tools/senses/check.py | grep 'd284\.'`: "docs/views/evidence/desk-d284.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 34, 4, 33, 11, 3, 8, 9, all within 40. Non-ASCII in quotes: the curly apostrophe in "Gicklhorn’s" (line 1), as printed. Line numbers are the file's (1-based). Format model audits 358 and 370 to 373.

Sources opened (WebFetch): api.crossref.org/works/ for 10.3897/zookeys.1191.114974, zookeys.1134.94198, subtbiol.47.113186, zookeys.1046.64489 (all answered); api.crossref.org/works/10.3897/zookeys.1028.63822 refused by the tool as a repeat of an earlier client_error and not retried; a Crossref list query (filter prefix:10.3897, April 2021, query "Caridina incolor stygobiotic Guizhou", the rules' permitted form) returned that DOI's record. Pages: zookeys.pensoft.net/article/114974/download/xml/ (three passes); zookeys.pensoft.net/article/94198/download/xml/ (one pass); zookeys.pensoft.net/article/63822/download/xml/ (two passes); subtbiol.pensoft.net/article/113186/download/xml/ (three passes); zookeys.pensoft.net/article/64489/download/xml/ returned PROVENANCE_REQUIRED ("Do not retry"), not retried or worked around; zookeys.pensoft.net/article_preview.php?id=64489 (three passes; the URL the record cites). Names: zoobank.org NomenclaturalActs 5393D9DA-DCC8-49B0-BC2C-4C45FC2E45F4 (Phreatodrobia bulla); species.biodiversitydata.se/species/2299967 and 2299961 (P. micra, P. nugax: genus placement); zoobank.org act C65B4812-... (turned out to be Paladilhiopsis falniowskii, genus placement only). GBIF, WoRMS, MolluscaBase, PMC, Plazi, Zenodo, novataxa, bionames, Wikipedia and mirrors were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

## Bibliographic and licence

- Line 1 (Komeda, Ohtsuka, Huys 2024). Crossref: Sota Komeda, Susumu Ohtsuka, Rony Huys; title identical; ZooKeys 1191, 307-338, no issue; issued 2024-02-15; CC BY 4.0 vor; relation empty. Page citation verbatim: "Komeda S, Ohtsuka S, Huys R (2024) A new genus and species of oceanic planktonic Tisbidae " | "(Crustacea, Copepoda, Harpacticoida) with enlarged modified eyes. ZooKeys 1191: 307–338. ". Licence sentence CC BY 4.0 (tool summary). Accepted.
- Line 2 (Lin, Huang, Liang, He 2022). Crossref: Jun-Hui Lin, Ya-Qin Huang, Qian-Yong Liang, Xue-Bao He; title identical; ZooKeys 1134, 23-37; issued 2022-12-05; CC BY 4.0 vor; relation empty. Page citation "Lin J-H, Huang Y-Q, Liang Q-Y, He X-B (2022)", ZooKeys 1134: 23–37 (tool reading); licence "Creative Commons Attribution License (CC BY 4.0)". Accepted.
- Line 3 (Feng, Chen, Guo 2021). Crossref (list query): Shuo Feng, Qing-Hua Chen, Zhao-Liang Guo; title identical; volume 1028, 29-47; issued 2021-04-05; CC BY 4.0 vor; relation has-preprint 10.3897/arphapreprints.e64556 (the record cites the version of record, not the preprint). Page citation "Feng S, Chen Q-H, Guo Z-L (2021)", ZooKeys 1028: 29–47 (tool reading); page licence CC BY 4.0 (tool summary). Accepted; the note's "Crossref record could not be read" is now outdated (uncounted fix below).
- Lines 4, 5 (Perez et al. 2023). Crossref: Kathryn E. Perez, Yamileth Guerrero, Roel Castañeda, Peter H. Diaz, Randy Gibson, Benjamin Schwartz, Benjamin T. Hutchins; title identical; Subterranean Biology 47, 1-27; issued 2023-12-04; one licence entry https://creativecommons.org/share-your-work/public-domain/cc0/, vor, start 2023-12-04; relation empty. Page citation verbatim: "Perez KE, Guerrero Y, Castañeda R, Diaz PH, Gibson R, Schwartz B, Hutchins BT (2023) Two new" | " phreatic snails (Mollusca, Caenogastropoda, Cochliopidae) from the Edwards and Edwards-Trinity" | " aquifers, Texas. Subterranean Biology 47: 1–27. ". Page licence verbatim: "This is an open access article distributed under the terms of the CC0 Public Domain Dedication." CC0 under audit 327: the dedication is printed on the publisher's own copy read; Crossref carries the same instrument (its URL is the CC0 information page, not the legal-code URL, but it names CC0 and nothing else) for the vor; no conflicting tag. Accepted. (ZooBank's act lists an extra "Benjamin F. Schwartz & Benjamin Schwartz"; the page and Crossref have one Schwartz, as the record does.)
- Lines 6, 7 (Hofman et al. 2021). Crossref: Sebastian Hofman, Jozef Grego, Aleksandra Rysiewska, Artur Osikowski, Andrzej Falniowski; title identical; ZooKeys 1046, 157-176; issued 2021-06-21; CC BY 4.0 vor; relation empty. Page citation verbatim: "Citation: Hofman S, Grego J, Rysiewska A, Osikowski A, Falniowski A (2021) Two new species of the Ba" | "lkan genus *Paladilhiopsis* Pavlović, 1913 (Caenogastropoda, Moitessieriidae). ZooKeys 1046: " | "157-176. ". Licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names

None of the genera is on main. All seven names are new taxa described in the paper cited.
- Gyorome guttatum, Nereis tricirrata, Caridina incolor, Vitropyrgus lillianae: original descriptions only; search results led only to Plazi treatment copies, DOAJ, novataxa and bionames, none a checklist. Accepted on the original description, as in audits 370 to 373.
- Phreatodrobia bulla: ZooBank nomenclatural act, verbatim "Phreatodrobia bulla", rank Species, parent Phreatodrobia, publication the paper cited (authority string as ZooBank prints it: "Perez, Castaneda in Perez, Guerrero, Castañeda, Diaz, Gibson, Schwartz & Schwartz & Hutchins, 2023"). Registered; no later status seen.
- Paladilhiopsis stellatus "Grego & Hofman, sp. nov.", P. arion "Rysiewska et Osikowski, sp. nov." (as printed): original description only. No checklist reachable: GBIF and MolluscaBase refused by rule; the one ZooBank act in the results was for P. falniowskii (genus placement only). Accepted on the original description.

Family and order:
- Tisbidae / Harpacticoida: printed "Order Harpacticoida Sars, 1903", "Family Tisbidae Stebbing, 1910". Met.
- Nereididae / Phyllodocida: printed "Order Phyllodocida Dales, 1962", "Family Nereididae de Blainville, 1818"; main files Nereididae under Phyllodocida 3 times. Met.
- Atyidae / Decapoda: taxonomic classification "Order Decapoda ... Family Atyidae" (tool summary), title "(Decapoda, Caridea, Atyidae)"; main has Atyidae/Decapoda 3 times. Met.
- Cochliopidae / Littorinimorpha: printed "Littorinimorpha Golikov & Starobogatov, 1975", "Truncatelloidea Gray, 1840", "Cochliopidae Tryon, 1866"; species.biodiversitydata.se (Phreatodrobia micra, P. nugax) gives "Order: Littorinimorpha", "Family: Cochliopidae". Met. Littorinimorpha is an order; class (Gastropoda) not filed as order.
- Moitessieriidae / order empty: the paper prints "Family Moitessieriidae Bourguignat, 1863" with no class or order line; its text names the superfamily "Truncatelloidea" ("representing several families belonging to the Truncatelloidea"), not an order. No checklist reachable to supply the order (a search-result title from worldspecies.org reads "Animalia > Mollusca > Gastropoda > Littorinimorpha > Moitessieriidae", not opened and not a named checklist). Empty order is not a fault (audit 370's ruling; main's Erhaia dijiang row has no order key). "Caenogastropoda" (title) is a subclass-level group and is rightly not filed as order. Met.

Name faults 0.

## Duplicates

git grep on origin/main (6873b0bc) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Moitessieri, Paladilhi, Gyorome, Tisbidae, tricirrata, "Caridina incolor", Vitropyrgus, Phreatodrobia, lillianae and the DOIs/article ids (zookeys.1191, 114974, zookeys.1134., 94198, zookeys.1028, 63822, subtbiol.47, 113186, zookeys.1046, 64489): one unrelated hit (PMID 11497415 in sheets/salamander.audit.md). All 180 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: hits only in research/desk-d284 itself (and the same salamander line). audit-3*.md hold-outs: none name these taxa or DOIs. Nereididae on main is Platynereis dumerilii and Hediste diversicolor only; no Caridina incolor (Caridina zhaoi, desk-d282, is a different species).

Duplicates 0.

## Trait keys and rulings

- eye_type filing (main, audits 370 to 372): absence as "none (...)"; reduction or variation as a descriptive string. Lines 2, 4, 5, 6, 7 file "none (...)"; line 1 a descriptive structure string; line 3 a descriptive range. All fit.
- Variation (line 3): "ranging from reduced to completely blind" is among-specimen variation, filed as a descriptive value with the proportions in conditions (79% pigmented cornea, 21% blind, N = 43), as audit 371 accepted "absent in 3 of 5". Filed correctly.
- Attribution by heading (lines 2, 4 to 7): each sentence sits under one new species' Description (or Soft parts) heading and states the value itself; acceptable as in audits 362, 364 and 370 to 373. Lines 1 and 3 name the species.

## Per-record findings

### Line 1, Gyorome guttatum, eye_type large paired frontal modified eyes

Abstract (single paragraph), verbatim in three abutting chunks: "The most distinguishable feature of G. guttatum gen. et sp. nov. is the presence of large, paired, " | "frontal modified eyes, each consisting of a baculiform ocellus, a globular (Gicklhorn’s?) organ, " | "and a semi-parabolic plate." Curly apostrophe and the comma before "and" confirmed. Preceded by "Within this clade, Gyorome gen. nov. appears most closely related to Neotisbella Boxshall, 1979."; followed by the Tisbe spinulosa sentence (tool summary). **Quote MATCH**, 34 words, ends seen. Value drops the comma and keeps "(Gicklhorn's?)", so the authors' doubt about the organ stays; it says no more than the quote. Diagnosis: "Cephalic region with large, paired, modified eyes"; female description "Anterior part of cephalosome with middorsal pair of baculiform ocelli (BO in Fig. 2A, B)" and "one pair of globular organs (GO in Fig. 2A, B) each surrounded by thin semi-parabolic plate (SP in Fig. 2A, B)"; the female description rests on n = 3 ("Total body length ranging from 1.64–1.80 mm (n = 3)."). Male description opens verbatim "Prosome resembling that of female except for denticles covering dorsal surface of cephalothorax and " | "pedigerous somites much denser and middorsal protrusion around posterior margin of cephalothorax " | "not expressed (Fig. 6A, B)." and does not mention eyes; the record says so. Type material: holotype undissected female 1.80 mm NSMT-Cr 31562; allotype male 1.47 mm, dissected on slide, NSMT-Cr 31563; paratypes dissected female NSMT-Cr 31564, undissected female NSMT-Cr 31565 (tool summary). Collection verbatim: "on 28 November 2018 during the 1828 research cruise by the TRV SEISUI-MARU of Mie University."; "An oblique tow (sampling depth 0–935 m) at speed of 2 knots was performed using an ORI net"; "Specimens were fixed in 10% neutralized formalin seawater immediately after capture". Conditions right.

Uncounted: the conditions could add that the female description rests on all three females (n = 3) and that the male description says the prosome resembles the female's except for denser denticles and the missing middorsal protrusion, which neither confirms nor denies male eyes.

**Line 1 MATCH.**

### Line 2, Nereis tricirrata, eye_type none (eyes absent)

Under "Description.", verbatim: "Eyes absent (Fig. 2B)." Preceded by "One pair of biarticulated palps arising antero-laterally, palpophores cylindrical, palpostyles globular."; followed by "Peristomium apodous, 1.5 times as long as chaetiger 1." **Quote MATCH**, 4 words. The Description opens "Holotype complete but broken into two fragments," and Fig. 2B is the holotype (tool summary). Abstract verbatim "The most noteworthy feature is the absence of eyes on the prostomium."; Introduction verbatim "two interesting nereidid specimens without prostomial eyes were collected from a sedimentary habitat."; Diagnosis character (1) "absence of eyes on the prostomium". Type material: holotype TIO-BTS-Poly-137, complete, 17°33'N, 111°9'E, 1766 m, 16 June 2019; paratype TIO-BTS-Poly-138, incomplete (45, 12 and 7 chaetigers), 18°26'N, 112°26'E, 1157 m, 21 June 2019; box sampler, R/V "Haiyangdizhi 10"; no sex or maturity stated (tool summary). Conditions right.

Uncounted: the paratype's own site, depth and date could be added, since the Introduction's two-specimen statement covers it.

**Line 2 MATCH.**

### Line 3, Caridina incolor, eye_type reduced to completely blind

Abstract, verbatim pieces: "Caridina incolor sp. nov. differs from epigean congeners by its smaller eyes which range from reduced to completely blind" | "; colorless body and appendages; long stylocerite and sixth" | "and sixth abdominal segment; and relatively large eggs." (overlap "and sixth" confirms the join); next sentence verbatim "In comparison to other cave species, Caridina incolor sp. nov.". **Quote MATCH**, 33 words, ends seen, names the species. Value: "eyes smaller than in epigean congeners, ranging from reduced to completely blind" says no more than the quote. Description, Eyes paragraph, verbatim piece "with the smaller pigmented cornea (79%, N = 43), or totally pigmentless and blind (21%)."; the rest (small, bullet-shaped, reduced, short stalk, no facets) tool summary. Type material: holotype adult male; paratypes 23 males and 19 females (lots 1 + 16 + 6 males, 10 + 9 females; tool summary), so N = 43 is the whole type series. Variation carried in value and conditions.

Uncounted: the note's Crossref sentence is outdated (list query returned CC BY 4.0 vor).

**Line 3 MATCH.**

### Line 4, Vitropyrgus lillianae, eye_type none (no visible eyes)

Under the species heading "Description.", verbatim: "Mantle tissue unpigmented. No visible eyes and no visible pigment at base of eyestalks. No ctenidium observed, osphradium rounded." **Quote MATCH**, 11 words. The genus treatment has only Type species, Diagnosis ("Animal eyeless and unpigmented.") and Taxonomic remarks; the Description sits under the species. "visible" kept in the value. Type material: holotype ANSP 494654, Comal Spring Upwelling #7, Landa Park, New Braunfels, Comal County, 2 May 2019, drift net, R. Gibson; paratypes ANSP 494656, same site, 1–5 June 2018 (tool summary); 95% ethanol from the general methods. No anatomy count; shell measurements verbatim "Average shell measurements for adults (n = 20)"; "Neither apocrine glands or papillae present on examined individuals." Conditions right.

Uncounted: conditions could give the shell n = 20 and that no count is given for the animals examined.

**Line 4 MATCH.**

### Line 5, Phreatodrobia bulla, eye_type none (eyes absent)

Under the species heading "Description.", verbatim: "Body visible through translucent shell. No eyes present. Ctenidium composed of triangular filaments, approximately as broad as high, stretching..." **Quote MATCH**, 3 words. Type material: holotype ANSP 494658, paratype ANSP 494660, Hidden Springs, Bell County, P. Diaz, 27 October 2021; number and live status not stated; shell measurements "(n = 14 adult individuals)" (tool summary with verbatim piece). No statement on eyes of other Phreatodrobia; the Introduction says cave snails are "typically small (<3 mm), depigmented, and eyeless." Conditions right.

Uncounted: conditions could give the shell n = 14.

**Line 5 MATCH.**

### Line 6, Paladilhiopsis stellatus, eye_type none (no eyes)

Under "Soft parts morphology and anatomy.", verbatim: "Soft parts morphology and anatomy. Body white, with no pigment, with no eyes." (first sentence after the run-in heading); followed by "Female reproductive organs (Fig. 8) typical of the genus Paladilhiopsis (Hofman et al. 2018),". **Quote MATCH**, 8 words. The same paragraph also describes the penis ("The simple penis (Fig. 9) typical of the genus, without any outgrowth,"), so the soft-part account rests on at least one female and one male, though no specimen count or holotype sex is given. Holotype verbatim: "Holotype. Ethanol-fixed specimen (Fig. 6C), interstitially in the gravel below the bottom of the spring; " | "J. Grego, A. Falniowski, R. Ozimec, M. Olšavský, J. Olšavská leg.; 08 August 2020; NHMW113632." Paratypes: ten ethanol-fixed paratypes at the Jagiellonian University plus dry paratypes (ZMUJ-M.2633–2642, HNHM, NHMW-MO, SMF, PG, JG-F1628) (tool summary). Spring Zvezda, Slime, Omiš district, Croatia. Conditions right on the eye basis.

Uncounted: conditions say "sex not stated"; true of the type listing, but the soft-parts paragraph describes female organs and a penis; the dry paratypes are omitted.

**Line 6 MATCH.**

### Line 7, Paladilhiopsis arion, eye_type none (no eyes)

Under "Soft parts morphology and anatomy.", the paragraph's three sentences in order, verbatim: "The body is white, without pigment, with no eyes." / "The arrangement of pellets in the rectum characteristic for the Moitessieriidae (Boeters and Gittenberger 1990)." / "The anatomy is unknown." **Quote MATCH**, 9 words. Type locality verbatim: "Vrelo “Lušac” (Gučina), BiH (42°42'04"N, 18°21'27"E) (locality 3)."; holotype ethanol-fixed ZMUJ-M.2643 (Fig. 6Q); paratypes five empty shells ZMUJ-M.2644–2648; 10 September 2019; Bou-Rouch pump (tool summary). The holotype is the only soft-bodied specimen, so the eye sentence rests on one animal; the record says so in the note.

Uncounted: the conditions say "the next sentence of the paper says 'The anatomy is unknown'"; the next sentence is the rectum-pellets one, and "The anatomy is unknown." follows it. The locality drops the printed diacritics ("Lušac", "Gučina").

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Gyorome guttatum, large paired modified eyes | MATCH | none | Abstract quote MATCH (34), three chunks; female n = 3; male eyes undescribed, as recorded |
| 2 | Nereis tricirrata, none (eyes absent) | MATCH | none | quote MATCH (4), holotype Description; Diagnosis and Introduction agree |
| 3 | Caridina incolor, reduced to completely blind | MATCH | none | quote MATCH (33), join seen; variation 79%/21% of N = 43 in conditions |
| 4 | Vitropyrgus lillianae, none (no visible eyes) | MATCH | none | quote MATCH (11); CC0 accepted under audit 327 |
| 5 | Phreatodrobia bulla, none (eyes absent) | MATCH | none | quote MATCH (3); CC0 accepted; ZooBank act seen |
| 6 | Paladilhiopsis stellatus, none (no eyes) | MATCH | none | quote MATCH (8); order empty acceptable (not printed, no checklist reachable) |
| 7 | Paladilhiopsis arion, none (no eyes) | MATCH | none | quote MATCH (9); single soft-bodied holotype stated |

Errors 0 of 7 audited records (0%), within the 5% bar; none held out. By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0 (lines 4, 5 CC0 page sentence plus Crossref CC0 vor, no conflict; line 3 Crossref CC BY 4.0 vor via list query); names 0 (original descriptions; ZooBank for P. bulla; Cochliopidae/Littorinimorpha also from species.biodiversitydata.se); filing convention 0; order/class 0; duplicates 0 against main, all 180 desk-d2* and audit-3* branches and the audit-3* hold-outs. Verdict: pass; merge with the uncounted fixes below at the owner's choice.

Unchecked: checklist entries for Gyorome guttatum, Nereis tricirrata, Caridina incolor, Vitropyrgus lillianae and both Paladilhiopsis species (WoRMS, MolluscaBase and GBIF refused by rule; no Catalogue of Life page reached; Vitropyrgus ZooBank LSID printed in the paper but not in search results, so not opened); the order for Moitessieriidae (no reachable checklist); zookeys.pensoft.net/article/64489/download/xml/ (PROVENANCE_REQUIRED, not retried), so lines 6 and 7 rest on the article_preview page; the page licence sentences of lines 1 and 3 and several type-material details rest on tool summaries; the Caridina Eyes paragraph beyond the 79%/21% piece; whether the Gyorome allotype is stated as adult.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). All changes uncounted.

Line 2:
- `conditions`: "sex not reported; box-sampler sediment from 1766 m" -> "sex not reported; the paratype came from a second site (18 26 N, 112 26 E, 1157 m, 21 June 2019); box-sampler sediment, holotype from 1766 m"

Line 3:
- `note`: "the Crossref record could not be read (client error)" -> "the single-DOI Crossref record failed (client error), but a Crossref list query returned CC BY 4.0 (vor) for this DOI"

Line 4:
- `conditions`: "sex and number of specimens not stated" -> "sex not stated; shell measurements rest on 20 adults, and no count is given for the animals examined for soft parts"

Line 5:
- `conditions`: "sex, number and live-collected status not stated" -> "sex and live-collected status not stated; shell measurements rest on 14 adults, and no count is given for the animals examined for soft parts"

Line 6:
- `conditions`: "plus ten ethanol-fixed paratypes" -> "plus ten ethanol-fixed paratypes and dry paratypes in several collections"
- `conditions`: "sex not stated; the soft-parts sentence is not tied to a named specimen" -> "sex of the types not stated, though the same soft-parts paragraph describes female reproductive organs and a penis; the soft-parts sentence is not tied to a named specimen"

Line 7:
- `conditions`: "Vrelo Lusac (Gucina)" -> "Vrelo Lušac (Gučina)"
- `conditions`: "and the next sentence of the paper says" -> "and the paragraph, after a sentence on the arrangement of pellets in the rectum, says"
- `note`: "The paper's following statement that the anatomy is unknown" -> "The paragraph's closing statement that the anatomy is unknown"
