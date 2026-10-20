# Input: Sekumpulan nilai mahasiswa.
# Proses: Memeriksa nilai yang memenuhi batas kelulusan 60.
# Output: Menampilkan nilai lulus dan jumlahnya.

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")