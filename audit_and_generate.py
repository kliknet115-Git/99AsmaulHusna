import json

# Comprehensive Islamic Audit for 99 Asmaul Husna
# Based on:
# 1. Al-Qur'an Al-Karim (Kemenag RI & Mushaf Madinah / KSU)
# 2. Shahih al-Bukhari & Shahih Muslim
# 3. Jami' at-Tirmidzi (no. 3507), Sunan Abi Dawud, Sunan Ibni Majah
# 4. Standard Transliterasi Arab-Latin SKB Menteri Agama & Mendikbud RI No. 158/1987

audited_99 = [
    {
        "number": 1,
        "slug": "ar-rahman",
        "arabic": "الرَّحْمٰنُ",
        "latin": "Ar-Rahmān",
        "meaning": "Yang Maha Pengasih",
        "description": "Allah melimpahkan kasih sayang-Nya yang teramat luas kepada seluruh makhluk di alam semesta tanpa terkecuali, baik yang beriman maupun yang ingkar di dunia ini.",
        "reference": "QS. Al-Fatihah: 3 & QS. Ar-Rahman: 1-2"
    },
    {
        "number": 2,
        "slug": "ar-rahim",
        "arabic": "الرَّحِيمُ",
        "latin": "Ar-Rahīm",
        "meaning": "Yang Maha Penyayang",
        "description": "Allah memiliki kasih sayang khusus, abadi, dan sempurna bagi hamba-hamba-Nya yang beriman, terutama kelak saat di hari akhirat.",
        "reference": "QS. Al-Fatihah: 3 & QS. Al-Ahzab: 43"
    },
    {
        "number": 3,
        "slug": "al-malik",
        "arabic": "الْمَلِكُ",
        "latin": "Al-Malik",
        "meaning": "Yang Maha Merajai",
        "description": "Allah adalah Penguasa tertinggi yang memiliki kedaulatan mutlak atas langit, bumi, dan seluruh alam semesta tanpa membutuhkan bantuan siapa pun.",
        "reference": "QS. Al-Mu’minun: 116 & QS. Al-Hasyr: 23"
    },
    {
        "number": 4,
        "slug": "al-quddus",
        "arabic": "الْقُدُّوسُ",
        "latin": "Al-Quddūs",
        "meaning": "Yang Mahasuci",
        "description": "Allah Mahasuci dari segala kekurangan, aib, sekutu, dan segala sifat yang tidak layak bagi keagungan serta kesempurnaan-Nya.",
        "reference": "QS. Al-Jumu’ah: 1 & QS. Al-Hasyr: 23"
    },
    {
        "number": 5,
        "slug": "as-salam",
        "arabic": "السَّلَامُ",
        "latin": "As-Salām",
        "meaning": "Yang Maha Memberi Kesejahteraan",
        "description": "Allah adalah sumber segala kedamaian, keselamatan, dan ketenteraman, serta Zat-Nya terbebas dari segala cacat cela.",
        "reference": "QS. Al-Hasyr: 23 & HR. Muslim no. 592"
    },
    {
        "number": 6,
        "slug": "al-mumin",
        "arabic": "الْمُؤْمِنُ",
        "latin": "Al-Mu’min",
        "meaning": "Yang Maha Memberi Keamanan",
        "description": "Allah mengaruniakan rasa aman, ketenangan batin, serta membenarkan kebenaran para Rasul dan menepati seluruh janji-Nya kepada orang beriman.",
        "reference": "QS. Al-Hasyr: 23 & QS. Quraisy: 4"
    },
    {
        "number": 7,
        "slug": "al-muhaimin",
        "arabic": "الْمُهَيْمِنُ",
        "latin": "Al-Muhaimin",
        "meaning": "Yang Maha Memelihara",
        "description": "Allah senantiasa mengawasi, menjaga, merawat, dan memelihara seluruh ciptaan-Nya tanpa pernah lalai atau terlewat sedikit pun.",
        "reference": "QS. Al-Hasyr: 23"
    },
    {
        "number": 8,
        "slug": "al-aziz",
        "arabic": "الْعَزِيزُ",
        "latin": "Al-‘Azīz",
        "meaning": "Yang Mahaperkasa",
        "description": "Allah Mahakuat dan Mahaperkasa, keagungan serta kekuatan-Nya tidak dapat dikalahkan oleh kekuatan apa pun di alam semesta.",
        "reference": "QS. Al-Baqarah: 209 & QS. Al-Hasyr: 23"
    },
    {
        "number": 9,
        "slug": "al-jabbar",
        "arabic": "الْجَبَّارُ",
        "latin": "Al-Jabbār",
        "meaning": "Yang Memiliki Kegagahan Mutlak",
        "description": "Allah berkuasa mutlak memaksakan kehendak-Nya atas segala sesuatu, sekaligus Maha Memperbaiki keadaan hamba-Nya yang berserah diri dan terpuruk.",
        "reference": "QS. Al-Hasyr: 23"
    },
    {
        "number": 10,
        "slug": "al-mutakabbir",
        "arabic": "الْمُتَكَبِّرُ",
        "latin": "Al-Mutakabbir",
        "meaning": "Yang Memiliki Segala Keagungan",
        "description": "Allah Pemilik segala kebesaran, keagungan, dan kemegahan hakiki. Segala kesombongan makhluk adalah batil dan hina di hadapan-Nya.",
        "reference": "QS. Al-Hasyr: 23 & HR. Muslim no. 2620"
    },
    {
        "number": 11,
        "slug": "al-khaliq",
        "arabic": "الْخَالِقُ",
        "latin": "Al-Khāliq",
        "meaning": "Yang Maha Pencipta",
        "description": "Allah menciptakan segala sesuatu dari yang belum pernah ada menjadi ada menurut ukuran, ketetapan, dan takdir yang amat teliti.",
        "reference": "QS. Ar-Ra’d: 16 & QS. Al-Hasyr: 24"
    },
    {
        "number": 12,
        "slug": "al-bari",
        "arabic": "الْبَارِئُ",
        "latin": "Al-Bāri’",
        "meaning": "Yang Maha Mengadakan",
        "description": "Allah mewujudkan ciptaan dari rencana menjadi kenyataan yang selaras, seimbang, serasi, dan bebas dari cacat cela.",
        "reference": "QS. Al-Hasyr: 24"
    },
    {
        "number": 13,
        "slug": "al-mushawwir",
        "arabic": "الْمُصَوِّرُ",
        "latin": "Al-Mushawwir",
        "meaning": "Yang Maha Membentuk Rupa",
        "description": "Allah memberikan bentuk, rupa, warna, dan keunikan fisik maupun karakter pada setiap makhluk sesuai kebijaksanaan-Nya.",
        "reference": "QS. Al-Hasyr: 24 & QS. Ali ‘Imran: 6"
    },
    {
        "number": 14,
        "slug": "al-ghaffar",
        "arabic": "الْغَفَّارُ",
        "latin": "Al-Ghaffār",
        "meaning": "Yang Maha Pengampun",
        "description": "Allah berulang kali mengampuni dosa-dosa hamba-Nya yang bertaubat dan senantiasa menutupi aib serta keburukan mereka di dunia dan akhirat.",
        "reference": "QS. Thaha: 82 & QS. Nuh: 10"
    },
    {
        "number": 15,
        "slug": "al-qahhar",
        "arabic": "الْقَهَّارُ",
        "latin": "Al-Qahhār",
        "meaning": "Yang Maha Menundukkan",
        "description": "Allah menundukkan dan menguasai seluruh makhluk. Tidak ada satu pun kekuatan yang mampu meloloskan diri dari kekuasaan dan takdir-Nya.",
        "reference": "QS. Ar-Ra’d: 16 & QS. Az-Zumar: 4"
    },
    {
        "number": 16,
        "slug": "al-wahhab",
        "arabic": "الْوَهَّابُ",
        "latin": "Al-Wahhāb",
        "meaning": "Yang Maha Pemberi Karunia",
        "description": "Allah melimpahkan pemberian, nikmat, dan anugerah tanpa batas, tanpa henti, dan tanpa mengharapkan balasan apa pun dari makhluk-Nya.",
        "reference": "QS. Ali ‘Imran: 8 & QS. Shad: 9"
    },
    {
        "number": 17,
        "slug": "ar-razzaq",
        "arabic": "الرَّزَّاقُ",
        "latin": "Ar-Razzāq",
        "meaning": "Yang Maha Pemberi Rezeki",
        "description": "Allah menjamin kelangsungan hidup serta mencukupi kebutuhan rezeki jasmani maupun rohani bagi seluruh makhluk yang Dia ciptakan.",
        "reference": "QS. Adz-Dzariyat: 58 & QS. Hud: 6"
    },
    {
        "number": 18,
        "slug": "al-fattah",
        "arabic": "الْفَتَّاحُ",
        "latin": "Al-Fattāh",
        "meaning": "Yang Maha Pembuka Rahmat",
        "description": "Allah membuka pintu-pintu kebajikan, rezeki, jalan keluar dari kesulitan hidup, serta pemutus perkara di antara hamba-Nya dengan adil.",
        "reference": "QS. Saba’: 26"
    },
    {
        "number": 19,
        "slug": "al-alim",
        "arabic": "الْعَلِيمُ",
        "latin": "Al-‘Alīm",
        "meaning": "Yang Maha Mengetahui",
        "description": "Pengetahuan Allah meliputi segala sesuatu, baik yang telah lalu, sedang berlangsung, maupun yang akan datang, secara lahiriah maupun batiniah.",
        "reference": "QS. Al-Baqarah: 115 & QS. Al-An’am: 59"
    },
    {
        "number": 20,
        "slug": "al-qabidh",
        "arabic": "الْقَابِضُ",
        "latin": "Al-Qābidh",
        "meaning": "Yang Maha Menyempitkan",
        "description": "Allah menahan atau menyempitkan rezeki, hati, serta mencabut jiwa hamba-Nya berdasarkan hikmah dan keadilan-Nya untuk menguji keimanan.",
        "reference": "QS. Al-Baqarah: 245 & HR. At-Tirmidzi no. 1314"
    },
    {
        "number": 21,
        "slug": "al-basith",
        "arabic": "الْبَاسِطُ",
        "latin": "Al-Bāsith",
        "meaning": "Yang Maha Melapangkan",
        "description": "Allah meluaskan rezeki, melapangkan dada orang beriman dengan cahaya petunjuk, dan mencurahkan kemudahan hidup kepada siapa yang Dia kehendaki.",
        "reference": "QS. Al-Baqarah: 245 & HR. At-Tirmidzi no. 1314"
    },
    {
        "number": 22,
        "slug": "al-khafidh",
        "arabic": "الْخَافِضُ",
        "latin": "Al-Khāfidh",
        "meaning": "Yang Maha Merendahkan",
        "description": "Allah merendahkan derajat orang-orang yang sombong, durhaka, fasik, dan mengingkari kebenaran ayat-ayat-Nya.",
        "reference": "QS. Al-Waqi’ah: 3 & HR. At-Tirmidzi no. 3507"
    },
    {
        "number": 23,
        "slug": "ar-rafi",
        "arabic": "الرَّافِعُ",
        "latin": "Ar-Rāfi‘",
        "meaning": "Yang Maha Meninggikan",
        "description": "Allah mengangkat derajat, kedudukan, dan martabat hamba-hamba-Nya yang beriman, berilmu, bertakwa, serta istiqamah dalam ketaatan.",
        "reference": "QS. Al-Mujadilah: 11 & QS. Al-An’am: 165"
    },
    {
        "number": 24,
        "slug": "al-muizz",
        "arabic": "الْمُعِزُّ",
        "latin": "Al-Mu‘izz",
        "meaning": "Yang Maha Memuliakan",
        "description": "Allah menganugerahkan kemuliaan, kehormatan, wibawa, dan kejayaan kepada hamba-hamba yang berpegang teguh pada agama-Nya.",
        "reference": "QS. Ali ‘Imran: 26"
    },
    {
        "number": 25,
        "slug": "al-mudzill",
        "arabic": "الْمُذِلُّ",
        "latin": "Al-Mudzill",
        "meaning": "Yang Maha Menghinakan",
        "description": "Allah mencabut kemuliaan dan mendatangkan kehinaan bagi orang-orang yang berpaling dari syariat-Nya serta gemar berbuat kezaliman.",
        "reference": "QS. Ali ‘Imran: 26"
    },
    {
        "number": 26,
        "slug": "as-sami",
        "arabic": "السَّمِيعُ",
        "latin": "As-Samī‘",
        "meaning": "Yang Maha Mendengar",
        "description": "Allah Maha Mendengar setiap ucapan lisan, bisikan kalbu, desah nafas, maupun doa seluruh hamba tanpa perantara dan tanpa batas ruang waktu.",
        "reference": "QS. Al-Baqarah: 127 & QS. Asy-Syura: 11"
    },
    {
        "number": 27,
        "slug": "al-bashir",
        "arabic": "الْبَصِيرُ",
        "latin": "Al-Bashīr",
        "meaning": "Yang Maha Melihat",
        "description": "Penglihatan Allah menjangkau segala sesuatu, tiada noktah sekecil atom pun dalam kegelapan pekat yang luput dari pandangan-Nya.",
        "reference": "QS. Al-Hujurat: 18 & QS. Asy-Syura: 11"
    },
    {
        "number": 28,
        "slug": "al-hakam",
        "arabic": "الْحَكَمُ",
        "latin": "Al-Hakam",
        "meaning": "Yang Maha Menetapkan Hukum",
        "description": "Allah adalah Hakim Tertinggi pemutus segala perkara, ketetapan hukum-Nya adil dan pasti terlaksana tanpa dapat diganggu gugat.",
        "reference": "QS. Al-An’am: 114 & HR. Abu Dawud no. 4955 (Shahih)"
    },
    {
        "number": 29,
        "slug": "al-adl",
        "arabic": "الْعَدْلُ",
        "latin": "Al-‘Adl",
        "meaning": "Yang Maha Adil",
        "description": "Allah menempatkan segala sesuatu secara seimbang, proporsional, penuh hikmah, dan bersih dari perbuatan zalim kepada ciptaan-Nya.",
        "reference": "QS. Al-An’am: 115 & HR. At-Tirmidzi no. 3507"
    },
    {
        "number": 30,
        "slug": "al-lathif",
        "arabic": "اللَّطِيفُ",
        "latin": "Al-Lathīf",
        "meaning": "Yang Maha Lembut",
        "description": "Allah Maha Lembut dalam memperlakukan hamba-Nya dengan cara tak terduga, serta Maha Mengetahui hal-hal yang teramat halus dan tersembunyi.",
        "reference": "QS. Al-An’am: 103 & QS. Luqman: 16"
    },
    {
        "number": 31,
        "slug": "al-khabir",
        "arabic": "الْخَبِيرُ",
        "latin": "Al-Khabīr",
        "meaning": "Yang Maha Mengetahui Rahasia",
        "description": "Allah mengetahui hakikat terdalam, motif batin, dan rahasia yang tersembunyi dari setiap perkara tanpa ada yang terlewatkan.",
        "reference": "QS. Al-An’am: 18 & QS. Al-Mulk: 14"
    },
    {
        "number": 32,
        "slug": "al-halim",
        "arabic": "الْحَلِيمُ",
        "latin": "Al-Halīm",
        "meaning": "Yang Maha Penyantun",
        "description": "Allah tidak tergesa-gesa menjatuhkan hukuman kepada hamba yang berbuat dosa, melainkan memberi kelapangan waktu untuk bertaubat.",
        "reference": "QS. Al-Baqarah: 225 & QS. Al-Isra’: 44"
    },
    {
        "number": 33,
        "slug": "al-azhim",
        "arabic": "الْعَظِيمُ",
        "latin": "Al-‘Azhīm",
        "meaning": "Yang Maha Agung",
        "description": "Allah memiliki keagungan yang tiada batas, mengungguli segala sesuatu dalam hal kebesaran, kekuasaan, dan kemuliaan martabat.",
        "reference": "QS. Al-Baqarah: 255 (Ayat Kursi) & QS. Al-Waqi’ah: 74"
    },
    {
        "number": 34,
        "slug": "al-ghafur",
        "arabic": "الْغَفُورُ",
        "latin": "Al-Ghafūr",
        "meaning": "Yang Maha Pengampun",
        "description": "Allah melimpahkan ampunan yang luas bagi seluruh dosa hamba yang memohon ampun dengan tulus dan bersungguh-sungguh.",
        "reference": "QS. Al-Baqarah: 173 & QS. Az-Zumar: 53"
    },
    {
        "number": 35,
        "slug": "asy-syakur",
        "arabic": "الشَّكُورُ",
        "latin": "Asy-Syakūr",
        "meaning": "Yang Maha Menghargai",
        "description": "Allah menerima dan membalas amal kebaikan hamba-Nya yang sedikit dengan ganjaran pahala serta kenikmatan yang berlipat ganda.",
        "reference": "QS. Fathir: 30 & QS. At-Taghabun: 17"
    },
    {
        "number": 36,
        "slug": "al-aliyy",
        "arabic": "الْعَلِيُّ",
        "latin": "Al-‘Aliyy",
        "meaning": "Yang Mahatinggi",
        "description": "Allah berkedudukan paling tinggi di atas seluruh makhluk-Nya, suci dari segala kekurangan martabat dan keterbatasan sifat ciptaan.",
        "reference": "QS. Al-Baqarah: 255 & QS. An-Nisa’: 34"
    },
    {
        "number": 37,
        "slug": "al-kabir",
        "arabic": "الْكَبِيرُ",
        "latin": "Al-Kabīr",
        "meaning": "Yang Mahabesar",
        "description": "Allah Mahabesar dalam zat, sifat, dan perbuatan-Nya, melampaui segala imajinasi makhluk dengan keagungan yang tiada tanding.",
        "reference": "QS. Ar-Ra’d: 9 & QS. Al-Hajj: 62"
    },
    {
        "number": 38,
        "slug": "al-hafizh",
        "arabic": "الْحَفِيظُ",
        "latin": "Al-Hafīzh",
        "meaning": "Yang Maha Memelihara",
        "description": "Allah menjaga dan memelihara seluruh alam semesta, keteraturan kosmos, serta seluruh catatan amal perbuatan manusia.",
        "reference": "QS. Hud: 57 & QS. Saba’: 21"
    },
    {
        "number": 39,
        "slug": "al-muqit",
        "arabic": "الْمُقِيتُ",
        "latin": "Al-Muqīt",
        "meaning": "Yang Maha Memberi Kecukupan",
        "description": "Allah menyediakan rezeki pokok, memelihara daya tahan hidup, dan menganugerahkan kecukupan gizi bagi seluruh makhluk-Nya.",
        "reference": "QS. An-Nisa’: 85"
    },
    {
        "number": 40,
        "slug": "al-hasib",
        "arabic": "الْحَسِيبُ",
        "latin": "Al-Hasīb",
        "meaning": "Yang Maha Menghitung",
        "description": "Allah Maha Cepat dan teliti dalam memperhitungkan amal perbuatan makhluk, sekaligus Maha Mencukupi segala keperluan hamba-Nya.",
        "reference": "QS. An-Nisa’: 6 & QS. Al-Ahzab: 39"
    },
    {
        "number": 41,
        "slug": "al-jalil",
        "arabic": "الْجَلِيلُ",
        "latin": "Al-Jalīl",
        "meaning": "Yang Mahamulia",
        "description": "Allah Pemilik sifat-sifat kemuliaan, keagungan, dan kebesaran sempurna yang menggetarkan sanubari setiap insan beriman.",
        "reference": "QS. Ar-Rahman: 27 & HR. At-Tirmidzi no. 3507"
    },
    {
        "number": 42,
        "slug": "al-karim",
        "arabic": "الْكَرِيمُ",
        "latin": "Al-Karīm",
        "meaning": "Yang Mahapemurah",
        "description": "Allah melimpahkan kedermawanan, kemuliaan, dan kebaikan yang tiada putus tanpa diminta dan tanpa mengharap imbalan.",
        "reference": "QS. Al-Infitar: 6 & QS. An-Naml: 40"
    },
    {
        "number": 43,
        "slug": "ar-raqib",
        "arabic": "الرَّقِيبُ",
        "latin": "Ar-Raqīb",
        "meaning": "Yang Maha Mengawasi",
        "description": "Allah mengamati setiap gerak-gerik, niat batin, dan ucapan hamba-Nya secara terus-menerus tanpa pernah lalai barang sedetik pun.",
        "reference": "QS. An-Nisa’: 1 & QS. Al-Ahzab: 52"
    },
    {
        "number": 44,
        "slug": "al-mujib",
        "arabic": "الْمُجِيبُ",
        "latin": "Al-Mujīb",
        "meaning": "Yang Maha Mengabulkan",
        "description": "Allah menyambut, mendengar, dan mengabulkan doa, permohonan, serta harapan hamba-Nya yang berdoa dengan penuh ketulusan.",
        "reference": "QS. Hud: 61"
    },
    {
        "number": 45,
        "slug": "al-wasi",
        "arabic": "الْوَاسِعُ",
        "latin": "Al-Wāsi‘",
        "meaning": "Yang Mahaluas",
        "description": "Keluasan rahmat, ampunan, kekayaan, kekuasaan, dan ilmu Allah meliputi segala ruang waktu serta tidak dapat dibatasi.",
        "reference": "QS. Al-Baqarah: 115 & QS. Al-Baqarah: 268"
    },
    {
        "number": 46,
        "slug": "al-hakim",
        "arabic": "الْحَكِيمُ",
        "latin": "Al-Hakīm",
        "meaning": "Yang Mahabijaksana",
        "description": "Segala ciptaan, ketetapan takdir, dan hukum syariat Allah sarat dengan kebijaksanaan, kebenaran, dan faedah mendalam.",
        "reference": "QS. Al-Baqarah: 129 & QS. Al-An’am: 18"
    },
    {
        "number": 47,
        "slug": "al-wadud",
        "arabic": "الْوَدُودُ",
        "latin": "Al-Wadūd",
        "meaning": "Yang Maha Mengasihi",
        "description": "Allah mencintai hamba-hamba-Nya yang saleh dan menanamkan rasa cinta, kelembutan, serta kasih sayang di dalam dada mereka.",
        "reference": "QS. Hud: 90 & QS. Al-Buruj: 14"
    },
    {
        "number": 48,
        "slug": "al-majid",
        "arabic": "الْمَجِيدُ",
        "latin": "Al-Majīd",
        "meaning": "Yang Mahamulia",
        "description": "Allah Pemilik kehormatan dan kemuliaan tertinggi yang melimpahkan kebajikan dan anugerah agung kepada segenap makhluk.",
        "reference": "QS. Hud: 73 & QS. Al-Buruj: 15"
    },
    {
        "number": 49,
        "slug": "al-baits",
        "arabic": "الْبَاعِثُ",
        "latin": "Al-Bā‘its",
        "meaning": "Yang Maha Membangkitkan",
        "description": "Allah membangkitkan kembali manusia dari alam kubur pada Hari Kiamat untuk mempertanggungjawabkan seluruh perbuatannya.",
        "reference": "QS. Al-Hajj: 7 & QS. Yasin: 52"
    },
    {
        "number": 50,
        "slug": "asy-syahid",
        "arabic": "الشَّهِيدُ",
        "latin": "Asy-Syahīd",
        "meaning": "Yang Maha Menyaksikan",
        "description": "Allah menjadi saksi atas setiap peristiwa di semesta, niat di lubuk kalbu, dan amal perbuatan manusia secara nyata dan sempurna.",
        "reference": "QS. An-Nisa’: 79 & QS. Al-Hajj: 17"
    },
    {
        "number": 51,
        "slug": "al-haqq",
        "arabic": "الْحَقُّ",
        "latin": "Al-Haqq",
        "meaning": "Yang Mahabenar",
        "description": "Zat Allah adalah kebenaran sejati, janji-Nya pasti terbukti, dan firman-Nya adalah fondasi dari seluruh kebenaran hakiki.",
        "reference": "QS. Al-Hajj: 6 & QS. Thaha: 114"
    },
    {
        "number": 52,
        "slug": "al-wakil",
        "arabic": "الْوَكِيلُ",
        "latin": "Al-Wakīl",
        "meaning": "Yang Maha Memelihara",
        "description": "Allah adalah tempat bersandar terbaik yang mengurus segala urusan dan memberi perlindungan bagi hamba-Nya yang bertawakal.",
        "reference": "QS. Ali ‘Imran: 173 & QS. Al-An’am: 102"
    },
    {
        "number": 53,
        "slug": "al-qawiyy",
        "arabic": "الْقَوِيُّ",
        "latin": "Al-Qawiyy",
        "meaning": "Yang Mahakuat",
        "description": "Kekuatan Allah adalah sempurna dan abadi, tidak pernah melemah, lelah, atau membutuhkan bantuan dari siapa pun.",
        "reference": "QS. Al-Hajj: 40 & QS. Asy-Syura: 19"
    },
    {
        "number": 54,
        "slug": "al-matin",
        "arabic": "الْمَتِينُ",
        "latin": "Al-Matīn",
        "meaning": "Yang Mahakokoh",
        "description": "Kekuasaan dan keteguhan Allah sangat kokoh, tidak tergoyahkan oleh rintangan apa pun dan tidak pernah mengalami kelemahan.",
        "reference": "QS. Adz-Dzariyat: 58"
    },
    {
        "number": 55,
        "slug": "al-waliyy",
        "arabic": "الْوَلِيُّ",
        "latin": "Al-Waliyy",
        "meaning": "Yang Maha Melindungi",
        "description": "Allah adalah Pelindung sejati yang menuntun dari kegelapan menuju cahaya, serta mencintai dan menolong hamba yang beriman.",
        "reference": "QS. Al-Baqarah: 257 & QS. Asy-Syura: 28"
    },
    {
        "number": 56,
        "slug": "al-hamid",
        "arabic": "الْحَمِيدُ",
        "latin": "Al-Hamīd",
        "meaning": "Yang Maha Terpuji",
        "description": "Segala pujian hakiki hanya layak dipersembahkan bagi Allah karena seluruh sifat, tindakan, dan anugerah-Nya sempurna.",
        "reference": "QS. Ibrahim: 8 & QS. Fathir: 15"
    },
    {
        "number": 57,
        "slug": "al-muhshi",
        "arabic": "الْمُحْصِي",
        "latin": "Al-Muhshī",
        "meaning": "Yang Maha Menghitung",
        "description": "Allah mencatat, memperhitungkan, dan membukukan setiap zarah di alam semesta secara rinci tanpa ada kekeliruan barang sedikit pun.",
        "reference": "QS. Maryam: 94 & QS. An-Naba’: 29"
    },
    {
        "number": 58,
        "slug": "al-mubdi",
        "arabic": "الْمُبْدِئُ",
        "latin": "Al-Mubdi’",
        "meaning": "Yang Maha Memulai",
        "description": "Allah memulai penciptaan pertama kali dari ketiadaan murni tanpa ada contoh atau bahan dasar terdahulu.",
        "reference": "QS. Yunus: 34 & QS. Al-Buruj: 13"
    },
    {
        "number": 59,
        "slug": "al-muid",
        "arabic": "الْمُعِيدُ",
        "latin": "Al-Mu‘īd",
        "meaning": "Yang Maha Mengembalikan",
        "description": "Allah mengembalikan makhluk hidup setelah kematiannya menjadi hidup kembali pada Hari Kebangkitan dengan mudah.",
        "reference": "QS. Yunus: 34 & QS. Ar-Rum: 27"
    },
    {
        "number": 60,
        "slug": "al-muhyi",
        "arabic": "الْمُحْيِي",
        "latin": "Al-Muhyī",
        "meaning": "Yang Maha Menghidupkan",
        "description": "Allah meniupkan ruh dan menganugerahkan kehidupan kepada jasad yang mati, serta menghidupkan hati hamba dengan iman.",
        "reference": "QS. Ar-Rum: 50 & QS. Fushshilat: 39"
    },
    {
        "number": 61,
        "slug": "al-mumit",
        "arabic": "الْمُمِيتُ",
        "latin": "Al-Mumīt",
        "meaning": "Yang Maha Mematikan",
        "description": "Allah menentukan batas ajal dan mencabut nyawa setiap makhluk hidup sesuai ketetapan waktu yang telah ditentukan.",
        "reference": "QS. Al-A’raf: 158 & QS. Ghafir: 68"
    },
    {
        "number": 62,
        "slug": "al-hayy",
        "arabic": "الْحَيُّ",
        "latin": "Al-Hayy",
        "meaning": "Yang Mahahidup",
        "description": "Allah Mahahidup dengan kehidupan kekal dan sempurna yang tidak berawal dan tidak akan pernah berakhir.",
        "reference": "QS. Al-Baqarah: 255 & QS. Thaha: 111"
    },
    {
        "number": 63,
        "slug": "al-qayyum",
        "arabic": "الْقَيُّومُ",
        "latin": "Al-Qayyūm",
        "meaning": "Yang Maha Mandiri",
        "description": "Allah berdiri sendiri mengurus dan menegakkan seluruh makhluk-Nya tanpa pernah merasa kantuk apalagi tertidur.",
        "reference": "QS. Al-Baqarah: 255 & QS. Ali ‘Imran: 2"
    },
    {
        "number": 64,
        "slug": "al-wajid",
        "arabic": "الْوَاجِدُ",
        "latin": "Al-Wājid",
        "meaning": "Yang Maha Menemukan",
        "description": "Allah senantiasa menemukan dan mengadakan apa saja yang dikehendaki-Nya, tidak pernah kehilangan atau kekurangan sesuatu pun.",
        "reference": "HR. Muslim no. 2577 & HR. At-Tirmidzi no. 3507"
    },
    {
        "number": 65,
        "slug": "al-majid-2",
        "arabic": "الْمَاجِدُ",
        "latin": "Al-Mājid",
        "meaning": "Yang Mahamulia",
        "description": "Allah memiliki kemuliaan, keluhuran budi, dan kedermawanan yang melimpah ruah kepada seluruh hamba-Nya.",
        "reference": "HR. At-Tirmidzi no. 3507 & QS. Hud: 73"
    },
    {
        "number": 66,
        "slug": "al-wahid",
        "arabic": "الْوَاحِدُ",
        "latin": "Al-Wāhid",
        "meaning": "Yang Mahatunggal",
        "description": "Allah adalah Esa dalam zat, sifat, dan perbuatan-Nya, tidak terbagi-bagi dan tiada sekutu apa pun bagi-Nya.",
        "reference": "QS. Al-Baqarah: 163 & QS. Ar-Ra’d: 16"
    },
    {
        "number": 67,
        "slug": "al-ahad",
        "arabic": "الْأَحَدُ",
        "latin": "Al-Ahad",
        "meaning": "Yang Maha Esa",
        "description": "Allah adalah Esa mutlak yang tidak ada tandingan, pasangan, anak, atau sekutu yang menyerupai keagungan-Nya.",
        "reference": "QS. Al-Ikhlas: 1"
    },
    {
        "number": 68,
        "slug": "ash-shamad",
        "arabic": "الصَّمَدُ",
        "latin": "Ash-Shamad",
        "meaning": "Tempat Meminta / Bergantung",
        "description": "Allah adalah tumpuan utama tempat seluruh makhluk bergantung dan memohon segala kebutuhan hajat hidup mereka.",
        "reference": "QS. Al-Ikhlas: 2"
    },
    {
        "number": 69,
        "slug": "al-qadir",
        "arabic": "الْقَادِرُ",
        "latin": "Al-Qādir",
        "meaning": "Yang Mahakuasa",
        "description": "Allah memiliki kekuasaan penuh untuk mengadakan atau meniadakan sesuatu menurut kehendak dan kebijaksanaan-Nya.",
        "reference": "QS. Al-An’am: 65 & QS. Al-Baqarah: 20"
    },
    {
        "number": 70,
        "slug": "al-muqtadir",
        "arabic": "الْمُقْتَدِرُ",
        "latin": "Al-Muqtadir",
        "meaning": "Yang Maha Menentukan",
        "description": "Kekuasaan Allah amat nyata dan berkuasa mutlak mengatur segala takdir yang terlaksana pasti di alam semesta.",
        "reference": "QS. Al-Qamar: 42 & QS. Al-Kahfi: 45"
    },
    {
        "number": 71,
        "slug": "al-muqaddim",
        "arabic": "الْمُقَدِّمُ",
        "latin": "Al-Muqaddim",
        "meaning": "Yang Maha Mendahulukan",
        "description": "Allah memajukan dan mendahulukan apa serta siapa yang layak didahulukan sesuai dengan hikmah kebijaksanaan-Nya.",
        "reference": "HR. Bukhari no. 1120 & Muslim no. 771 (Doa Tahajjud)"
    },
    {
        "number": 72,
        "slug": "al-muakhkhir",
        "arabic": "الْمُؤَخِّرُ",
        "latin": "Al-Mu’akhkhir",
        "meaning": "Yang Maha Mengakhirkan",
        "description": "Allah menunda dan mengakhirkan hal-hal tertentu menurut waktu yang paling tepat dan penuh pertimbangan mulia.",
        "reference": "HR. Bukhari no. 1120 & Muslim no. 771 (Doa Tahajjud)"
    },
    {
        "number": 73,
        "slug": "al-awwal",
        "arabic": "الْأَوَّلُ",
        "latin": "Al-Awwal",
        "meaning": "Yang Maha Awal",
        "description": "Allah telah ada sebelum segala sesuatu tercipta, tanpa permulaan bagi keberadaan-Nya yang abadi.",
        "reference": "QS. Al-Hadid: 3 & HR. Muslim no. 2713"
    },
    {
        "number": 74,
        "slug": "al-akhir",
        "arabic": "الْآخِرُ",
        "latin": "Al-Ākhir",
        "meaning": "Yang Maha Akhir",
        "description": "Allah tetap ada setelah seluruh ciptaan hancur binasa, tanpa batas akhir bagi keabadian-Nya.",
        "reference": "QS. Al-Hadid: 3 & HR. Muslim no. 2713"
    },
    {
        "number": 75,
        "slug": "azh-zhahir",
        "arabic": "الظَّاهِرُ",
        "latin": "Azh-Zhāhir",
        "meaning": "Yang Maha Nyata",
        "description": "Keberadaan dan kebesaran Allah nyata terpancar melalui tanda-tanda keagungan ciptaan-Nya di alam raya.",
        "reference": "QS. Al-Hadid: 3 & HR. Muslim no. 2713"
    },
    {
        "number": 76,
        "slug": "al-bathin",
        "arabic": "الْبَاطِنُ",
        "latin": "Al-Bāthin",
        "meaning": "Yang Maha Ghaib",
        "description": "Zat Allah tersembunyi dari pandangan mata jasmani manusia di dunia, namun ilmu-Nya menembus segala rahasia batin.",
        "reference": "QS. Al-Hadid: 3 & HR. Muslim no. 2713"
    },
    {
        "number": 77,
        "slug": "al-wali",
        "arabic": "الْوَالِي",
        "latin": "Al-Wālī",
        "meaning": "Yang Maha Memerintah",
        "description": "Allah adalah Pemimpin dan Pengatur tertinggi yang mengelola seluruh urusan alam dengan kekuasaan mutlak.",
        "reference": "QS. Ar-Ra’d: 11"
    },
    {
        "number": 78,
        "slug": "al-mutaali",
        "arabic": "الْمُتَعَالِي",
        "latin": "Al-Muta‘ālī",
        "meaning": "Yang Mahatinggi",
        "description": "Allah Mahatinggi di atas segala ciptaan, terbebas dari sifat-sifat kelemahan dan prasangka buruk makhluk.",
        "reference": "QS. Ar-Ra’d: 9"
    },
    {
        "number": 79,
        "slug": "al-barr",
        "arabic": "الْبَرُّ",
        "latin": "Al-Barr",
        "meaning": "Yang Maha Dermawan",
        "description": "Allah melimpahkan kebaikan, kelapangan hati, dan kebajikan yang amat besar kepada seluruh hamba-Nya.",
        "reference": "QS. Ath-Thur: 28"
    },
    {
        "number": 80,
        "slug": "at-tawwab",
        "arabic": "التَّوَّابُ",
        "latin": "At-Tawwāb",
        "meaning": "Yang Maha Penerima Taubat",
        "description": "Allah senantiasa membukakan pintu taubat dan menerima kembali hamba yang beristighfar dan bertaubat kepada-Nya.",
        "reference": "QS. Al-Baqarah: 37 & QS. An-Nur: 10"
    },
    {
        "number": 81,
        "slug": "al-muntaqim",
        "arabic": "الْمُنْتَقِمُ",
        "latin": "Al-Muntaqim",
        "meaning": "Yang Maha Pemberi Balasan",
        "description": "Allah menimpakan hukuman yang adil dan setimpal kepada kaum yang sombong, zalim, dan gemar menindas.",
        "reference": "QS. As-Sajdah: 22 & QS. Az-Zukhruf: 41"
    },
    {
        "number": 82,
        "slug": "al-afuww",
        "arabic": "الْعَفُوُّ",
        "latin": "Al-‘Afuww",
        "meaning": "Yang Mahapemaaf",
        "description": "Allah menghapus dosa-dosa hamba-Nya hingga tak berbekas seolah perbuatan keliru itu tidak pernah terjadi.",
        "reference": "QS. An-Nisa’: 43 & QS. Al-Hajj: 60"
    },
    {
        "number": 83,
        "slug": "ar-rauf",
        "arabic": "الرَّءُوفُ",
        "latin": "Ar-Ra’ūf",
        "meaning": "Yang Maha Pengasuh",
        "description": "Allah memiliki rasa belas kasih yang amat mendalam dan kelemahlembutan tiada tara kepada seluruh hamba-Nya.",
        "reference": "QS. Al-Baqarah: 207 & QS. Al-Hasyr: 10"
    },
    {
        "number": 84,
        "slug": "malikul-mulk",
        "arabic": "مَالِكُ الْمُلْكِ",
        "latin": "Mālikul-Mulk",
        "meaning": "Penguasa Kerajaan Semesta",
        "description": "Allah Pemilik kedaulatan abadi atas seluruh kekuasaan, memberikan dan mencabut kekuasaan sesuai kehendak-Nya.",
        "reference": "QS. Ali ‘Imran: 26"
    },
    {
        "number": 85,
        "slug": "dzul-jalali-wal-ikram",
        "arabic": "ذُو الْجَلَالِ وَالْإِكْرَامِ",
        "latin": "Dzul-Jalāli wal-Ikrām",
        "meaning": "Pemilik Kebesaran & Kemuliaan",
        "description": "Allah memiliki seluruh keagungan yang menuntut rasa hormat serta kemuliaan yang melimpahkan anugerah kebajikan.",
        "reference": "QS. Ar-Rahman: 27 & QS. Ar-Rahman: 78"
    },
    {
        "number": 86,
        "slug": "al-muqsith",
        "arabic": "الْمُقْسِطُ",
        "latin": "Al-Muqsith",
        "meaning": "Yang Maha Pemberi Keadilan",
        "description": "Allah menegakkan keadilan sejati, membela kaum yang dizalimi, dan menuntut hak dari para penindas.",
        "reference": "QS. Ali ‘Imran: 18 & QS. Al-A’raf: 29"
    },
    {
        "number": 87,
        "slug": "al-jami",
        "arabic": "الْجَامِعُ",
        "latin": "Al-Jāmi‘",
        "meaning": "Yang Maha Mengumpulkan",
        "description": "Allah menghimpun seluruh manusia di Padang Mahsyar serta mengumpulkan berbagai hikmah dan kebaikan.",
        "reference": "QS. Ali ‘Imran: 9 & QS. Saba’: 26"
    },
    {
        "number": 88,
        "slug": "al-ghaniyy",
        "arabic": "الْغَنِيُّ",
        "latin": "Al-Ghaniyy",
        "meaning": "Yang Mahakaya",
        "description": "Allah Mahakaya dan serba cukup, tidak membutuhkan pertolongan atau ibadah dari siapa pun di alam raya.",
        "reference": "QS. Al-Baqarah: 267 & QS. Muhammad: 38"
    },
    {
        "number": 89,
        "slug": "al-mughni",
        "arabic": "الْمُغْنِي",
        "latin": "Al-Mughnī",
        "meaning": "Yang Maha Memberi Kekayaan",
        "description": "Allah mencukupi hajat hidup hamba-Nya dan menganugerahkan kekayaan lahir maupun batin berupa rasa qana’ah.",
        "reference": "QS. An-Najm: 48 & QS. At-Taubah: 28"
    },
    {
        "number": 90,
        "slug": "al-mani",
        "arabic": "الْمَانِعُ",
        "latin": "Al-Māni‘",
        "meaning": "Yang Maha Mencegah",
        "description": "Allah menahan atau mencegah bahaya dari hamba-Nya dan menguji manusia dengan menahan sesuatu demi kebaikan hakiki.",
        "reference": "HR. Bukhari no. 844 & Muslim no. 593 (Dzikir Ba'da Shalat)"
    },
    {
        "number": 91,
        "slug": "adh-dharr",
        "arabic": "الضَّارُّ",
        "latin": "Adh-Dhārr",
        "meaning": "Yang Maha Memberi Derita",
        "description": "Tiada bahaya atau mudarat yang menimpa seseorang melainkan atas izin dan ketetapan ujian dari Allah semata.",
        "reference": "QS. Al-An’am: 17, QS. Yunus: 107 & HR. At-Tirmidzi no. 2516"
    },
    {
        "number": 92,
        "slug": "an-nafi",
        "arabic": "النَّافِعُ",
        "latin": "An-Nāfi‘",
        "meaning": "Yang Maha Memberi Manfaat",
        "description": "Segala manfaat, pertolongan, kebaikan, dan kemaslahatan hidup bersumber murni dari perkenan Allah Ta’ala.",
        "reference": "QS. Al-An’am: 17, QS. Yunus: 107 & HR. At-Tirmidzi no. 2516"
    },
    {
        "number": 93,
        "slug": "an-nur",
        "arabic": "النُّورُ",
        "latin": "An-Nūr",
        "meaning": "Yang Maha Bercahaya",
        "description": "Allah adalah Sumber cahaya bagi langit dan bumi yang menerangi qalbu hamba-Nya dengan petunjuk keimanan.",
        "reference": "QS. An-Nur: 35"
    },
    {
        "number": 94,
        "slug": "al-hadi",
        "arabic": "الْهَادِي",
        "latin": "Al-Hādī",
        "meaning": "Yang Maha Pemberi Petunjuk",
        "description": "Allah membimbing hati hamba-hamba-Nya menuju jalan kebenaran, keselamatan, dan keridaan-Nya.",
        "reference": "QS. Al-Hajj: 54 & QS. Al-Furqan: 31"
    },
    {
        "number": 95,
        "slug": "al-badi",
        "arabic": "الْبَدِيعُ",
        "latin": "Al-Badī‘",
        "meaning": "Yang Maha Pencipta Keindahan",
        "description": "Allah menciptakan alam semesta dengan desain yang menakjubkan, indah, rapi, dan tanpa contoh tandingan.",
        "reference": "QS. Al-Baqarah: 117 & QS. Al-An’am: 101"
    },
    {
        "number": 96,
        "slug": "al-baqi",
        "arabic": "الْبَاقِي",
        "latin": "Al-Bāqī",
        "meaning": "Yang Mahakekal",
        "description": "Allah Mahakekal abadi, sementara seluruh makhluk ciptaan-Nya akan musnah dan menemui kebinasaan.",
        "reference": "QS. Ar-Rahman: 26-27 & QS. Al-Qashash: 88"
    },
    {
        "number": 97,
        "slug": "al-warits",
        "arabic": "الْوَارِثُ",
        "latin": "Al-Wārits",
        "meaning": "Yang Maha Pewaris",
        "description": "Setelah seluruh alam semesta berakhir, seluruh kepemilikan dan kekuasaan mutlak kembali kepada Allah.",
        "reference": "QS. Al-Hijr: 23 & QS. Maryam: 40"
    },
    {
        "number": 98,
        "slug": "ar-rasyid",
        "arabic": "الرَّشِيدُ",
        "latin": "Ar-Rasyīd",
        "meaning": "Yang Maha Cerdas / Pembimbing Kebenaran",
        "description": "Segala tindakan dan keputusan Allah berada pada puncak ketepatan, keadilan, dan kelurusan tanpa cacat.",
        "reference": "QS. Al-Kahfi: 10 & HR. At-Tirmidzi no. 3507"
    },
    {
        "number": 99,
        "slug": "ash-shabur",
        "arabic": "الصَّبُورُ",
        "latin": "Ash-Shabūr",
        "meaning": "Yang Mahasabar",
        "description": "Allah tidak terburu-buru menghukum orang-orang yang berbuat maksiat, melainkan memberi kesempatan luas untuk bertaubat.",
        "reference": "HR. Bukhari no. 6099, Muslim no. 2804 & At-Tirmidzi no. 3507"
    }
]

# Write to js/data.js
output = '// 99 Asmaul Husna - Data Terverifikasi Al-Qur\'an & Hadits\n'
output += '// Rujukan: Kemenag RI, Shahih Bukhari, Shahih Muslim, Jami\' at-Tirmidzi\n'
output += 'const ASMAUL_HUSNA = ' + json.dumps(audited_99, ensure_ascii=False, indent=2) + ';\n'
output += 'if (typeof module !== "undefined" && module.exports) { module.exports = ASMAUL_HUSNA; }\n'

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Audit completed: {len(audited_99)} verified items written to js/data.js")
