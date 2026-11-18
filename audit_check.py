import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    raw = f.read().split('const ASMAUL_HUSNA = ')[1].split(';\nif')[0]
    data = json.loads(raw)

print(f"Total entries: {len(data)}")

for d in data:
    num = d['number']
    ar = d['arabic']
    lat = d['latin']
    mean = d['meaning']
    desc = d['description']
    ref = d['reference']
    print(f"[{num:02d}] {ar} | {lat} | {mean}")
    print(f"     Tafsir: {desc}")
    print(f"     Dalil:  {ref}")
    print("-" * 50)
