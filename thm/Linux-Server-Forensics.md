
# Linux Server Forensics 

- Task 5 :
    Pada task ini akan diminta untuk mencari password yang digunakan oleh penyusup untuk login. Pencarian dilakukan dengan mengecek pada folder /etc/passwd dan ditemukan hash dari password yang digunakan oleh penyusup nya. karena password nya dalam bentuk hash maka perlu di ubah jadi teks dengan brute fore menggunakan hashcat dengan code:
    ```bash
  hashcat -m 1500 -a 3 hai.txt --force
    ``` 
    untuk melakukan bruteforce dari aaaaaaaa - zzzzzzzz. setelah itu ditemukan bahwa passwordnya adalah mrcake

  
     

