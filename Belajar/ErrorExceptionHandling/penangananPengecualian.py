# Proses penanganan pengecualian menggunakan pernyataan try yang berpasangan dengan except.
# Misalnya kita ingin menangani pengecualian yang terjadi
# jika ada pembagian angka dengan nilai nol(0).Contoh :

# >> > z = 0
# >> > 1 / z
#
# Traceback(most recent call last):
# File"<stdin>", line 1, in < module >
# ZeroDivisionError: division by zero

# >> > try:
#     ...
#     x = 1 / z
# ...
# print(x)
# ... except ZeroDivisionError:
# ...
# print('tidak bisa membagi angka dengan nilai nol')

# tidak bisa membagi angka dengan nilai nol
