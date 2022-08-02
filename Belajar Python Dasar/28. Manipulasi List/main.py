##operasi

#index  0(-3)    1(-2)     2(-1)
data = ["ucup","otong","dudung"]

#mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data [-1]
print(f"data terkahir adalah = {data_terakhir}")

data_ucup = data [-3]
print(f"data ucup = {data_ucup}")

#mengambil info dari jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

#manipulasi data list
#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}")

#menambah di akhir llist
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

#menambah list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

#merubah data
#kita ubah data 2 mejadi michael
data[2] = "Michael"
print(f"data rubah = \n{data}")

#meremove data
data.remove("Ujang")
print(f"data remove = \n{data}")

#data.remove("Usep" akan eror karena huruf harus sesuai yaitu "usep")

#meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)