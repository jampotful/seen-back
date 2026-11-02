# desk-d203: animal sensory-trait records (task replaced plant screening)

Records filed: 8 in docs/views/evidence/desk-d203.jsonl, all abstract-only (partial true), all MDPI Insects, licence visible on the article page, DOI and author order checked on Crossref.
- Asiophrida xanthospilota (Insects 15(7): 532): spectral_range_nm (ERG responded to red, yellow, green, blue, UV; no nm values), polarization (microvilli orientation, unlikely polarization-sensitive).
- Eucryptorrhynchus scrobiculatus and E. brandti (Insects 14(8): 699): eye_type (apposition, about 550 ommatidia per eye, stated for both together) and interommatidial_deg (7.08 and 4.84 degrees, one record each from one "respectively" sentence).
- Cacopsylla chinensis (Insects 17(3): 287): eye_type (apposition, no clear zone), polarization (rhabdom microvilli in two orthogonal directions; anatomy only).

Main was grepped by species and DOI (docs/views incl. audit/corrected and audit/ALL) before filing; the three papers appear only in searched/wanted files, no evidence rows.

## Queries (WebSearch, 36 of 40 used)
Open-ended trait searches (hearing/ABR, electroreception, flicker fusion, infrared, spectral sensitivity, magnetoreception, acuity, vibration, fovea), then allowed_domains searches on peerj.com, journals.plos.org, mdpi.com and frontiersin.org for hearing, electroreception, ERG spectral sensitivity, compound-eye ultrastructure; species searches for Alligator mississippiensis, Halyomorpha halys / Pyrrhocoris / Oncopeltus, Bufo bufo / Anaxyrus / Lithobates; "peerj 2219 Sitophilus zeamais".

## Held out (with reason)
- Dasypus novemcinctus ABR (PeerJ 16602), Solea/Scophthalmus/Dicentrarchus/Scyliorhinus/Raja electric thresholds (Frontiers 1286149), Slipper lobsters (Frontiers 807347), Electrogena lateralis, Tripterygion delaisi, Artibeus spp. acuity, Euperipatoides rowelli, Betta splendens, Trichopsis vittata, Arctocephalus forsteri, Sebastes-type fish: already on main.
- Empoasca onukii acuity (Insects 14(4): 370; 0.28 and 0.14 cpd) and Sebastes schlegelii hearing (Frontiers 1257473; 200 Hz best, 86.4 dB): the value sentences are over 125 characters and WebFetch returned them only as unquoted text, so no verbatim quote could be confirmed. Retry only with a tool that returns whole long sentences.
- Histia flabellicornis (Insects 16(8): 771): every abstract sentence over 125 characters, none readable.
- Empoasca onukii foliage intensity (Insects 11(7): 426): key sentences over limit.
- Kryptopterus vitreolus magnetic avoidance above 20 uT (PLOS ONE 16(3): e0248141, CC BY): the sentence is 130 characters; the readable sentences carry no field value.
- Sitophilus zeamais (PeerJ 4:e2219, CC BY; Arnold et al., author list incomplete on page): results sentence readable, but the paper has many stimuli with mixed and Bonferroni-null outcomes; a single-sentence record would drop nulls. Needs full author list from Crossref (rate-limited here) and a multi-record design.
- Heliconius acuity (0.49 cpd): bioRxiv version is a preprint; published Biology Letters 19(12): 20230476 page shows no licence and no species names in the abstract.
- Halyomorpha halys ERG (J Pest Sci 2024): Springer, not readable here; Hyla chrysoscelis ABR (JCP A 2014): only a dissertation copy reachable.
- Lizard visual ecology review (Frontiers Amphibian Reptile Sci 2: 1426675, CC BY): values for Tiliqua rugosa and Ctenophorus acuity are in sentences over 125 characters; short sentences name no single species.
- Alpaca RGC acuity (12.5 to 13.4 cpd): master's thesis.
- Masked ABR (JARO 2018): methods paper, licence not stated.

## Owner questions
1. Several lead papers cannot be quoted because WebFetch cuts sentences over 125 characters; can the desk have a text route for open papers (the oa job) for Empoasca onukii (Insects 14(4): 370) and Sebastes schlegelii (Frontiers 1257473)?
2. spectral_range_nm with a string value for ERG responses that give no nm figures (Asiophrida): acceptable, or should such rows go under another trait?

## Desk disposition after audit 287

Audit 287: 1 of 8 records in error (12.5%), unfixable. Pooled audits 172 to 287: 265 of 622 (42.6%). Line 1 (Asiophrida xanthospilota ERG under spectral_range_nm) was dropped: main desk-d192:1 and :2 already carry the same paper's ERG finding under colour_vision, and the paper gives no wavelengths for the ERG lights. The unit's note that main had no rows from these papers was a missed grep. Seven records merged with the auditor's suggested conditions, method, value and note texts (ommatidia counts per sex, the Table 2 female-adult caveat, the polarization inference basis, licence version mismatch). Main's d192:1 note was not touched.

Owner questions: whether the abstract ERG sentence ("all five lights, including yellow and UV") should be appended to d192:1's note; MDPI licence version mismatch (page 3.0, Crossref 4.0); a text route for open-access sentences over 125 characters (Empoasca onukii Insects 14(4):370, Sebastes schlegelii Frontiers 1257473).
