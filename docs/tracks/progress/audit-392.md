# audit-392: desk-d300, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d300 files present untracked in the worktree (docs/tracks/progress/desk-d300.md and docs/views/evidence/desk-d300.jsonl, 7 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d300). Line numbers are the file's (1-based). HEAD equals origin/main (21a90ce4). `python3 -I tools/senses/check.py | grep 'd300\.'`: "docs/views/evidence/desk-d300.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 6, 19, 18, 9, 7, 10, 8, all within 40; the only non-ASCII characters are the ellipsis (lines 1, 3), µ and the en dash (line 3) and the en dash (line 6).

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/4478/download/xml/ and zookeys.pensoft.net/article_preview.php?id=4478 (two passes); zookeys.pensoft.net/article/3956/download/xml/; zookeys.pensoft.net/article/26308/download/xml/ (two passes); zse.pensoft.net/article/128211/download/xml/; zookeys.pensoft.net/article_preview.php?id=128260 (two passes) and zookeys.pensoft.net/article/128260/download/xml/ (the XML returned to the tool lacks the species treatment); europeanjournaloftaxonomy.eu/index.php/ejt/article/download/467/1013 (two passes); Crossref single-DOI lookups api.crossref.org/v1/works/ for the six DOIs. Plazi, Zenodo, PMC, DOAJ, bionames and university-repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches.

## Bibliographic and licence

- Line 1 (de Souza, Morais, Cordeiro, Leal-Zanchet 2015). Byline Stella Teles de Souza, Ana Laura Nunes Morais, Lívia Medeiros Cordeiro, Ana Maria Leal-Zanchet; Crossref lists Leal-Zanchet first (the record follows the page, right). The page's own citation line prints "de Souza ST, Morais ALM, Cordeiro LM, Leal-Zanchet AM (2015)"; "ALM" disagrees with the byline's Ana Laura Nunes Morais, so "Morais ALN" (from the byline) is defensible; optional note addition below, not counted. Title identical; ZooKeys 470: 1-16, no issue; issued 2015-01-12; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 2 (Stocchino, Sluys, Manconi 2014). Page Giacinta Angela Stocchino, Ronald Sluys, Renata Manconi; Crossref Giacinta Stocchino (order the same); title identical; ZooKeys 425: 71-88; issued 2014-07-15; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 3 (Leal-Zanchet, Marques 2018). Page and Crossref Ana Leal-Zanchet, Alessandro Marques; title identical including "(Platyhelminthes, Tricladida)"; ZooKeys 776: 13-25; issued 2018-07-26; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Lines 4, 5 (Pérez-García, Gouveia, Calado, Noreña, Cervera 2024). Page and Crossref Patricia Pérez-García, Filipa Gouveia, Gonçalo Calado, Carolina Noreña, Juan Lucas Cervera; title identical; Zoosystematics and Evolution 100(4): 1487-1513; issued 2024-11-07; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 6 (Cuadrado, Hernández-González, Noreña, Simões 2024). Page author line "Daniel Cuadrado, Alejandro Hernández-Gonzalez, Carolina Noreña, Nuno Simões"; the page's citation line prints "Hernández-González" (tool summary); Crossref Hernández-Gonzalez. The record's spelling matches the citation line and is accepted; the note's "The page prints Hernández-González" is half right (fix below, uncounted). Title identical; ZooKeys 1221: 103-144; issued 2024-12-13; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 7 (Stocchino, Sluys, Kawakatsu, Sarbu, Manconi 2017). Page and Crossref Giacinta Angela Stocchino, Ronald Sluys, Mahasaru Kawakatsu, Serban Mircea Sarbu, Renata Manconi; title identical; European Journal of Taxonomy 342: 1-21; issued 2017-08-08; Crossref CC BY 3.0 content-version unspecified; page prints "This work is licensed under a Creative Commons Attribution 3.0 License." Accepted under the "unspecified + page-printed" rule.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All seven species are described as new in the cited papers; names rest on the original descriptions (no checklist opened). Higher taxa as printed: "Family Dugesiidae Ball, 1974" (line 1); Tricladida, Dugesiidae in the title (line 2); "Family Geoplanidae Stimpson, 1857" (line 3); Suborder Acotylea, Superfamily Stylochoidea, "Family STYLOCHIDAE Stimpson, 1857" (lines 4, 5); Tricladida, Dendrocoelidae in the title (line 7). Order is filed as order in every line.

Line 6 leaves `family` empty, but the paper prints the classification heads "Leptoplanoidea Faubel, 1984" and "Stylochoplanidae Faubel, 1983" above Stylochoplana sisalensis, and the Emprosthopharynx treatment follows with no new family head, so the paper places the genus in Stylochoplanidae. Counted with line 6 below.

## Trait keys

eye_type (lines 1, 3, 4, 5, 7) and eyes_count (lines 2, 6) are on main; no new key. Trait-key faults 0.

## Duplicates

`git grep -i` on origin/main (21a90ce4) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for multidiverticulata, "Dugesia bifida", ferrariaphila, marimarensis, erytheius, hartei, obstinatum and the six DOI strings: no hit. Dugesia gemmulata, on main from desk-d285, rests on Liu et al. 2022, Zoosystematics and Evolution 98(2), DOI 10.3897/zse.98.83184, a paper this unit does not use. The 92 remote desk-d250 to d399 and audit-350 to 399 branches (desk-d300 excluded) grepped under docs/views and docs/tracks/progress for the same names and DOI strings: no hit. (A first grep over all 689 desk and audit branches was cut off by the time limit before it finished.) Duplicate faults 0.

## Per line

### Line 1, Girardia multidiverticulata, eye_type "absent (eyeless)"

Description: "Live specimens unpigmented and eyeless (Figs 4–6)." The record ends at "eyeless …", the ellipsis standing for the figure reference. **Quote MATCH.** Abstract "are unpigmented and eyeless."; Diagnosis "Blind and unpigmented Girardia species ..."; Discussion contrasts G. mckenziei (minute eyes), G. guatemalensis (two small eyes) and G. paramensis (a pair of eyes), other species; all as the note says. Type material (holotype MZUSP PL.1573, 18 slides; paratypes MZU PL.00184, 61 slides; PL.00185, 8 slides; PL.00186, transverse, 16 slides; "Buraco do Bicho" cave, July 2011), Methods "Live specimens were photographed in the field and in the laboratory (Figs 4–6)." and "fixed with 10% Formalin", and "Preserved specimens up to 20 mm long and 3 mm wide (Table 1)." all as filed.

Fault: the conditions say "sexes and maturity of the individual specimens not stated here". The Discussion says of paratype MZU PL.00184 "Despite the fact that this specimen is mature, it has a small copulatory bursa" (rest of sentence a tool summary). So at least one paratype is stated mature, and the record's statement is wrong for the type series. Fixable.

**Line 1 FIXABLE.**

### Line 2, Dugesia bifida, eyes_count 2

Description: "Two eyes present in the centre of the head; unpigmented auricular grooves marginally placed just posteriorly to the eyes." **Quote MATCH**; only the count is logged. Holotype ZMA V.Pl. 7189.1 (8 slides) and ten paratype lots CGAS Pla 7.1-7.5 and ZMA V.Pl. 7189.2-7189.6 near Antsariboti, 16 September 2011; all 22 individuals asexual at collection; about 4% of fissiparous specimens sexualised in the laboratory; fissiparous 6-7 mm, sexualised "11–15 mm × 1.5–2 mm" (tool summary for the 4%); Abstract and Diagnosis silent on eyes; Discussion "Dugesia myopa also has a short common oviduct and reduced eyes."; no variation in eye number reported. All as filed.

**Line 2 MATCH.**

### Line 3, Pasipha ferrariaphila, eye_type "monolobate eyes (pigment cups of 15-25 µm) in an irregular row around the anterior tip"

Description: "Eyes, initially monolobate (pigment cups of 15–25 µm) and disposed in an irregular row, surround anterior tip (Fig. 3)." The record ends at "tip …" for the figure reference. **Quote MATCH.** Following sentences "After that, some eyes become bilobed (pigment cups of 10–15 µm) and spread onto dorsal surface of body." and "Towards posterior end, eyes gradually becoming sparser." are given in the conditions. Type material: holotype MZUSP PL 2141 only, Conceição do Mato Dentro, 16 January 2014; "A single specimen was collected during the day by direct sampling."; "fixed in 70% ethyl alcohol during field work"; "After fixation, length of 22 mm, maximal width of 2 mm, and maximal height 0.7 mm."; maturity not stated in words (tool summary). Abstract and Diagnosis "eyes spreading over the dorsal surface". All as filed.

**Line 3 MATCH.**

### Line 4, Stylochus marimarensis, eye_type "cerebral eyes in two elongated clusters between the tentacles"

Description: "Two elongated clusters of cerebral eyes between the tentacles." **Quote MATCH.** The same Description: "Tentacular eyes situated at the base and tips of the tentacles." and "Marginal eyes along the body margin, more numerous anteriorly."; the value names only the cerebral group and the conditions give the other two, so all eye groups are covered. Holotype only, MNCN 4.01/2820 to 3058, Station 12, Santa Maria del Mar Beach, Cádiz, 2 March 2014, 55 mm, 237 slides; no additional material; Diagnosis silent on eyes. All as filed.

**Line 4 MATCH.**

### Line 5, Stylochus erytheius, eye_type "marginal eyes along the entire body margin"

Description: "Marginal eyes along the entire body margin." **Quote MATCH.** Same Description: "Nuchal conical tentacles transparent, with tentacular eyes at the base and tips" and "Poorly visible cerebral eyes in two scattered clusters between the tentacles."; both in the conditions. Holotype MNCN 4.01/3059 to 3113 and 4336 to 4535, Station 11 (La Caleta Beach), 9 October 2014, 71 mm, 254 slides; additional material MNCN 4.01/3962 (35 mm), 3964 (37 mm), 3966 (120 mm), as the conditions say (sizes not given there; optional). Diagnosis silent on eyes; Remarks refer to S. marimarensis. All as filed.

**Line 5 MATCH.**

### Line 6, Emprosthopharynx hartei, eyes_count [20, 30] eyes per nuchal tentacle

Description: "Nuchal tentacles rounded and prominent, with 20–30 eyes per tentacle." **Quote MATCH**; value per tentacle, as stated. Same Description "Two small clusters of cerebral eyes close to the tentacles are, 12–20 eyes per cluster (Fig. 20B)."; Remarks "lacks marginal eyes as do E. pallida, ..."; both given in the note, so all eye groups are accounted for. Holotype CRPPY-0095 (1; 18 slides; 13 m; 10 May 2018), paratypes CRPPY-0092 (4) and CRPPY-0093 (3) (14 m; 9 May 2018), Dzilam; "Body shape elliptical, 10 mm length and 7 mm width."; all as filed.

Faults:
1. `family` is empty although the paper places the genus under "Stylochoplanidae Faubel, 1983" (see Names). Fixable.
2. `method` says "preserved, sectioned type specimens". The Description does not say whether it rests on live or fixed animals; it describes body colour ("Body constitution solid with a translucent background (Fig. 20A).") and Fig. 20 shows a living specimen and one "in situ, showing natural colouration" (tool summary for the captions). The record claims more than the page says. Fixable (counted with fault 1 as one record error).

Uncounted: the note's "a separate Diagnosis give[s] no eye detail" — no Diagnosis heading was found in the species treatment (two passes, tool summary); and the author-spelling sentence (see Bibliographic). Fixes below.

**Line 6 FIXABLE.**

### Line 7, Dendrocoelum obstinatum, eye_type "absent (lacking eyes)"

Description: "Live animals unpigmented, typically whitish, and lacking eyes." **Quote MATCH.** Holotype ZMA V.Pl. 7264.1 (4 slides), paratypes ZMA V.Pl. 7264.2 and 7264.3 (4 slides each) and one entire immature specimen in ethanol (ZMA V.Pl. 7264), Movile Cave, 5 April 2011; "Preserved mature specimens measured 3–8 mm in length, and 1–2 mm in width."; Abstract "with a total of nine examined populations"; Abstract and Diagnosis silent on eyes; Discussion contrasts D. sinisai ("its two eyes"), D. caspicum and D. grimmi ("multiple eyes"). As filed.

Fault: the conditions say the paper "gives no count of individuals". The Other material lists, besides sectioned specimens, lots of entire immature specimens in ethanol with counts from Movile Cave and the wells, from 1 to 21 per lot ("21 entire immature specimens preserved in ethanol (CGAS Pla 13)"; e.g. 5 from Movile Cave 11 April 2011, 20 from Albeşti, 11 and 12 from other wells; about 90 in all, tool tally), and the Movile Cave section says "Only a few flatworm specimens were found per collection." The record must say that counts are given per lot, that most of the material is immature, and that the paper says nothing about eyes in the well populations or juveniles beyond the general live-animal sentence. Fixable.

**Line 7 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Girardia multidiverticulata, eyeless | FIXABLE | conditions | paper states paratype MZU PL.00184 mature; record says maturity not stated |
| 2 | Dugesia bifida, 2 eyes | MATCH | | quote, type series, asexual stage and Discussion contrast all right |
| 3 | Pasipha ferrariaphila, monolobate eyes at anterior tip | MATCH | | holotype only, fixed, later dorsal spread stated |
| 4 | Stylochus marimarensis, cerebral eyes | MATCH | | holotype only; tentacular and marginal groups given |
| 5 | Stylochus erytheius, marginal eyes | MATCH | | holotype plus additional material; tentacular and cerebral groups given |
| 6 | Emprosthopharynx hartei, 20-30 eyes per tentacle | FIXABLE | family, method | family Stylochoplanidae printed but left empty; "preserved, sectioned" not supported by the Description |
| 7 | Dendrocoelum obstinatum, lacking eyes | FIXABLE | conditions | Other material gives per-lot counts (about 90 entire immature specimens); record says no count |

Errors: 3 of 7 records (43%), all fixable; none to hold out. Verdict: **ACCEPT AFTER REPLACEMENT** (lines 2-5 as filed; lines 1, 6, 7 with the replacements below).

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1:
- `conditions`: "sexes and maturity of the individual specimens not stated here" -> "the Discussion states that paratype MZU PL.00184 is mature (its copulatory bursa small); maturity of the holotype and the other two paratypes is not stated"

Line 6:
- `family`: "" -> "Stylochoplanidae"
- `method`: "morphological description of preserved, sectioned type specimens" -> "morphological description of type specimens (holotype sectioned; the Description does not say whether the eye counts come from live or fixed animals, and Fig. 20 shows living specimens)"
- `note`: "The page prints Hernández-González; Crossref prints Hernández-Gonzalez, author order the same." -> "The page's author line and Crossref print Hernández-Gonzalez; the page's citation line prints Hernández-González, used here; author order the same."
- `note`: "species described as new in this paper; family not printed in the title." -> "species described as new in this paper; family Stylochoplanidae from the paper's classification heads (Leptoplanoidea Faubel, 1984; Stylochoplanidae Faubel, 1983), under which Emprosthopharynx follows Stylochoplana."

Line 7:
- `conditions`: "but gives no count of individuals" -> "and the Other material gives counts per lot: sectioned specimens and, as entire immature specimens in ethanol, lots of 1 to 21 from Movile Cave and the wells (about 90 in all); most material is immature, and the paper gives no eye statement for the well populations or juveniles beyond the general sentence on live animals"

Line 6 (uncounted):
- `note`: "Abstract and a separate Diagnosis give no eye detail." -> "The Abstract gives no eye detail and no Diagnosis is printed for the species."

Line 1 (uncounted):
- `note`: "Page order of authors is de Souza, Morais, Cordeiro, Leal-Zanchet (Pensoft XML);" -> "Page order of authors is de Souza, Morais, Cordeiro, Leal-Zanchet (Pensoft XML; the byline gives Ana Laura Nunes Morais, while the page's citation line prints 'Morais ALM');"
