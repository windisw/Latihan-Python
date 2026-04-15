# Mini Project: Cek Nilai Ujian

# Meminta input dari pengguna
nilai = int(input("Masukkan nilai ujian (0-100): "))

# Logika if-else
if nilai >= 0 and nilai <= 100:
    if nilai >= 75:
        print("Selamat, kamu lulus!")
    else:
        print("Maaf, kamu belum lulus.")
else:
    print("Nilai tidak valid, harus antara 0-100.")
