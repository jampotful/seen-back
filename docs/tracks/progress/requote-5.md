# Requote chunk 5 (recheck-45)

Work list: `docs/views/repair/chunks/chunk-5.jsonl`, 97 lines. Output: `docs/views/recheck/recheck-45.jsonl`.

Counts: fixed 74, retracted 0, table rows 8, unfixed 15.

Method: sentences were read from open pages (Vision Research via the NSF PAR copy, Endangered Species Research via the BMIS bycatch PDF, Molecular Biology and Evolution via the UCL repository PDF, Utah State thesis, MDPI, Frontiers, the Giresun copy of the Turkish J Agric For paper, the Trinity College Dublin copy of Healy et al., PLoS ONE via the PubAnnotation render of the PMC text). The fetch tool returned each sentence in pieces; the pieces were joined and the first and last words checked. Quotes longer than 40 words are clause-bounded excerpts with the cut marked by an ellipsis and described in `where`.

Notes for the desk:
- oa-1:8655 to 8658: two mirrors of the Current Biology abstract differ on "light averse" against "light-averse"; the unhyphenated form was used.
- oa-1:8651, 8652 and 8654 keep the bracketed reference numbers the PMC text prints.
- oa-2:9712 and 9713 end in an ellipsis because the sentence continues with a second species and the authors' molecular studies.
- oa-6:1043 is a clause-bounded excerpt (the full sentence runs to 44 words).
- harvest-c1:61 was already a complete sentence with the full stop missing.

## Table rows (no row written)
oa-9:2135, oa-9:2136, oa-9:2137, oa-9:2138, oa-9:2139, oa-9:2140, oa-9:2141, oa-9:2142 (rows of Tables 1 and 2 of the loggerhead and leatherback paper).

## Unfixed
- oa-1:10716 to 10722, 10724 to 10727 (11 lines): Royal Society Open Science full text (doi 10.1098/rsos.252149) not reachable; only the Adelaide repository record and abstract opened.
- oa-1:7405, oa-1:7406: PNAS 2014 article (doi 10.1073/pnas.1401871111) open only through PMC, which returned a browser check page.
- harvest-c1:20: Plant Cell Environ review (doi 10.1111/pce.13912), PMC copy blocked and no other open copy surfaced.
- harvest-c3:80: Weed Science 1952 (doi 10.1017/S0043174500079558), Cambridge page not permitted by the fetch tool.
