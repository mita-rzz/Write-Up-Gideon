from pwn import xor
#  I've encrypted the flag with my secret key, you'll never be able to guess it. 
# Remember the flag format and how it might help you in this challenge!
awal='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# diatas adalah hex yang diberikan
awal_a=bytes.fromhex(awal) # kode ini merubah format yang awalnya hex menjadi bytes
#karena hint yang diberikan maka hasil dari enkripsi nya harusnya crypto{....} ==> yang berasal dari format jawaban yang sebelumnya
#karena ... tidak diketahui maka key nya dapat diperoleh dari crypto{ xor huruf ke 1-7 di variabel awal_a 
hasil=b'crypto{' 
hah=awal_a[:len(hasil)]
key=xor(hah,hasil)
print(key) #hasilnya adalah myXORke , akan tetapi jika key ini dipakai maka tidak ada jawaban yang didapat. 
# oleh karena itu dengan menebak dari kata kata yang mungkin myXORke ==> myXORkey 
# key + 'y'
key+=b'y'
print(xor(awal_a,key)) # b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
