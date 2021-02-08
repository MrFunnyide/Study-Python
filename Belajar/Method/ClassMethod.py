# adalah fungsi yang mengubah metode menjadi metode dari class (class method).
# contohnya :

class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return 'hello world'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

# Pemanggilan dari objek

# k = Kalkulator()
# print(k.tambah_angka(1, 2))

# pembanggilan dari  class
# Kalkulator.tambah_angka(1, 2)  # tanpa perlu memberikan masukan untuk argumen cls