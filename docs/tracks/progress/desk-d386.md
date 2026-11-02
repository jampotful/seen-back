# desk-d386 progress

Angle: non-spider arthropods with per-species eye measurements, then (after about 25 calls found nothing usable) spider families. 40 records from one open Pensoft paper (unit desk-d386; log docs/views/evidence/desk-d386.jsonl). check.py: 0 problems.

## Filed
- ZooKeys 1217: 195-213 (10.3897/zookeys.1217.127555; Wang L-Y, Mu Y-N, Lu Q-L, Xu Y-Q, Bu H-T, Zhang F, Zhang Z-S, 2024; fetch tool returned the CC BY 4.0 licence sentence; WSC refincluded/18025 lists the species, all Thomisidae): Camaricus medog, Monaeses xizang, Sinothomisus beibeng, Sinothomisus dawai, Spilosynema motuo; male (holotype) and female (paratype) each; AME/ALE/PME/PLE, eye_diameter_mm (Methods: eye sizes are the maximum dorsal diameter, per fetch-tool summary).

## Weak spots
- WebFetch refuses to print sentences over 125 characters; the eye sentence was joined from two consecutive pieces, Methods and neighbouring sentences are summaries, not verbatim.
- Camaricus medog female: description tied to paratype SWUC-T-THO-01-02 only by the fetch tool; the type list does not assign sexes to 01-02~06.
- Spilosynema motuo male description carries no code (heading 'Male holotype'); Figure 2 legend reportedly says 'Spilosynema xizang' for the female.
- Monaeses xizang female interdistance printed 'PME-PLE 041' (no decimal point); it sits in the quote, not in any filed value. Some female lines print 'PLE, 0.xx' with a comma, kept.
- Crossref vor and per-species WSC validity pages not opened (UNCHECKED).
- Monaeses xizang is a lead in desk-d359.md ('paper not opened'); no evidence record on main.

## Not filed and why
- Thomisus yarang and Pharta xizang (same paper): Thomisus female paratype code conflicts between type list (-06-02-03) and description (-06-03); Pharta xizang has no holotype and no code tied to the measured males/females. Left for a unit that can read the page whole.
- Xizangiana plankton (BDJ 12: e116569, 2024): the fetch tool found no eye-size definition in Methods, so the trait key is unsupported; 8 records dropped. WSC spec-data/69200 shows it accepted.
- Brachyponera (ZooKeys 1230) ants: already on main (desk-d291). Tyrannochthonius (EJT 1058, 2026): only eye counts in clauses, no whole sentences returned by the tool, and the genus is on main from other papers. Androctonus najdensis (ZooKeys 1262), Mesomexovis caxcan (ZooKeys 1243), Caridina zhaoi (ZSE 102), Alluropus/Rhysida Vietnam (ZSE 101): no per-species eye measurement or count printed (checked). Harvestmen, isopods, amphipods, fireflies, bees, millipedes, centipedes, Collembola: searches returned only Plazi/Zenodo/aggregator copies or papers with no eye values; Collembola and centipede eye counts are already heavily filed on main. Pensoft CSV tables (ZooKeys 100001, ~2022: wasp 'Max. diameter eye' rows) were seen but the paper page was not reachable from search results, so not filed.
