# desk-d68 progress (fire-prone flora germination, single-species titles)

Started 29 October 2026. Branch research/desk-d68. WebSearch used: about 62 of 100. All five records are abstract-only (partial true). Each accepted name was read on a POWO, WFO or GBIF page opened in this session, and each cited id belongs to the accepted name.

## Filed (5 records, docs/views/evidence/desk-d68.jsonl)
- Arbutus unedo, GA3 and stratification (Demirsoy et al. 2010, Horticultural Science 37(1); sentence matched on the journal page and ideas.repec; the page prints "GA GA3" and the quote copies it).
- Lavandula stoechas, germination in light versus dark (Maher et al. 2000, Acta Horticulturae 541: 261-264; a different study from the plb.13329 record on main).
- Helichrysum amorginum, light enhanced germination (Argyriou et al. 2020, Bulletin UASVM Horticulture 77(1); WFO accepted; the header prints the DOI with a space, so the record carries the journal URL only).
- Chamaescilla corymbosa, scarification then smoke water (Allan et al. 2004, Aust J Bot 52(3): 345-351; the title prints the genus as "Chameascilla").
- Nicotiana attenuata, syringaldehyde as smoke germination cue (Cao et al. 2021, Seed Sci Res 31(4); GBIF accepted).

## Wanted lines (docs/views/wanted/desk-d68.jsonl, 5)
Schwachtje and Baldwin 2004 and Krock et al. 2002 (N. attenuata, all abstract sentences over 125 characters), Skordilis and Thanos 1995 (Pinus brutia far-red), Plummer and Bell 1995 (Rhodanthe humboldtiana), Ainsley et al. 2008 (Prostanthera eurybioides).

## Held out
- Rhodanthe humboldtiana (110-character GA3 inhibition sentence) and Prostanthera eurybioides ("Smoked water inhibited germination."): no POWO, WFO or GBIF page confirming Accepted could be opened (WFO and POWO pages were blocked or timed out).
- Cistus ladanifer (Dias 2019), Cistus creticus GA3 (Pela 2000, 87-character sentence about 13% germination with no comparison, not a direction), Chrysanthemoides monilifera subsp. (subspecies), Satureja thymbra (heat plus GA3 combined with salinity), Brunonia australis and Rhodanthe floribunda (sentences over 125 or no DOI), Erica australis (one 196-character sentence), Phillyrea latifolia (Bosque, no DOI, sentences over 125).
- Thesis and non-peer-reviewed leads (Tree Seeds 2002 Pinus pinaster proceedings with no authors, Cal Poly and Evergreen theses) not filed.
- Pooled papers not usable for a single species: Keeley and Fotheringham 1998 (two species), Tieu 1999, Norman 2006, Çatav 2012 and 2021, Thomas 2003, Enright and Kintrup 2001.
- Blocked or unreadable: x-mol (verification wall), peeref (login), idus and omu repositories (Anubis), crossref API (denied by the tool classifier), a 403 on direct curl to ishs.org.

## Advice
Acta Horticulturae pages on ishs.org print the abstract with each sentence short enough to quote; ask WebFetch to print a named sentence with its count and re-check on a second page. Fire-flora single-species titles from CSIRO, J-STAGE or open journals usually pool several species in one abstract, so the sentence has to name the species.
