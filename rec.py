import json,sys
# usage: rec.py searched|wanted  '<json>'
kind=sys.argv[1]; obj=json.loads(sys.argv[2])
open(f'/tmp/ws10/docs/views/{kind}/sweep-10.jsonl','a').write(json.dumps(obj,ensure_ascii=False)+'\n')
