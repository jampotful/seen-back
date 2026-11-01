# audit-417: desk-d312, evidence file lines 8 to 12

Audited 1 November 2026 from the desk-d312 files present untracked in the worktree (docs/tracks/progress/desk-d312.md and docs/views/evidence/desk-d312.jsonl, 12 lines; neither committed here, neither edited). Lines 1 to 7 (Tachycines) go to another auditor. HEAD equals origin/main (e250f5e71). `python3 -I tools/senses/check.py | grep d312`: "docs/views/evidence/desk-d312.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`): line 8 26, line 9 24, line 10 3, line 11 4, line 12 4, all within 40.

Crossref: single-DOI lookups api.crossref.org/v1/works/ for all five DOIs (10.3897/subtbiol.55.175661, zookeys.675.12690, zookeys.616.9442, zookeys.236.4068, zookeys.135.1721) were refused with PROVENANCE_REQUIRED, and the tool said not to retry; none was retried or worked around. Bibliographic fields were therefore checked against the publisher's printed citation line, title and front matter, and licence against the page-printed licence sentence. Each paper is the publisher's own free full text (Pensoft), which rules.md accepts without a Crossref cross-check; the Crossref licence could not be cross-checked for any of the five and is stated so here.

Sources opened (WebFetch, every URL from a WebSearch result; publisher article XML only): subtbiol.pensoft.net/article/175661/download/xml/ (four passes), zookeys.pensoft.net/article/12690/download/xml/ (two passes), zookeys.pensoft.net/article/9442/download/xml/, zookeys.pensoft.net/article/3272/download/xml/, zookeys.pensoft.net/article/2815/download/xml/. Not opened: PMC, plazi, BHL, antwiki PDF copy, DOAJ and library catalogue records (utm.my, uitm.edu.my, uv.mx, jioinstitute), omicsdi, GBIF, zenodo, bionames. No curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Repeats

`git grep -il -E` on origin/main (e250f5e71) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks) for Spelaeodelphax, Paramyrmetes, Ishigakicoccus, Neonipponaphis, Aleurodaphis and the five DOIs (also the bare id 175661). Only hit: docs/tracks/progress/desk-d297.md lines 17 and 21, which record that desk-d297 set Spelaeodelphax nexus aside and filed nothing; no record or sheet value. The same pattern over docs/views/evidence on every origin/research/* branch (731): only origin/research/desk-d312 itself. No repeats.

## Per line

### Line 8, Spelaeodelphax nexus, compound eyes and ocelli absent

Bibliographic: citation line "Santos JCCV, Asche M, Hoch H, Lopes Ferreira R (2026)" (front matter: Rodrigo L. Ferreira, disclosed in the note); title with the colon after "Neotropics" as printed; Subterranean Biology 55: 1-25, no issue; e-published 14 January 2026. Licence: page prints CC BY 4.0 (creativecommons.org/licenses/by/4.0/). The note's "Crossref CC BY 4.0 (vor)" could not be re-checked here (refusal above); the publisher's own free full text is accepted regardless.

Quote: species Diagnosis, run-in "Habitus": verbatim pieces "ocelli, tegmina strongly reduced in length without recogniza", "ut recognizable venation, hind wings reduced to narrow pads" followed by ".", and the comma after "ocelli" confirmed; opening "Small, light-colored and strongly troglomorphic delphacid devoid of compound eyes and ocelli". The stitched text equals the printed sentence. **Quote MATCH**, 26 words. Genus Diagnosis "compound eyes and ocelli totally absent, tegmina strongly reduced, wings vestigial", nymph "Head without compound eyes, ocelli or traces of them", species "Adults." heading followed by figure references only: all as conditions say. No class printed (classification gives Hemiptera, Delphacidae). Right.

Fault: **paratype count wrong.** The Paratypes entry, read verbatim: "... 1 ♀ (ISLA 126061) 4 nymph (ISLA 126062), and 04. vi. 2024," / "1 ♂ (ISLA 126062), 1 ♂ (ISLA 126063), 1 ♂ (ISLA 126065), 1 ♂ (ISLA 126066), 1 ♂ (ISLA 126067) (dissected)," / "1 ♂ (ISLA 126068), 1 ♂ (ISLA 126069), 1 ♀ (ISLA 125912), 1 ♂ (ISLA 125911) (SEM)." That is 8 males and 1 female on 4 June 2024; the conditions say "7 males and 1 female". One record error, fixable.

**Line 8 FIXABLE.**

### Line 9, Paramyrmetes foveipennis, eyes flattened but visible from above

Bibliographic: Lackner T; title verbatim in two pieces ("Redescription of the enigmatic neotropical inquiline Paramyrmetes foveipennis Bruch, 1929 with notes on myrmecophily" / "(Coleoptera, Histeridae) in the Saprininae subfamily"); ZooKeys 675: 57-73; e-published 19 May 2017. Page licence CC BY 4.0; accepted as publisher's own free full text, Crossref not cross-checked.

Quote: Re-description, Head and antennae: "Eyes flattened, but visible from above;" / "antennal scape slender, with several setae; pedicel approximately as long as following three antennomeres together;" / "8th antennomere saucer-like." Previous sentence ends "... interspaces with alutaceous microsculpture." **Quote MATCH**, one whole sentence, 24 words. Male lectotype designated here (Hersilia / La Geraldina, Santa Fé, "II.927", Hubrich, MNNC); redescription from the lectotype only; four other syntypes of unknown whereabouts; no other eye mention (tool summary). Classification Animalia, Coleoptera, Histeridae; Insecta only inside a reference title, so class blank is right. Optional (not counted): the label host "Pogonomyrmex var. carnivora" (tool summary) could be added.

**Line 9 MATCH.**

### Line 10, Ishigakicoccus shimadai, eye spot absent

Bibliographic: Tanaka H; title verbatim with the printed "Sternorryncha"; ZooKeys 616: 115-124; e-published 12 September 2016. Page licence CC BY 4.0; accepted as publisher's own free full text.

Quote: under "Slide-mounted specimens.": "Body elongate oval, slightly pyriform, 721–895 µm long, 379–632 µm wide." then "Eye spot absent." then "Antennae 5 segmented, ...". **Quote MATCH**, 3 words. Type series: holotype adult female, Ishigaki Is., Mt. Omoto, 16.II.2015, coll. T. Shimada; 3 adult female paratypes, same data; Acropyga yaeyamensis nest from Abstract and Methods: as in conditions. Genus Diagnosis also "Eye spot absent."; no eye mention in comparisons. Class: the treatment classification blocks print Animalia, Hemiptera, Rhizoecidae only; Insecta is in the article-categories biological-taxon list of the front matter. Filling class from that list is acceptable because the note discloses it, and it is consistent with lines 11 and 12, whose article-category lists (Aphidoidea; Hemiptera) carry no class. Not counted.

**Line 10 MATCH.**

### Line 11, Neonipponaphis pustulosis, 3-faceted eyes

Bibliographic: Jing Chen, Ge-Xia Qiao (= "Chen J, Qiao G-X"); title verbatim; ZooKeys 236: 81-89; 2 November 2012. Page licence Creative Commons Attribution License 3.0 (by/3.0); accepted as publisher's own free full text.

Quote: Apterous viviparous females, Mounted specimens: "Medial frons not protuberant (Figs 1, 9)." then "Eyes 3-faceted (Fig. 1)." then "Antennae short, ...". **Quote MATCH**, 4 words. Holotype apterous viviparous female and 13 paratype apterae, Mount Wuyi, Fujian, 11 Jun 2011, Castanopsis eyrei; generic diagnosis "Eyes with 3 facets in apterae and compound in alatae."; no eye mention in key or comments; no class printed. As in conditions.

Optional (not counted): conditions end with "Rank: the aphid eye of three facets is a triommatidium.", an unsourced gloss the page does not print; delete it or mark it as the unit's own term.

**Line 11 MATCH.**

### Line 12, Aleurodaphis sinojackiae, eyes with 3 facets

Bibliographic: Li-Yun Jiang, Ge-Xia Qiao; title verbatim; ZooKeys 135: 41-56; e-published 7 October 2011. Licence sentence "This is an open access article distributed under the terms of the Creative Commons Attribution License" without version, link by/3.0, as the note says; accepted as publisher's own free full text. The paper is a genus review, but the value comes from the original description of the new species from type material, so it is primary, not review-sourced.

Quote: apterous viviparous females, Head: "Front flat and straight." then "Eyes with 3 facets." then "Antennae 5-segmented (Figs 4, 22), ...". **Quote MATCH**, 4 words. Type material (tool summary): holotype apterous female, Hangzhou, 21 May 1985, V. F. Eastop, on Sinojackia xylocarpa; BMNH paratypes 28 apterous, 2 alate, 8 nymphs; NZMC 9 apterous, 11 alate, Nanjing, Jiangsu, 10 June 1987; Kôgakkan University 1 apterous, 1 alate: as in conditions. Alate description silent on eyes; genus Diagnosis "eyes normal" (alatae) and "eyes with 3 facets" (apterae). No class printed (article category Hemiptera).

**Line 12 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 8 | Spelaeodelphax nexus, compound eyes and ocelli absent | FIXABLE | conditions | 4 June 2024 paratypes are 8 males and 1 female, not 7 males |
| 9 | Paramyrmetes foveipennis, eyes flattened, visible from above | MATCH | | whole 24-word sentence; male lectotype only |
| 10 | Ishigakicoccus shimadai, eye spot absent | MATCH | | class from article-category list, disclosed |
| 11 | Neonipponaphis pustulosis, eyes 3-faceted | MATCH | | apterae only, as the generic diagnosis says |
| 12 | Aleurodaphis sinojackiae, eyes with 3 facets | MATCH | | apterae; alate description silent |

Errors: 1 of 5 records (20%); 1 fixable (line 8), 0 held out, 0 unfixable; no line to drop. Repeats: none. Crossref unreadable for all five DOIs (PROVENANCE_REQUIRED); bibliography from publisher citation lines and licence from page-printed sentences, all publisher's own free full text. Pooled verdict for lines 8 to 12 of desk-d312: **ACCEPT AFTER REPLACEMENT** (lines 9 to 12 as filed; line 8 with the replacement below, or dropped if it is not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 8:
- `conditions`: "7 males and 1 female (4 June 2024)" -> "8 males (ISLA 126067 dissected; 125911 SEM) and 1 female (4 June 2024)"

Optional, not counted:
- Line 9 `conditions`: "Hersilia / La Geraldina, Santa Fe province, Argentina, February 1927, J. Hubrich leg., MNNC" -> "Hersilia / La Geraldina, Santa Fé province, Argentina, label 'II.927', J. Hubrich leg., labelled with Pogonomyrmex var. carnivora, MNNC"
- Line 11 `conditions`: " Rank: the aphid eye of three facets is a triommatidium." -> "" (delete; the page does not print the term)
