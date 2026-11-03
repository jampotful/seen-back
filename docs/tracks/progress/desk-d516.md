# desk-d516 progress

evidence_intake: evidence-kind-v2
intake_base: d49376cc2e1d237227676c1e95f48eac4e8da702

Angle used: the Leads-text ANGLE (bat and other echolocation emission parameters, sense_echolocation, physiological_response, one record per parameter). Reptile/fish eye diameter and spiders not searched. About 31 WebSearches; WebFetch only on URLs seen in search results. 32 records in docs/views/evidence/desk-d516.jsonl; check.py plain and --require-evidence-kind: 0 problems.

## Filed
- Neophocaena asiaeorientalis (Fang et al. 2015, PLoS ONE 10(6): e0129143, 10.1371/journal.pone.0129143, PMC page, CC BY): Table 1 rows peak frequency, centre frequency, RMS bandwidth, -10 dB duration for the free-ranging Tianxingzhou group (4 animals, 79 clicks) and the Baiji aquarium group (7 animals, 68 clicks) (8 records). MDD 1006446. Species-level; main only has the genus-level Jensen et al. 2018 compilation.
- Duco et al. 2023, J Threat Taxa 15(10): 23931-23951, 10.11609/jott.8597.15.10.23931-23951 (CC BY 4.0 printed): Table 1 rows for Hipposideros lekaguli (MDD 1004614), H. diadema (1004592), Taphozous melanopogon (1004826), Rhinolophus arcuatus (1004658), R. philippinensis (1004727), Megaderma spasma (1004650); duration, FmaxE, Fini, Fter each (24 records). Bats released into a 2.74 x 2.1 x 1.5 m tent; three calls per bat chosen, so calls are not independent; table caption says mean +- SE.

## Weak spots
- All text through the WebFetch reader. It refuses multi-row table reproduction; each Table 1 row was obtained by a one-row request, and the quotes are the reader's cell lists with presence columns cut (marked). Spacing in cells may differ from print.
- Fang et al.: the quoted peak-frequency row prints the Tian-e-zhou range as 12-135 (apparent typo, that group not filed). Abstract gives -3 dB bandwidth 15 kHz for Tianxingzhou against 22 in Table 1, so -3 dB bandwidth is not filed. Peak/centre frequency are not defined in the Methods.
- Duco et al.: Fini/Fter not defined beyond the caption.

## Not filed and why
- Aerodramus brevirostris (Zool Res 34(1): 8-13, 10.3724/SP.J.1141.2013.01008): abstract-only; licence appears only in page metadata (CC BY 3.0), no visible statement; n not stated; held out as in d326.
- Hipposideros pratti CF frequency (Zool Stud 54: 44): publisher page prints no licence and springer is refused; Table 3 has no n. Pooled Table 2 (59.5 +- 0.6 kHz) has no n either.
- Cameroon bats (J Basic Appl Zool 79(1): 1-9, Bakwo Fils et al. 2018, 10.1186/s41936-018-0041-7): authors found on DOAJ, Table 2 readable, but no licence statement reachable; held out.
- Sorex unguiculatus (Ecol Evol 2019): already on main via audit/corrected; text has ranges only. Oilbird (RSOS 2017, 10.1098/rsos.170255): ranges only, no mean values in text. Kogia sima (JEB 2021, 10.1242/jeb.240689): only repository copy reached. Myotis cf. davidii/aurascens (ZooKeys 1262): not a settled species. Orcaella heinsohni (JASA): repository copies only. Sousa chinensis pulsed-signal trains (Front Mar Sci 9: 915668): train-level, species already on main. Pseudoromicia principis: no echolocation in the paper reached. Vietnamese Academia J Biol Hipposiderids: CC BY-NC-ND, no values.
- Not filed for lack of MDD page or verbatim row: Rhinolophus inops (row not reproduced), R. macrotis, Miniopterus paululus, H. antricola, H. bicolor, H. pygmaeus, Myotis horsfieldii, M. muricola, Tylonycteris pachypus, M. eschscholtzii (rows in same Duco table; candidates for a unit with MDD access).

## Desk disposition after audits 1036-1039 (3 November 2026)
Audits judged 32 lines. Errors in 29 lines, all fixed from the auditors' replacement blocks: n (click counts) added to values that the quoted row does not print; quotes not word for word; omitted bimodal Baiji peak frequency (tank reverberation); omitted pooling across sexes and sites after a Kruskal-Wallis null test; omitted taxonomy doubts and regional contrasts (H. lekaguli, H. diadema, R. arcuatus morphotype caveat, R. philippinensis range); M. spasma Discussion says one individual while Table 1 says 2 bats. Line 20 (Taphozous melanopogon Fter 20.16 kHz) is dropped: the end frequency is printed below the minimum frequency 22.18 kHz in the same row, unflagged by the paper. 31 records merged (Neophocaena asiaeorientalis 8, Hipposideros lekaguli 4, H. diadema 4, Taphozous melanopogon 3, Rhinolophus arcuatus 4, R. philippinensis 4, Megaderma spasma 4).
