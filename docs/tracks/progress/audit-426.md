# audit-426: desk-d317, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d317 files present untracked in the worktree (docs/tracks/progress/desk-d317.md and docs/views/evidence/desk-d317.jsonl; neither committed here, neither edited). This audit covers file lines 1 to 8 only; lines 9 to 16 go to another auditor. HEAD was origin/main (d44031679). `python3 -I tools/senses/check.py | grep d317`: "docs/views/evidence/desk-d317.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`), lines 1 to 8: 32, 32, 9, 17, 20, 20, 17, 11, all within 40.

Sources opened (WebFetch, every page URL from one of my WebSearch results): zookeys.pensoft.net/article/142538/download/xml/ (two passes), zookeys.pensoft.net/article_preview.php?id=2494 (two passes), www.mdpi.com/2075-4450/11/11/803 (two passes), subtbiol.pensoft.net/article_preview.php?id=73185 (two passes), subtbiol.pensoft.net/article/75613/download/xml/ (one pass), subtbiol.pensoft.net/article/52583/download/xml/ (one pass). Crossref single-DOI lookups (api.crossref.org/v1/works/) for all six DOIs; zookeys.103.1124 and subtbiol.41.75613 were rate-limited on the first call (sent in parallel) and answered on the single retry. PMC, DOAJ, Plazi, Zenodo, institutional repositories and library catalogue records (utm.my, uitm.edu.my, bg.ac.rs, icmbio) were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 8 WebSearches.

## Bibliographic and licence

- Lines 1 and 2 (Yin Z-W, Feng T, Zhou D-Y 2025). Citation line "Yin Z-W, Feng T, Zhou D-Y (2025) First report of subfamily Scydmaeninae (Coleoptera, Staphylinidae) from Shanghai ..."; Crossref the same order, ZooKeys 1231, 133-143, no issue, issued 2025-03-11. Title identical. Licence sentence "Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Accepted.
- Line 3 (Andújar C, Hernando C, Ribera I 2011). Author order, "ZooKeys 103: 49–62", 10 June 2011 and the CC BY licence sentence ("distributed under the terms of the Creative Commons Attribution License") match; Crossref CC BY 3.0 vor. **Title fault.** The page prints, in the article heading and the HTML title tag, "A new endogean, anophthalmous species of Parazuphium Jeannel from Northern Morocco (Coleoptera, Carabidae), with new molecular data for the tribe Zuphiini" (also the title in the search results). The filed title "A new species of endogean, anophthalmous Parazuphium ... (Coleoptera: Carabidae) ..." is the meta-citation_title / Crossref form, not what the page prints. The note's claim that "the page title has a colon after Coleoptera" is wrong: the colon is only in the meta-citation_title field. The page prints no "Citation:" line for this 2011 article. Recorded: page-printed title used in the replacement; the meta-citation/Crossref order differs.
- Line 4 (Sasakawa K, Mitsuduka Y, Itô H 2020). Byline order matches Crossref; "Insects 2020, 11(11), 803"; title identical; page sentence "Creative Commons Attribution (CC BY) license" with a 4.0 link, metadata CC BY 3.0, Crossref CC BY 4.0 vor. Accepted.
- Lines 5 and 6 (Pellegrini TG, Ferreira RL, Zampaulo RdeA, Vieira L 2022). Citation line printed exactly so; "Subterranean Biology 43: 97-126."; title identical including the colon; CC BY 4.0 sentence; Crossref CC BY 4.0 vor, issued 2022-06-10. Accepted.
- Line 7 (Ćurčić S, Vesović N, Vrbica M, Popović S, Radovanović Ž, Ćurčić NB, Rađa T 2021). XML author order as filed; last author printed "Tonći" (Crossref "Tonči"), page spelling rightly used; Subterranean Biology 41: 69-85; CC BY 4.0 sentence, Crossref CC BY 4.0 vor. Accepted.
- Line 8 (García R, Andújar C, Oromí P, López H 2020). Order as Crossref; 35: 1-14; issued 2020-06-15; CC BY 4.0 vor. Accepted.

Bibliographic faults: 1 (line 3 title). Licence faults 0. source.access "open" right throughout.

## Names and higher taxa

All eight are species described as new in the papers read (Euconnus (s. str.) imparitus and magnoculus Yin, Feng & Zhou 2025; Parazuphium aguilerai; Pterostichus (Nialoe) monolineatus; Coarazuphium xikrin and kayapo; Leonhardia solaki; Oromia orahan), with Plazi treatments under the same names in search results; no later synonymy came up. Orders and families are as printed in each title (Oromia also in its treatment classification block, which prints no class). No page prints a class for these species; class blank is right. eye_type fits every value.

## Repeats

`git grep -il` on origin/main (d44031679) over the whole docs/ tree for each of the eight species (binomial and epithet) and the six DOIs. Hits: only desk-d302.md (Euconnus imparitus and E. magnoculus as a dropped candidate, "head sentences returned only as paraphrase") and desk-d316.md (Oromia orahan XML blocked); no evidence, audit/corrected, audit/ALL or sheets row. Unmerged branches: docs/views/evidence/desk-dN.jsonl read from every origin/research/desk-d* branch through one `git cat-file --batch` (19 branches have no such file) and grepped for the same species and DOIs: the only hits are in desk-d317's own blob (identical to the untracked file). No repeats.

## Per line

### Line 1, Euconnus imparitus, eyes relatively small, barely convex, finely faceted

Male Head: "Head subrounded, as long as wide, broadest at eyes, length and width 0.36 mm; vertex and frons confluent, weakly convex;" / "supraantennal tubercles barely prominent; eyes relatively small, barely convex and finely faceted." **Quote MATCH**, one whole printed telegraphic Description sentence, 32 words. Holotype ♂ "late vii.2018, light trap, D-Y Zhou leg.", SNUC; known from the holotype only; "Female. Unknown."; Diagnosis "Head subspherical, eyes anteriorly situated, tempora much longer than eyes." carried. The key lead for E. imparitus (couplet 1) has no eye wording, and Comparative notes have none. **Line 1 MATCH.**

### Line 2, Euconnus magnoculus, eyes large, strongly convex, coarsely faceted

Male Head sentence verified whole in the same way (32 words); "Female. Unknown."; Diagnosis "Eyes greatly prominent, approximately 1.4 × as long as tempora." carried; holotype ♂ "07.vi.2023, Ting Feng leg.", SNUC. Faults (one record error, fixable): (a) **key wording omitted.** The male key, couplet 2, leads to E. magnoculus with "Eyes greatly convex, much longer than tempora (Fig. 3A)"; the conditions do not carry it (the task requires Key eye wording where printed). (b) "collecting method not stated" is true of the label only; the Biology section says the specimen came from a leaf-litter sample in secondary mixed forest (tool summary). **Line 2 FIXABLE.**

### Line 3, Parazuphium aguilerai, no trace of eyes or ocular scars

Description: preceded by "Head (Fig. 1) with trapezoidal shape.", then "No trace of eyes or ocular scars (Fig. 2b).", followed by "Length of head (from apex of mandible to base) 0.63 mm; ...". **Quote MATCH**, whole sentence, 9 words. Diagnosis "Eyes absent (Fig. 2b)." carried; P. ramirezi "with reduced eyes" carried; single known specimen, holotype ♂, 28-III-2008, Souk-Khemis-des-Anjra, Tetuan, 123 m, MCNB, under a large, deeply buried boulder. Faults: the title (above); the collectors are printed "Andújar, Hernando, Ribera & Aguilera leg." (conditions "Andujar"). Optional: the Recognition section also calls P. feloi (Canary Islands) anophthalmous. One record error. **Line 3 FIXABLE.**

### Line 4, Pterostichus monolineatus, eyes weakly convex

"Eyes weakly convex, with the anterior–posterior length longer than 1/2 of the length of antennal segment 1." **Quote MATCH**, 17 words; previous sentence on the left mandible, next "Antennal segment 2 with two setae." Holotype ♂ and paratypes "1♂1♀, same data as the holotype", 10.ix–4.x.2019, ST, leg. YM, NSMT; "subterranean baited traps (STs)" confirmed in Methods. The description covers both sexes (male n = 2, female n = 1 measurements), and the eye sentence is not sex-specific; Diagnosis, Notes and Discussion have no eye wording; the paper has no key or table with eye wording. **Line 4 MATCH.**

### Line 5, Coarazuphium xikrin, eyes reduced, depigmented, flattened

"Eyes reduced, depigmented, and flattened, situated laterally at the end of the genal sulcus," / "ommatidia are not visible at 50×." **Quote MATCH**, 20 words. Holotype ♂ Cave N1N8/N1-0020, 639 m, 17.VII–04.VIII.2014, Carste Company leg. (MZSP49180); ten paratypes counted from the page: 4 ♂ (N1-0022, N1-0037, N1-0016, N1-0168) and 6 ♀ (N1-0022, N1-0008, N1-0073, N1-0240, N1-0101, N1-0037), 2014-2015, caves as filed. Differential diagnosis, key ("Key for identification of adults of species of the genus Coarazuphium"), Introduction and Discussion carry no eye wording; collecting method not stated (tool summary). **Line 5 MATCH.**

### Line 6, Coarazuphium kayapo, eyes reduced, depigmented and flattened

Sentence printed without the comma after "depigmented", as the note says; 20 words. **Quote MATCH.** Holotype ♂ Cave S11B-0177, 641 m, 24.IX.2018, Ativo Ambiental leg. (ISLA 75757); paratype 1 ♀ Cave S11D-0111, 17.VII–04.VIII.2010, Carste Company leg. (MZSP49198). Differential diagnosis mentions eyes only as setal landmarks ("one pair of posterior supraorbital posteriad the eyes;"), as the conditions say. **Line 6 MATCH.**

### Line 7, Leonhardia solaki, anophthalmous

"Head: Longer than wide (HL/HW M 1.11, R 1.06–1.19), anophthalmous, with no occipital carina (Figs 2A, 3C)." **Quote MATCH**, 17 words. Holotype ♂ Golubnjača kod Skucana Pit, 1,005 m, 27 June 2018, leg. Tonći Rađa (IZFB); paratypes 2 ♂ 2 ♀ same data (IZFB, SSM) and 1 ♂ 2 ♀ 12 June 2018 (IZFB): as filed. Body length "(3.55 mm in males, 3.69 mm in females)" are means, as filed. Specimens "gathered by hand", floor and walls of the innermost part of the pit. Diagnosis, key and the Discussion text returned carry no eye wording; no Remarks section. Both sexes covered by one description. **Line 7 MATCH.**

### Line 8, Oromia orahan, eyeless

"Head globose, partially retracted into pronotum, carinated, with thick punctures, eyeless." **Quote MATCH**, 11 words (Male description). Material examined, read specimen by specimen: holotype 1 ♂ Reventón Oscuro, MSS1/1, 3 January 2015, P. Oromí leg., IPNA-CSIC; paratypes from the same locality, each 1 ♀: MSS2 5 Feb 2009, MSS3 8 June 2010, MSS1 7 Jan 2011, MSS2/4 16 Nov 2013, MSS1/3 3 Jan 2015; and 1 ♂ Monte de Los Acebiños, Hermigua, 8 December 2008, R. García leg. (RGB). So the unit's reading (5 ♀ plus 1 ♂) is right and the summariser's "all females except one" means the same thing; sexes are not ambiguous. MSS traps baited with liver or blue cheese; the Acebiños male was sifted from leaf litter and soil (tool summary). Faults (one record error, fixable): (a) **female description misstated.** The conditions say it "gives body size only"; it opens "Similar to male, but with total length 5.2–5.5 mm ..." and goes on with rostrum ("Rostrum longer than in males (1.5 mm)."), elytra, antennae, legs, fifth ventrite, spiculum ventrale and ovipositor, with no eye wording. (b) **genus statement omitted.** The Introduction prints "Oromia species are eyeless, with elongated and rather flattened bodies, slightly depigmented."; the conditions carry only the Barretonus note. The key has no eye characters. **Line 8 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Euconnus imparitus, eyes small, finely faceted | MATCH | | whole 32-word sentence; female unknown; Diagnosis carried |
| 2 | Euconnus magnoculus, eyes large, coarsely faceted | FIXABLE | conditions | key couplet 2 eye wording omitted; leaf-litter sample in Biology |
| 3 | Parazuphium aguilerai, no trace of eyes | FIXABLE | source.title, conditions, note | page prints "A new endogean, anophthalmous species of ... (Coleoptera, Carabidae)"; "Andújar" |
| 4 | Pterostichus monolineatus, eyes weakly convex | MATCH | | both sexes described, eye sentence not sex-specific |
| 5 | Coarazuphium xikrin, eyes reduced | MATCH | | 4 ♂ 6 ♀ paratypes confirmed |
| 6 | Coarazuphium kayapo, eyes reduced | MATCH | | comma difference printed so |
| 7 | Leonhardia solaki, anophthalmous | MATCH | | type counts and sexes confirmed |
| 8 | Oromia orahan, eyeless | FIXABLE | conditions | female description is not body size only; Introduction genus sentence "Oromia species are eyeless" omitted |

Errors: 3 of 8 records (37.5%); 3 fixable (lines 2, 3, 8), 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d317 lines 1 to 8: **ACCEPT AFTER REPLACEMENT** (lines 1, 4, 5, 6, 7 as filed; lines 2, 3 and 8 with the replacements below, or dropped if they are not applied). Pooled with the other auditor's lines 9 to 16 by the merger.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 2:
- `conditions`: "collecting method not stated." -> "the label gives no collecting method; the Biology section says the specimen came from a leaf-litter sample in secondary mixed forest."
- `conditions`: "The other new species, E. imparitus, has" -> "The male key (couplet 2) leads to this species with 'Eyes greatly convex, much longer than tempora (Fig. 3A)'. The other new species, E. imparitus, has"

Line 3:
- `source.title`: "A new species of endogean, anophthalmous Parazuphium Jeannel from Northern Morocco (Coleoptera: Carabidae), with new molecular data for the tribe Zuphiini" -> "A new endogean, anophthalmous species of Parazuphium Jeannel from Northern Morocco (Coleoptera, Carabidae), with new molecular data for the tribe Zuphiini"
- `conditions`: "Andujar, Hernando, Ribera and Aguilera leg." -> "Andújar, Hernando, Ribera & Aguilera leg."
- `note`: "The page title has a colon after Coleoptera; the article XML text returned a differently ordered title ('A new endogean, anophthalmous species of Parazuphium ... (Coleoptera, Carabidae)'), so the Crossref/page-header title is used." -> "The page heading and HTML title print 'A new endogean, anophthalmous species of Parazuphium ... (Coleoptera, Carabidae)', which is used; the page's meta-citation_title and Crossref give 'A new species of endogean, anophthalmous Parazuphium ... (Coleoptera: Carabidae)'."

Line 8:
- `conditions`: "(the female description reads 'Similar to male' and gives body size only)" -> "(the female description begins 'Similar to male, but with total length 5.2–5.5 mm' and gives rostrum, elytra, antennae, legs, ventrite 5, spiculum ventrale and ovipositor, with no eye wording)"
- `conditions`: "A Remarks note on the weevil genus Barretonus states that all its species are eyeless." -> "The Introduction says 'Oromia species are eyeless, with elongated and rather flattened bodies, slightly depigmented.' A Remarks note on the weevil genus Barretonus states that all its species are eyeless. The key has no eye characters."

Optional, not counted:
- Line 3 `conditions`: "which has reduced eyes." -> "which has reduced eyes; the Recognition section also calls P. feloi (Canary Islands) anophthalmous."
