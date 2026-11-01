# audit-400: desk-d305, evidence lines 9 to 16

Audited 1 November 2026 from the desk-d305 files present untracked in the worktree (docs/tracks/progress/desk-d305.md and docs/views/evidence/desk-d305.jsonl, 16 lines; neither committed here, neither edited). This audit takes file lines 9 to 16 (1-based); lines 1 to 8 go to another auditor. HEAD equals origin/main (49380a17). `python3 -I tools/senses/check.py | grep d305`: "docs/views/evidence/desk-d305.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`): 9, 8, 10, 8, 38, 28, 6, 20, all within 40.

Sources opened (WebFetch, every article URL from a WebSearch result or the record's own URL): zookeys.pensoft.net/article/80184/download/xml/ (truncated in the key, before the treatments), zookeys.pensoft.net/article/80184/ (outline only), zookeys.pensoft.net/article_preview.php?id=80184 (four passes, one per species), zookeys.pensoft.net/article/30139/download/xml/, europeanjournaloftaxonomy.eu/index.php/ejt/article/download/358/735 (two passes), zookeys.pensoft.net/article_preview.php?id=8580 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for all four DOIs, all read on the first call, plus a second read of 10.3897/zookeys.600.8580 for the spelling of the second author. Plazi, BHL, bionames, archive.org, PMC, the Frankfurt repository and other repository copies were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

Stitching and verbless sentences: every stitched quote in my range was rechecked against the page. The chaetognath sentences (lines 9 to 12) each came back as one piece, as printed, between full stops; Sarax (line 13) joins at "two pairs of lateral eyes," / "instead of three or none", Charinus israelensis (line 14) at "but with tapetum;" / "median eye tubercle absent", Charinus taboa (line 16) at "(less pigmentation in smaller specimens)" / "and with one seta"; each join falls at a space in the printed sentence. The chaetognath sentences are verbless descriptive sentences that stand between full stops inside a species Description written wholly in that style ("Hooks 8.", "Rigid and translucent body (Fig. 12)."); following audit-395's acceptance of a telegraphic Diagnosis sentence, they count as whole sentences. None is a heading or a clause cut from a longer sentence. The Charinus israelensis and Sarax sentences have verbs or are full sentences ending at a full stop; the israelensis sentence opens after "1st pair of furrows placed just behind lateral protrusion; all furrows reach middle line."

## Bibliographic and licence

- Lines 9 to 12 (Choo, Jeong, Soh 2022). Page byline Seohwi Choo, Man-Ki Jeong, Ho Young Soh; Crossref identical. Title identical. ZooKeys 1106: 165-211, no issue; issued 2022-06-21; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 13 (Miranda, Reboleira 2019). Page and Crossref Gustavo Silva de Miranda, Ana Sofia P. S. Reboleira; title identical; ZooKeys 820: 1-12; issued 2019-01-28; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 14 (Miranda, Aharon, Gavish-Regev, Giupponi, Wizen 2016). Page byline "Gustavo S. MIRANDA, Shlomi AHARON, Efrat GAVISH-REGEV, Alessandro P.L. GIUPPONI & Gil WIZEN"; Crossref same order. Page prints "European Journal of Taxonomy 234: 1–17 (2016)"; Crossref issue 234, no pages; issued 2016-09-28. Licence: page "This work is licensed under a Creative Commons Attribution 3.0 License."; Crossref CC BY 3.0, content-version unspecified; publisher's own free full text; accepted. **Fault (fixable):** the title. The page prints "A new species of Charinus Simon, 1892 (Arachnida: Amblypygi: Charinidae) from Israel and new records of C. ioanniticus (Kritscher, 1959)" with no comma after "Israel" (asked directly; Crossref also has none); the record has "from Israel, and new records".
- Lines 15, 16 (Vasconcelos, Giupponi, Ferreira 2016). Page byline Ana Caroline Oliveira Vasconcelos, Alessandro Ponce de Leão Giupponi, Rodrigo Lopes Ferreira; title identical; ZooKeys 600: 35-52; issued 2016-06-22; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted. Authors field "Vasconcelos A C O, Giupponi A P L, Ferreira R L" is right. **Fault (fixable), both lines:** the note says "Crossref spells the second author 'Ponce de León Giupponi'". Crossref's given name for the second author is "Alessandro Ponce de Leão", that is "Leão", the same as the page (second read, raw escape reported). The note states a Crossref discrepancy that does not exist.

Bibliographic faults: line 14 (title), lines 15 and 16 (note); licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Pterosagitta draco, Flaccisagitta enflata, Krohnitta subtilis and Parasagitta elegans are the names used in the 2022 redescriptions and in current plankton atlases (search results only; WoRMS refused by the tool and not opened); no sign of synonymy. Lines 13 to 16 are species described as new in the cited papers; searches returned them under the same names. Higher taxa as printed:
- Line 9: "Family Pterosagittidae Tokioka, 1965a"; lines 10, 12: "Family Sagittidae (Claus & Grobben, 1905)"; line 11: "Family Krohnittidae Tokioka, 1965"; order "Aphragmophora" (the XML gives "Aphragmophora" with "Tokioka, 1965a"); no class heading in the Systematics (Sagittoidea in title and Introduction only), class left empty. Right, by the audit-397 precedent for title-only higher taxa.
- Line 13: family heading "Charinidae Quintero, 1986"; Amblypygi only in the keywords and title; record gives order Amblypygi. Right (the note says where it comes from).
- Line 14: order and family as the note says (not re-read; no conflict seen). Right.
- Lines 15, 16: family heading "Charinidae Quintero, 1986"; order from the title. Right.

## Repeats

`git grep -i` on origin/main (49380a17) over the whole docs/ tree for Pterosagitta, Flaccisagitta, Krohnitta, "Parasagitta elegans", "Sagitta elegans", "Sagitta enflata", "Sarax timorensis", "Charinus israelensis", "Charinus taboa" and the four DOI strings: one hit, docs/tracks/progress/desk-d285.md line 15, which records that d285 dropped Sarax timorensis (no filed record). Every origin/research/desk-d* branch grepped for the same patterns under docs/: see the result line at the end of this section. The two Charinus taboa records are separate traits of one paper (median eyes, line 15; lateral eyes, line 16), each from its own sentence, and neither repeats the other or anything on main. Repeat faults 0.

## Per line

### Line 9, Pterosagitta draco, rectangular eyes with T-shaped pigment

Description: "Rectangular eyes with "T" shaped eye pigments (Fig. 12B)." between "Wide collarette extending over entire body and reaching anterior of seminal vesicles (Fig. 12A. C)." and "Intestinal diverticula absent (Fig. 3B)." **Quote MATCH** (the tool returns straight quotes; the record's curly quotes are not contradicted). Material examined: "Feb 2020, NIBRIV0000895299 (one specimen)." Value says no more than the quote and is scoped to this species' Description.

Fault: the conditions say "The Remarks do not mention eyes." The Remarks list among the characters consistent with Pacific records "a corona ciliata located between" / "the back of the eye and the neck", and the Description ends "Corona ciliata anteriorly opened with horseshoe shape beginning in neck region and ending just behind eyes (Figs 10B, 12A)." The statement is false (line 11's conditions draw this distinction correctly). Uncounted part of the same fix: the Description opens "Total body length ranged between 6.5 and 9.1 mm", a range, although Material examined lists one specimen; the conditions give only the one specimen. One record error, fixable.

**Line 9 FIXABLE.**

### Line 10, Flaccisagitta enflata, round eyes with star-shaped pigment

Description: "Round eyes with star-shaped eye pigments (Fig. 14B)." after "Blunt teeth (Fig. 14B)." **Quote MATCH.** Material: 3 + 4 + 1 = 8 specimens in three lots (Korea Strait Nov 2019; northern East China Sea Feb 2020, two lots). Remarks: "The transparent and flaccid body, star-shaped eye pigments and seminal vesicle morphology were consistent" / "with those recorded in previous studies by Alvariño (1967) and Nagasawa (1976)."; "In this study, only the small type (< 20 mm) of F. enflata was collected." Conditions right.

**Line 10 MATCH.**

### Line 11, Krohnitta subtilis, round eyes with E-shaped pigment

Description: "Round eyes with eye pigments in "E" shape (Fig. 11B)." after "Grasping spine abruptly curved (Fig. 8A)." **Quote MATCH.** Material: one specimen Korea Strait (NIBRIV0000895313), one northern East China Sea (NIBRIV0000895312), both Feb 2020. Remarks: corona ciliata "in front of the eyes" in Korean specimens versus "located behind the eye" in earlier records; conditions say so. Conditions right.

**Line 11 MATCH.**

### Line 12, Parasagitta elegans, square eyes with plus-shaped pigment

Description: "Square eyes "+" shaped eye pigments (Fig. 17B)." after "Caudal fin roundish triangular-shaped (Fig. 17C)."; no "with", as the record says. **Quote MATCH.** Material: "NIBRIV0000895306 (five specimens)", East Sea, Feb 2020; body length 32.5 to 37.0 mm. Remarks have no eye text (the corona ciliata sentence is in the Description). Uncounted: the conditions' "the Remarks mention that adults exceed 40 mm" paraphrases "Adult specimens (> 40 mm) collected in this study had small intestinal diverticula.", which sits oddly with the 32.5-37.0 mm range; the paraphrase does not touch the eye value.

**Line 12 MATCH.**

### Line 13, Sarax timorensis, two pairs of lateral eyes

Abstract: "The new species is here described bears the unique character state of two pairs of lateral eyes," / "instead of three or none as in all other living species of Amblypygi, and expands the biogeographic range of the genus." **Quote MATCH**, printed grammar kept, 38 words. Material: "Holotype: Timor-Leste: Lautém district, Puropoko Cave," ... "6–12.ix.2016, A.S.P.S. Reboleira leg. (male, NHMD)." "Female unknown." No paratypes. Diagnosis: "presence of only two pairs of lateral eyes" and "a unique character state known only from a few fossil species (Kronocharon longicalcaris Wunderlich, 2015" / "and Paracharonopsis cambayensis Engel & Grimaldi, 2014)." Description: "Median eyes and tubercle weakly developed (Fig. 1B);" ... "two pairs of lateral eyes (Fig. 2B, C) weakly developed, pale colored,". Discussion: "Sarax species lacking eyes are unknown ..."; "A distinct eye arrangement, however, is known in extinct taxa." Conditions right in substance. The value's "three pairs" for the quote's "three" follows from "two pairs of lateral eyes, instead of three"; accepted.

Uncounted: the conditions say "some species of Kronocharon and Paracharonopsis also have two pairs of lateral eyes" without saying they are extinct (Burmese amber and fossil species in the Diagnosis and Discussion), so a reader could take them as living exceptions to the Abstract's "all other living species". An optional wording is given below.

**Line 13 MATCH.**

### Line 14, Charinus israelensis, eyes small, median eyes almost absent

Description, Carapace: "Eyes small, lateral eyes poorly or non-pigmented, but with tapetum;" / "median eye tubercle absent and eyes almost absent, only a pair of small dots with remnant of lenses." after "1st pair of furrows placed just behind lateral protrusion; all furrows reach middle line." **Quote MATCH.** Types: holotype ♀ Mimlach cave, 30 Mar. 2014 (HUJINVAMB 111A); paratypes 1 ♀ Mimlach, 3 ♀♀ Susita cave 2 May 2013, 1 ♀ Mimlach 13 Jul. 2013, five female paratypes; conditions right. Abstract and Diagnosis wording as the conditions give.

Faults: (a) title comma (see Bibliographic). (b) The Discussion grades the median eyes differently and is not in the conditions: "... and the development of the median eyes" / "(weakly developed in C israelensis sp. nov. and well developed in C. pakistanus)." ("weakly developed" against the Description's "almost absent"); and the troglophile sentence the conditions cite opens "The new species of Charinus was found thus far solely in caves in northern Israel," / "and has a pronounced reduction of the visual system." and states that searches outside caves and survival experiments "were not done". One record error, fixable.

**Line 14 FIXABLE.**

### Line 15, Charinus taboa, median eyes reduced, with flat tubercle

Description, Carapace: "Median eyes reduced, with flat tubercle." after "Carina begins at the corners of the anterior margin and extends from the coxae of leg II" / "to the corners of the posterior margin." **Quote MATCH.** Type material: holotype male MNRJ 09091, Taboa cave, 15 Sept. 2005; paratypes from Taboa juvenile female ×2 (both printed MNRJ 09092), female ×3, male ×2, juvenile male ×2; BR 24 cave female and male (22 Jun. 2015) and female (18 Dec. 2015). Conditions' counts right (the BR 24 dates are not given, uncounted). Methods (tool summary): "The description of the species was based on the entire type material."; conditions' "not tied to a sex" right. Diagnosis "median eyes reduced, with flattened tubercle;" agrees.

Fault: the note's Crossref spelling (see Bibliographic). One record error, fixable.

**Line 15 FIXABLE.**

### Line 16, Charinus taboa, lateral eyes not very developed, unpigmented

Description: "Lateral eyes not very developed, without pigmentation (less pigmentation in smaller specimens)" / "and with one seta posterior to each triad." **Quote MATCH**; the next sentence opens "Frontal hump present at each side". Separate trait from line 15, separate sentence.

Faults: (a) the note's Crossref spelling (see Bibliographic). (b) The Diagnosis reads "lateral eyes not developed and without pigmentation (little pigmentation in smaller individuals);", stronger than the Description's "not very developed"; the conditions report the Diagnosis only as "unpigmented lateral eyes" and drop the "not developed" wording. One record error, fixable.

**Line 16 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Pterosagitta draco, rectangular eyes, T pigment | FIXABLE | conditions | says the Remarks do not mention eyes; they place the corona ciliata behind the eye |
| 10 | Flaccisagitta enflata, round eyes, star pigment | MATCH | | quote, three lots, Remarks cited |
| 11 | Krohnitta subtilis, round eyes, E pigment | MATCH | | quote, two specimens |
| 12 | Parasagitta elegans, square eyes, + pigment | MATCH | | quote as printed without "with" |
| 13 | Sarax timorensis, two pairs of lateral eyes | MATCH | | Abstract sentence whole, holotype only |
| 14 | Charinus israelensis, eyes small, median almost absent | FIXABLE | source.title, conditions | comma not printed in title; Discussion "weakly developed" median eyes omitted |
| 15 | Charinus taboa, median eyes reduced | FIXABLE | note | Crossref prints "Leão", not "León" |
| 16 | Charinus taboa, lateral eyes not very developed | FIXABLE | note, conditions | Crossref spelling; Diagnosis "not developed" omitted |

Errors: 4 of 8 records (50.0%); 4 fixable (lines 9, 14, 15, 16), 0 held out, 0 unfixable; no line to drop. Thin chaetognath records (lines 9 to 12): each value is what its species' Description prints and is scoped to that species; accurate. The rate is above 5%, so lines 9 to 16 merge by the drop-the-errors route: lines 10 to 13 as filed, lines 9, 14, 15 and 16 with the replacements below (or dropped if the replacements are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 9:
- `conditions`: "One specimen (NIBRIV0000895299, 9.1 mm, maturity stage 4) from the northern East China Sea, February 2020; no sex given." -> "Material examined lists one specimen (NIBRIV0000895299) from the northern East China Sea, February 2020, which the Remarks give as 9.1 mm at maturity stage 4, although the Description gives a body length range of 6.5-9.1 mm; no sex given."
- `conditions`: "The Remarks do not mention eyes." -> "The Remarks mention the eye only as a landmark (corona ciliata between the back of the eye and the neck), not its form."

Line 14:
- `source.title`: "from Israel, and new records" -> "from Israel and new records"
- `conditions`: "the Discussion suggests a possible troglophile." -> "the Discussion says the species, found so far only in caves in northern Israel, 'has a pronounced reduction of the visual system' and suggests a troglophile, noting that searches outside caves and survival experiments were not done; elsewhere the Discussion contrasts the median eyes as 'weakly developed in C israelensis sp. nov. and well developed in C. pakistanus'."

Line 15:
- `note`: "Crossref spells the second author 'Ponce de León Giupponi'; the page spelling 'Ponce de Leão Giupponi' is followed." -> "Page and Crossref both give the second author as Alessandro Ponce de Leão Giupponi."

Line 16:
- `note`: "Crossref spells the second author 'Ponce de León Giupponi'; the page spelling 'Ponce de Leão Giupponi' is followed." -> "Page and Crossref both give the second author as Alessandro Ponce de Leão Giupponi."
- `conditions`: "the Diagnosis repeats the reduced median eyes and unpigmented lateral eyes (little pigmentation in smaller individuals)." -> "the Diagnosis gives the median eyes as reduced and the lateral eyes as 'not developed and without pigmentation (little pigmentation in smaller individuals)', stronger than the Description's 'not very developed'."

Optional, not counted (line 13):
- `conditions`: "also have two pairs of lateral eyes." -> "also have two pairs of lateral eyes; both are extinct (fossil) species, as the Diagnosis and Discussion say."
