# desk-d625 progress

Angle: tympanum diameter columns of older frog papers already audited on main (eye_diameter_mm rows from units d340-d619 with no tympanum row for the same species and DOI); the OLD-ANGLE paragraph (reptiles and fish) was not followed. 31 records (log docs/views/evidence/desk-d625.jsonl), unit field desk-d625, evidence_kind anatomical_measurement, shaped on desk-d623 and desk-d624. check.py: 0 problems for this file (plain and --require-evidence-kind). 35 WebSearches. Every paper was reached through an own unfiltered search (exact title or species plus journal), the Pensoft/arphahub article_preview page read through WebFetch, the licence sentence read in three pieces (CC BY 4.0), the ASW page opened from an own search result and its comment read for splits.

Step 1: 41 DOIs on main carry amphibian eye_diameter_mm rows with no tympanum row for the same species and DOI (list built in an untracked scratch folder).

## Filed
- Ingerophrynus chrysolophus, Herpetozoa 38: 271-297 (10.3897/herpetozoa.38.e165173): TD for the nine type specimens (9 records; second column block of Table 1, same specimens as the desk-d484 ED rows).
- Pristimantis nebulosus, ZSE 98(2): 213-232 (10.3897/zse.98.84963): TD row of Table 1, four columns (holotype ZFMK 27643 as printed, topotypes MUSM 40298, 40299, 40326) (4 records; ED rows d602).
- Pristimantis gretathunbergae, ZooKeys 1081: 1-34 (10.3897/zookeys.1081.63009): holotype TY from the holotype list sentence (cut after TY) and the TY row of Table 2 for adult females (mean, n = 2) and adult males (mean, n = 7) (3 records).
- Ansonia karen, Vertebrate Zoology 71: 763-779 (10.3897/vz.71.e73529): VTD column of Table 1 for 15 type specimens (AUP-00664 not filed, VTD cell printed '1,51'); the Table 1 column 'TD' is not filed because the Methods define VTD and HTD but never 'TD'.

## Weak spots
- Every cell and column-to-specimen mapping is the WebFetch page reader's cell-by-cell reading of the Pensoft/arphahub preview; the reader expands abbreviations in row labels (marked as expansions in the notes, not quoted). Ingerophrynus and Ansonia headers and rows were read twice and agreed; for Ansonia the reader refused a one-shot dump of the whole table and the rows came in two passes.
- Ansonia paratype paragraph read in pieces and joined in the conditions; Ingerophrynus, Pristimantis nebulosus and gretathunbergae summary rows share one table row between columns/sexes (specimen or sex column named in the record).
- Pristimantis gretathunbergae females: mean of n = 2.

## Not filed and why
- No tympanum measurement defined or tabulated: Occidozyga nishikawai, Brachycephalus herculeus, Pristimantis vrazi (TY only in running text, undefined in Methods), Rhombophryne ellae (TDH/TDV only in the holotype prose list), R. longicrus (TDH/TDV only in running text with paratype in brackets), Pristimantis ruidus, Rhinella kumanday, Oreophryne chlorops (tympanum could not be measured), Scutiger khumbu, Noblella thiuni (TY defined, no value), Phrynopus remotum, Osornophryne backshalli, Physalaemus araxa, Pseudopaludicola coracoralinae.
- Platypelis ando: TD column defined but every cell reads 'NA'.
- Pristimantis paganus (PeerJ 20512): holotype list prints 'TD = 1.51' but the Methods define no TD (only a Duellman and Lehr citation); held out.
- Unreachable: Gracixalus damingshanensis, Brachytarsophrys guilinensis (megophryid, tympanum likely absent), Stumpffia lynnae: Pensoft pages returned 'Site under maintenance' late in the unit.
- Pristimantis pulchridormientes: only a zenodo repository copy and PMC reached; not opened.
- Dead as briefed: Zootaxa, Phyllomedusa, salamander and other non-frog DOIs, the d623 and d624 papers.

## Desk disposition after audits (4 November 2026)
Five audits (1280-1284) judged all 31 lines: 0 value errors. Pensoft and Herpetozoa pages went into maintenance during the audits, so some auditors could not read the whole licence sentence, byline or type paragraph. Merged (12): Pristimantis nebulosus x4 (lines 10-13; holotype ZFMK 27643 in the table vs 27634 in the text kept with the conflict disclosed), P. gretathunbergae x3 (14-16; the two means pool specimens the table does not identify, an owner question on pooled records) and Ansonia karen x5 (17-21), with the auditors' replacement text. HELD OUT unmerged, not counted as errors, pending a re-read once the pages return: Ingerophrynus chrysolophus x9 (lines 1-9; licence sentence and Methods TD item unread, plus faults found: Table 1 is under Materials and methods, three column blocks not two, Cyrillic с in the caption) and Ansonia karen x10 (lines 22-31; licence sentence, byline and paratype paragraph unverified by audits 1283 and 1284; audit 1282 read the licence as CC BY 4.0 for lines 17-21 before the outage and found the paratype text shortened). The auditors' corrected replacement lines for all 31 are in audit-1280 to audit-1284 on their branches.
