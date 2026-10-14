# Recheck 1, 14 October 2026 (sweep-21 and sweep-25)

Every source URL was opened with WebFetch (the fetcher returns a summary, so quotes were checked by asking for the exact string and the nearest verbatim sentence). Corrections are in `docs/views/evidence/recheck-1.jsonl` (fields `supersedes`, `action`, `reason`); the original files are untouched. No page was blocked (the 25:11 DOI redirected and was read at a Cambridge mirror).

Result: 28 records, 14 correct, 14 corrected (9 requote, 3 retract, 1 regrade, 1 retarget), 0 unverifiable.

| id | taxon / trait | verdict | note |
|---|---|---|---|
| sweep-21:1 | Platanthera bifolia sense_chemical | requote | stitched two sentences, added a comma; benzoates at other sites not on page |
| sweep-21:2 | P. bifolia diel | retract | "collected during the night" is a sampling time |
| sweep-21:3 | Phleum pratense light | correct | quote verbatim; 12 h/20 h photoperiod values confirmed |
| sweep-21:4 | Manduca sexta interommatidial | retarget | table is on PMC, not the Adelaide page; 0.96 deg confirmed; quote had "n = 4" and "+/-" added |
| sweep-21:5 | Manduca sexta interommatidial | correct | verbatim; 1.24 in Table 1, units not stated, preprint |
| sweep-21:6 | Manduca sexta acuity | requote | quote did not contain the 0.08 to 0.3 cycles/degree range; the grade stays m but it is a response band, not a cutoff |
| sweep-21:7 | Dryas octopetala light | requote | quote was the title; "2 to 3 C" should be 1.1 to 3.2 C above air |
| sweep-21:8 | Dryas octopetala diel | requote | quote was a keyword; abstract sentence supplies the value |
| sweep-21:9 | Rynchops niger binocular | requote | quote did not support 5 degrees |
| sweep-21:10 | Sarracenia purpurea chemical | retract | page never says S. purpurea scent is fatty-acid derivatives; limonene absent |
| sweep-21:11 | Galanthus nivalis chemical | requote | quote verbatim but too general for osmophore value |
| sweep-21:12 | Silybum marianum light | correct | verbatim |
| sweep-21:13 | Origanum vulgare diel | retract | dried oil by harvest time, minor effect; no diel rhythm shown |
| sweep-21:14 | Nymphaea nouchali diel | correct | verbatim, 7:00 to 23:00 |
| sweep-21:15 | Nymphaea 'Blue Bird' diel | correct | verbatim; cultivar named in methods, not abstract |
| sweep-21:16 | Lepidium draba light | correct | verbatim (as Cardaria draba, 2011) |
| sweep-21:17 | Sisymbrium officinale light | correct | quote is the title, which also names light; no abstract on page (Hilhorst and Karssen 1989) |
| sweep-25:1 | Hermetia illucens spectral | correct | verbatim; thesis by Volk 2018, no nm peaks, as logged |
| sweep-25:2 | Tradescantia ohiensis diel | correct | verbatim |
| sweep-25:3 | Osmia rufa spectral | correct | quote and 348/436/572 nm confirmed |
| sweep-25:4 | Xanthium strumarium light | requote | page says "no germination occurred in darkness" |
| sweep-25:5 | Meliphagidae spectral | regrade m to g | family-level, second-hand (Burd et al. 2014); SWS1 and hummingbird text not on page |
| sweep-25:6 | Tridax procumbens light | correct | verbatim; Tridax is "coat buttons" in the abstract, 76% confirmed |
| sweep-25:7 | Sphagneticola trilobata light | requote | page reads "were stronger" |
| sweep-25:8 | Marrubium vulgare light | correct | verbatim; 100% in alternating light/dark or darkness |
| sweep-25:9 | Silphium laciniatum light | correct | verbatim apart from the capital T |
| sweep-25:10 | Lycopus europaeus light | correct | verbatim; Thompson 1970, 6.5 C confirmed |
| sweep-25:11 | Elymus repens light | requote | page says "elongated to differentiate an inflorescence when exposed to a photoperiod of 14 h or longer" (Majek et al. 1984) |
