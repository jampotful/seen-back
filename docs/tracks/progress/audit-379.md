# audit-379: desk-d290, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d290 files present untracked in the worktree (docs/tracks/progress/desk-d290.md and docs/views/evidence/desk-d290.jsonl, 7 lines; neither committed here, neither edited). Worktree HEAD and origin/main 065e5c18 (Merge desk d289 (6 records) after audit 378). `python3 -I tools/senses/check.py | grep 'd290\.'`: "docs/views/evidence/desk-d290.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 4, 7, 7, 3, 2, 3, 3, all within 40; no quote contains a non-ASCII character. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all seven DOIs (49.135303 and 52.142113 rate-limited once, answered on retry); subtbiol.pensoft.net/article/79447/download/xml/ (two passes); subtbiol.pensoft.net/article_preview.php?id=184889 (the search returned the preview, not the XML; same article); zookeys.pensoft.net/article/176622/download/xml/ (two passes); subtbiol.pensoft.net/article/135303/download/xml/; subtbiol.pensoft.net/article/142113/download/xml/ (two passes); subtbiol.pensoft.net/article/188589/download/xml/; subtbiol.pensoft.net/article_preview.php?id=98075. All URLs were returned by a WebSearch first. PMC, Plazi, Zenodo, BHL, DOAJ, core.ac.uk, novataxa and university repository hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Malek-Hosseini et al. 2022). Crossref: Mohammad Javad Malek-Hosseini, Jure Jugovic, Yaser Fatemi, Matjaž Kuntner, Rok Kostanjšek, Christophe J. Douady, Florian Malard; title identical; Subterranean Biology 42, 97-124, no issue; issued 2022-03-11; CC BY 4.0 vor. Page byline in the same order; licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Line 2 (Jugovic et al. 2026). Crossref: Jure Jugovic, Mohammad-Javad Malek Hosseini, Yaser Fatemi, Jean-François Flot, Matjaž Kuntner, Valerija Zakšek; title identical; SB 55, 137-160; issued 2026-03-23; CC BY 4.0 vor. Page byline same order; licence sentence verbatim (CC BY 4.0). Accepted.
- Line 3 (Jugovic, Fišer, Zagmajster, Delić, Zakšek 2026). Crossref: same five in that order; title one string as in the record; ZooKeys 1267, 51-76; issued 2026-01-22; CC BY 4.0 vor. Page byline same; licence verbatim (CC BY 4.0); the page sets "named through public participation" apart (tool summary), as the note says. Accepted.
- Line 4 (Watiroyram, Koompoot 2024). Crossref: Santi Watiroyram, Kamonwan Koompoot; title identical; SB 49, 185-200; issued 2024-10-29; CC BY 4.0 vor. Page citation verbatim "Watiroyram S, Koompoot K (2024)."; licence verbatim (CC BY 4.0). Accepted.
- Line 5 (Rossetti, Sarbu, Ștefan, Motoc, Mazzini 2025). Crossref: same order; title identical; SB 52, 111-133; issued 2025-06-03; CC BY 4.0 vor. Crossref spells "Ştefan" with a cedilla; the page prints "Ștefan" with comma below (tool summary), and the record follows the page. Licence verbatim (CC BY 4.0). Accepted.
- Line 6 (Rossetti, Ștefan, Motoc, Sarbu, Mazzini 2026). Crossref: same order; title identical; SB 56, 137-159; issued 2026-06-01; CC BY 4.0 vor. Page byline verbatim "Giampaolo Rossetti, Andrei Ștefan, Rozalia Motoc, Serban M. Sarbu, Ilaria Mazzini"; licence verbatim (CC BY 4.0). Accepted.
- Line 7 (Külköylüoğlu, Ataman, Gibson, Diaz 2023). Crossref: Okan Külköylüoğlu, Alper Ataman, Randy Gibson, Peter Diaz; title identical; SB 45, 119-140; issued 2023-03-21; licence creativecommons.org/share-your-work/public-domain/cc0/ vor. Page verbatim "This is an open access article distributed under the terms of the CC0 Public Domain Dedication." CC0 rule met (dedication printed, no conflicting Crossref tag). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No checklist reached; all seven species are described as new in the cited papers, so the names rest on the original descriptions, as the desk says.

- Asellus ismailsezarii: Isopoda, Asellidae from the classification block and title. Met.
- Caridina tashanica, Spelaeocaris electa: Decapoda, Atyidae in the classification block (the ZooKeys title/abstract tag treats Decapoda at another rank, tool summary; the block's order is used). Met.
- Siamcyclops isanus: verbatim "Order Cyclopoida Burmeister, 1834", "Family Cyclopidae Rafinesque, 1815". Met.
- Mixtacandona thessalica: verbatim "Order Podocopida G.O. Sars, 1866", "Family Candonidae Kaufmann, 1900" (subfamily Candoninae not used). Met.
- Pseudocandona sulphurella: Podocopida, Candonidae (tool summary). Met.
- Tuberocandona leonidasi: verbatim "Order: Podocopida Sars, 1866", "Family: Candonidae Kaufmann, 1900". Met.

Name faults 0.

## Duplicates

git grep on origin/main (065e5c18) across the whole docs/ tree for ismailsezarii, tashanica, Spelaeocaris electa, Siamcyclops, Mixtacandona, Pseudocandona, sulphurella, Tuberocandona, leonidasi and the seven article ids: no species hits; "79447" only as a number inside docs/views/searched/desk-c8.jsonl and harvest-c23.jsonl (plant genus search logs), "98075" only inside a GBIF id in docs/views/no-view-us-fl-alachua.csv. Asellus on main appears only in desk-d280.md and the crab sheet (other species); Caridina rows on main are other species (C. zhaoi, C. incolor, per audits 372 and 374). Remote research/desk-* and research/audit-* branches (762) grepped under docs/ for the seven species, the genera Spelaeocaris, Siamcyclops, Mixtacandona, Tuberocandona and the seven DOIs: no file hits on any branch other than research/desk-d290 (whose files are untracked here).

Duplicates 0.

## Per-record findings

### Line 1, Asellus ismailsezarii, eye_type none

Under heading verbatim "Description of holotype and male type material", the sentence "No eye structures visible." stands between the frontal-margin sentence ("...each with small posterolateral protuberance, with few small, short stiff setae.") and "Pereonites (Fig. 3B) I–III with straight to slightly convex lateral margins..." **Quote MATCH**. Diagnosis of male verbatim "with depigmented body and complete loss of eyes"; Abstract "the first eyeless and depigmented asellid isopod from Iran". Holotype "mature male, body length (BL) 8.2 mm (TU-SP.1)"; paratypes verbatim "2 mature males, BL 8.2 mm (TU-SP.2), BL 6.5 mm (TU-SP.5), 1 juvenile male, BL 7.3 mm (TU-SP.7);" and "3 mature females, BL 8.1 mm (TU-SP.3), BL 8.1 mm (TU-SP.4), BL 6.7 mm (TU-SP.6);". Conditions match. No eye variation statement (tool summary). Value "none (no eye structures visible)" keeps the quote's wording.

Uncounted: the note says "The abstract notes that surface populations of the genus have evolved loss of eyes." The Abstract reads verbatim "Surface populations of Asellus have colonized groundwater at multiple occasions and localities, both in Europe and Asia," "giving rise to species and subspecies that have evolved troglomorphisms, such as depigmentation and loss of eyes." The eye loss belongs to the groundwater-derived species, not the surface populations. Replacement below.

**Line 1 MATCH.**

### Line 2, Caridina tashanica, eye_type eyestalks short, unpigmented

Under "Description of male holotype", run-in "Cephalothorax and cephalic appendages": "Eyestalks still present but short, without pigmentation." **Quote MATCH**. Holotype verbatim "male, CL 3.19 mm (voucher number TB483)"; paratypes verbatim "2 males and 1 female – male CL 4.17 (TB484) and 2.88 (TB485), female CL 3.86 mm (TB486)". Other eye text: Abstract "Morphologically, the new species is characterised by reduced eyes and pigmentation"; Diagnosis "(depigmented and with strongly reduced eyes without pigmentation; Fig. 6)"; Remarks "whereas in Caridina tashanica sp. nov. both eye and body pigment are lacking."; Discussion "The new species can be readily distinguished from all its Middle Eastern congeners by complete depigmentation, lack of eyes". The value says no more than the quote and the note flags the absence of cornea information.

Uncounted: the note mentions the Abstract's "reduced eyes" but not the Discussion's "lack of eyes", which a reader would want beside an eyestalks-present value. Replacement below.

**Line 2 MATCH.**

### Line 3, Spelaeocaris electa, eye_type eyestalks short, unpigmented

Under "Description of male holotype (first reported value) and other material (values in parentheses, where available)", subsection "Cephalothorax and cephalic appendages": "Eyestalks are present but short and unpigmented." (preceded by "The carapace surface is smooth and depigmented.") **Quote MATCH**. Diagnosis "(depigmented and blind)". Holotype adult male TB362, Buljovica, 14 March 2021. Type material on the page: allotype verbatim "adult female CL 6.6 mm (TB361), collection data same as holotype."; paratypes "2 adult males and 1 subadult male" (TB379, TB380, TB287; tool summary for the summary line); other material includes verbatim "6 adult females, 2 subadult females, 2 juvenile females". The Description gives female values ("♀♀ 6.2–7.5 mm (n = 7)").

Uncounted: the conditions say "the paratype sexes were not settled on the page read". The page settles them (allotype female; paratypes 2 adult males, 1 subadult male; other material includes females). Not counted, since the record flags its own gap and says nothing false. Replacement below.

**Line 3 MATCH.**

### Line 4, Siamcyclops isanus, eye_type nauplius eye indiscernible

Under "Description of adult female": "Nauplius eye indiscernible." **Quote MATCH**. "Description of adult male." has no eye sentence (tool summary). Holotype verbatim "one adult female dissected and mounted on one slide, THNHM-IV-20465."; allotype "one adult male dissected and mounted on one slide, THNHM-IV-20466."; paratypes of both sexes. Conditions match; eye key "nauplius eye" fits a copepod.

**Line 4 MATCH.**

### Line 5, Mixtacandona thessalica, eye_type none

Description, paragraph opening "Soft parts. A1 (Fig. 4A): ...": "Zenker organ (Fig. 5E): thin and with 5+2 spinous whirls." then "Eye absent." then "Other appendages as typical for the genus Mixtacandona." **Quote MATCH**. The paragraph covers both sexes inline (verbatim "A2 ♀ (Figs 4C, 6D): endopodite three-segmented (second segment undivided);"); no sex subheadings. Genus diagnosis verbatim "Eye pigment absent." Holotype "adult ♂ (GR972–MZUF691)"; paratypes 2 adult ♂, 2 adult ♀ numbered and "two adult ♂♂ and two adult ♀♀ stored in toto in ethanol (no numbers)". Value "none (eye absent)" is the quote's "absent", for an ostracod's eye (not eye spot). Conditions match.

**Line 5 MATCH.**

### Line 6, Pseudocandona sulphurella, eye_type eye not visible

"Eye not visible." is the last sentence of the Description, after the female genital lobe sentence and before Differential diagnosis (tool summary for context). **Quote MATCH**. No sex subheadings. Holotype adult ♂ MUST-GR1072; allotype adult ♀ MUST-GR1120; paratypes 4 adult ♂, 2 adult ♀, three adults of undetermined sex. Value keeps "not visible".

Uncounted: the conditions omit the allotype female. Replacement below.

**Line 6 MATCH.**

### Line 7, Tuberocandona leonidasi, eye_type eyes not visible

Description > Male, opening verbatim "Male: Measurements (based on midlength). L=0.51–0.56 mm, H=0.24–0.27 mm, W=0.20–0.28 mm (n=4)."; "Four large and one small central and two ventral muscle scars located about the center between the tubercles (Fig. 2F)." then "Eyes not visible." **Quote MATCH**, only eye sentence in the paper (tool summary). Type material: holotype adult male, allotype adult female (dissected), paratypes verbatim "Two ♂ (OK-TX-BCo-4) and two ♀ (OK-TX-BCo-5) mounted and sealed in glass slides." Value keeps "not visible"; male-only stated.

Uncounted: the conditions omit the allotype female. Replacement below.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Asellus ismailsezarii, none | MATCH | none | quote MATCH (4); holotype + male type material, paratypes stated; note paraphrase fix uncounted |
| 2 | Caridina tashanica, eyestalks short, unpigmented | MATCH | none | quote MATCH (7); male holotype heading, type series stated |
| 3 | Spelaeocaris electa, eyestalks short, unpigmented | MATCH | none | quote MATCH (7); paratype sexes settle-able, uncounted fix |
| 4 | Siamcyclops isanus, nauplius eye indiscernible | MATCH | none | quote MATCH (3); female holotype description only, stated |
| 5 | Mixtacandona thessalica, none | MATCH | none | quote MATCH (2); paragraph covers both sexes |
| 6 | Pseudocandona sulphurella, eye not visible | MATCH | none | quote MATCH (3); not sex-specific; allotype omitted, uncounted |
| 7 | Tuberocandona leonidasi, eyes not visible | MATCH | none | quote MATCH (3); CC0 printed and in Crossref; allotype omitted, uncounted |

Errors 0 of 7 audited records (0%). By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. The audit covered the whole unit; nothing is held out. Verdict: merge all seven lines (the uncounted replacements below are optional).

Unchecked: no checklist entry for any species; figures not viewed; the Pseudocandona context sentences, the Spelaeocaris paratype summary line and the absence of male eye sentences in lines 4 and 7 rest on tool summaries.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). All uncounted.

Line 1:
- `note`: "The abstract notes that surface populations of the genus have evolved loss of eyes." -> "The Abstract says surface populations of Asellus colonized groundwater, giving rise to species and subspecies that evolved loss of eyes."

Line 2:
- `note`: "The paper's Abstract describes reduced eyes and reduced pigmentation in a sentence too long to quote." -> "The paper's Abstract describes reduced eyes and reduced pigmentation in a sentence too long to quote; the Discussion distinguishes the species by 'complete depigmentation, lack of eyes'."

Line 3:
- `conditions`: "and the paratype sexes were not settled on the page read" -> "and the type series is allotype adult female (TB361) and paratypes 2 adult males and 1 subadult male, other material includes adult, subadult and juvenile females"

Line 6:
- `conditions`: "holotype adult male (MUST-GR1072); paratypes include" -> "holotype adult male (MUST-GR1072); allotype adult female (MUST-GR1120); paratypes include"

Line 7:
- `conditions`: "the page says two male and two female specimens were mounted as paratypes" -> "allotype adult female; the page says two male and two female specimens were mounted as paratypes"
