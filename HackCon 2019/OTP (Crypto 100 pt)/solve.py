c1 = b'\x05F\x17\x12\x14\x18\x01\x0c\x0b4'.hex()
c2 = b'>\x1f\x00\x14\n\x08\x07Q\n\x0e'.hex()


def convert_cipher(cipher):
    l_cipher = list(cipher)
    L = len(l_cipher)
    h_cipher = []
    for i in range(L // 2):
        tmp = l_cipher[i * 2: i * 2 + 2]
        tmp = "0x" + "".join(tmp)
        h_cipher.append(tmp)
    print(h_cipher)
    return h_cipher


h_c1 = convert_cipher(c1)
h_c2 = convert_cipher(c2)

dec = [0] * 10

dec[0] = chr(ord('d') ^ int(h_c2[0], 16) ^ int(h_c1[0], 16))
dec[1] = chr(ord('4') ^ int(h_c2[1], 16) ^ int(h_c1[1], 16))
dec[2] = chr(ord('r') ^ int(h_c2[2], 16) ^ int(h_c1[2], 16))
dec[3] = chr(ord('k') ^ int(h_c2[3], 16) ^ int(h_c1[3], 16))
dec[4] = chr(ord('{') ^ int(h_c2[4], 16) ^ int(h_c1[4], 16))
dec[5] = chr(ord('}') ^ int(h_c2[5], 16) ^ int(h_c1[5], 16))
dec[6] = chr(ord('c') ^ int(h_c2[6], 16) ^ int(h_c1[6], 16))
dec[7] = chr(ord('0') ^ int(h_c2[7], 16) ^ int(h_c1[7], 16))
dec[8] = chr(ord('d') ^ int(h_c2[8], 16) ^ int(h_c1[8], 16))
dec[9] = chr(ord('e') ^ int(h_c2[9], 16) ^ int(h_c1[9], 16))

m1 = "d4rk{"
for i in range(5):
    m1 += dec[i + 5]

m2 = ""
for i in range(5):
    m2 += dec[i]
m2 += "}c0de"

print(m1 + m2)
