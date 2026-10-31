# desk-d207 progress

Task: 5 to 10 new animal sensory-trait records from open papers, aimed at groups thin on main. Plant screening in the shared unit brief is superseded.

## Coverage grep (before filing)
Grepped docs/views (evidence, audit/corrected, audit/ALL, searched, wanted, gaps) by genus and by paper title, DOI or author. No rows on main for: Esox (only a try-species and no-view listing), Milnesium and tardigrades, Hippocampus, Syngnathus, Boleophthalmus, Periophthalmus, Aspidoscelis inornata, Chrysoperla carnea Kral and Stelzl (only a wanted line, sweep-49), Myrmeleon bore. Already on main, so skipped: Notamacropus/Macropus eugenii (Ebeling, wallaby dichromacy), Meriones/Rocha 2016 (PLOS ONE 0147318), Scutigera coleoptrata (Meyer-Rochow 2006) and Scolopendra mutilans (PNAS 2023), pit viper thermography (jeb.244478), Chelonia mydas colour vision.

## Records filed: 6 (docs/views/evidence/desk-d207.jsonl)
- Chrysoperla carnea, absolute_sensitivity (daily ERG change, no spectral change). Kral and Stelzl 1998, Eur J Entomol 95(3): 327-333. Page prints CC BY 4.0. No DOI exists on the page or in Crossref, so a url is used.
- Milnesium tardigradum, sense_light_nonvisual (null: infrared vs visible light, mobility). Shcherbakov et al. 2010, Contrib Zool 79(1): 33-38, DOI 10.1163/18759866-07901002 (Crossref CC BY-NC 4.0; repository page CC-BY 4.0).
- Aspidoscelis inornata, eye_movement (36 gaze shifts per min, field). Irwin 2024, Front Psychol 15: 1424329, CC BY.
- Esox masquinongy, behaviour_vision (blinded fish do not stalk) and sense_airflow (lateral-line-suppressed fish alter approach). New, Fewkes, Khan 2001, J Exp Biol 204(6): 1207-1221. Abstract only (ScienceOpen), partial true, access abstract.
- Myrmeleon bore, sense_vibration (heat-stress survivors more responsive). Miler and Czarnoleski, Curr Zool 68(3): 345-350 (Crossref issued 2021-12-09), DOI 10.1093/cz/zoab098, read from the PMC PDF mirror which prints CC BY-NC.

## Queries (WebSearch, about 38)
Seahorse visual acuity; pipefish vision/hearing; pike Esox sensory; tardigrade/ctenophore/bryozoan photoreception; katydid hearing; harvestman/scorpion eyes; Neuroptera vision/hearing; centipede/millipede eyes; peerj orthopteran; mdpi snake infrared; frontiers turtle; plos amphibian; goby/mudskipper (twice); Characiformes sensory; stonefly/caddisfly/mayfly; rodent/marsupial vision; bird hearing ABR; frog audiogram; gecko/anole sensory; scorpion UV; Opiliones; Hippocampus feeding; mdpi locust; lacewing/antlion; caddisfly light; rodent acuity (twice); snake chemosensory; Hypsibius/Milnesium; ctenophore Mnemiopsis; Esox predator; Syngnathus mate choice; Contributions to Zoology; Eur J Entomol; centipede open access; turtle open access; muskellunge; antlion vibration.

## Held out (reason)
- Hippocampus abdominalis/taeniopterus visual resolution (Vis Neurosci 28(4)) and seahorse spectral sensitivities (Vis Neurosci, Cambridge): Cambridge PDF URL refused (too long), landing page blocked, no open licence seen.
- Elacatinus lori larval sensory development (Sci Rep 11, 10.1038/s41598-021-91640-2): nature.com request was blocked (no permission answer, not retried); FIU repository page and DOAJ give only an abstract summary with no licence line.
- Pipefish sound production (PeerJ 1471), Pomatoschistus courtship sounds (PLOS ONE 0064620): sound production, not a sensory trait.
- Mudskipper cornea/COL8A2 (Front Ecol Evol 10: 871370) and mudskipper genome review (Animals 8(2): 24): gene or morphology, no stated sensory value in short sentences.
- Marsupial vision genes (Front Ecol Evol 10: 982073): gene evolution only.
- Mecopoda elongata tympanal motion (J Exp Biol 214: 3596): fetch returned no bibliographic data or licence; summariser gave only paraphrase.
- Bushcrickets position-dependent hearing (PMC4632538), BMC Frontiers in Zoology papers (s12983-021-00442-9, s12983-016-0182-9): PMC and Springer refused.
- Phalangium opilio vestigial eyes (Curr Biol 2024): licence not stated on the copy read.
- Mnemiopsis leidyi motility (Mar Biol J 2022, 10.21072/mbj.2022.07.4.01): licence not stated; the light-related result is only that large animals stayed in the lit area, in a long sentence.
- Dendrobaena, Echinotriton and other d205 items: not touched.
- Lizard visual ecology review (Front Amphib Reptile Sci 2: 1426675): review, licence line not shown.
- Irwin 2024 other species (frilled lizard 2.6 shifts/min, birds): the sentences do not name the species or give pooled values, so held.
- Kral and Stelzl second finding (about 1 log unit more sensitive at midnight than at noon): sentence read through fragments with a hyphenation uncertainty ("bluegreen-green"); not filed.

## Owner questions
1. Aspidoscelis inornata, Milnesium tardigradum, Esox masquinongy and Myrmeleon bore are not in gbif-names.tsv; names are as the papers give them (accepted names to be confirmed).
2. Kral and Stelzl 1998 has no DOI; the record uses the journal url. Confirm that is acceptable.
3. Esox masquinongy rows are abstract-only (partial true) from a journal without an open licence; confirm whether abstract-only rows are wanted for an otherwise empty genus.
4. Milnesium tardigradum licence differs between sources (repository CC-BY 4.0, Crossref CC BY-NC 4.0); both are open.
5. Irwin's gaze-shift counts are zoo and field observations, not a controlled sensory test; confirm eye_movement is the right key.
