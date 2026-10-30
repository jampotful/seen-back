# desk-d93 progress (South Asian plants in regional and open-access journals)

Started and finished 29 October 2026. Branch research/desk-d93. About 22 WebSearch and 40 WebFetch calls. 7 evidence records in docs/views/evidence/desk-d93.jsonl, no search records, no wanted lines. POWO and WFO could not be reached (proxy refusal), so every name was checked on GBIF species/match through WebFetch and each record says so.

## Filed
- Salacia fruticosa, diel (flowers open 11:00 to 12:00 h; protandrous, anthers 10:00 h, stigma receptive from 11:00 h for about 30 h). Subin K, Jose PA, Sarath TV, Journal of Threatened Taxa 10(15): 13002-13005, 2018, 10.11609/jott.3069.10.15.13002-13005. GBIF 7779185 accepted (paper's authority Wall. is a synonymous authority of the same binomial).
- Ophiorrhiza caudata, diel (anthesis 06:00 to 08:45 h; thrum opens before pin; Results and Discussion differ on morph timing). Theresa M, Sreekala AK, Mohanlal J, JoTT 13(13): 20056-20065, 2021, 10.11609/jott.6741.13.13.20056-20065. GBIF 5340946.
- Baccaurea courtallensis, diel (flowers open 06:30 to 10:00 h; three conflicting anther dehiscence times carried). Nandhini K, David VJ, Manimekalai V, Ravichandran P, JoTT 15(4): 22940-22954, 2023, 10.11609/jott.8180.15.4.22940-22954. GBIF 3082076. Fruit tree, not timber.
- Ilex embelioides, sense_chemical (GA3 soaks 18.09% at 200 mg/L up to 63.89% at 2,000 and 26.98% at 4,000 against 46.19% control; KNO3 lowered germination at 0.5, 1.5 and 2%; dark lowered in vitro GA3 germination at every dose). Malngiang L, Upadhaya K, Choudhury H, JoTT 15(8): 23805-23811, 2023, 10.11609/jott.8493.15.8.23805-23811. GBIF 5534321.
- Andrographis paniculata, sense_chemical (500 ppm GA3 above 85% against about 42% control; Results and Discussion differ). Jayawardhane J, Damunupola JW, Jayasuriya KMGG, Ceylon Journal of Science 50(2): 129-137, 2021, 10.4038/cjs.v50i2.7874. GBIF 3173178.
- Barleria prionitis and Rhinacanthus polonnaruwensis, sense_light_nonvisual (equal germination in light/dark and complete darkness: about 18% and 100%). Same paper. GBIF 3173129 and 5572961.

## Held out
- Hibiscus lobatus (Karthik et al., JoTT 17(8): 27323-27332, 2025, 10.11609/jott.9610.17.8.27323-27332): GA3 1 mg/L and H2SO4 15% data are in tables, but the abstract says field germination 4 to 6% while the tables give 17 to 33%, the in vitro light regime is not stated and no GA3 sentence is within 125 characters.
- Heracleum candicans (Butola and Badola, Indian Forester 130(5): 565-572, 2004, 10.36808/if/2004/v130i5/2040; GA3 250 uM, KNO3 100 mM, 30 min NaHClO3 81.3%) and Swertia chirayita (Bhatt, Rawal, Dhar, Seed Research 35(1): 66-69, 2007, 10.56093/sr.v35i1.165610; GA3 100 ppm): every abstract sentence runs past 125 characters and the Swertia PDF gave no text. Leads for a unit that can read the full text.
- Saussurea costus (Bhandari, Bisht, Prakash, Int. J. Conservation Science 11(3): 799-806, 2020; KNO3 5% 46%, GA3 44% against 16% control): every sentence naming the species also names Withania and Ocimum, and the paper reports no statistics.
- Andrographis paniculata light/dark (same Ceylon paper: no germination in complete darkness) and Barleria prionitis GA3 (above 95%): the only sentences are longer than 125 characters.
- Nepal Journal of Botany 2(1): 51-64, 2025 (Kafle et al., 37 species light/dark; 10.3126/njob.v2i01.78187): Table 1 did not extract, and no species sentence fits 125 characters.
- Nymphaea pubescens night-blooming (Begum, Ghosal, Chattopadhyay, Bangladesh J. Bot. 39(2): 179-183, 2010): the abstract sentence runs past 125 characters; the results sentence is not available whole.
- Aegle marmelos (Sri Lanka, 17 accessions pooled; journal details not printed in the file), Gladiolus genotypes (cultivars), Baccaurea courtallensis propagation (Current Science 125(4): 416-421, 2023; no light or GA3).
- Sri Lanka smoke work (Curtin repository, multi-species) and Coscinium fenestratum GA3 (OCR-garbled page, no bibliographic details).

## Blocked
POWO (powo.science.kew.org) refused through the proxy; WFO not tried. api.gbif.org opened only through WebFetch. No ResearchGate, academia.edu, Sci-Hub, LibGen or library-proxy page was opened (a Cambridge Core result behind an ezproxy host was left alone).

## Advice
threatenedtaxa.org PDFs, cjs.sljol.info (follow the 302 to storage.googleapis.com) and bdbotsociety.org print whole sentences and open without a login. Ask the fetch tool for sentences of 125 characters or fewer with their section, then confirm each quote with a yes/no request.

## Desk disposition after audit 183
Audit 183: 2 of 7 errors, both dropped (whole unit covered): line 2 Ilex embelioides (only 2,000 mg/L GA3 is significantly above the control; 500, 1,000 and 3,000 mg/L and both GA3 + KNO3 combinations share the control's letter, so the headline held for one dose of six, while two doses lowered germination significantly; the note wrongly said the combination claim was not tied to a comparison), line 4 Barleria prionitis (left out the next Results sentence, "However, they reached 100% germination after 300 days"). Refile both with those results carried. Held out by the desk after audit: line 6 Ophiorrhiza caudata diel (accepted at species level on GBIF only; POWO taxon page 758397-1 would not open and the WFO snapshot page opened for the genus only, so the accepted name is unconfirmed under the ruling that unconfirmed accepted names are held out; the record passed the audit on content and can be refiled once a POWO or WFO species page opens). Merged: Salacia fruticosa, Andrographis paniculata, Rhinacanthus polonnaruwensis (WFO June 2025 snapshot wfo-0000401628 opened by the desk: accepted) and Baccaurea courtallensis (WFO June 2025 wfo-0000304585 opened by the desk: accepted); line 7 wording corrected to one opening window and no stigma-receptivity timing reported.
