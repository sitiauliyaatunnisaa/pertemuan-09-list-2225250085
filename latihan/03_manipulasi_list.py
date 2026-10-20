# Input: Tiga nilai awal dalam list.
# Proses: Mengubah, menambah, menyisipkan, dan menghapus elemen.
# Output: Menampilkan list setelah dimanipulasi.

nilai = [75, 80, 65]

nilai[1] = 82
nilai.append(90)
nilai.insert(1, 70)
nilai.remove(65)

print(f"List setelah perubahan = {nilai}")