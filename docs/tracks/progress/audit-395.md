# audit-395: desk-d303, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d303 files present untracked in the worktree (docs/tracks/progress/desk-d303.md and docs/views/evidence/desk-d303.jsonl, 8 lines; neither committed here, neither edited; the untracked file is identical to origin/research/desk-d303). Line numbers are the file's (1-based). HEAD equals origin/main (8a0a5033). `python3 -I tools/senses/check.py | grep 'd303'`: "docs/views/evidence/desk-d303.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 10, 9, 13, 10, 10, 5, 11, 7, all within 40; no non-ASCII characters in any quote.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=192633 (two passes), ?id=74243 (two passes), ?id=37061 (two passes), ?id=21164; zookeys.pensoft.net/article/8562/download/xml/, /article/79382/download/xml/, /article/37061/download/xml/, /article/21164/download/xml/; zse.pensoft.net/article_preview.php?id=154936 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for the seven DOIs: six read; 10.3897/zookeys.1096.79382 returned a client error on the first call and on the retry, not worked around. Plazi, BHL, bionames, zoobank, PMC, GBIF, Zenodo, sealifebase and repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Line 1 (Azman, Sawamoto, Ahmad-Zaki 2026). Page and Crossref Abdul-Rahim Azman, Shozo Sawamoto, Abu-Bakar Ahmad-Zaki; title identical; ZooKeys 1284: 205-215, no issue; issued 2026-07-08; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 2 (Hirata, Kikuchi 2022). Page and Crossref Takuma Hirata, Tomohiko Kikuchi; title identical; ZooKeys 1097: 153-165; issued 2022-04-26; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 3 (Othman, Toda, Kikuchi 2016). XML byline "Othman, B.H.R.", "Toda, T.", "Kikuchi, T."; Crossref "Othman Ross; T. Toda; T. Kikuchi", as the note says; title identical; ZooKeys 605: 37-52; issued 2016-07-14; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 4 (Hirata, Fujiwara, Kikuchi 2019). Page and Crossref Takuma Hirata, Yoshihiro Fujiwara, Tomohiko Kikuchi; title identical; ZooKeys 897: 1-18; issued 2019-12-09; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 5 (Tzeng, Ma, Li 2022). Crossref unreadable (two client errors). Page (XML) You-Wei Tzeng, Lin Ma, Xinzheng Li; title as filed (returned in two pieces); ZooKeys 1096: 119-160, 2022; page prints the CC BY 4.0 sentence on the publisher's own free full text. Accepted on the page; the note's statement that Crossref's author order matches was not re-verified here (uncounted).
- Line 6 and 7 (Jiang, Zhou, Ma, Wang, Xie, Chen 2025). Page and Crossref Xuankong Jiang, Jiajun Zhou, Kayan Ma, Yaqin Wang, Zhicai Xie, Huiming Chen; title identical; Zoosystematics and Evolution 101(4): 1531-1554 (issue printed and in Crossref); issued 2025-08-22; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 8 (Angyal, Chávez Solís, Magaña, Balázs, Simoes 2018). Page Dorottya Angyal, Efraín Chávez Solís, Benjamín Magaña, Gergely Balázs, Nuno Simoes (Crossref "Benjamin Magana"); title identical; ZooKeys 735: 1-25; issued 2018-02-06; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All eight species are described as new in the cited papers ("sp. nov." or "sp. n."); names rest on the original descriptions. Searches for "Macrobrachium parvum" and "Mayaweckelia troglomorpha" returned only the original papers and their copies (no homonym, synonymy or transfer seen; WoRMS refused by the tool and not opened). No class heading is printed in any of the eight treatments, so the absent `class` field is not counted (audit-393 counted empty class only where printed). Higher taxa as printed:
- Line 1: "Order Mysida Haworth, 1825", "Family Mysidae Haworth, 1825", "Subfamily Palaumysinae Wittman, 2013". Right.
- Line 2: "Order Leptostraca Claus, 1880", "Suborder Nebaliacea Calman, 1904", "Family Nebaliidae Samouelle, 1819". Right.
- Line 3: "Order Leptostraca Claus, 1880", "Family Nebaliidae Samouelle, 1819". Right.
- Line 4: no order or family heading; the Introduction prints "The genus Nebalia is a member of the Order Leptostraca, Suborder Nebaliacea, Family Nebaliidae." Right (the note cites a sister paper instead of this sentence; uncounted).
- Line 5: "Order Tanaidacea Dana, 1849", "Suborder Apseudomorpha Sieg, 1980", "Superfamily Apseudoidea Leach, 1814", "Family Apseudidae Leach, 1814", "Subfamily Apseudinae Leach, 1814". Right.
- Lines 6, 7: "Family Palaemonidae Rafinesque, 1815"; no order heading, Decapoda printed in the title. Right.
- Line 8: "Order Amphipoda Latreille, 1816", "Suborder Senticaudata Lowry & Myers, 2013", "Family Hadziidae S. Karaman, 1943". Right.

## Trait key

eye_type throughout, on main. Trait-key faults 0.

## Duplicates

`git grep -i` on origin/main (8a0a5033) over the whole docs/ tree for jetama, agoensis, terazakii, tagiri, spinidigitus, guizhouense, "Macrobrachium parvum", Mayaweckelia, troglomorpha, Palaumysis, Sarsinebalia and the seven DOI strings: hits only for Buteo galapagoensis (docs/views/gaps), "Katagiri" in a crayfish reference (docs/views/sheets/crab.md) and "PMC9848977 Sarsinebalia" in docs/tracks/progress/desk-d279.md (a PMC page that returned reCAPTCHA, a different leptostracan paper, nothing filed). All 1,485 remote branches grepped for the same species and DOI patterns in every docs/ file that differs from origin/main: hits only on origin/research/desk-d303 itself. Duplicate faults 0.

## Per line

### Line 1, Palaumysis jetama, large eye, cornea globular and well pigmented

Male Description (heading "Male. Head and cephalic appendage"): "Eye (Fig. 4A, B, F) large, cornea globular, well pigmented." **Quote MATCH.** The heading does not say holotype, but Fig. 4's caption reads "holotype, male, 2.52 mm, UKMMZ-1632", so the record's "adult male holotype" stands; the type list gives "UKMMZ-1623", the captions "UKMMZ-1632", as the conditions say. Type material as filed (allotype ovigerous female; paratypes seven males and seven females, five females, ten males and five females); "SCUBA diving, 9 September 2025, 22 m depth". Diagnosis "Eyes well developed, with globular cornea."; female "Antennules, antennae, eyes, and abdominal somites generally as in male;"; Abstract, Remarks and key without eye text (tool summary). All in the conditions.

**Line 1 MATCH.**

### Line 2, Sarsinebalia agoensis, compound eye subrectangular with three terminal lobes

Diagnosis: "Compound eyes subrectangular, with three lobes on terminal margin." **Quote MATCH.** Description "Subrectangular in shape, ommatidial part covering most of eyestalk, with three serrated lobes on terminal margin (Fig. 1E)."; Abstract "the compound eye has three distal lobes;"; Remarks "S. agoensis sp. nov. is the only known species in the genus with three lobes on the terminal margin of the eyestalk;". All given.

Fault: the conditions say "further examined material three females", which counts six females. The page prints "Types material": holotype "adult ♀, 8.0 mm TL", paratypes "two adult ♀♀ (TL: 5.6–6.5 mm)"; then "Examined material": "Three ♀♀ (TL: 4.5–8.0 mm) collected from the Japanese Pacific coast near Ago Bay," R/V Tansei Maru KT 86-6, 120 m, May 1986. The paper does not say these are further specimens; the holotype's 8.0 mm is the range's maximum, so they read as the type series itself (the 4.5 mm minimum does not match the paratype range, which leaves it open). Sample composition stated beyond the paper. "Ago Bay, Japan" also drops "near" and the Pacific coast. Fixable.

**Line 2 FIXABLE.**

### Line 3, Nebalia terazakii, compound eye without papilla; ommatidial part 0.67 of eyestalk

Holotype description: "Compound eye without papilla (Fig. 1e), ommatidial part occupying 0.67 length of eyestalk." **Quote MATCH.** Holotype "female, post ovigerous, 2.2 mm carapace length and 5.3 mm total length, Ref UMTCrus 00478"; paratypes 12, 6, 5 and 4 adult females plus 32 juveniles (in the last lot). No heading named Diagnosis; Abstract "the eyes have no dorsal papilla or lobes."; Remarks "The area occupied by the ommatidial part of the eye is similar for N. terazakii sp. n., N. dolsandoensis," and "however, in N. koreana and N. pseudotroncosoi the area is larger and smaller respectively." All as filed.

**Line 3 MATCH.**

### Line 4, Nebalia tagiri, ommatidial part covering two-thirds of eye-stalk

Female holotype description: "Compound eye (Fig. 2C): ommatidial part covering two-thirds of eye-stalk." followed by "Supraocular plate reaching to ommatidial part." **Quote MATCH.** Holotype "adult ♀ of 10.7 mm TL"; allotype "adult ♂ of 7.0 mm TL"; paratypes 3 adult ♂♂, 3 adult ♀♀; allotype description without eye text; Abstract without eye text; Remarks "(1) smooth oval eye-stalk; (2) ommatidial part covering two-thirds of eye-stalk;". As filed.

Uncounted: the XML places the "Diagnosis" that holds "Surface of eyes smooth." under "Genus Nebalia Leach, 1814", before the "Nebalia tagiri sp. nov." heading (its characters are species-level). The conditions' "The Diagnosis says" is true; a note fix below says where it sits.

**Line 4 MATCH.**

### Line 5, Apseudes spinidigitus, eye lobe without visual elements

Description (paratype MBM032095): "Eye lobe well separated, wide and short, without visual elements." **Quote MATCH.** Holotype MBM287293, non-ovigerous simultaneous hermaphrodite, 8.3 mm, 43 m; paratype MBM032095, 8.5 mm (dissected), 55 m; MBM032282 four non-ovigerous simultaneous hermaphrodites (tool summary). Remarks "a pair of wide but short eye lobes without visual elements"; Abstract and Diagnosis without eye text (tool summary). Conditions right; the record says plainly the description is of the paratype.

**Line 5 MATCH.**

### Line 6, Macrobrachium guizhouense, cornea totally degenerated

Description: "Eyes with cornea totally degenerated." then "Ocular peduncle small, elliptical and non-pigmented (Figs 8, 9A)." **Quote MATCH.** The quote does not name the species; it sits in the M. guizhouense treatment, which `where` states. Holotype "male (IBGAS-Dec-Pal-493-1) (tl 52.1 mm, cl 14.5 mm, rl 7.2 mm)", Malai Cave, "9. VI. 2023"; paratypes 28 males and 61 females, Malai and Gengzao caves (tool summary). No Diagnosis heading ("Type materials." then "Description."). Remarks "completely degraded somatic pigmentation and eyes"; Table 4 "completely degraded"; Discussion lists it among stygobites with "non-functional eyes" (tool summary). Consistent with the value; no contrary wording. Name: new in this paper, no other usage found.

**Line 6 MATCH.**

### Line 7, Macrobrachium parvum, cornea strongly degenerated, small tip area pigmented

Description and Diagnosis: "Eyes with cornea strongly degenerated, only small area on tip pigmented." **Quote MATCH**; the quote does not name the species and sits in the M. parvum treatment. Holotype "male (IBGAS-Dec-Pal-484-1)", Nonglitun Cave, "10. IV. 2024"; paratypes 9 males, 32 females from Nonglitun, Nongguangshang and Shuiyuandi caves. Remarks "the presence of degenerated yet traceable body color and eyes", "We therefore classify it as a stygophile rather than a stygobite."; Table 4 row "Somatic pigmentation and eyes" "reduced"; Discussion "substantially reduced ocular structures". All in the conditions. Name: new in this paper; a search for "Macrobrachium parvum" found no earlier use.

**Line 7 MATCH.**

### Line 8, Mayaweckelia troglomorpha, eyeless

Diagnosis, first sentence: "Medium-sized, eyeless hadziid with conspicuous troglomorphic traits." **Quote MATCH.** Whole-sentence question: it is a complete orthographic sentence (capital to full stop) and the first of a Diagnosis written throughout in verbless telegraphic style (the next begins "The first antenna almost twice as long as body and three times as long as the second antenna;", the last "Largest males and females both measured 10 mm."). Nothing is cut from it, and it is the paper's own sentence unit, not a phrase lifted from a longer sentence. Judged a whole sentence under the quote rule, as audit-394 accepted the noun-phrase Diagnosis "A rather small eyeless trechine beetle, yellowish brown, body thin and elongate, sparsely pubescent." (desk-d302 line 5). No other sentence in the paper carries the value (Abstract, Description, Remarks without eye text; Etymology "highly adaptive troglomorphic features"), as the conditions say. Type material as filed (holotype ♂ 10 mm Nr. 00046, allotype ♀ 10 mm Nr. 00113, paratypes ♀ 7 mm, ♂ 8 mm, juveniles 3 and 5 mm).

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Palaumysis jetama, large globular pigmented eye | MATCH | | quote, holotype figure, type series, female and Diagnosis wording right |
| 2 | Sarsinebalia agoensis, eye with three terminal lobes | FIXABLE | conditions | "further" three females not printed; they read as the type series |
| 3 | Nebalia terazakii, no papilla, ommatidia 0.67 of stalk | MATCH | | quote, female series and juveniles right |
| 4 | Nebalia tagiri, ommatidia two-thirds of stalk | MATCH | | quote, female holotype only, Remarks right |
| 5 | Apseudes spinidigitus, eye lobe without visual elements | MATCH | | quote from paratype description, stated |
| 6 | Macrobrachium guizhouense, cornea totally degenerated | MATCH | | quote, no Diagnosis, consistent elsewhere |
| 7 | Macrobrachium parvum, cornea strongly degenerated | MATCH | | quote, stygophile wording given |
| 8 | Mayaweckelia troglomorpha, eyeless | MATCH | | whole telegraphic Diagnosis sentence; only eye statement |

Errors: 1 of 8 records (12.5%); 1 fixable (line 2), 0 held out, 0 unfixable; no line to drop. The rate is above 5%, so the unit merges by the drop-the-errors route: lines 1 and 3 to 8 as filed, line 2 with the replacement below (or dropped if the replacement is not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in its field in the line named.

Line 2:
- `conditions`: "two adult female paratypes (5.6-6.5 mm TL); further examined material three females." -> "two adult female paratypes (5.6-6.5 mm TL). The 'Examined material' entry lists three females (TL 4.5-8.0 mm) from the Japanese Pacific coast near Ago Bay (R/V Tansei Maru KT 86-6, 120 m, May 1986); the paper does not say whether these are the three type specimens or further females (the holotype's 8.0 mm is the range's maximum, the 4.5 mm minimum is below the paratype range)."
- `conditions`: "Ago Bay, Japan, 120 m." -> "Japanese Pacific coast near Ago Bay, 120 m, May 1986."

Line 4 (uncounted):
- `conditions`: "The Diagnosis says 'Surface of eyes smooth.'" -> "The Diagnosis, printed under the heading 'Genus Nebalia Leach, 1814' before the species heading, says 'Surface of eyes smooth.'"
- `note`: "Leptostraca and Nebaliidae are the order and family of the genus Nebalia and agree with the sister ZooKeys Nebalia paper." -> "The Introduction prints 'The genus Nebalia is a member of the Order Leptostraca, Suborder Nebaliacea, Family Nebaliidae.'"
