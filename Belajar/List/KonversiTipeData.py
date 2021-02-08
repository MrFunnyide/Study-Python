print(float(5))  # standar type (Konversi Tipe Data)
print(int(10.6))  # float ke int, menyebabkan kondisi floor(hilang nilai di belakang koma
print(int(-10.6))  # float ke int, menyebabkan kondisi floor(hilang nilai di belakang koma
print(float('2.5'))  # Konversi dari String ke float dan sebaliknya
print(str(2.5))  # Konversi dari String ke float dan sebaliknya
print("================")  # print(int(1p)) kode di sampaing akan menghasilkan  error

# Konversi Kumpulan Data
print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list('Hello'))
print("================")

# Untuk konversi ke dictionary, data harus memenuhi persyaratan key-value.
# Berikut adalah dua contoh konversi:
# 1. List dari beberapa List yang isinya pasangan nilai menjadi Dictionary.
# 2. Serta konversi List dari beberapa Tuple yang isinya pasangan nilai menjadi Dictionary.

print(dict([[1, 2], [3, 4]]))
print("================")
print(dict([(3, 26), (4, 44)]))
