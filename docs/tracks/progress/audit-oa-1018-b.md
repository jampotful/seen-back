# Audit oa-1018-b: the OA reading pass on `agent/oa-read-b`

Branch audited: `agent/oa-read-b` at `20860f5a` (267 evidence lines added to `docs/views/evidence/oa-2.jsonl`, diff against `main` at `89d023b1`). Prompt: `docs/tracks/prompts/oa-audit.md`, with the launch settings: 30 lines, `random.seed(1018)`, fetch branch `run/oa/audit-1018-b`.

## Sample (drawn before any record was read)

All 267 added lines in diff order, then `random.seed(1018)` and `random.sample(lines, 30)`:

1. docs/views/evidence/oa-2.jsonl:3516
2. docs/views/evidence/oa-2.jsonl:3517
3. docs/views/evidence/oa-2.jsonl:3366
4. docs/views/evidence/oa-2.jsonl:3427
5. docs/views/evidence/oa-2.jsonl:3477
6. docs/views/evidence/oa-2.jsonl:3578
7. docs/views/evidence/oa-2.jsonl:3410
8. docs/views/evidence/oa-2.jsonl:3525
9. docs/views/evidence/oa-2.jsonl:3425
10. docs/views/evidence/oa-2.jsonl:3372
11. docs/views/evidence/oa-2.jsonl:3513
12. docs/views/evidence/oa-2.jsonl:3405
13. docs/views/evidence/oa-2.jsonl:3352
14. docs/views/evidence/oa-2.jsonl:3464
15. docs/views/evidence/oa-2.jsonl:3413
16. docs/views/evidence/oa-2.jsonl:3328
17. docs/views/evidence/oa-2.jsonl:3568
18. docs/views/evidence/oa-2.jsonl:3544
19. docs/views/evidence/oa-2.jsonl:3545
20. docs/views/evidence/oa-2.jsonl:3424
21. docs/views/evidence/oa-2.jsonl:3561
22. docs/views/evidence/oa-2.jsonl:3354
23. docs/views/evidence/oa-2.jsonl:3467
24. docs/views/evidence/oa-2.jsonl:3559
25. docs/views/evidence/oa-2.jsonl:3414
26. docs/views/evidence/oa-2.jsonl:3408
27. docs/views/evidence/oa-2.jsonl:3554
28. docs/views/evidence/oa-2.jsonl:3342
29. docs/views/evidence/oa-2.jsonl:3579
30. docs/views/evidence/oa-2.jsonl:3566

## Texts and method

The 30 lines come from 7 papers, oa-2 entries 40, 46, 49, 51, 62, 74 and 75. They were fetched by `run/oa/audit-1018-b` (commit `2a156292`: `ci/oa/pub.pem` replaced by this audit's key, `ci/oa/list.jsonl` cut to those 7 lines), returned as `runs/oa/9-oa-2` on `ci`: all 7 read (2 Europe PMC XML, 5 PDF), 7 decrypted, 0 checksum mismatches. Key and texts stayed outside the repository, in a subfolder of `/tmp/oa` of their own because `/tmp/oa` already held another agent's files.

Each record was run through `quotecheck.py` against its text (25 verbatim, 3 table, 2 failed; both failures are typographic, see below), then read against the sentence or table row around the quote, the table heads and footnotes, and the reference it cites. Fields checked: quote, value, taxon, grade and partial. Typographic differences count as `confirm` (audit 31).

Grades follow the research rule, as the control room directed during this audit: BRIEF line 62 and `docs/views/audit/SAMPLE.md` ("The rule decided"). A value the paper gives for the record's own taxon is graded by what it reports, whether this paper measured it or cites it. That covers a cited study on the named species and a statement the paper makes about the record's group as a whole. `g` stands only for a taxon mismatch: a relative, or a subset standing for the record's group ("at least some", "most", "the few species studied", a data set of N species). A value the paper predicts rather than measures is `i`. This replaces the narrower wording of `oa-read.md` ("`m` only when the taxon is one named species measured in this paper", group values "`g` at most"). Records whose only fault is that narrower wording are counted as errors and also given as a separate number.

## Verdicts

| # | id (file:line) | taxon / trait | grade | verdict | reason |
|---|---|---|---|---|---|
| 1 | oa-2:3516 | Salticidae / eyes_count 4 | g, partial | correct: grade to m | Introduction sentence from its start, end cut marked. It says "salticids have four pairs of eyes" of the family as a whole and names no subset, so the rule gives m. Narrow wording |
| 2 | oa-2:3517 | Saltafresia / eye_role PME | g, partial | confirm | Verbatim with a marked cut; quotecheck fails only because the PDF prints "(Blest 1983; Land 1985)" without the inner spaces. "Most salticids in the clade" and "the few species studied" make it a subset claim, so g stands |
| 3 | oa-2:3366 | Marchantia paleacea / sense_light_nonvisual | m, partial | correct: taxon | Sentence verbatim and value right. The paper prints only "Marchantia paleacea var. diptera" (ref 15); the record raised it to the species and put the variety in note |
| 4 | oa-2:3427 | Erythrolamprus poecilogyrus / acuity_cpd 1.7 | m | confirm | Table 3 row verbatim; 1.7 is the hexagonal-array column (*), as `method` says |
| 5 | oa-2:3477 | Hasarius adansoni / receptor_classes UV, green | m | correct: grade to i | Sentence verbatim (spacing only). The paper infers the classes from the opsins it localized (RH1 "putatively green-sensitive", RH3 UV) and says its findings "agree with UV-G dichromacy", so the value is a prediction |
| 6 | oa-2:3578 | birds / sense_magnetic (model) | i | confirm | Results sentence verbatim. "Disk-shaped" comes from the sentence before, as `note` says. Model result, so grade i and partial false |
| 7 | oa-2:3410 | Sibynomorphus mikanii / diel | m, partial | confirm | Table 1 row verbatim, N = primarily nocturnal. The footnote "based on [77, 79]" (Marques et al. 2001; Torello-Viera and Marques 2017) makes it partial; cited on the record's own species, so m |
| 8 | oa-2:3525 | Anolis cristatellus / oil_droplets green 0.7988 | m | confirm | Two Results sentences, each quoted from its start, cuts marked; 0.7988 is the second green proportion, A. cristatellus; the abstract gives 80% |
| 9 | oa-2:3425 | Erythrolamprus miliaris / fovea | m | confirm | Table 4 row verbatim, "HS"; Results: a poorly defined horizontal streak, temporal |
| 10 | oa-2:3372 | Ceratodon purpureus / sense_light_nonvisual | m | confirm | Sentence verbatim: four known phytochromes and "the novel C. purpureus phytochrome discovered here" (CpPHY2_4) |
| 11 | oa-2:3513 | Salticidae / eye_role secondary eyes | g, partial | correct: grade to m | Verbatim with marked cuts. The secondary eyes' role is stated for jumping spiders in general, with no subset named, so the rule gives m. Narrow wording |
| 12 | oa-2:3405 | Atractus reticulatus / fovea | m | confirm | Table 4 row verbatim, "AC—dorsal"; Results: anisotropic area centralis, dorso-temporal |
| 13 | oa-2:3352 | chlorophytes / sense_light_nonvisual | g | confirm | Sentence verbatim. The value is the result in 96 transcriptomes, which stand for the group, so g; the paper's own mining, so partial false |
| 14 | oa-2:3464 | Trachemys scripta elegans / fovea | m, partial | confirm | Sentence verbatim. Refs 39 and 40 (Granda and Haden 1970; Grötzner 2005) studied this turtle, so m and partial. Rank label: uncounted row below |
| 15 | oa-2:3413 | Sibynomorphus mikanii / fovea none | m | confirm | Table 4 row verbatim, "Diffuse—central". The paper calls it a scattered, nondefined distribution, so "none" stands; `note` gives the central bias |
| 16 | oa-2:3328 | Lupinus angustifolius / sense_thermal | m, partial | confirm | Review sentence verbatim with a marked cut; Nelson et al. (2010) worked on the record's species |
| 17 | oa-2:3568 | birds / sense_magnetic field strength | g, partial | correct: grade to m | Sentence verbatim (spacing only). It is said of "the avian compass" in general, with no subset of birds named, so the rule gives m. Narrow wording |
| 18 | oa-2:3544 | Anolis / oil_droplets C1 | g, partial | confirm | Sentence verbatim. The source is an MSP study of 17 Caribbean anole species (Loew et al. 2002) standing for the genus, so g |
| 19 | oa-2:3545 | Anolis / oil_droplets C2 | g, partial | confirm | Same sentence and study |
| 20 | oa-2:3424 | Erythrolamprus miliaris / acuity_cpd 2.0 | m | confirm | Table 3 row verbatim; 2.0 is the square-array column (**) |
| 21 | oa-2:3561 | plants / sense_chemical | g, partial | confirm | Sentence from its start, end cut marked. The meta-analysis's 33 species stand for plants, so g; partial for the meta-analysis |
| 22 | oa-2:3354 | Volvox carteri / sense_light_nonvisual | m | confirm | Sentence verbatim; the paper searched the genome itself (Methods: BLASTp) |
| 23 | oa-2:3467 | Choloepus didactylus / fovea | m, partial | requote | The quote joins the start of one sentence to the middle of the next, so it reads as one sentence the paper does not contain. Value (vertical streak), m (ref 43 is on this sloth) and partial right |
| 24 | oa-2:3559 | plants / sense_chemical 39 of 48 | g, partial | confirm | Sentence verbatim. The data set covers 33 species in 15 families (Methods), which stand for plants, so g |
| 25 | oa-2:3414 | Sibynomorphus neuwiedi / diel | m, partial | confirm | Table 1 row verbatim; as #7 |
| 26 | oa-2:3408 | Dipsas albifrons / acuity_cpd 1.4 | m | confirm | Table 3 row verbatim; 1.4 is the square-array column (**) |
| 27 | oa-2:3554 | Anolis / oil_droplets C1 SWS, C2 UVS | g, partial | confirm | Sentence verbatim. Loew et al. (2002) is the 17-species study the Introduction describes, so g stands |
| 28 | oa-2:3342 | Porphyridium purpureum / sense_light_nonvisual | m | confirm | Sentence verbatim; the paper's own BLASTp search of the published genome |
| 29 | oa-2:3579 | birds / sense_magnetic ΔΩ (model) | i | confirm | The PDF text prints the sentence in a symbol font ("DU ¼ 89 , 88 , 87 , 85", "h ¼ 1, 2, 3, 5"), so quotecheck fails; the words and every number match. Model result, so grade i |
| 30 | oa-2:3566 | birds / sense_magnetic head-scanning | g, partial | confirm | Sentence verbatim (spacing only). "At least some migratory birds" is a subset, so g; Mouritsen, Feenders and Kropp 2004 (ref 28) |

## Errors and rate

- 30 records drawn, all 30 checked against their papers, none unverifiable.
- Errors: 6 of 30, **20%** (95% Wilson interval 9.5% to 37.3%). By verdict: 5 `correct`, 1 `requote`, 0 `retract`. By field: grade 4, taxon 1, quote 1. No value and no partial flag was wrong.
- Narrow grade wording, counted above and given separately as asked: **3 of 30** (oa-2:3513, 3516, 3568), group records graded `g` where the rule gives `m`. The mechanical regrade fixes these.
- Without those 3: **3 of 30, 10%** (3.5% to 25.6%): oa-2:3477 (a predicted value graded `m`), oa-2:3366 (taxon) and oa-2:3467 (quote).
- Both rates are above the 5% rule.

## Uncounted rows

| id | field | finding |
|---|---|---|
| all 30 | source | No metadata fault. All seven source objects equal `ci/oa/sources-r1.jsonl`, with the gaps filled from the papers: Weller and Ortega "6: 207"; Hauzman et al. "chapter 5, pp. 101-126", which matches the chapter's page numbers. |
| oa-2:3477, 3513, 3516, 3517 (entry 51); 3566, 3568, 3578, 3579 (entry 75) | url | Copied from sources-r1 as instructed. The PMC address uses the bare number (`pmc/articles/11756594`, `pmc/articles/2895366`) where PMC's own form is `PMC11756594`. Not opened, because the proxy refused it. |
| oa-2:3464 | rank | "species" for the trinomial Trachemys scripta elegans. The branch labels all three of its trinomials "species", and the whole log set is split about evenly (96 "species", 100 "subspecies"). |
| oa-2:3517, 3579 | quote | Fail `quotecheck.py` against this audit's texts on typography only: spaces inside parentheses (3517) and a symbol font in the PDF (3579). |

## Fault patterns

1. **Grade by rank.** In the whole branch, all 170 records at species rank are `m` and the 4 model results are `i`. The other 93 are all `g`: 85 at a rank above species, and 8 named by a common name (rats, mice, cats, humans, garden warbler, tomato, sagebrush, willow). The reader applied `oa-read.md` as worded. The rule gives `m` to a group record when the paper states the value for that group as a whole, and to a species the paper names by its common name (SAMPLE.md). In this sample, 3 of the 11 group records graded `g` are such statements; the other 8 rest on a stated subset and keep `g`. No species-rank record carries `g` for a cited value. The pattern shows up at group level and in the common-name records, so the regrade should be run over those 93.
2. **A predicted spectral class graded `m`.** oa-2:3477 logs UV and green receptor classes inferred from opsin localization. Its twin oa-2:3478 (Habrocestum africanum, the same sentence and value, outside the sample) should go to `i` with it. The paper's other 26 opsin records state where the opsins sit or how many were found, which the paper measured; they were not audited here.
3. **A quote spliced across two sentences** (oa-2:3467). oa-2:3525 also spans two sentences, but each part starts at the start of its sentence and the cuts are marked, so it stands.
4. **Taxon raised from the printed variety to the species** (oa-2:3366), with the variety kept in `note`.
5. **Quotes taken from the PMC web pages.** For entries 51 and 75, sources-r1 records the reading run's copy as HTML; this audit's run fetched the Europe PMC PDFs. Two quotes fail `quotecheck.py` against those texts and three pass only as table rows (3477, 3566, 3568). The differences are typographic and are not counted, but `oa-read.md` asks that every quote pass the check.

## Rows written

`docs/views/recheck/recheck-oa-1018-b.jsonl`: 6 rows in the recheck-5 schema (`unit`, `supersedes`, `action`, `reason` and the full corrected record), each also naming its `field` with the `old` and `new` value. They are oa-2:3366 (taxon), 3467 (requote), 3477 (grade to i), and 3513, 3516 and 3568 (grade to m). `tools/senses/check.py` passes on the file, and the new quote for 3467 passes `quotecheck.py` verbatim. No evidence file was edited.
