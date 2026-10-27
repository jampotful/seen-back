# Audit 88: desk-c11 (12 plant genera; branch origin/research/desk-c11, head dccf0f78)

## Samples (seed 88), drawn before any record was read

Search records (29 lines): `random.seed(88)`, `random.sample(range(1, 30), 20)`, sorted: 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 21, 24, 26, 27, 28.

Evidence records: all 8 lines of docs/views/evidence/desk-c11.jsonl are judged.

## Gate

`python3 -I tools/views/screen_candidates.py --check docs/views/searched/desk-c11.jsonl --wanted docs/views/wanted/desk-c11.jsonl` prints "0 problems".

## Evidence record verdicts (all 8), drafted first

| Line | Record | Verdict |
|---|---|---|
| 1 | Foeniculum vulgare sense_chemical | ok. link.springer.com 10.1007/BF00025215 opened: Thomas 1994, Plant Growth Regul 14(2): 139-143; all three varieties responded to GA4/7 solutions with higher germination in light at 20 to 30 C. Living seed, applied hormone (10(d)); grade m. |
| 2 | Tecoma stans diel | ok. threatenedtaxa.org JoTT 322 opened: Jonathan, Raju, Branham, Devi 2009, 1(2): 126-127, 10.11609/JoTT.o1871.126-7; "two anthesis schedules in a day", 0500-0800 and 1500-1700 hrs. |
| 3 | Achillea collina sense_chemical | ok. expertise.unimi.it 249132 opened: Manzo, Panseri, Giorgi 2013 (congress abstract); the quote is verbatim. Aphid- and jasmonic acid-induced emission of living plants (10(a), 10(d)). POWO (ipni 60477838-2, opened): Achillea collina accepted. |
| 4 | Achillea fragrantissima sense_light_nonvisual | ok. agjsr.agu.edu.bh paper 360 opened: Al-Charchafchi, Clor, Jawad 1986, 4(1): 22-31; the quote is verbatim. POWO 173984-1 (opened): accepted. |
| 5 | Mahonia aquifolium sense_chemical | ERROR (taxon). The value and quote hold (idpan.poznan.pl vol-74/74-149-155 opened: Pipinis et al. 2015, Dendrobiology 74: 149-155, DOI 10.12657/denbio.074.015 on the page). But POWO 31334-2 (opened) gives "Berberis aquifolium Pursh ... This species is accepted" with Mahonia aquifolium (Pursh) Nutt. as a homotypic synonym, and Berberis is a separate genus in queue.jsonl (Berberis thunbergii). By the audit 86 Eupatorium ruling the record logs a synonym of another genus. |
| 6 | Apocynum venetum sense_light_nonvisual | ok. PMC8248540 opened: Jiang, She, Tian, Tanveer, Wang 2021, 10.3389/fpls.2021.671157; the quote is verbatim. WFO 0000245931 (opened): accepted. Light against darkness (10(d)). |
| 7 | Bromus sterilis sense_light_nonvisual | ok. agriculturejournals.cz PSE 2024 70(5): 287-295 opened: seven authors as recorded, 10.17221/21/2024-PSE; the quote is in the abstract. POWO (Anisantha sterilis page, opened): "This name is a synonym of Bromus sterilis", so Bromus is the accepted genus. |
| 8 | Bromus auleticus sense_chemical | ok. inia.uy Gonzalez-and-Condon-2020.pdf opened: title "Germination of Bromus auleticus after different treatments to release seed dormancy", Silvana Gonzalez and Federico Condon, Seed Sci Technol 48(1): 27-31, 2020, DOI 10.15258/sst.2020.48.1.04. The rebuilt title, authors, year and DOI all match. The quote is verbatim; GA3 0.05% MGT 17.2 d against 19.2 d control and KNO3 alone not uniform across lots, as the value says. The POWO page for B. auleticus failed at its site; the name is in POWO's index (ipni 393544-1). |

(search records in progress)
