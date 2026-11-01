# audit-366: desk-d274, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d274 files present untracked in the worktree (docs/tracks/progress/desk-d274.md and docs/views/evidence/desk-d274.jsonl, 7 lines; neither committed here, neither edited; the evidence file is byte-identical to origin/research/desk-d274). Worktree HEAD and origin/main 83288436 (d272 merged after audit 365). `python3 -I tools/senses/check.py | grep 'd274\.'`: "docs/views/evidence/desk-d274.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 20, 20, 36, 36, 27, 36, 21, all within 40. Non-ASCII in quotes: "±" in lines 1 to 4, 6, 7; "µ" (U+00B5, micro sign, as the Biology page prints it, tool reading) and "–" in lines 3, 4; "Δ", "φ", "°" in line 5; "μ" (U+03BC) in lines 6, 7 and "…" in line 6's cut mark. Format model audit 358; abutting pieces under audit-324.md, cuts under audit-331.md; ommatidia_count / rhabdom_um / interommatidial_deg conventions per audits 362, 364, 365.

Sources opened (WebFetch): api.crossref.org/works/10.3390/biology14081032 and /10.3390/insects17030287 (both answered); www.mdpi.com/2079-7737/14/8/1032 (five passes) and www.mdpi.com/2075-4450/17/3/287 (two passes); bionames.org/doi/10.11646/zootaxa.1819.1.2; wiki.pestinfo.org/wiki/Cacopsylla_chinensis. The two plazi treatment URLs returned only a redirect notice. No curl, PMC, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened (the unipd.it repository PDF in a search result was not opened). Points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

## Bibliographic and licence

- Lines 1 to 5 (Xie et al. 2025). Crossref: Hua Xie, Hui Yuan, Yuyun Wang, Xinyu Tang, Meiru Yang, Li Zheng, Zongbo Li, in that order (record's initials match, order right); title identical to the record; Biology 14, issue 8, article 1032; issued and published online 2025-08-11; licence https://creativecommons.org/licenses/by/4.0/, content-version vor, delay 0; relation empty, no update-to. Page: no licence sentence in the text, meta-dc.rights CC BY 3.0. Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref vor). Faults 0.
- Lines 6, 7 (Ran et al. 2026). Crossref: Hongfan Ran, Min Li, Yiping Niu, Aihong Ma, Xiaofan Yang, in that order; title identical; Insects 17, issue 3, article 287; issued 2026-03-06; CC BY 4.0 vor, delay 0; relation empty. Page: no licence sentence, meta-dc.rights CC BY 3.0, "Open Access" label. Accepted. Faults 0.

source.access "open" right in all seven. Bibliographic faults 0; licence faults 0.

## Names, family and order

- Tomicus yunnanensis: docs/views/gaps/gbif-names.tsv line 4794 "Tomicus yunnanensis EXACT ACCEPTED" (the tsv has no family column). Original description (bionames.org, verbatim pieces): "Description of the Yunnan shoot borer, Tomicus yunnanensis Kirkendall & Faccoli sp. n." "(Curculionidae, Scolytinae), an unusually aggressive pine shoot beetle from southern China,", Zootaxa 1819: 25-39, 2008 (author line Kirkendall, Faccoli & Ye from the plazi search result title; the bionames page gives no author line). So the family is Curculionidae, Scolytinae its subfamily, from a named source. Main's own row for this paper and species (desk-d227 line 4, behaviour_vision) files "family": "Curculionidae", and audit 317 said the same. check.py has no family check, so blank family passes the script (main's oa-1 Tomicus rows and many canon rows are blank), but here the stated reason ("the title gives the subfamily Scolytinae only") is a sourcing gap that a named source closes, and it leaves the five new rows inconsistent with the merged row for the same paper. Counted as one fault on each of lines 1 to 5. If the owner rules a blank family acceptable whenever the title lacks it, lines 1, 2 and 5 become MATCH and the error count falls by three. Order Coleoptera right.
- Cacopsylla chinensis: pestinfo "Cacopsylla chinensis (Yang & Li, 1981)", synonym "Psylla chinensis" (verbatim); the name filed is the current one, as audit 287 accepted for desk-d203. Family Psyllidae and order Hemiptera as in the paper's title and main's desk-d203 rows. Met. Neither note names a checklist authority ("Name filed as printed."); additions offered below, uncounted.

Name faults: 5 (family blank, lines 1 to 5).

## Duplicates

git grep on origin/main (83288436) across the whole docs/ tree (evidence, audit/corrected, audit/ALL.jsonl, codex-findings, searched/, sheets, wanted, progress) for Tomicus, Cacopsylla, biology14081032, 14/8/1032, insects17030287, 17/3/287, and for the printed figures 240.00, 247.38, "43.5 ± 1.6", "11.9 ± 0.5", "57.0 ± 3.6", "1.9 ± 0.6": main holds, from these papers, only desk-d227 line 4 (Tomicus behaviour_vision, phototaxis) and desk-d203 lines 6, 7 (Cacopsylla eye_type and polarization); the other Tomicus rows are oa-1 lines 4433 to 4435 and their recheck/ALL copies (opsin_sequences_recovered, a different paper, retracted by the Codex findings). None of the six values appears anywhere on main. Branch-only additions over all 269 origin/research/desk-d2*, audit-3* and sweep branches: only desk-d203, d227, d228 (Tomicus behaviour_vision, line 8 dropped as a repeat by audit 320), audit-317/320 reports, progress notes (d233, d247, d260 Tomicus pilifer, d272) and desk-d274 itself. The desk-d272 hand-back's "Already taken: Tomicus yunnanensis Biology 14(8): 1032 (desk-d227)" refers to that phototaxis behaviour_vision record; none of the d274 records repeats it (different traits: ommatidia_count, rhabdom_um, interommatidial_deg). Cacopsylla records are new traits for that paper too. Duplicates 0.

## Trait keys and conventions

ommatidia_count is not in check.py TRAITS; lines 1 and 2 say "new trait", units "ommatidia/eye" (main's commonest form), sexes as separate records with both values in conditions (the d270/d271 convention, audits 363, 364). rhabdom_um and interommatidial_deg are in TRAITS. rhabdom_um on main covers lengths and widths; "µm (length)" offered for lines 3, 4, 7, uncounted, as in audit 365. Trait-key faults 0.

## Per-record findings

### Lines 1 and 2, Tomicus yunnanensis ommatidia_count, male 240.00 and female 247.38

Section 3.1, verbatim in one piece: "Males possessed an average of 240.00 ± 3.51 facets per eye, while females had 247.38 ± 3.18 facets per eye." No figure or table citation in or after it (the next sentence, "Facets within the dorsal third of the eye are predominantly quadrilateral in shape", carries its own Figure 1 citation). **Quote MATCH** (20 words); each value is one number of the sentence.

Verified, verbatim: preceding sentence "While the external morphology of the left and right compound eyes was identical, the number of facets and their surface area" | "distribution differed"; Section 2.2 "detached T. yunnanensis heads (10 males, 15 females)"; Section 2.1 "Adult specimens of T. yunnanensis were collected alive within pine stems or shoots during January–February" | "from the JiuLong Shan Forestry Station (25°0′35″ N, 103°7′15″ E), located in central Yunnan Province, Southwest China." (no year); Section 2.7 "analyzed using unpaired t-tests and LSD post-hoc tests following ANOVA in R"; Discussion 4.1 "Significant sexual dimorphism in facet number is absent in bark beetles (e.g., D. pseudotsugae, D. ponderosae, T. yunnanensis)" | "but occurs in some ambrosia beetles like H. hampei [36,37,39]."; Table 1 rows "Facet number in males | - | 14 | 240.0 ± 3.5 | 224–265" and "Facet number in females | - | 16 | 247.4 ± 3.2 | 224–266" (tool rendering of the rows); caption "Histological and optical parameters in the compound eyes of T. yunnanensis." with no SD/SE label. No t or p for the sexes in Results (tool summary). Wild-collected adults, as recorded. The records' n mismatch (10/15 vs 14/16), the unknown dispersion measure, the absent sex test, the Discussion sentence and the left/right difference are all disclosed correctly.

Uncounted: the Table 1 ranges (224–265 and 224–266) are not carried; my own arithmetic (no source; my construction): a range of 41 facets with SD 3.5 and n = 14 is implausible, so the "±" is more likely an SE (SD about 13); the boring reading is simply that the paper does not say. Note's "Name filed as printed" can name the authority.

**Lines 1 and 2 error (family left blank; Curculionidae per the original description and main's d227 row).** Otherwise MATCH. Fixable.

### Lines 3 and 4, Tomicus yunnanensis rhabdom_um, central 43.5 and peripheral 11.9

Section 3.2.3, verbatim in two pieces in one response: "Within this structure, the rhabdomeres of the six peripheral cells (R1–R6), measuring 11.9 ± 0.5 µm in length," | "encircle the central rhabdomere formed by R7 and R8 (which is significantly longer at 43.5 ± 1.6 µm)". Asked about the join, the tool said nothing lies between "in length," and "encircle" (conditions 1 to 3 of audit-324.md met on a second pass). But asked what lies between "43.5 ± 1.6 µm)" and the full stop, it returned " (Table 1)" ("([Table 1](#biology-14-01032-t001)).", link markup). The record's quote ends "µm)." and drops the trailing table citation without a mark, and its note calls the sentence whole. Under the quote rule a trailing citation cut must be marked; restoring it gives 38 words, within 40. Quote fault. Values and definitions right: peripheral R1–R6 rhabdomeres 11.9 µm, central rhabdomere of R7 and R8 43.5 µm; the eye fields carry those definitions; the open ("insula-pattern" open rhabdom, preceding sentence verbatim) structure means these are rhabdomere lengths, which the eye fields say. Table 1: "Length of peripheral rhabdomeres | µm | 6 | 11.9 ± 0.5 | 11.4–12.4", "Length of central rhabdomeres | µm | 17 | 43.5 ± 1.6 | 33.0–55.3" (tool rendering).

Omitted design and significant result. Section 2.1 (verbatim pieces): beetles "were exposed to either high-intensity LED light (1000 lux) for at least 2 h" or "kept in complete darkness for at least 24 h"; "Light-adapted beetles were decapitated and fixed in daylight". Section 2.7: "Eyes from both sexes were examined via LM and TEM, with at least three replicates per sex/treatment group." Section 3.3: "Concurrently, the rhabdom area expanded significantly from 120.4 ± 18.0 µm2 to 152.1 ± 23.7 µm2 (p < 0.001)." after "Following dark adaptation, cone dimensions significantly increased" (verbatim pieces); the tool reads the change as light- to dark-adapted. The paper does not say in which adaptation state, or for which sex, the rhabdomere lengths were measured, and gives no length comparison between states (tool summary). The records say "sex of the measured eyes not stated" but never mention the two adaptation states or that the rhabdom's cross-section changed significantly between them, so a reader cannot tell that the lengths are pooled or unlabelled across a factor that significantly altered the same structure. The "treatment group" in the records' own quote of Section 2 is left unexplained.

Also: family blank (as lines 1, 2). Uncounted: Table 1 ranges; Table 1 distal rhabdom diameter 6.7 ± 0.5 µm (tool summary); units "µm (length)".

**Lines 3 and 4 error (unmarked trailing "(Table 1)" cut while the note claims a whole sentence; light/dark adaptation design and the significant rhabdom-area change omitted; family blank).** Fixable.

### Line 5, Tomicus yunnanensis interommatidial_deg 3.2

Section 3.4, verbatim in two pieces: "Spatial resolution (interommatidial angle Δφ = A/R) was 3.2°; eye radius R was geometrically estimated" | "(R = (s2/4 + h2)/(2h), s = segment length, h = height)." Join: a single space, nothing else; no citation at the end (second pass). Before: "The F-number (f/A, A = maximum facet diameter) was 1.49, quantifying light-gathering efficiency."; after: "The acceptance angle Δρrh (rhabdom distal diameter/f) was 12.2°." The value 3.2° is printed in the sentence and in Table 1 ("Interommatidial angle | ° | - | 3.2 | -", tool rendering), so it is carried by the quote. **Quote MATCH** (27 words). "s2", "h2" are returned as plain digits; whether the page sets them as superscripts is unconfirmed (uncounted). The method's "calculated, not measured directly", A = maximum facet diameter (from the F-number sentence) and R estimated geometrically are right.

Uncounted additions: the record says the inputs are "not stated", but Table 1 gives them: facet diameter 21.0 ± 2.9 µm (n = 130, range 13.5–25.8) and eye radius 481.5 ± 53.9 µm (males, n = 12) and 481.9 ± 45.6 µm (females, n = 12) (tool rendering); Section 2.7 describes a second radius method, "The radius of curvature was measured at the broadest anterior-posterior point using a circular tool" (verbatim piece). My arithmetic (no source; my construction): 25.8 µm / 481.7 µm = 0.054 rad = 3.07°, and the mean facet 21.0 µm gives 2.50°, so 3.2° matches neither exactly; the boring reading is rounding or a different R from the geometric estimate. Not counted, since the value is printed as calculated and the record says so; the "Discussion repeats the value" claim was not checked.

**Line 5 error (family blank only).** Otherwise MATCH. Fixable.

### Line 6, Cacopsylla chinensis interommatidial_deg 1.9

Section 3 introductory paragraph, verbatim in two abutting pieces in one response: "The total length of the ommatidium is on average 76.0 ± 3.0 μm, while the average interommatidial angle" | " is 1.9 ± 0.6 deg, determined from the diameter of the corneal lens (15.6 ± 0.6 μm) and the eye radius of 87.8 ± 5.2 μm." It is the paragraph's last sentence (no citation). Whole sentence 44 words, so a cut is needed. Cut ruling (audit-331.md): the cut drops "and the eye radius of 87.8 ± 5.2 μm.", the second input of the derivation, which the method carries; it does not qualify "1.9 ± 0.6 deg". The cut is real and acceptable, marked "[…]", and the note gives the dropped text exactly. **Quote MATCH** (36 words with the mark).

Lens inconsistency: Section 3.1, verbatim, "The cornea is about 16.9 ± 1.7 μm in diameter, with a maximum thickness of 7.6 ± 1.7 μm at the center of each facet." and "It is formed by four cone cells and has an average length of 15.6 ± 0.6 μm." (the crystalline cone). The record discloses this in conditions. Met.

Omitted, consequential: the paper gives no formula (Methods silent; tool summary), and the printed inputs do not yield the printed value. My arithmetic (no source; my construction): 15.6 / 87.8 = 0.178 rad = 10.2°, and 16.9 / 87.8 = 11.0°; the tool, asked independently, made the same calculation ("about 0.178 rad, or roughly 10°, not 1.9°"; tool summary). A 1.9° angle from an 88 µm eye radius would need lenses about 2.9 µm across. The record's method ("calculated from corneal-lens diameter and eye radius") invites the reader to take Δφ = D/R, which gives roughly five times the logged value. This is a calculated-quantity confound the record must disclose. The boring answer: a units or transcription slip in the paper (the value could be in some other unit, or a different quantity), which the paper does not settle. Owner question: whether a calculated value contradicted by its own printed inputs should be filed at all; I recommend filing with the disclosure below and grade m kept, but would accept a hold.

Verified, verbatim: preceding sentence "Electron microscopic observations of the central eye region revealed no sexual dimorphism; thus," | " the measurements from males and females were combined (Table 1; see Table S1 for separate values)."; Section 2.1 "Adult specimens of C. chinensis were collected from a pear orchard in Fanzhuang Town"; "twelve live adults (6 females and 6 males) were exposed to 1000 lx for 2 h."; "The light-adapted specimens were decapitated and fixed under the same light intensities." June 2023 and Zhao County, Hebei (tool summary). Methods name an independent-samples t-test by sex with no result reported (tool summary). Table 1 rows not available as text (image only); caption "Measurements on the compound eyes of Cacopsylla chinensis." Wild-collected adults, light-adapted, as recorded.

Uncounted: the sex null concerns "the central eye region" and has no test statistic; the record can say so.

**Line 6 error (printed inputs give about 10°, not 1.9°, and no formula is printed; undisclosed).** Fixable by disclosure.

### Line 7, Cacopsylla chinensis rhabdom_um 57.0

Section 3.3, verbatim in two abutting pieces: "Under the crystalline cone lie eight retinular cells forming a centrally fused rhabdom," | " measuring approximately 57.0 ± 3.6 μm in length." First sentence of 3.3; before it "The nuclei of the secondary pigment cells are located in the distal regions," | " where their cytoplasm contains abundant mitochondria."; after it "Retinular cells are numbered following the system by Friedrich et al. (2011) [35]." No citation in the sentence. **Quote MATCH** (21 words); "approximately" carried in conditions; value says no more. Fused rhabdom of eight retinular cells: the eye field is right; total length (no central/peripheral split applies). All specimens light-adapted at 1000 lx, as recorded; no light-state or regional comparison of length is reported (distal and proximal diameters 3.0 ± 0.2 and about 2.4 ± 0.2 µm, tool summary). Sex: as line 6. Uncounted: units "µm (length)"; sex null from the central eye region, no test statistic.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Tomicus yunnanensis, ommatidia_count 240.00 (male) | error, fixable | family, note | quote MATCH (20); family blank where the original description and main's d227 give Curculionidae |
| 2 | Tomicus yunnanensis, ommatidia_count 247.38 (female) | error, fixable | family, note | as line 1 |
| 3 | Tomicus yunnanensis, rhabdom_um 43.5 (central R7/R8) | error, fixable | quote, conditions, note, family | unmarked trailing "(Table 1)" cut; light/dark adaptation and significant rhabdom-area change omitted; family blank |
| 4 | Tomicus yunnanensis, rhabdom_um 11.9 (peripheral R1–R6) | error, fixable | quote, conditions, note, family | as line 3 |
| 5 | Tomicus yunnanensis, interommatidial_deg 3.2 | error, fixable | family, note; conditions (uncounted) | quote MATCH (27), value printed and carried; family blank |
| 6 | Cacopsylla chinensis, interommatidial_deg 1.9 | error, fixable | method, conditions | cut real and acceptable; lens conflict disclosed; printed inputs give about 10°, undisclosed |
| 7 | Cacopsylla chinensis, rhabdom_um 57.0 | MATCH | units, conditions (uncounted) | whole sentence (21), fused rhabdom total length |

Errors 6 of 7 audited records (85.7%), above the 5% bar; none held out. By kind: family blank 5 (lines 1 to 5; 3 of the 6 errors rest on this alone, lines 1, 2, 5); quote form 2 (lines 3, 4, unmarked trailing citation); omitted design factor and significant effect 2 (lines 3, 4); calculated value contradicted by its printed inputs, undisclosed 1 (line 6); bibliographic 0; licence 0; checklist names 0; duplicates 0 against main and all 269 desk-d2*, audit-3* and sweep branches; trait keys 0. If the owner rules blank family acceptable, the count is 3 of 7 (42.9%), still above the bar.

Unchecked: Table S1 (per-sex Cacopsylla values); the Cacopsylla Table 1 rows (image only), so the n behind 1.9 and 57.0; whether "s2", "h2" are superscripts on the Tomicus page; the Tomicus Discussion's repetition of 3.2°; the Zootaxa 2008 author line beyond the plazi search-result title; which eye (left or right) the Tomicus facet counts come from (the paper does not say, tool summary).

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). "field = new string" replaces the whole field.

Lines 1 to 5, each, counted:
- `family` = "Curculionidae"
- `note`: "Order as printed in the paper's title; the title gives the subfamily Scolytinae only, so family is left blank." -> "Order as printed in the paper's title; family Curculionidae (subfamily Scolytinae) from the original description, Kirkendall, Faccoli & Ye 2008, Zootaxa 1819: 25-39, titled '(Curculionidae, Scolytinae)', as main's desk-d227 row for this paper files it (audit 366)."
- `note` (uncounted): "Name filed as printed." -> "Name filed as printed; Tomicus yunnanensis Kirkendall & Faccoli, 2008, EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv."

Lines 1 and 2, each, uncounted:
- `conditions`: "for facet number (unexplained);" -> "for facet number (unexplained; ranges 224–265 males, 224–266 females);"

Lines 3 and 4, each, counted:
- `quote`: "43.5 ± 1.6 µm)." -> "43.5 ± 1.6 µm) (Table 1)."
- `note`: "Whole sentence, seen complete in two WebFetch pieces joined with a single space." -> "Whole sentence, seen complete in two WebFetch pieces joined with a single space, including its trailing '(Table 1)' citation (restored by audit 366; 38 words)."
- `conditions`: "sex of the measured eyes not stated;" -> "beetles were either light-adapted (LED, 1000 lux, at least 2 h, fixed in daylight) or dark-adapted (complete darkness, at least 24 h) before fixation (Section 2.1), and neither the adaptation state nor the sex of the eyes measured for these lengths is stated, with no length comparison between states; the rhabdom cross-sectional area changed significantly between states, 120.4 ± 18.0 to 152.1 ± 23.7 µm2 (p < 0.001), with cone dimensions larger after dark adaptation (Section 3.3);"

Lines 3 and 4, each, uncounted:
- `conditions`: "dispersion measure not stated;" -> "dispersion measure not stated; Table 1 ranges 11.4–12.4 µm (peripheral) and 33.0–55.3 µm (central);"
- `units` = "µm (length)"

Line 5, uncounted:
- `conditions`: "sex, number of eyes and individuals for the calculated value not stated;" -> "one pooled calculated value (Table 1, n not given); Table 1 gives the inputs as facet diameter 21.0 ± 2.9 µm (n = 130, range 13.5–25.8) and eye radius 481.5 ± 53.9 µm (males, n = 12) and 481.9 ± 45.6 µm (females, n = 12); Section 2.7 describes a second radius method (circular tool at the broadest anterior-posterior point); 25.8/481.7 gives 3.07° and 21.0/481.7 gives 2.50° (auditor's arithmetic, audit 366), so the exact inputs behind 3.2° are not identifiable;"

Line 6, counted:
- `method`: "calculated from corneal-lens diameter and eye radius (87.8 ± 5.2 μm)" -> "calculated from corneal-lens diameter and eye radius (87.8 ± 5.2 μm); no formula is printed"
- `conditions`: "(an inconsistency in the paper, not resolved here)" -> "(an inconsistency in the paper, not resolved here); the printed inputs do not yield the printed angle: Δφ = D/R gives 15.6/87.8 = 0.178 rad, about 10.2°, or 11.0° with the 16.9 μm cornea, roughly five times 1.9 deg, and the paper gives no formula or other derivation (auditor's arithmetic, audit 366); the value is filed as printed"

Line 6 and line 7, each, uncounted:
- `conditions`: "the authors report no sexual dimorphism and combined males and females (per-sex values in Table S1, not seen);" -> "the authors report that electron microscopy of the central eye region revealed no sexual dimorphism and combined males and females (per-sex values in Table S1, not seen); Methods name an independent-samples t-test by sex, but no test statistic is reported;"
- `note`: "Name filed as printed." -> "Name filed as printed; Cacopsylla chinensis (Yang & Li, 1981), synonym Psylla chinensis, per pestinfo (accepted in audit 287)."

Line 7, uncounted:
- `units` = "µm (length)"
