s = 'Hello World!'
print(s[4])  # Ambil karkater kelilma dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = 'Halo Dunia!'  # ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print(s)
