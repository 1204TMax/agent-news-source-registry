#!/usr/bin/env python3
import json, re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'sources.jsonl'
ids=set(); ok=True
for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
    if not l.strip():
        continue
    o=json.loads(l)
    for k in ['id','name','url','type','reliability_score','signal_to_noise']:
        if k not in o:
            print(f'[ERR] line {i}: missing {k}'); ok=False
    if o.get('id') in ids:
        print(f'[ERR] line {i}: duplicate id {o.get("id")}'); ok=False
    ids.add(o.get('id'))
    if not re.match(r'^https?://', o.get('url','')):
        print(f'[ERR] line {i}: bad url'); ok=False
print('OK' if ok else 'FAILED')
raise SystemExit(0 if ok else 1)
