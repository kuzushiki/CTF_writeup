# Zelda1

Unity製のゼルダっぽいゲームが配布される

敵を倒すのが目的だが、敵に接触してもお互いノックバックするだけ

スペースキーで剣を振れるが、当てても接触したときと同じ

`dnSpy`というソフトを使って解析する

Unity製のゲームはC#で書かれており、
そのソースコードは`Managed/Assembly-CSharp.dll`を解析することで確認できる。

敵を倒すアプローチは、こちらの攻撃力を上げる方法と敵のHPをゼロにする方法などが考えられるが、
今回は後者のチートを試みる。

敵のHPに関係しそうなメソッドを見てみる

`Enemy`クラスに`TakeDamage`という関数がある
```
private void TakeDamage(float damage)
{
	this.health -= damage;
	if (this.health <= 0f)
	{
		base.StartCoroutine(this.ShowSome());
		base.gameObject.SetActive(false);
	}
}
```

どうやら`this.health <= 0f`を`true`にすれば倒せそうだ

というわけで判定文を以下のようにいじる

```
private void TakeDamage(float damage)
{
	this.health -= damage;
	if (this.health <= 999999f)
	{
		base.StartCoroutine(this.ShowSome());
		base.gameObject.SetActive(false);
	}
}
```

ゲームを実行してみる

敵に接触した瞬間に敵が消え、画面上部にフラグが現れる

`Flag: REVOLUTIONSTARTSWITHME`