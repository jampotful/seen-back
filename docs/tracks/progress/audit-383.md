# audit-383: desk-d292, evidence lines 9 to 15

Audited 1 November 2026 from the desk-d292 files present untracked in the worktree (docs/tracks/progress/desk-d292.md and docs/views/evidence/desk-d292.jsonl, 15 lines; neither committed here, neither edited). Lines 1 to 8 belong to audit 382. Worktree HEAD and origin/main 14e50fbb (Merge desk d290 (7 records) after audit 379). `python3 -I tools/senses/check.py | grep 'd292\.'`: "docs/views/evidence/desk-d292.jsonl: 15 records, 0 problems". Quote lengths (`len(q.split())`) for lines 9-15: 6, 4, 9, 9, 10, 10, 10, all within 40; the only non-ASCII character is the en dash in line 10's "Figs 10–12", which the page prints. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for the three DOIs; zookeys.pensoft.net/article_preview.php?id=29029 (two passes); bdj.pensoft.net/article_preview.php?id=103265; arthropod-systematics.arphahub.com/article_preview.php?id=106948 (two passes); wsc.nmbe.ch/refincluded/17436 (names). All URLs were returned by a WebSearch first. Plazi, Zenodo, optimap, bionames, GBIF, novataxa, university repository and catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

Page identity (the desk reported three ids returning a previous page's text: 24432, 38967, 38653, none of them cited in lines 9-15): each page fetched printed the cited title, citation line and DOI, and the treatments named in the records. The ZooKeys 29029 page is the Cyprus Dysderidae paper; the BDJ 103265 page is the Troglocoelotes paper; the ASP 106948 page is the Typhlonesticus paper. No stale text.

## Bibliographic and licence

- Lines 9-10 (Gücel, Charalambidou, Göçmen, Kunt 2019). Crossref: Salih Güçel, Iris Charalambidou, Bayram Göçmen, Kadir Boğaç Kunt; title identical; ZooKeys 825, 43-53, no issue; issued 2019-02-18; CC BY 4.0 vor. Page citation verbatim "Citation: Gücel S, Charalambidou I, Göçmen B, Kunt KB (2019) New data of spiders (Arachnida, Araneae) of Cyprus." and "1. Dysderidae found in caves. ZooKeys 825: 43-53."; byline "Salih Gücel" (Crossref spells Güçel; the record follows the page). Licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Line 11 (Zhou, Ye, Zhao 2023). Crossref: Guchun Zhou, Ru-rui YE, Zhe Zhao; title identical; Biodiversity Data Journal 11, e103265, no issue; issued 2023-07-14; CC BY 4.0 vor. Page byline same order; licence verbatim (CC BY 4.0). Accepted.
- Lines 12-15 (Isaia, Nicolosi, Infuso, Ribera 2023). Crossref: Marco Isaia, Giuseppe Nicolosi, Alessandro Infuso, Carles Ribera; title identical; Arthropod Systematics & Phylogeny 81, 801-818 (article number e106948), no issue; issued 2023-11-02; CC BY 4.0 vor. Page citation verbatim "Arthropod Systematics & Phylogeny 81: 801-818." (page range form, as the record files it); licence verbatim (CC BY 4.0). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All five species are described as new in the cited papers; names rest on the original descriptions. The World Spider Catalog reference page for Isaia et al. 2023 lists "Typhlonesticus angelicus Isaia & Ribera, 2023" and "Typhlonesticus santinellii Isaia & Ribera, 2023" as original descriptions (current status not shown on that page, tool summary). Families: verbatim "Family Dysderidae C.L. Koch, 1837" (lines 9-10); Agelenidae (Coelotinae as subfamily, not filed as family) from the BDJ title (line 11); Nesticidae from the ASP title (lines 12-15); Araneae the order throughout. Name faults 0.

## Trait key

eye_type is on main. eye_diameter_mm (lines 14-15) is not in TRAITS; it is used on the unmerged desk-d291 branch, and both lines flag it as a new trait. Uncounted: d291 files one eye per record with a numeric value; lines 14-15 file four eyes as one string ("AME 0.03; ALE 0.05; ..."), which a numeric reader cannot use. The merge step should decide whether to split them into four records each; not an error under any written rule.

## Duplicates

git grep on origin/main (14e50fbb) across the whole docs/ tree for kibrisensis, Dysderocrates, kalavachiana, Troglocoelotes, sinanensis, Typhlonesticus, angelicus, santinellii, the three DOIs and the article ids 29029, 103265, 106948: "sinanensis" only as Caridina sinanensis (desk-d290.md, audit-372.md); Typhlonesticus only as T. gocmeni (desk-d287, audit-376, desk-queue); "29029" only as a number inside unrelated rows (gbif-names.tsv, sweep-58, wanted-merged.csv, harvest-c11). All 676 remote research/desk-* and research/audit-* branches other than desk-d292 grepped in one pass under docs/views/evidence, docs/tracks/progress, docs/views/audit, docs/views/sheets and docs/views/searched for the five species and three DOIs: no file hits. Duplicates 0.

## Per-record findings

### Line 9, Dysderocrates kibrisensis, eye_type well developed

Under "Description of holotype": "Carapace red, smooth. Cephalic region much narrower and darker than thoracic region (Fig. 2)." then "Eyes well developed (Figs 2, 3)." then "Chelicerae blackish red." **Quote MATCH**. Holotype verbatim "Holotype ♀ (NMNU); CYPRUS, Lefkoşa, Beşparmak Mountains, Beşparmak (Pentadactylos) Cave" ... "collected as a dead specimen inside the cave, ca 40 m from the cave entrance, 15.I.2018, leg. S. Gücel."; "Male unknown." No other eye sentence (only the figure label "Eyes", tool summary). Conditions and note match.

**Line 9 MATCH.**

### Line 10, Harpactea kalavachiana, eye_type reduced

Under "Description of holotype": "Carapace with short blackish setae, fovea distinct." then "Eyes reduced (Figs 10–12)." then "Chelicerae and cheliceral fangs light brown." **Quote MATCH**. Holotype verbatim "Holotype ♀ (NMNU); CYPRUS Lefkoşa, Kalavaç Village, Saray (Palace) Cave" ... "hand collecting, 521 m, 14.VII.2017, leg. K.B. Kunt."; "Male unknown."

Uncounted: Comments say verbatim "The eyes of H. kalavachiana sp. n. are reduced, and the AME are distant from each other, much more than average (Fig. 11).", after "Most Harpactea species have six well-developed eyes," (sentence cut by the tool). Consistent with the value; the note omits it. Replacement below.

**Line 10 MATCH.**

### Line 11, Troglocoelotes sinanensis, eye_type strongly degenerated (reduced to white spots)

Under "Description", "Female (holotype)": "Abdomen 3.19 long, 2.15 wide; yellowish and covered with numerous fine hairs." then "Eyes strongly degenerated, reduced to white spots (Fig. 3D)." then "Clypeus height 0.31." **Quote MATCH**. Holotype female GZTR-230102-1, Huangjin Cave, Gaofeng Village, Sunjiaba Town, Sinan County, 2 January 2023; no other specimens; "Male: Unknown." (tool summary for the type block). Taxon discussion verbatim "The degenerated eyes and the pale body of Troglocoelotes sinanensis sp. nov. shows that it is a species well-specialised to subterranean life." Value keeps the quote's two qualifiers; "troglobitic" is in the title.

**Line 11 MATCH.**

### Line 12, Typhlonesticus angelicus, eye_type reduced, depigmented, no corneal lenses visible

Under "Description of the female" (holotype), Prosoma: "Eyes reduced and depigmented, no corneal lenses are visible." **Quote MATCH**. Also "AME reduced to a small spot of pigment." (in the note). Male paratype (Grotta dei Partigiani della Tura) verbatim "Reduced and depigmented eyes. No corneal lenses visible.", as conditions quote. Holotype female, Grotta Superiore delle Camoscere, 3.XII.2018; paratypes verbatim include "1f (MCSNB)", "1 juv. (CI)", "1f (CI)", "1m", "1m, 2juv. (CI)". Conditions match.

**Line 12 MATCH.**

### Line 13, Typhlonesticus santinellii, eye_type reduced, lacking pigment, no corneal lenses visible

Under "Description of the male" (holotype), Prosoma: "Sternum 0.88 long, 0.90 wide." then "Eyes reduced and lacking pigment, no corneal lenses are visible." **Quote MATCH**. Holotype male, Galleria del Pozzo, Miniere di Gorno, 14.X.2022; paratypes three females and a subadult male (tool summary). Female paratype verbatim "Eyes reduced and depigmented, no corneal lenses are visible.", as conditions quote.

Uncounted: the female paratype also has verbatim "AME reduced to a small spot of pigment."; the record omits it (line 12 carries the parallel sentence for angelicus). Replacement below.

**Line 13 MATCH.**

### Line 14, Typhlonesticus angelicus, eye_diameter_mm AME 0.03; ALE 0.05; PME 0.05; PLE 0.05

Female (holotype) Prosoma: "Eye diameter: AME 0.03, ALE 0.05; PME 0.05; PLE 0.05." **Quote MATCH**. Male paratype verbatim "Eye diameter: AME 0.04, ALE 0.05; PME 0.05; PLE 0.05.", as conditions quote. Units from Methods verbatim "All measurements are given in mm." Value lists the printed four values without adding to them.

Error (filing convention): `where` is empty. The quote names no species and no specimen; the desk's own convention ("Where a sentence names no species, `where` gives the treatment") and every record on main fill `where`. The conditions say "Female holotype" but no treatment or description heading is shown. Fixable.

Uncounted: the note says "the Methods do not describe how the eye diameter was measured". Methods say verbatim "Specimens were examined and measured using a Leica M80 stereoscopic binocular up to 60x magnification" and that troglomorphic-trait measurements "(diameter of anterior median eyes and femur elongation)" "are issued from Mammola et al. (2022)", "verified both on original publications and on original material". Replacement below.

**Line 14 FIXABLE.**

### Line 15, Typhlonesticus santinellii, eye_diameter_mm AME 0.01; ALE 0.05; PME 0.06; PLE 0.06

Under "Description of the female" (female paratype, Galleria del Pozzo), Prosoma: "Eye diameter: AME 0.01, ALE 0.05; PME 0.06; PLE 0.06." **Quote MATCH**. Conditions say the record is from the paratype, not the holotype. Units as line 14.

Error (filing convention): `where` empty, as line 14; a reader of the quote cannot tell which treatment or which specimen description it sits in beyond "Female paratype". Fixable.

Uncounted: the conditions say "the male holotype line reads "Eye diameter: AME 0.01, ALE 0.06; PME 0.05; PLE 0.06."". On the page that text is the end of one sentence, verbatim "Both eye rows recurved in dorsal view (PER 0.43 wide, AER 0.37), Eye diameter: AME 0.01, ALE 0.06; PME 0.05; PLE 0.06.", so the conditions quote starts mid-sentence without a cut marker. Same Methods-note fix as line 14. Replacements below.

**Line 15 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Dysderocrates kibrisensis, well developed | MATCH | none | quote MATCH (6); female holotype, male unknown, dead cave specimen stated |
| 10 | Harpactea kalavachiana, reduced | MATCH | none | quote MATCH (4); Comments eye sentence omitted, uncounted |
| 11 | Troglocoelotes sinanensis, strongly degenerated | MATCH | none | quote MATCH (9); single female holotype |
| 12 | Typhlonesticus angelicus, reduced, depigmented | MATCH | none | quote MATCH (9); male paratype sentence in conditions |
| 13 | Typhlonesticus santinellii, reduced, lacking pigment | MATCH | none | quote MATCH (10); female AME sentence omitted, uncounted |
| 14 | T. angelicus, eye_diameter_mm | FIXABLE | where | empty `where` for a quote naming no species; Methods note fix uncounted |
| 15 | T. santinellii, eye_diameter_mm | FIXABLE | where | empty `where`; conditions male quote unmarked mid-sentence, uncounted |

Errors 2 of 7 audited records (28.6%). By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0; names 0; filing convention 2 (lines 14, 15); duplicates 0. Both fixable; nothing unfixable, nothing held out. Verdict: merge lines 9-15 with the Replacement applied (the counted `where` fixes are required; the rest optional).

Unchecked: figures not viewed; the T. santinellii paratype list, the Troglocoelotes type block and the absence of further D. kibrisensis eye text rest on tool summaries; no checklist gave current status.

## Replacement

Each non-empty old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 10 (uncounted):
- `note`: "The paper gives no eye count in this sentence." -> "The paper gives no eye count in this sentence; the Comments add \"The eyes of H. kalavachiana sp. n. are reduced, and the AME are distant from each other, much more than average (Fig. 11).\""

Line 13 (uncounted):
- `note`: "Sentence names no species; it sits in the male holotype Description." -> "Sentence names no species; it sits in the male holotype Description. The female paratype Description also says \"AME reduced to a small spot of pigment.\""

Line 14:
- `where` (counted): "" -> "Taxonomy, Typhlonesticus angelicus sp. nov., Description of the female (holotype), Prosoma"
- `note` (uncounted): "and the Methods do not describe how the eye diameter was measured." -> "and the Methods say specimens \"were examined and measured using a Leica M80 stereoscopic binocular up to 60x magnification\"."

Line 15:
- `where` (counted): "" -> "Taxonomy, Typhlonesticus santinellii sp. nov., Description of the female (paratype), Prosoma"
- `conditions` (uncounted): "the male holotype line reads \"Eye diameter: AME 0.01, ALE 0.06; PME 0.05; PLE 0.06.\"" -> "the male holotype sentence ends \"… Eye diameter: AME 0.01, ALE 0.06; PME 0.05; PLE 0.06.\""
- `note` (uncounted): "and the Methods do not describe how the eye diameter was measured." -> "and the Methods say specimens \"were examined and measured using a Leica M80 stereoscopic binocular up to 60x magnification\"."
