# Zelda3

先ほどと同じゲームにフラグが隠されている

今回はゲームエリアの端っこに行くのが目的

また`dnSpy`というソフトを使って解析する

先ほどのチートで障害物をすり抜けることはできたので、今度は移動スピードを上げることを考える

移動スピードは以下のメソッドで計算される

```
private void MoveCharacter()
{
	this.change.Normalize();
	this.myRigidbody.MovePosition(base.transform.position + this.change * this.speed * Time.deltaTime);
}
```

`this.change * this.speed * Time.deltaTime`が移動量を表している（速さx時間）

ここで、以下のように変更してみる

```
private void MoveCharacter()
{
	this.change.Normalize();
	this.myRigidbody.MovePosition(base.transform.position + this.change);
}
```

ゲームを実行してみる

某漫画にでてくる瞬歩みたいな挙動になる（おそらく`this.speed * Time.deltaTime`が１以下の小さな値になるため）

池があるエリアの右上からジャングルに入る

さらに右上に進むとフラグがある

`EXPLORERFORLIFE`