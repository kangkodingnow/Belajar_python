#latihan perulangan membuat segitiga

sisi = 10

#1. menggunakan for

#dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# 2. menggunakan while
print("="*20)
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir while")

#3. hanya ganjil saja
print("="*20)
print("awal while")
count = 1
while True:
    if (count%2):
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        #akan kembali ke atas jika genap
        count += 1
        continue
    #akan break jika count melebihi sisi
    if count > sisi:
        break
print("akhir while")

#3. hanya ganjil saja
print("="*20)
print("awal while")
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    if (count%2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
print("akhir while")