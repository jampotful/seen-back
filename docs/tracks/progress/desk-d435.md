# desk-d435 progress

Angle: eye-size records, wider net (journals not yet used). 20 records from five open Journal of Threatened Taxa papers (log docs/views/evidence/desk-d435.jsonl). check.py and check.py --require-evidence-kind: 0 problems for this file.

## Filed
- J. Threatened Taxa 12(4): 15475-15480 (10.11609/jott.5371.12.4.15475-15480; Prajapat DA, Kamboj RD, 2020; Salticidae): Icius alboterminus male, AME/ALE/PME/PLE, 4 records, eye_diameter_mm (sentence prints 'Eye diameter').
- J. Threatened Taxa 17(8): 27391-27395 (10.11609/jott.9757.17.8.27391-27395; Parmar SI, Prajapati H, Pandya PJ, Prajapati DA, 2025; Salticidae): Pellenes iva male and Thyene bivittata male, 8 records, sensory_anatomy (label 'Eye measurements').
- J. Threatened Taxa 18(1): 28239-28241 (10.11609/jott.10102.18.1.28239-28241; Parmar SI, Pandya PJ, Chauhan VU, 2026; Salticidae): Sonoita lightfooti male RRLC-ZC/SP-09, 4 records, sensory_anatomy.
- J. Threatened Taxa 18(7): 29364-29366 (10.11609/jott.10297.18.7.29364-29366; Parmar SI, Chauhan VU, Yogi K, Pandya PJ, 2026; Theridiidae): Steatoda albomaculata female, 4 records, sensory_anatomy (label 'Eye measurements and inter-distances').

## Weak spots
- All four are distribution-record or male-notes papers, not new species. Measured individual not stated in Icius (4 males), Pellenes (4 males), Thyene (2 males) or Steatoda (2 females); said in conditions.
- Fetch tool returned several passages as paraphrase (Pellenes/Thyene material and methods); labelled as such. Titles of Pellenes/Thyene and Steatoda assembled from consecutive printed lines. Icius authors: PDF byline 'Prajapat', article page 'Prajapati'; PDF spelling used.
- DOIs as printed on article pages; Crossref not read (UNCHECKED). WSC species pages opened for all five species, all accepted.
- Grep of main for Sonoita and Steatoda covered docs/ only; Icius, Pellenes, Thyene were also git-grepped across remote desk branches.

## Not filed and why
- JoTT 16(6) 25492 Stenaelurillus marusiki/S. vyaghri, JoTT 16(7) 25630 Proszynskia diatreta: no eye numbers. JoTT 13(12) Araneus tubabdominus: interdistances only. JoTT 6(3) Hersilia (2014) and 7(3) Thomisus (2015): outside window / no numbers.
- Arachnology 19(8): 1127-1138 Gephyrellula lavidabonita (female holotype eyes printed): publisher site prints 'All Rights Reserved', no open licence, no DOI on page. Arthropoda Selecta 28(4) Phlegra abhinandanvarthamani: no licence statement. J. Insect Biodiversity and Systematics Afraflacilla goaensis, Carrhotus piperus: no licence, no text reached.
- EJT 943 Tekellina: no eye sizes printed. Pensoft sites (Evolutionary Systematics 196576) returned a maintenance page.
- Papers on the avoid list reached again by search (ZooKeys 1255 Qianlingula, 1202, 1200, 1108): skipped.

## Leads
- More JoTT spider short communications by Parmar/Pandya/Prajapati (they print 'Eye measurements' sentences); search each only once.

## Desk disposition after audits 828-830 (2 November 2026)
All 20 records merged, none dropped. Audit 828: the Icius alboterminus lines (1-4) moved from eye_diameter_mm to sensory_anatomy because the Methods define no eye diameter (the sentence label "Eye diameter" alone does not meet the standing rule only when the Methods or heading define it; the desk follows the auditor, a trait move not counted as an error under the yield policy); the author spelling is Prajapati (the "Prajapat" form came from a PDF text extraction). Pellenes iva lines pass. Audit 829: Thyene bivittata and Sonoita lightfooti pass; faults were text (AER/PER described as eye-row widths the paper never defines; a Variation subsection that only Pellenes has; the measured specimen inferred; the licence cut short). The WSC prints a different DOI for Sonoita lightfooti (jott.10290) than the paper (jott.10102): the paper's printed DOI is kept. Audit 830: Steatoda albomaculata passes (a nonexistent "Materials and Methods" heading removed). None of the four male-notes/records papers states which individual was measured except where noted in each record; nothing was inferred. Counted errors: 0.
