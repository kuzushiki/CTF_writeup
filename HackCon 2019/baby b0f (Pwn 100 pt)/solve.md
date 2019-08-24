# ポイント

- バッファオーバーフロー（以下BOF）

## 解く

プログラムを実行するといきなり入力を求められる

- 間違った入力をすると`Try Again`と表示される

デバッガで逆アセンブルしつつ実行

![image](https://user-images.githubusercontent.com/50363796/63631108-aab8b280-c65d-11e9-9de6-03d1556c2fa0.PNG)

どうやらこの比較命令が怪しい

```
RIP: 0x400760 (<main+153>:	cmp    DWORD PTR [rbp-0x4],0xdeadbeef)
```

BOFしてここを一致させることを考える

以下のコマンドでrsp,rbpを表示

```
x/32xw $rsp
x/32xw $rbp
```
以下の行に注目

```
0x7fffffffdeb0:	0x4141dfa0	0x000a4141	0x00000000	0xcafebabe
```

今回は`AAAA`と入力したが，その入力値が確認できる(`A`は`0x41`に相当)

さらに，`0xcafebabe`は`[rbp-0x4]`であることも分かる

つまり，`0xcafebabe`の部分を`0xdeadbeef`にできれば良い

ペイロードを作ってサーバに投げる[プログラム](solve.py)を作って実行

フラグゲット

## 補足

- 実は初めて解いたPwn問だったりする

- Pwntoolsを使用してます
  
  - [参考資料](https://hiziriai.hatenablog.com/entry/2017/09/18/124628)
