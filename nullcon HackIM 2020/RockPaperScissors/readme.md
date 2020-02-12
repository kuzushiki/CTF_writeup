# RockPaperScissors

じゃんけんをして20連勝すればいい


3^20分の1を当てるのはスマートでは無い

相手はコミットメントを生成し、勝負の前に表示してくれるので、コミットメントから出す手を推測できれば勝ちである

コミットメントは以下のように作られる（AESっぽい感じ）

```
sbox = [221, 229, 120, 8, 119, 143, 33, 79, 22, 93, 239, 118, 130, 12, 63, 207, 90, 240, 199, 20, 181, 4, 139, 98, 78, 32, 94, 108, 100, 223, 1, 173, 220, 238, 217, 152, 62, 121, 117, 132, 2, 55, 125, 6, 34, 201, 254, 0, 228, 48, 250, 193, 147, 248, 89, 127, 174, 210, 57, 38, 216, 225, 43, 15, 142, 66, 70, 177, 237, 169, 67, 192, 30, 236, 131, 158, 136, 159, 9, 148, 103, 179, 141, 11, 46, 234, 36, 18, 191, 52, 231, 23, 88, 145, 101, 17, 74, 44, 122, 75, 235, 175, 54, 40, 27, 109, 73, 202, 129, 215, 83, 186, 7, 163, 29, 115, 243, 13, 105, 184, 68, 124, 189, 39, 140, 138, 165, 219, 161, 150, 59, 233, 208, 226, 176, 144, 113, 146, 19, 224, 111, 126, 222, 178, 47, 252, 99, 87, 134, 249, 69, 198, 164, 203, 194, 170, 26, 137, 204, 157, 180, 168, 162, 56, 81, 253, 213, 45, 21, 58, 24, 171, 37, 82, 53, 50, 84, 196, 232, 242, 244, 64, 80, 10, 114, 212, 187, 205, 28, 51, 182, 16, 107, 245, 211, 85, 92, 195, 5, 197, 200, 31, 183, 61, 123, 86, 167, 154, 41, 151, 35, 247, 246, 153, 95, 206, 149, 76, 112, 71, 230, 106, 188, 172, 241, 72, 156, 49, 14, 214, 155, 110, 102, 116, 128, 160, 135, 104, 77, 91, 190, 60, 42, 185, 96, 97, 251, 218, 133, 209, 65, 227, 3, 166, 255, 25]
p = [5, 9, 1, 8, 3, 11, 0, 12, 7, 4, 14, 13, 10, 15, 6, 2]
round = 16

def gen_commitments():
    secret = bytearray(Random.get_random_bytes(16))
    rc = hash(secret + b"r")
    pc = hash(secret + b"p")
    sc = hash(secret + b"s")
    secret = hex(bytes_to_int(secret))[2:]
    rps = [("r", rc), ("p", pc), ("s", sc)]
    print(rps)
    random.shuffle(rps)
    return secret, rps

def hash(data):
    state = bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])
    data = pad(data, 16)
    print(data)
    data = group(data)
    print(data)
    for roundkey in data:
        print("roundkey", roundkey)
        for _ in range(round):
            state = repeated_xor(state, roundkey)
            for i in range(len(state)):
                state[i] = sbox[state[i]]
            temp = bytearray(16)
            for i in range(len(state)):
                temp[p[i]] = state[i]
            state = temp
        print("state", state)
    return hex(bytes_to_int(state))[2:]
```

概要をざっくり説明すると、`gen_commitments`では`secret`をまず生成し、それにそれぞれの手を足したものを`hash`に投げている

`hash`では入力をパディングし、分割し、パーツごとにXOR, 置換などのAESっぽい処理をする

例えばパーの場合は`b'/\xdcF\xcd1x\xa9\x02%\x12\xba\x81\x17\xff$^`と
`b'p\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'`に分けられる

2つ目のパーツの先頭1バイトが`p,r,c`のいづれかになることを利用する

`hash`には乱数を使った処理が無いので、逆算が可能である

得られるコミットメントにたいして`hash`と逆の処理を施してあげれば、元の入力を求められるはずである

以下のような関数を作る

```
def dec_hash(old_state_list):
    roundkey_list = [bytearray(b'r\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
        bytearray(b'p\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
        bytearray(b's\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f')
        ]

    total_state_list = []
    for old_state in old_state_list:
        new_state_list = []
        for roundkey in roundkey_list:
            state = int_to_bytes(old_state)
            temp = [0] * len(state)
            for i in range(len(state)):
                temp[i]  = state[p[i]]
            for i in range(len(state)):
                temp[i] = sbox.index(temp[i])
            new_state = repeated_xor(temp, roundkey)
            new_state_list.append(new_state[0])
        total_state_list.append(new_state_list)
    return total_state_list
```

復号結果は以下のようになる

```
[
    [bytearray(b'#\xb6\xcb\xa6\x850!\xedr\x15\x1c>\x89\xe7Ch'), 
    bytearray(b'!\xb6\xcb\xa6\x850!\xedr\x15\x1c>\x89\xe7Ch'), 
    bytearray(b'"\xb6\xcb\xa6\x850!\xedr\x15\x1c>\x89\xe7Ch')],

    [bytearray(b' W\x05\xa4\xdc\xfa\xdf\xe6\x90dJM\xb2\x10Et'), 
    bytearray(b'"W\x05\xa4\xdc\xfa\xdf\xe6\x90dJM\xb2\x10Et'), 
    bytearray(b'!W\x05\xa4\xdc\xfa\xdf\xe6\x90dJM\xb2\x10Et')], 

    [bytearray(b'"8\xa1\x9f\n\xe4\xbfu\xf26\xd7\xdd\xf6\x816\xf0'), 
    bytearray(b' 8\xa1\x9f\n\xe4\xbfu\xf26\xd7\xdd\xf6\x816\xf0'), 
    bytearray(b'#8\xa1\x9f\n\xe4\xbfu\xf26\xd7\xdd\xf6\x816\xf0')]]
```

３つのコミットメントを`r,p,c`のそれぞれで復号してみたもの

すると復号結果の1バイト目が一致することが分かる（上の例では`b'"'`）

これが一致しているものが正解である

上の例では上からチョキ、グー、パーとなる

（なぜ1バイト目しか一致しないのかは分かりませんでした）

後はコミットメントを読み取り、復号し、出す手を決めて送るプログラムをつくる

```
from pwn import *
import time

from Crypto import Random
from Crypto.Random import random
from Crypto.Util.number import *

sbox = [221, 229, 120, 8, 119, 143, 33, 79, 22, 93, 239, 118, 130, 12, 63, 207, 90, 240, 199, 20, 181, 4, 139, 98, 78, 32, 94, 108, 100, 223, 1, 173, 220, 238, 217, 152, 62, 121, 117, 132, 2, 55, 125, 6, 34, 201, 254, 0, 228, 48, 250, 193, 147, 248, 89, 127, 174, 210, 57, 38, 216, 225, 43, 15, 142, 66, 70, 177, 237, 169, 67, 192, 30, 236, 131, 158, 136, 159, 9, 148, 103, 179, 141, 11, 46, 234, 36, 18, 191, 52, 231, 23, 88, 145, 101, 17, 74, 44, 122, 75, 235, 175, 54, 40, 27, 109, 73, 202, 129, 215, 83, 186, 7, 163, 29, 115, 243, 13, 105, 184, 68, 124, 189, 39, 140, 138, 165, 219, 161, 150, 59, 233, 208, 226, 176, 144, 113, 146, 19, 224, 111, 126, 222, 178, 47, 252, 99, 87, 134, 249, 69, 198, 164, 203, 194, 170, 26, 137, 204, 157, 180, 168, 162, 56, 81, 253, 213, 45, 21, 58, 24, 171, 37, 82, 53, 50, 84, 196, 232, 242, 244, 64, 80, 10, 114, 212, 187, 205, 28, 51, 182, 16, 107, 245, 211, 85, 92, 195, 5, 197, 200, 31, 183, 61, 123, 86, 167, 154, 41, 151, 35, 247, 246, 153, 95, 206, 149, 76, 112, 71, 230, 106, 188, 172, 241, 72, 156, 49, 14, 214, 155, 110, 102, 116, 128, 160, 135, 104, 77, 91, 190, 60, 42, 185, 96, 97, 251, 218, 133, 209, 65, 227, 3, 166, 255, 25]
p = [5, 9, 1, 8, 3, 11, 0, 12, 7, 4, 14, 13, 10, 15, 6, 2]
round = 16


def pad(data, size = 16):
    pad_byte = (size - len(data) % size) % size
    data = data + bytearray([pad_byte]) * pad_byte
    return data


def repeated_xor(p, k):
    return bytearray([p[i] ^ k[i % len(k)] for i in range(len(p))])


def bytes_to_int(xbytes):
    return bytes_to_long(xbytes)


def int_to_bytes(x):
    return long_to_bytes(x, 16)


def group(input, size = 16):
    return [input[i * size: (i + 1) * size] for i in range(len(input) // size)]

def dec_hash(old_state_list):
    roundkey_list = [bytearray(b'r\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
        bytearray(b'p\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
        bytearray(b's\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f')
        ]

    total_state_list = []
    for old_state in old_state_list:
        new_state_list = []
        for roundkey in roundkey_list:
            state = int_to_bytes(old_state)
            temp = [0] * len(state)
            for i in range(len(state)):
                temp[i]  = state[p[i]]
            for i in range(len(state)):
                temp[i] = sbox.index(temp[i])
            new_state = repeated_xor(temp, roundkey)
            new_state_list.append(new_state[0])
        total_state_list.append(new_state_list)
    return total_state_list

def my_hand(total_state_list):
    s1, s2, s3 = map(lambda state: set(state), total_state_list)
    dup = s1 & s2 & s3
    dup = list(dup)[0]
    if total_state_list[0].index(dup) == 0:
        return b'p'
    elif total_state_list[0].index(dup) == 1:
        return b's'
    elif total_state_list[0].index(dup) == 2:
        return b'r'

io = remote('crypto1.ctf.nullcon.net', 5000)
recv_data = io.recv(1024)
for i in range(20):
    state_list = [recv_data.split(b' ')[-4], recv_data.split(b' ')[-3], recv_data.split(b' ')[-2][:-5]]
    # print(state_list)
    dec_list = dec_hash(list(map(lambda s: int(s, 16), state_list)))
    print(my_hand(dec_list))
    io.sendline(my_hand(dec_list))
    recv_data = io.recv(1024)
    print(recv_data)

io.interactive()
```

フラグゲット
`hackim20{b4d_pr1mitiv3_beats_all!1!_7f65}`