# desk-d494 progress

Angle: reptiles and fish by issue-by-issue search (no spiders). 12 records (log docs/views/evidence/desk-d494.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for this file (plain and --require-evidence-kind). About 40 WebSearches.

## Filed
- Vertebrate Zoology 75: 627-672 (10.3897/vz.75.e167366) Ichnotropis robusta (Lacertidae): holotype PEM R23420 and 4 paratypes, ED row of the type-series measurement table (CSV download); Methods define ED and give mm; Reptile Database page opened (types line agrees with the table's Type status and Sex rows).
- Herpetozoa 39: 291-302 (10.3897/herpetozoa.39.e202590) Boulenophrys calciphila (Megophryidae): holotype GEP a596 and 6 paratypes, Table 2 ED row (caption prints mm); ASW page opened.

## Weak spots
- Ichnotropis robusta: the article preview and XML text stop before the taxonomic section, so the table number, caption and heading path were not seen. The unit comes from the Methods sentence. The paratype PEM R23482 prints ED 3.8, an outlier against 2.9-3.1 for the rest (printed value, noted in each record). Licence phrase only partly returned.
- Boulenophrys calciphila: XML omits Table 2; the preview supplied it. ASW cites p. 293, the article prints 291-302.

## Not filed and why
- Cyrtodactylus shenbagathoppuensis and C. kalakadensis (Vertebrate Zoology 76, 10.3897/vz.76.e192746, CC BY 4.0): Table 4 prints ED for holotypes and paratypes with ED defined, but no Reptile Database page in two searches (July 2026 species); satpuraensis rows not returned. Lead if a page appears.
- Ovophis langbianus (Herpetozoa 39: 325-342): ED defined nowhere (holotype ED 2.36 only in text). Dasypeltis albigularis: no ED. Acanthosaura aurantiogularis, Hebius yangi, Calamaria similis, C. incredibilis: already examined by earlier units.
- Ichnotropis longicorpa: Reptile Database page opened (holotype PEM R23410), no measurement table reached; Table 3 of that paper has ranges without specimen codes.
- Luperosaurus alvarezi (PeerJ e20504): Reptile Database page opened again, no PeerJ page in results. Sphenomorphus tophus: on main (oa-13a).
- Fish (Pensoft CSV tables for Johnius javaensis, Pareuchiloglanis-type and cyprinid tables in ZSE): eye diameter only as % SL or % HL, or already dead.
- Charadrahyla (Herpetozoa 184954), Hemidactylus Odisha (175753): not opened.
- Pensoft preview of Herpetozoa 206094 returned the Dasypeltis paper (wrong paper); the XML gave the right one.

## Desk disposition after audits 983-984 (3 November 2026)
- Audit 984 (lines 6-12, Boulenophrys calciphila): 0 errors, 14 format faults (heading path shortened instead of given as printed; licence sentence cut without a mark). ED values, Table 2 column labels, sexes and type statuses match the article; the ASW page lists the species as valid. Replacements applied.
- Audit 983 (lines 1-5, Ichnotropis robusta, Vertebrate Zoology 75, DOI 10.3897/vz.75.e167366): all five lines held out and dropped (counted as errors). The auditor's searches did not reach the type-series table, so the ED values and the flagged 3.8 for PEM R23482 could not be verified. Authors, title, DOI, Reptile Database validity and absence from main were confirmed. Faults: licence phrase without cut mark; "Taxonomic account" heading in `where` never printed. The corrected lines are in /tmp/m311/audit-983.md. Owner question: a unit that reaches the table (the CSV download of the type-series table) could refile them.
