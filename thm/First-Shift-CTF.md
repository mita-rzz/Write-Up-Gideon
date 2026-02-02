# First Shift CTF
## Task 3
### Challenge Description
Pada task ini terdapat peringatan pada dashboard SOC yaitu adanya login vpn yang tidak wajar dari email susan.martin@probablyfine.thm  dengan IP 37.19.201.132  dari singapore.  Ternyata Susan pernah menginstall "security check" pada saat menggunakan wifi public. Ternyata setelah di hash didapat b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630.
Question:
#### 1. What is the ASN number related to the IP?
Ans: 
Autonomous System Number (ASN) adalah angka unik 16-bit atau 32-bit yang mengidentifikasi jaringan besar, ISP, atau organisasi di internet secara global, memungkinkan mereka bertukar informasi perutean (routing) menggunakan protokol BGP. ASN dapat ditemukan dengan :
1. Masuk ke URL TryDetectThis
2. Memasukkan alamat ip dari vpn login ke tab pencarian 
3. Nomor ASN dapat dilihat pada IP Overview  yaitu **212238**
   
   <img width="1857" height="941" alt="image" src="https://github.com/user-attachments/assets/2c8bb235-dfe6-4f21-9630-16497cfd2f46" />

#### 2. Which service is offered from this IP? 
Ans: 
Karena IP ini digunakan dalam koneksi melalui VPN maka servis yang ditawarkan oleh IP ini juga adalah **VPN**

#### 3. What is the filename of the file related to the hash?
Ans:
Untuk mengetahui nama file yang related dengan hash tersebut dapat dilakukan dengan:

1. Masuk ke URL TryDetectThis
2. Memasukkan HASH dari "security check"  
3. Melihat pada file detail lalu ke bagian File name
Dari file name tersebut ditemukan jawaban nya yaitu **zY9sqWs.exe**

<img width="1836" height="883" alt="image" src="https://github.com/user-attachments/assets/bbd2ed72-e62b-490d-8539-9b529d2710fc" />


#### 4. What is the threat signature that Microsoft assigned to the file?
Ans:
Threat signature adalah pola, pengidentifikasi unik, atau karakteristik khusus yang terkait dengan aktivitas berbahaya, seperti malware, serangan siber, atau intrusi. Threat signature berbeda beda tergantung vendor yang menganalisis nya. untuk mengetahui threat signature dari microsoft dapat dilihat pada bagian vendor Analysis lalu mencari pada bagian Micorsoft. Menurut microsoft threat signature nya adalah **Trojan:Win32/LummaStealer.PM!MTB**

<img width="1806" height="912" alt="image" src="https://github.com/user-attachments/assets/b015b1cc-e148-46e4-912b-70ecba54ccb7" />

#### 5.  One of the contacted domains is part of a large malicious infrastructure cluster.Based on its HTTPS certificate, how many domains are linked to the same campaign?
Ans:
Untuk mengetahui sebuah domain itu bagian dari large malicious infrastructure cluster dapat dilakukan dengan mengecek nya satu persatu. pada kolom detection terdapat beberapa nilai yaitu nilai dari berapa antivirus yang menyatakan domain ini berbahaya. Jadi pengecekan dapat dimulai dulu dari domain yang di anggap mencurigakan oleh antivirus tersebut terlebih dahulu.
Untuk melakukan pengecekan dapat dilakukan dengan :

1. Menyalin id  domain yang di inginkan
2. melakukan pencarian di TryDetectThis menggunakan id domain tersebut.
3. Melihat pada tabel HTTPS Certificate Data.
 
 gadgethgfub.icu di nyatakan sebagai   large malicious infrastructure cluster karena nama yang tidak biasa untuk domain, menggunakan ekstensi domain yang murah (biasanya digunakan hacker) dan memiliki banyak domain yang terhubung dengan domain tersebut. pada HTTPS certificate terdapat **151** domain yang terhubung dengan domain tersebut.

#### 6. The file matches one of the YARA rules made by "kevoreilly". What line is present in the rule's "condition" field?
Ans:  
