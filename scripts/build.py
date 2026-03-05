#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[]
for l in (root/'data'/'sources.jsonl').read_text(encoding='utf-8').splitlines():
    if l.strip(): rows.append(json.loads(l))
(root/'exports'/'sources.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# NewsSource Export','',f'- total: **{len(rows)}**','']
for i,r in enumerate(rows,1):
    md.append(f"{i}. **{r['name']}** `[{','.join(r.get('type_tags',[]))}]` — {r['url']}")
(root/'exports'/'NewsSource.md').write_text("\n".join(md)+"\n",encoding='utf-8')
print('built',len(rows))
