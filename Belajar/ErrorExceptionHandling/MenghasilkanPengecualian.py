# (raise exceptions) / mengahsilkan pengecualian
# Misalnya dalam contoh berikut, Anda mewajibkan sebuah dictionary memiliki kunci (key) total:

# >>> d = {'ratarata': '10.0'}
# >>> if 'total' not in d:
# ...     raise KeyError('harus memiliki total')
# ...
# Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
# KeyError: 'harus memiliki total'