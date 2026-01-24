from pwn import xor

awal = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
mid = bytes.fromhex(awal)
for i in range(256):
    try:
        a = xor(mid, i)
        
        teks = a.decode('ascii') 
        
        print(teks)
            
    except:
        pass 
