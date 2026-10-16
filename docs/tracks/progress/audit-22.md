# Audit 22: Healy et al. 2013 flicker fusion rows in canon-3

Batch follow-up to audit 21. Source: Healy K, McNally L, Ruxton GD, Cooper N, Jackson AL (2013), Animal Behaviour 86(4):685-696, doi 10.1016/j.anbehav.2013.06.018, Table 1, read in the TARA accepted manuscript (https://www.tara.tcd.ie/bitstreams/05b77346-ed5e-4c03-9040-cc63d1773d4f/download, open access). Legend as printed: e = electroretinogram, b = behavioural experiments, o = optimum methodology, s = suboptimum methodology.

Each logged quote was a pipe-separated rebuild of the row. Each is replaced by the printed row (6 to 8 words, under the 40-word cut), and the method field is set from the superscripts. Values were confirmed against the printed CFF cell.

| Record | Species / value | Printed row | Method |
|---|---|---|---|
| canon-3:685 | Anguilla anguilla / 14 | Anguilla anguilla 14b,s,2 71.128 0.0001328 NA L | behavioural experiment, suboptimum |
| canon-3:687 | Asio flammeus / 70 | Asio flammeus 70e,o,4 406.030 0.003228 5.4569 H | electroretinogram, optimum |
| canon-3:688 | Bubo virginianus / 45 | Bubo virginianus 45e,s,5 1450.031 0.003628 13.770 L | electroretinogram, suboptimum |
| canon-3:689 | Canis familiaris / 80 | Canis lupus familiaris 80b,s,6 13900.032 0.0018328 80.071 H | behavioural experiment, suboptimum |
| canon-3:692 | Caretta caretta / 40 | Caretta caretta 40e,s,9 135000.034 0.0000857 2.740 H | electroretinogram, suboptimum |
| canon-3:693 | Cavia porcellus / 50 | Cavia porcellus 50e,s,10 629.035 0.0030635 3.872 L | electroretinogram, suboptimum |
| canon-3:694 | Chelonia mydas / 40 | Chelonia mydas 40e,s,9 128000.036 0.0002536 8.671 H | electroretinogram, suboptimum |
| canon-3:695 | Columba livia / 100 | Columba livia 100e,s,4 315.037 0.004528 2.370 H | electroretinogram, suboptimum |
| canon-3:696 | Dermochelys coriacea / 15 | Dermochelys coriacea 15e,s,11 354000.038 0.0004358 30.073 H | electroretinogram, suboptimum |
| canon-3:697 | Felis catus / 55 | Felis catus 55e,s,12 3054.432 0.0039459 28.471 L | electroretinogram, suboptimum |
| canon-3:698 | Gallus gallus / 87 | Gallus gallus domesticus 87b,o,13 2710.039 0.002228 3.674 H | behavioural experiment, optimum |
| canon-3:699 | Gekko gecko / 20 | Gekko gecko 20e,s,14 54.840 0.0003428 0.275 L | electroretinogram, suboptimum |
| canon-3:700 | Homo sapiens / 60 | Homo sapiens 60b,o,15 67100.041 0.0011760 1300.076 H | behavioural experiment, optimum |
| canon-3:701 | Iguana iguana / 80 | Iguana iguana 80e,s,14 750.042 0.0002928 0.6175 H | electroretinogram, suboptimum |
| canon-3:702 | Macaca mulatta / 95 | Macaca mulatta 95b,o,16 7710.043 0.0020561 91.771 H | behavioural experiment, optimum |
| canon-3:703 | Melopsittacus undulatus / 74.7 | Melopsittacus undulatus 74.7b,s,17 33.628 0.0120428 1.570 H | behavioural experiment, suboptimum |
| canon-3:707 | Pagophilus groenlandicus / 32.7 | Pagophilus groenlandicus 32.7b,s,12 119600.046 0.0021163 228.578 L | behavioural experiment, suboptimum |
| canon-3:708 | Leucoraja erinacea / 30 | Raja erinacea 30e,o,22 500.047 0.0002447 2.3271 L | electroretinogram, optimum |
| canon-3:709 | Rattus norvegicus / 39 | Rattus norvegicus 39e,o,23 237.048 0.0067948 2.379 L | electroretinogram, optimum |
| canon-3:710 | Callospermophilus lateralis / 120 | Spermophilus lateralis 120e,o,10 215.549 0.0033564 3.680 H | electroretinogram, optimum |
| canon-3:713 | Sturnus vulgaris / 100 | Sturnus vulgaris 100e,s,25 75.028 0.01228 1.974 H | electroretinogram, suboptimum |
| canon-3:714 | Tamias amoenus / 100 | Tamias amoenus 100e,o,10 51.9152 0.0093766 1.9880 H | electroretinogram, optimum |
| canon-3:717 | Tupaia glis / 90 | Tupaia glis 90b,o,27 142.055 0.0042455 3.479 H | behavioural experiment, optimum |

## Counts

- Healy cff_hz rows in canon-3: 34.
- Already corrected earlier (audit 21 and check-18): 11 (canon-3:684, 686, 690, 691, 704, 705, 706, 711, 712, 715, 716).
- Corrected here: 23 (`docs/views/recheck/recheck-22.jsonl`, all `correct`).
- Unverifiable: 0.

## Notes

- Four names differ from the printed table: Canis familiaris is printed Canis lupus familiaris, Gallus gallus is printed Gallus gallus domesticus, Leucoraja erinacea is printed Raja erinacea, Callospermophilus lateralis is printed Spermophilus lateralis. The logged taxon is kept (current names) and the quote carries the printed name.
- canon-3:707 (Pagophilus groenlandicus, 32.7): the printed source number is 12, which the table's list gives as Loop & Berkeley (1975), a cat study. The number may be a typo in the paper. The row and value match; the method follows the printed superscripts (b, s).
- The same source-list concern could apply elsewhere: the Sturnus (25, Greenwood et al. 2004) and Anguilla (2, Adrian & Matthews 1926) letters are taken as printed and were not checked against those primary papers.
- The numbers run into the mass and metabolic-rate cells in the extracted text are reference numbers, as in audit 21.
- No Healy row in canon-3 is outside this table. Canon-3:717 (Chlamydomonas) is a different source and not in scope.
