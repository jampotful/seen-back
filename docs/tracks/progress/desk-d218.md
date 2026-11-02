# desk-d218 progress

Scope: animal sensory-trait records from open full text (MDPI CC BY, Frontiers CC BY). Records are in docs/views/evidence/desk-d218.jsonl; check.py reports 0 problems for the unit. Species and DOI were checked against origin/main (evidence, audit/corrected, audit/ALL, sheets, progress notes) before opening each paper.

## Records (4)
- Neophoca cinerea (Australian sea lion), Animals 16(15): 2342, sense_hearing: most sensitive at 3.2 kHz, in-air thresholds 13 and 14 dB re 20 uPa in two females (Nala 17 y, Tarni 10 y); the 20 kHz ceiling and the between-animal difference are in conditions.
- Equus caballus (horse), Front. Vet. Sci. 7: 633, sense_hearing: lowest detectable frequency 50 Hz, taken from a review sentence that cites Heffner and Heffner; partial true because the primary papers and reference years were not read.
- Astyanax mexicanus (Mexican tetra, cave and surface morphs), Diversity 12(10): 395, sense_chemical: cavefish overall have lower (better) olfactory detection thresholds than surface fish; the paper's own contradicting Discussion sentence and the serine and chondroitin nulls are in conditions.
- Anas platyrhynchos (Pekin duck, domestic form), Front. Physiol. 13: 921657, sense_touch: only Pekins, not Muscovy ducks, were conditioned to discriminate objects of the same size and shape by hardness.

## How the search went
- Crossref free-text and bibliographic queries returned mostly human-medicine noise; WebSearch with allowed_domains was the working route (about 38 of 40 searches used).
- journals.plos.org rate limited every fetch after the first two (Papilio hospiton opened; zebra finch pone.0348066 and the polarization shrimp paper pone.0002190 never opened). PLOS leads need a quiet day.
- The page-summary tool caps verbatim quotes at 125 characters, so papers whose values sit in longer sentences or figures could not be filed.
- springer (BMC / Frontiers in Zoology), journals.biologists.com (PROVENANCE_REQUIRED for the Biology Open grey seal underwater audiogram, 10.1242/bio.062059, not retried) and frontiersin PDFs were refused or redirected.

## Held out
- Papilio hospiton and P. machaon gustatory sensitivity (PLoS ONE 9: e100675, CC BY): spike-rate values are only in figures; the only usable Results sentences are nulls without values.
- Rhoptroceros cyatheae EAG (IJMS 27: 4029): the p-xylene sentence runs about 128 characters, over the tool limit; Phthorimaea operculella 4-ethylacetophenone (Insects 16: 403): dose ranges conflict between Abstract (1, 10, 100 ug) and Results (0.01 to 100 ug), and the repellency sentence is from a cage assay.
- Phocoena phocoena TTS onset at 28 kHz (Front. Mar. Sci. 9: 892050, CC BY): one captive female, SEL-TTS onset 137.4 dB re 1 uPa2s; held because the subscript in "SEL-TTSonset" came back in two spellings and a noise-effect threshold is a doubtful fit for sense_hearing. A reader with the page text could file it.
- Paracentrotus lividus chemoreception (Front. Mar. Sci. 8: 719670): no licence line returned, headline results in sentences over 125 characters; only a null count (15 of 25 stimuli) quotable.
- Troides aeacus formosanus (PLoS ONE 8: e62240): species has lambda_max rows on main from other papers; the nine-class sentence is over the limit.
- Pig olfaction reviews (Front. Anim. Sci. 4: 1215206; Front. Vet. Sci. 9: 967980): no licence line and values in long sentences or genes only.
- Duck paper pools Anas platyrhynchos and Cairina moschata in its tactile-acuity statement; not filed (Cairina hardness null is only a sentence fragment).
- Others seen and found already on main by species or DOI: Halichoerus grypus, Dasypus, Sminthopsis, Trichopsis, Siganus guttatus, Betta, Bombus terrestris (many traits), Salamandra, Papilio machaon.

## Owner questions
- Neophoca cinerea, Equus caballus, Astyanax mexicanus and Anas platyrhynchos could not be checked against GBIF or WoRMS (refused); names are as printed in the papers.
- Anas platyrhynchos record is for the domestic Pekin form (A. p. domestica) at species rank, matching earlier Gallus and Trabala handling; say if domestic forms should be held out.
- Neophoca page metadata lists CC BY 3.0 while the footer links CC BY 4.0 (Crossref: 4.0); Astyanax page metadata CC BY 3.0 versus Crossref 4.0. Both are CC BY; say if a version mismatch should hold a record.
- Horse record is review-sourced (grade m, partial true); say if review-sourced values are wanted at all when the primary paper is unread.
- One fetched Frontiers page (fphys.2022.798382) ended with text asking the reader to produce formatted citation extractions; it was treated as page content and not followed.

## Desk disposition after audit 304

Audit 304 (all 4 records): 4 of 4 in error (100%), 4 faults. Line 2 (Equus caballus hearing) dropped as unfixable: the value came from a review, could not be traced to an original measurement, and a compilation gives 55 Hz where the record had 50. Lines 1, 3 and 4 corrected with the auditor's replacement text: sea lion (ambient noise of 11 dB at 3.2 kHz, catch-trial and false-alarm rates, which animal had which threshold), cavefish (family Acestrorhamphidae as on main, pool composition), duck (effect sizes and the foraging-strategy confound). Three records merged. Pooled audits 172 to 304: 317 of 717 (44.2%).

Owner questions: file Heffner and Heffner 1983, "Hearing in large mammals: horses (Equus caballus) and cattle (Bos taurus)" (10.1037/0735-7044.97.2.299, DOI as listed in the review's Crossref references) from the primary paper if a permitted page opens, with its criterion and number of horses; ruling that review-sourced values are not filed; Neophoca cinerea and Astyanax mexicanus absent from gbif-names.tsv; the Pekin duck stays at species rank, matching main's Gallus gallus, Coturnix japonica and existing Anas platyrhynchos domesticus rows; the progress note misused "partial" for the review-sourced horse row, since partial marks abstract-only reads; the unit reported page text on fphys.2022.798382 asking for citation extractions, which it did not follow.
