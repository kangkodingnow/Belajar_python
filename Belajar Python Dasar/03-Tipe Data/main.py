# a = 10, a adalah variabel dengan nilai 10
#tipe data: angka satuan yang gak ada komanya(integer)
data_integer = 11
print("data :", data_integer)
print("-bertipe :", type(data_integer))

#tipe data: angka dengan koma(float)
data_float = 1.5
print("data :", data_float)
print("-bertipe :", type(data_float))

#tipe data: kumpulan karakter(string)
data_string = "ucup"
print("data :", data_string)
print("-bertipe :", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print("data :", data_bool)
print("-bertipe :", type(data_bool))

##tipe data khusus

#bilangan complex
data_complex = complex(5,6)
print("data :", data_complex)
print("-bertipe :", type(data_complex))

#tipe data dari bahasa c
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
data_c_long = c_long(102020200202020)
print("data : ", data_c_double)
print("-bertipe :", type(data_c_double))
print("data : ", data_c_long)
print("-bertipe :", type(data_c_long))

