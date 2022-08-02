# looping dari list

#for loop
print("\nFor Loop")
kumpulan_angka = [1,2,3,4,5,6,7]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup","otong","dadang","dinding","dudung"]

for nama in peserta:
    print(f"nama = {nama}")

#for loop dan range 
print("\nFor Loop dan range")
kumpulan_angka = [10,3,4,6,9,6,7]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

#while loop
print("\nnwhie loop")
kumpulan_angka = [10,3,4,6,9,6,7]

panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

#list comprehension
print("\nlist comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data]

angka = [10,3,4,6,9,6,7]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#enumerate
print("\nenumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")