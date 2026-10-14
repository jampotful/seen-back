import json,sys
B=json.load(open('/tmp/claude-0/-home-claude-seen-back/3f461d9e-57cb-5830-abd2-b578ff932c20/scratchpad/sweep5/sweep-2.json'))
cache={}
def get(ref):
    u,n=ref.split('#')
    if u not in cache:
        try: cache[u]=[json.loads(l) for l in open('docs/views/evidence/%s.jsonl'%u) if l.strip()]
        except Exception as e: cache[u]=[]
    L=cache[u]
    return L[int(n)-1] if 0<int(n)<=len(L) else None
for i in map(int,sys.argv[1:]):
    g=B[i]; print(i,g['genus'])
    for t,ref in g['closest'].items():
        r=get(ref)
        if r: print('  ',t,ref,r['taxon'],r['source'].get('authors','')[:30],r['source'].get('year'),r['source'].get('doi') or r['source'].get('url'),'|',str(r['value'])[:50])
        else: print('  ',t,ref,'?')
