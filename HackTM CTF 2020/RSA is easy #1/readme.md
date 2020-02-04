RSA問

`c`というファイルにて、
`e`および`n`の値と、大量の暗号文が与えられる

`rsa.py`はRSA暗号のソースコード。

`enc`という関数を見てみる

```rsa.py
def enc(key, p):
    e, n = key
    cipher = [pow(ord(char), e, n) for char in p]
    return cipher
```

フラグ文字列全体ではなく、1文字ずつを暗号化していることが分かる。

平文の候補は`0~9, a~z, A~Z +いくつかの記号`に限られるので、総当たりが可能

`Python`であれば`stirng.printable()`で`0123456789abc...`のような総当たりに使える文字列が得られる

総当たり攻撃を行うスクリプトを書く
`solve.py`

フラグゲット
`HackTM{why_ar3_MY_pR1va7es_pu8l1C_??}`