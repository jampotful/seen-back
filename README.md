# Real photographs with nothing alive in them
Made by .github/workflows/nonlife.yml (tools/world/nonlife_real.py) from Wikimedia Commons. manifest.csv gives every photo's
family, set (tune or test, by a hash of the id, fixed before anything was measured), the query that found it, its Commons page
(source), the address of the 500-pixel copy fetched, its licence (CC0, CC BY or public domain), the licence's address and the
author as Commons gives it. photos/<id>.jpg are those copies. nonlife-made.f16.npy and nonlife-made.ids.json are the pocket
encoder's unit vectors (tools/world/nonlife.py --made reads them beside manifest.csv).
