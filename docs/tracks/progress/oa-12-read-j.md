# oa-12 reading pass, reader J (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md` on `main`, with the launch prompt's rules (quotes of at most 40 words, cuts marked " … " inside one sentence only, `oa_lint.py --text` before each commit). Entries 9, 17, 18, 25, 51, 63, 65, 69, 72 and 73 of `oa-12`, in that order. Texts: the control room's decrypted copies in `/tmp/oa-shared/oa-12/oa-12-<entry>.txt` (on the control room's instruction no run branch was pushed). Reading branch: `agent/oa-read-j`.

## Counts so far

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 9 | Childs et al. 1997, sorghum Ma3 encodes phytochrome B (Plant Physiol 113: 611-619) | abstract only (PubMed Central landing page) | 3 | 3 | 0 | 0 | 3 |
| 17 | Ikegami et al. 2013, FcFT1 in fig (BMC Plant Biol 13: 216) | Europe PMC full-text XML, published version | 8 | 7 | 1 | 0 | 3 |

## Notes by paper

- Entry 9, not read in full. The job's text is the PubMed Central landing page: the abstract and a selected reference list. The full text is a 1.5 MB scanned PDF that did not come through. Three abstract values for Sorghum bicolor logged with `partial: true` and `access` "abstract" (the one change to the copied source object): Ma3 is a PHYB gene encoding a 123-kD phytochrome (frameshift in ma3), Ma3 is one of six genes regulating photoperiod sensitivity of flowering, and the 123-kD phytochrome predominates in light-grown plants. No line in `docs/views/sources/oa-12.jsonl`, so the paper stays wanted.
- Entry 17. Ficus carica, own measurements (`m`): leaf FcFT1 expression rises under 16L/8D and under 8L/16D (two records), peaking 12 h after lights on, and stays low in continuous darkness; expression rises immediately with light and is higher with more light. `g`: light-responsive promoter elements, predicted from sequence. Cited in the Discussion, `m` and `partial`: shading (Matsuura and Araki 1995) and day-length and light-intensity effects on fruit bearing (Teragishi et al. 1998, two papers). Not logged: seasonal expression (May to October, not a light response as measured), organ and node expression, and the transgenic tobacco flowering times (Table 1), which describe tobacco carrying the fig gene.
