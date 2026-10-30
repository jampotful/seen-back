# desk-d144 progress (animal vein: thin sense_* cells in taxa not yet covered)

Scope: sense_hearing, sense_magnetic, sense_thermal and sense_infrared cells on main. Checked main (evidence, audit/corrected, searched, wanted) by species, DOI and first author before filing: no line for Panulirus argus magnetic, Aedes aegypti thermal, Merimna atrata, Dicentrarchus labrax hearing or Bufo bufo magnetic. No search records and no wanted lines (the vein is sense traits, not harvest genera).

Records: 8 in docs/views/evidence/desk-d144.jsonl, all grade m, one named species each, full text read (Results and Discussion) for all but none abstract-only, so no "partial" flags. Limiting findings are carried in value, conditions or note.
- Panulirus argus sense_magnetic (Ernst and Lohmann 2018, J Exp Biol 221(5) jeb172205, 10.1242/jeb.172205): 33 of 49 in the control den; reason unknown, size effect unconfirmed. Crossref returned client_error, so authors and title are from the PDF itself.
- Aedes aegypti sense_thermal x2 (Corfas and Vosshall 2015, eLife 4 e11750, 10.7554/eLife.11750, CC BY): attraction at 2.5 C above ambient; upper threshold about 50 to 55 C. CO2 present, Peltier stimulus not a host.
- Merimna atrata sense_infrared x2 (Hinz et al. 2018, PLoS ONE 13(2) e0192865, 10.1371/journal.pone.0192865, CC BY): avoidance at 48.7 mW/cm2 (one beetle below criterion on one side); weak 11.4 mW/cm2 test 4 of 9, authors call it inconsistent.
- Dicentrarchus labrax sense_hearing (Rojas et al. 2026, Fish Physiol Biochem 52(1):9, 10.1007/s10695-025-01628-2, CC BY): best 300 Hz within 100 to 600 Hz; particle motion not measured. Order given as Perciformes per GBIF; family Moronidae.
- Bufo bufo sense_magnetic x2 (Landler and Gollmann 2011, Front Zool 8:6, 10.1186/1742-9994-8-6, CC BY): unimodal along the d-axis in the natural field; bimodal when reversed (unimodal test P = 0.10). Males only; cue conflict and learned route not excluded.

Names: GBIF species match (api.gbif.org/v1/species/match) gave ACCEPTED for all five species. Fish name not checked on Catalog of Fishes or FishBase (the FishBase page timed out on a permission request); GBIF lists Dicentrarchus labrax (Linnaeus, 1758) as accepted, and the paper title uses it.

Method note: WebFetch returns pieces of at most about 125 characters; each quote was reassembled from consecutive pieces and confirmed on a second fetch with a differently worded prompt (Merimna weak-IR sentence confirmed on PLoS ONE page after the DOAJ page). PMC opened for PMC12764546 and PMC3548892 but returned a reCAPTCHA page for PMC2933256 and PMC4512887. Crossref was refused for jeb.172205 and for a bibliographic query.

Held-out leads:
- Lohr, Brittan-Powell and Dooling 2013, JASA 133(1):337, 10.1121/1.4770255 (PMC3548892): woodpecker ABR audiogram, lowest thresholds 1.5 to 4 kHz in the Results; 9 downy, 2 hairy and 3 red-bellied birds pooled in that statement and the paper reports no significant difference among the species, so a species record needs a per-species figure or table not reached.
- Brittan-Powell et al. 2010, JASA, ABR in Gekko gecko (5) and Anolis carolinensis (7): both most sensitive around 1.6 to 2 kHz, anoles more sensitive above 5 kHz by over 20 dB. Abstract summary only (sonicfield.org), no DOI seen, PMC blocked; not filed.
- Ebert and Westhoff 2006, J Comp Physiol A 192:941, 10.1007/s00359-006-0131-8: Crotalus atrox behavioural IR detection to 100 cm (about 3.35e-3 mW/cm2); Springer paywalled, closed. Candidate for the wanted list by DOI.
- sense_taste is not a trait key in check.py or BRIEF; any taste record needs "new trait" in note. Taste is the thinnest animal cell (0 records), with sense_chemical at 522.
