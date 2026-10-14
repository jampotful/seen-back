import json,glob,sys
B=json.load(open('/tmp/claude-0/-home-claude-seen-back/3f461d9e-57cb-5830-abd2-b578ff932c20/scratchpad/sweep5/sweep-2.json'))
canon=[json.loads(l) for l in open('docs/views/research/canon.jsonl')]
ev=[]
for f in glob.glob('docs/views/evidence/*.jsonl'):
    for l in open(f):
        try: ev.append(json.loads(l))
        except: pass
na=[json.loads(l) for l in open('docs/views/papers-status.jsonl')]
na=[x for x in na if x['status']=='n/a']
i=int(sys.argv[1]); g=B[i]
print(json.dumps({k:g[k] for k in ('genus','family','order','traits','species','closest')}))
for t in g['traits']:
    print(t,[c['doi'] for c in canon if c['trait']==t])
for e in ev:
    if e['taxon'].split()[0]==g['genus']: print('EV',e['taxon'],e['trait'],e['value'],e['source'].get('doi'),e['grade'])
