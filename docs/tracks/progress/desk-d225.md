# desk-d225 progress

Scope: animal sensory-trait records from open full text (plant screening superseded). Records are in docs/views/evidence/desk-d225.jsonl; check.py reports 0 problems for the unit. About 38 WebSearches. Every species and DOI was grepped on origin/main (whole docs tree, including audit/corrected, searched, sheets, progress notes) before a paper was opened.

Host access this session: peerj.com search results opened but main already holds nearly every PeerJ paper the searches surfaced; journals.plos.org opened on roughly every second request (rate limit otherwise); nature.com opened intermittently (client error on several articles, no retry); api.crossref.org worked for single-DOI lookups about every second request.

## Records (9)
- Puffinus puffinus (Procellariidae), Sci Rep 11: 18941, behaviour_vision: fewer flying Manx shearwaters over a colony in light-on periods, stronger under green and blue than red. Conditions carry the unmatched intensities (1.4 to 32 W), the 1.4 W / 3.3 W inconsistency for dimmed white, randomised order, null red and 1 minute results.
- Microtus ochrogaster (Cricetidae), PLOS ONE 21(2): e0335120, sense_hearing: ABR range 1 to 46 kHz (tested range), peak 8 to 24 kHz wild-caught and 8 to 32 kHz laboratory-reared; anaesthesia, no chamber or noise reported.
- Odontotermes formosanus (Termitidae), PLoS ONE 9(3): e90906, sense_chemical: trail-following threshold 1 fg/cm for both components in activated workers; sample sizes per concentration not visible.
- Apis mellifera (Apidae), Sci Rep 10: 7872, behaviour_vision: 36% of bees left blue arms early against under 10% UV and 23% green; intensities not matched, UV dimmest.
- Vespa velutina (Vespidae), Sci Rep 7: 12956, sense_chemical: male EAG minimum doses 100 ng 4-OOA and 10 ng 4-ODA.
- Hippodamia variegata (Coccinellidae), PLOS ONE 20(6): e0327160, sense_chemical: 4 of 28 volatiles attractive in a Y-tube; dose series and EAG in conditions.
- Passer domesticus (Passeridae), PLOS ONE 11(12): e0167905, sense_chemical: captive third-generation males, not females, preferred hay over mouse-urine nest-box odour (marginal P = 0.047, interaction not significant).
- Rana dalmatina (Ranidae), PLOS ONE 19(5): e0302728, sense_chemical: odonate-cue conditioning changed mitral-cell properties; text/values inconsistency on membrane resistance in conditions.
- Culex pipiens (Culicidae), PLOS ONE 14(6): e0217484, lambda_max_nm 335 nm UV peak (second peak 540 nm in conditions). Crossref lookup failed twice; DOI from the page.

## Held out
- Petaurus breviceps colour vision (Sci Rep 15: 7585): Crossref deposits CC BY-NC-ND 4.0; pet-bred animals, n = 4.
- Zebra finch / Bengalese finch nest odour (PLOS ONE 7: e36615): abstract pools the zebra finch with the domesticated Bengalese finch and results are statistics clauses.
- Octopus vulgaris neighbour recognition (PLOS ONE 6: e18710): recognition proxy, no sense-specific sentence.
- Costelytra zealandica larval olfactometer (PeerJ 3: e1454): reader returned only paraphrase; population-level result.
- Orbicella faveolata soundscape settlement (PeerJ 4: e2557): sites differ in habitat as well as sound; abstract sentence is over 40 words and trait fit is unclear.
- Stomoxys red traps (Sci Rep 14: 17724): genus-level, several species pooled.
- Eigenmannia electrolocation tracking (Sci Rep 8: 5830): method paper.
- Nephila pilipes night light (PeerJ 5: e4070): prey interception, not a spider sensory trait.
- Bottlenose dolphin biosonar sensation levels (PLOS ONE 6: e29793), Aedes aegypti visual threats (Sci Rep 12: 25461), Aedes CO2 wind tunnel (Sci Rep 15: 13427), Bombus terrestris heat waves (Sci Rep 16: 53492), EMF bottom-dwelling species (Sci Rep 10: 60793): page refused or rate limited; open leads for a unit with access. Not on main by DOI.
- Species-checked as already on main: Pachyptila prions, Leptophobia aripa, Electrogena, Sirex, Serrasalmidae, Trichopsis, Betta, Dastarcus, krill and Calanus (d176), Latimeria (anatomy only).

## Owner questions
- Family names Termitidae/Blattodea (Odontotermes), Ranidae/Anura (Rana dalmatina), Culicidae (Culex) and Petauridae are not printed on the pages; I used standard taxonomy and main's family usage where it exists.
- Does a wild-derived, outbred laboratory colony (Microtus ochrogaster) and a third-generation captive house sparrow count as non-domestic? I filed both with the origin in conditions.
- Pet-bred sugar gliders: held out on licence, but would a pet-trade origin also count as domestic?

## Advice
Main is saturated for PeerJ and for heavily searched Sci Rep topics. The most productive route was a PLOS ONE or Sci Rep search on a species-and-sense phrase, then a single-DOI Crossref lookup; the page-summary tool returns abstract sentences in segments that can be rejoined only where consecutive.

## Desk disposition after audits 314 and 315

Audit 314 (lines 1-5): lines 1, 2, 4 in error, line 3 match, line 5 (Vespa velutina, nature.com page unopenable by the auditor) held out and dropped. Audit 315 (lines 6-9): all four in error, all fixable. Replacement text applied to lines 1-4 and 6-9; 8 records merged, 0 errors remaining by check.py. Audit 315 could not reach Crossref for the Passer domesticus DOI (page citation and licence verified instead); Rana dalmatina S1-S3 table values were not opened. Several P values in the Hippodamia and Passer conditions were read from tool summaries and should be confirmed against the pages if the records are ever re-audited. Owner answers: wild-derived laboratory colony of Microtus ochrogaster and managed Apis mellifera colonies are accepted as non-domestic; Passer domesticus third-generation captive-bred is accepted with origin stated. Vespa velutina retry only if the nature.com page opens.
