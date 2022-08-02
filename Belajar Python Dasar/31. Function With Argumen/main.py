#fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bernama:',nama)
siswa('mario')

#fungsi dengan menggunakan keywords arguments
def guru(nama,pelajaran):
    print('guru ini bernama:',nama)
    print('mengajar:',pelajaran)
guru(nama='popong',pelajaran='senirupa')
guru(pelajaran='olahraga',nama = 'endang')

#fungsi dengan mengguanakan default arguments
def penjagaSekolah(nama,shift,galak='tidak'):
    print('penjaga sekolah ini bernama:',nama)
    print('shiftnya:',shift)
    print('galak?', galak)

penjagaSekolah('entis','malam')
penjagaSekolah('maman','malam',galak='sangat')



