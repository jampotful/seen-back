# desk-d600 progress

Angle: new-species descriptions with defined ED, TD or eye-diameter measures in open journals (Vertebrate Zoology, Biodiversity Data Journal), reached by exact-title and phrase searches. 12 records (log docs/views/evidence/desk-d600.jsonl), evidence_kind anatomical_measurement. About 41 WebSearches. check.py: 0 problems for this file (plain and --require-evidence-kind).

## Filed
- Vertebrate Zoology 73: 153-159 (10.3897/vz.73.e94207) Oreophryne chlorops: holotype ED 4.8, Table 1 row. Search: 'Oreophryne chlorops Günther Iskandar Richards 2023 Vertebrate Zoology new species'.
- Vertebrate Zoology 72: 433-444 (10.3897/vz.72.e84516) Calamaria arcana: holotype eye diameter 1.4 mm, running text (quote cut and marked). Search: '"Vertebrate Zoology" 74 OR 75 OR 72 OR 71 "a new species of" Senckenberg Gesellschaft für Naturforschung herpetology description' (XML link).
- Biodiversity Data Journal 12: e136491 (10.3897/BDJ.12.e136491) Leptobrachella huynhi: ED for holotype and 3 paratypes (all female), Table 1 row. Main held only this paper's TD and NS rows (d583). Search: 'Leptobrachella huynhi Hoang Luong Nguyen Lai Chau Biodiversity Data Journal Table 1 measurements ED TD'.
- Vertebrate Zoology 74: 417-433 (10.3897/vz.74.e123251) Amnihyla kikori (Litoria kikori in the paper): EYE and TYM for holotype and the female paratype (Table 1); Amnihyla grinpela: holotype EYE and TYM (text list). ASW names as in d584. Search: exact title plus 'Richards Oliver Vertebrate Zoology'.

## Not filed and why
- Leptobrachella dushanensis (BDJ 12: e113427): Table 3 ED/TYD n = 4 group, but the paper lists three male paratypes and a Figure 4 caption calls MT DS20230310002 female, so sex of the pooled n = 4 is unresolved. Lead if the sexes are settled.
- Seven Nyctibatrachus species (PeerJ 5: e3007, EL in holotype text): peerj.com page reached prints no byline or licence sentence to the reader, and the full text only through PMC (not usable). Lead.
- Luperosaurus alvarezi (PeerJ 14: e20504), Nyctibatrachus kali (PeerJ 14: e20895), Leptobrachium mechuka/somani (PeerJ 14: e20397): no PeerJ article page reached; earlier desks list them.
- Sphenomorphus lingnanensis (ZSE 102(2): 411-420): no eye measurement in the paper.
- Trimeresurus ciliaris (VZ 73: e109854): on main (d490). Pareas temporalis, Pseudoeurycea jaguar (VZ), Boulenophrys changyangensis, Leptobrachella shimentaina, Megophrys qianbeiensis: XML read stopped before the description or no eye values in the part read.
- Acta Herpetologica, Zoological Research, Check List queries returned only Plazi, Zenodo, PMC and torrossa links; nothing fileable.

## Weak spots
- Text came through the WebFetch page reader (Arpha XML and article preview pages); table cells arrive flattened and the Litoria kikori Table 1 columns were mapped from a two-line header (eighth specimen is an uncatalogued PNGNM specimen).
- Neither Amphibian Species of the World nor the Reptile Database prints an explicit word 'valid'. Crossref not used.

## Desk disposition after audits 1198, 1199, 1200 (4 November 2026)
All 12 records merged. Counted errors: 6 (audit 1200: 6 fixable lines; audits 1198 and 1199: 0 record errors, wording faults only). The auditors' replacement text was applied.
- Audit 1200 (Amnihyla kikori and grinpela, Vertebrate Zoology 74:417-433): the page reader had inserted abbreviation expansions into the quotes ("EYE (horizontal diameter of eye)" where the paper prints "EYE 4.4"), the Methods entries were misquoted, the instrument claim "unstated" was false (EYE and TYM are in the dissecting-microscope list), and Table 1 has one 15-cell header row, not two lines. The values, column mapping and the female paratype R72337 (named in the header, Sex F) are correct. ASW names used (the paper says Litoria kikori and Litoria grinpela).
- Audit 1198: Oreophryne chlorops voucher is MZB.Amph.32875 and no paratypes exist; Calamaria arcana "eye diameter" had been mislabelled EyeD; Reptile Database synonym line added.
- Audit 1199: Leptobrachella huynhi (4 females; main had TD and NS from d583, no ED); the Variation section is under Notes, not Description.
- Open leads (not filed): Leptobrachella dushanensis BDJ 12:e113427 (pooled n=4 group of unresolved sex), seven Nyctibatrachus species PeerJ 5:e3007 (no licence sentence seen, full text only on PMC).
