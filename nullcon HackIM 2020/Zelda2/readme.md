# Zelda2

先ほどと同じゲームにフラグが隠されている

今回は通常は入れない池の中に侵入するのが目的

また`dnSpy`というソフトを使って解析する

どこを変更すればいいか分からなかったので「Unity 障害物 すり抜け」などのキーワードでググる

どうやら`Dynamic`ではなく`Kinematic`という設定にすれば良いらしい

`kinematic`で検索すると`isKinematic`というメソッドが見つかる

(検索オプションの`Match Any Search Item`にチェックを入れること！)

```
public bool isKinematic
		{
			get
			{
				return this.bodyType == RigidbodyType2D.Kinematic;
			}
			set
			{
				this.bodyType = ((!value) ? RigidbodyType2D.Dynamic : RigidbodyType2D.Kinematic);
			}
		}
```

`Kinematic`にするかどうかを決めているらしい

常時`Kinematic`にするために、`set`を変更する

```
public bool isKinematic
		{
			get
			{
				return this.bodyType == RigidbodyType2D.Kinematic;
			}
			set
			{
				this.bodyType = RigidbodyType2D.Kinematic;
			}
		}
```

ゲームを実行してみる

池に入ると、フラグが書かれたエリアにワープする

`FLAG IS BENDTHERULES42PIRATE`