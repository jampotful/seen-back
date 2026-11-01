# desk-d143 progress (animal vein: hearing, electroreception, magnetoreception, infrared, lateral line)

Scope: sense cells the gap tables do not show. `gaps.py --world 1200` covers vision rows only; counts of sense_* records on main showed thin animal cells: sense_hearing 15 taxa (no fish, frog, bird or mammal species), sense_electric 4, sense_magnetic 5 (birds and Arabidopsis only), sense_airflow 2, sense_infrared 12. d142's held-out list (Passer, Sciurus, Anolis, Trachemys, Harmonia, Danaus) was not repeated.

Records: 13 in docs/views/evidence/desk-d143.jsonl, all grade m, single named species, each checked against main (taxon and DOI) before filing. Authors and DOIs from Crossref (api.crossref.org, WebFetch).
- Etroplus maculatus and Steatocranus tinanti sense_hearing (Ladich and Schulz-Mirbach 2013, PLoS ONE, 10.1371/journal.pone.0057588), abstract, partial.
- Pipistrellus pygmaeus sense_magnetic x2 (Schneider et al. 2023, Biol Lett, 10.1098/rsbl.2023.0181), abstract, partial; includes the uniform-distribution (null direction) treatment.
- Tursiops truncatus sense_electric x2 (Huttner et al. 2023, J Exp Biol, 10.1242/jeb.245845), abstract via a mirror page, partial; 40-word limit met with one marked ellipsis.
- Caretta caretta sense_magnetic x2 (Lohmann 1991, J Exp Biol, 10.1242/jeb.155.1.37), page text read incl. Results (16 per condition).
- Crotalus oreganus sense_infrared x2 (Bakken et al. 2018, J Exp Biol, 10.1242/jeb.182121), abstract on a PubMed mirror, partial; includes the body-temperature result the authors could not explain.
- Danio rerio sense_airflow (Groneberg et al. 2015, Front Neural Circuits, 10.3389/fncir.2015.00009), abstract, partial; larvae only.
- Oryzias latipes sense_magnetic and Danio rerio sense_magnetic (Myklatun et al. 2018, Nat Commun, 10.1038/s41467-018-03090-6, CC BY), abstract, partial; the zebrafish record is the null (same sentence).

Method note: WebFetch returned pieces of at most about 120 characters; sentences were reassembled and each was confirmed on a second fetch (differently worded prompt). PMC and Europe PMC are blocked (reCAPTCHA or error) and curl is refused by the proxy, so full texts of PMC-only papers were not reached. No search records and no wanted lines written: the full per-trait protocol (two searches per trait per genus, citation step) was not run for any genus, since the vein is sense traits, not harvest genera.

Held-out leads:
- Brittan-Powell et al. 2005, JASA, 10.1121/1.1928767: Megascops asio ABR audiogram, "hear best between 1.5 and 6.4 kHz"; JASA is not open, and the sentence's spacing differed between two mirror pages, so not filed.
- Jeb237313 (J Exp Biol 224(2), "Three auditory brainstem response (ABR) methods tested and compared in two anuran species"): audiogram peaks 400-600 and 1500-1600 Hz for Pelophylax esculentus and Rana temporaria pooled in the abstract; needs per-species values from the full text.
- Hearing thresholds in European sea bass (PMC12764546) and Hyla chrysoscelis ABR (PMC3961062 or peeref listing): PMC blocked.
- Magnetic orientation of the common toad, Bufo bufo (PMC3072941, Front Zool 2011): PMC blocked; the only other result was a library-proxy mirror, left alone.
- Harris 2013 Potamotrygon motoro electroreception (0.005 mV/cm): a master's thesis, so excluded.
- Schneider, Schmitz and Schmitz 2015 (Front Physiol, Melanophila IR organ): a concept paper, no measurement; Melanophila already on main.
- J Exp Biol 226 pages for Hüttner 2023 and Royal Society page for Schneider 2023 timed out on a permission request; only mirror and repository pages were used.

## Desk disposition after audit 228
Audit 228 found 4 of 13 records in error (30.8%), all fixable with the auditor's replacement text, so all 13 were merged with the corrections applied. Line 1: filed under the synonym Etroplus maculatus; taxon changed to Pseudetroplus maculatus (Eschmeyer's Catalog of Fishes). Line 3 (Pipistrellus 120 degree shift): value, conditions, where and note rewritten to carry the Discussion's limiting result (the shifted bats did not turn by the predicted 120 degrees; reversal or stress possible). Line 6 (Tursiops AC): the 5 and 25 Hz thresholds come from one of the two dolphins. Line 7 (Caretta): conditions now carry the prior light exposure and the author's calibration suggestion. Uncounted context was also applied to lines 4 and 8, and the Tursiops url and eye field were corrected. The access field keeps "open" because the check vocabulary has no free-full-text value; the Caretta paper's licence is the Company of Biologists user licence. Lessons for the next animal unit: abstract-only reads hide the Discussion's limiting results, a species reported from one individual cannot be logged as "two animals", and a synonym check against the Catalog of Fishes or FishBase is needed for fish names. Held out: Megascops asio ABR audiogram (not open), Pelophylax and Rana ABR (two species pooled), European sea bass hearing and Bufo bufo magnetic (PMC blocked).
