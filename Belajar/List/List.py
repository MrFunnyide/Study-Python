x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(x[5])  # artinya mengambil elemen dengan index 5 dari List x.
print(x[-1])  # artinya mengambil elemen dengan index paling belakang ke-1 dari List x.
print(x[3:5])  # artinya membuat list dari anggota elemen List x dengan index 3 hingga sebelum index 5"""
# (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 3-4).'''
print(x[:5])  # artinya membuat list dari anggota elemen List x paling awal hingga sebelum index 5
# (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 0-4).
print(x[-3:])  # artinya membuat list dari anggota elemen List x mulai index ke-3 dari belakang hingga paling belakang.
print(x[1:7:2])  # artinya membuat list dari anggota elemen List x dengan index 1 hingga sebelum index 7,
#  dengan "step" 2 (dalam hal ini hanya index 1, 3, 5).

print("=============")

x = [1, 2, 3]
x[2] = 4
print(x)

print("=============")

x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

print("=============")

Binatang = ['Ayam', 'Babi', 'Kucing', 'Panda', 'Naga', 'Ular']
del Binatang[3]
print(Binatang)
del Binatang[3]
print(Binatang)

print("=============")
