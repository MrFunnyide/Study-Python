# kode yang sudah di berikan pass
# dan sudah mengantisipasi exception

import sys
data = ''
while(data != 'exit'):
    try:
        data = input('Tolong masukkan nilai int : ')
        print('mendapatkan integer : {} '.format(int(data)))
    except:
        if data == 'exit':
            pass  # keluar tanpa ada kesalahan apa pun
        else:
            print('error : {}'.format(sys.exc_info()[0]))