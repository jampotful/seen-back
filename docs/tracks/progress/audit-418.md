# audit-418: desk-d313, file lines 1-8 (Phylliidae)

Audited 1 November 2026 from the desk-d313 files present untracked in the worktree (docs/tracks/progress/desk-d313.md and docs/views/evidence/desk-d313.jsonl; neither committed here, neither edited). HEAD equals origin/main (f1569e4f4). Lines 9-16 belong to another auditor. `python3 -I tools/senses/check.py | grep d313`: "docs/views/evidence/desk-d313.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1-8: 22, 16, 23, 16, 18, 18, 16, 16, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=104413 (five passes), ?id=61033 (three passes), ?id=80808 (one pass); phasmida.speciesfile.org otus 852808, 852810, 852809, 852861, 852849 (and two unrelated otus pages); en.wikipedia.org/wiki/Cryptophyllium and /Vaabonbonphyllium (species lists citing Phasmida Species File). Crossref single-DOI lookups api.crossref.org/v1/works/ for 10.3897/zookeys.1173.104413, 10.3897/zookeys.1018.61033 and 10.3897/zookeys.1110.80808 each returned on the first call (no PROVENANCE_REQUIRED for these three). PMC, DOAJ, Plazi, BHL, the RBINS PDF, reviewer.ly and library catalogue records were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns pieces of about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Lines 1-5 (ZooKeys 1173). Byline and citation line "Cumming RT, Le Tirant S, Linde JB, Solan ME, Foley EM, Eulin NEC, Lavado R, Whiting MF, Bradler S, Bank S (2023)" identical in order to the record and to Crossref. Title with printed curly quotes as recorded. "ZooKeys 1173: 145-229"; Crossref volume 1173, page 145–229, issued 2023. Licence: page prints "This is an open access article distributed under the terms of the CC0 Public Domain Dedication."; Crossref licence creativecommons.org/share-your-work/public-domain/cc0/, vor. No conflict; accepted under the d313 ruling.
- Lines 6-7 (ZooKeys 1018). Byline/citation "Cumming RT, Bank S, Bresseel J, Constant J, Le Tirant S, Dong Z, Sonet G, Bradler S (2021)" identical in order to record and Crossref; "ZooKeys 1018: 1-179"; Crossref 1018, 1-179, issued 2021. Licence CC0 sentence on page, Crossref CC0 vor; accepted. **Title fault**: the page title and citation line print "Cryptophyllium, the hidden leaf insects – descriptions of a new leaf insect genus and thirteen species from the former celebicum species group (Phasmatodea, Phylliidae)" (en dash, Crossref identical); the record has "hidden leaf insects: descriptions". One error in each of lines 6 and 7, fixable.
- Line 8 (ZooKeys 1110). Byline "Royce T. Cumming, Stéphane Le Tirant"; citation "Cumming RT, Le Tirant S (2022) ... ZooKeys 1110: 151-200."; title identical; Crossref 1110, 151–200, 2022. Licence CC0 on page, Crossref CC0 vor; accepted.

The unit's statement that Crossref was unreadable is true for its own attempts; the auditor's lookups returned, and nothing in them conflicts with the records apart from the line 6-7 title punctuation, which the page shows too.

## Names, higher taxa, trait key

- Phasmida Species File: Phyllium samarense (852808), P. ortizi (852810), P. iyadaon (852809) and Cryptophyllium animatum (852861) open as valid, no synonyms. Cryptophyllium bankoi and Vaabonbonphyllium rafidahae were not reached on PSF directly; both are in the PSF-cited species lists on Wikipedia (Cryptophyllium 24 species, matching the PSF genus page's "24 valid extant species"; Vaabonbonphyllium groesseri and rafidahae) with no synonymy. Accepted.
- Order Phasmatodea and family Phylliidae are printed in all three titles; none of the three pages prints a class line (tool summary for 1173 and 1018; line 8's note says the XML prints Order/Family, which the preview page does not show as a block but the title carries). Class blank is right.
- eye_type: main carries 307 eye_type records, including morphological descriptions in the same style (e.g. "eye moderate in size, 1.7-2.6 (2.4 in holotype) times in snout length"; "compound eye subrectangular, with three lobes on terminal margin" for Sarsinebalia agoensis). These values fit the key; no owner question.

## Repeats

`git grep -il` on origin/main (f1569e4f4) over the whole docs/ tree for samarense, ortizi, iyadaon, animatum, bankoi, Vaabonbonphyllium, rafidahae, Phyllium, Phylliidae, zookeys.1173, zookeys.1018, zookeys.1110, 104413, 61033, 80808. Hits: desk-d312.md (P. samarense / ZooKeys 1173 only as a licence question), desk-d299.md (ZooKeys 1173 for a different paper, Echinogammarus ozbeki), and "80808" only as unrelated numeric substrings in audit/corrected and searched files. No evidence, sheet or corrected record. All 312 unmerged origin/research/desk-d* branches other than d313 grepped in one `git grep -il -E` over docs/ for the six species and three DOIs, excluding d312/d299 progress files inherited from main: completed, no hits. No repeats.

## Per line

### Line 1, Phyllium samarense, female, eyes ca ¼ of lateral margins

Female Head: "Compound eyes not strongly protruding from the head capsule and take up ca ¼ of the head capsule lateral margins (Fig. 4C)." **Quote MATCH**, 22 words. Holotype "Holotype ♀: “Philippines: Eastern Visayas, Northern Samar, Lope De Vega: April, 2017; Coll RC 17-206; DNA ID #W9”", IMQC; paratypes "(9 ♀♀, 6 ♂♂, 1 ♂ nymph, 2 ♀♀ nymphs, 6 eggs)" as recorded. "Ocelli absent." follows. Remarks on variation are about abdominal shape, as the record says. Not counted: Figure 4 panels A and C-G are a paratype female (holotype only panel B, tool summary), so the head figured with the quote is a paratype; and female coloration is "based upon living individuals in which some variation has been observed". Optional fix below.

**Line 1 MATCH.**

### Line 2, Phyllium samarense, male, large and bulbous, ca ⅖

Male Head: "Compound eyes large and bulbous, occupying ca ⅖ of the head capsule lateral margins (Fig. 5C)." **Quote MATCH**, 16 words; ocelli sentence as recorded. Male material: "Measurements of paratype males [mm]."; Figure 5 is "male paratype, Coll RC #16-259" (tool summary); holotype is the female. "Rests on paratype males" confirmed. Not counted: Remarks say "As in other Phyllium species, despite females having variable abdominal shapes, the males so far observed have all been uniform in their morphology (Fig. 3C)." and male coloration is "based upon living individuals"; optional fix.

**Line 2 MATCH.**

### Line 3, Phyllium ortizi, female, slightly protruding, ca ⅖

Female Head, returned in two pieces: "Compound eyes slightly protruding from the head capsule, not overly bulbous, taking up ca ⅖ of the head capsule" / "lateral margins (Fig. 11C)." **Quote MATCH**, 23 words. Holotype "Holotype ♀: “Philippines, Mindanao, Lanao Del Sur, Wao, February 2019; Collection SLT; DNA no. 35”", deposited IMQC; paratypes "(5 ♀♀, 14 ♂♂, 2 ♀♀ nymphs, 99 eggs)".

Fault: **colony origin omitted.** The female material behind the description is largely captive-reared: "Coloration description is based upon living individuals in culture (Fig. 10A, B, E).", "Within captive cultures a few individuals have expressed significant coloration variations.", "Measurements of paratype females [mm] (ex culture)."; Figure 11 panels other than D are a paratype (Coll RC), so the head in Fig. 11C is a paratype, not the wild holotype (tool summary). The conditions name only the holotype and paratype counts. One error, fixable.

**Line 3 FIXABLE.**

### Line 4, Phyllium ortizi, male, large and bulbous, ca ⅖

Male Head: "Compound eyes large and bulbous, occupying ca ⅖ of the head capsule lateral margins (Fig. 12C)." **Quote MATCH**, 16 words; ocelli sentence as recorded. Male description rests on paratypes, as recorded (Figure 12 "male paratypes", A-D Coll RC 21-001, tool summary).

Fault: **colony origin omitted.** "Measurements of paratype males [mm] (ex culture)." and "Coloration description is based upon living specimens in captivity (Fig. 10A, C, D)."; the paratype localities are in Suppl. material 1. The male eye record therefore rests on culture-reared paratype males, which the conditions do not say. One error, fixable.

**Line 4 FIXABLE.**

### Line 5, Phyllium iyadaon, male, slightly < ½

Male Head: "Compound eyes are large and bulbous, occupying slightly < ½ of the head capsule lateral margins (Fig. 9B)." **Quote MATCH**, 18 words. "Holotype ♂: “Philippines: Mindoro, Puerto Galera: April, 2017; Coll RC 17-221”", "Paratype: (1♂) • “Philippines: Mindoro, Puerto Galera: April, 2017; Coll RC 17-222”", "Female, freshly hatched nymph, and egg unknown.", measurements of holotype and paratype male separately; Fig. 9 A-E is the holotype male, so Fig. 9B is the holotype head. Ocelli sentence as recorded. No eye text in Differentiation. Right.

**Line 5 MATCH.**

### Line 6, Cryptophyllium animatum, male, > ⅓

Male Head: "Compound eyes large but not overly bulbous, occupying > ⅓ of the head capsule lateral margins (Fig. 10C)." **Quote MATCH**, 18 words. Heading prints "gen. et, sp. nov."; holotype male "VIETNAM: Quang Nam, Tay Giang, Axan Mt, 1,300 meters: July 2017 (Coll RC 17-261)", IMQC; no paratypes; "Females unknown."; "Measurements of holotype male [mm]."; Figure 10 is the holotype. Ocelli sentence as recorded. Generic characteristics, Differentiation and key carry no eye text (tool summary). Content right; title punctuation wrong (above).

**Line 6 FIXABLE** (title).

### Line 7, Cryptophyllium bankoi, male, ca. ⅖

Male Head: "Compound eyes large and bulbous, occupying ca. ⅖ of the head capsule lateral margins (Fig. 14B)." **Quote MATCH**, 16 words. Holotype male "VIETNAM: Quang Nam, Tay Giang, Axan Mt, 1,300 meters: June 2017, Coll RC 17-228", IMQC; Figure 14 holotype; measurements of holotype male; "Females unknown."; paratypes "(4 ♂♂, 1 ♂ nymph, 1 ♀ nymph)" with adult males from Daknong 2017, Bato Mt 2015, Ba Na-Nui Chua 2017 and Ngoc Linh 2016. Not counted: the nymphs are listed individually as "1 subadult ♀" (Bach Ma, 2011) and "1 subadult ♂" (Kon Chu Rang, 2018); optional fix. Title punctuation wrong (above).

**Line 7 FIXABLE** (title).

### Line 8, Vaabonbonphyllium rafidahae, male, ca. ⅖

Male Head: "Compound eyes large and bulbous, occupying ca. ⅖ of the head capsule lateral margins (Fig. 12G)." **Quote MATCH**, 16 words. "Holotype ♂", IMQC, label Mt. Hagen, Highlands Hwy., 1730 m, 23-VI-1989, L D. Munsey, Coll RC 19-106; no paratypes; "Females unknown."; "Measurements of holotype male [mm]"; Figure 12 is the holotype. Ocelli sentence as recorded. Not counted: Generic characteristics also say "Males have compound eyes which are strongly protruding and occupy ca. 2/5 of the head capsule lateral margins (Fig. 11C)", figured on another species; consistent with the value, optional addition.

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | P. samarense female, ca ¼ | MATCH | | quote, type data right; figured head is a paratype (optional) |
| 2 | P. samarense male, ca ⅖ | MATCH | | paratype males confirmed |
| 3 | P. ortizi female, ca ⅖ | FIXABLE | conditions | culture-reared female paratypes (coloration, measurements, Fig. 11C) omitted |
| 4 | P. ortizi male, ca ⅖ | FIXABLE | conditions | male paratypes "ex culture"/"in captivity" omitted |
| 5 | P. iyadaon male, < ½ | MATCH | | holotype figured and measured |
| 6 | C. animatum male, > ⅓ | FIXABLE | source.title | ": descriptions" for printed " – descriptions" |
| 7 | C. bankoi male, ca. ⅖ | FIXABLE | source.title | same title fault |
| 8 | V. rafidahae male, ca. ⅖ | MATCH | | holotype only, figured and measured |

Errors: 4 of 8 records (50%); 4 fixable (lines 3, 4, 6, 7), 0 held out, 0 unfixable; no line to drop. Quotes 8 of 8 verbatim. Repeats: none. Licences: CC0 on page and in Crossref (vor) for all three papers. Verdict for desk-d313 lines 1-8: **ACCEPT AFTER REPLACEMENT** (lines 1, 2, 5, 8 as filed; lines 3, 4, 6, 7 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 3:
- `conditions`: "paratypes 5 females, 14 males, 2 female nymphs, 99 eggs." -> "paratypes 5 females, 14 males, 2 female nymphs, 99 eggs (paratype localities in Suppl. material 1, not read). Much of the female material is captive-reared: 'Coloration description is based upon living individuals in culture (Fig. 10A, B, E).', 'Measurements of paratype females [mm] (ex culture).', and the head figured with the quote (Fig. 11C) is a paratype, not the holotype (Fig. 11D)."

Line 4:
- `conditions`: "so the male description rests on paratype males." -> "so the male description rests on paratype males, and these are culture-reared: 'Measurements of paratype males [mm] (ex culture).' and 'Coloration description is based upon living specimens in captivity (Fig. 10A, C, D).' The figured head (Fig. 12C) is paratype Coll RC 21-001."

Line 6:
- `source.title`: "hidden leaf insects: descriptions" -> "hidden leaf insects – descriptions"

Line 7:
- `source.title`: "hidden leaf insects: descriptions" -> "hidden leaf insects – descriptions"

Optional, not counted:
- Line 1 `conditions`: "(collection data in Suppl. material 1, not read)." -> "(collection data in Suppl. material 1, not read). The head figured with the quote (Fig. 4C) is a paratype female; only Fig. 4B is the holotype. Female coloration is 'based upon living individuals in which some variation has been observed.'"
- Line 2 `conditions`: "so the male description rests on paratype males." -> "so the male description rests on paratype males (Fig. 5 is male paratype Coll RC #16-259; male coloration 'based upon living individuals'). The Remarks say 'the males so far observed have all been uniform in their morphology (Fig. 3C).'"
- Line 7 `conditions`: "1 male nymph and 1 female nymph." -> "1 male nymph and 1 female nymph (listed as a subadult female from Bach Ma, 2011, and a subadult male from Kon Chu Rang, 2018)."
- Line 8 `conditions`: "based on a different species (V. groesseri);" -> "based on a different species (V. groesseri), and also say 'Males have compound eyes which are strongly protruding and occupy ca. 2/5 of the head capsule lateral margins (Fig. 11C)';"
- Lines 1-8 `note`: the Crossref sentence may say that the auditor's lookups returned: CC0 vor licence, volume and pages as recorded.
