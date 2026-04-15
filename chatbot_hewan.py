# Mini Project AI Chatbot Hewan
# List berisi
tuple (nama, kategori)
data_hewan = ("Kucing"
("Ayam",
"Mama lia"),
"Unggas"),
("Ikan",
"Pisces"),
("Ular",
"Reptil"),
("Burung", "Unggas")
# Set untuk kategori unik
kategori_unik = set( [kategori for →, kategori in data_hewan])
# Dictionary berisi deskripsi hewan
deskripsi_hewan = {
"Kucing": "Hewan mamalia yang suka bermain dan sering dijadikan pelihar
"Ayam": "Unggas yang sering dipelihara untuk diambil telur dan dagingny
"Ikan": "Hewan air yang bernapas dengan insang.",
"Ular": "Reptil yang tidak memiliki kaki dan sering melata.",
"Burung": "Unggas yang bisa terbang dengan sayapnya."
}
# Input dari
pengguna
pertanyaan = input("Masukkan nama hewan: ")
# Logika AI sederhana
if pertanyaan in deskripsi_hewan:
print (f"Kategori: {dict(data_hewan) [pertanyaan]}")
print(f"Deskripsi: {deskripsi_hewan [pertanyaan]}")
elif pertanyaan in kategori_unik:
print (f"Kategori {pertanyaan} berisi hewan: ") for nama, kategori in data_hewan: if kategori == pertanyaan:
print("-", nama)
else: print ("Maaf, saya belum tahu tentang itu.")
