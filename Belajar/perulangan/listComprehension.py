# membuat list dengan inline loop dan if

# contoh 1 : membuat nilai kuadrat dari semua item dalam list
# cara 1
angka = [1, 2, 3, 4, 5]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
print('==================')

# cara ke dua dengan list comprehension
nilai = [1, 2, 3, 4, 5]
pangkat_2 = [n**2 for n in nilai]
print(pangkat_2)

# sintaks dasar lis comprehension
# new_list = [expression for_loop_one_or_more condition]
