#operasi opertaor bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n',5*'=','or', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))#disini 0 menunjukkan jika kosong, 8 adalah banyaknya rentang, b adalah binarynya
print('nilai :', b,' , binary :', format(b, '08b'))
print(15*'-', '(|)')
print('nilai :', c,' , binary :', format(c, '08b'))

#bitwise AND (&)
c = a & b
print('\n',5*'=','AND', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))
print('nilai :', b,' , binary :', format(b, '08b'))
print(15*'-', '(&)')
print('nilai :', c,' , binary :', format(c, '08b'))

#bitwise XOR(^)
c = a ^ b
print('\n',5*'=','XOR', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))
print('nilai :', b,' , binary :', format(b, '08b'))
print(15*'-', '(^)')
print('nilai :', c,' , binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~ a
print('\n',5*'=','NOT', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))
print('nilai :', b,' , binary :', format(b, '08b'))
print(15*'-', '(~)')
print('nilai :', c,' , binary :', format(c, '08b'))

d = 0b0000001001
e = 0b1111111111
print('nilai :', e^d,' binary :', format(e^d, '08b'))

#shifting

#shifting right(>>)
c = a >> 2
print('\n',5*'=','>>', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))
print(15*'-', '(>>)')
print('nilai :', c,' , binary :', format(c, '08b'))

# shifting left(<<)
c = a << 2
print('\n',5*'=','<<', 5*'=')
print('nilai :', a,' , binary :', format(a, '08b'))
print(15*'-', '(<<)')
print('nilai :', c,' , binary :', format(c, '08b'))




