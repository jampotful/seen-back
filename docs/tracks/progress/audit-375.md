# audit-375: desk-d285, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d285 files present untracked in the worktree (docs/tracks/progress/desk-d285.md and docs/views/evidence/desk-d285.jsonl, 5 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d285). Worktree HEAD and origin/main 6873b0bc (Merge d283 after audit 373). `python3 -I tools/senses/check.py | grep 'd285\.'`: "docs/views/evidence/desk-d285.jsonl: 5 records, 0 problems". Quote lengths (`len(q.split())`): 29, 35, 6, 12, 15, all within 40. Non-ASCII in quotes: "[…]" cut mark in line 4 only. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/works/ for all five DOIs (10.3897/zookeys.530.6064, 10.3897/zse.98.83184, 10.3897/zookeys.937.49173, 10.3897/zookeys.1178.108276, 10.3897/zookeys.358.6384; all answered); zookeys.pensoft.net/article_preview.php?id=6064 (three passes); zse.pensoft.net/article_preview.php?id=83184 (one pass) and zse.pensoft.net/article/83184/download/xml/ (one pass); zookeys.pensoft.net/article/49173/download/xml/ (one pass); zookeys.pensoft.net/article/108276/download/xml/ (two passes); zookeys.pensoft.net/article/3607/download/xml/ (two passes). All URLs were returned by a WebSearch first. Names: zoraptera.speciesfile.org/otus/924545/overview redirected to misc.speciesfile.org (a URL not in any search result), not followed. PMC, Plazi, Zenodo, species-id.net, GBIF, WoRMS, BHL, DOAJ mirrors and library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 12 WebSearches.

## Bibliographic and licence

- Line 1 (de León-Espinosa, de León-González 2015). Crossref: Jesus A. de León-González, Angel de León-Espinosa (order reversed against print); title as recorded (first 125 characters seen, rest matches the search-result title); ZooKeys 530, 129-149, no issue; issued 2015-10-29; CC BY 4.0 vor; relation empty. Page byline Angel de León-Espinosa, Jesus A. de León-González; citation verbatim "de León-Espinosa A, de León-González JA (2015) Pycnogonids associated with the giant lion´s-paw scallop" ... "ZooKeys 530: 129-149" (tool summary for the tail). "As printed" is the page byline and citation line (FORMAT rule; audit 373 treated the reversed Crossref order of ZooKeys 569 the same way). Record right. Licence CC BY 4.0 sentence (tool summary) plus Crossref. Accepted.
- Line 2 (Liu et al. 2022). Crossref: Yi Liu, Xiao-Yu Song, Zhong-Yin Sun, Wei-Xuan Li, Ronald Sluys, Shuang-Fei Li, An-Tai Wang; title identical; Zoosystematics and Evolution 98, journal-issue 2, 233-243; issued 2022-06-29; CC BY 4.0 vor; relation empty. Page citation verbatim "Citation: Liu Y, Song X-Y, Sun Z-Y, Li W-X, Sluys R, Li S-F, Wang A-T (2022) Addition to the known diversity of Chinese", journal "98(2): 233–243" (tool summary). Licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Initials confirmed on the page (uncounted note fix). Accepted.
- Line 3 (Zhou, Yang 2020). Crossref: Xulin Zhou, Weicheng Yang; title identical (two verbatim pieces); ZooKeys 937, 21-29; issued 2020-06-01; CC BY 4.0 vor; relation empty. Page byline same order; licence sentence verbatim as above. Accepted.
- Line 4 (Matsumura, Maruyama, Ntonifor, Beutel 2023). Crossref: Yoko Matsumura, Munetoshi Maruyama, Nelson N. Ntonifor, Rolf G. Beutel; title identical (leading byte-order mark in Crossref); ZooKeys 1178, 39-59; issued 2023-09-01; CC BY 4.0 vor; relation empty. Page "Matsumura Y, Maruyama M, Ntonifor NN, Beutel RG"; licence verbatim in three pieces ("This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)," | "which permits unrestricted use, distribution, and reproduction in any medium," | "provided the original author and source are credited."). Accepted.
- Line 5 (Bernardi, Klompen, Zacarias, Ferreira 2013). Crossref: Leopoldo Bernardi, Hans Klompen, Mauricio Zacarias, Rodrigo Ferreira; title identical (two verbatim pieces); ZooKeys 358, 69-89; issued 2013-12-04; CC BY 3.0 vor, delay 0; relation empty; resource URL zookeys.pensoft.net/articles.php?id=3607 (so article id 3607 is the right copy). Page byline Leopoldo Ferreira de Oliveira Bernardi, Hans Klompen, Mauricio Sergio Zacarias, Rodrigo Lopes Ferreira, which gives the recorded initials LFO, H, MS, RL; no printed citation line returned for this paper. Licence: "open access article distributed under the terms of the Creative Commons Attribution License 3.0 (CC-BY)", licence URL creativecommons.org/licenses/by/3.0 (tool summary with verbatim pieces). Page 3.0 and Crossref 3.0 agree; no conflict. Accepted; the note's "read only as far as 'Creative Commons'" can now be replaced (uncounted).

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No named checklist was reachable: WoRMS refused by rule; the Zoraptera Species File hit redirected to a host not in any search result and was not followed; searches for pycnobase, the Turbellarian Taxonomic Database species page, the Orthoptera Species File page for Tachycines (Gymnaeta) trapezialis and an Opilioacarida list returned no species page. All five species are described in the cited paper, so the names rest on the original descriptions, as the desk said.

- Eurycyde bamberi: paper's headings "Class Pycnogonida Latreille, 1810", "Order Pantopoda Gerstäcker, 1863", "Family Ammotheidae Dohrn, 1881", "Genus Eurycyde Schiödte, 1857" (tool summary of headings). Pantopoda filed as order and Pycnogonida kept as the class, rightly (no class-as-order fault).
- Dugesia gemmulata: title "(Platyhelminthes, Tricladida, Dugesiidae)"; main already files Tricladida as order 18 times. Met.
- Tachycines trapezialis: Taxonomy heading "Rhaphidophoridae"; title "(Orthoptera, Rhaphidophoridae, Aemodogryllinae, Aemodogryllini)". Tachycines sits in Rhaphidophoridae as printed, not Gryllacrididae. Met.
- Zorotypus komatsui: "Family Zorotypidae Silvestri, 1913" then "Subfamily Zorotypinae Silvestri, 1913"; order Zoraptera in the title. Met.
- Neocarus proteus: "Family Opilioacaridae With, 1904", "Genus Neocarus Chamberlin & Mulaik, 1942"; no order heading. Introduction verbatim: "Opilioacarida is one of the orders of mites (Lindquist et al. 2009), but has a very small number of described species." The order therefore comes from a printed sentence, not only the title (uncounted note fix). Met.

Name faults 0.

## Duplicates

git grep on origin/main (6873b0bc) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Eurycyde, bamberi, Dugesia, gemmulata, Tachycines, trapezialis, Zorotypus, komatsui, Neocarus, proteus and the DOIs and article ids (zookeys.530, 6064, zse.98, 83184, zookeys.937, 49173, zookeys.1178, 108276, zookeys.358, 6384): only unrelated matches ("Dugesiana" journal in sweep-8 and sweep-71; Proteus anguinus rows; "6064" and "6384" inside eval numbers, wfo-0000826064 and PMC366384). No main row for any of the five species, genera or DOIs. All 181 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: hits only in research/desk-d285 itself. audit-3*.md hold-outs: none name these genera.

Duplicates 0.

## Trait keys and rulings

- eyes_count units: main has 12 rows with units "eyes" (totals) beside per-side rows; lines 1, 2, 5 give totals ("four pronounced eyes", "two eyes", "two pairs of eyes" = 4) with units "eyes", which fits. Line 5 could equally be filed as 2 "eye pairs" (2 rows on main), but 4 "eyes" says no more than "two pairs of eyes".
- eye_type: lines 3 and 4 are descriptive strings, the form audits 370 to 373 accept for presence or partial absence; line 4 does not use "none" because it states two separate absences (eye spots, ocelli) of a single morph, with the morph in the value; acceptable.
- Laboratory stock (line 2): audit 332 accepts laboratory populations of a wild species at species rank when no strain, line or breed is named. The Dugesia culture's wild origin is printed (below), so species rank is fine. What the record must state rightly is the composition of the measured animals (see line 2).
- Attribution: every quote sits under the single new species' own Description heading in a paper (or treatment) describing it, so a sentence not naming the species is attributable, as in audits 362 to 373.

## Per-record findings

### Line 1, Eurycyde bamberi, eyes_count 4

Description, verbatim in two abutting pieces in one response: "Small ocular tubercle, inserted at edge of cephalic segment, without lateral spines," | "twice as tall as its diameter capped with an inverted cone, with four pronounced eyes (Fig. 1B)." Tool confirms no comma between "diameter" and "capped". Preceded by "tenth segment smaller than previous ones, with a row of spines on the ventral surface (Fig. 1D)."; followed by "Trunk compact, spineless, suture lines slightly marked (Fig. 1A–B)." **Quote MATCH**, 29 words. Value 4 says no more than "four pronounced eyes". Type material verbatim: "Holotype (1 male), Ojo de Liebre bay, Guerrero Negro, Baja California Sur, scallop fishing area: El Datil," then coordinates, UANL-FCB-PYCNO-0031, "01/12/2012" (tool summary for the tail); no paratypes. Distribution verbatim: "This species is known only from Ojo de Liebre bay, Guerrero Negro, Baja California Sur, Mexico." Table 1 and Remarks describe the tubercle ("Short, globose, distally pointed, twice taller than its diameter.") with no eye count. Holotype-only basis stated in conditions. Right.

Fault: the note says the quote "is the first and only sentence of the Description". The Description has about 20 sentences (proboscis, chelifores, palp, ocular tubercle, trunk, legs, oviger, abdomen); the eye sentence is the fifth, and the paragraph opens "Proboscis articulated, proximal portion a cylindrical tube" (tool listing of sentence openings). A false statement about the source's context; counted.

Uncounted: "collected from scallop shells": Methods verbatim "giant lion´s paw scallops were captured by scuba diving at depths not exceeding 10 meters in four fishing areas", "Each scallop was collected individually in zip-lock bags to prevent loss of specimens associated with this clam." and "the associated fauna were separated under a stereomicroscope, and placed in vials with 70% ethanol for later identification." The fauna was sorted from whole bagged scallops, not specifically from shells.

**Line 1 error, fixable (note).**

### Line 2, Dugesia gemmulata, eyes_count 2

Description, verbatim in two abutting pieces in one response: "At a distance varying between 0.46 mm and 0.56 mm from the anterior body margin," | "two eyes are present in the middle of the low-triangular head, situated in pigment-free patches (n = 3; Fig. 3C)." Preceded verbatim by "The following measurements are based on sexualised individuals."; followed by a sentence on kidney-shaped eyecups with numerous retinal cells (tool summary). **Quote MATCH**, 35 words. Value 2 says no more. Verbatim also: "Sexualised and asexual individuals exhibited no differences in appearance, except for the body size." No supernumerary eyes; the Diagnosis has no eye statement (tool summary). Holotype verbatim "a rural streamlet in Qingzhen City, Guizhou, China, 26°33.83'N, 106°13.65'E, 3 February 2018" (IZCAS PLA-0101, Zhong-Yin Sun; 20 sagittal slides); paratypes verbatim "IZCAS PLA-0102, ibid., sagittal sections on 30 slides; IZCAS PLA-0103, ibid., horizontal sections on 18 slides."

Wild origin is stated: "The animals were collected from the underside of small pebbles in the riverbed," (verbatim piece). So laboratory rearing is acceptable at species rank (audit 332).

Fault: the conditions say the animals were "wild-collected as sexually immature animals and reared in the laboratory until they sexualised", which reads as the same wild animals maturing. Methods verbatim: "Only 15 specimens were collected at the beginning, none of which was sexually mature." and "During about two years of rearing under laboratory conditions, the animals multiplied by means of fission and," | "eventually, in total, about 30 specimens sexualised." The sexualised animals measured (n = 3, including the sectioned types) are therefore products of about two years of laboratory fission from 15 wild founders, not the wild-collected individuals themselves; that composition is not stated. Sample composition and colony origin; counted, fixable.

**Line 2 error, fixable (conditions).**

### Line 3, Tachycines trapezialis, eye_type

Description, Male, verbatim: "Ommateum normal, not reduced; ocelli visible." Preceded by "Body medium-sized (Fig. 5)."; followed by "Vertex divided into two conical tubercles (Fig. 1A, B)." **Quote MATCH**, 6 words. Value "compound eyes (ommateum) normal, not reduced; ocelli visible" glosses ommateum as compound eye and otherwise repeats the quote; no more than the quote. Type material verbatim: holotype "1♂, Diaosiyan Cave, Ziyun County, Guizhou," "25°35.06'N, 106°12.32'E, 1110–1120 m alt., October 2, 2019," Xulin Zhou leg.; paratype "1♀, same data as holotype." Female verbatim: "Other characters are similar to male (Fig. 6)."; no eye statement. Diagnosis has no eye statement. Discussion verbatim: "Eyes of these species vary from fully developed to reduced or absent, as in the totally blind T. (G.) omninocaecus." Conditions and note right.

**Line 3 MATCH.**

### Line 4, Zorotypus komatsui, eye_type

Description, paragraph heading verbatim "Head (Figs 1, 2A)."; then the sentence, verbatim in three consecutive pieces: "Head subtriangular, without black eye spots (Figs 1, 2A); ocelli absent; cephalic chaetotaxy as in Fig. 2A;" | "relatively long sinuate setae densely arranged on vertex, referred to as fontanelle" | "(e.g., Delamare-Deboutteville 1951; van Ryn-Tournel 1971) (Fig. 2A)." The quote starts at the sentence start and stops after "ocelli absent;" with "[…]". **Quote MATCH**, 12 words with the mark. The cut drops only the chaetotaxy and the fontanelle setae (26 words); no eye, ocellus, morph or sex qualifier is lost. The morph qualifier the launch prompt asks about sits outside the sentence and is carried by the value "(apterous male)" and the conditions. Diagnosis verbatim: "eye spots absent in apterous males". Type material verbatim: "Cameroon: apterous male, South-west region, Nyasoso, Mt Kupe, 4°50'12.5"N, 9°41'21.7"E, 16.v.2015, coll. Takashi Komatsu" | "(depository number/ SEHU48817-48818, parts of antennae mounted on another glass slide)."; no paratypes; no alate or female described (tool summary). Value says no more than quote plus the printed morph.

Uncounted: the conditions' "the winged morph, which in other Zoraptera carries compound eyes and ocelli" has no source in the record. The paper's Introduction and Discussion do not say so (tool summary); the only support in the paper is the alate female of Z. vinsoni, verbatim "Compound eyes and three black ocelli present.", while its male prints "Head subtriangular, slightly wider than pronotum, without black eye spots (Fig. 5D); ocelli absent;". The clause should cite that.

**Line 4 MATCH.**

### Line 5, Neocarus proteus, eyes_count 4

Description, Dorsum, first sentence verbatim: "Anterior dorsal shield in all stages with two pairs of eyes, and stout, ribbed setae." The next sentence concerns the setae-free dorsal idiosoma with transverse rows of lyrifissures (tool summary). **Quote MATCH**, 15 words. Value 4 = two pairs; "in all stages" covers the stages described: protonymph, deutonymph, tritonymph, adult female and male; the larva is not described (tool summary), as conditions say. Holotype "Holotype female.", epigean, Mariana, Minas Gerais, 21.XII.2011, MZLQ (tool summary with verbatim piece); paratypes of all four postlarval stages from 14 November to 21 December 2011 (tool summary; per-stage tallies not checked against Table 1). Methods verbatim: "come from collections conducted in 2011 in caves and the epigean environment of ferruginous outcrops" in "the Municipal district of Mariana, Minas Gerais, Brazil." No other eye mention in the paper (tool summary). No species author printed, as the note says.

Uncounted: licence sentence now read (CC BY 3.0); order from the Introduction sentence.

**Line 5 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Eurycyde bamberi, eyes_count 4 | error, fixable | note | quote MATCH (29), holotype male; note falsely calls it the Description's only sentence |
| 2 | Dugesia gemmulata, eyes_count 2 | error, fixable | conditions | quote MATCH (35); measured sexualised animals arose after two years of lab fission from 15 wild founders, not stated |
| 3 | Tachycines trapezialis, ommateum normal, ocelli visible | MATCH | none | quote MATCH (6), male holotype; Rhaphidophoridae as printed |
| 4 | Zorotypus komatsui, no eye spots, ocelli absent (apterous male) | MATCH | none | quote MATCH (12), cut drops no qualifier; morph in value |
| 5 | Neocarus proteus, eyes_count 4 | MATCH | none | quote MATCH (15); CC BY 3.0 page and Crossref |

Errors 2 of 5 audited records (40%), above the 5% bar; none held out. By kind: quotes 0; value exceeding quote 0; sample composition 1 (line 2); misstatement of source context 1 (line 1); bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0 against main, all 181 desk-d2* and audit-3* branches and the audit-3* hold-outs. Verdict: fail as filed; both faults are fixable by the replacement text below, after which all five lines can merge.

Unchecked: no named checklist entry for any of the five species (WoRMS refused by rule; Zoraptera Species File redirect not followed; no pycnobase, Turbellarian Taxonomic Database, Orthoptera Species File or Opilioacarida-list species page in search results); the Neocarus paratype tallies by stage against Table 1; the sentences following the Dugesia and Neocarus quotes and several type-material tails rest on tool summaries; figures not viewed; the end of the Eurycyde title rests on the search-result title and the page, Crossref's tail being cut by the tool.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1 (counted):
- `note`: "The sentence does not name the species; it is the first and only sentence of the Description." -> "The sentence does not name the species; it is the fifth of about twenty sentences of the holotype's Description (after proboscis, chelifores and palp; followed by 'Trunk compact, spineless, suture lines slightly marked (Fig. 1A–B).')."

Line 1 (uncounted):
- `conditions`: "(collected from scallop shells)" -> "(scallops collected by scuba at depths not exceeding 10 m, each bagged individually, the associated fauna separated under a stereomicroscope)"

Line 2 (counted):
- `conditions`: "wild-collected as sexually immature animals and reared in the laboratory until they sexualised;" -> "15 animals were wild-collected from under pebbles in the riverbed, none sexually mature; during about two years of laboratory rearing they multiplied by fission and about 30 specimens eventually sexualised, so the measured sexualised animals are laboratory fission products of those wild founders;"

Line 2 (uncounted):
- `note`: "Author initials were derived by the tool from the author list (no printed Citation field was returned), so the initials form is unconfirmed on the page." -> "Author initials as in the printed Citation line on the article_preview page ('Liu Y, Song X-Y, Sun Z-Y, Li W-X, Sluys R, Li S-F, Wang A-T (2022)'). Laboratory stock of wild origin accepted at species rank (audit 332)."

Line 4 (uncounted):
- `conditions`: "so nothing is known of the winged morph, which in other Zoraptera carries compound eyes and ocelli;" -> "so nothing is known of a winged morph (in the same paper the alate female of Z. vinsoni has 'Compound eyes and three black ocelli present.' while its male lacks eye spots and ocelli);"

Line 5 (uncounted):
- `note`: "Licence: page prints a Creative Commons sentence (read only as far as 'Creative Commons') and Crossref lists CC BY 3.0 (vor)." -> "Licence: page prints the Creative Commons Attribution License 3.0 (CC-BY) sentence (licence URL creativecommons.org/licenses/by/3.0) and Crossref lists CC BY 3.0 (vor)."
- `note`: "the order Opilioacarida is taken from the title." -> "the order Opilioacarida is taken from the title and the Introduction ('Opilioacarida is one of the orders of mites (Lindquist et al. 2009)')."
