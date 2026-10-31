# desk-d232

Sonnet 5.5 desk unit, gap-first method. Four records in docs/views/evidence/desk-d232.jsonl (check.py: 0 problems for this file). About 35 WebSearches. Every species and DOI was grepped across docs/ and the evidence files before opening. Crossref list queries through the page tool returned the same unrelated list for every query (broken), but single-DOI lookups (api.crossref.org/works/<doi>) worked and were used to confirm title, volume, issue, licence and author order. curl to Crossref was refused (403) and not retried.

## Records

1. Tyto alba, sense_hearing (Krumm et al. 2019, PLoS ONE 14(8) e0220652, 10.1371/journal.pone.0220652): single-reference minimum audible angle 4.9 +/- 0.3 deg for broadband noise (Results sentence, whole). Three owls, hand-reared, d' = 1 criterion, 40 dB SPL with roving. The Abstract (14 deg at 500 Hz to 6 deg at 8000 Hz, about 4 deg broadband) disagrees with the single-reference Results (13.7 and 8.4 deg), and the Discussion gives another 8000 Hz figure; noted in conditions. Family and order from the US Fish and Wildlife Service taxonomic tree page (paper prints genus and species only). Crossref CC BY 4.0 vor.
2. Falco tinnunculus, fovea (Cobo et al. 2026, Biology 15(12) 949, 10.3390/biology15120949): central fovea 217.66 um deep, temporal 106.38 um (Abstract sentence, whole). Single representative values from one eye of two euthanised wild-centre males, no shrinkage correction. Page metadata says Segovia first; byline and Crossref say Cobo first. Crossref CC BY 4.0 vor.
3. Tipula autumnalis, sense_chemical (Buda et al., printed 2025, Insects 16(1) 24, 10.3390/insects16010024): nine EAG-active cuticular hydrocarbons by GC-EAD (Abstract sentence, whole). Results fragment says nine from male washes and six from female washes, so the Abstract nine is one wash type; 11 male and 12 female antennae. Third author spelling differs between page and Crossref; page used. Crossref CC BY 4.0 vor.
4. Rosalia batesi, sense_chemical (Kiriyama et al. 2018, Insects 9(2) 48, 10.3390/insects9020048): olfactometer, females attracted to male odour, other three pairings no bias. Counts (42 of 50, chi2 = 31.39) sit in a long sentence and are labelled as read from it. Behavioural, not antennal.

## Held leads and why

- Libellula pulchella / Leucorrhinia intacta artificial-prey attacks (pone.0179483): species-by-prey-size interaction not significant (z = 1.539, P = 0.1238), key sentences over the tool limit, Pachydiplax pooled in the community experiment. Absent from main by DOI.
- Harmonia axyridis light intensity (insects16121280): DOI already appears in docs/views/recheck files; the paper has an internally inconsistent predation statistic (F = 4.956, p = 0.859) and no dark control. Not filed.
- Lacerta agilis UV-blocked males (pone.0019360): sunscreen as UV block, non-random assignment, treatment-group sizes printed in opposite orders, the treatment effect in the logistic model "fell just short of significant", and the key sentences exceed the tool limit.
- Habronattus pyrrithrix colour neophobia (pone.0254865): null result, but every statistic sits in a sentence over the tool limit (one at 127 characters); 52 of 128 spiders did not attack.
- Papilio demoleus colour selection (insects14030249): colour count inconsistent (eight listed, seven in results), numeric sentences long.
- Choristoneura fumiferana single-sensillum paper (insects14070653): numeric responses only in long sentences.
- Pacific oyster light (pone.0140149): Table 1 counts not in text; no numeric Abstract or Results sentence; held.
- Newt UV (pone.0030391): key sentences are fragments, text contradicts itself on UV peaks and male numbers.
- White-tailed deer vehicle flight distance (pone.0109988): CC0, but flight distance to a high-beam truck is a behavioural response with no sensory isolation; not filed.
- Common-name searches for mallard, toad, bullfrog, alligator, cottontail, turtles, garter snake, raptors, bumblebees, jumping spiders and fish hearing returned only papers already on main, or non-sensory papers.
- Not retried (no new information): walleye, Amalosia (Frontiers page not searched again), Gelasimus, Mooney murre, Vespa velutina (nature.com page refused), others in the brief's long list.

## Owner questions

1. Is a categorical olfactometer value with the counts in an over-limit sentence (record 4) acceptable, or should such records be dropped?
2. Record 1 chooses the single-reference Results sentence over the Abstract because the Abstract disagrees with the Results; an auditor may prefer the Abstract.
