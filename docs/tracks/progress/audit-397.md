# audit-397: desk-d304, evidence lines 9 to 15

Audited 1 November 2026 from the desk-d304 files present untracked in the worktree (docs/tracks/progress/desk-d304.md and docs/views/evidence/desk-d304.jsonl, 22 lines; neither committed here, neither edited). This audit takes file lines 9 to 15 (1-based); lines 1 to 8 and 16 to 22 go to two other auditors. HEAD equals origin/main (5f4bde4d). `python3 -I tools/senses/check.py | grep d304`: "docs/views/evidence/desk-d304.jsonl: 22 records, 0 problems". Quote lengths (`len(q.split())`): 27, 21, 27, 11, 11, 9, 7, all within 40; the only non-ASCII character is the en dash in line 11's "Figs 2A–C", which the page prints.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article/6064/download/xml/ (two passes, the XML returned truncated before the Remarks), zookeys.pensoft.net/article_preview.php?id=6064 (two passes), ?id=108286, ?id=12537 (two passes), ?id=2615; zookeys.pensoft.net/article/2615/download/xml/; zse.pensoft.net/article/65280/download/xml/ (truncated), zse.pensoft.net/article_preview.php?id=65280 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs, all read on the first call. Plazi, BHL, bionames, species-id, sealifebase, GBIF, PMC, par.nsf.gov, jyx.jyu.fi and other repository copies were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 11 WebSearches.

Stitching and typos: the unit's report says "pairsof" and "notobserved" are kept as printed; neither word is in lines 9 to 15 (they belong to the Prosphaerosyllis and Apistobranchus records, lines 5 and 6, another auditor's range). In my lines the stitched quotes (9, 10, 11) were rechecked against the page: each join falls at a space in the printed sentence ("cone-shaped," / "with two small projections"; "apparently eyeless," / "located on cephalic segment"; "prominent distal papillae;" / "four darkly pigmented eyes"), and the joined text is what the page prints.

## Bibliographic and licence

- Lines 9, 10 (de León-Espinosa, de León-González 2015). Page byline Angel de León-Espinosa, Jesus A. de León-González; Crossref reverses the order, as the note says; page byline followed. Title as printed with the acute accent "lion´s" (Crossref has an apostrophe); the record follows the page. ZooKeys 530: 129-149, no issue; issued 2015-10-29; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 11 (Zehnpfennig, Mahon 2023). Page and Crossref Jessica R. Zehnpfennig, Andrew R. Mahon; title identical; ZooKeys 1185: 163-180; issued 2023-11-28; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Lines 12, 13 (Vecchi, Stec 2021). Page and Crossref Matteo Vecchi, Daniel Stec; title identical; Zoosystematics and Evolution 97(1): 281-306 (issue in Crossref); issued 2021-05-19; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 14 (Lisi, Daza, Londoño, Quiroga 2017). Page and Crossref Oscar Lisi, Anisbeth Daza, Rosana Londoño, Sigmer Quiroga; title identical; ZooKeys 703: 1-14; issued 2017-09-27; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 15 (Liñero-Arana, Díaz Díaz 2011). Crossref "Ildefonso Linero-Arana", "Oscar Díaz-Díaz"; the page and the XML print "Ildefonso Liñero-Arana" and surname "Díaz Díaz" with a space (given name printed "Oscarn"). The record follows the page for the first author and Crossref's hyphen for the second; the page byline wins. **Fault (fixable).** Title identical; ZooKeys 117: 1-28; issued 2011-07-08; Crossref CC BY 3.0 vor; page prints "Creative Commons Attribution License" without a version, accepted under the rules (page with no versioned licence plus Crossref CC vor).

Bibliographic faults 1 (line 15); licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Searches for "Nymphon lituus", "Callipallene californiensis" and "Exogone (Exogone) dispar" returned treatments and checklists under these names (Plazi, sealifebase, GBIF, national biodiversity portals; none opened) and no sign of synonymy or transfer; WoRMS refused by the tool and not opened. Lines 11 to 14 are species new in the cited papers. Higher taxa as printed:
- Lines 9, 10: "Class Pycnogonida Latreille, 1810", "Order Pantopoda Gerstäcker, 1863", "Family Nymphonidae Wilson, 1878", "Family Callipallenidae Flynn, 1929". Right.
- Line 11: "Class Pycnogonida Latreille, 1810", "Order Pantopoda Gerstäcker, 1863", "Family Callipallenidae Hilton, 1942". Right.
- Lines 12, 13: no class, order or family heading printed (Eutardigrada and Macrobiotidae in the title only); order left empty. Right.
- Line 14: "Heterotardigrada Marcus, 1927", "Echiniscoidea Richters, 1926", "Echiniscidae Thulin, 1928". Right.
- Line 15: "Family Sillydae Grube, 1850" (misprint, noted), "Subfamily Exogoninae Langerhans, 1879"; no class or order heading, so class Polychaeta comes from the title; order empty. Right.

## Duplicates

`git grep -i` on origin/main (5f4bde4d) over the whole docs/ tree for lituus, californiensis, halanychi, annewintersae, rybaki, kristenseni, "Exogone ... dispar" and the five DOI strings: hits only for other species named californiensis (Hippolyte, Hemisquilla, Theatops), desk-d285's Eurycyde bamberi from the same ZooKeys 530 paper (a different species, as the notes say) and audit-375's list of opened DOIs. Every other origin/research/desk-d* branch grepped for the same species and DOI patterns in the evidence and progress files that differ from origin/main: no hits. Duplicate faults 0.

## Per line

### Line 9, Nymphon lituus, four eyes (two pairs)

Description: "Ocular tubercle inserted between the first pair of lateral processes, cone-shaped, with two small projections in the form of papillae, with two pairs of eyes (Fig. 4A)." **Quote MATCH.** Material: six lots UANL-FCB-PYCNO-0048 to -0053, Chocolatero, El Datil and La Concha, 2012-2013, seven specimens (tool summary: five males, two females). The account prints "Female gonopores ... These were observed on only two specimens (AD-8 and AC-15)." and "All other specimens (males) without readily visible gonopores." Two pairs is a total, not a per-side count; four eyes stands.

Fault: the conditions say "The species account has no Remarks section". The account has headings Material examined, Description, Standard measurements, Distribution and Remarks; the Remarks open "The genus Nymphon includes 277 valid species (Bamber et al. 2015)." and compare the oviger spine formula with Child's original description ("The other features do not present major variations."; tool summary for the rest), with no eye text. A false statement about the paper in conditions. Fixable.

**Line 9 FIXABLE.**

### Line 10, Callipallene californiensis, "apparently eyeless"

Description: "Ocular tubercle conical and apparently eyeless, located on cephalic segment just forward of the first pair of lateral processes (Fig. 3B)." **Quote MATCH.** One male UANL-FCB-PYCNO-0047, La Concha, 01/12/2012. Remarks (tool summary) compare the main claw with the original description, no eye text. The qualifier is kept in the value. One pass placed "Palps absent." immediately before the quote, another "Proboscis short and rounded distally (Fig. 3A), with three smooth lips."; uncounted.

**Line 10 MATCH.**

### Line 11, Austropallene halanychi, four eyes

Description of holotype: "Ocular tubercle (Figs 2A–C, 3B, C) low, rounded, slightly inclined backwards, prominent distal papillae;" "four darkly pigmented eyes, anterior pair larger than posterior pair (Fig. 2A, I)." **Quote MATCH.** Holotype male, NMNH 1548440, "Ross Shelf, 570 m depth, 31 January 2013"; no paratypes; Methods "at 560 m depth". Abstract, Diagnosis, Discussion and Table 3 without eye text, no Remarks section (tool summary); figure captions only. As filed.

**Line 11 MATCH.**

### Line 12, Macrobiotus annewintersae, eyes present

"Animals" under "Description of the new species": "Eyes present in live animals and after fixation in Hoyer's medium." **Quote MATCH.** Holotype female US.084.01 with 10 paratypes on the slide, 63 further paratypes on US.084.02-05, and 71 animals at Jyväskylä; differential diagnosis "having eyes (absent in M. anemone)"; Abstract "by the presence of eyes". As filed. Uncounted: the paper reports the species dioecious, with spermatozoa in female spermathecae and male testes and males with lateral gibbosities (tool summary); the conditions could say both sexes are in the material.

**Line 12 MATCH.**

### Line 13, Macrobiotus rybaki, eyes present

Same sentence under the rybaki "Animals" heading. **Quote MATCH.** Holotype male GR.011.11 with 11 paratypes on the slide, 160 further paratypes. Differential diagnosis (M. dariae, M. noemiae, M. santoroi, M. serratus) and Abstract without eye text (tool summary; the preview was cut during the comparisons). Uncounted: as line 12, dioecious with males and females (no spermatozoa seen in female spermathecae).

**Line 13 MATCH.**

### Line 14, Bryodelphax kristenseni, eyespots absent or not visible after mounting

Description of the holotype: "Body colourless, eyespots absent or not visible after mounting." **Quote MATCH**, value keeps the qualifier. Holotype mature female; 10 paratypes, 7 mature females, 2 juveniles, 1 larva (tool summary of slides 00137, 00138, 00143, 00144).

Faults: (a) the conditions say "no other sentence in the paper mentions eyespots", which is true of the word only. The Discussion cites this species on eyes: "With respect to Kristensen’s (1987) definition, we have preferred not to include the presence of “red granulate eyes”" / " as a character of the genus because the presence or absence of eyes is variable in many genera," / " and can be lost in the slide mounting process (e.g. B. kristenseni sp. n.)." This is the authors' own reading of the state (eyes possibly present and lost in mounting) and belongs in the conditions. (b) Material examined also lists "Four additional specimens, CBUMAG:TAR:00198 (1 specimen), 00100 (3 specimens)," from Bella Vista, 1,930 m, 2012, stages not stated; omitted. One record error, fixable.

**Line 14 FIXABLE.**

### Line 15, Exogone (Exogone) dispar, four eyes (two pairs)

Description: "Prostomium with two pairs of lentigerous eyes." after "Body relatively long, with up to 41 chaetigers." **Quote MATCH.** Material: 4 + 2 + 16 + 6 + 12 + 3 + 12 + 8 = 63 specimens in 8 lot entries, fine sand, sand with Gemma gemma, Aplysina fistularis and Ircinia felix, 1 to 4 m; no sex or stage; Remarks on abundance in Trinidad and Tobago, no eye text; no new species in the paper. Conditions right. Fault: second author's surname (see Bibliographic).

**Line 15 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Nymphon lituus, 4 eyes | FIXABLE | conditions | says the account has no Remarks; it has one |
| 10 | Callipallene californiensis, apparently eyeless | MATCH | | quote, single male, qualifier kept |
| 11 | Austropallene halanychi, 4 eyes | MATCH | | holotype only, depths both given |
| 12 | Macrobiotus annewintersae, eyes present | MATCH | | quote, type series, M. anemone contrast |
| 13 | Macrobiotus rybaki, eyes present | MATCH | | quote, type series |
| 14 | Bryodelphax kristenseni, eyespots absent or not visible | FIXABLE | conditions | Discussion sentence citing this species on eyes lost in mounting omitted; four Bella Vista specimens omitted |
| 15 | Exogone (Exogone) dispar, 4 eyes | FIXABLE | source.authors | "Díaz-Díaz" for printed "Díaz Díaz" |

Errors: 3 of 7 records (42.9%); 3 fixable (lines 9, 14, 15), 0 held out, 0 unfixable; no line to drop. The rate is above 5%, so lines 9 to 15 merge by the drop-the-errors route: lines 10 to 13 as filed, lines 9, 14 and 15 with the replacements below (or dropped if the replacements are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named.

Line 9:
- `conditions`: "The species account has no Remarks section and no other eye statement." -> "The species account's Remarks compare the oviger spine formula with Child's original description and say nothing about the eyes; the account has no other eye statement. Females were identified by gonopores on two specimens; the other five are called males for lack of visible gonopores."

Line 14:
- `conditions`: "Holotype mature female plus 10 paratypes (mature females, juveniles and a larva) from the Sierra Nevada de Santa Marta, Colombia." -> "Holotype mature female plus 10 paratypes (mature females, juveniles and a larva) from the Sierra Nevada de Santa Marta, Colombia; Material examined also lists four additional specimens from Bella Vista (1,930 m, 2012), stages not stated."
- `conditions`: "the Diagnosis and Remarks do not mention eyes and no other sentence in the paper mentions eyespots." -> "the Diagnosis and Remarks do not mention eyes. The Discussion leaves 'red granulate eyes' out of the genus definition 'because the presence or absence of eyes is variable in many genera, and can be lost in the slide mounting process (e.g. B. kristenseni sp. n.).'"

Line 15:
- `source.authors`: "Liñero-Arana I, Díaz-Díaz O" -> "Liñero-Arana I, Díaz Díaz O"
- `note` (same fault): "Crossref gives the first author as Linero-Arana, the page Liñero-Arana;" -> "Crossref gives the authors as Linero-Arana and Díaz-Díaz, the page Liñero-Arana and Díaz Díaz;"
