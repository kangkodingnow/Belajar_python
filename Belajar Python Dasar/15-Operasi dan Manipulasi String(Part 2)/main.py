# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal =" + salam)
salam = salam.upper()
print("upper =" + salam)

# merubah semua ke lower case
alay = "FARHAN KECE ABIEZZZ"
print("normal =" + alay)
alay = alay.lower()
print("lower =" + alay)

# merubah semua ke kapital di awal huruf
alay = "FARHAN KECE ABIEZZZ"
print("normal =" + alay)
alay = alay.title()
print("title =" + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower =" + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + " is upper =" + str(apakah_upper))

#isalpha() <-- untuk mengecek semuanya huruf
#isalnum() <-- huruf dan angka
#isdecimal() <-- angka saja
#isspace() <-- spasi, tab, newline(\n)
#istitle() <-- semua kata dimulai dengan huruf besar

judul = "it's okay not to be okay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title =" + str(cek_judul))

## mengecek komponen startswith() endswith() <-- keren

cek_start = "SangJangnim Oppa".startswith("SangJangnim")
print("start =" + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end =" + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm')) #mengembalikan ke bentuk listnya(liat line 53)

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(100, ":")
print("'" + tengah + "'")

# kebalikannya --> strip()
tengah = tengah.strip(":") # menghilangkan tanda (:)
print("'" + tengah + "'")
