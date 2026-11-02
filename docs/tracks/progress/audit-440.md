# audit-440: desk-d327, evidence lines 6 to 10

Audited 1 November 2026 from the desk-d327 files present untracked in the worktree (docs/views/evidence/desk-d327.jsonl, 10 lines, and docs/tracks/progress/desk-d327.md; neither committed here, neither edited). This audit covers 1-based file lines 6 to 10 only; another auditor has lines 1 to 5. HEAD 6dd1541c equals origin/main. `tools/senses/check.py` on the evidence file: 10 records, 0 problems. Quote lengths (`len(q.split())`), lines 6 to 10: 36, 24, 21, 30, 21, all within 40. Rules applied: /tmp/desk/rules.md (licence, quote, name, duplicate and scientific-context rules), with audits 290, 293 and 295 for Company of Biologists pages and audit-brief format. 7 WebSearch and 15 WebFetch calls (2 refused or blocked: en.wikipedia.org Scarabaeus_satyrus (permission not answered) and wiki.riteme.site (classifier denial); neither retried nor worked around).

Sources opened: journals.biologists.com pages named in the four records' `url` fields (jeb188532 two passes; jeb.087932 two passes; jeb.129122 one pass; jeb.02707 three passes) and cob.silverchair.com/jeb/article/210/5/865/... (two passes, returned by my WebSearch); api.crossref.org/works?filter=doi:... for all four DOIs (one query); core.ac.uk/download/80917247.pdf (Deschodt, Davis and Scholtz, on Escarabaeus). Names also checked in docs/views/gaps/gbif-names.tsv. No library proxy, ResearchGate, academia.edu, Sci-Hub, LibGen or PMC page was opened. WebFetch returns pieces of about 125 characters, so quotes were checked as MATCH/MISMATCH from consecutive verbatim pieces. No paper text is committed beyond single sentences and fragments quoted for verification.

## Licence (all lines)

Audit 295 accepted six JEB copies on cob.silverchair.com that printed only a publisher copyright line, with no licence line and no free or open-access label, on this evidence: the publisher's own page served Methods and Results in full without a login. It followed audits 290 and 293 and was followed by audits 296 to 300 and 368 (368 states that under audits 290 to 295 the d276 Podarcis muralis page "would pass as free full text"). Desk-d276 held that page because it printed no CC sentence; no audit upheld that ground.

What the four pages show (my passes, journals.biologists.com URLs as filed):

| DOI | article-level access label | rights text on the page | full text served without login | Crossref licence |
|---|---|---|---|---|
| 10.1242/jeb.188532 | none (no Open Access, Free, Get access or Purchase) | "© 2019. Published by The Company of Biologists Ltd" and link http://www.biologists.com/user-licence-1-1/ | yes, Methods and Results | user-licence-1-1, am only, start 2018-01-01, delay 0 |
| 10.1242/jeb.087932 | none (PDF and permissions links only) | "© 2013. Published by The Company of Biologists Ltd" | yes, Methods and Results | none |
| 10.1242/jeb.129122 | none | "© 2016. Published by The Company of Biologists Ltd." | yes, Methods and Results | user-licence-1-1, vor, start 2017-02-01, delay 397 |
| 10.1242/jeb.02707 | none ("Sign in" and "Open Access" appear only as site menu items) | "© The Company of Biologists Limited 2007" | yes: Methods, Results, figure legends (one pass truncated mid-Results by the tool, others returned the rest) | none |

Ruling: no page carries a free or open-access label, so free-to-read status cannot be shown by a label. It is shown by the page itself: each publisher page served the full Methods and Results to an anonymous fetch, with no paywall or abstract-only view. That is the publisher's own free full text that rules.md accepts and that audits 290 to 300 accepted on the same evidence. The licence rule is met on all five records; `access` "open" stands. The Crossref am-only entry for jeb.188532 does not matter because the record does not rest on a Crossref licence. The unit's licence statements in the notes match what I found. Licence faults 0.

Owner question 1 (recorded, not decided here): should a Company of Biologists page that serves full text without a login but shows no access label and no licence sentence keep counting as "publisher's own free full text" (audits 290 to 300, 368, and this audit), or should such pages be held as desk-d276 held Podarcis muralis? Desk rows merged after audits 290 to 300 rest on this reading, so a change would reach main too (not counted here).

## Bibliographic

All five match Crossref and the printed page: authors in printed order with correct initials (Foster: James J., John D., Basil el Jundi, Jochen, Lana, Emily, Marcus J., Dan-Eric, Sönke, Marie; Cheney: Karen L., Cait, Eva C., N. Justin; Tedore: Cynthia, Sönke; Oliva: Damián, Violeta, Daniel), titles verbatim, DOIs. Printed lines: "J Exp Biol 15 January 2019; 222 (2): jeb188532" (Crossref issued 2018, printed year wins; as filed); "J Exp Biol (2013) 216 (15): 2967–2973"; "J Exp Biol 1 August 2016; 219 (15): 2396–2401"; "J Exp Biol 1 March 2007; 210 (5): 865–880". Bibliographic faults 0.

## Names and higher taxonomy

- Line 6: the paper prints "Escarabaeus satyrus (Boheman, 1860)". This is not a misspelling. Deschodt, Davis and Scholtz (core.ac.uk PDF) treat Escarabaeus Zídek & Pokorný, 2011 as a genus and place "E. satyrus (Boheman, 1860)" in it. The caller's brief authority gives Scarabaeus satyrus Boheman, so the filed taxon stands, but the unit's "Accepted spelling" and "prints the genus as Escarabaeus" describe a generic placement as a spelling variant. Uncounted wording fix below. Wikipedia's Scarabaeus satyrus page could not be opened (blocked).
- Line 7, 8: Rhinecanthus aculeatus, EXACT ACCEPTED in gbif-names.tsv; Balistidae, Tetraodontiformes as on main (fish-shark rows).
- Line 9: Lyssomanes viridis, EXACT ACCEPTED; Salticidae, Araneae as on main (jumper rows).
- Line 10: the paper prints "adult male Chasmagnathus granulatus Dana 1851" and "(Decapoda: Grapsidae)" in the title; Neohelice granulata is EXACT ACCEPTED in gbif-names.tsv and main files it under Varunidae (sea-invertebrates:161, canon-4, desk-d177, audit 262 naming Chasmagnathus as a synonym). Filed correctly; the conditions disclose the printed name.
- Family, order and class filled "from general taxonomy": rules.md requires accepted names, not printed higher taxa, and main fills family and order from authority files, not from the paper (desk-d276 took them from a USFWS page). All values here equal those on main rows for the same species or genus group. Not a fault; uncounted that the unit did not name the source it used.

## Duplicates

git grep on origin/main across docs/ and views/ (evidence, audit/corrected, audit/ALL.jsonl, sheets, searched, wanted, gaps, tracks) for "satyrus", "Escarabaeus", "Scarabaeus s", "188532", "Rhinecanthus", "triggerfish", "087932", "Lyssomanes", "129122", "Tedore", "Neohelice", "Chasmagnathus", "02707", "Oliva D", "Foster JJ", "looming".

- **Line 9 repeats main.** docs/views/evidence/jumper.jsonl:239 and docs/views/audit/corrected/jumper.jsonl:239 (ALL.jsonl:2196, verdict confirm): Lyssomanes viridis, behaviour_vision, Tedore C and Johnsen S 2016, DOI 10.1242/jeb.129122, value "chose perches by brightness and ambient light; green substrates were not preferred over greys of matched brightness, and leaf shape made no difference", note "They preferred the grey whose photon flux was closest to real leaves." Same species, trait, DOI and finding. The unit's progress note lists other species already on main but missed this one. Counted; unfixable as a new row (the N=15 and the open-copy access could go to main's row as a correction, owner's call).
- Line 7, 8: main holds Rhinecanthus aculeatus colour_vision (Champ et al. 2016, 10.1098/rsos.160399), lambda_max_nm and acuity_cpd from other papers; none from 10.1242/jeb.087932. Not a repeat.
- Line 6: no Scarabaeus satyrus or jeb.188532 row; main's Foster rows (bee, insect:432) are other papers. Not a repeat.
- Line 10: main's Neohelice rows are motion (Oliva and Tomsic 2014, J Neurophysiol, MLG1 neurons), optomotor, acuity and hearing; none from jeb.02707 and none on behavioural escape latency. Not a repeat.

## Per line

### Line 6. Scarabaeus satyrus, polarization: OK (uncounted wording fixes)
Quote MATCH: Abstract sentence returned in three consecutive pieces ("We found that the South African dung beetle Escarabaeus satyrus can orient to polarized light for a range" / " of degrees of polarization similar to that observed in diurnal insects, reaching a lower threshold between 0.04 and 0.32," / " possibly as low as 0.11."). The cut ("similar to that observed in diurnal insects,") is marked and given in the note; it is a comparison, not a qualifier on the value. Value says no more than the quote. Results verbatim: "for DoLP>0.04 beetles were significantly better oriented (DoLP=0.99: W=1745, P=0.001; DoLP=0.32: W=1041.5, P=0.020)" "or showed some indication of improved orientation (DoLP=0.11: W=963, P=0.078)." The note carries the 0.11 non-significance. Sample size: no N in text or legends ("Each point represents relative orientation change for one individual, for one pair of trials"); the unit says so. Wild beetles collected at Stonehenge game farm, tested there 11 to 15 November 2016, kept in sand-filled boxes. Uncounted: the polarized stimulus was artificial ("four UV-emitting 18 W fluorescent bulbs" plus LEDs, through a diffuser and polarizer stack "suspended 12 cm above a 50 cm diameter arena"); the method's "UV-based stimuli" is right but thin, and "field tests under clear skies" could be read as tests against the sky's own polarization. Escarabaeus wording as above.

### Line 7. Rhinecanthus aculeatus, colour_vision: ERROR, fixable (sample composition)
Quote MATCH (two pieces). Value supported; per-colour z and P in the note MATCH. Fault: method says "Experiment 1 used 24 fish". The page: "In total, we tested 24 fish" ... "Eighteen fish learnt the task within 4–5 days" ... "the remaining six fish were omitted from the analysis", and the per-colour results rest on 2 to 5 fish each ("blue: z=2.15, N=4, P=0.03; green: z=5.07, N=5, P<0.001;" "yellow: z=3.63, N=4, P<0.001; orange: z=2.61, N=2, P=0.01; red: z=2.12, N=3, P=0.03"). The analysed n (18) and the 2 to 5 fish per colour are sample composition the row must carry. Also uncounted: fish were "transported back to the research stations or to aquaria at UQ", so "tested at the island research stations" is not established for every experiment; size range "7 to 21 cm standard length"; sex not given on the page.

### Line 8. Rhinecanthus aculeatus, behaviour_vision: ERROR, fixable (design and null results)
Quote MATCH (two pieces). Fault: method lists "four experiments of 24, 16, 8 and 16 fish (which experiment gives the bias was not read)". The bias comes from Experiment 2 (16 fish; "Fish showed a significant preference for the red stimuli in terms of the first model pecked" "(first model pecked: z=3.55, d.f.=93, P<0.001 ...)" "followed by green, yellow and then blue." "Preference for red and green was significantly greater than for blue (z>2.76, d.f.=93, P<0.01);" "however, there was no difference between blue and yellow (z=1.13, d.f.=93, P=0.26).") and Experiment 3 (8 fish, 148 trials; red/green/black pattern chosen over blue/yellow/black, "first model pecked: z=2.90, N=97, P=0.003"; "Luminance was non-significant (z=−1.57, N=97, P=0.12)"). Experiment 1 is the trained grey-distractor test and Experiment 4 (16 fish, blue and yellow only) found nothing: "There was no difference in whether pattern or solid colours were pecked first (z=−0.23, N=135, P=0.82)," "irrespective of pattern (dots, stripes; z=−0.55, N=135, P=0.58) or colour (blue, yellow; z=−0.85, N=135, P=0.40)." The row attributes the bias to 64 fish and omits the Experiment 4 nulls. The note's blue-versus-yellow null is right. No red-or-green-versus-yellow test is reported; "over yellow" rests on the Summary sentence and the rank order (the quote supports the value; the note should say so). Exp. 3 reports N=97 for 148 trials and Exp. 4 N=135 for 128 trials, unexplained on the page.

### Line 9. Lyssomanes viridis, behaviour_vision: ERROR, unfixable (repeats main)
Quote MATCH (two pieces); N=15, "exact multinomial test, N=15, two-tailed P<0.0001"; immatures from sweet gum at Black Creek Greenway (Wake Co.) and Jordan Lake State Recreation Area (Chatham Co.), NC, August 2012. Content right, but jumper:239 on main already files this species, trait, DOI and finding (see Duplicates). Hold out.

### Line 10. Neohelice granulata, behaviour_vision: OK (optional note additions)
Quote MATCH under Results, "Response threshold" ("Because the response started 2.4 s after the stimulus began to move" / ", the animals responded approximately 1 s before the collision."). Fig. 3 legend "N=18, one trial per crab." and Results "Analysis of the data in Fig. 4 (same data set of Fig. 3, N=17)" both confirmed, as the conditions say. The 2.4 s is a rounded mean: "triggered the escape response at a mean (± s.e.m.) of 2.41±0.07 s following the beginning of its expansion"; a repeat at other times of year gave "2.43±0.07 s, N=14". Stimulus: "a 5 cm black square," "which approached over a distance of 70 cm at a constant speed of 20 cm s–1". Exclusions: "On a few occasions, the animals had been walking before the start of image expansion; those trials were not included in the analysis." Summary: response elicited "in all tested animals"; no habituation at 3 min intervals; magnitude varies, timing consistent. Adult males, San Clemente del Tuyú. No omitted null.

## Summary

| line | record | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Scarabaeus satyrus, DoLP threshold 0.04 to 0.32 | OK | (uncounted) conditions, method, note | Quote MATCH with marked cut; 0.11 null in note; N not printed (disclosed); Escarabaeus is a generic placement, not a spelling |
| 7 | Rhinecanthus aculeatus, colour vision | ERROR, fixable | method, conditions | 24 tested but 18 analysed, 6 omitted; 2 to 5 fish per colour |
| 8 | Rhinecanthus aculeatus, red/green bias | ERROR, fixable | method, conditions, note | Bias from Exp. 2 (16 fish) and Exp. 3 (8 fish), not four experiments; Exp. 4 blue/yellow and pattern nulls omitted |
| 9 | Lyssomanes viridis, no green preference | ERROR, unfixable | (drop) | Repeats main jumper:239 (same DOI, trait, finding) |
| 10 | Neohelice granulata, escape at 2.4 s | OK | (optional) note | Quote MATCH; N=18 and N=17 both confirmed; mean 2.41 s |

Errors: 3 of 5 records (60%): scientific context or sample composition 2 (lines 7, 8, fixable), duplicate 1 (line 9, unfixable); licence 0; bibliographic 0; quote-form 0; name 0. Lines 6 and 10 can merge (line 6 after the wording fixes).

## Replacement

All replacements are plain string fields; old strings occur exactly once in the named line.

Line 7:
- `method`: "Experiment 1 used 24 fish" -> "Experiment 1 tested 24 fish, of which 18 learnt the task and were analysed (the remaining six were omitted); each colour rests on 2 to 5 fish (blue N=4, green N=5, yellow N=4, orange N=2, red N=3)"
- `conditions`: "and tested at the island research stations;" -> "and transported to the island research stations or to aquaria at UQ (the page does not tie each experiment to a site); 7 to 21 cm standard length; sex not stated;"

Line 8:
- `method`: "four experiments of 24, 16, 8 and 16 fish (which experiment gives the bias was not read)" -> "Experiment 2 (16 fish, two models of semi-randomly chosen colours per trial, stopped early to record an initial bias): red preferred for first model pecked (z=3.55, d.f.=93, P<0.001), followed by green, yellow and blue; red and green above blue (z>2.76, d.f.=93, P<0.01). Experiment 3 (8 fish, 148 trials): red/green/black pattern chosen over blue/yellow/black (first model pecked z=2.90, N=97, P=0.003); luminance non-significant (P=0.12)"
- `conditions`: "tested at the island research stations" -> "Experiment 2 at Lizard Island Research Station in October 2008"
- `note`: "A response bias in foraging" -> "Experiment 4 (16 fish, blue and yellow models plain, dotted or striped, 128 trials) found no difference for pattern versus solid (z=-0.23, N=135, P=0.82), pattern type (P=0.58) or blue versus yellow (z=-0.85, N=135, P=0.40). The page gives N=97 for 148 trials (Exp. 3) and N=135 for 128 trials (Exp. 4) without explanation. No red-or-green-versus-yellow test is reported; 'over yellow' rests on the Summary sentence and the rank order. A response bias in foraging"

Line 9: drop (repeats main jumper:239). Optionally the owner may correct main's row with N=15 and the publisher's free full text.

Optional (uncounted) fixes:

Line 6:
- `conditions`: "the paper prints the genus as Escarabaeus" -> "the paper prints Escarabaeus satyrus (Boheman, 1860), a generic placement (Escarabaeus Zídek & Pokorný, 2011, used as a genus by Deschodt, Davis and Scholtz), filed here under Scarabaeus satyrus per the desk's name authority"
- `note`: "Accepted spelling is Scarabaeus satyrus." -> "Filed as Scarabaeus satyrus per the desk's name authority; Escarabaeus is a genus name in current use for this species, not a misspelling."
- `method`: "(UV-based stimuli, unpolarized control)" -> "(artificial UV light from fluorescent bulbs and LEDs through a diffuser-and-polarizer stack 12 cm above the arena, the number of diffusers setting the degree of polarization; unpolarized control)"

Line 10:
- `note`: "Walking-device behaviour, not free escape." -> "Results: mean onset 2.41±0.07 s (N=17); repeated at other times of year, 2.43±0.07 s (N=14). Trials in which the crab was already walking before expansion were excluded. Walking-device behaviour, not free escape."

## Owner questions

1. JEB licence (above): keep accepting Company of Biologists pages that serve full text without a login but show no access label and no licence sentence, or hold them as desk-d276 held Podarcis muralis?
2. Line 9: correct main's abstract-graded jumper:239 from the free full text (N=15, second-darkest grey), or leave it?
3. Line 6: the desk's animal name authority places satyrus in Scarabaeus; Deschodt, Davis and Scholtz place it in Escarabaeus. Confirm Scarabaeus satyrus for the app.
