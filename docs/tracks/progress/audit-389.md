# audit-389: desk-d297, evidence lines 6 to 9

Audited 1 November 2026 from the desk-d297 files present untracked in the worktree (docs/tracks/progress/desk-d297.md and docs/views/evidence/desk-d297.jsonl, 9 lines; neither committed here, neither edited). Lines 1-5 are audit-388's. Line numbers are the file's (1-based). HEAD equals origin/main (a85bc4ef). `python3 -I tools/senses/check.py | grep 'd297\.'`: "docs/views/evidence/desk-d297.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 6-9: 5, 14, 6, 12, all within 40; the only non-ASCII character is the en dash in line 9 ("1–2"), which the page prints.

Sources opened (WebFetch): subtbiol.pensoft.net/article_preview.php?id=60483 (two passes); subtbiol.pensoft.net/article/9804/download/xml/ (two passes); zookeys.pensoft.net/article/2813/download/xml/ (two passes); mdpi.com/2076-2615/13/20/3199 (two passes; the record's url; searches returned mdpi.com pages of this DOI (/review_report, /reprints) but not the bare article path, and the fetch went through without a provenance refusal); Crossref single-DOI lookups api.crossref.org/v1/works/ for the four DOIs. PMC, Plazi, bionames, peeref, DOAJ, GBIF, ICMBio, educapes, BHL, news and wiki hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Line 6 (Hoch, Sendra, Montagud, Teruel, Ferreira 2021). Page and Crossref same order (Hannelore Hoch, Alberto Sendra, Sergio Montagud, Santiago Teruel, Rodrigo Lopes Ferreira); title identical; Subterranean Biology 37: 1-26, no issue; issued 2021-01-11; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 licence sentence. Accepted.
- Line 7 (Cordeiro, Bichuette, Moreira 2023). Page and Crossref same order (Isabelle R. S. Cordeiro, Maria Elina Bichuette, Felipe F. F. Moreira); title identical; Animals 13(20): 3199; issued 2023-10-13; Crossref CC BY 4.0 vor; page prints "Creative Commons Attribution (CC BY) license". Accepted.
- Line 8 (Lucañas, Lit Jr 2016). XML prints "Cristian C. Lucañas; Ireneo L. Lit Jr."; Crossref "Lucanas" (accent dropped), same order; title identical; Subterranean Biology 19: 51-64, no issue; issued 2016-09-28; Crossref CC BY 4.0 vor; XML prints the CC BY 4.0 sentence. Accepted.
- Line 9 (Vilkamaa, Hippa, Taylor 2011). XML "Pekka Vilkamaa, Heikki Hippa, Steven J. Taylor"; Crossref "Steven Taylor", same order; title identical; ZooKeys 135: 69-75, no issue; issued 2011-10-07; Crossref CC BY 3.0 vor; XML prints the CC BY 3.0 licence (tool summary). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All four species are described as new in the cited papers; names rest on the original descriptions (no checklist opened; Plazi treatments surfaced for three, not opened). Kinnaridae/Hemiptera (line 6, as in the title), Hydrometridae/Hemiptera (line 7, title), Nocticolidae/Blattodea (line 8; Nocticola treated in the paper's Blattodea), Sciaridae/Diptera (line 9; title and keywords print Sciaridae, so Camptochaeta is filed in the right family, not Cecidomyiidae or Mycetophilidae). Names faults 0.

## Trait keys

Lines 7 and 8 use ommatidia_count, not in check.py TRAITS but used on main (see audit-387) and flagged "new trait ommatidia_count (already used on main)". Line 6 uses eye_type. Line 9 uses eye_bridge_width_facets, new, with "new trait" and a definition in the note, so check.py passes. Judgement: the eye bridge (the dorsal band of facets joining the two compound eyes) and its width in facet rows is a standing character in sciarid descriptions, as this paper's own use and comparison ("by having a narrower eye bridge" against C. mutua and C. pellax) shows; the key names a real, printed measurement, so it is not invented. ommatidia_count would be wrong (1-2 is a width, not a count of facets in the eye), and eye_type would carry it only as free text. The key is a one-off that no view yet reads, which is a cost to the desk's vocabulary but not an error in the record. Trait-key faults 0.

## Duplicates

`git grep -i` on origin/main (a85bc4ef) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for Valenciolenda, fadaforesta, Spelaeometra, hypogea, gonzalezi, Camptochaeta, prolixa, eye_bridge and the DOI strings subtbiol.37.60483, ani13203199, subtbiol.19.9804, zookeys.135.1624: hypogea hits are Sinocyclocheilus (desk-d280) and a Passiflora searched row, unrelated; gonzalezi hits desk-d291.md only, which set the nymph count aside without filing it ("N. gonzalezi '3-4 facets' is for nymphs"). No filed repeat. All 687 remote research/desk-* and research/audit-* branches (d297, audit-388, audit-389 excluded), under docs/views/evidence, docs/tracks/progress and docs/views/audit, for the same species and DOI strings: no hit. Duplicate faults 0.

## Per line

### Line 6, Valenciolenda fadaforesta, eye_type none

"Compound eyes and ocelli absent." **Quote MATCH.** Type material matches the conditions: holotype male (Murciélagos cave, Vilamarxant, 5 April 2016); paratypes 1 male same data, 1 male and 1 female 30 April 2017, 1 male 24.VI.2017, 1 male Coves de Sant Josep, Castelló, 4 June 2016 (4 males, 1 female); additional material 5 fifth-instar nymphs. Nymph Head "Compound eyes absent, their former position recognizable as a slightly vaulted area dorsally of antennae." as the note says.

Error (location): the quoted sentence sits in the genus Description, under "Head (Fig. 2)", within "Valenciolenda Hoch & Sendra, gen. nov." (preceded by "Rostrum elongate; in repose well surpassing caudal margin of hind coxae; third joint shorter than second."). The species Description has no adult Head paragraph; it says "Configuration, shape and proportions of head and thorax as described for the genus." The record's where ("Valenciolenda fadaforesta sp. nov., Description, Head") names a heading that does not exist, and the note's "The genus Diagnosis repeats the state" reverses which text is the genus's. The attribution to the species stands (monotypic genus; the species Description refers to the genus; the species Diagnosis prints "compound eyes and ocelli absent," inside a longer sentence). Fixable.

**Line 6 FIXABLE.**

### Line 7, Spelaeometra hypogea, ommatidia_count 7

Male description, head paragraph: "Eye highly reduced, composed of just seven ommatidia, with two ocular setae" (piece; the trailing "(Figure 4D,E)" was not returned by the tool in either pass, and the Figure 4 caption reads "(E) Reduced eye with seven ommatidia."). **Quote MATCH** as far as returned. Per eye: the same paragraph reads "Dorsum of head with a pair of dorsal ridges rising near eyes", so the animal has two eyes and "Eye" is the singular of description; seven is odd, so a total over two eyes would need asymmetry the paper does not mention. "ommatidia per eye" is a fair reading, and the conditions say honestly that per eye is not stated outright. Type material: holotype male CEIOC 82865, paratypes 1 male and 1 female CEIOC 82866, Gruna do Enfurnado, 15 April 2010, as filed; female "Very similar to apterous male." with no eye sentence. Not counted: the female's eye is measured ("OL: 0.07, EYE: 0.01", same as the paratype male) and the note gives only the males' figures; optional addition below. Abstract and Discussion silent on eyes, as the note says.

**Line 7 MATCH.**

### Line 8, Nocticola gonzalezi, ommatidia_count 3-4 (nymphs)

Description, Nymphs, whole paragraph: "Nymphs. Similar to female. Opaque white. Eyes reduced to 3-4 distinct facets." Plain hyphen in "3-4" (tool reports hyphen-minus). **Quote MATCH**; Nymphs is the last sub-part of the N. gonzalezi Description, so the attribution and where are right. No instar given. Type material: holotype male BLA-00220 (13 May 2013); paratypes 1 female BLA-00221, 1 male BLA-00222, nymphs BLA-00223 and BLA-00224a-d (10.x.2013), Cave 5, Burdeos, Polillo Island, as in the conditions. Diagnosis "Compound eyes reduced, much smaller in female." and the Male sentence are in the note; the stage limit is stated. Value stays at the nymphs.

**Line 8 MATCH.**

### Line 9, Camptochaeta prolixa, eye_bridge_width_facets 1-2 (male)

Male Head: "Eye bridge 1–2 facets wide, medially lacking ommatidia, sometimes narrowed into stripe." **Quote MATCH**, en dash as printed. Holotype male Root Cave, 25 May 2006; 6 paratype males (Root Cave, Lehman Cave, Lehman Cave Annex, Cave 24); other material 1 female Lehman Cave; female "Slightly larger than male, wing length 3.0 mm, without diagnostic characters." with no eye sentence. Abstract "and in some specimens, reduction of the eye bridge" and the Discussion "tendency to a reduced eye bridge" are carried. Not counted: the quote's own qualifier "medially lacking ommatidia" means the bridge has no facets at its mid-line, which the value 1-2 does not show; the Discussion counts "11 specimens" while the material lists 8 (tool summary; the paper does not explain it); the Discussion's comparison "by having a narrower eye bridge" against C. mutua and C. pellax is not carried. Optional additions below.

**Line 9 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Valenciolenda fadaforesta, none | FIXABLE | where, note | quote MATCH (5) but it is the genus Description Head, not a species Head |
| 7 | Spelaeometra hypogea, 7 per eye | MATCH | none | quote MATCH (14); "eyes" plural elsewhere supports per eye; caveat stated |
| 8 | Nocticola gonzalezi, 3-4 (nymphs) | MATCH | none | quote MATCH (6); nymph stage and all types stated |
| 9 | Camptochaeta prolixa, bridge 1-2 facets (male) | MATCH | none | quote MATCH (12); sound new key; reduced-bridge variation carried |

Errors 1 of 4 audited records (25%). By kind: quotes 0; location 1 (line 6); value meaning 0; omitted variation 0; sample composition 0; bibliographic 0; licence 0; names 0; trait key 0; duplicates 0. Fixable; nothing unfixable, nothing held out. Verdict: merge lines 6-9 with the Replacement applied (line 6 required; lines 7 and 9 optional).

Unchecked: figures not viewed; the "(Figure 4D,E)" tail of the line 7 quote was not returned by the tool; the "11 specimens" discrepancy in line 9 rests partly on tool summary; no checklist opened for current status of the four names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 6:
- `where`: "Taxonomy, Valenciolenda fadaforesta sp. nov., Description, Head" -> "Taxonomy, Valenciolenda gen. nov., Description, Head (monotypic genus; the species Description says 'Configuration, shape and proportions of head and thorax as described for the genus.')"
- `note`: "The genus Diagnosis repeats the state inside a longer sentence." -> "The quoted sentence is in the genus Description, Head; the species adult Description has no Head paragraph and refers to the genus. The genus Diagnosis and the species Diagnosis ('compound eyes and ocelli absent,') repeat the state inside longer sentences."

Line 7 (uncounted):
- `note`: "maximum ocular width 0.01 mm in both, as measurements in the same paper." -> "maximum ocular width 0.01 mm in both, as measurements in the same paper; the paratype female measures OL 0.07, EYE 0.01 (no ommatidia count). The male head paragraph also has 'a pair of dorsal ridges rising near eyes', so the animal has two eyes."

Line 9 (uncounted):
- `conditions`: "Male description from holotype male" -> "The bridge is 'medially lacking ommatidia', so at the mid-line it has no facets; the Discussion says C. prolixa has 'a narrower eye bridge' than C. mutua and C. pellax. Male description from holotype male"
