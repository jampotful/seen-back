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
