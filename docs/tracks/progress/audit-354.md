# audit-354: desk-d258, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d258 files present untracked in the worktree (docs/tracks/progress/desk-d258.md and docs/views/evidence/desk-d258.jsonl, 8 lines; neither committed here, neither edited). Worktree HEAD and origin/main a9fc0999 (desk-d257 after audit 353). `python3 -I tools/senses/check.py | grep 'd258\.'`: "docs/views/evidence/desk-d258.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 33, 31, 39, 13, 38, 26, 32, 37, all within 40; non-ASCII "χ" (line 1), "−" and "…" (line 3), "…" (line 5), checked against the page where the page was opened. Format model audits 352 and 353; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for all seven DOIs (10.1371/journal.pone.0000556, 10.1371/journal.pone.0304220, 10.1371/journal.pone.0045016, 10.3389/fevo.2024.1470023 (two passes, title in two pieces), 10.1371/journal.pone.0236660, 10.3390/insects9030091, 10.1371/journal.pone.0172422; all answered, none robots_disallowed); journals.plos.org pone.0000556 (three passes), pone.0304220 (two), pone.0045016 (two; the first declined the sentence and gave a summary), pone.0236660 (two), pone.0172422 (two); frontiersin.org fevo.2024.1470023/full (one). mdpi.com/2075-4450/9/3/91 (line 6) returned "PROVENANCE_REQUIRED ... The permission request for this URL was not answered in time. Do not retry."; it was not retried and no other copy or path was tried. Names: api.obis.org/v3/taxon/<name> for Salvator merianae, Trissolcus basalis, Listronotus bonariensis and Leptoglossus zonatus (total 0 each, terrestrial); the query form `taxon?scientificname=` named in the launch prompt failed (client_error) and was not worked around beyond the path form used in audits 331, 351 and 353. Species pages from WebSearch results: reptile-database.reptarium.cz/Salvator/merianae, nzor.org.nz (Trissolcus basalis; Listronotus bonariensis), wiki.pestinfo.org (Chen et al. 2021, Systematic Entomology 46: 1088-1113), gd.eppo.int/taxon/LEPLZO. No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 5 WebSearches and 25 WebFetch calls used.

## Bibliographic and licence

- Line 1 (Raine and Chittka 2007). Crossref: Nigel E. Raine, Lars Chittka; title identical; PLoS ONE 2(6) e556; issued 2007-06-20; CC BY 4.0 content-version unspecified; relation empty. Page: "This is an open-access article distributed under the terms of the Creative Commons Attribution License,". Accepted (unspecified + page-printed sentence). Faults 0.
- Line 2 (Van Hee et al. 2024). Crossref: nine authors in the recorded order (Sara Van Hee ... Bart Lievens); title identical (two pieces joined at "Trissolcus basalis" | "in response to"); PLOS ONE 19(5) e0304220; issued 2024-05-21; CC BY 4.0 vor. Page prints the Creative Commons Attribution License sentence. Faults 0.
- Line 3 (Choe, Villafuerte, Tsutsui 2012). Crossref: as recorded; PLoS ONE 7(9) e45016; issued 2012-09-20; CC BY 4.0 unspecified; page CC BY sentence (tool summary on pass 1). Faults 0.
- Line 4 (Vereijssen et al. 2024). Crossref: Jessica Vereijssen, Rob van Tol, Michael Rostás, Chikako van Koten, Stephen Goldson; title in two verbatim pieces ("Olfactometer-measured responses of Listronotus bonariensis (Kuschel) (Coleoptera: Curculionidae)" | "to feeding-induced grass volatiles and conspecific frass as influenced by the weevil's seasonality"), identical to the record; Frontiers in Ecology and Evolution 12, 1470023, no issue; issued 2024-11-19; CC BY 4.0 vor. Page shows no licence sentence (tool summary). Accepted (no page sentence + Crossref vor CC). Faults 0.
- Line 5 (Richard et al. 2020). Crossref: ten authors in the recorded order; title identical; PLOS ONE 15(8) e0236660; issued 2020-08-12; CC0 1.0 vor. Page: "The work is made available under the Creative Commons CC0 public domain dedication." Accepted. Faults 0.
- Line 6 (Franco-Archundia et al. 2018). Crossref: four authors in the recorded order; title identical; Insects 9(3) 91; issued 2018-07-26; CC BY 4.0 vor. Publisher page not opened (above), so the page licence and all page content are unverified.
- Lines 7 and 8 (Rothery, Scott, Morrell 2017). Crossref: as recorded; title identical; PLOS ONE 12(2) e0172422; issued 2017-02-17; CC BY 4.0 vor; relation has-preprint 10.1101/103671 (the record cites the version of record, which is right); funders Westland Horticulture and University of Hull. Page prints the Creative Commons Attribution License sentence. Faults 0.

Bibliographic faults 0; licence faults 0. source.access "open" right for lines 1 to 5, 7, 8.

## Names

- Bombus terrestris (line 1): main gbif-names.tsv:701 EXACT ACCEPTED; Apidae, Hymenoptera as on main's rows. Colony source (launch question): not commercial. Verbatim: "The nine bumblebee colonies used in this study were raised in the laboratory from nest searching queens" "caught around Würzburg, Germany."; colour-naive by rearing in darkness. Laboratory colonies founded by wild queens of a wild species are acceptable at species rank (audit 332); the managed-colony question does not arise. Met.
- Trissolcus basalis (line 2): not in gbif-names.tsv; OBIS total 0. NZOR: "Trissolcus basalis (Wollaston, 1858)", preferred name, but classified Platygastridae (Platygastroidea, Hymenoptera), the older broad family. Chen et al. 2021 (Systematic Entomology 46: 1088-1113) recognise "Scelionidae stat.rev." as a family within Platygastroidea; the paper prints Scelionidae. The record's Scelionidae follows the current classification; that Chen et al. place Trissolcus (Telenominae) in Scelionidae was not read on a species page (unchecked). Met, note addition uncounted.
- Linepithema humile (line 3): main gbif-names.tsv:2701 EXACT ACCEPTED; Formicidae (title as printed), Hymenoptera. Met.
- Listronotus bonariensis (line 4): not in gbif-names.tsv; OBIS total 0. NZOR: "Listronotus bonariensis (Kuschel, 1955)", preferred name, Curculionidae, Coleoptera. Met; note provenance addition uncounted.
- Salvator merianae (line 5): not in gbif-names.tsv; OBIS total 0. Reptile Database: "Salvator merianae DUMÉRIL & BIBRON, 1839"; "Higher Taxa Teiidae, Tupinambinae, Gymnophthalmoidea, Sauria, Squamata (lizards)"; Tupinambis merianae listed among synonyms. Wild-caught invasive animals held in outdoor pens (not a captive-bred stock). Met; note addition uncounted.
- Leptoglossus zonatus (line 6): not in gbif-names.tsv; OBIS total 0. EPPO LEPLZO: preferred name "Leptoglossus zonatus (Dallas)", Coreidae, Hemiptera. Name met, but the line is held out (below).
- Parus major, Passer domesticus (lines 7, 8): gbif-names.tsv:3611 and :3613 EXACT ACCEPTED; Paridae and Passeridae, Passeriformes. Free-living birds at feeders. Met.

Name faults 0.

## Duplicates

git grep on origin/main (a9fc0999) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, progress) for each DOI suffix (0000556, 0304220, 0045016, 1470023, 0236660, insects9030091, 0172422), for Trissolcus, Listronotus, Salvator, Tupinambis, "Leptoglossus zonatus", Rothery, Raine, and for each species' rows with their traits; then the branch-only additions (`git diff origin/main...<branch>`) of all 134 remote branches matching origin/research/desk-d2* or origin/research/audit-3*; and grep of docs/tracks/progress/audit-3*.md.

- No DOI of this unit is filed on main or any other branch. The "0000556" hit is an unrelated string in searched/rescreen-1.jsonl (Linaria). Trissolcus appears only in desk-d226 (T. mitsukurii, not opened) and desk-d235 (not filed). Salvator/Tupinambis appear only in gaps, the QUEUE note on pupil shape, codex findings and audit-59 (no sense_chemical row).
- Leptoglossus zonatus: desk-d255.md on main lists this same paper as not filed: "Leptoglossus zonatus colours (insects9030091; internal contradictions in the statistics, lab-reared)". That is a prior desk hold-out of the same record, not cited in desk-d258's note or progress file (counted with line 6's hold-out reason, not as a duplicate).
- Bombus terrestris on main: one behaviour_vision row (10.1242/jeb.00570, target-detection precision by body size), a different paper and finding. Linepithema humile: interommatidial_deg only. Parus major: colour_vision rows from a review (10.1017/S1464793102005985), no behaviour_vision. Passer domesticus: one behaviour_vision row (10.1242/jeb.246063, "near-resolving foraging category") and one sense_chemical row (pone.0167905). Launch question: the feeder-choice rows are from a different paper and a different finding (colour choice at feeders against a foraging-mode classification), so they are not repeats.

Duplicates 0.

## Trait keys and rulings

- behaviour_vision, unrewarded two-colour artificial flowers (line 1): acceptable.
- sense_chemical, Trissolcus Y-tube (line 2): owner question. Keep under sense_chemical with the disclosure. The trait records the wasp's olfactory response to an odour source in a Y-tube with clean-air controls and position swaps; whether the source is plant volatiles alone or plant plus host-egg odour changes what the odour is, not which sense the result concerns. The paper does not say whether egg masses or bugs were removed ("Plants were used in the experiments 24 h after exposure to feeding or within 24 h after discovery of an egg mass"; removal not stated, tool summary), so the value must not say the plants were "carrying" eggs, and conditions keep the record's existing disclosure.
- sense_chemical, Argentine ant Y-maze, weevil still-air olfactometer, tegu scent-trail Y-maze (lines 3 to 5): acceptable.
- behaviour_vision, feeder colour choice (lines 7, 8): owner question on pseudo-replication. Acceptable at grade m with disclosure. The authors write "as it was not possible to distinguish between individuals of the same species," and "each visit to the feeders was counted as an independent data point."; the model adds "Observation period and site were added as random effects to account for non-independence of visits", which handles clustering by period and site but not repeat visits by one bird within a period. The values claim only visit-level differences ("visited ... less"), which is what visit counts support; they make no claim about individual preference. The disclosure is already in conditions; the authors' own sentence is added (uncounted). Each species is carried by its own sentence and statistic, so one paper supports two lines.
- Grade m right for lines 1 to 5, 7, 8.

## Per-record findings

### Line 1, Bombus terrestris, violet over blue

Results sentence verbatim in two abutting pieces in one response, joined at "(bee UV-blue)" | "over blue", same join on a second pass ("In this bumblebee population, we observed a significant overall bias towards choosing violet (bee UV-blue)" | "over blue (bee blue) flowers in laboratory preference tests" "(χ2 = 15.8, df = 8, p = 0.044)."). **Quote MATCH**, 33 words; value says no more ("colour-naive" and "unrewarded" are design, verified).

Verified, verbatim: "Colony colour biases (n = 9 colonies) were calculated by averaging across the 10–15 forager bees tested per colony" "(101 bees were tested in total)."; "(1652 flower choices were recorded in total)."; "differ in the position of their short wave reflectance peak," "which are at wavelengths of 435 and 460 nm respectively."; "flight arena (120 cm×100 cm×35 cm)"; "16 unrewarding, coloured test flowers: 8 violet (bee UV-blue) and 8 blue (bee blue) targets."; "All flowers were changed between foraging bouts"; "In the nine colonies tested, the median bias for violet (over blue) ranged from 47.7% to 63.6%"; "(Mann-Whitney U = 29.5, p = 0.012)."; "rs = 0.678; n = 9; p = 0.045) for the nine colonies tested."; the 2001 correlation "positive, though not statistically significant" (rs = 0.82, n = 5, p = 0.089, tool summary); forager mass uncorrelated (tool summary).

Not carried: the paper reports no green-receptor (achromatic) contrast or brightness comparison between the two colours, only the short-wave peaks and a colour-hexagon distance of about 0.3 units (tool summary), so intensity matching is not shown; the test behind "χ2 = 15.8, df = 8" is not named and its reference proportion is not stated (tool summary; the units field's "chi-squared across 9 colonies" reads more into it than the paper says); "The number of flower choices evaluated per forager ranged from 6 to 58 (mean±1 SE = 16.4±0.9)"; the test-flower layout is not described (training flowers "arranged randomly" and "regularly reshuffled", tool summary); foraging rate was measured in the field near Gieshügel, Würzburg, 14 June to 12 July 2002, and the Fisher combination of the two years gave χ2 = 11.04, df = 4, p = 0.026 (tool summary).

**Error (intensity/achromatic matching not reported and not disclosed; test unnamed; unequal choices per bee).** Fixable.

### Line 2, Trissolcus basalis, oviposition-induced pepper volatiles

Results sentence verbatim in two abutting pieces in one response ("In two-choice Y-tube olfactometer bioassays, females of T. basalis significantly preferred sweet pepper volatiles" | " induced by N. viridula oviposition over volatiles from non-infested control plants (Co versus Co_O: P = 0.009)."); first piece identical on a second pass. **Quote MATCH**, 31 words.

Value says more than the quote: "plants carrying Nezara viridula eggs" is not printed (the quote says "induced by N. viridula oviposition", and egg removal is not stated), and "spent significantly more time" comes from the following sentence ("More specifically, the wasps spent 60.5% more time in the olfactometer arm containing the oviposition-induced" | " plant volatiles."). The value must be cut to the quote.

Verified, verbatim: "Twenty-four hours prior to the experiments, female T. basalis that were 5–7 days old were individually transferred"; "To maintain the parasitoid colony, N. viridula egg masses were individually exposed to two mated T. basalis females."; "Charcoal-filtered air at a flow rate of 0.8 L min-1 was pumped into each of the olfactometer arms"; "Wasp responses were recorded for 10 min"; "Each bioassay was replicated using five pairs of plants, and ten female wasps per pairwise combination were tested"; "The position of the plants was switched after testing five wasps"; "Behavioural data were analysed by linear mixed models (LMMs) with fungal treatment as a fixed factor"; controls "physiological saline solution to obtain non-inoculated, control plants (Co)."; plants "individually exposed to two gravid N. viridula females or were left untouched."; "while the uninfested plants were incubated in cages under the same conditions." Pairings Co vs Co_F P = 0.868, Co_F vs Bb_F P = 0.158, Co_F vs Th_F P = 0.440, Co_O vs Th_O P = 0.019 with 38.4 % more time in the T. harzianum arm, Co_O vs Bb_O P = 0.009 with contradictory direction text (tool summary). The record's nulls and the conflict are right, but it attaches "its direction" to both fungus pairings, whereas only the B. bassiana direction is inconsistent.

Not carried: handling of non-responding wasps is not reported, and the tested females' mating status and oviposition experience are not stated (tool summary).

**Error (value exceeds quote; non-response handling unreported).** Fixable.

### Line 3, Linepithema humile, (Z)-9-hexadecenal

Results sentence returned on the second pass in three consecutive verbatim excerpts in one response ("Y-maze bioassays also indicated that high concentrations of synthetic (Z)-9-hexadecenal were effective" | "at attracting worker ants, as more than 90% of ants chose the arms treated with 200 pg cm−1" | "(1.5×10−2-ant equivalent cm−1) and 20 pg cm−1 (1.5×10−3-ant equivalent cm−1) of (Z)-9-hexadecenal", followed by a Table 1 citation). The first pass declined the sentence but its short quote "more than 90% of ants chose the arms" agrees; the desk read the same joins. The cuts drop two ant-equivalent conversions and the trailing table reference, none a qualifier (audit-331 conditions met); minus signs "−" match. **Quote MATCH**, 39 words; value says no more.

Verified (tool summary on pass 1): 0.2 pg cm−1 did not attract; the dolichodial plus iridomyrmecin mixture alone did not attract at subthreshold levels, and with 0.2 pg cm−1 (Z)-9-hexadecenal "65–86% ants chose the treated arm,"; (Z)-9-hexadecenal not detected in trail extracts, GC-MS limit about 0.1 ng; three filter-paper arms at 120 degrees, 5 ants per maze, each ant used once, 12 or 24 replicates, solvent-only control, chi-squared and one-sided Dunnett-type test; Berkeley colony fragments, summer 2011. The record carries all of these and discloses that Table 1 was not read. **MATCH.**

### Line 4, Listronotus bonariensis, frass suspension

Results sentence read whole in one piece: "Frass in suspension (Subtreatment 6) was also significantly attractive to the diapausing weevils." **Quote MATCH**, 13 words; value says no more ("conspecific" and "over water" are design).

Verified (tool summary unless quoted): Table 2 subtreatment 6, 35.2 % (45/128) water against 64.8 % (83/128) frass, p = 0.012; subtreatment 2, 61.4 % (124/202) undamaged against 38.6 % (78/202) damaged, p < 0.001 (the record's text/table conflict is right); "The weevils were not sexed, as field populations are known to approximate a 1:1 sex ratio"; held 1 to 3 weeks at 18 ± 2 °C, 16:8 L:D, starved 24 h; still-air olfactometer after the Y-tube "produced no results"; 10 weevils per run, 4 h runs beginning 4 to 6 h after scotophase, dishes turned 90 degrees; "those that remained undecided (i.e., no choice) were excluded from the analysis."; "one-sample binomial exact test"; "This study found no significant response of reproductive L. bonariensis populations at all to the VOC/HIPVs", p > 0.05 in all cases.

Not carried: diapausing weevils were collected at four sites (Taiko, 1 March 2011; Upper Takaka, 16 March; Lincoln, 28 April; North Otago, 30 May) and reproductive weevils at one (Irwell, 21 September to 22 November 2011), so the seasonal contrast is confounded with collection site and population; the record gives only "New Zealand pastures". The frass n (83 of 128 choosers) is not given (the record's "about 65 %" is right; uncounted). Sex was recorded later only by dissecting responsive weevils (uncounted).

**Error (season confounded with collection site omitted).** Fixable.

### Line 5, Salvator merianae, female trailing of male scent

Results sentence verbatim in three consecutive pieces in one response ("Females (n = 7 for all trial types) in spring showed a preference for male scent" | "in the Male-only trials (7/7; P < 0.001) and marginal preferences in the Male vs. female trials" | "(6/7 chose male scent; P = 0.054) and Female-only trials (6/7; P = 0.054)"), followed by "(Fig 1)." on the second pass. The two cuts drop the marginal statistics and the figure reference, keeping "marginal"; acceptable under audit 331. **Quote MATCH**, 38 words; value says no more.

Verified, verbatim: "Male (n = 7) and female (n = 7) Argentine black and white tegus (Salvator merianae) were caught" "in the vicinity of Homestead, FL (Miami-Dade County)"; "Tegus were captured and brought to the field station at different times (2010, 2013, 2018)"; "all animals were acclimated to captivity and spent at least one winter in the outdoor pens prior to testing."; "To create a scent trail, a randomly chosen stimulus animal was selected,"; "The open arm was randomly selected."; "tegus were assigned to trial types in a fully randomized design."; "acclimated for approximately 60 min, then allowed to explore the maze."; "Males and females experienced all trial types in Spring."; bias tests "(males: 2/7 chose the North arm, P = 0.224;" "females: 3/7 chose the North arm, P = 0.5)."; male results "(5/7, P = 0.224)", "(4/7, P = 0.5)", "(2/7 chose female, P = 0.224)."; measures "Arm choice, choice penalty score, rate of tongue-flicking (tongue-flicks per min), pauses, turns," "passes through each arm, and various trailing times were recorded." No exclusions reported (tool summary).

Not carried: "Binomial tests were used for arm choice data." with tails and exactness unstated; by the auditor's calculation an exact binomial test on n = 7 gives at least 0.0078 (one-tailed) for 7/7 and 0.0625 for 6/7, so the printed "P < 0.001" and "P = 0.054" do not match an exact binomial test (the males' 0.224 and 0.5 do match one-tailed values), and the value's "P < 0.001" is the paper's figure, not a checked one. Launch question on tongue-flick against other measures: the stimulus is a scent trail and the measures are arm choice, time, turns, penalty score and tongue-flick rate (no bite measure); significant results from the same trials are not carried: "Females also spent more time in the target arm," (F1,41 = 53.47, P < 0.001, mainly Female-only trials), "Turning behavior was female-biased" (F1,41 = 27.19, P < 0.001), "Male RTF was higher than female RTF in each trial type" (sex effect F1,41 = 22.11, P < 0.001), and in fall "male tegu performance in the Y-maze trials was similar to spring." with lower tongue-flick rates (statistics tool summary).

**Error (test details and P-value inconsistency undisclosed; same-trial significant measures omitted).** Fixable.

### Line 6, Leptoglossus zonatus, card colours

Publisher page not opened (permission request not answered; the tool said not to retry, and it was not retried). Quote, design, n, statistics and nulls are unverified. Crossref bibliography and licence are right (above). desk-d255 on main had already not filed this paper for "internal contradictions in the statistics", and desk-d258's own conditions disclose a df conflict (text df = 4, figure legend df = 5) and a chi-squared statistic attached to a Kruskal-Wallis comparison. **HOLD OUT** (page not opened by the auditor; prior desk hold-out on main not addressed).

### Line 7, Parus major, feeder colour

Results sentences verbatim, the quote in two abutting pieces in one response ("There were significantly fewer visits to yellow than to all other colours except red (p < 0.05 in all cases)," | "while red was visited significantly less often than green (p = 0.017)."), preceded by "For great tits ([Fig 2C], [S2 Table]), there was a significant effect of colour on number of visits" "(F7,259 = 2.671, p = 0.011)." **Quote MATCH**, 32 words; value says no more.

Verified, verbatim: "we recorded bird visit rates to 8 different coloured feeders at three sites on 78 sampling days" "during the winter/spring of 2014/15 (November 2014 to May 2015)."; the three sites; "Data were collected across a total of 370 observation periods (Otley: 208; Tophill; 26 Botanic Gardens: 136)," "and a total of 7535 visits to the feeders were recorded"; "The metal parts of each feeder were painted a single colour using Hammerite Metal Paint."; "it was not possible to measure reflectance in the UV range or transform the RGB values into avian colour space"; Poisson GLMM, "Observation period and site were added as random effects to account for non-independence of visits"; FDR correction; greenfinch "(F7,140 = 1.3.383, p = 0.217)" (as printed), starling "(F7,84 = 1.232, P = 0.294),"; coal tit overall effect "but no significant pairwise comparisons were found after correction for multiple testing."; "no other species was recorded more than 100 times"; feeders "Natures Feast Royal Seed Feeders, Westland Horticulture." and seed from the same firm; "Consumables/travel funding was received from Westland Horticulture to carry out the research." "Westland Horticulture played a role in the conceptualisation of the research question," (so "The funder was the feeder manufacturer" is right). Blue tit and robin were also analysed (tool summary); not needed for these lines. **MATCH.** Uncounted additions: the overall F, unequal periods per site, the authors' independent-data-point sentence, and the funder's role in conceiving the question.

### Line 8, Passer domesticus, feeder colour

Quote verbatim in two abutting pieces with the in-text links rendered as brackets on the second pass ("The yellow feeder was visited significantly less often than all other colours ([Fig 2E], [S4 Table], p < 0.05 in all cases)" | "and red was visited less often than blue, green, silver and black (p < 0.05)."), preceded by "For house sparrows, there was a significant effect of colour on visits (F7,399 = 11.139, P < 0.001)." The record's "(Fig 2E, S4 Table, p < 0.05 in all cases)" matches the printed text with links removed. **Quote MATCH**, 37 words; value says no more. Design verified as line 7. **MATCH.** Uncounted additions as line 7 with the sparrow F.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Bombus terrestris, violet over blue | error, fixable | units, conditions, note (uncounted) | quote MATCH (33); no achromatic/intensity comparison, test unnamed, 6 to 58 choices per bee |
| 2 | Trissolcus basalis, oviposition-induced volatiles | error, fixable | value, conditions | quote MATCH (31); value adds "carrying eggs" and "more time"; non-response handling unreported |
| 3 | Linepithema humile, (Z)-9-hexadecenal | MATCH | none | quote MATCH (39), cuts acceptable |
| 4 | Listronotus bonariensis, frass suspension | error, fixable | conditions, note (uncounted) | quote MATCH (13); season confounded with collection site |
| 5 | Salvator merianae, female trailing | error, fixable | conditions, note (uncounted) | quote MATCH (38); printed P values do not fit an exact binomial on n = 7, tails unstated; time, turning and tongue-flick results omitted |
| 6 | Leptoglossus zonatus, card colours | HOLD OUT | none | page not opened by auditor; desk-d255 hold-out for internal statistical contradictions not addressed |
| 7 | Parus major, feeder colour | MATCH | conditions, note (uncounted) | quote MATCH (32) |
| 8 | Passer domesticus, feeder colour | MATCH | conditions, note (uncounted) | quote MATCH (37) |

Errors 4 of 7 audited records (57%), above the 5% bar, plus 1 held out unaudited: scientific-context 4 (lines 1, 2, 4, 5), of which value exceeding quote 1 (line 2), omitted design confounds 3 (lines 1, 2, 4), omitted results or test detail 2 (lines 1, 5); names 0; quote form 0; bibliographic 0; licence 0; duplicates 0 against main, all 134 desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. HOLD OUT: line 6.

Answers to the desk-d258 owner questions.
1. Trissolcus: keep under sense_chemical with the disclosure, but the value must say "induced by oviposition", not "carrying eggs".
2. Passer domesticus feeder-choice row: not a repeat of main's foraging-mode row (different paper and finding); acceptable.
3. Visits as data points: acceptable at grade m with the disclosure and the authors' own sentence; the values claim visit-level differences only.
Launch questions: Bombus colonies were from wild queens, not commercial; Salvator merianae is the accepted name (Reptile Database, Teiidae, Squamata), animals wild-caught.

## Unchecked

- Line 1: the unnamed test behind χ2 = 15.8, df = 8; test-flower layout; Figure 4 values.
- Line 2: the mating status and experience of tested wasps; whether egg masses stayed on plants; Trissolcus in Scelionidae on a species-level page under Chen et al. 2021.
- Line 3: Table 1 (per-concentration n and control result).
- Line 4: number of runs and excluded undecided weevils for subtreatment 6; dissection sex ratios.
- Line 5: whether the binomial P values were computed by a normal approximation or other method.
- Line 6: everything on the publisher page.
- Lines 7, 8: Table 1 per-species visit counts; which sites contributed great tit and sparrow visits.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For blank fields the form is field = new string.

Line 1, counted:
- `units`: "categorical (colony-level choice bias, chi-squared across 9 colonies)" -> "categorical (colony-level choice bias across 9 colonies; chi-squared statistic as printed, test not named)"
- `conditions`: "no side-swap or position-randomisation detail was read." -> "the arrangement of the 16 test flowers is not described (only the training flowers are said to be arranged randomly and reshuffled). The paper gives the two colours' short-wave reflectance peaks and a colour-hexagon distance (about 0.3 units) but no green-receptor (achromatic) contrast or brightness comparison, so intensity matching is not shown; the test behind chi2 = 15.8, df = 8 is not named and its reference proportion is not stated. Choices per bee ranged from 6 to 58 (mean 16.4 +/- 0.9 SE). Colony foraging rates were measured in the field near Wuerzburg (14 June to 12 July 2002); combining the 2001 and 2002 correlations by Fisher's method gave chi2 = 11.04, df = 4, p = 0.026."
- `note` (uncounted): "Not on main or any desk branch" -> "Colonies from wild nest-searching queens, not a commercial supplier (audit 354). Not on main or any desk branch"

Line 2, counted:
- `value`: "females spent significantly more time in the arm with volatiles of sweet pepper plants carrying Nezara viridula eggs than in the arm with clean control-plant volatiles (P = 0.009)" -> "females significantly preferred sweet pepper volatiles induced by Nezara viridula oviposition over volatiles from non-infested control plants (P = 0.009)"
- `conditions`: "Co_O vs Th_O was significant (P = 0.019) and Co_O vs Bb_O significant (P = 0.009) but the text is inconsistent on its direction, so those are not logged." -> "Co_O vs Th_O was significant (P = 0.019, wasps about 38 % longer in the Trichoderma harzianum arm) and Co_O vs Bb_O significant (P = 0.009) but the text is inconsistent on the Beauveria bassiana direction, so those are not logged. Bug-exposed and control plants were all caged; the handling of wasps that made no choice is not reported, and the tested females' mating status and oviposition experience are not stated. The value is the preference sentence; residence time is the measure and the 60.5 % figure is in the next sentence."

Line 4, counted:
- `conditions`: "Argentine stem weevils collected from New Zealand pastures and held 1 to 3 weeks;" -> "Argentine stem weevils collected from New Zealand pastures and held 1 to 3 weeks at 18 +/- 2 C, 16:8 L:D, starved 24 h before assays; diapausing weevils came from four sites (Taiko, Upper Takaka, Lincoln, North Otago) and reproductive weevils from one (Irwell), so season is confounded with collection site and population;"
- `conditions` (uncounted): "Table 2 gives about 65 % choosing frass (p = 0.012)" -> "Table 2 gives 64.8 % (83 of 128 choosing weevils) choosing frass against 35.2 % (45) choosing water (p = 0.012)"
- `note` (uncounted): "Family and order from the title as printed." -> "Family and order from the title as printed and NZOR (Listronotus bonariensis (Kuschel, 1955), preferred name, Curculionidae, Coleoptera; audit 354)."

Line 5, counted:
- `conditions`: "Choice outcome, not a threshold." -> "Choice outcome, not a threshold. The paper says only that binomial tests were used (tails and exactness not stated); by the auditor's calculation an exact binomial test on n = 7 cannot give less than 0.0078 (one-tailed) for 7/7, and gives 0.0625 for 6/7, so the printed P < 0.001 and P = 0.054 do not match an exact binomial test (the males' 0.224 and 0.5 do). The same animals ran every trial type in spring. Other measures from the same trials: females spent more time in the target arm (F1,41 = 53.47, P < 0.001, mainly in Female-only trials), turning was female-biased (F1,41 = 27.19, P < 0.001), and males had higher tongue-flick rates than females in every trial type (F1,41 = 22.11, P < 0.001); in fall, male Y-maze performance was similar to spring, with lower tongue-flick rates. No bite measure was taken."
- `note` (uncounted): "the paper uses Salvator merianae." -> "the paper uses Salvator merianae, the accepted name on the Reptile Database (Salvator merianae Dumeril & Bibron, 1839; Teiidae, Tupinambinae, Squamata; Tupinambis merianae a synonym; audit 354)."

Line 6: HOLD OUT (publisher page not opened by the auditor; desk-d255's hold-out for internal contradictions in the statistics, on main, not addressed by the desk).

Line 7, uncounted:
- `conditions`: "Per-species visit counts are in Table 1 (image, not read)." -> "Per-species visit counts are in Table 1 (image, not read). Overall colour effect for great tits F7,259 = 2.671, p = 0.011. Observation periods were unequal across sites (Otley 208, Botanic Gardens 136, Tophill 26). The authors state that individuals could not be distinguished and that each visit was counted as an independent data point. Westland Horticulture made the feeders and seed, funded consumables and travel, and helped conceive the research question, with no stated role in data collection, analysis or writing."

Line 8, uncounted:
- `conditions`: "Per-species visit counts are in Table 1 (image, not read)." -> "Per-species visit counts are in Table 1 (image, not read). Overall colour effect for house sparrows F7,399 = 11.139, P < 0.001. Observation periods were unequal across sites (Otley 208, Botanic Gardens 136, Tophill 26). The authors state that individuals could not be distinguished and that each visit was counted as an independent data point. Westland Horticulture made the feeders and seed, funded consumables and travel, and helped conceive the research question, with no stated role in data collection, analysis or writing."

Verdict: 4 of 7 audited records in error (57%), above the 5% bar; lines 1, 2, 4 and 5 fixable with the replacement text above; line 6 held out; lines 3, 7 and 8 MATCH.
