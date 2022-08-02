#scope variable: local
namaKucing = 'casandra'
def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')
print('nama kucing saya menjadi',namaKucing)

#scope variable: global
namaKucing = 'casandra'
makananKucing = 'royal canin'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakananKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('ketie')
kasihMakananKucing('universal','alex')
print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)