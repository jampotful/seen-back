# desk-d524 progress

Angle: new open papers with species-level echolocation parameters (sense_echolocation, evidence_kind physiological_response, one record per parameter). 10 records (log docs/views/evidence/desk-d524.jsonl); check.py reports 0 problems for this file (plain and --require-evidence-kind). About 29 WebSearches.

## Filed
- Srinivasulu et al. 2019, PLOS ONE 14(10): e0213562 (10.1371/journal.pone.0213562), Rhinolophus andamanensis: mean FMAXE 57.65 +- 0.56 kHz and mean duration 46.63 +- 8.59 ms, n = 156 calls (one Results sentence; bats not counted; calls from rest and flight, so not a resting frequency). Reached with allowed_domains [journals.plos.org, peerj.com]; the exact-title unfiltered search returns only PMC, bioRxiv and aggregators.
- Vu et al. 2025, Biodiversity Data Journal 13: e165516 (10.3897/BDJ.13.e165516), Xuan Nha Nature Reserve, Vietnam: peak frequency and mean duration for Hipposideros armiger, H. poutensis, Rhinolophus episcopus, R. pearsonii (one individual each; SD basis and call count not stated). Quotes were assembled from consecutive fragments of at most 100 characters returned by the WebFetch reader.

## Not filed and why
- Sun et al. 2013 (pone.0070368, lead 1): journals.plos.org page read; Table 1 cells are not in the page text (caption and footnote only), so no population rows. Licence sentence and the RF definition are printed ('the stable CF portion of the echolocation pulses emitted by the motionless bat'). Needs a table source the auditors can open.
- Same PLOS table problem: Sousa plumbea/Tursiops aduncus clicks (pone.0230319, Tables 1 and 3 are images); R. clivosus pone.0187769 (on main species).
- Hipposideros larvatus colonies (pone.0151382): the text gives colony peak frequencies but n is undefined and the roosting-area recording method is not described; held out.
- Same Vu et al. paper, not filed: Hipposideros griffini, Rhinolophus thomasi, R. perniger and Tylonycteris tonkinensis (no MDD species page reached in my own searches; text values are in the paper).
- Pham 2021 Diversity 13(1): 18 and Thong 2022 Diversity 14(4): 258: species already on main (d517 and others). Otomops (PeerJ 4864): O. harrisoni on main, Musanze row is Otomops sp.
- Gyorossy 2024 Sci Rep 14: 23335 (Vietnamese bat calls): held out earlier (Crossref CC BY-NC-ND), tables not in the page text.
- Blocked or rate-limited this unit: BMC Evol Biol 14: 60, RSOS Lonchorhina aurita page, Wiley (ece3.73485, ece3.8296), Crossref API (permission unanswered), and repeated PLOS rate limits on pone.0041744 (Rhinolophus hildebrandtii complex) and pone.0148053 (R. swinnyi/simulator), both untested leads.

## Weak spots
- WebFetch reader output, not raw page text; sentences were reassembled from pieces. Licence for the Vu paper was read on the XML download copy.

## Desk disposition after audits 1064, 1065 and 1066 (3 November 2026)
Audit 1064 (lines 1-2, Srinivasulu et al. 2019): 2 faults (omitted Doppler shift compensation clause). Audit 1065 (lines 3-6, Vu et al. 2025, Hipposideros armiger and H. poutensis): 4 fixable errors (missing authorities in heading paths, unprinted "adult", unlabelled +/-, uncut-marked method quotes). Audit 1066 (lines 7-10, Vu et al. 2025, Rhinolophus episcopus and R. pearsonii): 16 faults (heading, authorities, SD wording). All fixed from the replacement blocks; all 10 records merged, none dropped.
