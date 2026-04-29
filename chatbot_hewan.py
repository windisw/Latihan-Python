# Mini Project AI Chatbot Hewan

# List berisi tuple (nama, kategori)
data_hewan = [
    ("Kucing", "Mamalia"),
    ("Ayam", "Unggas"),
    ("Ikan", "Pisces"),
    ("Ular", "Reptil"),
    ("Burung", "Unggas")
]

# Dictionary berisi deskripsi hewan
deskripsi_hewan = {
    "Kucing": "Hewan mamalia yang suka bermain dan sering dijadikan peliharaan.",
    "Ayam": "Unggas yang sering dipelihara untuk diambil telur dan dagingnya.",
    "Ikan": "Hewan air yang bernapas dengan insang.",
    "Ular": "Reptil yang tidak memiliki kaki dan sering melata.",
    "Burung": "Unggas yang bisa terbang dengan sayapnya."
}

# Input dari pengguna
pertanyaan = input("Masukkan nama hewan atau kategori: ")

# Logika AI sederhana
if pertanyaan in deskripsi_hewan:
    print(f"Kategori: {dict(data_hewan)[pertanyaan]}")
    print(f"Deskripsi: {deskripsi_hewan[pertanyaan]}")
else:
    print("Maaf, saya belum tahu tentang itu.")
