# desk-d518 progress

evidence_intake: evidence-kind-v2
intake_base: 7b43aedc64c70645d8c5be9827c6b01d42ac5e28

Angle used: the echolocation ANGLE (sense_echolocation, physiological_response, one record per parameter); the reptile/fish paragraph and spiders were not searched. About 32 WebSearches; WebFetch only on URLs seen in search results. 27 records in docs/views/evidence/desk-d518.jsonl; check.py plain and --require-evidence-kind: 0 problems.

## Filed
- Jung K, Molinari J, Kalko EKV 2014, PLoS ONE 9(1): e85279, 10.1371/journal.pone.0085279 (PMC PDF, CC BY printed): search-flight calls of New World molossids, Tables 1-3, one row per call type; start frequency, end frequency and call duration (mean +- 1 SD, NC/NS in conditions) for Neoplatymops mattogrossensis (2 call types), Nyctinomops macrotis (1), Cynomops greenhalli (2), Eumops dabbenei (2), Eumops nanus (2) (27 records). MDD pages 1005233, 1005237, 1005168, 1005178, 1005185. Only Tadarida brasiliensis from this paper is on main. Reached by the unfiltered search: Neotropical bat echolocation call parameters species table Phyllostomidae OR Emballonuridae OR Molossidae open access Scientific Reports OR PeerJ OR PLOS ONE call duration peak frequency mean

## Weak spots
- The reader extracts the PDF with the plus-minus sign as "6" (32.661.7 = 32.6 +- 1.7). Decoding is confirmed by the Table 3 footnote ("mean 61 standard deviation") and SF-EF=BW arithmetic, but the quote keeps the extracted form; an auditor on the PLoS HTML will see the sign.
- Number of individuals is not stated; SD is across calls; each species also has a second call type not filed for N. macrotis (only one printed).

## Not filed and why
- Srinivasulu et al. 2016 (JoTT 8(14): 9667-9672): Table 1 not in the reader text from either download URL; n not resolved. Not filed. (The core.ac.uk copy returned a different paper, an Andaman Hipposideros diadema masoni note; subspecies, not filed.)
- Pontoporia blainvillei, Bittencourt et al. 2025, Front Mar Sci, 10.3389/fmars.2025.1641888 (CC BY): whole sentence "Clicks occurred from 88.7 kHz and 250 kHz, with a mean peak frequency of 132.4 +- 6.8 kHz." exists, but the n behind it is unstated (Table 2 n = 55 + 34 reproduces 132.4 but the text counts 43 trains and 109 packets sequences and 12,505 detected clicks); single hydrophone, off-axis not excluded; reader refuses verbatim Table 2 rows. Lead for a unit with a verbatim-row reader; main has only Jensen et al. 2018 for this species (different DOI, Fc not peak).
- Chakravarty 2017 Tadarida teniotis (JoTT 9(7), CC BY): Tables 2-3 absent from the reader text, no numbers in text.
- Smarsh et al. 2021 Rousettus aegyptiacus (Proc R Soc B 288: 20211714, CC BY): adult instantaneous frequency 46.3 +- 0.12 kHz, but n inconsistent (3 vs 4 adults, 37 clicks), row label garbled by extraction, text/table duration units conflict; held out.
- ChiroVox (PeerJ 12445): no per-species values; Taray et al. 2021 (Philippine J Sci 150(6B)): no licence, values only in PDF; Zambia (Acta Chiropterologica 2025) repository copy only; Sonozotz (Ecol Evol 10(11)): no text reachable; short-finned pilot whale JASA 2021: already on main (oa-7), no open copy; Fra 2025 sperm whale survey: no values; ZooKeys 1262 Myotis cf. davidii/aurascens: unsettled species.
- Remaining species in Jung et al. 2014 (Molossops temminckii and neglectus, Molossus x4, Cynomops planirostris, Promops nasutus and centralis, Eumops glaucinus and auripendulus, Nyctinomops laticaudatus) are free on main; Promops centralis Low row prints NC 12 with NS 13 (sequences above calls), so check before filing; rows for the others were read for Molossops neglectus, Promops centralis and Eumops auripendulus in this unit's notes only.
