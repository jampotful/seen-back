# desk-d165 (invertebrate and cartilaginous-fish vision vein; 30 October 2026)

Branch research/desk-d165. Five records in docs/views/evidence/desk-d165.jsonl from two papers, both PLoS ONE, both with the CC Attribution statement read on the PMC page (Crossref lists CC BY 4.0). Crossref fetched first for each (WebFetch, one try each).

## Records
- Claes JM et al. 2014, 10.1371/journal.pone.0104213: rod lambda max for Etmopterus spinax 487.5 nm (microspectrophotometry), E. splendidus 485 nm and Squaliolus aliae 491 nm (detergent-extract difference spectra). Names valid in Catalog of Fishes. Abstract says 484-491, Results 485-491 (Results used). Main held only a group-level receptor_classes line from this paper.
- Fenk LM et al. 2010, 10.1371/journal.pone.0015838: Cupiennius salei juvenile pupil-to-lens ratio about 0.5 just after moulting and about 0.9 in following days (new trait pupil_lens_ratio, flagged in note). WSC accepted, family Trechaleidae.

## Held out
- Giglio A et al. 2022, Life 12(5): 741 (10.3390/life12050741): interommatidial angle Tenebrio molitor 6.89 deg (N=14) and Tribolium castaneum 12.99 deg (N=9); Pterostichus melas italicus 4.09, Clinidium canaliculatum 7.36. MDPI page text shows no CC statement (metadata rights link to CC BY 3.0 only; Crossref says 4.0), same hold as desk-d163 applied to a metadata-only link. Also the angle sentences do not name the species and N is undefined; C. canaliculatum genus sits under Carabidae on GBIF; subspecies for P. melas.
- Liang Z-L et al. 2024, Insects 15(7): 532 (Asiophrida xanthospilota ERG, ommatidia): same MDPI licence issue; species name not confirmed on any authority page.
- Kecskemeti S et al. 2021, Sci Rep (10.1038/s41598-021-92230-y), Lycoriella ingenua ERG peaks 370.1 and 526.3 nm: Springer page shows Open access label but no CC text; PMC copy blocked (permission prompt unanswered).
- Drozdova P et al. 2021, BMC Ecol Evol 21: 81: CC BY 4.0 confirmed, but transcriptome counts by species not given for the Baikal species and light-trap catches are lumped.
- Hart NS et al. 2020, Mol Biol Evol 37(3): 811 (shark and ray opsins): page shows copyright line with all rights reserved, no CC.
- Jessop A-L et al. 2020, J Exp Biol 223: jeb230979 (Gelasimus dampieri spectral sensitivity): page shows only a Company of Biologists copyright line. Garm A et al. 2007 (Tripedalia ERG), Battelle B-A et al. (Limulus opsins, JEB 2013 and 2015, 2010): no CC statement. Octopus polarization pages (PMC7212343, PMC8077535), PMC4317242-type and PMC10985371/4629671 pages: permission prompt or reCAPTCHA, left alone. Claes 2014 anatomical resolving power: Table 4 values and Results text disagree in what was fetched (about 3.1 vs 3.33 cpd for E. spinax), so not filed.

## Limits
Only two papers were clean. WebFetch of PMC pages was often blocked or reCAPTCHA'd, and most invertebrate vision papers in this vein are in journals that print no CC text on the page read. Untouched: copepods, isopods, Onychophora, horseshoe-crab acuity, bird spectral sensitivity.

## Desk disposition after audit 250
Audit 250 judged 5 records: 0 errors. Merged 5 records with the auditor's recommended uncounted fixes: E. spinax provenance (longline, euthanized), one pigment per retina in the shark extracts, the post-moult widening of the spider "pupil" as a lens-growth morphological measure, the 210 h time scale to 95% of asymptote, and the 5 to 10 µm diameter uncertainty. Trait key pupil_lens_ratio is accepted by check.py through the "new trait" note allowed in BRIEF; adopting it into the vocabulary is an owner decision (main also uses unlisted keys pupil and pupil_area_ratio).
