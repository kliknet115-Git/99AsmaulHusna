# PROMPT GOOGLE ANTIGRAVITY — ASMAUL HUSNA 99 RADIAL READER

## 1. Peran dan tujuan

Bertindak sebagai Senior Frontend Engineer, UI/UX Designer, dan PWA Engineer. Kembangkan fitur utama aplikasi **Asmaul Husna – 99 Nama Allah** berdasarkan dua referensi visual yang disertakan:

1. `reference/asmaul-husna-wheel-mockup.png` — mockup UI digital, sebagai referensi visual utama.
2. `reference/original-hand-sketch.jpeg` — sketsa awal pengguna, sebagai referensi struktur dan ide roda 99 segmen.

Bangun antarmuka yang benar-benar interaktif, bukan menampilkan gambar referensi sebagai screenshot/background. Semua elemen roda, angka, teks Arab, kontrol, dan animasi harus dibuat sebagai komponen UI aktual.

Target utama adalah iPhone melalui Safari dan aplikasi yang dibuka dari Home Screen sebagai PWA. Tetap responsif pada Android dan desktop.

## 2. Prinsip visual yang wajib diikuti

Ikuti komposisi mockup:

- Satu layar utama dengan orientasi portrait.
- Latar belakang gradasi biru muda ke putih, dengan aksen navy dan gold.
- Header bertema islami dengan judul “Asmaul Husna” dan subjudul “99 Nama-nama Allah”.
- Roda melingkar besar di tengah layar, terdiri dari tepat 99 segmen radial.
- Area pusat roda menampilkan nama yang sedang aktif: nomor, tulisan Arab, transliterasi, arti, ringkasan makna, dan referensi jika telah diverifikasi.
- Segmen aktif diberi warna biru yang jelas, sedangkan segmen lain memakai putih/biru sangat muda dengan garis pemisah halus dan aksen emas.
- Di bawah roda terdapat kontrol: Ulangi, Sebelumnya, Play/Pause, Berikutnya, dan Auto 1–99.
- Di bawah kontrol terdapat indikator progres nomor dan progress bar.
- Bagian bawah memiliki akses ke Daftar 1–99, Favorit, Terakhir Dibaca, dan Tentang.
- Gunakan ornamen islami secara halus. Jangan membuat dekorasi mengganggu keterbacaan.

Warna acuan:

- Navy: `#17365D`
- Royal blue: `#2563EB`
- Pale blue: `#EAF2FF`
- Background: `#F7F9FE`
- Soft gold: `#D6B779`
- Main text: `#17233B`

Typography:

- UI: system font iOS / Inter.
- Arab: font lokal yang mendukung Arabic shaping dan harakat, misalnya Noto Naskh Arabic atau Amiri.
- Teks Arab harus memiliki line-height lapang dan tidak terpotong.

## 3. Roda 99 segmen — persyaratan utama

Buat roda menggunakan SVG dinamis atau teknologi vektor yang setara. Jangan menggunakan gambar statis untuk roda.

Persyaratan:

1. Roda terdiri dari tepat 99 segmen yang sama besar, mewakili nomor 1 sampai 99.
2. Setiap segmen dapat dipilih dengan sentuhan/tap.
3. Tampilkan nomor pada setiap segmen. Pastikan urutan melingkar 1, 2, 3, ... 99 benar, tanpa nomor hilang atau duplikat.
4. Nomor yang sedang aktif diberi highlight biru dan ukuran/kontras yang cukup.
5. Saat nomor aktif berubah, highlight berpindah ke segmen yang sesuai.
6. Area tengah otomatis berubah mengikuti data nomor aktif.
7. Ketika pengguna memilih segmen secara manual, mode otomatis dihentikan sementara agar tidak terjadi konflik kontrol.
8. Buat roda tetap proporsional pada lebar layar kecil. Prioritaskan area sentuh yang nyaman.
9. Tambahkan akses alternatif berupa daftar 1–99 bagi pengguna yang sulit memilih segmen yang rapat.
10. Pastikan roda dapat digunakan dengan keyboard pada desktop dan memiliki label aksesibilitas.

Arah dan posisi awal roda boleh menyesuaikan mockup, tetapi urutan angka harus konsisten dan mudah dipahami. Dokumentasikan arah urutannya.

## 4. Perilaku tombol dan mode PLAY

Fitur ini berfungsi sebagai **mode baca otomatis**. PLAY bukan sekadar animasi dekoratif.

### Play

- Memulai dari nomor aktif saat ini.
- Jika belum ada nomor aktif, mulai dari nomor 1.
- Menampilkan nama aktif di tengah roda.
- Menahan setiap nama selama durasi baca yang dipilih.
- Setelah durasi habis, pindah ke nomor berikutnya dan memperbarui highlight serta isi panel tengah.
- Lanjut sampai nomor 99.
- Jangan mempercepat perpindahan secara berlebihan; pengguna harus punya waktu membaca.

### Pause / Resume

- Pause menghentikan perpindahan otomatis tanpa mengubah nomor aktif.
- Resume melanjutkan dari nomor yang sama, bukan mengulang dari nomor 1.

### Sebelumnya / Berikutnya

- Berpindah satu nomor setiap kali ditekan.
- Memperbarui highlight roda dan konten tengah.
- Bila mode otomatis sedang berjalan, perpindahan manual mengambil alih dan timer otomatis di-reset/dihentikan dengan perilaku yang konsisten.

### Ulangi

- Kembali ke nomor 1.
- Jika mode otomatis aktif, ulangi rangkaian dari nomor 1.
- Jika mode otomatis tidak aktif, cukup pilih nomor 1.

### Auto 1–99

- Mengaktifkan urutan otomatis dari nomor 1 sampai 99.
- Gunakan kontrol Play/Pause yang sama untuk memulai dan menghentikan.
- Setelah nomor 99, tampilkan status selesai.
- Sediakan pilihan apakah berhenti di 99 atau mengulang dari 1. Default: berhenti di 99.

### Durasi baca

Sediakan pilihan durasi per nama, misalnya 5, 8, 10, dan 15 detik. Default 8 detik. Tampilkan durasi yang dipilih secara jelas. Timer harus dibersihkan dengan benar ketika pengguna pause, pindah halaman, memilih nama manual, atau komponen di-unmount.

Jangan menggunakan `setInterval` yang dapat menumpuk. Gunakan mekanisme timer/state yang aman dan bersihkan timeout saat state berubah.

## 5. Isi panel tengah

Untuk nama aktif, tampilkan:

1. Nomor urut, contoh `1 / 99`.
2. Tulisan Arab dengan harakat.
3. Transliterasi Latin.
4. Arti Bahasa Indonesia.
5. Penjelasan singkat yang telah ditinjau.
6. Referensi Al-Qur'an atau hadis hanya jika sumbernya benar-benar mendukung keterangan tersebut.

Jika referensi tidak tersedia atau belum diverifikasi, jangan membuat referensi palsu. Sembunyikan bagian referensi atau tampilkan status “Referensi sedang diverifikasi”.

Tambahkan tombol favorit pada panel/header. Status favorit tersimpan pada perangkat.

## 6. Data dan integritas konten agama

Pisahkan seluruh konten dari kode UI di file JSON, misalnya `src/data/asmaul-husna.json`.

Skema minimal setiap data:

```json
{
  "number": 1,
  "slug": "ar-rahman",
  "arabic": "",
  "transliteration": "",
  "meaning": "",
  "description": "",
  "references": [],
  "verification_status": "pending"
}
```

Ketentuan penting:

- Harus tersedia tepat 99 record dengan nomor unik 1–99.
- Jangan menyalin tulisan Arab, angka, transliterasi, atau dalil yang tampak pada mockup gambar sebagai sumber data. Gambar hanya acuan desain dan dapat mengandung teks/angka ilustratif yang tidak akurat.
- Jangan mengarang atau melengkapi sendiri konten agama yang belum diverifikasi.
- Jangan menandai data sebagai `verified` tanpa pemeriksaan sumber yang dapat ditelusuri.
- Jika data belum tersedia, tampilkan placeholder yang jujur seperti “Konten menunggu verifikasi”, bukan teks Arab atau arti rekaan.
- Sumber konten harus dicatat per nama, termasuk URL, kitab/surah, nomor ayat/hadis, dan catatan status penilaian.
- Bedakan nama Allah, sifat, dan lafaz yang diperselisihkan. Jangan menyatakan bahwa satu daftar populer merupakan satu-satunya susunan yang disepakati tanpa dasar yang jelas.

Gunakan data final yang sudah disetujui pemilik proyek. Jangan mengubah database produksi hanya karena AI mengusulkan koreksi.

## 7. Halaman/fitur pendukung

Implementasikan akses berikut tanpa menghilangkan fokus halaman utama:

- **Daftar 1–99:** daftar vertikal dengan nomor, tulisan Arab, Latin, dan arti; tap item memilih nomor tersebut dan kembali ke tampilan roda atau membuka detail.
- **Favorit:** daftar nama yang disimpan.
- **Terakhir Dibaca:** simpan posisi terakhir secara lokal.
- **Tentang:** informasi aplikasi dan sumber referensi.
- **Pengaturan:** durasi otomatis, pilihan berhenti/ulang setelah nomor 99, dan preferensi tampilan.

Gunakan `localStorage` untuk favorit, posisi terakhir, dan preferensi. Pastikan data ini tidak terhapus ketika konten aplikasi diperbarui.

## 8. PWA dan optimasi iPhone

Aplikasi harus mengikuti PRD proyek yang sudah ada. Pastikan:

- React + TypeScript + Vite (jika stack proyek saat ini memang menggunakan stack tersebut; periksa repository sebelum mengubah konfigurasi).
- PWA manifest, service worker, cache aset inti, dan offline fallback.
- Mendukung GitHub Pages dengan Vite `base` path yang sesuai nama repository.
- Navigasi tidak menghasilkan 404 saat halaman di-refresh.
- Gunakan HTTPS.
- Tambahkan `apple-touch-icon` dan metadata iOS yang diperlukan.
- Mendukung `display: standalone`.
- Gunakan `100dvh` dengan fallback yang sesuai.
- Gunakan `env(safe-area-inset-top)` dan `env(safe-area-inset-bottom)`.
- Hindari horizontal scrolling.
- Area sentuh tombol minimal 44 × 44 px.
- Tidak mengandalkan hover.
- Font Arab tersedia secara lokal/offline.
- Animasi harus halus tetapi hemat baterai.

## 9. Aksesibilitas dan kenyamanan membaca

- Kontras teks harus memadai.
- Status aktif tidak boleh dibedakan hanya dengan warna; sertakan indikator bentuk/label.
- Tombol memiliki `aria-label`.
- Hormati preferensi `prefers-reduced-motion`.
- Sediakan kontrol untuk memperbesar ukuran tulisan Arab.
- Jangan membuat pergantian otomatis terlalu cepat.
- Saat pengguna membuka pengaturan atau daftar, jangan terus memajukan nomor di belakang layar.

## 10. Komponen yang disarankan

Pisahkan implementasi menjadi komponen yang mudah dirawat, misalnya:

- `AsmaulHusnaWheel`
- `WheelSegment`
- `ActiveNamePanel`
- `PlaybackControls`
- `ReadingProgress`
- `ReadingDurationSelector`
- `BottomNavigation`
- `AsmaulHusnaList`
- `FavoritesPage`
- `SettingsPage`

Buat hook terpisah untuk pengelolaan playback, misalnya `useAutoRead`, agar logika timer tidak bercampur dengan komponen visual.

## 11. Pengujian wajib

Sebelum menyatakan selesai, lakukan pengujian berikut:

1. Jumlah segmen tepat 99.
2. Nomor seluruh segmen 1–99 unik dan berurutan.
3. Tap nomor 1, 2, 50, dan 99 menampilkan data yang sesuai.
4. Play berjalan dari nomor aktif.
5. Auto 1–99 dimulai dari nomor 1.
6. Pause mempertahankan nomor aktif.
7. Resume melanjutkan dari nomor yang sama.
8. Next dan Previous berfungsi di batas nomor 1 dan 99.
9. Perpindahan dari 99 mengikuti pengaturan selesai/ulang.
10. Perubahan nomor memperbarui highlight segmen dan panel tengah secara bersamaan.
11. Timer tidak berjalan ganda setelah Play/Pause berulang.
12. Keluar dari halaman menghentikan timer otomatis.
13. Favorit dan terakhir dibaca tetap tersimpan setelah reload.
14. Tidak ada angka, teks Arab, atau referensi palsu dari gambar mockup yang masuk ke database.
15. Tampilan diuji pada lebar 320 px, 375 px, 390 px, 430 px, serta desktop.
16. Uji Safari iOS, termasuk mode Home Screen bila tersedia.
17. Uji offline setelah cache awal berhasil.
18. Uji GitHub Pages pada subpath repository.

## 12. Cara kerja Antigravity

Sebelum coding:

1. Baca `PRD.md` dan struktur repository saat ini.
2. Periksa file data Asmaul Husna yang sudah tersedia.
3. Baca kedua file referensi gambar di folder `reference/`.
4. Buat rencana implementasi singkat dan daftar file yang akan diubah.
5. Jangan menghapus atau mengganti fitur yang sudah ada tanpa alasan teknis.

Saat implementasi:

1. Buat roda SVG dinamis dengan 99 segmen.
2. Implementasikan state nomor aktif dan kontrol baca otomatis.
3. Hubungkan panel tengah ke data JSON.
4. Implementasikan favorit dan riwayat.
5. Pastikan desain konsisten dengan mockup.
6. Jalankan build, lint, dan tes yang tersedia.

Setelah implementasi, berikan ringkasan:

- File yang dibuat/diubah.
- Fitur yang berhasil diterapkan.
- Cara menjalankan secara lokal.
- Cara deploy ke GitHub Pages.
- Hasil pengujian dan keterbatasan yang belum selesai.

**Prioritas tertinggi:** kesesuaian visual dengan referensi, roda 99 segmen yang benar-benar berfungsi, mode baca otomatis yang nyaman, ketepatan data agama, dan kompatibilitas iPhone Safari.
