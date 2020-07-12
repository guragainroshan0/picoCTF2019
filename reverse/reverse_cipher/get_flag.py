f = open("rev_this")
a= f.read()
res =[]
a = [ ro for ro in a ]
for i in range(8,23):
    if i & 1 == 0:
        res.append(chr(ord(a[i])-5))
    else:
        res.append(chr(ord(a[i])+2))

print(''.join(res))

