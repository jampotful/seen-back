# audit-406: desk-d309, evidence file lines 8 to 14

Audited 1 November 2026 from the desk-d309 files present untracked in the worktree (docs/tracks/progress/desk-d309.md and docs/views/evidence/desk-d309.jsonl, 20 lines; identical to origin/research/desk-d309; neither committed here, neither edited). This audit judges file lines 8 to 14 only (two other auditors take 1-7 and 15-20). Note that the unit's progress file numbers its records differently from the file: the Tabanidae trio it calls 10-12 are file lines 8-10, and Barryichthys, Oculogryphus and the polyclad pair are file lines 11-14. HEAD equals origin/main (d87091c8f). `python3 -I tools/senses/check.py | grep d309`: "docs/views/evidence/desk-d309.jsonl: 20 records, 0 problems". Quote lengths (`len(q.split())`), lines 8-14: 16, 13, 9, 19, 12, 11, 32, all within 40.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=21144 (two passes), id=34521 (four passes), id=21502 (one pass), id=3776 (two passes); en.wikipedia.org/wiki/Prostheceraeus_vittatus, obis.org/taxon/142224 and sealifebase.se/summary/Prostheceraeus-vittatus for the name only. Crossref single-DOI lookups api.crossref.org/v1/works/ for all four DOIs (zookeys.404.7122 rate-limited on the first call, read on the one retry). PMC, GBIF, Plazi, Zenodo, core.ac.uk, the University of Pretoria and Glasgow repositories, library catalogue hosts (libmast.utm.my, openaccess.library.uitm.edu.my, ebusca.uv.mx, searchworks.jioinstitute.edu.in), zin.ru and paperity were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Answers to the unit's questions (for lines 8-14)

1. Eye shape, size and colour as eye_type: main already holds such rows under eye_type (desk-d307 Electrotettix attenboroughi "compound eyes large, globose, projecting somewhat dorsally"; Burmella clypeata "eyes brown, elongated, relatively large, widely separated medially"; desk-d298 Toxicocalamus longhagen "small eye, round pupil"; desk-d303 Palaumysis jetama "large eye, cornea globular"). Lines 8-11 phrase their values in the same way; accepted.
2. Telegraphic sentences: lines 10, 11 and 14 quote whole printed sentences with no finite verb ("Eyes separated by dark brown frons with black hair."; "Eye large, positioned on dorsolateral surface of head; ...", "Tentacular eyes on the dorsal margin of tentacles ..."). Each is a whole printed sentence from a Description, ending at its own full stop, with no cut; under the audit-395 precedent these pass. None of my lines is a bare heading or a fragment cut from a longer sentence.
3. Not raised by my lines (Cottus is line 7).

## Bibliographic and licence

- Lines 8-10 (Mugasa, Villinger, Gitau, Ndungu, Ciosi, Masiga 2018). Byline "Claire M. Mugasa, Jandouwe Villinger, Joseph Gitau, Nelly Ndungu, Marc Ciosi, Daniel Masiga"; Crossref same order. Title identical on page and Crossref. Citation line "ZooKeys 769: 117-144"; Crossref 769, 117-144, issued 2018-06-26, no issue. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 11 (Conway, Moore, Summers 2019). Byline "Kevin W. Conway, Glenn I. Moore, Adam P. Summers"; Crossref same. Title identical. ZooKeys 864: 35-65, issued 2019-07-15. Page CC BY 4.0; Crossref CC BY 4.0 vor. Accepted.
- Line 12 (Yiu, Jeng 2018). Byline "Vor Yiu, Ming-Luen Jeng"; Crossref same. Title identical (citation line returned in pieces, joined at spaces). ZooKeys 739: 65-78, issued 2018-02-22. Page CC BY 4.0; Crossref CC BY 4.0 vor. Accepted.
- Lines 13-14 (Noreña, Marquina, Perez, Almon 2014). Byline and Crossref same order. Title identical. ZooKeys 404: 1-22, issued 2014-04-22; Pensoft article id 3776 against DOI suffix 7122, as the note says. Page CC BY 4.0; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Tabanidae (lines 8-10): the page has no classification block and no Order or Family heading; the Introduction prints "Biting flies of the family Tabanidae (Order Diptera)" and the genus headings ("Genus Haematopota", "Genus Chrysops", "Genus Tabanus"). Order and family filled from that sentence, class blank: right. Names: a search turned up only the Tabanidae catalogue site (tabanidae.myspecies.info) and no synonymy for the three; not contradicted.
- Barryichthys hutchinsi (line 11): no classification block; "Gobiesociformes" only inside a reference title; title "(Teleostei, Gobiesocidae)". Family filled, order blank (a reference title is not the page placing this species), class blank (Teleostei is not a class): right. Name described here; the Australian Faunal Directory lists "Species Barryichthys hutchinsi Conway, Moore & Summers, 2019" (search-result title, not opened).
- Oculogryphus chenghoiyanae (line 12): no classification block or rank headings; title "(Coleoptera, Lampyridae)"; subfamily Ototretinae in the Introduction only. Order and family from the title, class blank: right.
- Prostheceraeus vittatus, Euryleptodes galikias (lines 13-14): page prints "Suborder Cotylea" and "Family Euryleptidae" headings, no Order heading; Polycladida in the title. Order from the title, family from the heading, class blank: right. Euryleptodes galikias described here. Prostheceraeus vittatus: Wikipedia gives it as accepted citing WoRMS (Tyler 2018), with Eurylepta vittata as a synonym; SeaLifeBase gives Prostheceraeus vittatus (Montagu, 1815) in Euryleptidae. Not counted, for the owner: a GBIF search-result title reads "Eurylepta vittata (Montagu, 1815)" (GBIF not opened, refused per rules); the GBIF backbone may treat the species under Eurylepta. The current WoRMS status could not be read.

## Repeats

`git grep -il` on origin/main (d87091c8f) over the whole docs/ tree for "Haematopota fenestralis", fenestralis, "Chrysops brucei", "Tabanus gratus", zookeys.769.21144, Barryichthys, zookeys.864.34521, Oculogryphus, zookeys.739.21502, "Prostheceraeus vittatus", Euryleptodes, galikias, zookeys.404.7122. Hits: "fenestralis" only as Lobelia fenestralis (oa-7, germination rows; a plant, unrelated) and in gaps/gbif-names.tsv; "Prostheceraeus vittatus" only in docs/views/gaps/try-species.json (a wanted-species list, no trait value). No evidence, audit, corrected, ALL, sheets or searched hit for any species or DOI. Every origin/research/desk-d*, audit- and sweep branch not merged into main, grepped over its docs/ files that differ from main: hits only in desk-d309 itself. No repeats.

## Per line

### Line 8, Haematopota fenestralis, female eyes banded and separated by a wide frons

Results, Morphological description, Haematopota fenestralis, Head: "Eyes black with colourful bands and separated by wide, more or less square greyish black frons." after "Head black, broader than long (Suppl. material 2: Figure S11A)." and before "Frons with short black hair and few white hairs." **Quote MATCH**, whole sentence, 16 words. Fig. 4 caption "eyes have bright coloured bands" agrees. Males: "Male flies were collected in negligible numbers and where thus not included in the study." Kenyan flies "NG2G traps baited with less than 3 weeks old cow urine and acetone", stored in 95% ethanol, then "Flies were pinned and placed in entomological boxes for morphological identification"; method "pinned" right. No genus-level eye sentence; species-level only.

Fault: **specimen count and sites misstated.** Table 2 lists Haematopota fenestralis at three sites, all Kenya: Buffalo Ridge (4 submitted, 2 sequenced), Marere Circuit (3, 3), Zunguluka (4, 0). The totals 11 and 5 are right, but the conditions say "from four sites". One record error, fixable.

Not counted: "(dichoptic)" in the value glosses "separated by ... frons" with its technical term; the note says the paper does not use it. It adds no fact, so it is left; the owner may strip it.

**Line 8 FIXABLE.**

### Line 9, Chrysops brucei, female eyes separated by a dark brown frons

Head: "Head as wide as thorax with black eyes separated by dark brown frons." **Quote MATCH**, 13 words; value uses only the eye part and says no more. Uganda: "F-traps (Kuzoe and Schofield 2005) baited with 1,8-octenol", "for 3 to 5 days depending on the fly density", stored in 70% ethanol. Table 2: Mabamba (1 submitted, 0 sequenced), Jahazi (1, 1); "2 flies submitted and 1 sequenced (Jahazi)" right. No count examined morphologically (page gives only about 995 female tabanids from Uganda overall). Ocelli sentence in conditions consistent with the paragraph (tool summary). Conditions right.

**Line 9 MATCH.**

### Line 10, Tabanus gratus, female eyes separated by a dark brown frons

Head: "Eyes black with green and black bands when fresh that disappear after the sample dries up." then "Eyes separated by dark brown frons with black hair." **Quote MATCH**, whole printed sentence (telegraphic; passes under audit-395), 9 words. Table 2: Mukinyo, Kenya (1, 1), Sangaiwe, Tanzania (5, 2), Poacher's Hide, Tanzania (1, 1): 7 and 4 right. Traps NG2G with cow urine and acetone, right. Preceding band sentence carried in conditions. Conditions right.

**Line 10 MATCH.**

### Line 11, Barryichthys hutchinsi, eye large and dorsolateral

Description: "Eye large, positioned on dorsolateral surface of head; ventral margin of orbit not visible in ventral view (Fig. 5A)." between "Widest point of head midway between orbit and opercular opening; wider than widest point of body." and "Snout of moderate length, triangular, narrowest anteriorly." **Quote MATCH**, whole sentence with figure reference, 19 words. Holotype WAM P.28981-004, male, 15.4 mm SL, Cottesloe Reef platform, 16 January 1986; paratypes WAM P.28981-003 (4, 16.0-16.9 mm SL), WAM P.34510-001 (5, 2 C&S, 14.2-16.3 mm SL, 29 January 1985), WAM P.34940-001 (1 female, 18.7 mm SL, Trigg Reef platform, 13 January 1986): 10 paratypes in three lots, as filed. Table 1 n = 5, 21.0-24.0 % HL, holotype 24, mean 22.1, as filed; B. algicola 21.4-24.9, as filed.

Faults: (a) **Non-type material omitted, and the eye field limits the statement to the type series.** The species account lists "Other material" from South Australia: "AMS I.20171-012, 6 (2 C&S), 12.4–13.1 mm SL (immature); South Australia; Kangraoo Island, Vivonne Bay" and "AMS I.49000-001, 2 (1 CT ... 14.0–14.6 mm SL; Victor Harbor, Bluff Jetty" (25 March 2015). Remarks: "These specimens have been excluded from the type series" and data from them "has contributed to the description above" (second clause tool summary). The Distribution gives two Western Australian and two South Australian sites. The record's eye field "adults of the type series" and conditions "Species description based on the male holotype ... and 10 paratypes" are therefore too narrow, and "adults" is not printed (one referred lot is labelled immature). (b) **Contrasting wording elsewhere not carried.** Diagnosis: "ventral margin of orbit obscured by cheek in ventral view"; Discussion: "...but not in B. hutchinsi," / "in which only the lateralmost part of the eye is visible in ventral view" / "with the ventral eye margin obscured by the cheek (Fig. 5A)." The conditions give the Discussion only as "the most obvious external difference". Also, CT scans: the holotype and one AMS I.49000-001 specimen (tool summary), consistent with the method field. One record error, fixable.

**Line 11 FIXABLE.**

### Line 12, Oculogryphus chenghoiyanae, female compound eyes with 13 ommatidia

Description, "Female (Figs 5–8).": "Compound eyes small, slightly produced laterally, facing forward rather, with 13 ommatidia." after "Epicranium more pigmented laterally than dorsally, epicranial and frontal sutures obscure." **Quote MATCH**, 12 words, printed word order kept. Per eye or both not stated; the value says so and claims neither. Holotype male 5.V.2017; paratypes 1 male 8.V.2017, 1 female same data as holotype, 1 female 12.V.2017, all Tei Tong Tsai, Lantau Island: two females, as filed; the text does not say which females the description rests on (female measurements from ethanol-fixed specimens, tool summary). Remarks: "Their external morphology highly resembles Stenocladius females (c.f. Ohba et al 1997)." / "Some minor differences like the orientation of eyes and number of ommatidia are observed." Male: Diagnosis "compound eyes strongly emarginate posteriorly and approximate ventrally"; UV section "Male specimens also produced a blue-green fluorescence, but only from their enlarged compound eyes." The only ommatidia mentions in the paper are these two; no genus-level eye sentence. Conditions right. ommatidia_count key on main, note says so.

**Line 12 MATCH.**

### Line 13, Prostheceraeus vittatus, cerebral eyes in two anastomosing groups

Description: "Cerebral eyes form two compact elongated, frontally anastomosing groups (Figure 4A)." and next "Tentacular eyes scarce and mainly at base of tentacles." **Quote MATCH**, 11 words, printed punctuation (no comma after "compact") kept. Material 15/03/2010 and 24/02/2012, one sectioned, MNCN 4.01/648–662 (15 slides); A Tiñosa 24 m, Petón Bajo 16 m: as filed. No genus or family eye statement for Prostheceraeus (the only other Euryleptidae eye remark is P. roseus, a different species).

Fault: **conditions say sizes are not given, but the page prints them, and the maturity remark is missing.** Description: "Elongated worms 10–30 mm long and 7–15 mm wide." Remarks: "Lang (1884) mentions in the original description that specimens less than 1.5–2 cm in length were immature." / " However, sometimes our specimens from the Atlantic coast were mature, despite their small size (c. 1.5 cm in length)." The eye field's "adults" is not printed. Polyclads are hermaphrodite, so "Sexes ... not given" adds nothing. One record error, fixable.

**Line 13 FIXABLE.**

### Line 14, Euryleptodes galikias, tentacular, marginal and cerebral eye arrangement

Description, returned in two consecutive pieces joined at a space: "Tentacular eyes on the dorsal margin of tentacles (Figure 3D), marginal eyes in two small clusters on anterior margin" / " (Figure 3E) and cerebral eyes in two elongated anteriorly anastomosing clusters (Figure 3E)." Joined text equals the record's quote character for character. **Quote MATCH**, whole sentence, 32 words. Holotype only: MNCN 4.01/502–572 (71 slides), Ribeira, Ria de Arosa, 5 m, 09/12/2012; no other material; living specimen "25 mm long and 14.4 mm wide" (not needed for the eye value). Discussion contrast with E. insularis "the tentacular eyes over the tentacles, and the frontal marginal eyes" paraphrased in the conditions and marked as paraphrase; acceptable. No diagnosis section, no genus eye statement. Value restates the quote; commas added in the value ("two elongated, anteriorly") change nothing. Conditions right.

**Line 14 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 8 | Haematopota fenestralis, eyes separated, banded | FIXABLE | conditions | Table 2 has three sites, not four |
| 9 | Chrysops brucei, eyes separated | MATCH | | traps, counts, males excluded all right |
| 10 | Tabanus gratus, eyes separated | MATCH | | whole telegraphic sentence; counts right |
| 11 | Barryichthys hutchinsi, eye large, dorsolateral | FIXABLE | eye, conditions | 8 referred South Australian specimens (6 immature) omitted; "adults" not printed; Diagnosis and Discussion wording on the orbit margin not carried |
| 12 | Oculogryphus chenghoiyanae, 13 ommatidia | MATCH | | per eye or both left open as printed; two female paratypes |
| 13 | Prostheceraeus vittatus, cerebral eye groups | FIXABLE | eye, conditions | sizes said absent but printed (10–30 x 7–15 mm); maturity remark missing; "adults" not printed |
| 14 | Euryleptodes galikias, eye arrangement | MATCH | | stitched text equals page; holotype only |

Errors: 3 of 7 records (42.9%); 3 fixable (lines 8, 11, 13), 0 held out, 0 unfixable; no line to drop. Bibliographic, licence, repeat and name faults 0. The rate is above 5%, so these lines merge only by the drop-the-errors route: lines 9, 10, 12, 14 as filed, lines 8, 11 and 13 with the replacements below (or dropped if they are not applied). Verdict for lines 8-14: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 8:
- `conditions`: "Table 2 lists 11 flies submitted for sequencing from four sites and 5 sequenced" -> "Table 2 lists 11 flies submitted for sequencing from three Kenyan sites (Buffalo Ridge 4, Marere Circuit 3, Zunguluka 4) and 5 sequenced"

Line 11:
- `eye`: "eye, adults of the type series (male holotype, paratypes)" -> "eye, species description (male holotype, paratypes and referred South Australian specimens)"
- `conditions`: "the sex is stated for the holotype and one 18.7 mm female paratype only." -> "the sex is stated for the holotype and one 18.7 mm female paratype only. Other material referred to the species and excluded from the type series, whose data the Remarks say contributed to the description: AMS I.20171-012 (6 specimens, 2 cleared and stained, 12.4 to 13.1 mm SL, immature; Vivonne Bay, Kangaroo Island, South Australia) and AMS I.49000-001 (2 specimens, 1 CT-scanned, 14.0 to 14.6 mm SL; Victor Harbor, South Australia, 25 March 2015)."
- `conditions`: "the Discussion calls this the most obvious external difference between the two." -> "the Discussion calls this the most obvious external difference between the two. The Diagnosis says the ventral margin of the orbit is 'obscured by cheek in ventral view', and the Discussion says that in B. hutchinsi 'only the lateralmost part of the eye is visible in ventral view'."

Line 13:
- `eye`: "cerebral eyes, adults (two specimens)" -> "cerebral eyes (two specimens)"
- `conditions`: "Sexes and sizes are not given in the text read." -> "The Description gives the worms as 10 to 30 mm long and 7 to 15 mm wide; the Remarks say Lang (1884) called specimens under 1.5 to 2 cm immature, but that the authors' Atlantic specimens were sometimes mature at about 1.5 cm."

Optional, not counted:
- Line 8 `value`: drop " (dichoptic)" if the owner wants values limited to printed wording (the same gloss is in lines 9 and 10).
- Line 13 `note`: add that a GBIF search-result title gives "Eurylepta vittata (Montagu, 1815)"; WoRMS status not read; the owner may confirm the accepted genus before merge.
