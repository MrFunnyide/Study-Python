# STRUKTUR UMUM
# for item in items:
#     if cari(item):
#         # ditemukan
#         proses_item()
#         break
# else:
#     # item tidak ditemukan
#     not_found_in_container()

# STRUKTUR PSEUDOCODE YANG DI IKUTI DALAM MEMBUAT ELSE
# PADA PERULANGAN ADALAH :

# if any(something_about(thing)for each thing in container)
#     do_something(that_thing)
# else:
#     no_such_thing()

# contoh :

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        print(n, 'adalah bilangan prima')
