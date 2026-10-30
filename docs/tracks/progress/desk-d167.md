# desk-d167 (animal vision vein: fish, bird, damselfly, mayfly; 30 October 2026)

Branch research/desk-d167. Eight records in docs/views/evidence/desk-d167.jsonl from four papers, each with CC BY 4.0 listed on Crossref (fetched first, one try each) and a Creative Commons statement read on the page where the fetch returned one.

## Records
- Caves EM et al. 2021, J Exp Biol 224(24): jeb243420 (10.1242/jeb.243420): Xiphophorus hellerii (printed "helleri"; FishBase uses hellerii) anatomical acuity about 3 cpd (3 males, 3 females), optomotor acuity 0.8 cpd males and 3.0 cpd females (13 males, 12 females); the grating-against-grey assay (males 1-2, females 2-3 cpd) and the not-explained-by-eye-size result are carried in the notes.
- Chaib S et al. 2021, Biology Open 10(9): bio058796 (10.1242/bio.058796): Melopsittacus undulatus moving-target detection threshold 0.107 degrees = 4.68 cpd equivalent; 5 of 7 birds learned; main's 14.3 cpd grating value is noted as the higher figure. PMC text returned no licence line; Crossref lists CC BY 4.0.
- Roberts NS et al. 2025, Proc R Soc B 292(2047): 20242511 (10.1098/rspb.2024.2511): Ischnura elegans expressed LWS opsins LWA2 548, LWF1 531, LWE1 533 nm (HEK293T, in vitro). Quotes use " … " omissions to stay under 40 words.
- Egri A et al. 2025, Sci Rep 15(1): 29465 (10.1038/s41598-025-14294-4): Electrogena lateralis female eye cff 104.5 Hz (n = 6, dark-adapted ERG). Main already holds the male dorsal 148.7 Hz and the spectral peaks (desk-d164).

## Held out
- Ischnura elegans SWb1 397 and SWb2 416 nm: the sentence runs about 50 words with a mutant-control clause, no whole-sentence quote fits.
- Electrogena male ventral FFF 104.1 Hz: the whole sentence is 54 words.
- Sharkey CR et al. 2021, Front Ecol Evol (10.3389/fevo.2021.676369), Pygopleurus israelitus lambda max 631 nm: page states CC BY, but Crossref failed twice, so dropped per brief (main holds 628 nm for the species).
- Wakakuwa M et al. 2010 PLoS ONE (10.1371/journal.pone.0015015; Pieris rapae expressed blue opsins 450 and 420 nm): Crossref CC BY 4.0 read, but the PLOS page fetch returned the wrong article, doi.org and PMC were blocked.
- Egri-type and Gecarcinus lateralis (Lall and Cronin 1987): repository record states copyright, no CC. Swordtail PMC copy not reachable (redirect not approved); the journal PDF was used instead.
- Authority checks: GBIF API fetches were not approved; Plazi (Ischnura), FishBase (Xiphophorus) and main's existing records (Melopsittacus, Electrogena) were used.

## Untouched
Cephalopod eye counts, spiders, Hymenoptera, Coleoptera acuity, crustacean cells.

## Desk disposition after audit 252

Audit 252 judged all 8 records: 2 counted errors. Line 1 (Xiphophorus hellerii anatomical acuity) duplicated main (audit/corrected/fish-shark.jsonl line 154) and is dropped; the grade g to m upgrade belongs to the audit path for that record. Line 8 (Electrogena lateralis female flicker fusion) had a claimed significance test the paper does not report; note replaced with the auditor's text. The other six merge with the uncounted fixes: false "not on main" statements replaced, the authors' behavioural/attentional and optomotor-confound caveats on the Xiphophorus records, the licence-bearing URL and 7.7 to 10 cpd comparison on the budgerigar record, and the LWS co-expression caveat on the Ischnura records. 7 records merged. Lesson: grep main must include docs/views/audit/corrected and audit/ALL.
