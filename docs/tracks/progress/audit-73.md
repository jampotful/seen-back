# Audit 73: harvest-56 (branch research/harvest-56, commit b403a772)

Gate: `screen_candidates.py --check` on the 35 records and 20 wanted lines prints "0 problems".

## Sample (seed 73, 20 of 35 lines)

Line numbers (1-based): 1, 3, 4, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 23, 29, 31, 32, 33.

## Method

For every sampled record I ran `harvest_get.py` for the genus and compared `queries` with the harvest's query and family-review lines (all 20 match word for word, then two "web: " searches each), checked every `screened` id against the harvest output (W2225398011 and W1565762554 come only from `screen_candidates.py`, as the earlier audits found), read `chased`, and compared `canon` with docs/views/research/canon.jsonl by trait and taxon. Main's rows were searched in docs/views/audit/corrected and docs/views/evidence (the two stores rows.py reads) under Stomoxys, Lessonia, Mesembrinibis, Harpiprion, Macronectes, Phaetusa, Sterna simplex, Acanthagenys, Anthochaera, Conopophila, Ardeotis, Choriotis, Elaenia, Campylopterus, Nesoptilotis, Lichenostomus, Athetis, Proxenus, Hydrilla, Ostrinia, Enyo; gbif-names.tsv and taxonomy-extra.tsv were read for the splits. I used about 48 WebSearches and 25 fetches of URLs my searches returned. No library proxy, ResearchGate or academia.edu page was opened. One result (a springerlink.bibliotecabuap.elogim.com mirror, returned for the Ardeotis acuity search) was left unopened.

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Stomoxys cff_hz; corner_hz | ok. Own searches (flicker fusion, photoreceptor recording, ERG, spectral sensitivity) found no stable fly value. Dodt 1951 and 1954 are human and vertebrate; Hardie 1979 is Calliphora and Musca; an arXiv paper on biting-fly vision (2605.17049) covers Aedes, tabanids and tsetse, not Stomoxys. Four canon entries named; canon also lists Invertebrate vision (Warrant and Nilsson 2006, Insecta) and Visual ecology (Cronin et al. 2014) for these traits and the record leaves them out (a lead, not an error: point 8). |
| 3 | Lessonia acuity_cpd; interreceptor_deg | ok. Kelp confusion handled; the animal is Lessonia rufa. Own searches found no negrito retina or acuity paper. Both screened works plainly hold no acuity measurement (SWS1 survey; vulture retinas). |
| 4 | Lessonia binocular_deg; fov_h_deg | ok. No negrito visual field found (results were species pages and the Durban symposium page on bird visual fields). Four canon compilations named. |
| 6 | Lessonia lambda_max_nm; spectral_range_nm | ok. Twelve canon compilations named, matching the canon file for birds. Odeen and Hastad 2003 (MBE 20:855) was sampled by a fetch summary, which names Myiarchus tyrannulus and Manacus manacus as its tyrannids and no Lessonia. |
| 7 | Mesembrinibis acuity_cpd; interreceptor_deg | ok. Own searches found no green ibis eye paper. The 1999 Condor paper is Eudocimus and Rynchops; Martin and Portugal 2011 is on the wanted list. |
| 8 | Mesembrinibis cff_hz | ok. No ibis flicker value found. |
| 9 | Mesembrinibis lambda_max_nm; spectral_range_nm | ok. Twelve canon compilations named. No ibis pigment found. |
| 10 | Macronectes acuity_cpd; interreceptor_deg | ok. Mitkus et al. 2016 (jeb140905) studies Leach's storm petrel and northern fulmar and mentions the southern giant petrel only for a fovea reported by O'Day 1940; it is a different genus pair, as the record implies. |
| 13 | Phaetusa binocular_deg; fov_h_deg | ok. Lucas et al. 2024 (Sci Nat) studied Anous, Gygis, Onychoprion, Larosterna, Ardenna and Puffinus, no Phaetusa. Its canon entry and Cantlay et al. 2024 are named in `screened`, and the `canon` list itself omits both (a lead, not an error). |
| 14 | Phaetusa cff_hz | ok. No tern flicker value found. |
| 15 | Acanthagenys acuity_cpd; interreceptor_deg | ok. No honeyeater retina or acuity paper found. Main's Anthochaera carunculata acuity row (Caves et al.) is another genus, not synonymous. |
| 16 | Acanthagenys binocular_deg; fov_h_deg | ok. No honeyeater visual field found. |
| 17 | Acanthagenys cff_hz | ok. No honeyeater flicker value found. |
| 18 | Ardeotis acuity_cpd; interreceptor_deg | ok. Main's two Ardeotis kori rows (binocular, fov_h) are for other traits. My searches found no bustard acuity paper. |
| 19 | Ardeotis cff_hz | ok. No bustard flicker value found. |
| 23 | Elaenia lambda_max_nm; spectral_range_nm | ok. The two identifiers are identified below. Neither bears on lambda_max_nm or spectral_range_nm. |
| 29 | Campylopterus cff_hz | ok. Own searches found only the Anna's hummingbird paper. Haarlem et al. 2026 named. |
| 31 | Nesoptilotis binocular_deg; fov_h_deg | ok. Main holds Lichenostomus flavescens (now Ptilotula flavescens, SWS1 only) and Conopophila rufogularis (SWS1 only); neither is Nesoptilotis or a field row. |
| 32 | Nesoptilotis cff_hz | ok. No honeyeater flicker value found. |
| 33 | Athetis cff_hz; corner_hz | ok. Bernhard and Ottoson 1960 and 1964 (Cerapteryx) are dark-adaptation, not flicker. Main holds no Athetis, Proxenus or Hydrilla row. |

Sample: 0 errors in 20. No extension needed.

## Specific tests set in the launch prompt

- Genus splits. Nesoptilotis (Lichenostomus), Acanthagenys, Phaetusa, Mesembrinibis, Lessonia and Campylopterus: main holds no row under any older or newer name for the traits the records cover. Lichenostomus flavescens and Conopophila rufogularis SWS1 rows exist and are other genera. The notes say so where it matters (31, 32). No Fowlea pattern.
- Point 8 (canon). Every sampled record names the canon compilations that cover its taxon for the main bird and fly items. Omissions that cover the taxon: Invertebrate vision and Visual ecology on line 1 (cff_hz, corner_hz), Visual ecology on lines 14, 17, 19, 29 and 32 (cff_hz), the same books on line 33, and Lucas et al. 2024 and Cantlay et al. 2024 on line 13 (named in `screened`). The check script does not enforce this list. Under point 8 the omissions cost no record; I list them as uncounted.
- Point 9 (light-trap table). Main's open traits for Ostrinia, Enyo and Athetis (via `harvest_get.py`) list acuity_cpd, cff_hz, corner_hz and interommatidial_deg; spectral_range_nm is not open for any of them. The unit holds no spectral_range_nm record for a moth genus (the moth records are cff_hz and corner_hz). The screening agent's statement holds. Main holds Ostrinia nubilalis lambda_max_nm rows (van der Kooi et al.), and Enyo lugubris and Amphipyra pyramidea opsin-recovery rows only.
- pupil_shape. The cell is not open for any sampled genus (harvest headers), and the unit has no pupil_shape record. Nothing to test.
- The Elaenia identifiers. oa.mg 10.1002/cne.21992 is Coimbra, Trevia, Marceliano, Andrade-da-Costa, Diniz and Yamada 2009, "Number and distribution of neurons in the retinal ganglion cell layer in relation to foraging behaviors of tyrant flycatchers", J Comp Neurol 514(1):66. It reports retinal ganglion-cell counts and maps for the yellow-bellied elaenia (Elaenia flavogaster, about 4.15 million cells, a central fovea and a temporal area) and the mouse-coloured tyrannulet. PubMed 19260061 is the same paper (sweep-8 and sweep-41 identified PMID 19260061 as the Elaenia flavogaster and Phaeomyias murina ganglion-cell topography; my fetch of the PubMed page met a browser check, so the match rests on that and on the two results coming back together). It bears on Elaenia acuity_cpd, interreceptor_deg and fovea, which the unit left to wanted line 10 (a different paper), and it does not bear on lines 21, 22 or 23 (binocular_deg, fov_h_deg, cff_hz, lambda_max_nm, spectral_range_nm). Main holds no Elaenia row, and the wanted files hold no Coimbra et al. 2009 line for Elaenia. The third repeated result, a Pesquisa FAPESP article ("Visao extraordinaria a hora de cacar"), I did not open.

## Rate

- Sample: 0/20 = 0%. No error, so no extension.
- Pooled with audits 43 to 51 and 55 to 72 (7 errors in 627): 7/647 = 1.1%.
- Verdict: the unit passes.

## Leads (compilations or papers whose species lists I could not see)

- Coimbra et al. 2009 (above): Elaenia flavogaster acuity_cpd, interreceptor_deg, fovea. Add to the wanted list.
- Tyrrell and Fernandez-Juricic 2017 S1 Table and Martin 2007 (canon): species lists unseen; bear on lines 4, 13, 16, 31 (Lessonia, Phaetusa, Acanthagenys, Nesoptilotis binocular_deg and fov_h_deg) and on the Elaenia, Campylopterus and Mesembrinibis field cells.
- Haarlem et al. 2026 and Healy et al. 2013: species lists unseen; bear on lines 1, 8, 14, 17, 19, 29, 32, 33 (every cff_hz record).
- Odeen and Hastad 2013, Odeen, Hastad and Alstrom 2011, Hunt et al. 2009, Toomey et al. 2016, Emerling 2017 and the other canon pigment compilations: species lists unseen; bear on lines 6, 9 and the Elaenia, Ardeotis and Macronectes pigment cells. Odeen and Hastad 2003 was read by fetch summary only.
- Lisney et al. 2015 (hummingbird eye morphology and retinal topography, Brain Behav Evol 86:176) and Tyrrell et al. 2018 (hummingbird visual space, Front Neurosci 12:16): the fetched pages gave no species lists; they bear on Campylopterus acuity_cpd and the field cells (lines 27 and 28, not sampled).
- Empidonax paper (Sci Rep 2019, 10.1038/s41598-019-51774-w, wanted line 10): its 48-species survey (Table S3) was unseen and may name an Elaenia; the main species are Empidonax. Bears on Elaenia cells only if Table S3 lists it.
- Research Square preprint 10.21203/rs.3.rs-4203706/v1 (wanted lines 4, 11, 18): species lists unseen; bears on the Lepidoptera acuity cells, not on the sampled cff_hz record 33.
- The SORA record (Ornitologia Neotropical 15, supplement, pp. 215-222) that the record for line 6 mentions: I could not identify the article.

## Wanted lines (faults listed, not counted)

- Lines 9, 15 and 17 (Pollinating birds differ in spectral sensitivity): the AGRIS record shows Odeen and Hastad, 2010, J Comp Physiol A 196(2):91-96, DOI 10.1007/s00359-009-0474-z. The lines carry no authors, year 0 and no DOI; the page names families only (Trochilidae, Meliphagidae, Nectariniidae), no genera, so the species lists are unseen.
- Line 10 (A novel cellular structure in the retina of insectivorous birds): the study species are Empidonax virescens and E. minimus; the line's reason names Elaenia flavogaster as a hit for a search, which the page does not support beyond the unseen Table S3.
- Lines 1 to 8, 11 to 14, 16 to 20 not opened.
