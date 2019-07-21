アセンブラらしきコードが確認できる:`oldman.asm`

- 形式を見た感じ，pdp-11に似てたのでwikiを参考する:<https://ja.wikipedia.org/wiki/PDP-11>

- 意味を推測し逆アセンブル

  - `#0d, #32d, #1d, #0, #33d`はただの数字

  - `r1 ~ r3`は変数

  - `mov #MSG r1`は`r1`を文字列のポインタにするという意味
  
    - 例えば`r1+1`は#MSGの２番目の文字になる

  - ややこしいのが以下の３行

```
swab r2
clrb r2
swab r2
```
 
  - `swab`は8bitローテーション，`clrb`は（おそらく）下位8bitをクリア

  - よって上位8bitをクリアするという意味になる

  - 逆アセンブルの結果:`oldman.py`

  - プログラムを実行してフラグゲット:`cybrics{pdp_gpg_crc_dtd_bkb_php}`
