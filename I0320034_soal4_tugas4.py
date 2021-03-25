# Pendaftar
usia = 21
hasil_ujian = "Lulus"

# Syarat pendaftaran :
# Usia minimal
lulus_usia = usia >= 21
# Lulus ujian kualifikasi
syarat_ujian = "Lulus ujian kualifikasi"

# Hasil
print("Hasil pendaftaran :")
if hasil_ujian in syarat_ujian:
    if lulus_usia:
        print("Anda dapat mendaftar di kursus")
    if not lulus_usia:
        print("Anda tidak dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")
