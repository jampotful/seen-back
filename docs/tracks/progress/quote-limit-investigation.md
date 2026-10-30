# Evidence quotation limit investigation, 28 October 2026

Base: `5bfa70884640ba0ba967ef5736f3cc97a23b9452`. No open matching quote-limit PR or 125-character issue was returned by the repository searches at investigation time.

## Finding and origin

The repository evidence rule is **40 whitespace-separated words**, not 125 characters. `tools/senses/check.py:problems` checks `len(q.split()) > MAX_QUOTE_WORDS`; `addlog.py` uses that same function. Neither imposes a character cap. `quotecheck.py` checks source matches, not maximum quote length; it does not certify sentence boundaries, subject attribution or scientific support. BRIEF's evidence example and its public-repository quotation guidance both specify 40 words.

The earliest explicit explanation located in the checked-out documents is [audit 4](audit-4.md), opening paragraph and closing point 2. It calls 125 characters the **fetch summariser's cap per quoted piece**, and describes consecutive pieces being reassembled. The GitHub path history attributes that report to [commit 712f353e](https://github.com/jampotful/seen-back/commit/712f353e716c08af43c996c4d10fa86c2b7728cb), 14 October. Audits 5–11 repeat this retrieval explanation while retaining the 40-word record limit.

By 28 October, [audit 118](audit-118.md), evidence verdict 1, explicitly concludes that a sentence exceeding 125 characters cannot yield a compliant quote; its history points to [ede3e407](https://github.com/jampotful/seen-back/commit/ede3e407d26986093faa181d85c25a50705b227c). The objection to turning a clause into a sentence there remains valid. The inference from sentence character length to unusable evidence does not. Audits 111 and 116, desk-d32 and desk-d34, and other reports repeat the character-based exclusions. Historical reports remain as the record of those decisions, not current authority for quote length.

Searches across instructions, research documents, tools, CI and progress reports found no separate scientific, legal or publication requirement for 125 characters. The available repository evidence identifies an external tool output constraint that spread into desk/audit practice. This investigation did not inspect the original WebFetch runtime or establish the provider's underlying rationale; it does not override that tool's restrictions or make a legal determination. The correction directs readers to legal source retrieval, not requests for pieces to evade a cap. Public source access and the existing 40-word publication limit remain required.

## Named examples checked against sources

Counts below use Python `len(q)` and `len(q.split())` on the exact stored passages. All six candidate/recovered records pass the actual record validator, including the three held candidates; passing it alone does not admit evidence.

| Taxon and passage | Characters | Words | Scientific reading and disposition |
|---|---:|---:|---|
| Epacris tasmanica, abstract null result without heat shock | 128 | 20 | Original publisher abstract supports a null effect of darkness and smoked-water treatments **in the absence of heat shock**. It does not establish general light insensitivity. Candidate held for source-text verification. |
| Scilla paui, English Summary darkness result | 129 | 22 | 100% germination after eight weeks at 5°C and four weeks at 15/4°C in darkness. This is not by itself a light/dark effect or an obligate darkness requirement. Candidate held. |
| Scilla paui, English Summary gibberellic-acid result | 153 | 23 | Supports qualitative promotion and the authors' dormancy classification, not a numerical treatment benefit. Candidate held. |
| Melilotus suaveolens, Results light sensitivity | 182 | 28 | Germination differs among 0, 15 and 62.5 µmol m−2 s−1 treatments. The sentence also names C. microphylla; the record logs only M. suaveolens. Recovered with full sentence. |
| Toxicodendron vernicifluum, Results GA3 comparison | 162 | 26 | 7.8 ± 5.0% versus mock 2.7 ± 1.1%; **not statistically different**. Recovered with that qualification intact. |
| Toxicodendron vernicifluum, Results GA4 comparison | 218 | 34 | Significant promotion, 22.2 ± 9.8%; full sentence retained, including authors' approximate-fold wording and figure citation. Recovered. |

The reported ~135-character shortest Toxicodendron sentence was not needed: the directly checked 162-character GA3 and 218-character GA4 sentences both fit under 40 words. No quotation was shortened, reconstructed from summariser pieces, translated or given manufactured punctuation. There are no ellipses in the final recovered/candidate quotations.

The recovered records are in `docs/views/evidence/quote-limit-recovery.jsonl`. Doses, temperatures, light regimes, durations, replication and source locations are in each record. The Toxicodendron Results text points to Fig 2A, while its caption identifies the GA comparison as Fig 2C; the records explicitly preserve this discrepancy. They retain ± terms without inventing an error-bar definition. Main had an Epacris **smoke** record in sweep-96, but no duplicate of these recovered records was found. No older evidence or audit verdict is automatically reinstated.

## Source provenance and remaining retrieval gaps

Sources opened on 28 October 2026:

- Gilmour, Crowden and Koutoulis (2000), *Australian Journal of Botany* 48(5): 603–609, [10.1071/BT99029](https://doi.org/10.1071/BT99029). Publisher abstract inspected at ConnectSci. Full paper was access restricted. Direct abstract HTML retrieval returned 403. Only the 20-word null-result sentence is retained as a candidate, with `access: abstract` and `partial: true`.
- Santiago, Herranz, Copete, Herranz and Ferrandis (2017), *Bosque* 38(2): 271–283, [10.4067/S0717-92002017000200005](https://doi.org/10.4067/S0717-92002017000200005). English Summary compared on SciELO and the journal page; Spanish Methods and Results inspected on [SciELO](https://www.scielo.cl/scielo.php?pid=S0717-92002017000200005&script=sci_arttext). Methods specify 1000 mg L−1 GA3, 20/7°C, light/dark trials, sampling at four, eight and twelve weeks. These design details are not silently substituted into the abstract's result. Direct SciELO HTML/PDF and journal-page downloads returned 403. The journal's PDF viewer returned unrelated material through web retrieval and was not used. Both abstract candidates remain `partial: true`.
- Lai, Chen, Jiang, Zhou, Zheng and Shimizu (2016), *AoB PLANTS* 8: plw031, [10.1093/aobpla/plw031](https://doi.org/10.1093/aobpla/plw031). Publisher Methods/Results inspected; published XML downloaded from [Europe PMC fullTextXML, PMC4940479](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4940479/fullTextXML). Article metadata supplies complete authors and CC BY 4.0 license. Paragraph text extracted with `''.join(p.itertext())`, whitespace collapsed, one paragraph per line. Targeted Methods/Results review, not a claim of whole-paper OA-pass completion.
- Nemoto, Watanabe, Yoshida and Nishihara (2022), *PLOS ONE* 17(8): e0272665, [publisher article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0272665). Public HTML downloaded; article identifies CC BY. Text extracted with Python's HTMLParser, retaining inline text adjacency and placing block boundaries on separate lines; scripts/styles omitted and whitespace collapsed. Targeted Methods/Results/caption review.

Paper HTML/XML and derived full text stayed outside the repository. SHA-256 fingerprints of the successful downloads and derived check inputs:

| Input | SHA-256 |
|---|---|
| PLOS HTML | `eb8c72ee2b541e68d63e331f8446934b06e5befd08d0d1df2d470d7dafbaf287` |
| PLOS extracted text | `73ef95bcc60b63bc709e88d8624645cf7a6afd6571109c017cd1d0c7639bfb7a` |
| Europe PMC XML | `5ae1e3af21427d5a6f760b79069af5fb91811a0814aff3f2578b8b0804b84232` |
| Europe PMC paragraph text | `2fd8d561d04be7f15470e6ddba66f590faf43e4bf1e593634a3e69e142a71ef1` |

`docs/views/drafts/quote-limit-candidates.jsonl` retains three fully attributed candidate observations for Epacris and Scilla outside the evidence directory. They are not mechanically source-verified or counted as recovered evidence. Next: obtain the legal source text or abstract via a permitted route (the existing encrypted OA workflow is available), run quotecheck, review taxon/conditions again, and only then admit them. A download failure is not a negative biological finding. No question for the owner is needed to preserve these candidates.

## Focused correction and validation

BRIEF, oa-read and desk-audit now explicitly distinguish the 40-word evidence rule from tool output limits and preserve quotation/scientific standards. `check.py` gains only explanatory comments; its validation behavior is unchanged. `tools/senses/test_quote_limit.py` exercises a real complete 162-character/26-word Results sentence through the validator, addlog and checker CLIs in a disposable layout. It also verifies the 40/41-word boundary, irregular whitespace, rejection without append, empty quotes, source requirements, opened status and grades.

Validation:

- `python3 -I tools/senses/test_quote_limit.py`: 4 tests pass, offline.
- `python3 -I tools/senses/check.py docs/views/evidence/quote-limit-recovery.jsonl docs/views/drafts/quote-limit-candidates.jsonl`: 3 + 3 records, zero problems.
- `quotecheck.py` against the downloaded PLOS extraction: 2 verbatim, zero failed; against Europe PMC extraction: 1 verbatim, zero failed. These were actual source texts, not fixture text copied from the records. The held candidates were deliberately not checked against a self-constructed source.
- Repository-wide checker: nine existing missing DOI/URL problems, intake-4-failed lines 2–7 and intake-5-failed lines 1–3. The base checker against the same inputs reports those identical nine problems; no new problem.
- `git diff --check` passes. No app build, paid extraction, coverage regeneration, source-paper upload or main-branch merge is part of this change.

This fixes the demonstrated instruction/practice mismatch. Wider revisiting of other character-rejected leads remains separate source-review work; none is automatically accepted by this change.
