# desk-d396 progress

Angle: remaining new species of ZooKeys 1221: 205-277 (not filed by desk-d395), then a second open Pensoft Salticidae paper. 45 records (log docs/views/evidence/desk-d396.jsonl). check.py: 0 problems, also with --require-evidence-kind.

## Filed
- ZooKeys 1221: 205-277 (10.3897/zookeys.1221.135640; Wang C, Mi X, Li S, Xu X, 2024): Cheliceroides jinxini (male), Mintonia shiwandashan (male), Pancorius medog (female), Piranthus maddisoni (male); AME, ALE, PLE; 12 records.
- ZooKeys 1192: 141-178 (10.3897/zookeys.1192.114589; Wang C, Mi X, Li S, 2024; Crossref vor CC BY 4.0, page prints CC BY 4.0): Attulus jimani, Colaxes cibagou, Epeus pengi, Evarcha zayu, Pancorius nyingchi (male and female each), Icius zang (male); 33 records.
- All records sensory_anatomy: the sentences print 'Eye sizes', the Methods define no eye dimension. Values checked by script against the number printed for the eye label; no zeros.

## Weak spots
- The fetch tool summarises and cuts at 125 characters; type lines and neighbouring sentences are tool-returned pieces, not page copies. Neither paper says which type specimen was measured.
- ZooKeys 1221: the publisher preview text ends inside the male description of Piranthus maddisoni, so the 1221 species after it (Simaetha hainan, Stertinius lhoba, Synagelides kongmingi, S. xuandei, S. yunchangi, S. yidei, S. zilongi, Yaginumaella daweishan, Y. moinba, Y. pingbian) and the P. maddisoni female were not reachable. Only four of the remaining new species were reachable, not six; Okinawicius nepalicus (comb. nov.) and Padillothorax exilis are not new species and were not filed.
- WSC species pages opened for all but Mintonia shiwandashan and Piranthus maddisoni (UNCHECKED); family pages not opened.
- Pancorius medog and Piranthus maddisoni: the 'Results' heading above the family heading was not read separately for them (taken from the paper's single Results section).

## Not filed and why
- ZooKeys 1192: Icius zang female (printed 'ALE 0.26 PLE 0.19' without a comma); Synagelides medog female and Phintella longapophysis female (fetch returned identical sentences, possible tool error); Stertinius liqingae, Synagelides tianquan, Yaginumaella erlang (type lines returned only as paraphrase, not verbatim). Leads for a later unit.
