# desk-d81 progress (Mediterranean, Macaronesian and Middle Eastern natives)

Started and finished 29 October 2026. Branch research/desk-d81. About 30 WebSearch calls used. No search records and no wanted lines were written (no trait protocol was completed for a genus).

## Filed (8 records, docs/views/evidence/desk-d81.jsonl, all sense_light_nonvisual, grade m, read from open full text)
All eight come from the open "Mediterranean plant germination reports" series in Flora Mediterranea (the journal prints no issue number). Each report carries one DOI and the PDF prints no per-entry DOI; Crossref lists no authors for report 5, so the authors are the entry authors as printed in the PDF.
- Lythrum hyssopifolia, report 7, entry 160: Di Stefano M, Cristaudo A, Flora Mediterranea 35: 271-291 (2025), DOI 10.7320/FlMedit35.271. GBIF species 3188747 opened, ACCEPTED.
- Lythrum borysthenicum (printed in the paper as Middendorfia borysthenica), report 7, entry 161, same citation. GBIF species 7892122 opened, ACCEPTED; GBIF name match returns Middendorfia borysthenica as its synonym; a WFO list page (wfo-0000366761) shows the same equivalence. POWO could not be opened, so audit 168's POWO test is not met; the desk may hold this record out.
- Myosotis sicula, entry 162, same citation. GBIF 5660719 opened, ACCEPTED.
- Antinoria insularis (Poaceae), entry 159, same citation. GBIF 4133143 opened, ACCEPTED. One figure (82% peak) in the conditions line was read through a summary of a 127-character sentence.
- Dianthus graminifolius, entry 164: Scafidi F, Mazzara Curcurù G, Pipitone G, same report. GBIF 7698339 opened, ACCEPTED.
- Senecio leucanthemifolius, report 6, entry 133: Di Paola AI, Blandino C, Emma G, Di Stefano M, Cristaudo A, Flora Mediterranea 34: 159-194 (2024), DOI 10.7320/FlMedit34.159. GBIF 7624085 opened, ACCEPTED. The >=85% light-only figure is from a 189-character sentence read through a summary.
- Silene nefelites, report 5, entry 120: Scafidi F, Salmeri C, Flora Mediterranea 33: 279-297 (2023), DOI 10.7320/FlMedit33.279. GBIF 7637268 opened, ACCEPTED. Exact alternating regime for this taxon not read.
- Dianthus borbonicus, report 5, entry 117, same citation. GBIF 8602057 opened, ACCEPTED.
The quotes are verbatim whole sentences of 74 to 110 characters. Verbatim wording was confirmed through WebFetch of the PDFs (the summariser would not return long passages; short sentences were returned with character counts). Full-text pdftotext check was not possible: curl to herbmedit.org is refused by the proxy.

## Held out
- Gairola and El-Keblawy 2019 (Plant Biosystems 154(5): 635-642, DOI 10.1080/11263504.2019.1674397; Reseda aucheri, Oligomeris linifolia, Ochradenus arabicus, O. aucheri, O. baccatus): every GA3 and light-versus-dark sentence names two or more species.
- Pedicularis olympica GA3 (Kirmizi et al. 2010, Turkish J Bot 34(3), DOI 10.3906/bot-0912-287): already on main (desk-d63).
- Cyclamen alpinum darkness germination (Bürün and Şahin 2009, Turk J Bot 33: 277-283, DOI 10.3906/bot-0709-8): the only darkness sentence is 279 characters.
- Linum olympicum GA3 and darkness (Kirmizi et al. 2018, Horticulture, Environment, and Biotechnology 59(5): 629-635; no DOI on the page): journal is horticultural, outside the vein.
- Rhamnus alaternus shade (Miralles et al. 2011, Scientia Horticulturae 127(4): 562-570, DOI 10.1016/j.scienta.2010.12.005): horticultural journal, abstract sentences long.
- Eruca sativa photo-thermal germination (Barazani et al. 2012, J Arid Environments 85: 93-96, DOI 10.1016/j.jaridenv.2012.06.011): all result sentences long, desert journal.
- Isoplexis isabelliana seed-bank viability (Mediterranean Botany 42, DOI 10.5209/mbot.69341): storage viability, no light or chemical trial reported as a result of the species.
- Linaria pseudolaxiflora GA3 (Flora Mediterranea 34, entry 135): the GA3 result sentences are 138 and 193 characters.
- Matthiola incana subsp. rupestris, Hyoseris lucida subsp. taurina, Helichrysum panormitanum subsp. latifolium (subspecies); Silene kemoniana (result sentences 239 and 282 characters); Glaucium flavum, Sideritis chamaedryfolia (entries in reports 7; not opened in full).

## Not yet mined (leads for a later unit)
Flora Mediterranea reports 3, 4 (FL31 283-290, FL32 207-219, FL32 220-226, FL34 entries 121 to 149, FL35 entries 150 to 163 and 165 to 166) hold more single-taxon light and GA3 sentences; Glaucium flavum (entry 150: light germination reduced to 33% at 25/10 C and 9.6% at 15 C) and Sideritis chamaedryfolia (entry 151: enhanced germination in the dark) have short whole sentences.

## Blocked
api.crossref.org and herbmedit.org via curl (proxy 403; WebFetch worked), herbmedit.org/papers pages (PROVENANCE_REQUIRED), scispace.com, digital.csic.es (Anubis), acikerisim.omu.edu.tr (Anubis), tandfonline.com, aminer.org, peeref.com (login), POWO search API, list.worldfloraonline.org/wfo-0000745271.

## Desk disposition after audit 171

Audit 171 judged all 8 records correct (0 of 8 errors) and the desk merged all eight (Lythrum hyssopifolia, Lythrum borysthenicum, Myosotis sicula, Antinoria insularis, Dianthus graminifolius, Senecio leucanthemifolius, Silene nefelites, Dianthus borbonicus), all from the open-access Flora Mediterranea germination reports 5 to 7. Wording fault fixed before merging: the `where` field of lines 7 and 8 (Silene nefelites, Dianthus borbonicus; report 5) named herbmedit.org, but the PDF was opened at the University of Palermo open repository, iris.unipa.it; the desk changed it to iris.unipa.it. Middendorfia borysthenica is a synonym of Lythrum borysthenicum (GBIF and WFO), and GBIF 7892122 is the accepted species' own id.
