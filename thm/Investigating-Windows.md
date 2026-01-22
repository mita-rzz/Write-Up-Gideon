
# Investigating Windows
 
#### 1. Whats the version and year of the windows machine?
Ans: pertama tama perlu untuk membuka "run" di mesin yang disediakan. lalu mengetik 'winver' lalu mengklik enter. dapat diketahui mesin yang digunakan adalah **Windows Server 2016**.

#### 2.Which user logged in last?
Ans: untuk menjawabnya pertama perlu mengetahui user nya siapa aja dengan menggunakan command 

```bash
    net user 
```

Setelah di jalankan maka akan nampak user yang ada yaitu akun administrator default account dan lainnya. Lalu mengecek kapan terakhir login dengan menggunakan:

```bash
    net user <username>
```
lalu kita coba satu persatu ke username yang ada. dan diketahui user terakhir adalah **administrator**.

#### 3.  When did John log onto the system last?
Ans: Untuk menjawab nya menggunakan command 
```bash
    net user John
```
Setelah dijalankan maka akan langsung menampilkan informasi tentang user john salah satu nya adalah kapan john terakhir log on yaitu pada **03/02/2019 5:48:32 PM**

#### 4. What IP does the system connect to when it first starts?
Ans: IP yang pertama kali muncul ini ada di CMD saat awal memulai mesin yaitu 10.34.2.3

#### 5. What two accounts had administrative privileges (other than the Administrator user)? 
Ans: Untuk mengetahui akun yang memiliki hak administrative  dapat dilakukan dengan menggunakan command:
```bash
    net localgroup administrators
```
maka akan langsung di tampilkan akun yang memiliki hak administrative yaitu Guest dan  Jenny.

