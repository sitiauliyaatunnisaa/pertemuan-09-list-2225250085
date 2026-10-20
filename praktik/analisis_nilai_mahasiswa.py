
# Input: Sepuluh nilai mahasiswa.
# Proses: Menghitung statistik dan memeriksa kelulusan.
# Output: Ringkasan nilai dan daftar nilai yang lulus.

def rata_rata(data):
    """Menghitung rata-rata dan menangani list kosong."""
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan list nilai yang memenuhi batas kelulusan."""
    lulus = []

    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)

    return lulus


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai) if banyak_data > 0 else None
maksimum = max(nilai) if banyak_data > 0 else None

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Menampilkan ringkasan
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {banyak_data}")
print(f"Total nilai         : {total}")
print(f"Rata-rata           : {rata:.2f}")
print(f"Nilai minimum       : {minimum}")
print(f"Nilai maksimum      : {maksimum}")
print(f"Batas kelulusan     : 60")
print(f"Jumlah mahasiswa lulus       : {jumlah_lulus}")
print(f"Jumlah belum lulus           : {jumlah_belum_lulus}")
print(f"Daftar nilai yang lulus      : {lulus}")

# Pengujian fungsi dengan beberapa test case
print("\n=== PENGUJIAN FUNGSI ===")

data_uji = [60, 70, 80]
print(f"Rata-rata [60, 70, 80] = {rata_rata(data_uji):.2f}")
print(f"Minimum / maksimum = {min(data_uji)} / {max(data_uji)}")
print(f"Jumlah lulus = {len(nilai_lulus(data_uji))}")

data_batas = [59, 60, 61]
print(f"Nilai lulus [59, 60, 61] = {nilai_lulus(data_batas)}")

data_kosong = []
print(f"Rata-rata list kosong = {rata_rata(data_kosong)}")