# audit-398: desk-d304, evidence lines 16 to 22

Audited 1 November 2026 from the desk-d304 files present untracked in the worktree (docs/tracks/progress/desk-d304.md and docs/views/evidence/desk-d304.jsonl, 22 lines; neither committed here, neither edited; the untracked file is identical to origin/research/desk-d304). This audit covers file lines 16 to 22 only (1-based); lines 1 to 8 and 9 to 15 go to two other auditors. HEAD equals origin/main (5f4bde4d). `python3 -I tools/senses/check.py | grep d304`: "docs/views/evidence/desk-d304.jsonl: 22 records, 0 problems". Quote lengths (`len(q.split())`): 7, 10, 11, 7, 10, 9, 9, all within 40; no non-ASCII characters in any quote.

All seven lines cite one paper: Liñero-Arana and Díaz Díaz 2011, ZooKeys 117: 1-28, DOI 10.3897/zookeys.117.858.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=2615 (two passes) and zookeys.pensoft.net/article/2615/download/xml/ (two passes); api.crossref.org/v1/works/10.3897/zookeys.117.858 (answered first time); for names, sealifebase.org SpeciesSummary id=39415 and a kiwix mirror of the Wikipedia "Syllis" page. Plazi, GBIF, BHL, species-id.net, PMC and Zenodo results were not opened; no curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened (an ezproxy result in one search was skipped). WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Crossref: Ildefonso Linero-Arana, Oscar Díaz-Díaz; "Syllidae (Annelida, Polychaeta) from the Caribbean coast of Venezuela"; ZooKeys 117, pages 1-28, no issue; published online 2011-07-08; licence http://creativecommons.org/licenses/by/3.0/ (vor).
- Page: header "ZooKeys 117: 1–28, doi: 10.3897/ZooKeys.117.858", "Published 8 July 2011"; title identical; body byline "Ildefonso Liñero-Arana, Oscarn Díaz Díaz" (XML contrib surname "Díaz Díaz", unhyphenated; the page metadata gives "Oscar Díaz-Díaz"); copyright "(C) 2011 Ildefonso Liñero-Arana. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, ..." with no version on the preview page (the XML links by/3.0). Publisher's own free full text, CC BY. Accepted.
- Author order, title, journal, volume, pages, year and access "open" right on all seven lines. Uncounted: the record's "Díaz-Díaz O" follows Crossref and the page metadata, while the printed byline has "Díaz Díaz" without hyphen; the record follows the printed byline for the first author (Liñero-Arana) and not for the second. The rule fixes author order, which is right; a replacement is offered below.

Bibliographic faults 0; licence faults 0.

## Names and higher taxa

All seven are known species recorded from Venezuela, none new in the paper. Names in current use: Exogone lourei Berkeley & Berkeley, 1938 (SeaLifeBase, no synonym line; species-id.net and Plazi results carry "Exogone (Exogone) lourei"); Sphaerosyllis piriferopsis Perkins, 1981 and S. taylori Perkins, 1981 (search results, including a JMBA paper on Sphaerosyllis from Cuba with a syllid list, not opened); Syllis amica Quatrefages, 1866, S. gracilis Grube, 1840, S. pseudoarmillaris Nogueira & San Martín, 2002, S. vittata Grube, 1840 (Syllis species list). WoRMS refused by the tool; no synonymy or transfer seen in any result. Name faults 0.

Higher taxa: the page prints "Family Sillydae Grube, 1850" (misspelt; the title says Syllidae); subfamily headings Exogoninae (lines 16 to 18) and Syllinae (lines 19 to 22) as the notes say; no class or order heading. `class` "Polychaeta" rests on the printed title "(Annelida, Polychaeta)"; `order` blank where nothing is printed. Right.

## Trait key

eyes_count throughout, value 4 from "two pairs" in every quote; no per-side count read as a total (pairs times two). Trait-key faults 0.

## Duplicates

`git grep -i -F` on origin/main (5f4bde4d) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks, wanted) for lourei, piriferopsis, Sphaerosyllis, "Syllis amica", "Syllis gracilis", pseudoarmillaris, "Syllis vittata", Exogone, "zookeys.117", "id=2615", Linero, Liñero, Sillydae: "zookeys.117" hits are all zookeys.1177 or zookeys.1178 (other papers); "Sphaerosyllis" hits only desk-d294's mention of Prosphaerosyllis modinouae (a different paper, lines 1 to 8's business); Exogone, the species names, the DOI and the authors have no hit. For all 304 origin/research/desk-d* branches, every docs/ file differing from origin/main was grepped for the species and the DOI: hits only on origin/research/desk-d304 itself. Duplicate faults 0.

## Per line

Every eye sentence below was returned verbatim by the page; none is stitched from pieces (each is under 125 characters), and none carries a typo.

### Line 16, Exogone (Exogone) lourei, two pairs of lentigerous eyes

Description: "Body with up to 50 chaetigers." then "Prostomium with two pairs of lentigerous eyes." then "Median antenna digitiform, lateral antennae short, ovoid." **Quote MATCH**, whole sentence, from the species' Description. Material (tool summary of lots): GCPG198 (3), fine sand, 2 m; BMER203 (15), fine sand, 4 m; BMC101 (7); BMLV101 (9), inside dead Millepora alcicornis, 1-2 m; BMC103 (7), medium sand, 1-2 m: 41 specimens in 5 lots, 1 to 4 m, as filed. No other eye or eyespot wording in the Description (tool summary); no Remarks on eyes. No sexes or stages printed.

**Line 16 MATCH.**

### Line 17, Sphaerosyllis piriferopsis, two pairs, trapezoidal

"Antennae clavate." then "Prostomium with two pairs of lentigerous eyes in trapezoidal arrangement." then "Palps fused dorsally." **Quote MATCH.** Material PAPC106 (12), coarse sand near a seagrass bed, 0.5-1.3 m; BMER103 (8), fine to coarse sand, 1 m: 20 in 2 lots, as filed. No eyespot wording; no Remarks. Uncounted: the note's "it follows a body-length sentence" is wrong here (it follows "Antennae clavate.").

**Line 17 MATCH.**

### Line 18, Sphaerosyllis taylori, two pairs, slightly trapezoidal

"Antennae clavate." then "Prostomium with two pairs of lentigerous eyes in slightly trapezoidal arrangement." then "Palps fused." **Quote MATCH.** Material PAPC106 (2), coarse sand, 2 m; GCLB104 (8), coarse sand near a seagrass bed, 0.5-1.3 m: 10 in 2 lots, 0.5 to 2 m, as filed. No eyespot wording; no Remarks. Same uncounted note slip as line 17.

**Line 18 MATCH.**

### Line 19, Syllis amica, two pairs of lentigerous eyes

"Prostomium with two pairs of lentigerous eyes." **Quote MATCH.** Material lots printed: 15, 2, 6, 8, 4, 28, 11, 6, 15, 8, 34 = 137 specimens in 11 lot entries; fine, coarse and medium sand, inside dead Millepora alcicornis, with Aplysina fistularis, Ircinia felix and Chondrila nucula; 0.5 to 3 m. As filed. No Remarks.

**Line 19 MATCH.**

### Line 20, Syllis gracilis, two pairs, trapezoidal

"Prostomium with two pairs of lentigerous eyes in trapezoidal arrangement." **Quote MATCH.** Material 8, 4, 2, 4, 4, 3, 16, 6 = 47 in 8 lots, with Chondrila nucula, Aplysina fistularis, Ircinia felix, and fine to coarse sand; 1 to 3 m. As filed. No Remarks.

**Line 20 MATCH.**

### Line 21, Syllis pseudoarmillaris, two pairs, trapezoidal

"Prostomium with two pairs of eyes in trapezoidal arrangement." **Quote MATCH.** Material PAPC106 (8), epibionts on Americonuphis magna tubes, 0.3-0.6 m; GCLB205 (3), fine sand, 1 m: 11 in 2 lots, 0.3 to 1 m. As filed. The `eye` field rightly omits "lentigerous". Uncounted: the shared note says "'lentigerous' means lens-bearing as printed", but this account does not print "lentigerous".

**Line 21 MATCH.**

### Line 22, Syllis vittata, two pairs, trapezoidal

"Prostomium with two pairs of eyes in trapezoidal arrangement." **Quote MATCH.** Material BMIL803 (8), on rocks covered by Enteromorpha intestinalis, 1-2 m: one lot, as filed. Same uncounted note slip as line 21.

**Line 22 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 16 | Exogone (Exogone) lourei, 4 eyes | MATCH | | quote, 41 in 5 lots, no other eye wording |
| 17 | Sphaerosyllis piriferopsis, 4 eyes | MATCH | | quote, 20 in 2 lots |
| 18 | Sphaerosyllis taylori, 4 eyes | MATCH | | quote, 10 in 2 lots |
| 19 | Syllis amica, 4 eyes | MATCH | | quote, 137 in 11 lot entries |
| 20 | Syllis gracilis, 4 eyes | MATCH | | quote, 47 in 8 lots |
| 21 | Syllis pseudoarmillaris, 4 eyes | MATCH | | quote, 11 in 2 lots |
| 22 | Syllis vittata, 4 eyes | MATCH | | quote, 8 in one lot |

Errors: 0 of 7 records (0%); 0 fixable, 0 held out, 0 unfixable; no line to drop. Verdict for lines 16 to 22: **ACCEPT** (as filed; the uncounted replacements below are optional). Pooled with the audits of lines 1 to 8 and 9 to 15 when those report.

## Replacement

No counted error. Uncounted, optional; each old string occurs once in its line.

Lines 16 to 22 (`source.authors`, same in each line):
- "Liñero-Arana I, Díaz-Díaz O" -> "Liñero-Arana I, Díaz Díaz O"
- `note`: "Crossref gives the first author as Linero-Arana, the page Liñero-Arana;" -> "Crossref gives the authors as Linero-Arana and Díaz-Díaz, the printed byline Liñero-Arana and Díaz Díaz (given name misprinted 'Oscarn');"

Lines 17 and 18:
- `note`: "it follows a body-length sentence and does not name the species" -> "it follows 'Antennae clavate.' and does not name the species"

Lines 21 and 22:
- `note`: "Four eyes is the product of two pairs; 'lentigerous' means lens-bearing as printed." -> "Four eyes is the product of two pairs; this account does not say 'lentigerous', unlike the other Syllis accounts filed from the paper."
