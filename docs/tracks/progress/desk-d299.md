# desk-d299: eye states and counts in groundwater amphipods and millipedes, 6 records

Branch research/desk-d299 from origin/main. About 45 WebSearches (3 extended) plus fetches; every fetched article URL came from a WebSearch first. `python3 -I tools/senses/check.py | grep 'd299\.'`: 6 records, 0 problems. Crossref read by DOI for all six (author order matches the pages; all CC BY 4.0, five vor, EJT 819 content-version unspecified with the page-printed CC BY sentence). Repeat check after filing: grep of main docs/ and of the desk-d26x to d299 and audit-36x to 38x branch evidence and progress files by species and DOI: no repeats. New trait: none (ommatidia_count already used on main, flagged in the notes).

Filed (docs/views/evidence/desk-d299.jsonl):
1. Synurella odessana (Crangonyctidae, Amphipoda), "vestigial 7 detached ommatidia, black", Subterranean Biology 15; holotype male, paratypes 1 male and 2 females; per-eye reading not stated; Diagnosis says reduced number of ommatidia.
2. Hyleoglomeris erecta (Glomerida), "Ocelli 6(9)+1", printed notation, Zoosystematics and Evolution 102(3).
3. Hyleoglomeris rukouqu, "Ommatidium at least 7+1", holotype male and a female paratype, Subterranean Biology 30.
4. Gammarus sezgini (Gammaridae), eyes kidney-shaped, surface contrast record, holotype male, Zoosystematics and Evolution 100(3).
5. Caucaseuma strasseri (Chordeumatida), 20-25 (mainly 23) ommatidia in 6 rows in both sexes, cavernicolous, EJT 819; Discussion says counts do not differ between cave and epigean Caucaseuma.
6. Phoxirostus longicarpus (Laphystiopsidae, seamount amphipod), eyes reniform, bulging laterally, holotype female, Diversity 16(9).

Dropped:
- On main already: Gammarus tumaf (d283), Cylindroiulus villumi (d287), Caridina zhaoi and C. sinanensis (d290/d282), Hyleoglomeris alba, halang, translucida, Glyphiulus longus (d289).
- Sentence only in pieces or over the tool's reach: Phasmon typhlops (ZooKeys 1008, eye sentence of about 170 characters returned in two quotes), Caridina sinanensis and C. incolor (eye sentence long), Echinogammarus ozbeki (ZooKeys 1173, long), Glyphiulus promdami (Key couplet only).
- No eye sentence in the paper text: Niphargus hakani, N. elburzensis, N. zagrosensis, Stygobromus bakeri, Bogidiella pingxiangensis (figure page only), Strigamia ziyunensis and six congeners, Hyalella puna and H. tepehuana (figure pages only), Desmoxytes (ZooKeys 577).
- Colour only, no state or count: Thereuopoda kaijiangensis and T. edgecombei (ZooKeys 1264), Ischiomysis proincisa (cornea ratios), Koiulus interruptus (EJT 326: "Subtriangular, composed of 30-45 ocelli." follows a run-in heading and the genus and species are described together; held back as a fragment-like sentence and as a possible genus-level reading).
- Not filed for other reasons: Mimops orientalis (redescription, not new; "no response when the pale areas are illuminated" is an untested-design behaviour sentence), Parapseudomma stenurum (Nauplius; page prints no licence sentence), Gyorome guttatum (copepod, outside the angle), Phoxirostus yapensis (eye wording only reached as a clause).
- Blocked: Cryptops troglobitic Botswana species (ZooKeys, PDF URL PROVENANCE_REQUIRED, not in search results as an article page); Zootaxa/mapress, Plazi, Zenodo, PMC, BHL, zobodat copies not used.
- Searches for Pseudoniphargus, Metacrangonyx, Hadzia, Typhlogammarus, Hyalella cave species, Typhlatya/Halocaridina, cave crabs and crayfish, Callipodida, Polyzoniida and Scolopendromorpha returned closed journals (Zootaxa, Zoosystema), Plazi pages or items without eye sentences.

Retrieval note: Crossref single-DOI lookups worked one at a time; list queries returned a client error or rate limit. Pensoft download/xml URLs surfaced by search carried the full text; the tool's 125-character window split most Polydesmida and caridean eye sentences.

## Desk disposition after audit 391

Audit 391: 3 errors in 6 records (lines 1, 3, 4: specimen of the count, other species with eye text, omitted Variability wording), all fixed with the auditor replacements; optional lines 2 and 6 fixes applied. All 6 merged.
