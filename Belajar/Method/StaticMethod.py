# sebuah fungsi yang mengubah metode menjadi metode statis (static method).
# Metode statis (static method) tidak menerima masukan argumen pertama secara implisit.

# contohnya :
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return 'hello world'

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

# Pemanggilan dari class

# a = Kalkulator.kali_angka(2, 3)
# print(a)

# pemanggilan dari objek
# k = Kalkulator()
# a = k.kali_angka(2, 3)
# print(a)