# desk-d446 progress

Angle: eye-size records, wider net, forty-first round. One paper yielded new records; the rest of the open spider pool I reached was already on main, in a closed journal, or printed no eye numbers. 8 records (log docs/views/evidence/desk-d446.jsonl).

## Filed
- Biodiversity Data Journal 13: e137852 (printed DOI 10.3897/BDJ.12.e137852; Hao L, Yu K, Zhang F, 2025; Halonoproctidae): Latouchia jinyun, male holotype MHBU-ARA-10000049 and female paratype MHBU-ARA-10000050, AME/ALE/PME/PLE each, trait eye_diameter_mm because the Description sentence prints the literal label 'Eye diameters and interdistance'. WSC species page 71021 (from my search results): accepted, Halonoproctidae.

## Weak spots
- The female sentence ends with a repeated MOA clause (0.43 long) that differs from the 0.51 printed one sentence earlier; no eye value is affected, and the quote is the whole sentence (36 words).
- Printed DOI is BDJ.12 while the citation line prints volume 13 (same as desk-d415 for the other species of this paper); journal string follows the printed volume 13.
- Crossref not read (UNCHECKED). Text came as fetch-tool pieces of the publisher preview page; the Methods units sentence was read in the same fetch.

## Not filed and why
- Latouchia yaoi (same paper): the page text ends inside the paratype material, before the Description (reached with offsets 0, 60000 and 68000).
- ZooKeys 1239 (three new genera of wolf spiders): Pensoft ZooKeys pages returned 'Site under maintenance' on three tries; only Houcosa zhaoi is on main (desk-d436).
- PeerJ 12: e16781 Dolomedes gregoric male, D. rotundus, D. hydatostella female: the publisher HTML text stops (90084 characters) before D. rotundus; the PDF stops inside the D. gregoric male description; no WSC species page for D. gregoric appeared in my search results (D. rotundus WSC 69346 is accepted). D. gregoric male values were read (AME 0.41, ALE 0.30, PME 0.57, PLE 0.61) but not filed.
- Diversity 18(1): 54 Herennia: the species of that paper (eva, maj, tsoi, tone) are all on main.
- ZooKeys 1197 Sinahahnia eyu/fanjingshan, ZooKeys 1215, ZooKeys 1221, ZooKeys 1249 Zoica: already on main or on the avoid list.
- EJT 1051 (Ouakri et al., Cesonia africana, Menemerus currens): the PDF prints no eye measurement numbers.
- Zoological Studies 63-21 (Pseudochthonius): page prints no licence and no eye data; Zootaxa Epidelaxia/Dolichognatha: closed; Scientific Reports 15: 42253 Dolomedes indicus: no publisher page appeared in my search results.
- Non-spider searches (scorpions, pseudoscorpions, harvestmen, crustaceans) returned no open paper with printed eye sizes.

## Searches
About 38 WebSearches; no Crossref URL was built or fetched.

## Desk disposition after audits (2 November 2026)

Audit 876 judged all 8 lines (Latouchia jinyun, BDJ 13: e137852). No wrong taxon, quote or value, WSC accepted, nothing dropped, not on main. Text faults corrected by replacement text: the sibling genus treatment 'Latouchia Pocock, 1901' wrongly put in as a parent heading in `where` and conditions, and the female note naming only the MOA length difference when the front width also differs (0.21 against 0.25). TRAIT: the auditor moved all 8 lines to sensory_anatomy because the Materials and methods print no eye dimension and no word 'diameter'. The desk kept eye_diameter_mm: both the male and female quoted sentences print the label 'Eye diameters and interdistance' (the standing label ruling), and desk-d415 already files the other three species of this paper on main as eye_diameter_mm, so one trait reading per paper holds across main. OWNER QUESTION (carried): eye_diameter_mm vs sensory_anatomy for label-only evidence (d415 and d446 together). All 8 merged.
