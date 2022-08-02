class mahasiswa():
    __nilai = 0 #private
    jurusan = "teknik tata boga"
    def __init__(self,input_nama,input_nim):#init=initialization
       self.nama = input_nama #public
       self.nim = input_nim#public
       print(self.nama)
       print(self.nim)

    def uts(self,input_nilai):
        self.__nilai += input_nilai
    
    def uas(self,input_nilai):
        self.__nilai += input_nilai
    
    def check_status(self):
        if self.__nilai <= 60:
            print(self.nama,"tidak lulus")
        else:
            print(self.nama,"lulus")
  
    def tidur(self):
        print(self.nama,"tidur di kelas")
# main programnya
otong = mahasiswa("otong surotong",133020020)
ucup = mahasiswa("michael ucup",105221036)

otong.uts(10)
otong.uas(40)

otong.check_status()

ucup.uts(30)
ucup.uas(100)

ucup.check_status()
"""
ucup = mahasiswa()
otong.nama = "otong surotong"
ucup.nama = "michael ucup"
print(otong.nama)
print(ucup.nama)
otong.belajar("dengan giat")
ucup.tidur()
"""
