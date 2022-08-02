#set, himpunan 

superhero = set()

superhero.add("mak lampir")
superhero.add("wiro sableng")
superhero.add("si buta dari gua hantu")
superhero.add("gatot kaca")
superhero.add(212)

print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(genap))
print(ganjil.intersection(prima))