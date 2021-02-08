jumlah_baris = 10
baris = 0
bintang = 0
while baris < jumlah_baris:
    if (bintang) >= (baris + 1):
        print()
        baris = baris + 1
        bintang = 0
        continue
    print('*', end='')
    bintang = bintang + 1
