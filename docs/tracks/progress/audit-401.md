# audit-401: desk-d306, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d306 files present untracked in the worktree (docs/tracks/progress/desk-d306.md and docs/views/evidence/desk-d306.jsonl, 12 lines; neither committed here, neither edited). This audit takes file lines 1 to 6 (1-based); lines 7 to 12 (Dollocaris, Bathylychnops, Pinelema, Pholis, including the 44-word Bathylychnops sentence) go to another auditor. HEAD equals origin/main (23d6aba8). `python3 -I tools/senses/check.py | grep d306`: "docs/views/evidence/desk-d306.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`): 25, 25, 26, 9, 31, 11, all within 40; no quote in this range carries an ellipsis or a cut.

Sources opened (WebFetch, every URL from a WebSearch result): europeanjournaloftaxonomy.eu/index.php/ejt/article/download/1735/6515 (two passes), zookeys.pensoft.net/article_preview.php?id=3887 (two passes), zookeys.pensoft.net/article_preview.php?id=3692 (two passes), zookeys.pensoft.net/article_preview.php?id=24477 (two passes), wsc.nmbe.ch/species/5929/Tarsonops_irataylori, wsc.nmbe.ch/refincluded/16427. Crossref single-DOI lookups api.crossref.org/v1/works/ for all four DOIs, each answered on the first call. en.wikipedia.org/wiki/Caponina asked for permission that was not answered; not retried. Plazi, BHL, PMC, bionames, DOAJ, repository copies (uniatlantico, Frankfurt, digilab.uwr) not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

Stitching: the Caponina sentences (lines 1 to 3) and the Panorpodes sentence (line 5) each came back as two consecutive pieces, and in each case the first piece ends at a comma and the second opens the rest of the same printed sentence: "Six eyes, AME the largest, dark, separated by about half their diameter, ALE pale translucent, smaller than AME," / "PLE pale translucent and smaller than ALE." (alejandroi; bochalema and huila as filed); "The head is slightly flattened, 450 ± 15 µm in length and 315 ± 17 µm in width (n = 10) (Fig. 2A–C)," / "lacking compound eyes, ocelli, or stemmata (Fig. 2C)." Each Caponina sentence follows "Carapace flat with soft cuticle." and the Panorpodes sentence opens the Head capsule subsection; each ends at a full stop. Whole sentences, one section each, as printed.

## Desk d288's drop of the Caponina sentences

docs/tracks/progress/desk-d288.md (on main, line 14) dropped Caponina alejandroi, bochalema and huila because "the eye sentence is longer than the tool's 125 characters and was only reachable by asking the tool for pieces, which the brief forbids; left as a retrieval gap". That was a retrieval rule, not a finding about the paper. The current rules (rules.md TOOLS: WebFetch returns ~125 chars per sentence) and desk-audit.md ("There is no 125-character evidence limit"; a tool cap calls for legal retrieval, not a negative finding) no longer forbid reading a sentence in consecutive pieces, and audit-400 accepted sentences read that way. The source is the publisher's own free full text (EJT, CC BY 4.0). The reason no longer applies; the three records are judged on their merits.

## Bibliographic and licence

- Lines 1 to 3 (Sánchez-Ruiz, Martínez, Bonaldo 2022). Page byline "Alexander SÁNCHEZ-RUIZ 1,*, L eonel MARTÍNEZ 2 & Alexandre B. BONALDO 3" (tool spacing); Crossref same order. Title identical to the page (printed over two lines) and Crossref. Page prints "European Journal of Taxonomy 813: 87–102 (2022)"; Crossref volume 813, no issue or pages, issued 2022-04-14. Licence: page "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)."; Crossref CC BY 4.0, content-version unspecified. Accepted.
- Line 4 (Bond, Taylor 2013). Page byline "Jason E. Bond 1,†, Steven J. Taylor 2,‡"; Crossref Jason Bond, Steven Taylor (no middle initials, same order). Title identical. Page "ZooKeys 289: 57–64"; Crossref pages 57-64, no issue, issued 2013-04-12. Licence: page "Creative Commons Attribution License 3.0 (CC-BY)"; Crossref CC BY 3.0 vor. Accepted.
- Line 5 (Jiang, Yue, Hua 2014). Page byline "Lu Jiang 1, Chao Yue 1,2, Baozhen Hua 1"; Crossref lists Hua, Jiang, Yue; the record follows the page, right. Title identical. "ZooKeys 398: 69–82"; issued 2014-04-04. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 6 (Kadej 2018). Byline "Marcin Kadej"; title identical (page prints it over two pieces with the comma after "importance"); "ZooKeys 758: 115-135."; Crossref issued 2018-05-15; page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Lines 1 to 3: the three Caponina species are described as new in this paper; the World Spider Catalog's "Included taxa" page for the reference (wsc.nmbe.ch/refincluded/16427) lists all three under these names in Caponiidae, with no synonymy shown. The Taxonomy section prints the headings "Class Arachnida Cuvier, 1812", "Order Araneae Clerck, 1757", "Family Caponiidae Simon, 1890", "Genus Caponina Simon, 1892". **Fault, all three lines:** `class` is blank although the page prints Class Arachnida, and the note says "Higher taxa from the title (Araneae, Caponiidae); no class or order heading read", which is false. Order and family values are right.
- Line 4: World Spider Catalog: "Tarsonops irataylori Bond & Taylor, 2013", "ACCEPTED", Caponiidae (tool summary of the status line). The page prints no Class, Order or Family heading (the species heading only); class blank is right. Uncounted part of the line 4 fix: the note says "Order and family from the Abstract"; the Abstract gives the family only ("A new species of Caponiidae"), and the order comes from the title "(Araneae, Caponiidae)".
- Line 5: Panorpodes kuandianensis, the name used throughout the paper; class, order, family from the title "(Insecta, Mecoptera, Panorpodidae)"; no higher-taxon headings in this morphology paper. Right.
- Line 6: the page prints "Subfamily Megatominae Leach, 1815", "Tribe Megatomini Ganglbauer, 1904", "Genus Ctesias Stephens, 1830" and no class, order or family heading; order and family from the title "(Coleoptera, Dermestidae)"; class blank is right. Ctesias serra (Fabricius, 1792) is the name in the title and the paper; no sign of synonymy in the results seen.

## Repeats

`git grep -n -i -F` on origin/main (23d6aba8) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks, gaps, eval) for Caponina, Tarsonops, Panorpodes, Ctesias and the DOI strings ejt.2022.813, 813.1735, zookeys.289.4493, zookeys.398.6675, zookeys.758.24477 (and the bare 24477 and 6675, which hit only unrelated numbers): one relevant hit, docs/tracks/progress/desk-d288.md line 14 (the d288 drop, no record filed). Every origin/research/desk-d* branch other than d306 grepped for the same patterns in the docs/ files that differ from origin/main: hit only in desk-d288's progress note. Repeat faults 0.

## Per line

### Line 1, Caponina alejandroi, six eyes, AME largest and dark

Description (male): "Six eyes, AME the largest, dark, separated by about half their diameter, ALE pale translucent, smaller than AME," / "PLE pale translucent and smaller than ALE." **Quote MATCH**, 25 words. Holotype "♂; Boyacá Department, Santuario de Flora y Fauna Iguaque, El Caimo, Sector Chaina;" / "5°25′ N, 73°27′ W; alt. 2730 m; 24 Sep. 2003; A. Roberto leg.; IAvH-I 3747." Paratypes: 1 ♂ same data (IAvH-I 3114); 1 ♀ same data, 12 Jul. 2001 (IAvH-I 3755); 1 ♂ Villa de Leyva, Colegio Antonio Nariño, 2200 m (IAvH-I 3750); 1 ♀ same (IAvH-I 3749); 1 ♀ Vereda Sopotá, Finca El Peladero, 2185 m (IAvH-I 3115): 2 males and 3 females, as the conditions say. Female: "Carapace and eyes as in male." Diagnosis has no eye wording. Abstract: "C. alejandroi sp. nov. (male and female)". Discussion "Representatives of Caponina have between 4 and 6 eyes (with aberrant individuals with 3 or 5 eyes, respectively," and the emended diagnosis's eight-eyed, two-eyed and eyeless genera are in the conditions. Value says no more than the quote. Uncounted: the identification key's couplet reads "Six eyes (rarely fi ve)" against "Four eyes (rarely three)"; the conditions carry the same variation through the Discussion sentence, so the omission is not counted; an optional addition is given below.

Fault: class blank and false note (see Names). One record error, fixable.

**Line 1 FIXABLE.**

### Line 2, Caponina bochalema, six eyes, AME largest and dark

Description: "Six eyes, AME largest, dark, separated by about half their diameter, ALE pale translucent and smaller than AME," / "PLE pale translucent and smaller than ALE." **Quote MATCH** (no "the" before "largest", as printed), 25 words. Holotype "♂; Santander Department, Municipality of Bochalema, Parque Nacional Natural Tamá, Finca Campesina;" / "7°31′53.14′′ N, 72°19′23.94′′ W; alt. 1450–1600 m; 30 Apr. 2004; E. González leg.; IAvH-I 3757." Holotype only (tool summary); Female "Unknown."; Abstract "C. bochalema sp. nov. (male)". Conditions right.

Fault: class blank and false note. One record error, fixable.

**Line 2 FIXABLE.**

### Line 3, Caponina huila, six eyes, AME largest and dark

Description: "Six eyes, AME the largest, dark, separated by about half their diameter, ALE pale translucent and smaller than AME," / "PLE pale translucent and smaller than ALE." **Quote MATCH**, 26 words. Holotype "♂; Huila Department, Garzón, Vereda El Espinal, Reserva privada “Taky-Huaylla”;" / "2°17′43′′ N, 75°35′37′′ W; alt.1000 m; 16–19 Sep. 2002; M. Ospina leg.; IAvH-I 3761." Holotype only; Female "Unknown." Conditions right (the record's straight quotes around Taky-Huaylla in the conditions field are not a quote field).

Fault: class blank and false note. One record error, fixable.

**Line 3 FIXABLE.**

### Line 4, Tarsonops irataylori, two eyes

Description: "Two eyes, eyes separated by distance equal to radius." between "Clypeus height 1.5× eye diameter." and "Sternum lightly setose, widest between coxae II, III (Fig. 4)." **Quote MATCH**, 9 words. Holotype "Holotype male from BELIZE: Toledo District: Cave near Pueblo Creek Cave: 37 km WNW of Punta Gorda", 16 April 2011 (tool summary of the date); "Specimen collected live, preserved in 70% ethanol."; Introduction "Unfortunately, this newly discovered species is known from only a single specimen." Table 1 "Number of eyes": Cubanops 2, Nops 2, Nopsides 4, Nyetnops 2, Orthonops 2, "Tarsonops (all other species)" 2, T. irataylori 2; key couplet 1 "4 eyes" (Nopsides) / 1′ "2 eyes". Conditions right on these.

Fault: the Discussion is not in the conditions, which say instead that "the paper carry no Remarks on eyes": "Although this species was taken from just inside a cave, it does not exhibit any obvious troglomorphies," / "and may be accidental in this habitat." For a two-eyed spider from a cave this is the paper's own statement that the eyes are not cave-reduced and that the cave record may be accidental; a reader of the filed record ("from a Belize cave") could take the opposite. One record error, fixable (the note's Abstract attribution is fixed in the same pass, uncounted).

**Line 4 FIXABLE.**

### Line 5, Panorpodes kuandianensis, first-instar larva without compound eyes, ocelli or stemmata

Head capsule: sentence as quoted (see Stitching). **Quote MATCH**, 31 words. "The first instar larva is white and 2.9 ± 0.31 mm in length (n = 10) (Fig. 1)."; "The head is hypognathous and eyeless, with mandibulate mouthparts directed downward"; collection "Huaboshan (41°06'N, 125°02'E, elev. 650–1100 m)," / "Kuandian County, Liaoning Province of northeastern China from late June to July in 2011 and 2012."; "The adults were reared in pairs in plastic jars covered with a piece of gauze."; preparation of "First instar larvae" only; Discussion "resulting in a failure to obtain the following instar larvae and pupae." (later instars not described, as the conditions say). Abstract "The larva of Panorpodes is remarkable for the absence of compound eyes on the head"; Discussion "The larvae of Panorpodes, however, are completely eyeless, congruent with the larvae of Brachypanorpa (Byers 1997)."; "seven ommatidia (or "stemmata") in Bittacidae", "A dorsal ocellus is also present on the larval head of Bittacidae", "approximately 20–40 ommatidia in Panorpidae", "three “stemmata” in Boreus". Conditions right; value says no more than the quote; species-level sentence (the species' own Head capsule account).

**Line 5 MATCH.**

### Line 6, Ctesias serra, six stemmata on the head (four plus two below)

Description: "Larva, last instar. Length 5.0–7.0 mm."; head: "Six stemmata present on the head (four + two other below)." between "Head protracted and hypognathous." and "Frons triangular, without frontal, median tubercle (Fig. 8)." **Quote MATCH**, 11 words. The paper has no other sentence with "stemma" or "ocelli" (asked across the whole article); no larval Diagnosis or key.

Per-side or total: the sentence says "on the head", and Table 2.3's "# of stemmata" column gives Ctesias "6" with no per-side wording either (other cells: Dermestes "6" with footnote 5, "According to Zhantiev (2000) Dermestes depressus lacks stemmata."; Thylodrias 3; Trinodes 6; Attagenus 4–5; Anthrenus 6; Globicornis 6; Reesa 4; Trogoderma 5; the superscript markers are inferred from flattened text, tool summary). Nothing on the page settles per side against in all. The record files the trait as eye_type, not as a count, its value repeats "on the head" and adds no total, and the conditions state the ambiguity; that is within "value says no more than the quote". Accepted as eye_type; it must not be converted to eyes_count or a stemmata total.

Faults: (a) material: Material examined lists "(1 exuvia, 1 pupa) Warszawa, Saska Kępa ... 10.V.1955" and "(1 exuvia, 4 larvae) Polonia, Dojlidy ad. Białystok 19.III.1959", so two exuviae and one pupa, and a Warszawa locality the conditions omit; the conditions say "plus an exuvia and a pupa". Larvae 2 + 2 + 1 + 7 + 4 + 1 = 17, right. (b) The conditions say the Ctesias row of the comparison table "was not readable"; the page prints 6 for Ctesias in Table 2.3, which bears directly on the per-side question the record raises. One record error, fixable.

**Line 6 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Caponina alejandroi, six eyes | FIXABLE | class, note | page prints Class Arachnida; note says no class or order heading read |
| 2 | Caponina bochalema, six eyes | FIXABLE | class, note | same |
| 3 | Caponina huila, six eyes | FIXABLE | class, note | same |
| 4 | Tarsonops irataylori, two eyes | FIXABLE | conditions (note uncounted) | Discussion "does not exhibit any obvious troglomorphies ... may be accidental" omitted |
| 5 | Panorpodes kuandianensis, larva eyeless | MATCH | | quote whole, first instar only, Discussion contrasts cited |
| 6 | Ctesias serra, six stemmata on the head | FIXABLE | conditions | two exuviae not one, Warszawa omitted; Table 2.3 prints 6 for Ctesias |

Errors: 5 of 6 records (83.3%); 5 fixable (lines 1, 2, 3, 4, 6), 0 held out, 0 unfixable; no line to drop. Questions from the unit: the Ctesias "on the head" sentence is not a total and is acceptable only as filed (eye_type, wording repeated, ambiguity in conditions); the d288 reason for dropping the Caponina sentences no longer applies. The rate is above 5%, so lines 1 to 6 merge by the drop-the-errors route: line 5 as filed, lines 1, 2, 3, 4 and 6 with the replacements below (or dropped if the replacements are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Lines 1, 2 and 3 (each line):
- `class`: `"class": ""` -> `"class": "Arachnida"`
- `note`: "Higher taxa from the title (Araneae, Caponiidae); no class or order heading read." -> "Higher taxa as printed in the Taxonomy headings: Class Arachnida Cuvier, 1812; Order Araneae Clerck, 1757; Family Caponiidae Simon, 1890."

Optional, uncounted (lines 1, 2 and 3): append to `conditions` "The identification key separates 'Six eyes (rarely five)' from 'Four eyes (rarely three)'." (the page prints "fi ve" with a ligature break).

Line 4:
- `conditions`: "The Diagnosis (ventral keel and membrane extension on the anterior metatarsi) and the paper carry no Remarks on eyes." -> "The Diagnosis (ventral keel and membrane extension on the anterior metatarsi) has no eye wording, and the paper has no Remarks section; the Discussion says that although the species was taken from just inside a cave, 'it does not exhibit any obvious troglomorphies, and may be accidental in this habitat.'"
- `note` (uncounted): "Order and family from the Abstract ('A new species of Caponiidae'); no order heading read." -> "Family from the Abstract ('A new species of Caponiidae') and the title; order from the title (Araneae, Caponiidae); the page prints no class, order or family heading."

Line 6:
- `conditions`: "plus an exuvia and a pupa" -> "plus two exuviae and one pupa (one exuvia and the pupa from Warszawa, Saska Kępa, 1955; one exuvia from Dojlidy, 1959)"
- `conditions`: "the Ctesias stemmata row was not readable and Dermestes shows 6." -> "its '# of stemmata' column (Table 2.3) gives 6 for Ctesias, as for Dermestes (footnote: D. depressus lacks stemmata), Trinodes, Anthrenus and Globicornis, against 3 in Thylodrias, 4-5 in Attagenus, 4 in Reesa and 5 in Trogoderma, and does not say per side or in all either."
