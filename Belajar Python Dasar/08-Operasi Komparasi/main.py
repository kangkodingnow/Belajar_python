#operasi komparasi

#setiap hasil dari operasi adalah boolean

# >,<,>=,<=,==,, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('===========lebih besar dari(>)')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b,'>', 2, '=', hasil)

#kurang dari
print('============ kurang dari(<)')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=',hasil)
hasil = b < 2
print(b,'<',2,'=', hasil)

# lebih dari samadengan
print('============ lebih dari samadengan(<=)')
hasil = a>= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b,'>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

#kurang dari samadengan <=
print('============= kurang dari samadengan(<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

#sama dengan (==)
print('============= samadengan(==)')
hasil = a == 4
print(a, '==', 4,"=", hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

#tidak samadengan(!=)
print('============ tidak samadengan(!=)')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

#'is' sebagai komparasi object identity
print('=============== objek identity')
x = 5 #ini adalah assigment membuat object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 #ini adalah assigment membuat object
y = 6
print('nilai x =', x,', id = ', hex(id(x)))
print('nilai y =', y,', id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)
print('x is y =', hasil)

print('================ object identity(is not)')
x = 5 #ini adalah assigment embuat object
y = 5
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex (id(x)))
hasil = x is not y
print('x is y =', hasil)

x = 5 #ini adalah assigment membuat object
y = 6
print('nilai x =',x, ', id = ', hex(id(x)))
print('nilai y =', y,', id = ', hex(id(y)))
hasil = x is not y 
print('x is y =', hasil)
print('x is y =', hasil)