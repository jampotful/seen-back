# audit-378: desk-d289, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d289 files present untracked in the worktree (docs/tracks/progress/desk-d289.md and docs/views/evidence/desk-d289.jsonl, 6 lines; neither committed here, neither edited). Worktree HEAD and origin/main faedc72f (Merge desk d287 (7 records) after audit 376). `python3 -I tools/senses/check.py | grep 'd289\.'`: "docs/views/evidence/desk-d289.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 19, 16, 3, 15, 10, 12, all within 40. The only non-ASCII character in any quote is the en dash in line 1 ("2–5"), which the page prints. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all five DOIs (10.3897/zookeys.1056.71395, zookeys.1149.99651 (rate-limited once, answered on retry), zookeys.1108.85423, bdj.1.e1000, 10.5852/ejt.2026.1034.3169); zookeys.pensoft.net/article/71395/download/xml/ (two passes); zookeys.pensoft.net/article/99651/download/xml/; zookeys.pensoft.net/article/85423/download/xml/ (two passes); bdj.pensoft.net/article_preview.php?id=1000 (two passes); europeanjournaloftaxonomy.eu/index.php/ejt/article/download/3169/14093/ (two passes). All URLs were returned by a WebSearch first. PMC, Plazi, DOAJ, BHL, core.ac.uk, vliz, novataxa and repository hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Line 1 (Likhitrakarn, Golovatch, Jantarit 2021). Crossref: Natdanai Likhitrakarn, Sergei I Golovatch, Sopark Jantarit; title identical; ZooKeys 1056, 173-189, no issue; issued 2021-08-20; CC BY 4.0 vor. Page licence sentence verbatim opening "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Record URL is the article_preview page; the XML of the same article, also returned by the search, was read. Accepted.
- Line 2 (Nguyen, Stoev, Nguyen, Vu 2023). Crossref: Anh D. Nguyen, Pavel Stoev, Lien T. P. Nguyen, Tam T. Vu; title identical; ZooKeys 1149, 181-195; issued 2023-02-23; CC BY 4.0 vor. Page byline in the same order; licence CC BY 4.0 (tool summary). Accepted.
- Lines 3 and 4 (Kuroda, Eguchi, Oguri, Nguyen 2022). Crossref: Mai Kuroda, Katsuyuki Eguchi, Emiko Oguri, Anh D. Nguyen; title identical; ZooKeys 1108, 161-174; issued 2022-06-24; CC BY 4.0 vor. Page licence sentence verbatim opening (CC BY 4.0); byline in the same order. Accepted.
- Line 5 (Golovatch 2013). Crossref: Sergei Golovatch, sole author; title identical including "(Diplopoda, Glomerida, Glomeridae)"; Biodiversity Data Journal 1, e1000; issued 2013-11-06; CC BY 3.0 vor. Page citation verbatim "Golovatch S (2013)" and "Biodiversity Data Journal 1: e1000"; licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 3.0)". Accepted.
- Line 6 (Cifuentes, Da Silva 2026). Crossref: Julio Cifuentes, Luis P. Da Silva; title identical; EJT 1034; issued 2026-01-27; CC BY 4.0 with content-version unspecified. Page verbatim "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)"; header "European Journal of Taxonomy 1034: 271–305"; running header "(2026)"; dates "Received: 12 October 2024 • Accepted: 17 February 2025 • Published: 27 January 2026". Accepted under the rule (Crossref "unspecified" plus page-printed Creative Commons Attribution License). The page's own citation line below the abstract reads "Cifuentes J. & Da Silva L.P. 2025." while header, running head, DOI and publication date read 2026; the record's 2026 follows the printed header and date, so not counted (see Uncounted).

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No checklist reached; all six species are described as new in the cited papers, so the names rest on the original descriptions, as the desk says.

- Glyphiulus longus: "Family Cambalopsidae Cook, 1895"; order Spirostreptida from the title and subject metadata (the classification block's order field reads Diplopoda, the class, as the tool summarises; not used). Met.
- Paracortina kyrang: "Order Callipodida Pocock, 1894", "Family Paracortinidae Wang & Zhang, 1993". Met.
- Hyleoglomeris alba, H. halang, H. translucida: "Family GLOMERIDAE Leach, 1815"; Glomerida from the titles. Met.
- Trichoniscoides castanheirensis: Trichoniscidae; Isopoda as order, Oniscidea (suborder) not used. Met.

Name faults 0.

## Duplicates

git grep on origin/main (faedc72f) across the whole docs/ tree for Glyphiulus, longus, Paracortina, kyrang, Hyleoglomeris, halang, translucida, Trichoniscoides, castanheirensis, the five DOIs and the article ids (71395, 99651, 85423): only unrelated matches ("longus" in Acanthophis praelongus rows of oa-2.jsonl, gbif-names and a Florida view; "halang" inside "Phalangium" in audit-353 and desk-d207; 71395 and 85423 as numbers inside eval and view files). All 671 remote research/desk-* and research/audit-* branches, grepped under docs/views/evidence/, docs/views/audit/ and docs/tracks/progress/desk-* for the same genera, DOIs and article ids: hits only in research/desk-d289 itself (its two files).

Duplicates 0.

## Per-record findings

### Line 1, Glyphiulus longus, eyes_count 2-5 per eye patch

Description verbatim: "Body with 56p+2a+T rings/segments (♂ holotype); ♀ paratypes with 50–57p+2(1)a+T rings." then "Eye patches transversely ovoid, each composed of 2–5 rather flat ocelli in a single longitudinal row (Fig. 1A, C)." **Quote MATCH**, figure reference kept. Table 1 eyes row verbatim "2–5, blackish to brownish". Description opening verbatim "Length of holotype ♂, 23.5 mm; that of paratypes, 22.8–26.5 mm (♀)." Holotype "Holotype ♂: Thailand, Nan Province, Pon, Thung Chang District, Tham Nam Lod"; paratypes "3 ♀: same locality as holotype; CUMZ-CAM171", "1 ♀: same locality as holotype; ZMUM", "1 ♀: same locality as holotype; NHM-PSU", so five female paratypes and no male paratype. No eye statement in Diagnosis or Remarks; no per-sex or per-specimen ocelli count (tool summary). Value "per eye patch" is the quote's "each".

Uncounted: the conditions say the range covers "the type series" without giving its make-up (one male holotype, five female paratypes); since the range spans both sexes undivided, the sexes should be named.

**Line 1 MATCH.**

### Line 2, Paracortina kyrang, eyes_count 19

Description eye sentence verbatim: "Eyes (Fig. 2B, C) black, well delineated, composed of 19 ommatidia in three horizontal rows (9+3+7)." **Quote MATCH**. It stands in the male holotype description; the female paragraph opens "Females. Head unmodified" and has no eye statement (tool summary). Diagnosis verbatim "eyes reduced, composed of 19 or 20 ommatidia in two or three rows." Holotype "1 male (IEBR-Myr 921)", 2.xi.2021; paratypes "1 female, 1 juvenile (IEBR-Myr 932), 1 female (IEBR-Myr 935),"; non-types "1 male, 1 male juvenile, 1 female juvenile (IEBR-Myr 954),". The record states holotype-only and the Diagnosis range. Units "per eye" read "Eyes ... composed of 19 ommatidia in three rows (9+3+7)" as each eye; the note discloses the reading, and one row formula for two eyes would not split; accepted.

**Line 2 MATCH.**

### Line 3, Hyleoglomeris alba, eye_type none

Description first paragraph verbatim, in order: "Body length 4.38 mm, width of the second segment ~ 2.02 mm." "Color entirely white, unpigmented (Figs 6–8)." "Ocelli totally absent." **Quote MATCH**, third sentence, under the species' own Description (attribution shown in "where" and note). Diagnosis verbatim "a completely troglobiotic form with no eyes, an unpigmented body, and a roundly triangular syncoxital lobe." Holotype male IEBR-Myr 919, Ky Rang cave, 2 Nov. 2021; paratypes verbatim "2 females," (IEBR-Myr 917, 12 Oct. 2020) and "1 male," (IEBR-Myr 928, 17 March 2022).

Uncounted: the conditions could name the paratypes (2 females, 1 male); the Diagnosis's species-wide statement already covers both sexes.

**Line 3 MATCH.**

### Line 4, Hyleoglomeris halang, eyes_count "6+1"

Description verbatim opening "Body length 6 mm, width of the second segment ca. 3.5 mm."; run-in label "Head." then "Ocelli 6+1; lenses convex, black contrasting against to a pale blackish background of the head." then "Tömösváry's organs transverse and strongly horseshoe-shaped, ~ 2 × as wide and long." **Quote MATCH** ("against to" as printed). The paper nowhere explains "6+1" (tool summary), and the record files the notation without interpretation, as the brief requires. Diagnosis has no eye statement. Variability verbatim covers syncoxital horns ("Syncoxital horns can be 2.0 × longer than the syncoxital lobe, each horn directed ventromesad.") and trichosteles only. The Description does not say it is based on the holotype alone. Holotype male IEBR-Myr 898H; paratypes verbatim "1 male, 1 female;" (IEBR-Myr 898P, 10 Oct 2020) and "1 male, 1 female;" (IEBR-Myr 926, 15 March 2022).

Uncounted: the conditions could name the paratypes (2 males, 2 females).

**Line 4 MATCH.**

### Line 5, Hyleoglomeris translucida, eyes_count "ca 6+1"

Description verbatim: "Body entirely pallid (Fig. 3)." then "Ocelli ca 6+1, convex, completely translucid, poorly discernible (Fig. 3)." **Quote MATCH**; "ca" kept in value. Diagnosis has no eye statement ("Differs from congeners in a completely unpigmented body."). Materials under H. translucida: holotype "1 male," Cave Coumellos, Archangelos, Rhodes, 1987-05-02, NMNHS; paratypes "2 males, 6 females, 2 juveniles," same locality and date, NMNHS; paratypes "1 male, 1 female," same data, ZMUM. Description opening verbatim "Length of holotype ca 4.1 mm, width (maximum on tergum 2) ca 1.8 mm; length of paratypes ca 4.0-4.3 mm,", so the Description draws on the paratypes too.

**Error (sample composition, fixable):** the conditions end "the description rests on this single male". The page lists twelve paratypes (3 males, 7 females, 2 juveniles) and the Description gives paratype measurements. The statement misreports the sample on which the "ca 6+1" stands. Replacement below.

**Line 5 ERROR (fixable).**

### Line 6, Trichoniscoides castanheirensis, eyes_count 1

Description verbatim: "Coloration. Orange, with marked muscle insertions and one large black ocellus (Fig. 21A)." **Quote MATCH** (run-in label "Coloration." omitted, as the record's "where" names it; same practice as line 4's "Head."). The paragraph follows Measurements, which give both sexes; no sex stated (tool summary). Fig. 21 caption verbatim "Fig. 21. Trichoniscoides castanheirensis sp. nov. A. ♀ (LPS792b), habitus." Diagnosis verbatim "Ocular apparatus with large black ocellus." (first pass; a second pass gave the Diagnosis colour sentence as "Coloration orange." Both may be present; not resolved). Holotype ♂ MNCN 20.04/21006 (ex. LPS792a), Castanheira, 12 Nov. 2023; paratypes verbatim "1 ♀; same data as for holotype; MNCN 20.04/21007 (ex. LPS792b)", "1 ♀; same data as for holotype; LPS792c", "1 ♂, same data as for holotype; JC1048 (ex. LPS794)." No other ocellus statement or variation (tool summary). Value 1 is the quote's "one".

**Line 6 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Glyphiulus longus, 2-5 per eye patch | MATCH | none | quote MATCH (19); type series 1 male + 5 females, uncounted fix |
| 2 | Paracortina kyrang, 19 | MATCH | none | quote MATCH (16); holotype-only and Diagnosis 19 or 20 stated |
| 3 | Hyleoglomeris alba, none | MATCH | none | quote MATCH (3); Diagnosis species-wide |
| 4 | Hyleoglomeris halang, 6+1 | MATCH | none | quote MATCH (15); notation not interpreted, as the paper gives none |
| 5 | Hyleoglomeris translucida, ca 6+1 | ERROR (fixable) | conditions | "rests on this single male" false: 12 paratypes listed and measured |
| 6 | Trichoniscoides castanheirensis, 1 | MATCH | none | quote MATCH (12); Crossref unspecified + page CC BY 4.0 |

Errors 1 of 6 audited records (16.7%). By kind: quotes 0; value exceeding quote 0; sample composition 1 (line 5, fixable); bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. The audit covered the whole unit and the only error is fixable, so no record is unfixable and none is held out. Verdict: apply the line 5 replacement, then merge all six lines (with the replacement applied the unit carries 0 errors, under the 5% bar).

Unchecked: no checklist entry for any species; figures not viewed; the Paracortina licence sentence, the halang "6+1" absence-of-explanation, the T. castanheirensis sex reading and Diagnosis wording rest on tool summaries.

## Uncounted

- Line 6 page citation line prints "2025" against header, running head and publication date 2026; the record follows the header. Owner may note it.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 5 (counted):
- `conditions`: "the description rests on this single male" -> "paratypes 2 males, 6 females, 2 juveniles (NMNHS) and 1 male, 1 female (ZMUM), same locality and date; the Description gives holotype and paratype lengths and does not say which specimens the ocelli sentence rests on"

Line 1 (uncounted):
- `conditions`: "the range 2-5 covers the type series (holotype and paratypes together)" -> "the range 2-5 covers the type series (holotype male and five female paratypes together)"

Line 3 (uncounted):
- `conditions`: "no variation in paratypes noted" -> "paratypes 2 females and 1 male from the same cave; no variation in paratypes noted"

Line 4 (uncounted):
- `conditions`: "no paratype ocelli variation noted" -> "paratypes 2 males and 2 females from the same cave; no paratype ocelli variation noted"
