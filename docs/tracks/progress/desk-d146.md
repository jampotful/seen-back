# desk-d146 progress (animal vein: thin sense_* cells in taxa not yet covered)

Scope: sense_hearing and sense_vibration. Main (evidence, audit/corrected, ALL, searched, wanted) was grepped by species, DOI and first author before filing; none of the five taxa below had a sense_* line. No search records and no wanted lines (the vein is sense traits, not harvest genera).

Records: 6 in docs/views/evidence/desk-d146.jsonl, all grade m, one named species each, all read from open full texts (Results and Discussion), so no "partial" flags. Authors, volume and issue taken from Crossref via WebFetch for every DOI; GBIF species match gave ACCEPTED for all five species (Catalog of Fishes not needed, no fish).
- Cicadatra atra sense_hearing (Windmill, Sueur and Robert 2009, J Exp Biol 212(24):4079, 10.1242/jeb.033019): tympanal-ridge motion peak 9.4 kHz in the one individual shown; eight females, 66 dB SPL sweep; no neural recording and no best frequency across animals.
- Nomophila nearctica sense_hearing (Nakano and Mason 2018, PLOS ONE 13(8):e0202679, 10.1371/journal.pone.0202679, CC BY): significantly fewer escape responses at 40 and 50 dB SPL than at 100 dB SPL (pooled rates in the note). Behavioural, tethered moths tested repeatedly, 30 kHz only, no sample size per level in the Results (96 moths in Methods).
- Dryophytes chrysoscelis sense_hearing (Schrode et al. 2014, J Comp Physiol A 200(3):221, 10.1007/s00359-014-0880-8, PMC author manuscript): ABR regions of best sensitivity near 1.2 and 2.6 kHz; 61 to 63 dB in the lower region; 35 frogs; ABR thresholds 15 to 25 dB above midbrain thresholds; no sex or size effect. The paper says Hyla chrysoscelis; filed under the accepted name.
- Pagurus bernhardus sense_vibration x2 (Roberts et al. 2016, J Exp Mar Biol Ecol 474:185, 10.1016/j.jembe.2015.09.014; accepted manuscript on the Hull repository): antenna movement 0.11 to 0.29 m/s2 RMS (n=35, most sensitive 90 Hz); locomotion 0.09 to 0.44 (n=10, 40 Hz and 210 Hz). Ranges of averages across seven frequencies; water-borne particle motion not excluded; crabs held for weeks were less sensitive.
- Copiphora gorgonensis sense_hearing (Jonsson et al. 2016, J R Soc Interface 13(122):20160560, 10.1098/rsif.2016.0560, PMC copy): tympanal best response 23.63 kHz plus or minus 4.06, 42 membranes of 21 animals; mechanical, no threshold; sex difference p = 0.055.

Quote method: each quote is a whole sentence of at most 40 words, reassembled from consecutive 125-character pieces and confirmed on a second fetch with a differently worded prompt. The first draft Nomophila quote (48 words) was replaced by the 22-word sentence on 40 and 50 dB SPL so that no cut was needed; the value says no more than that sentence.

Held-out leads:
- Penna et al. 2024, S Afr J Herpetol 30(1):20, 10.2994/SAJH-D-21-00029.1 (Discoglossus pictus, D. galganoi, multi-unit torus recordings, minimum thresholds about 40 dB SPL below 0.5 kHz and about 50 dB near 1.6 kHz): UCM repository record has no file and the BioOne and DOI pages were blocked; abstract only through the repository record, no per-species figure.
- Beatini, Proudfoot and Gall 2018, J Comp Physiol A 204(2):145, 10.1007/s00359-017-1216-2 (Aegolius acadicus ABR, range about 0.7 to 8.6 kHz, best 1.6 to 7.1 kHz): Springer paywalled.
- Sueur, Windmill and Robert 2010, JASA 127(3):1681, 10.1121/1.3291036 (Cicada orni, Cicadatra atra, Lyristes plebejus tympanal tuning): no full text reachable (AIP page blocked); abstract has no frequencies.
- Fukomys magnetoreception ("Eyes are essential for magnetoreception in a mammal"): only the bioRxiv preprint and a PMC page (PMC7536053) behind a reCAPTCHA page; published version not read, so not filed.
- Cui et al. 2017, PLoS ONE 12(1):e0169449, 10.1371/journal.pone.0169449 (Babina daunchina ABR under anaesthesia): group thresholds only in a figure; text gives one frog.
- Maekawa et al. 2011, Parasit Vectors 4:10, 10.1186/1756-3305-4-10 (Anopheles stephensi, heated Peltier at one temperature, 35 C): single temperature with CO2, no threshold; not filed under sense_thermal.
- eLife 77628 (Ancylecha fenestrata katydid pinnae): page blocked by a permission request. Tick thermal (PMC6707551) and Aedes thermal are already on main.
- sense_taste still has no trait key in check.py.

Blocked or refused: elifesciences.org/articles/77628, doi.org/10.2994/SAJH-D-21-00029.1, pubs.aip.org (permission requests unanswered); PMC returned a reCAPTCHA page on some fetches (PMC7536053, PMC2644656). No workaround attempted.
