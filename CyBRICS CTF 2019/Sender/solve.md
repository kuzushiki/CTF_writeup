txtファイルを見るといくつか特殊なエンコードの文字列があるのでデコード

 - `VXNlcm5hbWU6ZmF3a2Vz`, `UGFzc3dvcmQ6Q29tYmluNHQxb25YWFk=`はbase64，

 - `=62=74=77=2E=0A=0A=70=61=73=73=77=6F=72=64 ...`はQuoted Printable

 - それぞれユーザ名・パスワード，アーカイブのパスワードが得られる

 - txtファイルのやりとりは以下の流れ

  1. fawkes@ugm.cybrics.netに接続

  1. fawkesがarea51に何かのデータをメールで送る

  1. fawkesが「add - archive pw」という件名で再度area51にメールを送る

- 先程得られたユーザ名・パスワードでこちらもfawkes@ugm.cybrics.netに接続し，送信メールを確認できれば良さそう

- 念の為ポートスキャンしとく`nmap ugm.cybrics.net`

- pop3が空いているので接続 `nc ugm.cybrics.net 110`

  - Dovecotというサーバにつながる

- 先程得られたユーザ名・パスワードで認証が通る

```
user wakes
pass Combin4t1onXXY
```

- `list`コマンドでメールのリストを確認すると，1というメールがある

- `RETR 1`でメールの中身を見ると大量のbase64でエンコードされた文字列が

- `secret_flag.zip`というファイル名らしいのでデコードしてからzip形式で保存

- 開くとパスワードが聞かれるので先程使わなかった方を入力し解除

- フラグゲット:`cybrics{Y0uV3_G0T_m41L}`
