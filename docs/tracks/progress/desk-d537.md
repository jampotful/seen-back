# desk-d537 progress

Angle: NEW ANGLE only (animal sense_chemical in vertebrates and non-insect invertebrates; the OLD-ANGLE reptile/fish eye-diameter paragraph was not followed). evidence_intake: evidence-kind-v2; intake_base 2e8a8c995 (main at launch). 1 record (docs/views/evidence/desk-d537.jsonl), sense_chemical, evidence_kind behavioural_response. About 40 WebSearches; no Crossref in any form. check.py: 0 problems (plain and --require-evidence-kind).

## Filed
- Cyprinodon rubrofluviatilis (Fishes 8(6): 315, 10.3390/fishes8060315): conspecific skin alarm cue reduced post-stimulus water column position against a water control (Cue F1,140 = 21.170, p < 0.001; Population effects not significant). Whole Results sentence, 37 words. Wild-sourced females from five Red River sites. Catalog of Fishes page (fishcatget spid=13686) reached from my own search: valid, Fowler 1916.

## Weak spots
- Sentence assembled from three WebFetch reader chunks (the reader returns about 125 characters per sentence); needs a check against the page.
- Licence: footer CC BY sentence; page metadata says CC BY 3.0, footer link CC BY 4.0. Crossref not used.
- Per-treatment n after exclusions is not printed (160 fish, one hyperactive fish and eight trials dropped).

## Not filed and why
- Astyanax mexicanus in situ extract test (EvoDevo 4: 25, 10.1186/2041-9139-4-25): wild-caught, CC BY, CF-like 24 s v 1.8 s control (P < 0.01, n = 5 v 4), but the page prints only "Bibliowicz, J., Alie, A., Espinasa, L. et al."; full author list not reachable without PMC or springer. Lead if a publisher page with the full byline is reached.
- Four wild Taiwan rodents, leopard cat odour (Front Zool 17: 27): page prints no DOI and an "et al." author list; no statistics in the species sentences.
- Anolis sagrei (PeerJ 4: e1874): pet-trade stock. Hoover Manenti Melotto fire salamander larvae (Diversity 16: 312): reared in lab, sites pooled, no licence sentence. Roe deer repellent (Animals 15: 2932): drone abundance outcome, commercial repellent. Nothobranchius embryo cue (Fishes 11: 118): commercial breeder stock.
- Already on main or held earlier: Bufotes balearicus tadpoles (ani12192603), Caecidotea communis, Gadus morhua (d148, d255), Sargassum shrimps (d226, d252), Littoraria irrorata (d222), Xiphocaris elongata (PeerJ 11011, d201).
- Excluded by brief: both Paracentrotus lividus Frontiers papers (749493, 719670), Pagès Movement Ecology 2021, Carcinus maenas, Procambarus, Hypophthalmichthys, Larimichthys, Podarcis.
- Fetch failures: nature.com (Panulirus ornatus s41598-023-39567-8, client_error), peerj 408 (a URL not from my results; blocked, not retried).
