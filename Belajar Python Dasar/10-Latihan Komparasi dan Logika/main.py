# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3-----------10++++++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\n atau\n lebih besar dari 10\n:"))

#++++++3--------------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 =", isKurangDari)

#----------------10+++++++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

#+++++++3---------10+++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan:", isCorrect)

# ------3+++++++++10-------
# kasus irisan
print("\n", 10*"=", "\n")
inputUser = float(input("masukkan angka yang bernilai \n lebih dari 3 \n dan \n kurang dari 10\n"))

# ------3+++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("kebih dari dari 10 =", isLebihDari)

# ++++++++++++++++10-------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

# ------3++++++++10-------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)
