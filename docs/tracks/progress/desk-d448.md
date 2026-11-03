# desk-d448 progress

Angle: eye-size records, wider net, forty-third round. 32 records from one open EJT paper (log docs/views/evidence/desk-d448.jsonl). check.py: see below.

## Filed
- European Journal of Taxonomy 989: 289-310 (10.5852/ejt.2025.989.2901; Wang L-Y, Yang Y-S, Marusik YM, Zhang Z-S, 2025; Dictynidae in the paper, Argyronetidae on the current WSC pages; Dictynidae/Devade): Devade longa and D. pulla (new species; male holotype and female paratype each), D. mongolica (male SWUC-DIDM-01, female SWUC-DIDM-02; redescription) and D. qiemuensis stat. rev. (male SWUC-DIDQ-272, female SWUC-DIDQ-274). AME/ALE/PME/PLE, trait eye_diameter_mm (Methods: 'Eye sizes were measured as the maximum dorsal diameter.'; 'All measurements are in millimetres.').

## Weak spots
- Every eye sentence prints a stray comma after PLE ('PLE, 0.11'); the number after it is taken as PLE (stated in each record).
- The fetch tool returns each eye sentence in two pieces; joined with the en dash as printed. Neighbouring sentences and Methods are tool-returned pieces.
- Family field: current WSC (Argyronetidae); the paper's title and Family heading print Dictynidae. WSC pages for the four species opened from search results (spec-data/71851, 71852, species/9079, species/47801): all accepted. D. mongolica and D. qiemuensis are not new species and list no type material (Material examined only).
- Crossref not read; licence taken from the publisher PDF and article page (CC BY 4.0).

## Not filed and why
- Trilacuna jimengi, T. nangunhe (BDJ 13 e175820): no AME/PLE values, only ALE separation in diameters.
- Australoneon (Records of the Australian Museum 77(5)): reachable text ended before Methods and descriptions.
- Bungulla pipilata (AJT 102): eye ratios only, no diameters.
- Aname EJT 985 (55 species): PDF link seen only on a fetched page, not in my own search results; Bermejoa panguana (Arachnology 20(3)): no publisher page reached.
- Already filed on main: Hahnia dabashan and Sinahahnia chengkou (ZooKeys 1254, desk-d379); Spinirta (EJT 917); Icius alboterminus (JoTT 12(4)); Spiricoelotes (ZooKeys 1245, avoid list).
- Araneus tubabdominus (JoTT 13(12)): eye sizes given only as an order (AME>ALE>PME=PLE), skipped.

## Leads
- EJT 985 Aname, EJT 1007 Microstigmatidae, EJT 1016 Zodariidae, Arachnology 20(3) Bermejoa panguana and Arachnology 20(3) Psalmopoeinae: need a publisher page in search results.
- WSC bibliography pages 743, 744, 748, 752, 757 were read; open-journal 2025 candidates: AJT 104 (three trapdoor spiders), BDJ 13 e155306 (already on main), Arachnology 20(1) Raveniola.

## Desk disposition after audits (2 November 2026)

Audits 885-888 judged all 32 lines (Devade longa, D. pulla, D. mongolica, D. qiemuensis stat. rev.; EJT 989: 289-310). No wrong taxa, quotes or values and nothing dropped. WSC accepts all four species in Devade (family Argyronetidae; the paper prints Dictynidae). The Methods define eye size as the maximum dorsal diameter in mm, so eye_diameter_mm stands. Text faults corrected by replacement text: the licence note attributed the PDF's licence sentence to the article page (which prints "Creative Commons Attribution 4.0 International License"; both say CC BY 4.0), a Methods copy missing five sentences without a cut mark, an unverified issue-date claim, and an overstated "same author group" note. All 32 merged.
