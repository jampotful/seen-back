# audit-427: desk-d317, evidence lines 9 to 16

Audited 1 November 2026 from the desk-d317 files present untracked in the worktree (docs/tracks/progress/desk-d317.md and docs/views/evidence/desk-d317.jsonl; neither committed here, neither edited). This audit takes file lines 9 to 16; another auditor takes lines 1 to 8. HEAD equals origin/main (d44031679). `python3 -I tools/senses/check.py | grep d317`: "docs/views/evidence/desk-d317.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`) for lines 9 to 16: 12, 12, 12, 5, 5, 24, 11, 22, all within 40.

Sources opened (WebFetch, every page URL from a WebSearch result): subtbiol.pensoft.net/article/61733/download/xml/ (two passes), zookeys.pensoft.net/article/4583/download/xml/ (two passes), jhr.pensoft.net/article_preview.php?id=77931 (two passes), zookeys.pensoft.net/article/3053/download/xml/ (one pass), zookeys.pensoft.net/article/2247/download/xml/ (one pass), zookeys.pensoft.net/article_preview.php?id=27320 (two passes), en.wikipedia.org/wiki/Trilasma and /wiki/Haslundiella (species lists only). Crossref single-DOI lookups api.crossref.org/v1/works/ answered for subtbiol.38.61733 (second call, after one rate limit), zookeys.477.8706, jhr.89.77931, zookeys.217.3136 and zookeys.52.471. zookeys.806.27320 was rate-limited twice and not worked around; its bibliographic check uses the citation line printed on the page. PMC, GBIF, DOAJ, library catalogue records (utm.my, uitm.edu.my, uv.mx), core.ac.uk, aminer, peeref, reviewer.ly, BHL and Plazi were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Lines 9 to 11 (García, Andújar, Oromí, Emerson, López 2021). XML contributor list and Crossref identical in order; title identical; printed "Subterranean Biology 38: 1–18", electronic publication 02 March 2021; Crossref 2021-03-02, pages 1-18, no issue. Licence: XML "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Accepted.
- Line 12 (Giupponi, Kury 2015). Page byline prints Giupponi then Kury; Crossref lists Kury first; the record follows the printed order, as it should. Title identical; pages 1-15; issued 2015-01-26. XML CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 13 (Honsberger, Huber, Wright 2022). Byline and Crossref identical; title identical including the okina printed as U+2018 in "Hawai‘i" (the record has U+2018); "Journal of Hymenoptera Research 89: 73-87"; issued 2022-02-28. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 14 (Faille, Bourdeau, Fresneda 2012). Byline and Crossref identical; full title identical; ZooKeys 217: 11–51; 2012. XML "Creative Commons Attribution License 3.0 (CC-BY)"; Crossref CC BY 3.0 vor. Accepted.
- Line 15 (Shear 2010). Page prints "William A. Shear"; title printed with "México" (Crossref drops the accent; printed form used, right); page prints 9–46 against Crossref 9-45; printed range used, right. XML prints the CC BY sentence with no version; Crossref CC BY 3.0 vor. Accepted.
- Line 16 (Molero, Tahami, Gaju, Sadeghi 2018). Crossref not read (rate limit, twice). Page citation line "Molero R, Tahami MS, Gaju M, Sadeghi S (2018) A survey of basal insects (Microcoryphia and Zygentoma) from subterranean environments of Iran, with description of three new species. ZooKeys 806: 17-46." matches the record in order, title, volume, pages and year. Page CC BY 4.0 sentence. Accepted on the page alone; the note's "Crossref CC BY 4.0 (vor)" was not re-checked here.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Baezia aranfaybo, B. madai, B. tizziri: described as new in the paper; each treatment's Taxon classification block prints Animalia, Coleoptera, Curculionidae (no class). Order and family right; class blank right.
- Metagovea ligiae: new in the paper; classification block Animalia, Opiliones, Neogoveidae (no class). Right. No Opiliones checklist page was opened; Plazi treatment titles in search results carry the name as filed. Not counted.
- Mymaromma menehune: new in the paper. The article preview page has no "Taxon classification" line (tool summary), so the note's "classification block prints Animalia, Hymenoptera, Mymarommatidae" was not confirmed on the copy read; family Mymarommatidae is printed in the title, and Hymenoptera is the journal's and reference titles' order. Fill acceptable; note wording not counted.
- Trechus bouilloni: new in the paper; title prints "(Coleoptera, Carabidae, Trechinae)". The XML pass did not show a classification block (tool summary); order and family are printed in the title either way. No Carabidae catalogue page (Carabcat) was returned by search; GBIF (refused source) and Plazi list the name as filed. Not counted.
- Trilasma ranchonuevo: new in the paper; Nemastomatidae printed in the title and the classification; Wikipedia's genus page lists the species from Shear 2010, citing Schönhofer's 2013 catalogue (catalogue itself not opened). Order Opiliones printed in the title. Right.
- Haslundiella iranica: classification block prints "Order Microcoryphia (=Archaeognatha)", "Family Machilidae"; species heading "Haslundiella iranica Gaju, Molero, Tahami & Sadeghi, sp. n.". Wikipedia genus page lists the species (from GBIF). Right.

No page prints a class for any of the eight lines; class blank is right throughout.

## Repeats

`git grep -il` on origin/main (d44031679) over the whole docs/ tree for Baezia, aranfaybo, madai, tizziri, subtbiol.38.61733, 61733, Metagovea, zookeys.477.8706, Mymaromma, jhr.89.77931, 77931, bouilloni, zookeys.217.3136, Trilasma, ranchonuevo, zookeys.52.471, Haslundiella, zookeys.806.27320. Hits: "Baezia" and "61733" in desk-d316.md (blocked-XML note, no record); "61733" in harvest-c11.jsonl (a Paulownia search record; numeric coincidence); "madai" only as Ishigakicoccus shimadai (desk-d312); "Haslundiella" in desk-d288.md as a dropped candidate. No record on main for any of the eight species or five DOIs. Unmerged branches: the docs/views/evidence/desk-dN.jsonl blob of every research/desk-d* branch not merged into main (317 paths, 19 missing) read with one `git cat-file --batch`; every hit for these species and DOIs sits in one blob, f8e53daec, which is origin/research/desk-d317 itself and equals the worktree file. Repeats: none.

## Per line

### Line 9, Baezia aranfaybo, eyes lacking

Male Description: "Head partially retracted into pronotum, microreticulated with abundant irregular punctation, lacking eyes." Previous sentence "Apterous."; next "Rostrum robust, similar in both sexes, ...". **Quote MATCH**, whole telegraphic sentence, 12 words. Type material matches (holotype male, Cueva de Longueras, 470 m, emerged from roots, 9 Feb 2011, H. López, DZUL; paratypes 2 females 20 Oct 2006 and 20 Aug 2007; other material six individuals from soil washing, 4 Feb 2020, no sex). Female description and Differential diagnosis do not mention eyes (tool summary); Abstract "seven eyeless species", carried in the note. Value no more than the quote.

**Line 9 MATCH.**

### Line 10, Baezia madai, eyes lacking

Same sentence in the male Description, between "Apterous." and "Rostrum robust, widest at antennal insertion, 2× as long ...". **Quote MATCH**. Holotype male only, Cueva de Las Tijaraferas (Cueva de Barros), El Paso, La Palma, 536 m, 10 July 1986, J.L. Martín (DZUL); no paratypes or other material; Female "Unknown."; Methods "was collected in a volcanic cave with pitfall traps baited with blue cheese." All as filed.

**Line 10 MATCH.**

### Line 11, Baezia tizziri, eyes lacking

Same sentence, same neighbours. **Quote MATCH**. Holotype male MSS Barranco de los Hombres, Garafía, 249 m, 20 Sept 2017, R. García (DZUL); paratype 1 male 18 Nov 2020; other material elytra remains, Cueva de La Fajana de Franceses, 120 m, 23 Jan 2002; Methods "derive from the MSS (mesovoid shallow substratum) on La Palma using subterranean traps"; Female "Unknown.". All as filed. (Optional: say the female is unknown.)

**Line 11 MATCH.**

### Line 12, Metagovea ligiae, eyes and eye lenses absent

Male Description: "Eyes and eye lenses absent." Next sentence "Ozophore conical of type 2 (sensu Juberthie 1970: 1373; ...)". The previous sentence came back as "Anterior margin of dorsal scutum with a pair of processes lateral to chelicerae." where the note names "Lateral margin of prosoma bulging ..."; neighbour wording only, not counted. **Quote MATCH**, 5 words. Diagnosis "eyes and eye lenses absent (Figs 1A, C, D)"; female description and Discussion silent on eyes. Habitat sentences as filed.

Fault (one record error, fixable): **paratype count wrong.** Conditions say "paratypes 5 males and 10 females" but the itemised lines that follow, and the page, give 1 ♀ (QCAZ 322), 1 ♂ and 1 ♀ (MCZ 45452), and 3 ♂ and 8 ♀ (MNRJ 8434): 4 male paratypes, 10 female. The page prints no total.

**Line 12 FIXABLE.**

### Line 13, Mymaromma menehune, about 35 ommatidia (ommatidia_count 35)

Female Description, Head: "Eye with about 35 ommatidia." Next "Ocelli absent."; nearby "Malar space short, about the length of one ommatidium." **Quote MATCH**, 5 words. "Eye" is singular, per eye, no n or range; units "ommatidia per eye (about)" and value 35 say no more than the quote; female, as filed. Diagnosis, Discussion and remarks have no eye wording and no congener counts (tool summary). Trait key ommatidia_count fits.

Fault (one record error, fixable): **type status and locality.** Conditions put the paratypes at "Molokai (Mapulehu and Halawa Valleys, 1995-1996, yellow sticky board traps)". The only Moloka‘i paratype line is "Moloka‘i • Mapulehu Valley near Ili‘Ili‘opae heiau, 10–40’, 8–22.xii.1995 and 12–26.iv.1996, W.D. Perreira, yellow sticky board traps (1♀ & 1♂ slide mounted, CNC)"; "Hālawa Valley, 200’, 29.ix–13.x.1995" appears under Other material, not the type series. Also, the male description opens "Similar to female except as follows:" and lists no eye difference, which the conditions should carry beside "The male description has no eye sentence".

**Line 13 FIXABLE.**

### Line 14, Trechus bouilloni, eyes reduced, flat, about eight ommatidia across

Description of the holotype: "Eyes reduced, flat; ommatidia well defined; maximum diameter of about eight ommatidia," / "temples approximately twice the length of eyes, strongly wrinkled to the neck." Previous "Ventral pubescence limited to one seta on each half sternite."; next "Frontal furrows deeply impressed." **Quote MATCH**, one whole sentence, 24 words. Holotype 1 ♂ MNHN, Puerto de Lizarraga, MSS, trap 1–5–1980/15–8–1980, Bourdeau and Fresneda; "Z: 900 m"; paratypes "52 ♂♂, 62 ♀♀, same label data as holotype". No eye wording in Diagnosis, Affinities, female genitalia, Size or Distribution (tool summary). The value, a text description, says no more than the quote and rightly avoids ommatidia_count. "traps 50 cm deep" was not seen in the pass read; not counted.

**Line 14 MATCH.**

### Line 15, Trilasma ranchonuevo, eyes relatively large, bulging

Description: "Circumocular keels suppressed, subocular portion vaguely indicated, eyes relatively large, bulging." Previous "Carapace arcuate, about 1.5X as wide as long, with complete lateral and posterior submarginal keels; ..."; next "Median hood process arising dorsally on eye tubercle, ...". **Quote MATCH**, 11 words. "Male holotype (TMM) from Rancho Nuevo, Tamaulipas, México, collected 10 April 1982 by Terri Treacy."; no paratypes; the key says "(females unknown)". Diagnosis and Notes silent on eyes; the key's eye wording ("reduced eyes") belongs to T. sbordonii only. As filed.

**Line 15 MATCH.**

### Line 16, Haslundiella iranica, compound eyes black, wider than long

Description: "Compound eyes black (Fig. 3, from adult female, those of males not clearly visible), wider than long" / "(l/w: 0.65 and cl/l: 0.53)." **Quote MATCH**, 22 words, printed colons and spacing kept. Table 1 legend defines "eyes cl/l" as "eye contact line/eye length", so the value's "contact line/length 0.53" is printed. Diagnosis "Compound eyes wider than long (l/w = 0.65), lateral ocelli in sublateral position."; ocelli "brownish, sublateral, transversally ovoid"; Discussion silent on eyes. Type material: holotype male MNCN, Mirza Cave, Rafsanjan, Kerman, 20.VI.2015; paratypes 1 male (UCO) same data, 1 female juvenile same locality and date, 1 female (ZM-CBSU) Khane Khoda cave, Yazd, 30.IX.2015; habitat "somewhere between the endogean and parahypogean zones", "collected with a fine brush". As filed. (The only adult female listed is the Yazd paratype, so the sentence describes that specimen; optional.)

**Line 16 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Baezia aranfaybo, eyes lacking | MATCH | | whole sentence; types and female silence right |
| 10 | Baezia madai, eyes lacking | MATCH | | holotype only; blue-cheese pitfall traps right |
| 11 | Baezia tizziri, eyes lacking | MATCH | | MSS holotype and male paratype right |
| 12 | Metagovea ligiae, eyes and lenses absent | FIXABLE | conditions | "5 males" paratypes; the page and the record's own itemisation give 4 |
| 13 | Mymaromma menehune, about 35 ommatidia per eye | FIXABLE | conditions | Hālawa Valley material is Other material, filed as paratypes; male "Similar to female except" omitted |
| 14 | Trechus bouilloni, eyes reduced, flat | MATCH | | whole 24-word sentence; holotype male; 52 ♂, 62 ♀ paratypes |
| 15 | Trilasma ranchonuevo, eyes large, bulging | MATCH | | male holotype; females unknown |
| 16 | Haslundiella iranica, eyes black, wider than long | MATCH | | sentence and ratios verbatim; cl defined in Table 1 legend |

Errors: 2 of 8 records (25%); 2 fixable (lines 12, 13), 0 held out, 0 unfixable; no line to drop. Repeats: none on main or on any unmerged desk branch. Bibliography and licence: no faults (line 16 checked against the page citation line only, Crossref refused by rate limit). Verdict for lines 9 to 16 of desk-d317: **ACCEPT AFTER REPLACEMENT** (lines 9, 10, 11, 14, 15, 16 as filed; lines 12 and 13 with the replacements below, or dropped if they are not applied). Pool with the auditor of lines 1 to 8 for the unit verdict.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 12:
- `conditions`: "paratypes 5 males and 10 females" -> "paratypes 4 males and 10 females"

Line 13:
- `conditions`: "Molokai (Mapulehu and Halawa Valleys, 1995-1996, yellow sticky board traps)" -> "Molokai (Mapulehu Valley, Dec 1995 and Apr 1996, yellow sticky board traps, 1 female and 1 male); Hālawa Valley material (1995) is listed under Other material, not as paratypes"
- `conditions`: "The male description has no eye sentence and the Diagnosis has no eye wording;" -> "The male description opens 'Similar to female except as follows:' and lists no eye difference; the Diagnosis has no eye wording;"

Optional, not counted:
- Line 11 `conditions`: "Male description. Holotype male:" -> "Male description; the female is unknown. Holotype male:"
- Line 13 `note`: "The classification block prints Animalia, Hymenoptera, Mymarommatidae (no class)." -> "No Taxon classification line was seen on the article preview page; family from the title, order Hymenoptera (no class)."
