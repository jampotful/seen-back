# desk-d224 progress

Scope: animal sensory-trait records from open full text. Records are in docs/views/evidence/desk-d224.jsonl; check.py reports 0 problems for the unit. journals.plos.org returned RATE_LIMIT_EXCEEDED on every fetch for the whole session (about 12 attempts, spaced), so no PLOS paper could be opened; PeerJ, MDPI, Frontiers and BMC pages opened. nature.com and link.springer.com did not open. Species and DOI were checked against origin/main (whole docs tree) before each paper was opened, and Crossref confirmed authors, volume, issue, article number and licence for every MDPI DOI filed.

## Records (9)
- Frankliniella occidentalis (Insects 11(7): 423), behaviour_vision, three records: blue LEDs most attractive then green with moderate UV; blue-green mixture less attractive than either alone; red least attractive (1%, p < 0.01).
- Danio rerio larvae (Frontiers in Zoology 7(1): 8), acuity_cpd: 0.16 cpd at 5 dpf by optokinetic response (histology limit 0.24 cpd is in conditions).
- Xyleborus affinis and Xyleborus ferrugineus (Insects 13(7): 655), sense_chemical: 70% ethanol gave the strongest EAG responses (one record per species, from a sentence naming both).
- Fopius arisanus (Insects 11(4): 231), sense_chemical: oviposition damage made citrus and peaches more attractive to females in a Y-tube.
- Aedes albopictus (Insects 13(3): 290), sense_chemical, two records: decanoic acid attractive to males at an intermediate concentration; no significant female response.

## Held out
- Harp seal vibrissae (PLoS ONE 8: e0054876), Pacific oyster hearing (PLoS ONE 12: e0185353), snake airborne/groundborne sound (PLoS ONE 18: e0281285), tsetse papers (PLoS NTDs e0007460, e0007510, e0000632, e0000435): not on main by DOI, never opened because of the PLOS rate limit.
- Ringed seal amphibious audiograms (JEB 218(14): 2250): publisher page has no licence and Crossref has no CC licence.
- Flash VEP in diurnal birds of prey (PeerJ 4: e2217) pools four species; UV window marking visibility (PeerJ 2: e621) is a model with blue tit and peafowl cone data, no animals tested.
- Garden warbler compass recalibration (Front. Behav. Neurosci. 10: 29): abstract sentences with the null result are over 125 characters and the stars-visible detail is inconsistent between Methods and Discussion.
- Cataglyphis noda learning walks (Front. Behav. Neurosci. 11: 226): key abstract sentences over 125 characters, value needs two sentences.
- Cataglyphis fortis olfactory landmarks (Front. Zool. 6: 5): page redirects to springer (refused host).
- Dolphin with early hearing loss (Front. Mar. Sci. 12: 1634494): single deaf animal, no licence sentence on the page.
- Thamnophis melanogaster neonates (PeerJ 8: e8718): already in the held-out list.
- Already on main by DOI or species: Leptophobia aripa, Euxesta eluta, Ixodes scapularis and Amblyomma americanum, Culex thermopreference, Vespa and Vespula LED phototaxis (ani14111543), Betta, armadillo, croaking gourami, Papilio polytes.

## Owner questions
- Danio rerio larval acuity: the page prints an Open Access statement naming the Creative Commons Attribution License but the link text was empty and Crossref carries no licence field for 10.1186/1742-9994-7-8. Filed on the page statement alone; hold it out if the audit rule needs a Crossref CC tag.
- Frankliniella occidentalis: the paper prints one blue LED as 567 nm in section 3.2 and 467 nm elsewhere; no blue wavelength is claimed in the records.
- Xyleborus pair: one sentence names both species and each species has its own record; say if a two-species sentence should be filed once as a genus-level record instead.
- Several species rows may fall under the older note that main already holds Frankliniella occidentalis for other traits (lambda_max_nm audit rows); no overlap by paper or trait.

## Desk disposition after audits 312 and 313

Audit 312 (lines 1 to 5): 5 of 5 in error (100%). Audit 313 (lines 6 to 9): 4 of 4 in error (100%). Combined for d224: 9 of 9, all fixable and corrected with the auditors' replacement text; none dropped. Pooled audits 172 to 313: 358 of 762 (47.0%).

Faults: Frankliniella occidentalis x3 (green and UV tied in the six-colour test, so green ranked above UV only in other experiments; the 75% blue mixture exception; mixture replicate counts; ambient fluorescent light; line 3 quote dropped "(Figure 3)" unmarked and now carries it; the blue LED is 467 nm, 567 nm in section 3.2 is a misprint); Danio rerio (cut-off rule misdescribed; 41 against 74 sample sizes; no age effect from 4 to 6 dpf); Xyleborus affinis (no ethanol-versus-bark statistic printed; stimulus amounts); Xyleborus ferrugineus (air-subtraction normalisation and discarded non-responses; an invented extra control removed; colony origin); Fopius arisanus (the mango result, where infested fruit was no more attractive, was missing; an F value had been cited from a different experiment; colony and generations); Aedes albopictus x2 (decanoic acid itself repelled males at the high dose, p = 0.027; the strain and temperature clause; females were caged with males).

Owner questions: licence rulings (both auditors): the Danio rerio record rests on the BMC page statement alone, which is acceptable on the exact copy read; MDPI dc.rights CC BY 3.0 against Crossref CC BY 4.0 acceptable; the two-species Xyleborus sentence stays as one record per species (audits 299 and 300 precedent); Frankliniella has only review rows on main under lambda_max_nm (methods.jsonl:696 to 698), no overlap; names to gbif-names.tsv if absent (Frankliniella occidentalis, Xyleborus affinis and X. ferrugineus, Fopius arisanus, Aedes albopictus, Danio rerio larval acuity is a new paper on a species already on main for adult acuity); the Fopius mango null is carried in conditions, not as its own record.
