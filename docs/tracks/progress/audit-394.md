# audit-394: desk-d302, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d302 files present untracked in the worktree (docs/tracks/progress/desk-d302.md and docs/views/evidence/desk-d302.jsonl, 6 lines; neither committed here, neither edited). Line numbers are the file's (1-based). HEAD equals origin/main (0c6d4f2d). `python3 -I tools/senses/check.py | grep 'd302\.'`: "docs/views/evidence/desk-d302.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 7, 7, 7, 11, 14, 11, all within 40; no non-ASCII characters in any quote.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=3726, ?id=3442, ?id=13802, ?id=47322; zookeys.pensoft.net/article/3744/download/xml/; www.mdpi.com/2075-4450/16/8/806 (two passes) and www.mdpi.com/2075-4450/16/12/1251 (the correction); Crossref single-DOI lookups api.crossref.org/v1/works/ for all six DOIs. Plazi, BHL, bionames, zoobank, PMC, GBIF, Zenodo and repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Yin, Hlaváč, Li 2013). Page and Crossref Zi-Wei Yin, Peter Hlaváč (Crossref Hlavac), Li-Zhen Li; title identical; ZooKeys 275: 23-65, no issue; issued 2013-03-04; Crossref CC BY 3.0 vor; page prints the CC-BY 3.0 sentence. Accepted.
- Line 2 (Yin, Li 2012). Page and Crossref Zi-Wei Yin, Li-Zhen Li; ZooKeys 251: 83-118, no issue; issued 2012-12-18; Crossref CC BY 3.0 vor; page prints the CC-BY 3.0 sentence. Title as filed matches the metadata form (single spaces, curly apostrophe); the body prints double spaces inside the final parenthesis, which the note records. Accepted.
- Line 3 (Jiang, Yin 2017). Page and Crossref Ri-Xin Jiang, Zi-Wei Yin; title identical; ZooKeys 694: 11-30; issued 2017-08-28; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 4 (Lohaj, Čeplík, Lakota 2013). Page and Crossref Roman Lohaj, Dávid Čeplík, Ján Lakota; title identical; ZooKeys 278: 91-104; issued 2013-03-21; Crossref CC BY 3.0 vor; page prints the CC-BY 3.0 sentence. Accepted. The note says Crossref spells the second author "Čepelík"; Crossref gives "Čeplík", the same as the page (uncounted note fix below).
- Line 5 (Fang, Li, Wang, Tian 2020). Page and Crossref Jie Fang, Wenbo Li, Xinhui Wang, Mingyi Tian; title identical; ZooKeys 923: 33-50; issued 2020-04-01; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 6 (Sitar, Kenesz, Barbu-Tudoran, Moldovan 2025). Page Cristian Sitar, Marius Kenesz, Lucian Barbu-Tudoran, Oana Teodora Moldovan (Crossref Oana Moldovan); title identical; Insects 16(8): 806; issued 2025-08-04; Crossref CC BY 4.0 vor; the article page prints no licence sentence in the text returned (metadata rights URL CC BY 3.0). Accepted under "publisher page with no licence sentence + Crossref CC licence vor" and "CC BY 3.0 page vs CC BY 4.0 Crossref". The correction (Insects 16(12): 1251) prints the CC BY 4.0 sentence.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All six species are described as new in the cited papers ("sp. n." or "sp. nov."); names rest on the original descriptions. One search for later synonymy or transfer of Duvalius gejzadunayi returned only the original paper and its copies. Families: Staphylinidae (Pselaphinae, lines 1 to 3, as in the titles), Carabidae (Trechini, lines 4, 5), Leiodidae (line 6), order Coleoptera throughout; right.

Line 6: the subgenus name Pachyandrus is not the name first printed. The correction Insects 16(12): 1251 (published 10 December 2025) states "Because the name Pachyphallus [1] is preoccupied we propose replacing it with Pachyandrus." and "all mentions of Pachyphallus throughout the article need to be revised and replaced with Pachyandrus."; the article page now prints Pachyandrus and "Correction published on 10 December 2025, see Insects 2025, 16(12), 1251." The record does not mention the replacement name or the correction, and its note calls Leptodirini a subfamily; Leptodirini is a tribe (of Cholevinae, Leiodidae). Counted with line 6.

## Trait keys

ommatidia_count (lines 1 to 3) is already on main (desk-d270, d271, d272, d274, d291 and others, units "ommatidia/eye" or "ommatidia per compound eye"); it is absent from the check.py key list, which the notes say. The papers print "facets"; in a beetle compound eye each corneal facet is the lens of one ommatidium, so a facet count is an ommatidium count, and the notes state the assumption openly. Key accepted. "New trait" in the notes is loose wording for a key already on main (no fix asked). eye_type (lines 4 to 6) is on main. Trait-key faults 0.

## Duplicates

`git grep` on origin/main (0c6d4f2d) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for Dayao emeiensis, tendothorax, zhouchaoi, gejzadunayi, huangshanicus, ponoricum and the six DOI strings: one hit only, "D. emeiensis" in docs/views/searched/sweep-47.jsonl line 12, which is Diastrophus emeiensis (a gall wasp), not this beetle. All 1,482 remote branches except research/desk-d302 grepped for the same strings in every docs/ file that differs from origin/main on that branch (files equal to main are covered by the main grep): no hit. The same pipeline run on research/desk-d302 finds its own two files, so the method returns hits where they exist. Duplicate faults 0.

## Per line

### Line 1, Dayao emeiensis, ommatidia_count about 15 facets per eye (female)

Female description: "Eyes each composed of about 15 facets." **Quote MATCH**; male description "eyes each composed of about 25 facets." Holotype ♂ and paratype ♀, E'mei Shan, 2200 m, leaf litter sifted, 2012.vii.23. Abstract and Diagnosis without eye text (tool summary). Value, per-eye unit, "about" and the female eye field right.

Fault: the conditions call the Nibashan specimen "a further female" with about 20 facets per eye, which reads as variation within this species. The Notes say only that "A female specimen (in pcPH) from Nibashan Mt., (Daxiangling Mts., ca. 50 km. W E'meishan)" "has each eye composed of about 20 facets." and add "An associated male from Nibashan is needed for species identification." The specimen is not identified as D. emeiensis, so the record overstates the variation. Fixable.

**Line 1 FIXABLE.**

### Line 2, Linan tendothorax, ommatidia_count about 16 facets per eye (female)

Female description: "Eyes each composed of about 16 facets." **Quote MATCH**; male "eyes each composed of about 17 facets." Type material 3 ♂♂, 14 ♀♀: holotype ♂ Xue Shan, 2510 m, 10.IX.2009; paratypes 1 ♂, 7 ♀♀ same data, 1 ♀ same data leg. Wrase, 3 ♀♀ Laobei Shan, 3 ♀♀ Wuliang Shan, 1 ♂ Ailao Shan. Diagnosis, Comparative notes and Abstract without eye text (tool summary). The conditions leave the Wrase female inside "further paratypes" without naming it; the total 3 males and 14 females is right.

**Line 2 MATCH.**

### Line 3, Batrisodes zhouchaoi, ommatidia_count about 55 facets per eye (male)

Male description: "Each eye composed of about 55 facets." **Quote MATCH.** "Female. Unknown." Holotype ♂ ant nest under rock, paratype ♂ ant colony under bark, Zipingpu, 1180 m, 03.iv.2017; host ants Lasius sp. and Nylanderia sp. (tool summary). Diagnosis without eye text; no Comments. Other species in the paper: males about 50 to 75, females about 40 to 50 (tool summary), as the conditions say.

**Line 3 MATCH.**

### Line 4, Duvalius gejzadunayi, eye_type reduced

Description: "Eyes completely reduced, in some specimens present as a dark spot." **Quote MATCH.** Abstract "totally reduced eyes"; Diagnosis "anophthalmous trechine species"; key "eyes totally absent"; no Variability section; holotype ♂ and 6 ♂♂, 7 ♀♀ paratypes, Pećina u Dubokom potoku cave, traps 17.4.-11.8.2009. All as filed; the value keeps the dark-spot variation and the conditions give the contrasting wording.

Uncounted: the note's claim that Crossref spells the second author "Čepelík" is wrong (Crossref "Čeplík").

**Line 4 MATCH.**

### Line 5, Wanoblemus huangshanicus, eye_type none (eyeless)

Diagnosis of the species (the whole paragraph): "A rather small eyeless trechine beetle, yellowish brown, body thin and elongate, sparsely pubescent." **Quote MATCH.** It is the species Diagnosis under "Wanoblemus huangshanicus Tian & Li, sp. nov.", not a genus diagnosis or a comparison (the genus dates from an earlier paper and has no diagnosis here). Abstract "(an anophthalmic trechine)"; Description and Remarks without eye text (tool summary). Type material 1 ♂ holotype 2016-IV-22, paratypes 3 ♂♂, 2 ♀♀ same date and 12 ♂♂, 15 ♀♀ 2018-XII-24, Shenxian Dong, 33 in all, as filed. "where" names the heading.

**Line 5 MATCH.**

### Line 6, Protopholeuon (Pachyandrus) ponoricum, eye_type none (without eyes)

Description: "Head: Longer than wider (HL/HW: 1:1.18), non-retractable, without eyes (Figure 6J,K)." **Quote MATCH**; heading "3.4. Protopholeuon (Pachyandrus) ponoricum Sitar & Moldovan sp. nov.". Holotype ♂ November 2018; paratypes 6 ♀♀ November 2018, 1 ♂, 4 ♀♀ 25 October 2021, Ponor Cave. Abstract, diagnoses and Discussion without eye text; the genus redescription (3.1) "non-retractable, without eyes, with a strongly expressed occipital carina."; the other new taxa have no Head sentence (tool summary). Value and conditions right.

Fault: the subgenus Pachyandrus is a replacement name for the preoccupied Pachyphallus, published in the correction Insects 16(12): 1251 (10 December 2025); the record is silent on it and its note calls Leptodirini a subfamily (it is a tribe of Cholevinae). Fixable.

**Line 6 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Dayao emeiensis, about 15 facets per eye (female) | FIXABLE | conditions | Nibashan female given as variation though the paper leaves its identity open |
| 2 | Linan tendothorax, about 16 facets per eye (female) | MATCH | | quote, 3 ♂♂ 14 ♀♀, male 17 right |
| 3 | Batrisodes zhouchaoi, about 55 facets per eye (male) | MATCH | | quote, 2 males, female unknown right |
| 4 | Duvalius gejzadunayi, eyes reduced | MATCH | | quote, dark-spot variation and contrasting wording given |
| 5 | Wanoblemus huangshanicus, eyeless | MATCH | | species Diagnosis, 33 type specimens right |
| 6 | Protopholeuon (Pachyandrus) ponoricum, without eyes | FIXABLE | note | replacement name from the correction omitted; Leptodirini called a subfamily |

Errors: 2 of 6 records (33%); 2 fixable (lines 1, 6), 0 held out. Verdict: **ACCEPT AFTER REPLACEMENT** (lines 2 to 5 as filed; lines 1 and 6 with the replacements below).

## Replacement

Each old string is copied from the desk file and occurs once in its field in the line named.

Line 1:
- `conditions`: "and the Notes section gives about 20 facets per eye for a further female from Nibashan Mt.;" -> "and the Notes section gives about 20 facets per eye for a female from Nibashan Mt. (ca. 50 km W of E'meishan) that is not identified to species ('An associated male from Nibashan is needed for species identification.'), so it is not variation within D. emeiensis;"

Line 6:
- `note`: "Subfamily Leptodirini is placed in Leiodidae as printed in the title." -> "Tribe Leptodirini (Cholevinae) of Leiodidae as printed in the title. The subgenus name Pachyandrus replaces the preoccupied Pachyphallus first printed in the article (correction Insects 16(12): 1251, 10 December 2025: 'Because the name Pachyphallus [1] is preoccupied we propose replacing it with Pachyandrus.'); the article page read prints Pachyandrus."

Line 4 (uncounted):
- `note`: "Crossref spells the second author Čepelík where the page byline prints Čeplík (page spelling used); order matches;" -> "Crossref and the page byline both spell the second author Čeplík; order matches;"
