# audit-396: desk-d304, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d304 files present untracked in the worktree (docs/tracks/progress/desk-d304.md and docs/views/evidence/desk-d304.jsonl, 22 lines; neither committed here, neither edited). This audit covers file lines 1 to 8 only (1-based); lines 9-15 and 16-22 go to two other auditors. HEAD equals origin/main (5f4bde4d). `python3 -I tools/senses/check.py | grep d304`: "docs/views/evidence/desk-d304.jsonl: 22 records, 0 problems". Quote lengths (`len(q.split())`): 13, 37, 39, 20, 38, 37, 30, 30, all within 40. Non-ASCII in quotes: an en dash in line 6 ("5b–d", printed so) and the two "…" cut marks in line 7.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article/161942/download/xml/ (two passes) and article_preview.php?id=161942; subtbiol.pensoft.net/article/55090/download/xml/ (four passes); subtbiol.pensoft.net/article/13701/download/xml/ (two passes); zookeys.pensoft.net/article/49349/download/xml/ and article_preview.php?id=49349 (two passes); zookeys.pensoft.net/article_preview.php?id=73847; zookeys.pensoft.net/article_preview.php?id=6064. Crossref single-DOI lookups (api.crossref.org/v1/works/) for all six DOIs, all read first time. Name check for the mammal from the WebSearch result mammaldiversity.org/taxon/1006995 ("Euroscaptor darwini"). Plazi, BHL, bionames, sealifebase, PMC, GBIF and repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 8 WebSearches.

## Bibliographic and licence

- Line 1 (Nguyen, Bui, Dau, Le, Vu 2025). Page and Crossref Son Truong Nguyen, Hai Tuan Bui, Vinh Quang Dau, Phuong Dinh Le, Yen Huong Vu; title identical; ZooKeys 1255: 239-274, no issue; issued 2025-10-10; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Lines 2, 3 (Núñez, Glasby, Naranjo 2020). Page and Crossref Jorge Núñez, Christopher J. Glasby, Manuel Naranjo; title identical; Subterranean Biology 36: 35-49; issued 2020-11-16; Crossref CC BY 4.0 vor; page prints the CC BY sentence. Accepted.
- Line 4 (Conde-Vela 2017). Page and Crossref Víctor Manuel Conde-Vela; title identical; Subterranean Biology 23; issued 2017-09-14; Crossref CC BY 4.0 vor; page prints CC BY 4.0. Crossref gives pages 19-28, the page's XML fpage 19, lpage 46; the record's 19-46 follows the page. Accepted.
- Lines 5, 6 (Neal, Paterson, Blockley, Scott, Sherlock, Huque, Glover 2020). Page and Crossref in that order; title identical; ZooKeys 938: 1-86; issued 2020-06-03; Crossref CC BY 4.0 vor. Accepted.
- Line 7 (Lee, Meißner, Yoon, Min 2021). Crossref Geon Hyeok Lee, Karin Meißner, Seong Myeong Yoon, Gi-Sik Min; title identical; ZooKeys 1070: 151-164; issued 2021-11-15; Crossref CC BY 4.0 vor. Accepted.
- Line 8 (de León-Espinosa, de León-González 2015). Page byline "Angel de León-Espinosa, Jesus A. de León-González" and citation line "de León-Espinosa A, de León-González JA (2015)"; Crossref reverses the order, as the note says; the page wins. Title identical (with "lion´s-paw"); ZooKeys 530: 129-149; issued 2015-10-29; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Line 1: Euroscaptor darwini has a Mammal Diversity Database taxon page (mammaldiversity.org/taxon/1006995, from the search result); order Eulipotyphla and family Talpidae printed in the title. Lines 2-7 are species new in the cited papers; line 8 is an existing species (Hilton 1942). Class Polychaeta for lines 2-7 and the blank orders follow the desk report; no order heading was seen on the pages (tool summary). Line 8 prints "Class Pycnogonida Latreille, 1810 Order Pantopoda Gerstäcker, 1863"; family Ammotheidae. Name faults 0.

## Duplicates

`git grep -i` on origin/main (5f4bde4d) over the whole docs/ tree for Euroscaptor, darwini, canariarum, llanetensis, christopheri, Namanereis, "Apistobranchus jasoni", jasoni, modinouae, Prosphaerosyllis, "Spio pigmentata", duodorsospinosa and the six DOI strings and article numbers. Hits: no Euroscaptor anywhere ("darwini" hits are other taxa); Namanereis, Apistobranchus, Prosphaerosyllis only in desk-d294.md's dropped list and in the note of desk-d294.jsonl line 6 (Leitoscoloplos olei, same DOI, which says these two "were not filed"); Spio pigmentata only in desk-d301.md's dropped list; zookeys.530.6064 in desk-d285.jsonl and audit-375.md (Eurycyde bamberi, another species). All other research/desk-d* remote branches grepped for the species and DOI patterns: hits only in their copies of desk-d294.jsonl (the same note). Duplicate faults 0.

## Per line

### Line 1, Euroscaptor darwini, eyes vestigial, not externally visible

Description of the holotype, External morphology, ninth sentence: "The eyes are vestigial and not externally visible, deeply recessed beneath the skin." **Quote MATCH** (the article_preview page returned the section sentence by sentence; an XML pass missed it, a tool fault). Holotype adult male, 10 November 2024, about 935 m; paratypes two females 9 April 2025 and two females 13 April 2025 (about 1007 m). Introduction "minute and concealed eyes" is genus-level and excluded, as the conditions say; Diagnosis without eye text (its "vestigial" is the tail). Value no wider than the quote; not genus-level or review-sourced.

**Line 1 MATCH.**

### Line 2, Namanereis canariarum, eyes absent

Description, returned in three consecutive pieces: "Prostomium semi-circular in shape, slightly wider than long; cleft absent, shallow dorsal hollow present;" / "two short conical frontal antennae, smooth, extending beyond tip of palpophore;" / "palps broad and globose, biarticulated, with globular palpostyles; eyes absent (Fig. 2a)." **Quote MATCH**; the stitched text is what the page prints.

Fault: the conditions place the holotype at "Gran Canaria". The page prints "Holotype: TFMCBM-AN/240, coll. J. Núñez, 8-2-2002;" with no locality, and the Type locality "Canary Islands, Fuerteventura, Las Playitas" (14 m, brackish water well); Gran Canaria (Fataga water mine) holds only the twelve non-type specimens. Locality stated against the paper. Fixable. Uncounted: "fragmented" for the paratypes was not seen on the page (not checked further).

**Line 2 FIXABLE.**

### Line 3, Namanereis llanetensis, eyes absent

Description, three pieces: "Prostomium hexagonal, two times wider than long, without a cleft but with a shallow dorsal hollow;" / "two conical frontal antennae, smooth, extending beyond the tip of palpostyle;" / "palps broad and globose, biarticulated, with globular palpostyles; eyes absent (Fig. 3a)." **Quote MATCH.** Holotype 86 chaetigers, 34 mm; "Paratypes with 83–88 chaetigers"; four paratypes, one a female with gametes (tool summary).

Fault: the conditions say "Los Llanetes, Fuerteventura". The Type locality reads "Canary Islands, Gran Canaria, Los Llanetes water mine (Valsequillo)", 415 m. Wrong island. Fixable.

**Line 3 FIXABLE.**

### Line 4, Namanereis christopheri, eyes absent

Description, two pieces: "Prostomium wider than long, anterior margin entire, groove present;" / "antennae cirriform, as long as prostomium; eyes absent (Fig. 2A, C)." **Quote MATCH.** No Diagnosis; Remarks without eyes; Abstract "shares the common morphological characters of absence of eyes and pigmentation"; key couplet 5 "Eyes present" / "Eyes absent". As filed.

Fault: the conditions give "Type material 11 specimens, holotype plus paratypes (1 and 10)". The page prints "Holotype LACM-AHF 1227 and paratypes LACM-AHF 1228 (1), and LACM-AHF 1229 (10)," which is twelve specimens. Fixable.

**Line 4 FIXABLE.**

### Line 5, Apistobranchus jasoni, eyes absent

article_preview pieces: "Prostomium bluntly rounded, wider than long, continuing posteriorly as short caruncle terminating in middle of chaetiger 1" / "(Figs 13d; 14a);" / "palps missing (notobserved);" / "eyes absent;" / "paired nuchal organs prominent, located posterior to the origin of palps (Fig. 13d)." **Quote MATCH.** "notobserved" falls inside one returned piece, not at a piece boundary, so it is printed so and not a chunking artefact.

Fault: the Description opens "Holotype (NHM.2018.12712), incomplete specimen, 6 mm long and 1 mm wide for 40 chaetigers (Fig. 13a).", so the eye clause describes the holotype; and the species account lists a long "Other materials" set of non-type specimens (63 entries, tool summary) whose eyes are not described. The conditions give only the two types. Holotype-only scope and sample composition omitted. Fixable.

**Line 5 FIXABLE.**

### Line 6, Prosphaerosyllis modinouae, four eyes (two pairs)

article_preview pieces: "Two pairsof large red eyes present (Figs 5b–d; 8a), in trapezoid arrangement," / "with anterior and posterior pair close together (almost appearing as a single eye)," / "anterior pair cup-shaped, posterior pair circular; presence of additional eyespots not confirmed." **Quote MATCH.** "pairsof" sits mid-piece in both the HTML and the XML returns, so it is printed. Four from "two pairs" is the product the note states; "not confirmed" kept.

Fault: the conditions say "a third fragment mentioned in the Description". The Description (tool summary) describes the holotype ("a complete, very small, slender specimen, 4.5 mm long"), two complete paratypes and an incomplete paratype (1.2 mm, 12 chaetigers) under NHM.2018.24236, the number also given to a complete paratype; "fragment" is not printed. The account also lists "Other materials" (non-type individuals, ten by the tool's count) not in the conditions. Sample composition misstated and omitted. Fixable.

**Line 6 FIXABLE.**

### Line 7, Spio pigmentata, four eyes (two pairs)

Description pieces: "Prostomium entire and rounded anteriorly, slightly expanded at anterolateral margin, extending to chaetiger 1;" / "prostomium with orange-brown pigmentation on anterior part, middle part of prostomium comparatively broad," / "posterior part with highly elevated papilla;" / "two pairs of black eyes arranged in trapezoid; anterior pair larger, slightly crescent-shaped or oval, widely spaced;" / "posterior pair smaller, rounded, closely spaced; weak transverse depression between anterior and middle part of prostomium" / "(Figs 3A, B, 6A, 7A)." The quote keeps the start, marks the interior cut and the trailing cut (including the figure reference) with "…"; no eye qualifier is dropped. **Quote MATCH** under the quote rule. Holotype "Complete, without palps"; paratypes 4 + 3 + 2 complete = nine; Methods "Adult specimens examined"; Diagnosis, Abstract, Discussion and Table 1 without eye text, no Remarks (tool summary). Conditions right. Uncounted: "The only new species in the paper" was not checked.

**Line 7 MATCH.**

### Line 8, Nymphopsis duodorsospinosa, four eyes

Description pieces: "A well-developed ocular tubercle inserted a little behind the anterior margin of the body," / "tall, cylindrical, ending in a conical apex, with four black eyes near the top (Fig. 2B)." **Quote MATCH.** Material 15 lots, 21 females, 29 males, 2 unsexed (tool tally, matches the conditions); Remarks "size and shape of the eye tubercle" only. Uncounted: the page heading reads "Nymphopsis duodorsospinosa Hilton, 1942c" without parentheses (tool return), while `where` adds parentheses, which would signal a genus transfer; a note fix is given.

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Euroscaptor darwini, eyes vestigial, not visible | MATCH | | holotype sentence, species-level, MDD name |
| 2 | Namanereis canariarum, eyes absent | FIXABLE | conditions | holotype placed on Gran Canaria; type locality is Las Playitas, Fuerteventura |
| 3 | Namanereis llanetensis, eyes absent | FIXABLE | conditions | Los Llanetes is on Gran Canaria, not Fuerteventura |
| 4 | Namanereis christopheri, eyes absent | FIXABLE | conditions | type series is 12, not 11 |
| 5 | Apistobranchus jasoni, eyes absent | FIXABLE | conditions | holotype-only description and non-type material omitted |
| 6 | Prosphaerosyllis modinouae, 4 eyes | FIXABLE | conditions | "third fragment" not printed; incomplete paratype and non-type material omitted |
| 7 | Spio pigmentata, 4 eyes | MATCH | | marked cuts, no qualifier dropped |
| 8 | Nymphopsis duodorsospinosa, 4 eyes | MATCH | | quote, material and Remarks right |

Stitching and typos: every rebuilt sentence (lines 2-6, 8) is what the page prints; "pairsof" and "notobserved" are printed, not tool artefacts. No quote correction needed.

Errors: 5 of 8 records (62.5%); 5 fixable (lines 2-6), 0 held out, 0 unfixable; no line to drop. All five are conditions faults; values and quotes stand. The rate is above 5%, so the unit merges by the drop-the-errors route for these lines: lines 1, 7, 8 as filed, lines 2-6 with the replacements below (or dropped if not applied). Verdict for lines 1-8: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named.

Line 2:
- `conditions`: "holotype (46 mm, 133 chaetigers, Gran Canaria, 2002, sex and maturity not stated)" -> "holotype (46 mm, 133 chaetigers, collected 8-2-2002; its entry gives no locality, and the Type locality is Las Playitas, Fuerteventura, a brackish water well at 14 m; sex and maturity not stated)"

Line 3:
- `conditions`: "(Los Llanetes, Fuerteventura, 2010)" -> "(Los Llanetes water mine, Valsequillo, Gran Canaria, 415 m, 2010)"

Line 4:
- `conditions`: "Type material 11 specimens, holotype plus paratypes (1 and 10)" -> "Type material 12 specimens, holotype plus paratypes (1 and 10)"

Line 5:
- `conditions`: "the paratype's eyes are not described separately." -> "the Description is of the holotype ('Holotype (NHM.2018.12712), incomplete specimen, 6 mm long and 1 mm wide for 40 chaetigers'), and the paratype's eyes are not described separately. A long list of non-type 'Other materials' is given; their eyes are not described."

Line 6:
- `conditions`: "(holotype and two paratypes listed, a third fragment mentioned in the Description, so the count is ambiguous)" -> "(holotype and two paratypes listed; the Description also describes an incomplete paratype, 1.2 mm with 12 chaetigers, under the catalogue number it gives a complete paratype, so the count is ambiguous; a further list of non-type 'Other materials' is given, eyes not described)"

Line 8 (uncounted):
- `where`: "Nymphopsis duodorsospinosa (Hilton, 1942c)" -> "Nymphopsis duodorsospinosa Hilton, 1942c"
