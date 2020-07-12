f=open("whitepages.txt",'rb')
s = f.read()
f.close()
f=open("reversed","wb")
f.write(s)
f.close()

for data in s:
    print(data,end="")

