# Mini Project: Sistem Penilaian Nilai Ujian

# Input nilai dari pengguna
nilai = int(input("Masukkan nilai ujian (0-100): "))

# Logika menggunakan if, elif, else
if nilai >= 85:
    print("Grade: A - Sangat Baik")
elif nilai >= 70:
    print("Grade: B - Baik")
elif nilai >= 55:
    print("Grade: C - Cukup")
elif nilai >= 40:
    print("Grade: D - Kurang")
else:
    print("Grade: E - Sangat Kurang")

print("Program selesai.")
