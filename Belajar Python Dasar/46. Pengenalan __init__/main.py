class mahasiswa():
    nama = "nama"
    
    def __init__(self,input_nama,input_nim):#init=initialization
       self.nama = input_nama
       self.nim = input_nim
       print(self.nama)
       print(self.nim)
    def belajar(self,kondisi):
        print(self.nama,"sedang belajar",kondisi)
    def tidur(self):
        print(self.nama,"tidur di kelas")
# main programnya
otong = mahasiswa("otong surotong",133020020)

"""
ucup = mahasiswa()
otong.nama = "otong surotong"
ucup.nama = "michael ucup"
print(otong.nama)
print(ucup.nama)
otong.belajar("dengan giat")
ucup.tidur()
"""
