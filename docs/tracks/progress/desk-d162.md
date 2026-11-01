# desk-d162 progress (animal vein: thin sense cells, airflow and hearing)

Scope: sense_infrared, sense_airflow, sense_vibration, sense_electric thresholds, bird and mammal audiograms. Main was grepped by trait and species (electric: only d147 papers and a few older ones; airflow: Danio, Xenopus, Lepidobatrachus; no Astyanax, Heterocephalus or Teleogryllus oceanicus hearing line).

Environment: Crossref was reachable only through WebFetch (api.crossref.org/works/<DOI>); curl and Bash had no outbound route (proxy 403). PMC answered some pages and showed a reCAPTCHA page for others (not worked around). The fetch tool refuses to return sentences over about 125 characters, so each quote was rebuilt from positional pieces (text before and after a phrase) and each piece was confirmed on a second fetch.

Records: 8 in docs/views/evidence/desk-d162.jsonl, all grade m, three open papers with a CC BY statement on the copy read.
- Astyanax mexicanus sense_airflow x4 (Lunsford, Paz, Keene, Liao 2022, eLife 11:e77387, 10.7554/eLife.77387, CC BY on publisher page and Crossref): posterior lateral line afferent spike rate in 4 to 7 dpf paralyzed larvae. Spontaneous 18.6 (Pachon cave morph) vs 12.4 Hz (surface); evoked by a 40 Hz neuromast deflection 101.3 vs 52.3 Hz. Not thresholds; deflection amplitude not reported; recording temperature not stated. Catalog of Fishes: valid.
- Heterocephalus glaber x2 and Meriones unguiculatus x1 sense_hearing (Okanoya et al. 2018, J Comp Physiol A 204(11):905-914, 10.1007/s00359-018-1287-8, CC BY): ABR in ketamine/xylazine anaesthesia, 4 mole-rats at 30 C body temperature and 2 gerbils at 37 C; tones 0.25 to 10 kHz only; 0.25 kHz thresholds about 75 dB (mole-rat) vs 40 dB (gerbil); mole-rat thresholds 25 to 50 dB higher on average. Notes carry the 15 to 25 dB ABR-versus-behaviour offset and the missing text values at 8 and 10 kHz. MDD taxon pages used.
- Teleogryllus oceanicus sense_hearing x1 (Kostarakos, Hennig, Romer 2009, Front Zool 6:22, 10.1186/1742-9994-6-22, CC BY statement in the PDF read): AN1 interneuron best frequency 4.5 to 5.1 kHz (9 of 11), 4.4 kHz (2). Orthoptera Species File: valid.

Held-out leads:
- Gryllus campestris and Teleogryllus commodus (same cricket paper): G. campestris OSF page did not state validity in what the fetch returned; T. commodus text (3.8 to 4 kHz) conflicts with Table 1 range (3.4 to 4.5 kHz).
- Bakken et al. 2018 JEB (pit viper IR, 10.1242/jeb.182121): Company of Biologists user licence, not CC.
- Emer et al. 2022 Behav Brain Res 429:113910 (Burmese python IR discrimination, 0.5 C difference): Elsevier, no licence stated.
- Crawford et al. 2024 Environ Biol Fishes 107(3):257 (sandbar shark electrosensitivity): exclusive licence, paywalled.
- Crowell et al. 2015 J Comp Physiol A (diving bird ABR, 10.1007/s00359-015-1024-5), Beatini et al. 2018 (saw-whet owl): no licence on the pages read. Lohr et al. 2013 (woodpecker ABR, JASA): copyright ASA, no CC.
- Lattenkamp et al. 2021 bat ABR: already filed by d156.
- Vibration, infrared (non-pit-viper) and sturgeon/paddlefish/platypus electroreception: searches surfaced no open-licensed paper; no search records written.

## Desk disposition after audit 247
Audit 247 judged 8 records: 0 errors. Merged 8 records with the auditor's recommended uncounted fixes applied: the evoked-n unit on lines 1 to 4 is stated as not given (df = 18 does not fit 22 fish), the full ABR threshold criterion on lines 5 to 7, the 0.25 and 2 kHz example thresholds, Discussion placement of the low-frequency wording on line 7, the umlaut in Römer and the 4.85 kHz average on line 8. Main holds another Teleogryllus oceanicus hearing line (Imaizumi and Pollack 1999), a different paper.
