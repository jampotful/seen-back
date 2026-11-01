# audit-376: desk-d287, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d287 files present untracked in the worktree (docs/tracks/progress/desk-d287.md and docs/views/evidence/desk-d287.jsonl, 7 lines; neither committed here, neither edited). Worktree HEAD and origin/main ff133bd0 (Close d286 with 0). `python3 -I tools/senses/check.py | grep 'd287\.'`: "docs/views/evidence/desk-d287.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 2, 2, 7, 10, 4, 9, 2, all within 40 (the desk note's list "2, 2, 8, 9, 3, 9, 2" is off for lines 3 to 5; a progress-note slip, not a record fault). No non-ASCII characters in any quote. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all seven DOIs (10.3897/subtbiol.36.58272, zookeys.801.24102, subtbiol.37.61573, zookeys.795.27619, zookeys.419.5739, zookeys.69.739, subtbiol.49.118293; two first attempts rate-limited, both answered on retry); subtbiol.pensoft.net/article/58272/download/xml/; zookeys.pensoft.net/article/24102/download/xml/; subtbiol.pensoft.net/article/61573/download/xml/; zookeys.pensoft.net/article/27619/download/xml/; zookeys.pensoft.net/article_preview.php?id=3895 (the record's article/3895 xml URL did not appear in this audit's searches, so the preview page, which did, was read instead); zookeys.pensoft.net/article/2464/download/xml/ and article_preview.php?id=2464; subtbiol.pensoft.net/article/118293/download/xml/. All URLs were returned by a WebSearch first. PMC, Plazi, Zenodo, DOAJ, BHL, library catalogue and repository hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Garcia, Miralles-Núñez, Pérez-Fernández 2020). Crossref: Lluc Garcia, Adrià Miralles-Núñez, Toni Pérez-Fernández; title identical; Subterranean Biology 36, 51-61, no issue; issued 2020-11-16; CC BY 4.0 vor. Page citation verbatim "Garcia L, Miralles-Núñez A, Pérez-Fernández T (2020) First record of the genus Graeconiscus Strouhal, 1940"; licence sentence verbatim in three pieces (CC BY 4.0). Accepted.
- Line 2 (Taiti, Argano, Marcia, Scarpa, Sanna, Casu 2018). Crossref: same six in the same order; title identical; ZooKeys 801, 229-263; issued 2018-12-03; CC BY 4.0 vor. Page licence sentence verbatim (CC BY 4.0). Accepted.
- Line 3 (Falniowski, Grego, Rysiewska, Osikowski, Hofman 2021). Crossref: same five in the same order; title identical; Subterranean Biology 37, 89-104; issued 2021-02-16; CC BY 4.0 vor (the desk's Crossref client_error did not recur; Crossref now confirms the licence). Page citation "Falniowski A, Grego J, Rysiewska A, Osikowski A, Hofman S (2021)"; licence sentence verbatim opening (CC BY 4.0). Accepted.
- Line 4 (Reboleira, Enghoff 2018). Crossref: Ana Sofia P.S. Reboleira, Henrik Enghoff; title identical; ZooKeys 795, 93-103; issued 2018-11-08; CC BY 4.0 vor. Page citation verbatim "Reboleira ASPS, Enghoff H (2018) First continental troglobiont Cylindroiulus millipede (Diplopoda, Julida, Julidae)."; licence sentence verbatim. Accepted.
- Line 5 (Ribera, Elverici, Kunt, Özkütük 2014). Crossref: Kadir Kunt, Carles Ribera, Mert Elverici, Recep Özkütük (order differs from print); title identical; ZooKeys 419, 87-102; issued 2014-06-24; CC BY 4.0 vor; resource URL articles.php?id=3895. Page byline verbatim "Carles Ribera 1, Mert Elverici 2, Kadir Boğaç Kunt 3, Recep Sulhi Özkütük 4"; citation "Ribera C, Elverici M, Kunt KB, Özkütük RS (2014)". The record follows print, as audits 373 and 375 rule. Licence sentence verbatim (CC BY 4.0). Accepted.
- Line 6 (Lukić, Houssin, Deharveng 2010). Crossref: Louis Deharveng, Marko Lukić, Céline Houssin (order differs from print); title identical; ZooKeys 69, 1-16; issued 2010-11-18; CC BY 3.0 vor; resource URL articles.php?id=2464. Page header byline Marko Lukić, Céline Houssin, Louis Deharveng; no printed citation line. Licence verbatim opening "This is an open access article distributed under the terms of the Creative Commons Attribution License," (no version printed) with Crossref CC BY 3.0 vor; accepted (page with an unversioned Creative Commons Attribution sentence plus Crossref CC vor). Accepted.
- Line 7 (Mehrafrooz Mayvan, Parimuchová, Kováč 2024). Crossref: Mahmood Mehrafrooz Mayvan, Andrea Parimuchová, Ľubomír Kováč; title identical; Subterranean Biology 49, 31-51; issued 2024-06-03; CC BY 4.0 vor. Page citation "Mehrafrooz Mayvan M, Parimuchová A, Kováč Ľ (2024)"; licence sentence verbatim opening (CC BY 4.0). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout; printed years match Crossref issued years.

## Names and higher taxa

No checklist was reachable (WoRMS refused by rule; no World Spider Catalog or Collembola checklist species page in search results). All seven species are described as new in the cited papers, so the names rest on the original descriptions, as the desk says.

- Graeconiscus gevi: heading verbatim "Family Trichoniscidae Sars 1989" (the paper's misprint, as the note says); Isopoda filed as order, Oniscidea (suborder) not used. Met.
- Alpioniscus onnisi: "Family Trichoniscidae Sars, 1899". Met.
- Horatia ozimeci: "Family Hydrobiidae Stimpson, 1865", "Subfamily Horatiinae D. W. Taylor, 1966"; the taxon classification block gives Order "Littorinimorpha" (tool summary). Family filed, not subfamily. Met.
- Cylindroiulus villumi: "Order Julida Brandt, 1833", "Family Julidae Leach, 1814". Met.
- Typhlonesticus gocmeni: "Family Nesticidae Simon, 1894"; Araneae. Met.
- Tritomurus veles: family Tomoceridae; the page names the subfamilies (Tomocerinae, Lepidophorellinae) but no order; Entomobryomorpha and Tomoceroidea are absent (tool summary). Empty order is not a fault (audit 370's ruling, applied in audit 372); Collembola, a class-level name, rightly not filed as order (audit 371). Met.
- Oncopodura moghanensis: the XML classification block tags Entomobryomorpha as order and Oncopoduridae as family; title and abstract tag Entomobryomorpha as suborder (tool summary of the tags). Filed as the classification block gives it, as main files the parallel collembolan order Poduromorpha after audit 371; the note states the inconsistency. Met.

Name faults 0.

## Duplicates

git grep on origin/main (ff133bd0) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, codex-findings, progress notes) for Graeconiscus, gevi, Alpioniscus, onnisi, Horatia, ozimeci, Cylindroiulus, villumi, Typhlonesticus, gocmeni, Tritomurus, veles, Oncopodura, moghanensis, the seven DOIs, and the article ids (58272, 24102, 61573, 27619, 5739, 3895, 2464, 118293): only unrelated matches ("gevi" inside "longevity"; Cylindroiulus punctatus rows, a different species; "24102" in an Adelaide handle and a WFO id in audits 46 and 139). All 185 remote branches matching desk-d2* or audit-3*: species, genus, DOI and article-id hits only in research/desk-d287 itself (plus the same unrelated "24102" lines in branch copies of audits 46 and 139). No audit-3* branch names these genera.

Duplicates 0.

## Trait keys and rulings

All seven are eye_type with value "none (...)", the form main and audits 370 to 375 accept for eye absence; eyes_count is not used, rightly (no count printed). Every quote sits under the single new species' own Description heading, so a sentence not naming the species is attributable (audits 362 to 375). The desk progress note's hold-outs (sentences over 40 words, genus-level clauses, unread descriptions) are consistent with the QUOTE RULE.

## Per-record findings

### Line 1, Graeconiscus gevi, eye_type none

Description, first five sentences verbatim: "Maximum size observed: 3.2 mm (female), 3 mm (male)." "Body unpigmented." "Eyes absent." "Contour regularly ovoid, without interruption between pereon and pleon (Figs 2A, 4A–D)." "Pereon tergites very convex, with epimera expanded towards outside." **Quote MATCH**, third sentence as stated. Holotype verbatim "1 male; Málaga, Antequera, Cueva del Yeso III;" ... "27 Apr. 2008; Toni Pérez-Fernández leg.; MNCN 20.04/12093."; paratypes 3 males and 4 females (MNCN 20.04/12094 to 12100) plus CLLG lots of males and females from the same cave (2008 and 2009). Diagnosis verbatim "A blind and unpigmented species of"; Discussion contrasts G. thermophilus as "an oculated and slightly pigmented species". No eye variation printed. Conditions and note right.

**Line 1 MATCH.**

### Line 2, Alpioniscus onnisi, eye_type none

Description first paragraph verbatim in order: "Maximum length: ♂, 7.5 mm; ♀, 9 mm." "Colourless body, outline as in Fig. 5A." "Dorsal surface smooth with lanceolate scale-setae as in Fig. 5B." "Many gland pores on lateral margins of pleonites 4 and 5, telson and lateral surface of uropodal protopod (Fig. 5E)." "Cephalon (Fig. 5C, D) with suprantennal line medially blunt;" | "antennal lobes quadrangular obliquely directed outwards with concave dorsal surface." "Eyes absent." **Quote MATCH**, sixth sentence as "where" says. Holotype verbatim "♂ (MZUF 9817), Grotta Giuanniccu Mene", "Monte Castello di Quirra, Villaputzu 20.IV.2012,"; paratypes verbatim "many ♂♂ and ♀♀ (MZUF 9817), same data as holotype." with further lots (e.g. "1 ♀ (MZUF 9818), same locality, 8.I.2011"). No eye variation found; the Remarks were cut by the tool, so the ipogean-tomb lot was not seen.

Uncounted: the note lists "two cephalon sentences", which with the four earlier sentences would make "Eyes absent." the seventh; the cephalon text is one sentence divided by a semicolon, so "where" (sixth) is right and the note's wording is the slip.

**Line 2 MATCH.**

### Line 3, Horatia ozimeci, eye_type none

Description verbatim: "Soft parts morphology and anatomy. The body white, pigmentless, with no eyes. The anatomy unknown." **Quote MATCH**, 7 words. Holotype verbatim "Dry shell with operculum (Fig. 4B), J. Grego, A. Falniowski, M. Olšavský and J. Olšavská leg., August 5-th 2020, OZRM 11600." (Fig. 4 caption gives OZRM 11603, as the note says). Paratype verbatim "The single live collected paratype (Fig. 4A) has been destroyed for DNA extraction; GenBank number: MW448545." Further paratype lots (OZRM 11601/1 specimen, NHMW 113607/1, JG 1542/28, JG F0724/24) carry no statement of live bodies (tool summary). No sex stated. Type locality verbatim "Spring Izvor Ruda – Beguša, Ruda, sand at the stream bottom below the spring lake,". The conditions rest the soft-parts sentence on the single live paratype and the note marks this as inferred; the page names only one live-collected specimen, so the inference holds. Value says no more than the quote.

**Line 3 MATCH.**

### Line 4, Cylindroiulus villumi, eye_type none

Description second paragraph verbatim: "Body length up to 13 mm in females and 11.4 mm in males." "Vertical body diameter (H): 0.9 mm (females) and 0.7 mm (males)." "Integument unpigmented (Figure 1); eyes absent (Figs 1, 2A, B)." **Quote MATCH** (whole sentence, third), 10 words. Holotype verbatim "Holotype, male, Portugal, Estremenho karst massif, Algar do Pena Cave", "ASPS Reboleira leg., 04 Nov 2014."; paratypes verbatim "1 male, 2 females," | "4 juvenile males and 1 juvenile; same data but 28 Mar 2018, 1 female and 1 juvenile." Diagnosis verbatim "Differs from all other species in the group by the lack of eyes". No eye variation. Conditions right.

**Line 4 MATCH.**

### Line 5, Typhlonesticus gocmeni, eye_type none

Male Prosoma paragraph verbatim, three sentences: "Carapace approximately circular in dorsal view." "Cephalic region not differentiated from the rest of the carapace." "Eyeless (Figs 18, 19)." **Quote MATCH**, 4 words, third sentence. Female verbatim "All somatic characters as in male but slightly larger in size." Type material: holotype male AUZM, Keloğlan Cave, Dodurgalar Town, Acıpayam District, Denizli, 10 July 2011; paratypes 1 male, 1 female, 9 juveniles (AUZM) and 1 male, 1 female (CRBA), same data (tool summary), so 2 males, 2 females, 9 juveniles as filed. Diagnosis has no eye statement; the Discussion speaks of the genus group (tool summary). Conditions state the female sentence. Right.

**Line 5 MATCH.**

### Line 6, Tritomurus veles, eye_type none with ocular-spot variation

Description verbatim: "Primary granulation of integument fine and regular, mostly composed of hexagonal meshes (Figs 6, 25, 32);" | "some areas with fusion of primary granules resulting in quadrangular or irregular meshes (Fig. 15)." then "Eyes absent, ocular spot weak (Fig. 3) or absent." **Quote MATCH**, 9 words, figure reference reproduced. The variation clause is in quote and value. Type material verbatim "Holotype male, 7 paratypes on slides (5 females, 2 with sexual plate not observable)," | "12 paratypes in 96% alcohol, 2 paratypes metalized for SEM, 17 July 2008, leg. M. Lukić;" plus "1 paratype on slide (male), 14 July 2008", "3 paratypes in 96% alcohol" and "4 paratypes in 96% alcohol" from other dates and collectors; locality "Croatia, Biokovo Mt., Sveti Jure: Amfora jama." Abstract verbatim "(absence of eyes, reduced pigmentation, slender claw, pointed tibiotarsal tenent hairs)".

Uncounted: the conditions name only the holotype and the 7 slide paratypes of the first lot; the material also includes a male slide paratype and 21 alcohol or SEM paratypes. Nothing in the eye sentence turns on them, so this is a completeness fix.

**Line 6 MATCH.**

### Line 7, Oncopodura moghanensis, eye_type none

Head paragraph verbatim: "Eyes absent." followed by "PAO well developed and located near base of Ant I, very distinct and large, about 24 µm in diameter," (opening piece). **Quote MATCH**, 2 words. Holotype verbatim "female on slide [MoCa101], dark zone, the end part of the cave, 2nd cave floor", "collected from water pond surface, 28.ix.2022"; paratypes verbatim "4 specimens on slides [MoCa102, MoCa103, MoCa104, MoCa105]", "hand collecting on a stalagmite, 30.iv.2022"; locality verbatim "Iran, Razavi Khorasan province, Mashhad city, Moghan village, Moghan Cave". Paratype sex not stated, as filed. No other eye statement for the species (tool summary); Introduction verbatim "is an eyeless genus of the family".

Uncounted: the conditions could add that the paratypes were hand-collected on a stalagmite (the holotype from a pond surface).

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Graeconiscus gevi, none | MATCH | none | quote MATCH (2), male holotype, paratypes both sexes |
| 2 | Alpioniscus onnisi, none | MATCH | none | quote MATCH (2), male holotype, paratypes both sexes; note sentence-count slip uncounted |
| 3 | Horatia ozimeci, none | MATCH | none | quote MATCH (7); rests on the single destroyed live paratype, stated |
| 4 | Cylindroiulus villumi, none | MATCH | none | quote MATCH (10), whole sentence; both sexes |
| 5 | Typhlonesticus gocmeni, none | MATCH | none | quote MATCH (4), male description; female "as in male" stated |
| 6 | Tritomurus veles, none, ocular spot weak or absent | MATCH | none | quote MATCH (9), variation kept; empty order allowed |
| 7 | Oncopodura moghanensis, none | MATCH | none | quote MATCH (2), female holotype; Entomobryomorpha per classification block |

Errors 0 of 7 audited records (0%), under the 5% bar; none held out, no unfixable errors. By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0 against main and all 185 desk-d2* and audit-3* branches. Verdict: merge all seven lines; the uncounted fixes below may be applied at merge.

Unchecked: no checklist entry for any species; the A. onnisi Remarks and later paratype lots (tool cut); the state of the Horatia non-live paratype lots (tool summary); the spider type-material split and the Oncopodura classification tags rest on tool summaries; figures not viewed.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). All uncounted.

Line 2:
- `note`: "(after the size line, body colour, dorsal surface, gland pores, and two cephalon sentences)" -> "(after the size line, body colour, dorsal surface, gland pores, and the cephalon sentence, which a semicolon divides)"

Line 6:
- `conditions`: "Holotype male (Amfora jama, Biokovo Mt., Sveti Jure, Croatia, 17 July 2008) and 7 paratypes on slides (5 females, 2 with sexual plate not observable);" -> "Holotype male (Amfora jama, Biokovo Mt., Sveti Jure, Croatia, 17 July 2008) and 7 paratypes on slides (5 females, 2 with sexual plate not observable), with further paratypes from the same cave (1 male on slide, 19 in alcohol, 2 metalized for SEM; 2001 and 2008);"

Line 7:
- `conditions`: "4 paratype slides (sex not stated) from the same cave, 30 April 2022;" -> "4 paratype slides (sex not stated) from the same cave, hand-collected on a stalagmite, 30 April 2022;"
