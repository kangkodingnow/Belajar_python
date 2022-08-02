class mahasiswa():
    nama = "nama"
    
    def belajar(self,kondisi):
        print(self.nama,"sedang belajar",kondisi)
    def tidur(self):
        print(self.nama,"tidur di kelas")
# main programnya
otong = mahasiswa()
ucup = mahasiswa()
otong.nama = "otong surotong"
ucup.nama = "michael ucup"
print(otong.nama)
print(ucup.nama)
otong.belajar("dengan giat")
ucup.tidur()
