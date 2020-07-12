a=[  106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
                    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
                                0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o142, 0o71 ,
                                
                                            'e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c' ]


for data in a:
    try:
        print(chr(data),end="")
    except:
        print(data,end="")
"""
for data in a[8:16]:
    print("**",int(str(data),16),"**",data)
    print(chr(int(str(data),16)),"HEX")#,end="")
for data in a[16:24]:
    print(chr(int(str(data),8)),end="")

for data in a[24:32]:
    print(data,end="")
"""
