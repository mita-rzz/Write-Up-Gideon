import math

if __name__ == "__main__":
    awal=int(input("masukkan awal"))
    d ='label'
    # s=biner(awal)
    for i in d:
        a=int(ord(i))
        ns=a^awal
        # nx=binaryToDecimal(ns)
        print(chr(ns), end='')


