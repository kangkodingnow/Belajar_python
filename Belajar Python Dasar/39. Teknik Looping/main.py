#teknik looping

nama_band = ["Payung Teduh","Fourtwenty","Dialag Dini Hari","Mr.Sonjaya","Parahyena"]
kumpulan_lagu = ["Akad","Zona Nyaman","Rumahku","Sang Filsuf","Sindoro"]

#enumerate

for index,band in enumerate(nama_band):
    print(index,':',band)

#ZIP

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,"menyanyikan lagu yang berjudul:",lagu)

playlist = {'baby baby','ada apa dengan cinta','cenat cenut','jaran goyang'}
for lagu in sorted(playlist):
    print(lagu)

print('='*20)
#Dictionary
playlist2 = {'Payung Teduh': 'akad', 'Fourtwenty': 'Zona Nyaman','Dialog Dini Hari':'Rumahku'}
for i in playlist2.items():
    print(i)

