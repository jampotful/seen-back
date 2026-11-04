# desk-d624 progress

Angle: other sensory columns (tympanum diameter, and the eye-diameter column of one unfiled paper) of frog papers already audited on main and of the unfiled d623 papers; the OLD-ANGLE paragraph (reptiles and fish) was not followed. 122 records (log docs/views/evidence/desk-d624.jsonl), unit field desk-d624, evidence_kind anatomical_measurement, one record per labelled measurement, shaped on desk-d623. check.py: 0 problems for this file (plain and --require-evidence-kind). 39 WebSearches. Every paper was reached through an own unfiltered search (exact title or species plus journal), the Pensoft article_preview page read, the licence sentence read in pieces (CC BY 4.0 everywhere; JoTT: CC BY 4.0 copyright line), the ASW page opened from an own search result and its comment read for splits.

## Filed
- Nidirana guangxiensis, ZooKeys 1059: 35-56 (10.3897/zookeys.1059.68140): Table 4 TD and ED for 19 specimens (38 records; the species was not on main under any trait).
- Gephyromantis angano (4) and G. tahotra (2 comparison specimens), ZSE 93(2): 451-466 (10.3897/zse.93.14906), Table 1 TD cell (ED rows d607/d609).
- Leptobrachella aspera (4, TMP), ZooKeys 995; Amolops dafangensis (3, TYD), ZooKeys 1189; L. kungfu (6, TMP), ZooKeys 1259; Odorrana nagao (5, TD), ZooKeys 1280; L. deocaensis (5, TD), ZooKeys 1267; Odorrana yangi (8, TYD), ZooKeys 1275; Zhangixalus thaoae (3, TYD), ZooKeys 1197; L. xinshaoensis (3, TYD), ZSE 102(1); Boulenophrys changyangensis (4, TYD), ZSE 101(3); Rhacophorus dulongensis (2, TD), ZSE 100(3); B. nebulosa (7, TD), ZSE 101(4); B. calciphila (7, TD), Herpetozoa 39; L. weixinensis (3, TD), ZSE 101(4); Cophixalus rajampatensis (7, TyD), ZSE 91(2); B. dalaolingensis (9 paratypes, TD), ZooKeys 1253.
- Leptobrachella tamdil, JoTT 12(8): 15951-15954: HTD and VTD of MZMU 1631 only (2), as d486 filed only that ED cell.
Each record quotes the whole table row (label and all cells, with range/mean cells where printed), names the specimen by the column read, and states the header, Sex row and type material in conditions.

## Weak spots
- Every cell and column-to-specimen mapping is the WebFetch page reader's cell-by-cell reading of the Pensoft preview; the reader expands abbreviations in row labels (marked as expansions in the notes, not quoted). Where a table was read twice (nebulosa, nagao, thaoae) the cells agreed; the ED row read in the same pass matched the audited ED rows already on main for every paper.
- Several Methods sentences came back in pieces or paraphrased; bylines and licence sentences were re-read verbatim before filing (one byline guessed in a first draft was corrected against the printed names before the commit).
- Cophixalus rajampatensis: TyD cell of MZB 12169 is printed '0..9' (typo), that specimen not filed; values below 10 mm were measured with a microscope micrometer.
- B. dalaolingensis holotype NNUYC 240510: text prints TD 2.5, Table 2 prints 2.7 (conflict noted in d499); holotype TD held out.
- ASW prints different volume numbers for some papers (dalaolingensis 1235 vs 1253; rajampatensis 92 vs 91); the printed volume is used.

## Not filed and why
- Raorchestes jakoid/jadoh (JoTT 17(7)): every TD cell reads 'Indistinct' and the species row labels are misaligned with the specimen codes (the d613 conflict).
- Odontophrynus toledoi: only the MNHN landing page (no full text, PDF link not in own results) reached. Dendropsophus bilobatus: Table 3 absent from the publisher XML and no preview page in own results. Nidirana guangdongensis: only the XML (Table 6 absent). Leptobrachella shimentaina: only a zobodat repository copy. Pristimantis similaris, Odorrana-type leads beyond budget.
- L. dorsospina (ZooKeys 995): table beyond the text the page reader returned.

## Desk disposition after audits (4 November 2026)
Seventeen audits (1263-1279) judged all 122 lines: 0 counted errors, nothing dropped, all merged with the auditors' replacement text (cut marks, heading paths with printed authorities, Methods eye passages, type material read from the pages instead of copied from earlier units, duplicated licence sentences removed). One quote changed at merge (a curly apostrophe printed on the page, G. angano locality). Held out by the unit before audit and left as owner questions: Boulenophrys dalaolingensis holotype (text TD 2.5 vs Table 2 2.7), Cophixalus rajampatensis MZB 12169 (cell printed "0..9"), Raorchestes jakoid/jadoh (TD cells "Indistinct", species labels misaligned with specimen codes). Unreached: Odontophrynus toledoi, Dendropsophus bilobatus, Nidirana guangdongensis, Leptobrachella shimentaina, Pristimantis similaris, L. dorsospina.
