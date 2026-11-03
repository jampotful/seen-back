# desk-d483 progress

Angle: lizards, geckos, snakes and turtles with a Reptile Database page reached from my own searches, plus fish with mm eye diameter. No spiders. 4 records (log docs/views/evidence/desk-d483.jsonl). check.py: 0 problems for this file (plain and --require-evidence-kind). About 38 WebSearches.

## Filed
- Evolutionary Systematics 9(2): 221-228 (10.3897/evolsyst.9.170645) Lycodon irwini (Colubridae): holotype DOSMB 05114, Table 1 row 'Eye dia' 3.09; Methods define no eye dimension, so sensory_anatomy with a note (paratype and referred specimen cells are dashes).
- Zoosystematics and Evolution 101(1): 245-255 (10.3897/zse.101.138964) Hemiphyllodactylus laowozhenensis (Gekkonidae): holotype and 2 paratype males, Table 3 ED row (2.48, 2.42, 2.4); ED defined as greatest horizontal diameter of the eyeball.

## Weak spots
- Text came through the WebFetch page reader (Pensoft XML and article preview); column-to-code mapping is the reader's. The article_preview page for id 138964 returned a different paper (Trimeresurus); the XML download was used.
- Lycodon irwini: Methods say 0.1 mm precision, table prints two decimals; Table 1 caption has no unit. Crossref not checked for either paper. Reptile Database pages for both names opened from search results; neither prints an explicit 'valid'.

## Not filed and why
- Gekko wuzhengjuni (ZSE 102(2) 185568): the Reptile Database page reached is Goniurosaurus wuzhengjuni (a different species, ZSE 102(2) 611-620, Chen et al.); no page for the Gekko name.
- Hemiphyllodactylus pakhaensis (ZooKeys 1268): ED values opened (1.95, 1.83, 2.38, 1.92; ED defined), but no Reptile Database page in my results (only genus-level and other species).
- Trimeresurus liqibini: already on main (d477). Calamaria similis and C. incredibilis (d455), C. hunanensis (d477): on main.
- Plagiopholis yangi, Scincella gigas, Sphenomorphus puhoatensis: no Reptile Database page in results. Luperosaurus alvarezi: RDB page opened, but PeerJ article pages not reachable (fetch failed or blocked); Cyrtodactylus raimonaensis, khambui: Zootaxa, only a third-party PDF.
- Pareas melanops (Zoologia): no ED in text or Table 2. Crossorhombus pescadores (ZooKeys 1273): eye as ratio in HL and % SL. Claea dafangensis: on main. Leptobrachella yachangensis and Boulenophrys yezhongensis: already looked at by d480/d481; yezhongensis prints only sex-group ranges in Table 3 and % HL for the holotype.

## Desk disposition after audit 968 (3 November 2026)
- Audit 968 (lines 1-4): 0 errors, 9 faults (unmarked quote cuts in all four lines; header-row order misdescribed in line 1). Replacements applied; nothing dropped.
- Owner question: Lycodon irwini line 1 stays sensory_anatomy. The Methods define no eye measure and Table 1 prints only "Eye dia" with no unit (mm taken from the Methods caliper sentence). Same open question as label-only evidence elsewhere (eye_diameter_mm vs sensory_anatomy).
