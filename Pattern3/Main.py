baris = 10
b = 0
for i in range(baris, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ') # tampilkan nomor
    # baris demi baris untuk menampilkan pola dengan benar
    print('\r')
				 
	 
