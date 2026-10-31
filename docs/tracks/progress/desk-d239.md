# desk-d239

Evidence-only unit (sense_hearing, sense_electric, acuity_cpd). 4 records in docs/views/evidence/desk-d239.jsonl; check.py reports 0 problems. About 38 WebSearches.

## Records
1. Mecopoda elongata, sense_hearing: travelling-wave velocity 4 to 12 m/s over 6 to 48 kHz (Udayashankar, Kossl, Nowotny 2012, PLoS ONE 7(2) e31008, 10.1371/journal.pone.0031008). Lab-bred colony (Frankfurt); species named only in Methods. Held lead from d238 retried.
2. Mormyrus rume (paper: subspecies proboscirostris), sense_electric: echo-response latency 19 to 25 ms to all playbacks (Worm, Kirschbaum, von der Emde 2017, PLoS ONE 12(9) e0184622). Captive-bred, n = 8, seven playbacks in random order; nulls in conditions.
3. Dascyllus aruanus, acuity_cpd 2.65 (Tosetto, Hart, Ryan 2024, PeerJ 12 e18152, 10.7717/peerj.18152). Anatomical, 3 retinas, all neural cells counted together; behavioural 1.1 cpd is an assumed ratio and not logged. Quote in two pieces.
4. Culex pipiens (pipiens form), sense_hearing: Johnston's organ thresholds 30 to 53 dB SPVL, mean 39.8 +/- 4.8 (n = 96 units) (Lapshin, Vorontsov 2023, Insects 14(9) 743, 10.3390/insects14090743). Wild-caught females. Quote in two pieces.

## Held leads and why
- Siganus guttatus hearing (10.3390/ani14202967): already on main (desk-d193). My first DOI grep used head -2 and missed it; later checks used full-DOI grep across main and branches.
- Exorista japonica broadband photoreceptors (pone.0160441, primary paper; main holds only review-sourced values): PLOS fetch rate-limited five times. Retry.
- Alouatta caraya ganglion cells (pone.0115291): PLOS rate-limited. Main has other Alouatta caraya acuity (figshare source).
- Salmo salar infrasound (pone.0063696): fish from a production cage (farmed stock), 12 vs 12.5 Hz conflict between abstract and Methods. Held.
- Acheta domesticus cercal hairs (insects3041028): colony origin unstated, domesticated species, hair mechanics not a clean sense value. Held.
- Honeybee antennal-lobe airflow (fphys.2021.790453): bee source unstated; null sentence has no antecedent in the quote; tone level not given. Held.
- Scaphoideus titanus vibrational masking (pone.0032954): pest-management mating result, a 2014 correction exists. Held.
- Elasmobranch ampullae counts (pone.0016008): one specimen per species, morphology only. Held.
- Already on main or d22x/d23x: 17962, 14230, 18491, 16602, 0221659, 0062995, 0192865, 0037627, 1257473, conservation6030099, pone.0086531 and others.
- Not sensory measurements: Parribacus (d186 on main), Scylla light spectrum, Schizocosa air-particle signals, tadpole perspective, FADAR grouper detector, PeerJ 3595 (single-author analysis of published ERG data).

## Owner questions
1. Mormyrus: filed under species Mormyrus rume (OBIS accepted) although the paper studied M. r. proboscirostris; say if you want the subspecies noted differently.
2. Culex pipiens: main files Culex pipiens pipiens under acuity_cpd and Culex pipiens under lambda_max; this row uses Culex pipiens.
3. Mecopoda quote says "the bushcricket"; the species comes from Methods. Accept?
