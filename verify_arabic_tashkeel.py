import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    raw = f.read().split('const ASMAUL_HUSNA = ')[1].split(';\nif')[0]
    data = json.loads(raw)

for d in data:
    ar = d['arabic']
    lat = d['latin']
    # Check tashkeel: dammah on final consonant (marfu')
    # Arabic characters:
    # 064F: dammah (ُ)
    # 0651: shaddah (ّ)
    # Note: mangqush words like Al-Wali, Al-Muta'ali, Al-Baqi, Al-Hadi
    # In nominative (marfu'), ism mangqush: الْوَالِي, الْمُتَعَالِي, الْهَادِي, الْبَاقِي (the dammah on ya' is muqaddarah / implied).
    print(f"{d['number']:02d}: {ar} | {lat}")
