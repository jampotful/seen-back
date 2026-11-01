# audit-356: desk-d260, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d260 files present untracked in the worktree (docs/tracks/progress/desk-d260.md and docs/views/evidence/desk-d260.jsonl, 6 lines; neither committed here, neither edited). Worktree HEAD and origin/main 93f9a0bb (desk-d259 after audit 355). Branch history of research/desk-d260 (which carries a merge of main) was ignored; only the evidence file as copied was audited. `python3 -I tools/senses/check.py | grep 'd260\.'`: "docs/views/evidence/desk-d260.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 36, 38, 23, 23, 37, 30, all within 40. Non-ASCII: curly "’" in line 1's "Cohen’s" (page prints the curly form, tool reading) and "χ" twice in line 5, both checked. Format model audits 354 and 355; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md (no line uses a cut).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all five DOIs (10.1371/journal.pone.0182146, 10.3390/jmse11030623, 10.1371/journal.pone.0204663, 10.3390/agronomy16100957, 10.1371/journal.pone.0268678; all answered, none robots_disallowed); journals.plos.org pone.0182146 (two passes), pone.0204663 (two), pone.0268678 (two); mdpi.com 2077-1312/11/3/623 (two), 2073-4395/16/10/957 (one). Names: api.obis.org/v3/taxon?scientificname= for Ilyanassa obsoleta and Tritia obsoleta (both failed with client_error, not worked around); the path form api.obis.org/v3/taxon/<name> for Ilyanassa obsoleta, Tritia obsoleta and Melipona bicolor (answered; Melipona bicolor total 0); moure.cria.org.br catalogue?id=118211 (genus Plebeia page, no use); tb.plazi.org treatment 280B1036D92F894EBEABF68A188BFB46 (redirect notice only); zenodo.org/records/5452960 (Plazi treatment deposit, answered). WoRMS, GBIF not opened (refused per rules). No curl, mirror, PMC, repository copy of a paper, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

## Bibliographic and licence

- Line 1 (Putman et al. 2017). Crossref: Breanna J. Putman, Jonathan P. Drury, Daniel T. Blumstein, Gregory B. Pauly; title identical; PLOS ONE 12(8) e0182146; issued 2017-08-09; CC BY 4.0 vor; relation empty. Page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License,". Accepted. Faults 0.
- Line 2 (Manz, Lord, Morales 2023). Crossref: as recorded; title identical; Journal of Marine Science and Engineering 11(3) 623; issued 2023-03-16; CC BY 4.0 vor. Page: no body licence sentence, metadata CC BY 3.0. Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0.
- Lines 3, 4 (Koethe et al. 2018). Crossref: Sebastian Koethe, Sarah Banysch, Isabel Alves-dos-Santos, Klaus Lunau; title identical; PLOS ONE 13(9) e0204663; issued 2018-09-28; CC BY 4.0 vor. Page prints the Creative Commons Attribution License sentence. Accepted. Faults 0.
- Line 5 (Santander et al. 2026). Crossref: six authors in the recorded order; title identical; Agronomy 16(10) 957; issued 2026-05-12; CC BY 4.0 vor. Page: no body sentence, metadata CC BY 3.0. Accepted. Faults 0.
- Line 6 (Saavedra, Tomás, Amo 2022). Crossref and the page both print "Gustavo Tomás"; the record writes "Gustavo Tomas". **Fault 1** (author not as printed). Title identical; PLOS ONE 17(5) e0268678; issued 2022-05-19; CC BY 4.0 vor; page prints the Creative Commons Attribution License sentence. Licence accepted.

Bibliographic faults 1 (line 6); licence faults 0; source.access "open" right throughout.

## Names

- Sceloporus occidentalis (line 1): not in gbif-names.tsv; main's gaps cells carry it as Phrynosomatidae, Squamata; the desk's Reptile Database reading not reopened (unchecked). Met.
- Ilyanassa obsoleta (line 2): OBIS path form: "Ilyanassa obsoleta", "(Say, 1822)", "accepted", taxonID 467490, Nassariidae, Neogastropoda, Gastropoda. "Tritia obsoleta": "superseded combination", acceptedNameUsage "Ilyanassa obsoleta" (467490). gbif-names.tsv:3224 "Nassa obsoleta EXACT SYNONYM Ilyanassa obsoleta". The record's name is the accepted one, not a synonym; WoRMS's Tritia listing is not followed by OBIS, which maps it back to Ilyanassa. Owner question 3 answered: filed correctly. Met. Snails wild-collected (Raritan Bay intertidal, tool summary).
- Partamona helleri (line 3): main's canon-3.jsonl:285, :286 carry the species with Apidae, Hymenoptera. Met.
- Melipona bicolor (line 4): not in gbif-names.tsv; OBIS total 0. Zenodo record 5452960 (Plazi deposit of the treatment "Melipona (Eomelipona) bicolor Lepeletier" from Rozen, Almeida, Smith and Jones 2021, American Museum Novitates 3971, 10.1206/3971.1 as printed on the deposit page) lists "Order Hymenoptera" and "Family Apidae" for the species. The record's values are right; its source (other species of the genus on main) is not a source for the species, and the note now cites the treatment (uncounted, values unchanged). Owner question 1 answered: Apidae, Hymenoptera confirmed at species level; the name is used as valid in a 2021 treatment. The paper names only Meliponini in the text (Apidae and Hymenoptera appear only in reference titles, tool summary).
- Bagrada hilaris (line 5): the paper prints "Bagrada hilaris (Burmeister) (Hemiptera: Pentatomidae)" (verbatim); main's desk-d233 rows agree. Met.
- Cyanistes caeruleus (line 6): gbif-names.tsv has it accepted (Parus caeruleus its synonym), as the note says. Met.

Name faults 0.

## Duplicates

git grep on origin/main (93f9a0bb) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, progress, codex-findings, desk-queue) for each DOI suffix (0182146, jmse11030623, 0204663, agronomy16100957, 0268678), for each species name, Tritia, Nassa obsoleta, Parus caeruleus, and the first authors Putman, Manz, Koethe, Santander, Saavedra; then the branch-only additions (`git diff origin/main...<branch>`) of all 138 remote branches matching origin/research/desk-d2* or origin/research/audit-3*; then grep of docs/tracks/progress/audit-3*.md.

- No DOI of this unit is on main or any other branch; the only branch hits are research/desk-d260 itself.
- Sceloporus occidentalis: gaps rows only on main; old branches audit-32 to audit-38 carry oa-2 eye_diameter and corneal_diameter rows ("Sceloporus occident"), different traits and source. Not a repeat.
- Ilyanassa obsoleta: main holds corrected/ground-invertebrates.jsonl:148 under the synonym Nassa obsoleta, trait polarization, a different paper and trait. Not a repeat.
- Partamona helleri: canon-3 lambda_max_nm and receptor_classes rows; no behaviour_vision. Melipona bicolor: searched files only. Not repeats.
- Bagrada hilaris: desk-d233.jsonl:2, :3 on main (sense_chemical, EAG, Arif et al. 2020, insects11020109); audit-326 and desk-d258 mention it. Different paper and finding (behavioural Y-tube with plant volatiles); by the audit-346 precedent (same species and trait, different paper and value) not a repeat. Confirmed.
- Cyanistes caeruleus: vision rows on main (lambda_max_nm, cff_hz, ocular media, behaviour_vision); no sense_chemical row. desk-d253.md holds out pone.0203269 (pooled Parus major / Cyanistes nest-box scent), a different paper. Not a repeat.

Duplicates 0.

## Trait keys and rulings

- Line 1, behaviour_vision from a coloured-shirt flight-initiation trial (owner question 2). Acceptable. One person did every trial at a standardised 0.5 m/s, shirts were worn in random order and changed every 3 to 4 trials, start distance and distance to refuge entered the model as covariates, and the shirts' reflectance was measured and modelled; the stimulus difference between treatments is visual only. The record must not read the result as hue discrimination: by the paper's own modelled luminance contrast (light blue > grey > red > dark blue), red differs from dark blue in luminance as well as hue, which the conditions already say ("The shirts differ in more than hue"). A visually mediated difference in escape, not a sensitivity measure.
- Lines 2, 5, 6 sense_chemical, lines 3, 4 behaviour_vision: acceptable. Line 4 is a null with a defined, measured stimulus set. Grade m right for all six.

## Per-record findings

### Line 1, Sceloporus occidentalis, red v dark blue shirts

Results sentence verbatim in three abutting pieces in one response, twice ("After correcting for multiple comparisons, we found that lizards fled at longer distances" | "when approached with red compared to dark blue" | "(Fig 1), a difference with a large effect (p = 0.033, Cohen’s d = 0.83)."); the curly apostrophe is printed (second pass). **Quote MATCH**, 36 words.

Value says more than the quote: "T-shirt colour affected flight initiation distance (F = 2.89, p = 0.039)" comes from another sentence ("T-shirt color influenced the distance at which lizards fled from an approaching threat (F = 2.89, p = 0.039,"); it must move to conditions.

Verified, verbatim: "pace of 0.5 m/s, which was standardized beforehand"; "One person performed all fieldwork (BJP)."; "we still only conducted trials on warm, sunny days (> 22°C)", "between 0900–1300 h"; "Only lizards that were relatively large adults were sampled"; "we included the main factors of T-shirt color and site, the covariates of start distance and distance to refuge,"; "After explaining significant variation in FID by start distance (F = 5.23, p = 0.024)," "and non-significant variation by distance to refuge (F = 1.83, p = 0.179),"; "found no effect of sex on FID (t89 = 0.345, p = 0.731)"; "Because sex did not affect the two response variables, we did not include it in further analyses."; the trial counts, random order, nulls (p = 0.082, d = 0.68; F = 1.51, p = 0.222; color*site F = 0.154, p = 0.927), capture chi2 = 8.32, p = 0.040 and the collared-lizard proxy and luminance ranking all match the record.

Not carried: the significant start-distance covariate and the null for distance to refuge, the sex null (sex composition not reported), the single observer, approach speed, temperature and time window, adults only. Covariates and the sex null are results of the same model.

**Error (value says more than the quote; significant covariate and sex null omitted).** Fixable.

### Line 2, Ilyanassa obsoleta, food arm in acidified water

Results sentence verbatim in two abutting pieces in one response ("... were more than five times less likely" | "to successfully choose the food side of the Y-maze (12%) than in the control treatments (67% success)."), start and end as recorded. **Quote MATCH**, 38 words.

Value says more than the quote: "(Fisher's exact test p < 0.001)" is from the next sentence ("Fisher’s exact test showed a significant difference in the snails’ ability to locate food between the two treatments", p < 0.001, tool summary for the figure); it must move to conditions.

Verified: Table A1 (tool reading of the table): set 2, 10 min, acid 11 empty, 18 no decision, 4 food; control 4, 7, 22; n 66, p < 0.001 (4/33 = 12 %, 22/33 = 67 %, matching the quote); set 1 p = 0.55; set 3 acid 11, 11, 4, control 0, 8, 8, p = 0.002; "No snails in the control treatments chose the empty side of the Y-maze, while 42% made this choice in acidified treatments." (verbatim); "We conducted experiments at three different times with different researchers; this was not the initial design." (verbatim); pooled 84/27, 87/36, 88/27 % as the record says; starvation, single use and side randomisation not stated (tool summary). The record carries all of these except the set's empty-arm counts (uncounted addition) and the 2017 p = 0.55 (record "p > 0.05", uncounted).

**Error (value says more than the quote).** Fixable.

### Line 3, Partamona helleri, purer and bluish colours

Abstract sentence verbatim in two abutting pieces in one response ("The results show that P. helleri chose colours of higher spectral purity and preferred bluish colours" | ", while M. bicolor made generalized colour choices."). **Quote MATCH**, 23 words.

Value says more than the quote: "significantly more often than less pure ones (Wilcoxon W = 98, p = 0.0003)" and "intensity did not influence choice (W = 93, p = 0.236)" are from the Results ("(W = 98, p = 0.0003, Wilcox test)", "(W = 93, p = 0.236, Wilcox-test)"); they must move to conditions. The Results give no test statistic for dominant wavelength; Figures 2 and 3 captions: "were compared by using a GLMM with Tukey's all pair comparisons as post-hoc test." (verbatim). Design verified: 24 and 20 bees, 57 tests each, one decision per foraging bout, training as recorded, campus hives of unstated origin; "108 of 144" and "17 of 144" verbatim.

**Error (value says more than the quote).** Fixable.

### Line 4, Melipona bicolor, colour preferences absent

Abstract sentence verbatim in two abutting pieces in one response ("The results of P. helleri are consistent with findings for honeybees and bumblebees" | ", while colour preferences in M. bicolor seem to be absent."). **Quote MATCH**, 23 words.

Value says more than the quote and drops its qualifier: the quote says preferences "seem to be absent"; the value states "no distinct colour preference" and carries t statistics from the Results ("spectral purity: t = -0.6589, df = 9, p = 0.5264;", "intensity: t = -0.8655, df = 11, p = 0.4053, Student’s t-test"). The Results give no statistic for dominant wavelength ("Concerning dominant wavelength, workers of M. bicolor showed no distinct preferences", verbatim). The statistics move to conditions. The df below n is unexplained in the paper (tool summary), as the record says.

**Error (value says more than the quote, qualifier dropped).** Fixable. Family/order source replaced (uncounted, see Names).

### Line 5, Bagrada hilaris, coriander and parsley repel females

Results 3.1 sentence verbatim in two abutting pieces in one response ("Adult females of B. hilaris (n = 25) were significantly repelled by volatiles from C. sativum" | "(χ2 = 9; df = 1; p < 0.01) and P. crispum (χ2 = 6.76; df = 1; p = 0.01)."); semicolons and spacing as printed. **Quote MATCH**, 37 words.

Value says more than the quote: the male clause ("males were repelled only by Pelargonium hortorum volatiles (chi2 = 6.67, p = 0.01)") is the next sentence ("For adult males (N = 25), repellency was observed only with P. hortorum volatiles" "(χ2 = 6.67; df = 1; p = 0.01)."); it moves to conditions.

Verified: colony from two organic cabbage fields in Quillota, restocked with field insects; "Newly emerged males and females were then sexed during copulation" (verbatim); starved 5 h; Y-tube 130°, 0.2 L/min; "A maximum response time of five minutes was allowed per insect."; non-responders discarded and excluded, numbers only in Figures 1 and 2 (tool summary); "ranged from 25 to 35 individuals of each sex" (verbatim); pot switched every 10 replicates; O. basilicum attracted males (χ2 = 4.48; df = 1; p = 0.03); the nine species; nulls with their own statistics (tool summary). Not carried or misdescribed: the record says adults were "sexed after emergence"; the paper sexed them during copulation, so tested insects had mated (sample composition). The record's reading of 25 to 35 as insects run to reach 25 responders is an inference, reworded (uncounted).

**Error (value says more than the quote; mating status misdescribed).** Fixable. Not a repeat of main's EAG rows.

### Line 6, Cyanistes caeruleus, sanitation under predator scent

Abstract sentence verbatim in two abutting pieces in one response ("However, females reduced time devoted to nest sanitation activities when predator chemical cues were detected" | "inside the nest-box, likely as an anti-predatory strategy to minimize their own risk of predation."). **Quote MATCH**, 30 words.

Value says more than the quote: the F and contrast statistics and the three null measures come from the Results ("(F2,41 = 3.81, p = 0.03", "differences were only significant when comparing the control and the predator treatments (p = 0.04)", "However, there were no significant differences among treatments."); they move to conditions (the nulls are already there).

Verified, verbatim: "Parent blue tits were captured with nest-box traps when tending 6-day-old nestlings."; "The sex of the adults was determined by the presence of a brood patch, present only in females."; "The capture of adults two days before the experiment may have caused adults to be more cautious"; "We did not include males in this model because males never cleaned the nest."; odour from cages of "two adult male ferrets and two adult male rabbits"; "Two absorbent papers (11 x 13 cm) with the corresponding scent were hidden between the nest and the walls."; "An observer, blind to treatments, analyzed video recordings."; nests 19, 16, 10 (tool summary). Not carried: capture two days before the trial and the authors' caution caveat (design confound); the two-donor odour source (uncounted); the sex main effects of the same models (females entered sooner, F1,42 = 208.51, p = 0.003; provisioned more, F1,40 = 28.69, p < 0.001; tool summary for the statistics), carried as uncounted context because they do not bear on the odour response. Author spelling as above.

**Error (author accent; value says more than the quote; capture confound omitted).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Sceloporus occidentalis, red v dark blue | error, fixable | value, conditions | quote MATCH (36); F test not in quote; start-distance covariate and sex null omitted |
| 2 | Ilyanassa obsoleta, food arm 12 v 67 % | error, fixable | value, conditions | quote MATCH (38); Fisher p not in quote; name accepted (OBIS) |
| 3 | Partamona helleri, purer and bluish | error, fixable | value, conditions | quote MATCH (23); W statistics and intensity null not in quote |
| 4 | Melipona bicolor, preferences absent | error, fixable | value, conditions; note (uncounted) | quote MATCH (23); t statistics not in quote, "seem to be" dropped; family/order source replaced |
| 5 | Bagrada hilaris, females repelled | error, fixable | value, conditions | quote MATCH (37); male clause not in quote; insects sexed during copulation |
| 6 | Cyanistes caeruleus, sanitation | error, fixable | source.authors, value, conditions | quote MATCH (30); "Tomás"; statistics not in quote; capture two days before trial omitted |

Errors 6 of 6 audited records (100%), above the 5% bar; none held out. By kind: value says more than the quote 6 (every line; the desk's notes say the extra statistics came from other sentences, so the pattern is systematic, as in audit 352); scientific-context 3 (lines 1, 5, 6); bibliographic 1 (line 6); quote form 0; licence 0; names 0 (one source replaced, uncounted); duplicates 0 against main, all 138 desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0.

Answers to the desk-d260 owner questions.
1. Melipona bicolor: Apidae, Hymenoptera confirmed for the species by the Plazi treatment deposit (Rozen et al. 2021, American Museum Novitates 3971); a genus row on main is not a species source, and the note is corrected.
2. Coloured-shirt FID trial: acceptable as behaviour_vision (single observer, fixed speed, random shirt order, measured and modelled shirt colours, distance covariates), read as a visually mediated escape difference that may rest on luminance as well as hue.
3. Ilyanassa obsoleta: accepted in OBIS; OBIS lists Tritia obsoleta as a superseded combination with Ilyanassa obsoleta the accepted name. Filed correctly.

## Unchecked

- Line 1: the Reptile Database page for family and order (not reopened); sex composition of the sample (not in the paper); chromatic contrast values.
- Line 2: Table A1 cells read through the tool (the last control row garbled); whether snails were reused.
- Lines 3, 4: why df is 9 and 11 for 20 bees; Figures 2 and 3 GLMM results; colony origin (not stated).
- Line 5: the number of non-responders (figures only); the seven null statistics per sex (tool summary).
- Line 6: per-contrast p for the rabbit control (not printed); treatment F for the null measures (not printed).
- Melipona bicolor accepted status beyond the 2021 treatment (no checklist page opened; Moure's catalogue page opened was a different genus).

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For an empty new string the old string is deleted.

Line 1, counted:
- `value`: ", Cohen's d = 0.83); T-shirt colour affected flight initiation distance (F = 2.89, p = 0.039)" -> ", Cohen's d = 0.83)"
- `conditions`: "Nulls: red v light blue" -> "Overall, T-shirt colour affected FID (F = 2.89, p = 0.039). The model included start distance and distance to refuge as covariates: start distance explained significant variation in FID (F = 5.23, p = 0.024), distance to refuge did not (F = 1.83, p = 0.179). Sex had no effect on FID (t89 = 0.345, p = 0.731) and was dropped from later analyses; the sex composition of the sample is not given. One person performed all trials, approaching at a standardised 0.5 m/s, on warm sunny days (> 22 C) between 0900 and 1300 h; only relatively large adults were sampled. Nulls: red v light blue"
- `note` (uncounted): "Not on main or any desk branch (grep of 0182146 and Sceloporus occidentalis)." -> "Not on main or any desk branch (grep of 0182146 and Sceloporus occidentalis). Curly apostrophe in 'Cohen’s' as printed (audit 356)."

Line 2, counted:
- `value`: " (Fisher's exact test p < 0.001)" -> ""
- `conditions`: "Other sets:" -> "Fisher's exact test for this set p < 0.001 (the Results sentence after the quote); Table A1 counts for the set: acidified 4 food, 11 empty, 18 no decision; control 22 food, 4 empty, 7 no decision. Other sets:"
- `note` (uncounted): "gbif-names.tsv lists Nassa obsoleta as a synonym of Ilyanassa obsoleta." -> "gbif-names.tsv lists Nassa obsoleta as a synonym of Ilyanassa obsoleta; OBIS gives Tritia obsoleta (Say, 1822) as a superseded combination with Ilyanassa obsoleta the accepted name (audit 356)."

Line 3, counted:
- `value`: "chose spectrally purer colours significantly more often than less pure ones (Wilcoxon W = 98, p = 0.0003) and preferred bluish colours; intensity did not influence choice (W = 93, p = 0.236)" -> "chose colours of higher spectral purity and preferred bluish colours"
- `conditions`: "P. helleri: blue and UV-absorbing white" -> "P. helleri statistics (Results): spectral purity W = 98, p = 0.0003 (Wilcoxon), intensity no effect (W = 93, p = 0.236); the Results text gives no test statistic for dominant wavelength (Figures 2 and 3 compare pooled choices by GLMM with Tukey all-pair comparisons). P. helleri: blue and UV-absorbing white"

Line 4, counted:
- `value` = "colour preferences seem to be absent in dual-choice tests of dominant wavelength, spectral purity and intensity"
- `conditions`: "A null for colour preference in this species;" -> "Results statistics: no preference for spectral purity (t = -0.6589, df = 9, p = 0.5264) or intensity (t = -0.8655, df = 11, p = 0.4053, Student's t-test); for dominant wavelength the Results say only that workers showed no distinct preferences (no statistic in the text). A null for colour preference in this species;"
- `note` (uncounted): "family and order Apidae, Hymenoptera are those on main for Melipona quadrifasciata and M. marginata (same genus, canon-3 rows) and are not printed in the paper (it gives the tribe Meliponini). Not in gbif-names.tsv; accepted-name status unchecked." -> "family Apidae and order Hymenoptera from the Plazi treatment 'Melipona (Eomelipona) bicolor Lepeletier' (Zenodo record 5452960, from Rozen, Almeida, Smith and Jones 2021, American Museum Novitates 3971, 10.1206/3971.1; audit 356); the paper names only the tribe Meliponini. Not in gbif-names.tsv; OBIS has no record."

Line 5, counted:
- `value`: "; males were repelled only by Pelargonium hortorum volatiles (chi2 = 6.67, p = 0.01)" -> ""
- `conditions`: "Nulls: Pelargonium hortorum had no effect on females" -> "Males (n = 25) were repelled only by Pelargonium hortorum volatiles (chi2 = 6.67, df = 1, p = 0.01). Nulls: Pelargonium hortorum had no effect on females"
- `conditions`: "adults sexed after emergence" -> "newly emerged adults sexed during copulation (so tested insects had mated; age not otherwise given)"
- `conditions` (uncounted): "(25 to 35 insects per sex had to be run because non-responders were excluded, so the test is of responders)" -> "(the Methods say 25 to 35 individuals of each sex were tested; insects that did not move toward either arm within 5 min were scored as non-responses and excluded, their number shown only in Figures 1 and 2, so the test is of responders)"

Line 6, counted:
- `source.authors`: "Gustavo Tomas" -> "Gustavo Tomás"
- `value`: " (treatment effect F2,41 = 3.81, p = 0.03; only the water-control versus predator contrast was significant, p = 0.04); entry latency, provisioning rate and number of begging nestlings did not respond to the odour treatment" -> ""
- `conditions`: "Parents were captured and marked and sexed by brood patch." -> "Parents were captured with nest-box traps when nestlings were 6 days old, two days before the trial, and sexed by brood patch (present only in females); the authors say the capture may have made adults more cautious. Female sanitation differed by treatment (F2,41 = 3.81, p = 0.03), significant only between the water control and the predator cue (p = 0.04); no statistics are printed for the other two contrasts. Odour donors were two adult male ferrets and two adult male rabbits; two absorbent papers (11 x 13 cm) per box. Regardless of odour, females entered sooner (F1,42 = 208.51, p = 0.003) and provisioned more (F1,40 = 28.69, p < 0.001) than males."

Verdict: 6 of 6 audited records in error (100%), above the 5% bar; all six fixable with the replacement text above; none held out.
