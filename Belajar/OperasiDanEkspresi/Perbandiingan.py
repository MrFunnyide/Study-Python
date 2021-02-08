from operator import *
print(5 < 3)  # false  (less than )
print(5 > 3)  # true  (greater than )
x = 3
y = 6
print(x <= y)  # true  (less than or equal to)
print(x >= y)  # false (greater than or equal to)
a = 2
b = 2
print(a == b)  # true ( equal to )
d = 'str'
e = 'Str'
print(e == d)  # false
print(e != d)  # true

# penggunaan le, lt, gt, ge, eq, ne

hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for function in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(function.__name__, function(hijau, kuning)))
