# Lab-08

```text
“VMW” を index で指定して “VMware” を取り出すのではなく、”Google” を取り出すように変更してみましょう。
Index の最大値以上の index を指定して出力の違いを確認してみましょう。
リストに新たに “Apple” を追加してみましょう。

（Optional）Lab-7 の例を利用して、dict を for 文でループさせてみましょう。
```

- Lab-08 では Python で利用可能なデータ型である `list` 型(リスト型)を扱ってみましょう
  - list 型のデータは、同一のデータ型のデータを一つのデータに格納することができます
    - 異なるデータ型のデータを格納することも技術的には可能ですが、このような使い方は可読性や保守性の観点から、基本的には避けるべきであるとされています
  - list 型データは、dict 型のように Key-Value の形式ではないため、代わりに `index` を利用して、まとめたデータ(`要素`)にアクセスします

- list 型は `for ... in ...` の制御構文(=繰り返し)と密接な関係があります
  - 繰り返し処理を行いたいデータを list 型の変数にまとめておき、それぞれの要素に同じ処理を行う

- 以下のように、list 型のデータに対して、データを格納して、値を参照することができます

```python
# list 型のデータを定義、出力する
# (4つの文字列型のデータを list 型のデータにまとめる)
companies = ["Amazon", "Google", "Microsoft", "VMware"]
print(companies)

# index を指定して、格納したデータにアクセスする
print(companies[3])

# list 型に格納したそれぞれのデータに対して、print() 処理を行う
for c in companies:
    print(f"Name: {c}")
```

***

- 実行結果(例)

```bash
# list 型データを扱ってみる
(venv) 2021/09/21_04:18:33 Lab-08 % python lab_08.py 
['Amazon', 'Google', 'Microsoft', 'VMware']

Google

['Amazon', 'Google', 'Microsoft', 'VMware', 'Apple']
Name: Amazon
Name: Google
Name: Microsoft
Name: VMware
Name: Apple

# Optional: list 型ではなく dict 型のデータをループさせてみる
(venv) 2021/09/21_04:19:01 Lab-08 % python lab_08_option.py 
VMW
GOOG
AAPL
AMZN
MSFT
```
