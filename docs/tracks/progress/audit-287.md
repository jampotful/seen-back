# audit-287: desk-d203 (8 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d203 files present untracked in the worktree (docs/tracks/progress/desk-d203.md and 8 evidence lines in docs/views/evidence/desk-d203.jsonl; neither committed here, neither edited). HEAD 7ff94881 equals origin/main. `tools/senses/check.py` on the evidence file: 8 records, 0 problems. Quote lengths (`len(q.split())`): 19, 15, 20, 20, 18, 18, 11, 11, all within 40. No searched or wanted file, so every record was judged and there is no sample to draw. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit) and the publisher-copy licence rule; the shared brief's plant-screening items are superseded for this animal unit. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps), views/, src/ and docs/tracks for "Asiophrida", "Eucryptorrhynchus", "Cacopsylla chinensis", "C. chinensis", "pear psyllid" and the DOI suffixes 15070532, 14080699 and 17030287, every trait included, and the notes and conditions of the main rows found. 6 WebSearch and 14 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3390/INSECTS15070532, /10.3390/INSECTS14080699 and /10.3390/INSECTS17030287 (all answered in uppercase, none robots_disallowed); the three record URLs on www.mdpi.com (2075-4450/15/7/532 once, 14/8/699 three passes, 17/3/287 once; each carries the full text); for names, lkcnhm.nus.edu.sg (Raffles Bulletin of Zoology page and PDF RBZ-2024-0026), wiki.pestinfo.org/wiki/Cacopsylla_chinensis, biodiversity.org.au/afd/taxa/Asiophrida/bibliography, an iNaturalist flag page and a Zootaxa page (both off-topic), and two plazi treatment pages that returned only a redirect notice (not followed). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Liang et al. 2024 (lines 1, 2), fresh Crossref: Zu-Long Liang, Tian-Hao Zhang, Jacob Muinde, Wei-Li Fan, Ze-Qun Dong, Feng-Ming Wu, Zheng-Zhong Huang, Si-Qin Ge, in the recorded order; title as recorded (returned in two chunks that join to the recorded string); Insects 15(7), page 532; issued and online 2024-07-13; licence CC BY 4.0 (vor); relation empty; no update-to.
- Hao et al. 2023 (lines 3 to 6): Yingying Hao, Qi Wang, Chao Wen, Junbao Wen, in order; title verbatim as recorded; Insects 14(8), page 699; issued 2023-08-10; CC BY 4.0 (vor); relation empty; no update-to.
- Ran et al. 2026 (lines 7, 8): Hongfan Ran, Min Li, Yiping Niu, Aihong Ma, Xiaofan Yang, in order; title verbatim as recorded; Insects 17(3), page 287; issued 2026-03-06; CC BY 4.0 (vor); relation empty; no update-to.

Licence on the copy read: each MDPI page gives only the rights field https://creativecommons.org/licenses/by/3.0/, where Crossref gives 4.0; audit 276 found the same 3.0 field on five MDPI pages and read it as a site-wide tag. Publisher's own CC BY copy; met. Uncounted: the notes say "licence shown on that page" without naming it; "CC BY (page metadata 3.0, Crossref 4.0)" would be exact.

Bibliographic faults 0; licence faults 0.

## Names

- Eucryptorrhynchus scrobiculatus (lines 3, 5) and E. brandti (lines 4, 6): Tseng and Cheng 2024, Raffles Bulletin of Zoology 72: 324-334 (PDF on the museum's site), treat E. brandti (Harold, 1880) and E. scrobiculatus (Motschulsky, 1854) as valid; its Remarks say E. scrobiculatus was once a junior synonym of E. chinensis (Olivier, 1791), which is a junior homonym of Curculio chinensis Linnaeus, 1758, so Alonso-Zarazaga (2013) made E. scrobiculatus the valid name (tool summary). Accepted. Uncounted: the same paper finds two clades within E. scrobiculatus (Ningxia against southern China, Vietnam and Taiwan), a cryptic species not yet described; Hao et al.'s animals bore into Ailanthus altissima, and their locality could go in `conditions` once read.
- Cacopsylla chinensis (lines 7, 8): pestinfo gives "Cacopsylla chinensis" "(Yang & Li, 1981)", synonym "Psylla chinensis"; a plazi treatment title in my search reads "Cacopsylla (Hepatopsylla) chinensis (Yang & Li)". Accepted.
- Asiophrida xanthospilota (lines 1, 2): UNVERIFIED, as in audit 276. Not in gbif-names.tsv; the AFD page names "Asiophrida Medvedev, 1999" but lists no species; two further pages my search returned were other taxa. Name as printed in the paper. Uncounted.

Name faults 0; 1 name unverified (2 records).

## Duplicates

- Asiophrida xanthospilota on main: desk-d192:1 (colour_vision, "electroretinogram responses strong to blue and green light and weak to red light, in both sexes", Abstract, same paper; method "electroretinogram (ERG) with monochromatic stimuli (red, yellow, green, blue, UV)"; conditions give females' green and males' blue maxima, red lowest in both, and the ca. 100 lux level) and desk-d192:2 (colour_vision, male ERG to green, blue and UV higher than female, Results 3.4, same paper). No row in audit/corrected or audit/ALL. **Line 1 repeats this finding under another trait key**: same paper, same ERG experiment, the adjacent abstract sentence (line 1's own note quotes d192:1's quote sentence), and its value, a response to each of the five lights in both sexes, is carried by d192:1's method and value together with d192:2's UV comparison. Line 2 (polarization) is a different finding; no main row or note carries it.
- Eucryptorrhynchus and Cacopsylla chinensis: no evidence row on main under any trait; the Ran et al. DOI appears only in harvest-42 screened lists for Scolypopa (another genus's search). Not repeats.

Duplicates 1 (line 1). Contradictions 0.

## Per-paper findings

### Liang et al. 2024, Asiophrida xanthospilota (lines 1, 2)

Abstract sentences 6 to 9 (verbatim): "The orientation of microvilli indicates that Asi. xanthospilota is unlikely to be a polarization-sensitive species."; "ERG testing showed that both males and females reacted to stimuli from red, yellow, green, blue, and ultraviolet light."; "Both males and females exhibited strong responses to blue and green light but weak responses to red light."; then the phototaxis sentence (positive to all five lights, blue strongest). Methods 2.5: "The stimulation was conducted using LED beads emitting five different lights (red, yellow, green, blue, ultraviolet)" "with an approximate illuminance of ca. 100 lux." (two chunks); no nm for the ERG LEDs. Results 3.2.2: "The orientation of the microvilli suggests that Asi. xanthospilota is unlikely to perceive polarized light."; "The microvilli of peripheral rhabdomeres are roughly oriented towards the centre of the ommatidium." Discussion 4.1: the microvilli in different rhabdomeres "roughly orient themselves in three directions," "indicating that it is unlikely to be a polarization-sensitive species." (chunks). Orientation was read from TEM cross sections (70 nm ultrathin sections, Figure 5; tool summary). The rhabdom is open: six peripheral rhabdomeres (R1 to R6) and two distal segments from R7, R8 contributing none (Abstract).

Line 1. Quote MATCH, whole abstract sentence 7. Counted (duplicate, unfixable): see Duplicates. Trait key (owner question 2): a string under spectral_range_nm is not acceptable for this paper. The ERG stimuli are named colours at equal illuminance with no wavelength given anywhere in the paper (the nm bands in Methods 2.6 belong to the phototaxis rig), so the row states no range in nm and cannot be given one; d192 already filed the ERG under colour_vision, which is where a colour-name response belongs. `conditions` also says "peak wavelengths of the lights are not in the abstract" when the full text on the page read gives none either, and omits the ca. 100 lux level. Drop the line. If the owner wants the "all five, including yellow and UV" reading kept, it fits d192:1's note: append "Abstract, previous sentence: 'ERG testing showed that both males and females reacted to stimuli from red, yellow, green, blue, and ultraviolet light.'"

Line 2. Quote MATCH, whole abstract sentence 6. Value matches the quote; `conditions` correctly calls it an inference from structure. Confirm. Uncounted, suggested: `conditions` should give the basis the Discussion states (microvilli of different rhabdomeres roughly in three directions; peripheral microvilli roughly toward the ommatidial centre; open rhabdom) and `note` the Results 3.2.2 sentence, which says the same thing.

Grade m right on both (one named species, measured). `partial` true right for an abstract-only reading.

### Hao et al. 2023, Eucryptorrhynchus scrobiculatus and E. brandti (lines 3 to 6)

Abstract (verbatim): "E. scrobiculatus and E. brandti possess a pair of reniform apposition compound eyes and contain about 550 ommatidia per eye." and "The interommatidial angle of E. scrobiculatus and E. brandti are 7.08 ± 0.31° and 4.84 ± 0.49°, respectively." Results repeats the pair: "The interommatidial angle was 7.08 ± 0.31° and 4.84 ± 0.49° for E. scrobiculatus and E. brandti, respectively". So both species' values do come from one "respectively" sentence, in the abstract and again in Results, in the stated order. Ommatidia counts (Results, verbatim): "The number of ommatidia of female and male E. scrobiculatus was 561 ± 7 and 554 ± 5, respectively"; "the number of ommatidia of female and male E. brandti was 538 ± 11 and 511 ± 7, respectively". Methods: SEM used "ten (five males and five females) E. scrobiculatus and E. brandti adults"; the LM and TEM sample sizes are not stated; Data Analysis lists the measurements, "interommatidial angle" among them, without saying how the angle was obtained (the tool's first summary said longitudinal LM sections); ± is not defined as SD or SE (t-test and one-way ANOVA with Tukey). The tool reports that the text cites Table 2 for the angle, and Table 2's caption reads "Comparison of the internal microstructure of the compound eyes between E. scrobiculatus and E. brandti female adults."; Table 2 is an image, so the angle row and its sex could not be confirmed, and the Results sentence sits between external-morphology sentences on both sexes.

Lines 3 and 4. Quote MATCH. eye_type "compound-apposition" is main's vocabulary (46 rows). One shared sentence filed once per species is right. Confirm. Uncounted: the per-sex counts (561/554 and 538/511) belong in `conditions` beside "about 550", which rounds over a 511 to 561 spread.

Lines 5 and 6. Quote MATCH; 7.08 to scrobiculatus and 4.84 to brandti follow the order of "respectively". interommatidial_deg is a valid key (tools/senses/check.py TRAITS; 5331 rows on main). Grade m right for each (each species measured in the source). Confirm. Uncounted (unverified, fix anyway): the sex of the measured adults is not stated beside the value, and the text's citation of Table 2 points to female adults; say so rather than "Adults".

### Ran et al. 2026, Cacopsylla chinensis (lines 7, 8)

Abstract (verbatim): "The eyes are of the apposition type, lacking a clear zone."; "The microvilli of the rhabdom are arranged in two orthogonal directions."; sample "(n = 12 adult)." Methods: "twelve live adults (6 females and 6 males)." Discussion: "An orthogonal arrangement of microvilli can be found in the rhabdom of C. chinensis," "a structural feature often associated with polarization sensitivity in insects." and "In the absence of direct functional or specialized structural data (e.g., a distinct DRA) in C. chinensis," "any inference regarding polarization sensitivity in this species remains speculative." (chunks). No dorsal rim area is described for the species.

Line 7. Quote MATCH. Species tie through the single-species title and abstract is sound. Confirm. Uncounted: add "6 females and 6 males" to `method`.

Line 8. Quote MATCH. The value's parenthesis "(anatomy only; no polarization sensitivity tested)" is a statement about the study, which the Discussion's "In the absence of direct functional ... data" supports. Confirm. Uncounted, suggested: keep the value to the quote ("rhabdom microvilli arranged in two orthogonal directions") and move the parenthesis to `conditions`, citing the Discussion sentence that inference on polarization sensitivity "remains speculative" and that no distinct DRA is reported.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Asiophrida xanthospilota, ERG responses to five colours (spectral_range_nm) | drop | whole record | Quote MATCH; repeats main desk-d192:1 and 2 (same paper, same ERG, adjacent abstract sentence) under another key, and no nm exists in the paper for a spectral_range_nm row |
| 2 | Asiophrida xanthospilota, unlikely polarization-sensitive (microvilli) | confirm | | Quote MATCH; new finding, not on main |
| 3 | Eucryptorrhynchus scrobiculatus, compound-apposition | confirm | | Quote MATCH; name valid (Tseng and Cheng 2024) |
| 4 | Eucryptorrhynchus brandti, compound-apposition | confirm | | Quote MATCH; name valid |
| 5 | Eucryptorrhynchus scrobiculatus, interommatidial 7.08° | confirm | | Quote MATCH; first of the "respectively" pair, repeated in Results |
| 6 | Eucryptorrhynchus brandti, interommatidial 4.84° | confirm | | Quote MATCH; second of the pair |
| 7 | Cacopsylla chinensis, compound-apposition, no clear zone | confirm | | Quote MATCH; name accepted |
| 8 | Cacopsylla chinensis, rhabdom microvilli orthogonal | confirm | | Quote MATCH; authors call any polarization inference speculative, as the record says |

Errors per record: line 1: 1 (duplicate); lines 2 to 8: 0 each.

Evidence errors: 1 of 8 (12.5%): duplicates 1 (line 1); scientific-context 0; quote-form 0; name 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: line 1 (drop).

Pooled with audits 172 to 286: 265 of 622 evidence records (42.6%; audit 286's 264 of 614, and 1 of 8 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1): drop the record. Optional merge into main desk-d192:1 `note`, appended: "Abstract, previous sentence: 'ERG testing showed that both males and females reacted to stimuli from red, yellow, green, blue, and ultraviolet light.'"

Uncounted, suggested:
- Line 2 `conditions`: "Inference from TEM cross sections of the rhabdom (open rhabdom: six peripheral rhabdomeres R1-R6 and two distal R7 segments; R8 contributes none); the microvilli of different rhabdomeres roughly orient in three directions and peripheral microvilli roughly toward the ommatidial centre (Results 3.2.2, Discussion 4.1); no behavioural or electrophysiological test of polarization"
- Lines 3 and 4 `conditions`: "The abstract states the eye type and about 550 ommatidia per eye for both species together; Results give 561 ± 7 (female) and 554 ± 5 (male) for E. scrobiculatus and 538 ± 11 and 511 ± 7 for E. brandti; SEM on ten adults (five males, five females) of each species"
- Lines 5 and 6 `conditions`: "Adults (the text cites Table 2, captioned for female adults; the table is an image and the sex of the measured eyes could not be confirmed); 7.08 ± 0.31° for E. scrobiculatus and 4.84 ± 0.49° for E. brandti in both the abstract and Results; ± not defined as SD or SE; sample size for the angle not stated"
- Line 7 and 8 `method`: "transmission electron microscopy of 12 adults (6 females and 6 males)"
- Line 8 `value`: "rhabdom microvilli arranged in two orthogonal directions"; `conditions`: "Anatomy only; the Discussion says an orthogonal arrangement is often associated with polarization sensitivity in insects but that, without functional data or a distinct dorsal rim area, any inference for this species remains speculative"
- All records `note`: "licence shown on that page" to "CC BY on the MDPI page (rights field 3.0; Crossref 4.0)".

## Progress note

The note's "the three papers appear only in searched/wanted files, no evidence rows" is wrong for Asiophrida xanthospilota: main holds desk-d192:1 and 2 from the same paper, and desk-queue.md line 250 lists that unit. That missed grep is what let line 1 through. Bibliographic and licence statements are accurate. Owner question 2 is answered above (no; colour_vision, and here already filed). Held-out leads were not re-checked (they are not filed records).

Verdict: 1 error in 8 (12.5%), above the 5% bar; pooled 42.6%. Error line: 1 (drop). Lines 2 to 8 can merge as they stand, with the uncounted text above if the owner wants it.

This report is model output and carries no authority.
