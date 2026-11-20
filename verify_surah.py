import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    raw = f.read().split('const ASMAUL_HUSNA = ')[1].split(';\nif')[0]
    data = json.loads(raw)

# Surah index mapping (Standard 114 Surahs)
surahs = {
    "Al-Fatihah": 1, "Al-Baqarah": 2, "Ali ‘Imran": 3, "Ali 'Imran": 3, "An-Nisa’": 4, "An-Nisa'": 4,
    "Al-Ma’idah": 5, "Al-An’am": 6, "Al-An'am": 6, "Al-A’raf": 7, "Al-A'raf": 7, "Al-Anfal": 8,
    "At-Taubah": 9, "Yunus": 10, "Hud": 11, "Yusuf": 12, "Ar-Ra’d": 13, "Ar-Ra'd": 13,
    "Ibrahim": 14, "Al-Hijr": 15, "An-Nahl": 16, "Al-Isra’": 17, "Al-Isra'": 17, "Al-Kahfi": 18,
    "Maryam": 19, "Thaha": 20, "Al-Anbiya’": 21, "Al-Hajj": 22, "Al-Mu’minun": 23, "Al-Mu'minun": 23,
    "An-Nur": 24, "Al-Furqan": 25, "Asy-Syu'ara'": 26, "An-Naml": 27, "Al-Qashash": 28,
    "Al-‘Ankabut": 29, "Ar-Rum": 30, "Luqman": 31, "As-Sajdah": 32, "Al-Ahzab": 33,
    "Saba’": 34, "Saba'": 34, "Fathir": 35, "Yasin": 36, "Ash-Shaffat": 37, "Shad": 38,
    "Az-Zumar": 39, "Ghafir": 40, "Al-Mu'min": 40, "Fushshilat": 41, "Asy-Syura": 42,
    "Az-Zukhruf": 43, "Ad-Dukhan": 44, "Al-Jatsiyah": 45, "Al-Ahqaf": 46, "Muhammad": 47,
    "Al-Fath": 48, "Al-Hujurat": 49, "Qaf": 50, "Adz-Dzariyat": 51, "Ath-Thur": 52,
    "An-Najm": 53, "Al-Qamar": 54, "Ar-Rahman": 55, "Al-Waqi’ah": 56, "Al-Hadid": 57,
    "Al-Mujadilah": 58, "Al-Hasyr": 59, "Al-Mumtahanah": 60, "Ash-Shaff": 61, "Al-Jumu’ah": 62,
    "Al-Munafiqun": 63, "At-Taghabun": 64, "Ath-Thalaq": 65, "At-Tahrim": 66, "Al-Mulk": 67,
    "Al-Qalam": 68, "Al-Haqqah": 69, "Al-Ma’arij": 70, "Nuh": 71, "Al-Jinn": 72,
    "Al-Muzzammil": 73, "Al-Muddatstsir": 74, "Al-Qiyamah": 75, "Al-Insan": 76, "Al-Mursalat": 77,
    "An-Naba’": 78, "An-Naba'": 78, "An-Nazi’at": 79, "‘Abasa": 80, "At-Takwir": 81,
    "Al-Infithar": 82, "Al-Infitar": 82, "Al-Muthaffifin": 83, "Al-Insyiqaq": 84, "Al-Buruj": 85,
    "Ath-Thariq": 86, "Al-A’la": 87, "Al-Ghasyiyah": 88, "Al-Fajr": 89, "Al-Balad": 90,
    "Asy-Syams": 91, "Al-Lail": 92, "Adh-Dhuha": 93, "Al-Insyirah": 94, "At-Tin": 95,
    "Al-‘Alaq": 96, "Al-Qadr": 97, "Al-Bayyinah": 98, "Az-Zalzalah": 99, "Al-‘Adiyat": 100,
    "Al-Qari’ah": 101, "At-Takatsur": 102, "Al-‘Ashr": 103, "Al-Humazah": 104, "Al-Fil": 105,
    "Quraisy": 106, "Al-Ma’un": 107, "Al-Kautsar": 108, "Al-Kafirun": 109, "An-Nashr": 110,
    "Al-Lahab": 111, "Al-Ikhlas": 112, "Al-Falaq": 113, "An-Nas": 114
}

for d in data:
    ref = d['reference']
    # Check if surah exists in reference
    found = False
    for s in surahs:
        if s in ref:
            found = True
            break
    if not found and "Hadits" not in ref and "HR." not in ref:
        print(f"Warning on #{d['number']} {d['latin']}: Reference '{ref}' might not match known surah name!")

print("Check finished.")
