print("Pintu masuk wahana cepet-cepetan")
print("Silahkan masukkan Nama , umur dan tinggi anda di bawah")
Nama = str(input("masukkan nama anda : "))
Umur = int(input("Masukkan Umur anda : "))
Tinggi = int(input("Masukkan Tinggi anda : "))

if Tinggi >= 170:
    print("Selamat datang ", Nama, "\nsilahkan masuk kewahana kami")
else:
    print("maaf ", Nama, "\nAnda belum bisa masuk kewahana kami")

print("============================")
bilangan = 4
if bilangan % 2 == 0:
    print('Bilangan {} adalah genap '. format(bilangan))
else:
    print('bilangan {} adalah ganjil'. format(bilangan))
