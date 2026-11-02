# Audit 441: desk-d328 (8 evidence records, sensory_anatomy)

Auditor: fresh Opus, 1 November 2026. Scope: all 8 lines of `docs/views/evidence/desk-d328.jsonl` (1-based file lines). Rules: `/tmp/desk/rules.md` (31 Oct), `docs/views/research/SENSORY-ANATOMY.md`, `docs/views/research/BRIEF.md` record template, `tools/senses/check.py` (40-word limit, `len(quote.split())`). `check.py --require-evidence-kind` on the unit file: 8 records, 0 problems. WebSearch used: 6. Every page below was opened by WebFetch on the publisher's own site; Crossref read by single-DOI lookups (api.crossref.org/works/<doi>). No proxy, PMC, ResearchGate or workaround used.

## Unit-wide checks

- **Repeats of main.** `grep -r` of docs/ (evidence, audit, sheets, searched, wanted, gaps, progress) by species and by each DOI: no DOI of this unit occurs anywhere outside the unit. Vespa mandarinia and V. orientalis are on main only as `diel` (oa-4, Huang et al. 2024 Animals); Aromia bungii only as `sense_chemical` EAG (desk-d227, Insects 10(9): 274, a different paper); Hierodula patellifera only as a wanted/searched vision line (JEB circadian ERG). Scydosella, Cybister and Ophraella: absent. No repeats.
- **Trait key.** Legacy main files glomerulus and sensilla counts under `sense_chemical` (oa-9: sphingid glomeruli, Manduca sensilla). SENSORY-ANATOMY.md (31 Oct) moves new organ-only counts to `sensory_anatomy` with `evidence_kind`; the unit follows the newer rule. Accepted. `evidence_kind` is inconsistent inside the unit: a count of sensilla types is `anatomical_measurement` on lines 4 and 7 but `anatomical_presence` on lines 5 and 8. SENSORY-ANATOMY.md defines `anatomical_measurement` as "A count, dimension, arrangement or other structural measurement"; a number of types is a count, so lines 5 and 8 are misfiled (counted on line 8; line 5 already errs).
- **Author form.** rules.md requires author order exactly as printed and does not itself name a form, but the BRIEF.md record template is `"authors": "Surname A, Surname B"` and every desk unit merged from d310 to d327 uses that initials form (e.g. d322 "Li Q, Pei S-J, ..."; d325 "Seibert AM, Koblitz JC, ..."). This unit writes full given names on all 8 lines. Order is right on all 8 (checked against page bylines and Crossref). Audit 405 counted the initials form as a bibliographic error and gave the rate both ways; I do the same below.

## Per-line verdicts

**Line 1, Vespa mandarinia, 281 ± 2.9 glomeruli (Couto et al. 2021, Sci Rep 11: 20883). Fixable.**
- Crossref 10.1038/s41598-021-00280-z: Antoine Couto, Gérard Arnold, Hiroyuki Ai, Jean-Christophe Sandoz; title identical; Scientific Reports 11, issue 1, article 20883; issued 2021-10-22; CC BY 4.0 vor and tdm. The nature.com page byline prints "Gérard Arnold" (truncated list). The record spells "Gerard": error if full names are kept; moot once rendered as initials.
- Licence: the WebFetch text of the page ends inside the Discussion (offsets 40000, 55000, 75000 all stop at "At this stage, without func"), so neither Methods nor any licence sentence is retrievable; page shows no conflicting tag; Crossref CC BY 4.0 vor. Accepted under "page with no licence sentence + Crossref vor".
- Name: Vespa mandarinia Smith, 1852 is the heading valid name in Smith-Pardo, Carpenter and Kimsey 2020 (Insect Systematics and Diversity 4(3), Zenodo treatment 3847056), with V. magnifica Smith 1852 and the nobilis/sonani names as synonyms. Accepted.
- Quote: reassembled whole sentence is "It ranged from 231 ± 3.6 (mean ± SD, n = 3) glomeruli in V. orientalis to 281 ± 2.9 (n = 3) glomeruli in V. mandarinia with intermediate cases at 265 ± 7.2 glomeruli in V. velutina (n = 7) and 240 ± 2.9 glomeruli in V. crabro (n = 4) (Fig. 3a and Table 1)." That is 57 words, so it cannot be quoted whole; the 28-word quote starts at the sentence start, contains both values with "mean ± SD" and n, and marks its cut. No qualifier of these two values is dropped. Accepted. But `where` says only "the trailing figure reference" was cut; the cut also drops the V. velutina and V. crabro values. Fixable misdescription.
- Order/family: the Introduction prints "The genus Vespa (Hymenoptera, Vespidae) comprises 22 species of large eusocial wasps". The record says class, order and family are not printed and leaves them blank. Error, fixable (class is not printed).
- Caste: the Discussion (subsection "Worker macroglomeruli") prints "We conclude that only the ALs of V. mandarinia and V. crabro workers contain a macroglomerulus", so the V. mandarinia lobes reconstructed were workers'. Sex is not printed. The record's "caste not stated in the text read" is therefore out of date for this line (recommended fix, not counted). Wild-caught confirmed ("our wild caught hornets").
- Internal inconsistency, unreported: the paper gives V. velutina n = 6 in the staining section and n = 7 in the glomerulus count and Fig. 4 caption. It touches only the conditions aside (recommended note, not counted).
- Value says no more than the quote; grade m; anatomy only. Accepted.

**Line 2, Vespa orientalis, 231 ± 3.6 glomeruli (same paper). Fixable.** Same bibliographic, `where`, order/family and author-form faults as line 1. Vespa orientalis Linnaeus is an uncontested valid name (no check spent). Caste for V. orientalis is not stated in the retrievable text (the "Worker macroglomeruli" sentence names only V. mandarinia and V. crabro); the record's caveat stands for this line. Quote shared with line 1 and valid for this value.

**Line 3, Scydosella musawasensis, 131 antennal sensilla (Diakova and Polilov 2020, PeerJ 8: e10401). Fixable (author form only); OK otherwise.**
- Crossref: Anna V. Diakova, Alexey A. Polilov; title matches; PeerJ 8, e10401, issued 2020-11-23; CC BY 4.0, content-version unspecified. Page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License,". Accepted under the "unspecified + page-printed CC Attribution" rule.
- Quote "The antenna of S. musawasensis bears 131 sensilla (Figs. 2 and 3A)." read whole on the page; 12 words; contains the value.
- Table 2's n row (4, 61, 38, 2, 14, 2, 1, 7, 2) sums to 131; the per-type text/table conflict on BS1, BS2, SS2 is confirmed in my fetch too (text: 7, 2, 1; table: 1, 7, 2). Carrying only the total is correct. Page also prints "No intraspecific variation was found in the number and location of the sensilla" and no sex difference in number; Methods "A total of 15 females and 12 males were fixed"; "collected for earlier projects", no locality. All carried.
- Name: the page prints "Scydosella musawasensis (Hall, 1999) (Coleoptera: Ptiliidae)"; Polilov 2015 (ZooKeys) also writes "Scydosella musawasensis Hall, 1999". The launch prompt's "Hall 2000" does not match the printed authority; no authority is stored in the record, so nothing to change. Accepted name; order/family from the title correct.

**Line 4, Hierodula patellifera, 7 types and 4 subtypes (Wang et al. 2025, Insects 16(7): 655). Fixable (author form only); OK otherwise.**
- Crossref: Huan Wang, Yang Wang, Yang Liu, Geer Teni, Huiwen Li; title identical; Insects 16, 7, 655; issued 2025-06-24; CC BY 4.0 vor. Page citation line "Insects 2025, 16(7), 655"; same author order. No licence sentence in the body text; page metadata (meta dc.rights) read: https://creativecommons.org/licenses/by/3.0/. Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref).
- Quote (Simple Summary) read whole: "Seven types and four subtypes of sensilla were identified in nymphs and adults." Accepted.
- Section 3.2, now read in consecutive pieces: "Four subtypes of sensilla were identified in the nymphs (sensilla trichodea: StI, StII; sensilla campaniformia: ScaI, ScaII), and the undefined cuticular structure was only found on the tip of the 9th instar." and "The sensilla of adult antennae were almost consistent with that of nymphs, but the undefined cuticular structure was only observed in nymphs." The record's "almost consistent" and its decision not to split subtypes by stage already cover this; the note's "could not read" sentence can be updated (optional).
- Origin: oothecae collected April 2022 on dry branches along a road in Dongwan, Guangdong, reared in lab; carried. Name: Hierodula patellifera (Audinet-)Serville is the valid name in Plazi treatments (treatment.plazi.org, two treatments surfaced). Accepted.

**Line 5, Cybister japonicus, 5 sensilla types (Song et al. 2017, PLoS ONE 12(3): e0174643). Fixable.**
- Name: **Cybister japonicus Sharp is a junior synonym of Cybister chinensis Motschulsky, 1854.** Nilsson and Petrov 2007, "On the identity of Cybister chinensis Motschulsky, 1854 (Coleoptera: Dytiscidae)", Koleopterologische Rundschau 77: 43-48 (zobodat PDF), abstract: "thereby confirming its synonymy with C. japonicus SHARP, 1882, first published by ZAITZEV (1915)." Wikipedia's Cybister chinensis taxobox lists "Synonyms: Cybister japonicus Sharp, 1873". Filed under a synonym: error. Fixable by refiling under Cybister chinensis with the paper's name in the note. No Cybister record of any species on main.
- Bibliography: Crossref and the page agree (authors in order Li-Mei Song ... Li-Ping Ban; PLOS ONE 12(3) e0174643; 2017-03-30; CC BY 4.0 vor). Page citation line prints the initials form "Song L-M, Wang X-M, Huang J-P, Zhu F, Jiang X, Zhang S-G, et al. (2017)". Licence sentence printed in full on the page. Accepted.
- Order/family: Introduction prints "The diving beetle Cybister japonicus Sharp (Coleoptera: Dytiscidae) lives in stagnant waters". Record says not printed and leaves them blank. Error, fixable.
- Quote read whole in two pieces: "Five types of sensilla on the antennae were identified by scanning electron microscope (SEM) and transmission electron microscope (TEM)." Accepted. `evidence_kind` should be `anatomical_measurement` (see unit-wide).
- Origin: "obtained from the Huangsha Aquatic Products Trading Market in Guangzhou"; "Ten insects for each gender were used for SEM observations." Carried.

**Line 6, Cybister japonicus, sex difference in sensilla counts (same paper). Fixable.**
- Same synonym, order/family and author-form faults as line 5.
- Quote: my fetch returned the sentence as "In general, males have a larger number of each type of sensilla than in females except the type I s. coeloconica (P<0.05)." ending with a full stop and no table reference. The record ends "(P<0.05) …" and says a trailing table reference was cut. I cannot tell from the summariser whether a "(Table 1)" follows; both renderings keep every qualifier, so not counted. Recommend running quotecheck.py against the page.
- Sample: Methods state counts were compared with "independent Student's t-tests" and give "Ten insects for each gender were used for SEM observations" and ten antennae per sex for light microscopy, but do not say how many antennae were counted for Table 1 (table body not retrievable). The record's `method` presents the two tens as the counting sample. Recommended wording fix, not counted. (My own inference, not printed: per-type means such as 66.33 and 77.67 end in thirds, which would fit three antennae per sex.)
- Value matches quote; per-type figures kept in conditions as unquoted context, labelled so. Accepted on content.

**Line 7, Aromia bungii, 12 sensilla types (Di Palma et al. 2019, Insects 10(4): 88). Fixable (author form only); OK otherwise.**
- Crossref: Antonella Di Palma, Marco Pistillo, Raffaele Griffo, Antonio P. Garonna, Giacinto S. Germinara; Insects 10, 4, 88; issued 2019-03-28; CC BY 4.0 vor. Page citation "Insects 2019, 10(4), 88", same order. No licence sentence in body; page metadata read: CC BY 3.0. Accepted.
- Quote read whole: "Twelve different types of sensilla were morphologically described on the antennae of A. bungii." Accepted.
- Contradiction confirmed and carried: Abstract "three multiporous olfactory receptors", Conclusions "two". ST1 only in males: carried. Origin: larvae in logs from cut-down trees at Marigliano (Naples, Campania, Italy), 11 April 2017, adults reared in cages: carried. Name valid (Aromia bungii (Faldermann, 1835), also accepted on main in desk-d227). Order/family from title correct.

**Line 8, Ophraella communa, 6 sensilla types (Ma et al. 2022, Insects 13(2): 183). Fixable.**
- Crossref: Chao Ma, Yang Yue, Yan Zhang, Zhen-Ya Tian, Hong-Song Chen, Jian-Ying Guo, Zhong-Shi Zhou; Insects 13, 2, 183; issued 2022-02-09; CC BY 4.0 vor. Page same order, "Insects 2022, 13(2), 183". Body prints no licence sentence; meta dc.rights read: CC BY 3.0. Accepted.
- Quote reassembled from two consecutive pieces, whole sentence, 25 words. Accepted. Page also prints "Both male and female antennae had all six types of sensilla, and no sexual dimorphism was noted in sensillar types or distribution." Carried in substance. No contrary type count in Results or Discussion.
- Origin: "Live O. communa beetles were obtained from the Institute of Plant Protection, China Academy of Agriculture Sciences" and lab-reared on A. artemisiifolia: carried.
- Name: Ophraella communa LeSage, 1986 valid (Plazi treatment, regional checklists). Accepted.
- `evidence_kind` `anatomical_presence` for a count of six types: error, fixable (filing convention; the paper's rough density classes are not the value filed).

## Counts

Records audited 8; held out 0; unfixable 0.

- Counting the author-name form as an error (audit 405 precedent): **8 of 8 lines in error, all fixable**.
- Treating the author form as uncounted: **5 of 8 lines in error (lines 1, 2, 5, 6, 8)**, all fixable. By kind: names 2 (lines 5, 6: junior synonym Cybister japonicus); bibliographic 2 (lines 1, 2: "Gerard" for printed "Gérard"); higher taxa omitted though printed 4 (lines 1, 2, 5, 6); `where` misdescribes the cut 2 (lines 1, 2); filing convention 2 (lines 5, 8: evidence_kind), line 5 already counted. Quotes 0, value exceeding quote 0, licence 0, duplicates 0, omitted contrary results 0.

Lines 3, 4 and 7 are clean apart from the author form.

## Replacement

All edits are raw substring replacements inside the single JSON line named; every old string occurs exactly once in that line (checked by script). Replacements touching more than one field are listed per field.

Line 1 (Vespa mandarinia):
- `"authors": "Antoine Couto, Gerard Arnold, Hiroyuki Ai, Jean-Christophe Sandoz"` -> `"authors": "Couto A, Arnold G, Ai H, Sandoz J-C"`
- `"rank": "species", "trait"` -> `"rank": "species", "order": "Hymenoptera", "family": "Vespidae", "trait"`
- `with the trailing figure reference cut)` -> `cut after 'V. mandarinia', which drops the V. velutina and V. crabro values and the figure and table reference)`
- `Class, order and family are not printed in the text read, so they are left out.` -> `Order and family as printed in the Introduction ('The genus Vespa (Hymenoptera, Vespidae) comprises 22 species'); class is not printed.`
- `the four authors are from Crossref.` -> `the four authors are from Crossref, and the page prints the second as Gérard Arnold.`

Line 2 (Vespa orientalis): the same five replacements as line 1, verbatim.

Line 3 (Scydosella musawasensis):
- `"authors": "Anna V. Diakova, Alexey A. Polilov"` -> `"authors": "Diakova AV, Polilov AA"`

Line 4 (Hierodula patellifera):
- `"authors": "Huan Wang, Yang Wang, Yang Liu, Geer Teni, Huiwen Li"` -> `"authors": "Wang H, Wang Y, Liu Y, Teni G, Li H"`

Line 5 (Cybister, sensilla types):
- `"taxon": "Cybister japonicus"` -> `"taxon": "Cybister chinensis"`
- `"rank": "species", "trait"` -> `"rank": "species", "order": "Coleoptera", "family": "Dytiscidae", "trait"`
- `"evidence_kind": "anatomical_presence"` -> `"evidence_kind": "anatomical_measurement"`
- `"authors": "Li-Mei Song, Xue-Min Wang, Jian-Ping Huang, Fang Zhu, Xiang Jiang, Shan-Gan Zhang, Li-Ping Ban"` -> `"authors": "Song L-M, Wang X-M, Huang J-P, Zhu F, Jiang X, Zhang S-G, Ban L-P"`
- `Class, order and family are not printed in the pages read, so they are left out.` -> `Order and family as printed in the Introduction ('Cybister japonicus Sharp (Coleoptera: Dytiscidae)'). The paper uses Cybister japonicus Sharp, a junior synonym of Cybister chinensis Motschulsky, 1854 (Nilsson and Petrov 2007, Koleopterologische Rundschau 77: 43-48, confirming Zaitzev 1915); filed under the accepted name.`

Line 6 (Cybister, sex difference):
- `"taxon": "Cybister japonicus"` -> `"taxon": "Cybister chinensis"`
- `"rank": "species", "trait"` -> `"rank": "species", "order": "Coleoptera", "family": "Dytiscidae", "trait"`
- `"authors": "Li-Mei Song, Xue-Min Wang, Jian-Ping Huang, Fang Zhu, Xiang Jiang, Shan-Gan Zhang, Li-Ping Ban"` -> `"authors": "Song L-M, Wang X-M, Huang J-P, Zhu F, Jiang X, Zhang S-G, Ban L-P"`
- `Licence as in the other Cybister record.` -> `Licence as in the other Cybister record. The paper uses Cybister japonicus Sharp, a junior synonym of Cybister chinensis Motschulsky, 1854 (Nilsson and Petrov 2007, Koleopterologische Rundschau 77: 43-48); filed under the accepted name; order and family as printed in the Introduction.`

Line 7 (Aromia bungii):
- `"authors": "Antonella Di Palma, Marco Pistillo, Raffaele Griffo, Antonio P. Garonna, Giacinto S. Germinara"` -> `"authors": "Di Palma A, Pistillo M, Griffo R, Garonna AP, Germinara GS"`

Line 8 (Ophraella communa):
- `"authors": "Chao Ma, Yang Yue, Yan Zhang, Zhen-Ya Tian, Hong-Song Chen, Jian-Ying Guo, Zhong-Shi Zhou"` -> `"authors": "Ma C, Yue Y, Zhang Y, Tian Z-Y, Chen H-S, Guo J-Y, Zhou Z-S"`
- `"evidence_kind": "anatomical_presence"` -> `"evidence_kind": "anatomical_measurement"`

If the owner keeps full given names instead of initials, drop the author replacements on lines 3, 4, 7, 8, 5 and 6, and on lines 1 and 2 use `"authors": "Antoine Couto, Gerard Arnold, Hiroyuki Ai, Jean-Christophe Sandoz"` -> `"authors": "Antoine Couto, Gérard Arnold, Hiroyuki Ai, Jean-Christophe Sandoz"`.

## Optional fixes (not counted)

- Line 1 `conditions`: `the sex/caste of the counted animals is not stated in the text read, and the Methods section was not read` -> `the Discussion states 'only the ALs of V. mandarinia and V. crabro workers contain a macroglomerulus', so the V. mandarinia lobes counted were workers'; sex is not printed and the page text ends in the Discussion, so Methods could not be read; the paper gives V. velutina n = 6 in the staining section and n = 7 in the count`
- Line 2 `conditions`: `the sex/caste of the counted animals is not stated in the text read, and the Methods section was not read` -> `the caste of the V. orientalis animals is not stated in the retrievable text, which ends in the Discussion, so Methods could not be read; the paper gives V. velutina n = 6 in the staining section and n = 7 in the count`
- Line 4 `note`: `The Section 3.2 sentence on subtypes names four subtypes in nymphs; I could not read the whole sentence, so the split of subtypes between nymphs and adults is not carried.` -> `Section 3.2 states the four subtypes (StI, StII, ScaI, ScaII) were identified in the nymphs and that adult sensilla 'were almost consistent with that of nymphs', with an undefined cuticular structure only in nymphs; no separate adult subtype list is printed.`
- Line 6 `method`: `(the Methods give ten antennae per sex for light microscopy and ten insects per sex for SEM)` -> `(the Methods give ten antennae per sex for light microscopy and ten insects per sex for SEM, compare counts with Student's t-tests, and do not state how many antennae were counted per sex)`
- Line 6 `quote`: run quotecheck.py; if the page sentence ends at "(P<0.05)." with no table reference, drop the trailing " …".
