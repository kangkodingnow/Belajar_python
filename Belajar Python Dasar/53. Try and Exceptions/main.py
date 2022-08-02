"""
try:
    a = 1/0
except:
    print("error pembagi nol")

print("akhir dari program")
"""

while True:
    try:
        Pembilang = int(input("masukkan angka Pembilang:"))
        Penyebut = int(input("masukkan angka Penyebut:"))
        hasil = Pembilang/Penyebut
        break
    
    except ValueError:
        print("yang anda masukkan bukan angka\n")
   
    except ZeroDivisionError:
        print("angka pembilang yang anda masukkan adalah 0, pilih yang lain\n")

    except Exception as err:
        print(err) #Menampilkan error dengan bahasa inggris

"""
Type of Exceptions errors;
1. IOError #input output error
2. importError #Mengatasi jika tidak ada package
3. ValueError 
4. Division by Zero
5. KeyboardInterrupted
6. EOFError
"""


print("berhasil, anda memasukkan angka:",hasil)