# Encoders on the world photos

Made by `tools/world/encoders.py` (2026-10-13T03:50:21Z). Heads fitted on the world fitting photos alone and read alone; the original models' vectors.

| Model | image parameters | width | every group: test right | old groups right | `other` given a view | groups passing (of 19) | after the fold: groups carried | pass on test | old groups right | `other` given a view |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| tinyclip-39m-16 | 38,587,392 | 512 | 0.7097 | 0.7407 | 0.1767 | 5 | primate, whale, bat, flyingfox | 4 | 0.769 | 0.1681 |
| bioclip-b16 | 86,192,640 | 512 | 0.7845 | 0.7957 | 0.19 | 12 | slime, spider, jumper, salamander, scorpion, tick, primate, whale, bat, flyingfox | 10 | 0.81 | 0.136 |
| bioclip25-mobile-fastvit | 11,569,068 | 1024 | 0.3829 | 0.3638 | 0.2933 | 0 | none | 0 | 0.405 | 0.315 |

Every group's marks on the test photos with all nineteen carried (named / right when called):

| Group | tinyclip-39m-16 | bioclip-b16 | bioclip25-mobile-fastvit |
|---|---|---|---|
| fungus | 0.5733 / 0.6078 | 0.69 / 0.7065 | 0.3433 / 0.3745 |
| slime | 0.79 / 0.7476 | 0.8567 / 0.8211 | 0.56 / 0.4516 |
| spider | 0.7167 / 0.6981 | 0.8633 / 0.8576 | 0.37 / 0.4189 |
| jumper | 0.74 / 0.7929 | 0.8767 / 0.9359 | 0.4633 / 0.4469 |
| fish | 0.6733 / 0.6733 | 0.8 / 0.7643 | 0.2967 / 0.3134 |
| shark | 0.78 / 0.7524 | 0.8267 / 0.8522 | 0.5 / 0.3348 |
| snail | 0.5767 / 0.5563 | 0.7167 / 0.6847 | 0.3567 / 0.3441 |
| sealife | 0.6 / 0.5696 | 0.7433 / 0.6969 | 0.35 / 0.3832 |
| crab | 0.4633 / 0.5245 | 0.6233 / 0.6727 | 0.1567 / 0.2238 |
| salamander | 0.6967 / 0.699 | 0.8367 / 0.848 | 0.34 / 0.3158 |
| worm | 0.59 / 0.598 | 0.67 / 0.659 | 0.3233 / 0.3745 |
| scorpion | 0.7433 / 0.7534 | 0.8467 / 0.8819 | 0.39 / 0.4134 |
| tick | 0.8067 / 0.7333 | 0.8767 / 0.8885 | 0.46 / 0.4367 |
| mammal | 0.4467 / 0.5276 | 0.5733 / 0.6056 | 0.14 / 0.19 |
| primate | 0.8967 / 0.8226 | 0.9033 / 0.8212 | 0.59 / 0.4863 |
| whale | 0.8533 / 0.8179 | 0.8933 / 0.7976 | 0.6233 / 0.425 |
| bat | 0.8567 / 0.8006 | 0.84 / 0.9 | 0.5367 / 0.4626 |
| flyingfox | 0.7567 / 0.7965 | 0.8133 / 0.8026 | 0.4233 / 0.4686 |
| cephalopod | 0.6533 / 0.6644 | 0.7367 / 0.7568 | 0.35 / 0.3633 |
