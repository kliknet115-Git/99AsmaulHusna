# 🌟 Asmaul Husna — 99 Nama-nama Allah (Mobile-First PWA)

Aplikasi Web Progresif (**Progressive Web App / PWA**) modern yang didesain secara **Mobile-First** dan dioptimalkan secara khusus untuk pengalaman pengguna **iPhone / iOS Safari**, serta siap di-hosting langsung secara gratis menggunakan **GitHub Pages**.

---

## ✨ Fitur Utama

1. **99 Asmaul Husna Lengkap & Terverifikasi:**
   - Kaligrafi & teks Arab berharakat jelas (*Noto Naskh Arabic / Amiri*).
   - Transliterasi Latin resmi Indonesia.
   - Arti singkat & makna mendalam (tadabbur).
   - Dalil rujukan dari ayat Al-Qur'an & Hadits Shahih.

2. **Pengalaman Native iPhone (iOS Safari Optimized):**
   - **Tampilan Layar Penuh (Standalone):** Tanpa bilah peramban (URL bar) saat dipasang di layar utama.
   - **Apple Touch Icon:** Ikon aplikasi 180×180 px resolusi tinggi bernuansa emas dan royal navy.
   - **Dukungan Safe Area Insets:** Menyesuaikan notch iPhone, Dynamic Island, dan home indicator bawah (`env(safe-area-inset-*)`).
   - **Momentum Scrolling & Haptic Feedback:** Sentuhan halus khas iOS dengan efek getar saat berdzikir atau menyimpan favorit.
   - **Navigasi Geser (Touch Swipe Gestures):** Cukup usap layar ke kiri atau kanan untuk berpindah ke nama sebelum atau sesudahnya.

3. **Audio Pelafalan:**
   - Tombol dengarkan pelafalan bahasa Arab menggunakan *Web Speech API* & *Harmonic Solfeggio Chime* (528 Hz).

4. **Tasbih / Penghitung Dzikir Digital:**
   - Tersedia di halaman detail setiap nama dengan target 33x, 99x, 100x, atau hitungan bebas.
   - Dilengkapi reset dan getaran haptic setiap sentuhan.

5. **Kuis Hafalan Interaktif:**
   - Uji ingatan dan hafalan 99 nama Allah dengan kuis pilihan ganda 4 opsi.

6. **Koleksi Favorit & Riwayat Terakhir Dibaca:**
   - Simpan nama-nama yang ingin sering dibaca ke tab Favorit (tersimpan lokal di memori HP).
   - Melanjutkan bacaan terakhir dengan sekali ketuk dari Beranda.

7. **Pencarian Cepat & Filter Rentang:**
   - Cari berdasarkan nomor (1–99), tulisan Arab, Latin, maupun arti bahasa Indonesia.
   - Filter cepat rentang 1–33, 34–66, 67–99, atau Semua.

8. **Mode Gelap / Dark Mode:**
   - Kenyamanan membaca saat malam hari atau waktu tahajjud.

9. **100% Offline (Service Worker):**
   - Setelah dibuka sekali di ponsel, aplikasi tetap bisa diakses kapan pun meski tanpa kuota internet atau saat mode pesawat (*airplane mode*).

---

## 🚀 Cara Menghubungkan ke GitHub & Hosting di GitHub Pages

Aplikasi ini menggunakan struktur file statis murni tanpa ketergantungan server khusus (*zero-build*), sehingga langsung dapat di-hosting secara gratis di **GitHub Pages**.

### Langkah 1: Buat Repository di GitHub
1. Buka [GitHub](https://github.com) dan login ke akun Anda.
2. Klik tombol **New Repository** (atau tanda `+` di kanan atas).
3. Beri nama repository, misalnya: `99AsmaulHusna` atau `asmaul-husna`.
4. Pilih opsi **Public**.
5. Jangan centang "Add a README file" (karena kita sudah menyiapkannya secara lokal).
6. Klik **Create repository**.

### Langkah 2: Upload / Push Kode dari Komputer Anda
Buka Terminal / PowerShell di folder proyek ini (`99AsmaulHusna`), lalu jalankan perintah berikut:

```bash
# 1. Inisialisasi Git
git init

# 2. Tambahkan semua file proyek
git add .

# 3. Buat commit pertama
git commit -m "feat: inisialisasi PWA Asmaul Husna untuk iPhone Safari"

# 4. Ganti branch utama menjadi main
git branch -M main

# 5. Sambungkan ke repository GitHub Anda (ganti USERNAME dan REPO_NAME)
git remote add origin https://github.com/USERNAME/99AsmaulHusna.git

# 6. Push kode ke GitHub
git push -u origin main
```

*(Ganti `USERNAME` dengan nama akun GitHub Anda).*

---

### Langkah 3: Aktifkan Fitur GitHub Pages
1. Di halaman repository GitHub Anda, klik tab **Settings** (di sebelah kanan atas).
2. Di bilah menu sebelah kiri, klik menu **Pages** (di bawah bagian *Code and automation*).
3. Pada bagian **Build and deployment**:
   - **Source**: Pilih **Deploy from a branch**.
   - **Branch**: Pilih **`main`** dan folder **`/ (root)`**.
4. Klik tombol **Save**.
5. Tunggu 1–2 menit hingga proses deploy selesai. Halaman Anda akan aktif di alamat:
   ```
   https://USERNAME.github.io/99AsmaulHusna/
   ```

---

## 📱 Cara Membuka & Memasang di iPhone (iOS Safari)

Setelah GitHub Pages aktif, Anda bisa langsung mengaksesnya dari smartphone:

1. **Buka Safari:** Buka peramban **Safari** di iPhone Anda (pastikan menggunakan Safari untuk fitur PWA penuh).
2. **Kunjungi Alamat:** Masukkan URL GitHub Pages Anda (misal: `https://USERNAME.github.io/99AsmaulHusna/`).
3. **Ketuk Tombol Share:** Ketuk ikon **Bagikan (Share)** di bagian tengah bilah menu bawah Safari (ikon kotak dengan panah ke atas: `⎋ / [↑]`).
4. **Pilih Tambah ke Layar Utama:** Gulir menu ke bawah lalu ketuk **"Tambah ke Layar Utama" (Add to Home Screen)**.
5. **Konfirmasi:** Ketuk **"Tambah" (Add)** di pojok kanan atas.
6. **Selesai!** Ikon aplikasi **Asmaul Husna** akan muncul di layar utama iPhone Anda. Saat diketuk, aplikasi akan terbuka dalam **layar penuh (full-screen)** tanpa bilah alamat Safari, persis seperti aplikasi App Store asli!

---

## 📂 Struktur Berkas Proyek

```text
99AsmaulHusna/
├── index.html              # Halaman utama aplikasi (Mobile-first, semantic HTML5)
├── manifest.webmanifest    # Konfigurasi PWA standar modern
├── manifest.json           # Fallback manifest PWA
├── sw.js                   # Service Worker (offline cache engine)
├── .gitignore              # Berkas yang diabaikan Git
├── README.md               # Dokumentasi lengkap proyek
├── css/
│   └── style.css           # Styling modern iOS Safari, safe-area, animasi, dark mode
├── data/
│   └── asmaul-husna.json   # Basis data JSON 99 Asmaul Husna terverifikasi
├── js/
│   ├── data.js             # Basis data 99 Asmaul Husna (format JS modul/global)
│   ├── wheel.js            # Engine Roda 99 Segmen SVG & pemutar audio otomatis
│   ├── app.js              # Logika aplikasi (navigasi, pencarian, tasbih, tema)
│   └── pwa.js              # Registrasi Service Worker & petunjuk instalasi iPhone
└── icons/
    ├── apple-touch-icon.png# Ikon khusus iPhone Home Screen (180x180)
    ├── icon-192.png        # Ikon PWA standar (192x192)
    ├── icon-512.png        # Ikon PWA high-res & splash screen (512x512)
    ├── favicon.png         # Ikon tab peramban
    └── icon.svg            # Ikon vektor resolusi tak terbatas
```

---

## 📜 Lisensi & Sumber Data
Konten Asmaul Husna, teks Arab, transliterasi Latin, makna, dan referensi ayat dirangkum berdasarkan rujukan kitab-kitab Islam mu'tabar dan Al-Qur'an Al-Karim. Proyek ini bebas digunakan untuk tujuan edukasi dan dakwah.
