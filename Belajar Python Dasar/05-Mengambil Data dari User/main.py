#data yang dimasukkan pasti string
data = input("masukkan data: ")
print("data =", data, ", type =", type(data))

#jika kita ingin mengambil int, maka
angka = float(input("masukkan angka:"))
print("data =", angka, ", type =", type(angka))
angka = int(input("masukkan angka: "))
print("data =", angka, ", type =", type(angka))

#bagaimana dengan boolean
biner = bool(int(input("masukkan nilai boolen: ")))

print("data = ", biner, ", type =", type(biner))