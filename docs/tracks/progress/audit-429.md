# audit-429: desk-d318, evidence lines 8 to 14

Audited 1 November 2026 from the desk-d318 files present untracked in the worktree (docs/tracks/progress/desk-d318.md and docs/views/evidence/desk-d318.jsonl, 14 lines; neither committed here, neither edited; the file is identical to origin/research/desk-d318). This audit covers file lines 8 to 14 only; another auditor takes lines 1 to 7. HEAD equals origin/main (b5e93f6e4). `python3 -I tools/senses/check.py | grep d318`: "docs/views/evidence/desk-d318.jsonl: 14 records, 0 problems". Quote lengths (`len(q.split())`) for lines 8 to 14: 27, 36, 26, 12, 7, 22, 18, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): europeanjournaloftaxonomy.eu/index.php/ejt/article/download/2547/11497 (two passes), zookeys.pensoft.net/article/47061/download/xml/ (one pass), zookeys.pensoft.net/article/33955/download/xml/ (three passes), bdj.pensoft.net/article_preview.php?id=116082 (two passes), zookeys.pensoft.net/article/24538/download/xml/ (one pass). Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs, each answered on the first call. WoRMS, GBIF, PMC, DOAJ, library catalogue records (utm.my, cas.cz, uanl.mx), Hokkaido and Frankfurt repositories, core.ac.uk and reviewer.ly were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Lines 8 and 9 (Jaume-Schinkel, Kvifte 2024). Citation line "European Journal of Taxonomy 935: 81–100"; Crossref volume 935, no page range, issued 2024-05-23; authors Santiago Jaume-Schinkel, Gunnar Mikalsen Kvifte in that order; title identical. Page prints "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)."; Crossref CC BY 4.0 unspecified. Accepted.
- Line 10 (Tsuyuki, Kajihara 2020). ZooKeys 918: 15–28; Crossref same authors and order, 15-28, CC BY 4.0 vor, issued 2020-03-12. Page licence CC BY 4.0 (tool summary). Accepted.
- Line 11 (Oya, Kimura, Kajihara 2019). Title printed in full ("... with inference on the phylogenetic position of Plehniidae"), ZooKeys 864: 1–13; page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0), ..."; Crossref CC BY 4.0 vor, issued 2019-07-15. Accepted.
- Lines 12 and 13 (Góngora-Garza, Tovar-Hernández, de León-González 2024). Byline "Gerardo Góngora-Garza, María Ana Tovar-Hernández, Jesús Angel de León-González" (Crossref has given name "María" only; the filed "MA" follows the byline). Title as printed with the space in "Parasphaerosyllis indica". Citation "Biodiversity Data Journal, 12, e116082, 2024"; page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 14 (Štys, Baňař 2018). Byline "Pavel Štys, Petr Baňař" (the Crossref rendering through the tool showed "Šťys"; the page prints "Štys", as filed). ZooKeys 796: 33–47; page CC BY 4.0 sentence; Crossref CC BY 4.0 vor, issued 2018-11-15. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Eugenys: headings print Class Insecta, Order Diptera, Family Psychodidae; filed as printed. Right.
- Enchiridium daidai: Taxon classification prints Animalia, Polycladida, Prosthiostomidae; keywords give Platyhelminthes; Turbellaria only as article category; no class (Rhabditophora or other) printed. Class blank right.
- Paraplehnia seisuiae: Taxon classification Animalia, Polycladida, Plehniidae; no class printed. Class blank right.
- Parasphaerosyllis: Taxon classification prints Annelida › Polychaeta › Phyllodocida › Syllidae. Class Polychaeta, order and family as printed. Right.
- Xenicocephalus tomhenryi: Taxon classification Animalia, Hemiptera, Enicocephalidae; the Abstract prints "(Insecta: Hemiptera: Heteroptera: Enicocephalomorpha: Enicocephalidae)". Class Insecta is printed on the page, so the blank class is a fault (counted, line 14).
- Names: all six are species described (or, for P. indica, re-described) in the papers read; WoRMS cannot be opened here (rules.md), and the searches returned no synonymy notice. The Psychodidae and Heteroptera names are as described in 2024 and 2018. Not counted.

## Repeats

`git grep -il` on origin/main (b5e93f6e4) over the whole docs/ tree for Eugenys, ejt.2024.935, Enchiridium, daidai, 918.47061, Paraplehnia, seisuiae, 864.33955, Parasphaerosyllis, e116082, Xenicocephalus, tomhenryi, 796.24538. Only hit: Enchiridium in docs/views/gaps/try-species.json, as "Enchiridium punctatum" (another species, no value). Unmerged branches: docs/views/evidence/desk-dN.jsonl read from all 318 origin/research/desk-d* branches (git show per branch) and grepped for the same species and DOIs; only origin/research/desk-d318 itself matches. No repeats.

## Per line

### Line 8, Eugenys singularis, eye bridge 3 facet rows

Description Head, three consecutive pieces: "Slightly wider than long; eye bridge contiguous, eye bridge with three facet rows; " / "no enlarged alveoli on postocular area; interocular suture non-discernible in examined material " / "(Fig. 6A)." **Quote MATCH**, 27 words, whole printed Head sentence after the "Head." label. Type material: holotype male and one male paratype, same data, LACM; "Measurements (in mm; n = 2)"; "Female: Unknown"; Diagnosis on hypopods only (tool summary). Value 3 exactly as printed for this species and sex; trait key fits. The conditions spell the locality "Sarapiqui"; the page prints "Puerto Viejo de Sarapaquí, Est. Biol. LaSelva". The place is identified correctly; spelling not counted (optional fix below).

**Line 8 MATCH.**

### Line 9, Eugenys upsilon, eye bridge 2 to 3 facet rows

"Head (holotype)." block, three consecutive pieces: "Wider than long; eye bridge contiguous, eye bridge with two facet rows on narrowest part " / "and three facet rows on remaining part of bridge; no enlarged alveoli on postocular area; " / "interocular suture appears absent (Fig. 7A)." **Quote MATCH**, 36 words. Holotype male (Ecuador, Pichincha, Pedro Vicente Maldonado, Roadway to Pachijal, 750 m, 1–9 Feb. 2022, I. Kilian); paratypes six males and one female, same data; "Measurements (in mm; n = 7)"; female "Same as male except for palpi consisting of three segments" with no eye wording (tool summary). Value [2, 3] with the narrowest/remaining split in conditions; eye field "adult male holotype" matches the heading. Counts, sexes and dates right.

**Line 9 MATCH.**

### Line 10, Enchiridium daidai, cerebral-eyespot clusters of 20 to 52

Description: "Pair of cerebral-eyespot clusters, each consisting of 20–52 eyespots" / "(left 20 and right 23 in holotype);" / "each cluster of an antero-posteriorly elongated spindle shape (Fig. 2B)." Previous sentence "Ventral surface translucent, without color pattern."; next begins "Marginal-eyespot clusters forming single marginal band, ...". **Quote MATCH**, 26 words. Material: holotype ICHUM 5993, 26 Jul 2018, 13–14 m off Bonomisaki, Kagoshima (sections plus remainder in ethanol); paratypes ICHUM 5994 and 5995, 5 m, Nago, Okinawa, 22 May 2019 (tool summary). Conditions right on counts, localities and dates. The conditions say "sex/maturity not read"; the Remarks say all specimens had reached sexual maturity (tool summary), which supports the eye field "adults". A disclosed gap, value unaffected; not counted (optional fix below). Class blank right.

**Line 10 MATCH.**

### Line 11, Paraplehnia seisuiae, eyespots small and embedded

Description: "Marginal and cerebral eyespots small and embedded in parenchyma (Fig. 1C, D)." Previous: "... female gonopore situated 2.5 mm posterior to male gonopore."; next: "At least 47 and 28 eyespots arranged in anterior body margin and from just behind brain" / "to anterior to brain, respectively, but detailed distribution of eyespots could not be observed." **Quote MATCH**, 12 words. Remarks: "The eyespots were invisible in the living specimen (Fig. 1A), probably because of the thickness" / "and opaqueness of the body, as well as the small size of each eyespot." "Live specimen 26 mm in length, 11 mm in width." "Tentacles lacking." Material: "One specimen: holotype, ICHUM 5345, 44 slides (14 slides for the anterior part" / "and 30 slides for the posterior part of the body)," / "dredged from 298–310 m depths, the Sea of Kumano, between 34°08.0'N, 136°37.8'E" / "to 34°07.8'N, 136°37.9'E, Japan."

Collection date, as asked: **the paper prints none.** Material examined has no date and no collector; the Methods paragraph ("A single polyclad specimen was collected by dredging during the research cruise No. 1722 by" / "Training/Research Vessel (TRV) Seisui-maru. ...") read whole gives none; captions, Tables 1 and 2 and Acknowledgements give none (tool summary); the only dates are received/accepted/published 2019 and the funding number "2017". The record's "collection date not read" should state that none is printed (replacement below; a disclosed gap, not counted). Sexual maturity is not stated; both gonopores are described.

**Line 11 MATCH** (with the date wording replaced).

### Line 12, Parasphaerosyllis irregulata, two pairs of eyes trapezoidal

Description: "Prostomium oval, wider than long." "Two pairs of eyes in trapezoidal arrangement." "Eyes of anterior pair longer than inferior pair, closer to external border of prostomium." "Eyespots absent (Fig. 2A)." **Quote MATCH**, 7 words, whole sentence. "Holotype complete, 35 mm long, 0.9 mm wide, 310 chaetigers." Holotype UANL 8158, 5 May 2015, 3 m, San Lorenzo Channel; paratype entries UANL 8159, ECOSUR 0000, CNAP–ICML 0000 (each individualCount 1) and UANL 8160 (no individualCount printed), all 5 May 2015, 3 m; no total given; sex and stage not stated. "four paratypes" is four paratype entries, one with no count; not counted (optional fix below). The eye field "adults" is not printed but a complete 310-chaetiger holotype; not counted.

**Line 12 MATCH.**

### Line 13, Parasphaerosyllis indica, four lensed eyes (holotype)

Description: "Four lensed eyes in trapezoidal arrangement, eyes from the anterior pair larger and more separate" / "than posterior pair of eyes (Fig. 1A)." followed by "Right anterior eye divided into two lobes, appearing to have two fused eyes." and "Eyespots absent." **Quote MATCH**, 22 words. Holotype BMNH 1937.9.2.156, Arabian Sea, Oman, 13.5 m, 2 November 1933. Value says no more than the quote; the fused right anterior eye is in conditions.

**Line 13 MATCH.**

### Line 14, Xenicocephalus tomhenryi, eyes prominent, semiglobular

Structure, Head: "Eyes prominent, semiglobular, with numerous separate, convex facets," / "eye width much shorter than synthlipsis, dorsal ocular index 1.94." Previous ends "... much shorter than strongly produced medial clypeo-mandibular projection."; next begins "Postocular part and postocular constriction (long and shallow)". **Quote MATCH**, 18 words. Type material: holotype female, macropterous, "Ecuador camino / Aloag-Tandapi / Pr. Pichincha 2600m", "12.II.1983", "A. Roig", "Drake Colln. ex / J. Maldonado C. / Coll. 1996", USNM; no paratypes. Species comparison "X. tomhenryi F: ... eyes short" vs "X. josifovi M: ... eyes long"; the dimorphism question is printed as the heading "Head (size of eyes sexually dimorphic?)" (tool summary). Conditions right.

Fault (one record error, fixable): **class blank though printed.** The Abstract prints "(Insecta: Hemiptera: Heteroptera: Enicocephalomorpha: Enicocephalidae)"; the note itself says Insecta is printed there. Class is filled as printed, so `class` should be "Insecta" (as on lines 8 and 9 of this unit).

**Line 14 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 8 | Eugenys singularis, 3 facet rows | MATCH | | whole Head sentence; holotype + 1 male paratype; female unknown |
| 9 | Eugenys upsilon, 2-3 facet rows | MATCH | | Head (holotype); 6 male + 1 female paratypes; n = 7 |
| 10 | Enchiridium daidai, 20-52 cerebral eyespots | MATCH | | whole sentence; class not printed |
| 11 | Paraplehnia seisuiae, eyespots small, embedded | MATCH | conditions (gap wording) | no collection date printed anywhere; "not read" replaced |
| 12 | Parasphaerosyllis irregulata, two pairs trapezoidal | MATCH | | whole telegraphic sentence; Polychaeta printed |
| 13 | Parasphaerosyllis indica, four lensed eyes | MATCH | | holotype re-description |
| 14 | Xenicocephalus tomhenryi, eyes prominent | FIXABLE | class | Abstract prints Insecta; class left blank |

Errors: 1 of 7 records (14.3%); 1 fixable (line 14), 0 held out, 0 unfixable; no line to drop. Repeats: none on main or on any unmerged desk branch. Verdict for desk-d318 lines 8 to 14: **ACCEPT AFTER REPLACEMENT** (lines 8 to 13 as filed, line 11 with its date wording replaced; line 14 with the class replacement below, or dropped if it is not applied). The pooled verdict for the unit also needs the lines 1 to 7 audit.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 14 (counted):
- `class`: `"class": ""` -> `"class": "Insecta"`
- `note`: "class Insecta appears only in the Abstract taxon line, so class is left blank" -> "class Insecta from the Abstract taxon line '(Insecta: Hemiptera: Heteroptera: Enicocephalomorpha: Enicocephalidae)'"

Line 11 (closes the disclosed reading gap; not counted):
- `conditions`: "collection date not read" -> "no collection date is printed (Material examined, Methods, captions, tables and Acknowledgements give none; the cruise is given only as No. 1722)"

Optional, not counted:
- Line 8 `conditions`: "Puerto Viejo de Sarapiqui" -> "Puerto Viejo de Sarapaquí (as printed)"
- Line 10 `conditions`: "sex/maturity not read" -> "the Remarks say all specimens had reached sexual maturity"
- Line 12 `conditions`: "four paratypes (UANL 8159, UANL 8160, ECOSUR, CNAP-ICML) from the same locality and date, sizes not given" -> "four paratype entries (UANL 8159, ECOSUR 0000 and CNAP-ICML 0000, one specimen each; UANL 8160 with no count printed) from the same locality and date, sizes not given"
