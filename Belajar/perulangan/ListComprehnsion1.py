# contohKe3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # output ['d','i']

# dibandingkan dengan

# contohKe4 Implementasi dengan list comprehension
list_a = ['d', 'i', 'c', 'o']
list_b = ['d', 'i', 'n', 'g']
yang_Sama = [c for c in list_a for d in list_b if c == d]
print(yang_Sama)  # output ['d', 'i']

# contohKe5 Kecilkan semua huruf
list_c = ['Hello', 'World', 'In', 'Python']
small_list_c = [_.lower() for _ in list_c]
print(small_list_c)

# Anda tidak perlu bingung saat melihat kode di Internet yang menuliskan seperti contoh di atas,
# karena garis bawah (underscore) termasuk penamaan variabel yang valid
# Secara umum "_" biasa digunakan sebagai throwaway variable (variabel tidak penting).
