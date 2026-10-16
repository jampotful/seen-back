# The rows pass: voice check and drafts

Written by `tools/views/voice_check.py` and `tools/views/rows.py`; each tool owns one block.

<!-- voice-check:start -->
## Voice check

`tools/views/voice_check.py` read 444 rows in 44 views (a row held in both a view's own list and its trial list counts once).
342 rows (77%) break at least one rule that a script can see; 1153 findings in all.

### By rule

| rule | findings |
|---|---:|
| humans | 46 |
| app | 628 |
| voice_words | 14 |
| banned | 0 |
| contrast | 0 |
| fragment | 7 |
| spelling | 156 |
| length | 4 |
| numbers | 159 |
| dash | 0 |
| hedge | 0 |
| grade_words | 139 |

### By view

| view | rows flagged | humans | app | voice_words | banned | contrast | fragment | spelling | length | numbers | dash | hedge | grade_words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 16 | 5 | 33 | 1 |  |  |  | 6 |  | 3 |  |  | 8 |
| jumper | 13 | 1 | 35 | 5 |  |  |  | 4 |  | 1 |  |  | 3 |
| whale | 8 | 2 | 19 |  |  |  |  | 9 | 2 | 9 |  |  | 3 |
| bee | 11 | 3 | 25 |  |  |  |  | 4 |  | 6 |  |  | 4 |
| bird | 10 | 2 | 21 |  |  |  |  | 1 |  | 12 |  |  | 5 |
| deer | 10 | 2 | 21 | 1 |  |  |  | 6 |  | 3 |  |  | 4 |
| fish | 11 |  | 19 |  |  |  |  | 2 |  | 10 |  |  | 6 |
| insect | 10 | 3 | 19 |  |  |  |  | 2 |  | 6 |  |  | 7 |
| dog | 8 | 3 | 20 |  |  |  |  | 5 |  | 2 |  |  | 4 |
| salamander | 10 |  | 21 |  |  |  |  | 10 |  | 1 |  |  | 2 |
| fox | 7 | 2 | 21 |  |  |  |  | 7 |  | 1 |  |  | 1 |
| fungus | 10 |  | 17 | 2 |  |  |  | 5 |  |  |  |  | 8 |
| owl | 7 | 2 | 23 |  |  |  | 2 | 4 |  |  |  |  | 1 |
| cephalopod | 8 | 3 | 11 |  |  |  |  | 3 | 1 | 8 |  |  | 3 |
| hawk | 7 | 2 | 11 |  |  |  |  | 1 |  | 12 |  |  | 3 |
| reef | 8 |  | 22 |  |  |  |  | 4 |  |  |  |  | 3 |
| shark | 8 |  | 23 |  |  |  |  | 4 |  | 1 |  |  | 1 |
| bigcat | 7 | 4 | 18 |  |  |  |  | 6 |  |  |  |  |  |
| spider | 7 |  | 18 |  |  |  | 1 | 1 | 1 | 2 |  |  | 5 |
| sealife | 10 |  | 14 |  |  |  |  | 4 |  | 3 |  |  | 6 |
| squirrel | 8 | 1 | 10 |  |  |  |  | 4 |  | 10 |  |  | 2 |
| alligator | 7 | 1 | 9 |  |  |  |  | 2 |  | 10 |  |  | 4 |
| bat | 10 |  | 14 |  |  |  |  | 5 |  | 3 |  |  | 4 |
| tick | 7 |  | 11 |  |  |  |  | 6 |  | 4 |  |  | 5 |
| primate | 5 | 3 | 9 |  |  |  |  | 5 |  | 5 |  |  | 3 |
| duck | 7 | 2 | 17 |  |  |  |  | 2 |  | 1 |  |  | 1 |
| frog | 10 | 1 | 11 |  |  |  | 1 |  |  | 8 |  |  | 2 |
| mammal | 8 | 1 | 10 |  |  |  |  | 5 |  | 4 |  |  | 3 |
| rabbit | 9 |  | 8 | 1 |  |  | 1 | 4 |  | 7 |  |  | 1 |
| snail | 9 |  | 9 |  |  |  |  | 7 |  | 1 |  |  | 4 |
| worm | 6 |  | 11 | 2 |  |  |  | 4 |  | 1 |  |  | 3 |
| scorpion | 8 |  | 11 |  |  |  | 1 | 2 |  | 2 |  |  | 4 |
| millipede | 5 | 1 | 12 |  |  |  |  | 3 |  |  |  |  | 3 |
| slime | 5 |  | 11 | 1 |  |  |  | 3 |  |  |  |  | 4 |
| centipede | 6 |  | 13 |  |  |  |  | 2 |  | 1 |  |  | 2 |
| plant | 5 | 1 | 7 |  |  |  |  | 4 |  | 2 |  |  | 3 |
| reptile | 7 |  | 8 |  |  |  |  |  |  | 9 |  |  |  |
| crab | 8 |  | 8 | 1 |  |  |  | 2 |  | 3 |  |  | 2 |
| wader | 8 | 1 | 7 |  |  |  |  |  |  | 6 |  |  | 2 |
| flyingfox | 7 |  | 6 |  |  |  |  | 5 |  |  |  |  | 4 |
| woodlouse | 6 |  | 7 |  |  |  |  | 2 |  | 2 |  |  | 4 |
| harvestman | 3 |  | 7 |  |  |  |  | 1 |  |  |  |  | 1 |
| other | 1 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |
| person | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |
<!-- voice-check:end -->
