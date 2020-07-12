#import binascii
from string import printable as ascii_printable
from pwn import *
conn = remote('2019shell1.picoctf.com',31615)
while True:
    a= conn.recv().decode()
    print(a.split("the ")[1])
    data = a.split("the ")[1]
    #print(data)
    numbers=data.split(" as")[0]
    bases = numbers.split(" ")
    #print(bases)
    out = []
    comb = [2,8,16,64]
    for com in comb:
        out = []
        for number in bases:
            try:
                r = chr(int(number.strip(),com))
                if r not in ascii_printable:
                    break
                out.append(r)
            except:
                break
            print(r)
        break
    data_to_send = ''.join(out) #+ '\r\n'
    print(data_to_send)
    conn.sendline(data_to_send.encode())
    
#for line in a:
    #print(line)
