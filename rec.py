import json,sys,glob
sys.path.insert(0,'/tmp/ws8')
B=json.load(open('/tmp/claude-0/-home-claude-seen-back/3f461d9e-57cb-5830-abd2-b578ff932c20/scratchpad/sweep5/sweep-2.json'))
canon=[json.loads(l) for l in open('/tmp/ws8/docs/views/research/canon.jsonl')]
def S(i,queries,chased,found,where=("WebSearch","WebFetch"),traits=None,level="genus"):
    g=B[i]; t=traits or g['traits']
    c=[]
    for x in canon:
        if x['trait'] in t and x['doi'] and x['doi'] not in c: c.append(x['doi'])
    r={"taxon":g['genus'],"level":level,"trait":"; ".join(t),"queries":queries,"where":list(where),"canon":c,"chased":chased,"found":found,"date":"2026-10-14"}
    open('/tmp/ws8/docs/views/searched/sweep-8.jsonl','a').write(json.dumps(r,ensure_ascii=False)+"\n")
def W(**k):
    k.setdefault("unit","sweep-8"); k["records"]=int(k.get("records",0)); k["priority"]=int(k.get("priority",2))
    assert isinstance(k["for"],list) and isinstance(k["rows"],list) and isinstance(k["views"],list) and isinstance(k["get"],str)
    open('/tmp/ws8/docs/views/wanted/sweep-8.jsonl','a').write(json.dumps(k,ensure_ascii=False)+"\n")
