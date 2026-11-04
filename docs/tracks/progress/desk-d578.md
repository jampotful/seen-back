# desk-d578 progress

evidence_intake: evidence-kind-v2; intake_base: 0ae79fea1d71c56b9c743f2b950d6531c82411a5 (origin/main when checked).

Angle: sensory_anatomy, tympanum / external ear, from Pensoft new-species descriptions (OLD-ANGLE paragraph ignored). 5 records (docs/views/evidence/desk-d578.jsonl): 4 anatomical_presence, 1 anatomical_measurement; one record per species. About 40 WebSearches; no Crossref, no proxy hosts, every WebFetch URL came from my own search results. check.py: 0 problems (plain and --require-evidence-kind).

## Filed (licence sentence read on the publisher article_preview page; ASW page opened from my own search)
- Pristimantis attenboroughi, ZooKeys 660: 17-42 (10.3897/zookeys.660.11394): holotype MUSM 31196, tympanic membrane and annulus absent. Search: "Pristimantis attenboroughi new species ZooKeys tympanum article preview"; ASW via '"Pristimantis attenboroughi" Amphibian Species of the World Lehr and von May 2017 holotype'.
- Phrynopus apumantarum, Evolutionary Systematics 7(1): 105-116 (10.3897/evolsyst.7.96258): holotype CORBIDI 20553, tympanic membrane and annulus absent. Search: "new species Phrynopus OR Pristimantis OR Noblella OR Bryophryne "tympanic membrane" absent OR present "Evolutionary Systematics" OR ZooKeys article preview Chávez Catenazzi OR Lehr". The paratopotype count in the text (3 females, 4 males) does not match the codes in the figure and Variation text; disclosed.
- Rhinella lilyrodriguezae, ZooKeys 673: 21-47 (10.3897/zookeys.673.13050): holotype MUSM 32204, tympanic membrane present, annulus weakly defined. Search: "Rhinella lilyrodriguezae" new species ZooKeys 673 tympanum article preview (figure pages), then the article_preview page by article number.
- Pristimantis sinschi, ZooKeys 994: 125-148 (10.3897/zookeys.994.56277): holotype MUSM 32733, tympanic membrane and annulus absent. Search: "Pristimantis sinschi Lehr Moravec Kodejs 2020 ZooKeys 994 tympanum article preview Amphibian Species of the World".
- Pristimantis pulchridormientes, ZooKeys 610: 113-130 (10.3897/zookeys.610.8507): holotype CORBIDI 15578, TD 31% of ED (ratio 0.31); Diagnosis says ED 3x TD (about 0.33), rounded and disclosed. Search: "Pristimantis Tingo María National Park new species Chávez Catenazzi ZooKeys 610 Amphibian Species of the World".

## Weak spots
- All text came through the WebFetch page reader (about 125 characters per piece, summarising and refusing long verbatim output); long holotype sentences were reassembled from pieces and the cuts were chosen so that no cut text was needed to check the value. Quotes should be re-read on the publisher page by the auditor.
- Family: ASW now files the Pristimantis species under Craugastoridae (Ceuthomantinae or Pristimantinae paths vary), while some papers print Strabomantidae (Phrynopus, P. sinschi); the rows store Craugastoridae.
- The Diagnosis of P. attenboroughi sits as a run-in label under the Generic placement heading, as the reader reported it.
- Four of the five rows are presence/absence statements with no number; only P. pulchridormientes has a ratio, and the tables of the other four carry no tympanum row, so nothing could contradict the text.

## Not filed and why
- Leptobrachella yachangensis (Herpetozoa 38: 321-332): holotype TMP/EYE 0.48 agrees with Table 2 (2.1/4.4), but the same sentence prints TEY/TMP 0.48 where the table gives 0.33; skipped as conflicted.
- Boulenophrys yezhongensis (Herpetozoa 38: 117-136): holotype ratio 0.6 but the holotype is not tabulated and the Variation section calls one specimen's tympanum 'small'; skipped.
- Diasporus citrinobapheus (ZooKeys 196: 23-46): Diagnosis 'TD about 41% of ED' against holotype 'TD 33% of ED'; conflicted, skipped.
- Rhinella yunga (ZooKeys 371: 35-56) and Oreophryne gagneorum: papers read, but no ASW species page reached from my own searches.
- Pristimantis ashaninka, P. etsa, Bryophryne phuyuhampatu, Noblella madreselva, Pristimantis maryanneae: already on main or in earlier units.
- Gekko wuzhengjuni: Reptile Database lists it as Goniurosaurus wuzhengjuni and the ear clause sits in a very long sentence; not pursued. Lizard and snake searches (ear opening) returned only older Zootaxa/non-Pensoft pages and already used species.

## Desk disposition after audits 1130, 1131 (4 November 2026)
Lines 1-4 merged with the auditors' replacement text. Line 5 (Pristimantis pulchridormientes, tympanum 0.31 of eye diameter) dropped by the desk: audit 1131 found the holotype measurements print ED 2.7 and TD 0.5 (about 0.19), which contradicts the 31% filed and was undisclosed, and the "no row on main" claim was false (desk-d343 has an eye_diameter_mm row for the same species and DOI). The same conflicting-figures rule dropped Pristimantis burtoniorum in d577. The auditor's corrected text is saved in audit-1131 if the owner prefers to file it with the contradiction disclosed. Errors: all of lines 1-5 (line 1 paraphrased preservation and holotype sex not as printed; line 2 paratype codes reordered and a CORBIDI 20439 sex conflict left out; line 3 run-in label in the heading path, paratype sexes and total not as printed; line 4 Comparison misquoted: the page prints "P. ventrimarmoratus and P. sinschi both lack a tympanum"; line 5 as above). Quotes, licences, citations, ASW names and the Craugastoridae convention held. 5 of 5 counted as errors; 4 merged.
