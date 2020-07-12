a = "jU5t_a_sna_3lpm13g34c_u_4_m3rf48"
chars = [ro for ro in a]
data=['r']*32
for i in range(0,8):
    data[i]=chars[i]
for i in range(8,16):
    data[23-i]=chars[i]

for i in range(16,32,2):
    data[46-i]=chars[i]
for i in range(31,16,-2):
    data[i]=chars[i]
print(''.join(data))

