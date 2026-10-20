# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Siti Auliyaatunnisaa  
**NIM:** 2225250085  
**Kelas:** 3A

## Tujuan

Mempelajari penggunaan list dalam Python untuk menyimpan dan mengolah data numerik, menggunakan indeks dan slicing, memanipulasi elemen list, menghitung statistik, melakukan penyaringan data, serta membuat fungsi yang dapat digunakan kembali.

## Struktur Program

Folder `latihan/` berisi enam program latihan, yaitu pembuatan list, indeks dan slicing, manipulasi list, agregasi nilai, filter kelulusan, dan fungsi statistik.

Folder `praktik/` berisi program `analisis_nilai_mahasiswa.py` yang digunakan untuk menganalisis sepuluh nilai mahasiswa, menghitung statistik, menentukan kelulusan berdasarkan batas nilai 60, serta menampilkan ringkasan hasil analisis.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code dari direktori utama repository.

```bash
python latihan/01_buat_list.py
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
python praktik/analisis_nilai_mahasiswa.py
```

Jika menggunakan lingkungan yang menjalankan Python melalui perintah `python3`, ganti `python` dengan `python3`.

## Test Case

Pengujian dilakukan menggunakan beberapa data numerik untuk memastikan fungsi statistik dan kelulusan berjalan dengan benar.

| Data uji | Hasil yang diharapkan | Status |
|---|---|---|
| `[60, 70, 80]` | Rata-rata 70.00 | Perlu diuji |
| `[60, 70, 80]` | Minimum 60 dan maksimum 80 | Perlu diuji |
| `[60, 70, 80]` | Jumlah lulus 3 | Perlu diuji |
| `[59, 60, 61]` | Nilai lulus `[60, 61]` | Perlu diuji |
| `[]` | Rata-rata 0 tanpa error | Perlu diuji |

Status pengujian diperbarui setelah program benar-benar dijalankan.

## Refleksi

Melalui latihan ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel. Indeks digunakan untuk mengakses elemen tertentu, sedangkan slicing digunakan untuk mengambil sebagian elemen list. Saya juga memahami bahwa fungsi membantu membuat program lebih terstruktur dan dapat digunakan kembali.

Salah satu hal yang perlu diperhatikan adalah penggunaan batas indeks pada slicing serta penanganan list kosong agar program tidak mengalami kesalahan ketika menghitung rata-rata.